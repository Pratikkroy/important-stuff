# register body data
register_json_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Register',
    'description': 'Data needed while register',
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email'
        },
        'phone': {
            'type': 'string',
            'minLength': 10
        },
        'password': {
            'type': 'string',
            'minLength': 6
        },
        'isAdmin': {
            'type': 'boolean'
        },
        'name':{
            'type': 'object',
            'properties': {
                'first': {
                    'type': 'string',
                    'maxLength': 30
                },
                'last': {
                    'type': 'string'
                }
            },
            'required': ['first']
        }
    },
    'anyOf': [
            { 'required': ['email'] },
            { 'required': ['phone'] },
        ], 
    'required': ['password','isAdmin', 'name']
}


