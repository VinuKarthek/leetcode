import json
import re
import boto3
from boto3.dynamodb.conditions import Key


class InvalidResponse(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


# Don't modify this function name and arguments
def query_user_notes(user_email):
    dynamo_db = boto3.resource('dynamodb')
    user_notes_table = dynamo_db.Table('user-notes')
    
    # Query the user-notes table using the user email and sort by create_date in descending order
    result = user_notes_table.query(
        IndexName='email-create_date-index',  # Assuming a GSI on email and create_date
        KeyConditionExpression=Key('user').eq(user_email),
        ScanIndexForward=False,  # DESC ORDER
        Limit=10 
    )

    # Return the list of notes
    notes = result.get('Items', [])
    
    return notes


# Don't modify this function name and arguments
def get_authenticated_user_email(token):
    dynamo_db = boto3.resource('dynamodb')
    tokens_table = dynamo_db.Table('token-email-lookup')

    # Validate the given token with one from the database
    response = tokens_table.get_item(
        Key={
            'token': token
        }
    )
    # and return user email if the tokens match ...
    # Check if the token exists in the database
    if 'Item' not in response:
        raise InvalidResponse(status_code=401)
    
    # Get the email associated with the token
    return response['Item']['email']


def authenticate_user(headers):
    authentication_header = headers['Authentication']

    # Validate the Authentication header
    match = re.match(r'^Bearer\s+(\S+)$', authentication_header)
    if not match:
        raise InvalidResponse(status_code=403)
    token = match.group(1)

    user_email = get_authenticated_user_email(token)

    return user_email


def build_response(status_code, body=None):
    result = {
        'statusCode': str(status_code),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }
    if body is not None:
        result['body'] = body

    return result


# Don't modify handler, make other functions feet it
def handler(event: dict, context):
    try:
        user_email = authenticate_user(event['headers'])
        notes = query_user_notes(user_email)
    except InvalidResponse as e:
        return build_response(status_code=e.status_code)
    else:
        return build_response(
            status_code=200,
            body=json.dumps(notes)
        )
