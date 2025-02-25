import os 
def handler(event, context): 
    version = os.environ.get("VERSION","1.0.0")
    response_body ={
        "message":"Hello World!",
        "Version":"1.0.0"
    }
    return {"statusCode": 200, "body": response_body}