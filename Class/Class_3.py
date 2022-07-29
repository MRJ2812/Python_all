class salary:
    
    def set_value(self,name,salary):
        self.name = name
        self.salary = salary
    
    def calculate(self):
        return self.salary + 100
    
    def display(self):
        print(f"Name {self.name} and {self.calculate()}")                # Call another method ,, give self
    
employee = salary()
employee.set_value("joy", 1000)

employee.display()