# ft_filter.py

def ft_filter(func, iterable):
    """
    Custom implementation of the built-in filter function.
    Returns an iterator with elements that satisfy the given function.
    """
    return (word for word in iterable if func(word))
