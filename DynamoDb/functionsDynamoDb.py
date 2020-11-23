import boto3
from boto3.dynamodb.conditions import Key

def add_processed_file(file_name):
    file = {
        'id': file_name
    }
    
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('task-log')
    
    table.put_item(Item=file)


def check_for_file(file_name):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('task-log')
    
    response = table.get_item(
        Key={
            'id': file_name
        }
    )
    
    if 'Item' in response:
        print('DynamoDb get_item query:')
        print(response['Item'])
        return True
    else:
        print('Nothing found')
        return False