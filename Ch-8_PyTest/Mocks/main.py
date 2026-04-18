import requests

def api_call(url):

    import requests   
    response = requests.get(url)
    return {"data": response.json()}