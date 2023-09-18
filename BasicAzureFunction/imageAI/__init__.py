import logging

import azure.functions as func
import openai 
import os

secret_key = '<your OpenAI secret key>'

def main(req: func.HttpRequest) -> func.HttpResponse:
    # The following is a sample request, in JSON format, you can use to test
    # this function.  
    # Allowed sizes are: '256x256', '512x512', '1024x1024'.
    # {"prompt":"create an image of a beatiful wild flowers meadow", "n":1, "size":"512x512"}
    logging.info('Python HTTP trigger function processed a request.')

    # Set the secret key for authentication.
    openai.api_key = secret_key
    
    # Get variables from the HTTP request body.
    req_body = req.get_json()
    
    # Display info to the console.
    # logging.info(req_body)

    # Call OpenAI API. For the list of the allowed parameters,
    # see https://platform.openai.com/docs/api-reference/images/create. 
    output = openai.Image.create(
        prompt = req_body['prompt'],
        n = req_body['n'],
        size = req_body['size']
    )
    
    # Format the reponse. Get the URL of the produced foto. 
    # This gives you the URL of the first photo. 
    # If you have mutliple photos, you must iterates through 
    # the data object. 
    output_text = output['data'][0]['url']

    # Echo the reponse.
    return func.HttpResponse(f"{output_text}", status_code=200)
   