def my_decorator(fx):

    def mainfunc(*args):
        print("Before calling the function")
        response = fx(*args)
        print("After calling the function")
        return response

    return mainfunc


@my_decorator
def fetch_data(url:str,path:str):
    return f"Fetching data from {url} and saving to {path}"

response = fetch_data("https://example.com/data","/tmp/data.csv")
print(response)