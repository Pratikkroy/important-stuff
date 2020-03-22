from django.utils.decorators import decorator_from_middleware_with_args
from custom_middlewares.validator import RequestBodyValidatorMiddleware

def request_body_validator(json_schema):
    def decorator_func(func):
        params_validator = decorator_from_middleware_with_args(RequestBodyValidatorMiddleware)
        @params_validator(json_schema)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator_func