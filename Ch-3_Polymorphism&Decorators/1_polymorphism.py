class api_fetch:
    def fetch(self):
        print("Fetching data from API...")

class database_fetch:
    def fetch(self):
        print("Fetching data from Database...")

class s3_fetch:
    def fetch(self):
        print("Fetching data from S3...")

obj = database_fetch()
obj.fetch()