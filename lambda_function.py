def lambda_handler(event, context):
    return bieuthuc(event['a'], event['b'], event['c'])

def tong2so(a,b):
    return a+b

def bieuthuc(a,b,c):
    return tong2so*a-b+c