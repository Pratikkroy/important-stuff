class Singleton(object):
  _instances = {}
  def __new__(cls, *args, **kwargs):
    if cls not in cls._instances:
        cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
    return cls._instances[cls]




'''
A wrong method of implementing singleton class in python
using __new__ is better because it is a static method.
__new__ runs before the class is accessed(instance created).

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    pass

'''