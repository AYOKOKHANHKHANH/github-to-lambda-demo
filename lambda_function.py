import pandas as pd

def lambda_handler(event, context):
    d = {'col': [1,2], 'col': [3,4]}
    df = pd.DataFrame(date=d)
    print(df)
    print('Litle Pony')