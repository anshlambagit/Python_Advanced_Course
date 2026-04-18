class company:

    title:str = "consultancy"

    def __init__(self, company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return f"Company Name: {self.company_name}"


class employee(company):

    def __init__(self,employee_name:str, company_name:str):

        self.employee_name = employee_name
        self.company_name = company_name
    
    def info(self):
        response = company.info(self)
        print(f"The employee : {self.employee_name}, {response} ")


class contractor(company):

    def __init__(self, contractor_name:str, company_name:str):

        self.contractor_name = contractor_name
        self.company_name = company_name
    
    def info(self):
        response = company.info(self)
        print(f"The contractor : {self.contractor_name}, {response} ")


obj = employee("John Doe", "Tech Solutions")
obj.info()

obj2 = contractor("Jane Smith", "Tech Solutions")
obj2.info()