import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table_name')

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        body["form_id"] = str(uuid.uuid4())
        table.put_item(Item=body)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Data stored successfully!",
                "form_id": body["form_id"]
            }),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
