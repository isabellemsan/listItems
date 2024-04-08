import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("items")

def lambda_handler(event, context):
    response = table.get_item(Key={'items_id': 'Yellow'})
    return response  