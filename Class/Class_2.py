class salary:
    
    def set_value(self,name,salary):
        self.name = name
        self.salary = salary
               
    
    def calculate(self):
        return self.salary + 100
    
    
employee = salary()
employee.set_value("joy", 2000)

print(employee.calculate())