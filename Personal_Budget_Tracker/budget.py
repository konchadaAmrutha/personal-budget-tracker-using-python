class Expense :
    def __init__(self, name , category , amount) -> None:
        self.name = name 
        self.category = category
        self.amount = amount

    '''If you want to print burget then we get output as <budget.Expense object at 0x0000026F68A3FFD0> to overcome this we use repr'''
    def __repr__(self) :
        return f" Expense : {self.name} , {self.category} , {self.amount}"
    
