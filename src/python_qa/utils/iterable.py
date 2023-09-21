from typing import Callable, List, Iterable


def filtered(func: Callable, iterable: Iterable):
    return type(iterable)(filter(func, iterable))


def select_items(items: List[dict], **kwargs) -> List:
    res = []
    if kwargs:
        for item in items:
            selected = True
            for k, v in kwargs.items():
                if item.get(k) != v:
                    selected = False
                    break
            if selected:
                res.append(item)
    return res


def select_item(items: List[dict], **kwargs) -> dict:
    res = select_items(items, kwargs)
    if res:
        return res[0]
    return {}
