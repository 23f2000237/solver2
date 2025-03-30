import json

request_body = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': 'Respond in JSON'},
        {'role': 'user', 'content': 'Generate 10 random addresses in the US'}
    ],
    'max_tokens': 150,
    'response_format': 'json'
}

# Response structure
response_structure = {
    'addresses': [],
    'additionalProperties': False
}

# Printing the request body and the expected response structure
print(json.dumps({'request_body': request_body, 'response_structure': response_structure}, indent=2))