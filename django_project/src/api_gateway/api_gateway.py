from src.utils import ClassShouldNotInstantiateException
from .validator import JSONSchemaValidator

# task of api gateway :
# authentication (session and token based)
# authorization,
# validation of request header, body and query params and
# parse request data


class ApiGatewayService:
    
    def __init__(self, *args, **kwargs):
        raise ClassShouldNotInstantiateException

    @staticmethod
    def authorize_with_api_key(self, api_key):
        pass

    @staticmethod
    def validate_request_header(self, json_schema, header):
        pass

    @staticmethod
    def validate_request_body(self, json_schema, body):
        return JSONSchemaValidator.validate_json(json_schema, body)

    @staticmethod
    def validate_request_query_params(self,json_schema, query_params):
        pass
    
    staticmethod
    def parse_request_data(self, parser):
        pass
