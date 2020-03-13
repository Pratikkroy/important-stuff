# login body data
login_json_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Login',
    'description': 'Data needed while login',
    
    'definitions': {
        'email': {
            'type': 'string',
            'format': 'email',
        },
        'phone': {
            'type': 'string',
            'minLength': 10
        },
    },
    
    'type': 'object',
    'properties': {
        'password': {
            'type': 'string',
            'minLength': 6
        },
        'loginType': {
            "enum": ["email", "phone"]
        }
        
    },
    'required': ['password','loginType'],
    
    'if': {
        'properties': { 'loginType': { 'const': 'email' } }
    },
    'then': {
        'properties': { 
            'email': { "$ref": "#/definitions/email" },
        },
        'required': ['email'],
    },
    'else': {
        'properties': { 
            'phone': { "$ref": "#/definitions/phone" },
        },
        'required': ['phone'],
    },
    'oneOf': [
        { 'required': ['email'] },
        { 'required': ['phone'] }
    ], 
}

