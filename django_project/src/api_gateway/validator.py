import traceback
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from ..utils import HttpStatus, HttpResponse, ClassShouldNotInstantiateException

def encoder(data):
    if isinstance(data,int) or isinstance(data,str):
        return [data]
    return list(data)

class JSONSchemaValidator:

    def __init__(self, *args, **kwargs):
        raise ClassShouldNotInstantiateException
    
    @staticmethod
    def validate_json(json_schema, json_data):
        '''
        this method will return 
        status = 409 when the json_data is invalid against the provide json schema
        return None when all the required properties are present and valid
        '''
        try:
            validate(instance=json_data, schema=json_schema)
            return None
        except ValidationError as validation_error:
            # below commented lines are kept for testing purpose
            # print("ValidationError .... ",validation_error)
            # print("absolute_path", validation_error.absolute_path)
            # print("absolute_schema_path", validation_error.absolute_schema_path)
            # print("relative_path", validation_error.relative_path)
            # print("relative_schema_path", validation_error.relative_schema_path)
            # print("schema", validation_error.schema)
            # print("schema_path", validation_error.schema_path)
            # print("validator", validation_error.validator)
            # print("validator_value", validation_error.validator_value)
            # print("path", validation_error.path)

            try:
                return HttpResponse(
                    http_status=HttpStatus.HTTP_409_CONFLICT,
                    data={
                        'validationError': validation_error.validator,
                        'validationValue': encoder(validation_error.validator_value),
                        'absoluteSchemaPath': list(validation_error.absolute_schema_path),
                        'absolutePath': list(validation_error.absolute_path),                   
                    }
                )

            except Exception:
                traceback.print_exc()
                return HttpResponse(
                    http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR,
                    data='JSON_VALIDATION_ERROR'
                )