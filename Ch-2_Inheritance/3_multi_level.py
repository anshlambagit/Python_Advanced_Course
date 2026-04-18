class company:

    title:str = "consultancy"

    def __init__(self, company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return f"Company Name: {self.company_name}"


class manager(company):

    def __init__(self, manager_name:str, company_name:str):

        self.manager_name = manager_name
        self.company_name = company_name
    
    def info(self):
        response = company.info(self)
        print(f"The manager : {self.manager_name}, {response} ")
        return f"The manager : {self.manager_name}, {response} "

class employee(manager):

    def __init__(self,employee_name:str, manager_name:str, company_name:str):

        self.employee_name = employee_name
        self.manager_name = manager_name
        self.company_name = company_name
    
    def info(self):
        response = manager.info(self)
        print(f"The employee : {self.employee_name}, {response} ")
        return f"The employee : {self.employee_name}, {response} "

obj = employee("John Doe", "Alice Johnson", "Tech Solutions")
obj.info()