"""
    This File Include Small
    Example Of Singleton Pattern
    --------------------------
    @pattern Singleton
    @author sina
"""

# Simple Class to Show This pattern
class SingletonObject(object):
    class __SingletonObject():

        # Initialize
        def __init__(self):
            self.value = 'Hello World'

        def __str__(self):
            return self.value

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            instance = SingletonObject.__SingletonObject()

        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
