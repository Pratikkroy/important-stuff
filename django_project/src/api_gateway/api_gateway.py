from src.utils.status import Status
from .validator import JSONSchemaValidator

# task of api gateway :
# authentication (session and token based)
# authorization,
# validation of request header, body and query params and
# parse request data


class ApiGatewayService:

    def __init__(self, *args, **kwargs):
        self._validator = JSONSchemaValidator()

    def authorize_with_api_key(self, api_key):
        pass

    def validate_request_header(self, json_schema, header):
        pass

    def validate_request_body(self, json_schema, body):
        return self._validator.validate_json(json_schema, body)

    def validate_request_query_params(self, json_schema, query_params):
        pass

    def parse_request_data(self, parser):
        pass
