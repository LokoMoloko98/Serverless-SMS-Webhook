import requests
import json
import os

def lambda_handler(event, context):
    api_key = os.environ.get('CLICKATELL_API_KEY')
    whatsapp_cell_to = os.environ.get('CELL_NUMBER_TO_WHATSAPP')
    sms_cell_to = os.environ.get('CELL_NUMBER_TO_SMS')
    #request_data = json.loads(event['body'])

    # Define the URL for the API call
    url = "https://platform.clickatell.com/v1/message"

    # Define the headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": api_key
    }

    # Define the JSON payload for the request
    payload = {
        "messages": [
            {
                "channel": "whatsapp",
                "to": whatsapp_cell_to,
                "content": "<Test Message>"
            },
            {
                "channel": "sms",
                "to": sms_cell_to,
                "content": "<Test Message>"
            }
        ]
    }

    # Send the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code and handle accordingly
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'SMS successfully sent'})
        }
    elif response.status_code == 207:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'SMS successfully sent'})
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'ERROR: SMS FAILED TO Send'})
        }
    