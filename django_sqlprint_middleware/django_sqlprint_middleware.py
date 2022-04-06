# -*- coding: utf-8 -*-

from __future__ import print_function
try:
    from django.utils.deprecation import MiddlewareMixin as Parent
except ImportError:
    Parent = object

import textwrap

from django.conf import settings
from pygments import highlight, lexers, formatters
from pygments_pprint_sql import SqlFilter


class SqlPrintMiddleware(Parent):
    """Output the sql used in the view.
    """
    def process_response(self, request, response):
        """Output all the sql queries for the Django orm.
        """
        from django.db import connection
        should_run = getattr(settings, 'SQLPRINT_MIDDLEWARE', True)
        if not should_run:
            return response
        x_db_hits = getattr(settings, 'X_DB_HITS', True)
        runnable = settings.DEBUG or settings.TESTING
        max_queries = getattr(settings, 'SQLPRINT_MAX_QUERIES', 1200)
        min_queries = getattr(settings, 'SQLPRINT_MIN_QUERIES', 0)

        queries = connection.queries
        dbhits = len(queries)
        if runnable and x_db_hits:
            response['X-DB-hits'] = str(dbhits)

        if runnable:
            if dbhits > min_queries:
                self.print_queries(request, queries)

            if max_queries and dbhits > max_queries:
                raise RuntimeError(textwrap.dedent("""\
                    A single request caused {dbhits} db hits, which is more than
                    settings.SQLPRINT_MAX_QUERIES
                    """.format(dbhits=dbhits)))

        return response

    def print_queries(self, request, queries):
        """Output all the queries.
        """
        lexer = lexers.MySqlLexer()
        lexer.add_filter(SqlFilter())

        totsecs = 0.0
        for query in queries:
            print(query['time'], 'seconds used on:')
            totsecs += float(query['time'])
            print(highlight(query['sql'], lexer, formatters.TerminalFormatter()))

        print('Number of queries:', len(queries))
        print('Total time:', totsecs, 'seconds')
