from mysql_flow.queries import wrap

_template1 = "INSERT INTO {table} ({columns}) VALUES ({values});"
_template2 = "INSERT INTO {table} VALUES ({values});"
_template3 = "INSERT INTO {table} ({columns}) VALUES {value_tuples};"
_template4 = "INSERT INTO {table} VALUES {value_tuples};"
_template5 = "INSERT INTO {tableB} SELECT * FROM {tableA};"


def append_query(tableA, tableB):
    return _template5.format(tableA=tableA, tableB=tableB)


def _with_columns(table, columns, values, single_query=True):
    if single_query:
        return _template1.format(table=table, columns=columns, values=values)
    return _template3.format(table=table, columns=columns, value_tuples=values)


def _without_columns(table, values, single_query=True):
    if single_query:
        return _template2.format(table=table, values=values)
    return _template4.format(table=table, value_tuples=values)


def insert_query(columns_specified=True, **kwargs):
    """
    :param columns_specified: if inserting into specified fields or not
    :param kwargs: table, columns(optional), values
    :return: a constructed inserting sql query
    """
    if columns_specified:
        return _with_columns(kwargs["table"], kwargs["columns"], kwargs["values"])
    else:
        return _without_columns(kwargs["table"], kwargs["values"])


def multipe_insert_query(if_specify_columns=True, **kwargs):
    """
    kwargs["rows"] could be a two dimensional array
    """
    rows = kwargs["rows"]
    values = ", ".join(
        ["({})".format(", ".join([wrap(ele) for ele in row])) for row in rows]
    )
    if if_specify_columns:
        return _with_columns(
            kwargs["table"], kwargs["columns"], values, single_query=False
        )
    else:
        return _without_columns(kwargs["table"], values, single_query=False)
