import os
import io
import boto3
import json
import base64

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-01-12-16-31-47-514" ## TODO: fill in
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])

    # Instantiate a Predictor
    # predictor = sagemaker.predictor.Predictor(ENDPOINT) ## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    # inferences = predictor.predict(image, initial_args={'ContentType': 'application/x-image'}) ## TODO: fill in
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                       ContentType='application/x-image',
                                       Body=image)
    print(response)
    result = response['Body'].read().decode('utf-8')
    
    # We return the data back to the Step Function    
    event["inferences"] = result
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }