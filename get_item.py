import json
import boto3
import os 

db_name = os.environ.get('my_db_name')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('db_name')

def lambda_handler(event, context):
    items_id = event.get('items_id')
    response = table.get_item(Key={'items_id': items_id})
    return response  