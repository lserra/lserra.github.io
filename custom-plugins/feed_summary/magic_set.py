import inspect

import six


def magic_set(obj):
    """Add a function/method to an object at runtime."""

    def decorator(func):
        is_class = isinstance(obj, six.class_types)
        try:
            args = inspect.getfullargspec(func).args
        except AttributeError:  # pragma: no cover
            args = inspect.getargspec(func)[0]

        if not args or args[0] not in ("self", "cls", "klass"):
            replacement = staticmethod(func) if is_class else func
        elif args[0] == "self":
            if is_class:
                replacement = func
            else:

                def replacement(*args, **kwargs):
                    return func(obj, *args, **kwargs)

                replacement.__name__ = getattr(func, "__name__", "replacement")
        else:
            if is_class:
                replacement = classmethod(func)
            else:

                def replacement(*args, **kwargs):
                    return func(obj.__class__, *args, **kwargs)

                replacement.__name__ = getattr(func, "__name__", "replacement")

        setattr(obj, func.__name__, replacement)
        return replacement

    return decorator

