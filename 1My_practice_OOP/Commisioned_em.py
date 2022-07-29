class H_employee:
    
     
    def __init__(self,soldAmount, percentage, due, paidAmount):
        self.soldAmount = soldAmount
        self.percentage = percentage
        self.due = due
        self.paidAmount = paidAmount
    
    
    def calculate(self):
        return (self.soldAmount * (self.percentage / 100)) + self.due
    
    def pay_now(self,paidamount):
        self.paidAmount = paidamount
        if (self.due > 0):
            if(self.paidAmount > self.due):
                self.due = 0
            else:
                pass
            

                
        
        
    
