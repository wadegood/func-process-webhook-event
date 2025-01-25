import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="func_process_webhook_event", methods=("POST","GET"))
def func_process_webhook_event(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == 'POST':
        message = req.get_body()
        logging.info(message)
        return func.HttpResponse("Message Received from Strava.",status_code=200)
    
    if req.method == 'GET':
        hub_challenge = req.params.get('hub.challenge')

        if hub_challenge:
            logging.info('Validation Successful. Strava subscription is now active.')
            return func.HttpResponse(json.dumps({"hub.challenge":hub_challenge}),
            status_code=200)
        else:
            logging.info('Validation failed. Unable to setup Strava subscription')
            return func.HttpResponse("Validation Failed. Please try again.",status_code=401)
    
    else:
        return func.HttpResponse(
             "Internal Server Error.",status_code=500)