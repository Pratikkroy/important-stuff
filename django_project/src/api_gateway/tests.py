from .validator import JSONSchemaValidator

# login body data
g_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Auth',
    'description': 'Data needed while login',
    'type': 'object',
    'properties': {
        'auth_id': {
            'oneOf':[
                        {'type': 'string',
                         'minLength': 6,
                         'maxLength': 20
                        },
                        {'type': 'string',
                        "minLength": 2,
                        "maxLength": 3
                        },
                        
                    ]
        },
        'password': {
            'type': 'string',
        },
        'name': {
            'type': 'object',
            'properties': {
                'firstname': {
                    'type': 'string'    
                },
                'lastname': {
                    'type': 'string'
                }
            },
        }
    },
    # 'oneOf': [
    #     {
    #         'required': ['auth_id']
    #     },
    #     {
    #         'required': ['password']
    #     }
    # ],
    # 'required': ['auth_id', 'password','name']
}

l_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Login',
    'description': 'Data needed while login',
    'type': 'object',
    'properties': {
        'email_address': {
            'type': 'string',
            'minLength': 1
        },
        'password': {
            'type': 'string',
            'minLength': 1
        }
    },
    'required': ['email_address', 'password']
}


def validator(schema, request):
    response = JSONSchemaValidator.validate_json(
        json_schema=schema, json_data=request.data)
    print(response)
    return response


class Request:

    def __init__(self, req):
        self.data = req


if __name__ == '__main__':

    l_request = {
        "auth_id": "rahul",
        "password": "a",
        "name":{
            "firstname":"Rahul"
        }
    }

    r = Request(l_request)
    s = g_schema
    validator(s, r)
    # import json
    # print(json.dumps(None))