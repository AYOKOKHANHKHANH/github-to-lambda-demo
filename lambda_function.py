import json
def lambda_handler(event, context):
    return tong2so(event['a'], event['b'])

def tong2so(a,b):
    return a+b