import os
import boto3


def handler(event, context):

    path = event["rawPath"]
    if path != "/":
        return {"statuscode": 404, "body": "Not found."}
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ.get("TABLE_NAME"))

    response = table.get_item(key={"key": "visit_count"})
    if "Item" in response:
        visit_count = response["Item"]["value"]
    else:
        visit_count = 0

    new_visit_count = visit_count + 1
    table.put_item(Item={"key": "visit_count", "value": new_visit_count})
    version = os.environ.get("VERSION", "1.0.0")
    response_body = {
        "message": "Hello World 🚀",
        "Version": version,
        "visit_count": new_visit_count,
    }
    return {"statusCode": 200, "body": response_body}
