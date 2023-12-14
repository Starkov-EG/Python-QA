class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def has_instance(cls):
        return cls._instance is not None

    @classmethod
    def get_instance(cls):
        return cls._instance

    @classmethod
    def remove_instance(cls):
        if cls._instance:
            del cls._instance
            cls._instance = None
