# login body data
json_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Login',
    'description': 'Data needed while login',
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'minLength': 1
        },
        'password': {
            'type': 'string',
            'minLength': 1
        }
    },
    'required': ['email', 'password']
}


