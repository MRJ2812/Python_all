class H_employee:
    
    
    def __init__(self,HourlySalary,Hours,DueAmount):
        self.HourlySalary = HourlySalary
        self.DueAmount = DueAmount
    
    
    def calculate(self):
        return self.HourlySalary + self.DueAmount
    
