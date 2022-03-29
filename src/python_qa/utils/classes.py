def is_attrs_class(cls):
    return getattr(cls, "__attrs_attrs__", None) is not None
