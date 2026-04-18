def pandas_decorator(fx):

    def mainfunc(*args):
        response = fx(*args)
        # Do some pandas specific processing here
        response.to_parquet("Ch-3_Polymorphism&Decorators\\temp.parquet")
        return response
    
    return mainfunc

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df


response = csv_to_parquet("Ch-3_Polymorphism&Decorators\\orders.csv")
print(response.head())