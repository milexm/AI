import logging

import azure.functions as func
import openai 

secret_key = '<your secret key>'

def main(req: func.HttpRequest) -> func.HttpResponse:
    # The following is a sample request, in JSON format, you can use to test
    # this function.  
    # {"model":"text-davinci-003", "prompt":"create an ad for chocolate company", "max_tokens":200, "temperature":0}
    logging.info('Python HTTP trigger function processed a request.')

    # Set the secret key for authentication.
    openai.api_key = secret_key
    
    # Get variables from the HTTP request body.
    req_body = req.get_json()
    
    # Display info to the console.
    # logging.info(req_body)

    # Call OpenAI API. For the list fo the allowed parameters,
    # see https://platform.openai.com/docs/api-reference/chat/create. 
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )
    
    # Format the reponse.
    output_text = output['choices'][0]['text']

    # Echo the reponse.
    return func.HttpResponse(f"{output_text}", status_code=200)
   