from jsonschema import validate
from jsonschema.exceptions import ValidationError

from ..utils.status import Status


class JSONSchemaValidator:

    def __init__(self, *args, **kwargs):
        pass

    def validate_json(self, json_schema, json_data):
        '''
        this method will return 
        status = 400 when a required attribute from json_schema is not present in json_data
        status = 412 when a required attribute from json_schema is not satisfying any condition 
                defined in the properties key in json schema

        return None when all the required properties are present and valid
        '''
        try:
            validate(instance=json_data, schema=json_schema)
        except ValidationError as validation_error:

            # below commented lines are kept for testing purpose
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

                # one or many required properties are missing
                if validation_error.validator == 'required':

                    # when there is only one required properties
                    if len(validation_error.absolute_schema_path) == 1:
                        required_properties = json_schema.get('required')

                    # when there are more than one required properties
                    else:
                        schema_path, properties_list_index, properties_list_key = validation_error.absolute_schema_path
                        required_properties = json_schema.get(
                            schema_path)[properties_list_index].get(properties_list_key)

                    for properties in required_properties:
                        # check if this property is present in json data
                        if json_data.get(properties) is None:
                            status = Status()
                            response = status.HTTP_400_BAD_REQUEST
                            response.update({
                                'message': properties.upper()+'_REQUIRED'
                            })
                            return response

                # json_data does not match any of the given required properties
                elif validation_error.validator == 'oneOf':
                    status = Status()
                    response = status.HTTP_400_BAD_REQUEST
                    response.update({
                        'message': 'REQUEST_BODY_INVALID'
                    })
                    return response

                # required properties are present but properties are not valid
                else:
                    status = Status()
                    response = status.HTTP_412_PRECONDITION_FAILED
                    response.update({
                        'message': validation_error.path[0].upper()+'_INVALID'
                    })
                    return response

            except:
                status = Status()
                response = status.HTTP_400_BAD_REQUEST
                response.update({
                    'message': 'JSON_VALIDATION_ERROR'
                })
                return response
        return None
