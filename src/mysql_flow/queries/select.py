from mysql_flow.queries import wrap

_template1 = "SELECT {columns} FROM {table};"
_template2 = "SELECT DISTINCT {columns} FROM {table};"


def select_query(table, columns="*", distinct=False):

    if distinct:
        return _template2.format(columns=columns, table=table)
    return _template1.format(columns=columns, table=table)
