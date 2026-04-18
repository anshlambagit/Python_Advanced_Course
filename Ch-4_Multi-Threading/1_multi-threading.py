import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url: str):

    print("Fetching data from:", url)
    time.sleep(5)
    print("Data fetched from:", url)
    return "Data from " + url

urls_list = ["https://example.com/api/data1", 
             "https://example.com/api/data2", 
             "https://example.com/api/data3", 
             "https://example.com/api/data4", 
             "https://example.com/api/data5"]


results = []
with ThreadPoolExecutor(max_workers=len(urls_list)) as executor:
    futures = executor.map(fetch_data, urls_list)
    results.extend(futures)

print(results)