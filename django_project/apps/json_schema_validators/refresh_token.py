# refresh_token body data
refresh_token_json_schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Login',
    'description': 'Data needed while refresh_token',
    
    'type': 'object',
    'properties': {
        'refresh_token': {
            'type': 'string',
        }   
    },
    'required': ['refresh_token']
}

