# update_credentials body data
update_credentials_json_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'update_credentials',
    'description': 'Data needed while update_credentials',
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
    },
    'oneOf': [
            { 'required': ['email'] },
            { 'required': ['phone'] },
            { 'required': ['password'] },
        ], 
}


