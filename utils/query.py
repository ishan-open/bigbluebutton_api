from urllib.parse import quote
from ..exceptions.api_exception import DictMeta
from ..core.api_parameters import ApiParameters


def query_generator(query_dict: dict):
    if not isinstance(query_dict, dict):
        raise ValueError(f"query must be a dict, not {type(query_dict)}")

    query = ""
    for key, value in query_dict.items():
        if value is None:
            continue

        if isinstance(value, bool):
            value = "true" if value else "false"

        if key == ApiParameters.meta:
            if isinstance(value, dict):
                value = "".join([f"{x}={quote(y)}," for x, y in value.items()])
                query += f"meta_{key}={value}&"

            else:
                raise DictMeta

        else:
            query += f"{key}={quote(str(value))}&"

    return query
