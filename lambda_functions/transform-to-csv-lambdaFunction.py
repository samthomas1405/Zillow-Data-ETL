import json
import boto3
import pandas as pd

s3_client = boto3.client("s3")


def lambda_handler(event, context):

    source = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    target_bucket_name = "zillow-transform-from-json-to-csv"

    target_file_name = key[:-5]

    waiter = s3_client.get_waiter("object_exists")
    waiter.wait(Bucket=source, Key=key)

    response = s3_client.get_object(Bucket=source, Key=key)

    content = response["Body"].read().decode("utf-8")

    json_content = json.loads(content)

    data = []
    for i in json_content["results"]:
        zillow_data.append(i)

    df = pd.DataFrame(data)


    selected_columns = [
        "bathrooms",
        "bedrooms",
        "city",
        "daysOnZillow",
        "homeStatus",
        "homeType",
        "livingArea",
        "price",
        "rentZestimate",
        "streetAddress",
        "zipcode",
    ]

    df = df[selected_columns]
    print(df)

    csv_data = df.to_csv(index=False)

    object_key = f"{target_file_name}.csv"
    s3_client.put_object(Bucket=target_bucket_name, Key=object_key, Body=csv_data)

    return {"statusCode": 200, "body": json.dumps("Transformed into CSV successfully")}
