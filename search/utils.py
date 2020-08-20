import boto3
import requests

subscription_key = "ddd508c68228430389aa3cd991cd24de"

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

search_term = "Azure Cognitive Services"


dynamo_db_access_key = "AKIAJQIDJOUWBWNLXXYA"

dynamo_db_secret_key = "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"

def create_dynamodb():
    return boto3.resource('dynamodb')

def create_search_request(query):
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    return  response.json()

def write_to_search_table(dynamodb, data):
    try:
        table = dynamodb.Table('Search')
        # {"search_id": 0, "search_query": "azure"}
        with table.batch_writer() as batch:
            batch.put_item(Item=data)

        return True
    except:
        return False