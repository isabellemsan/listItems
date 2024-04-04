import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("items")

def lambda_handler(event, context):
 table.put_item(Item={'items_id': 'Banana'})
 response= table.scan()
 return response