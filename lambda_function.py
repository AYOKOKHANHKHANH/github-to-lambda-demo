import json
def lambda_handler(event, context):
    return bieuthuc(event["a"],event["b"])

def tong2so(a,b):
    return a+b

def bieuthuc(a,b):
    return tong2so(a,b) * tong2so(a,b) + a - b