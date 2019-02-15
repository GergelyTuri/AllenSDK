class LazyProperty(object):
    
    def __init__(self, api_method, *args, **kwargs):

        self.api_method = api_method
        self.args = args
        self.kwargs = kwargs
        self.value = None

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.value is None:
            self.value = self.calculate()
        return self.value

    def __set__(self, obj, value):
        raise AttributeError("Can't set LazyLoadable attribute")

    def calculate(self):
        return self.api_method(*self.args, **self.kwargs)