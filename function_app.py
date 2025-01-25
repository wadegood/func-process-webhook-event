import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="func_process_webhook_event")
def func_process_webhook_event(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    hub_challenge = req.params.get('hub.challenge')
    
    if hub_challenge:
        return func.HttpResponse(json.dumps({"hub.challenge":hub_challenge}),
        status_code=200)
    
    else:
        return func.HttpResponse(
             "Validation Failed. Please try again.",
             status_code=401
        )