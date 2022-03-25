import functools
import json

import cattr

from python_qa.utils.func import func_parameters_dic
from python_qa.utils.classes import is_attrs_class


class Decorators:
    @staticmethod
    def request_typing(response_type=None, error_type=None):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                f_args = func_parameters_dic(func, *args, **kwargs)  # ToDo: to realize
                data = f_args.get("data", None)
                if is_attrs_class(data):
                    data = cattr.unstructure(data)
                    f_args.pop("data")
                    f_args["json"] = json.dumps(data)
                    args = f_args.values()
                resp = func(*args, **kwargs)
                if response_type and resp.status_code // 100 == 2:
                    resp.typed = cattr.structure(resp.json(), response_type)
                elif error_type:
                    resp.typed = cattr.structure(resp.json(), error_type)
                return resp
            return wrapper
        return decorator


deco = Decorators
