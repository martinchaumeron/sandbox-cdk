import json
import os
import uuid
from datetime import datetime, timezone

import boto3

s3 = boto3.client("s3")
BUCKET = os.environ["BUCKET_NAME"]


def main(event, context):
    params = event.get("queryStringParameters") or {}
    message = params.get("message", "hello")

    key = f"messages/{datetime.now(timezone.utc):%Y-%m-%d}/{uuid.uuid4()}.json"
    body = {
        "message": message,
        "received_at": datetime.now(timezone.utc).isoformat(),
        "request_id": context.aws_request_id,
    }

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(body).encode("utf-8"),
        ContentType="application/json",
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"stored": key, "echo": message}),
    }