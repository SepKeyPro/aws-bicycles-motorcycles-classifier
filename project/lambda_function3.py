import json
import re


THRESHOLD = .95


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = event['inferences']## TODO: fill in
    stop = "\[]"
    for s in stop:
        inferences = inferences.replace(s,"") 
    pred1 = float(inferences.split(',')[0])
    pred2 = float(inferences.split(',')[1])
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = False
    if (pred1 >= THRESHOLD or pred2 >= THRESHOLD):
        meets_threshold = True

    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }