class DotDict(dict):
    """
    A dictionary subclass that allows for attribute-like access to dictionary keys.

    This class is useful in unittest contexts where fixtures or test data need to be accessed in a more readable way.

    Examples:
        >>> dotdict = DotDict({'foo': 'bar'})
        >>> dotdict.foo
        'bar'
        >>> dotdict.baz = 'qux'
        >>> dotdict['baz']
        'qux'
        >>> del dotdict.foo
        >>> dotdict.get('foo')
        None
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
