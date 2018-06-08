# -*- coding: utf-8 -*-

from collections import OrderedDict
import inspect

class DataSaver:
    """Save extra data associated with the values that need to be learned.

    Parameters
    ----------
    learner : Learner object
        The learner that needs to be wrapped.
    arg_picker : function
        Function that returns the argument that needs to be learned.

    Example
    -------
    Imagine we have a function that returns a dictionary
    of the form: `{'y': y, 'err_est': err_est}`.

    >>> _learner = Learner1D(f, bounds=(-1.0, 1.0))
    >>> learner = DataSaver(_learner, arg_picker=operator.itemgetter('y'))
    """

    def __init__(self, learner, arg_picker):
        self.learner = learner
        self.extra_data = OrderedDict()
        self.function = learner.function
        self.arg_picker = arg_picker
        
        forbidden = ['_tell', '__init__']

        methods = inspect.getmembers(type(self.learner), inspect.isfunction)
        for name, func in methods:
            attr = getattr(self.learner, name)
            if name not in forbidden:
                setattr(self, name, attr)

        properties = inspect.getmembers(type(self.learner),
            lambda o: isinstance(o, property))
        for name, func in properties:
            if name not in forbidden:
                prop = property(lambda self: getattr(
                    type(self.learner), name).fget(self.learner))
                setattr(type(self), name, prop)

    def _tell(self, x, result):
        y = self.arg_picker(result) if result is not None else None
        self.extra_data[x] = result
        self.learner._tell(x, y)
