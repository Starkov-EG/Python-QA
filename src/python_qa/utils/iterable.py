from typing import Callable, List, Iterable


def filtered(func: Callable, iterable: Iterable):
    return type(iterable)(filter(func, iterable))


def select_items(items: List[dict], inverse: bool = False, **kwargs) -> List:
    res = []
    if kwargs:
        for item in items:
            selected = True
            for k, v in kwargs.items():
                if (item.get(k) != v and not inverse) or (item.get(k) == v and inverse):
                    selected = False
                    break
            if selected:
                res.append(item)
    return res


def select_item(items: List[dict], inverse: bool = False, **kwargs) -> dict:
    res = select_items(items, inverse, kwargs)
    if res:
        return res[0]
    return {}
