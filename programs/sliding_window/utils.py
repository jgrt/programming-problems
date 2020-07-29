class BaseError(Exception):
    def __init__(self, message, **ctx):
        super(BaseError, self).__init__(message)
        self.message = message
        self.ctx = ctx


class EmptyArrayError(BaseError):
    pass


class InvalidSizeError(BaseError):
    pass


class InvalidValueError(BaseError):
    pass


class SolutionNotFound(BaseError):
    pass
