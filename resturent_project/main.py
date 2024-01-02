from abc import ABC,abstractclassmethod
class user(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        
class customer(user):
    def __init__(self, name, phone, email, address,money) -> None:
        self.wallet=money
        self.__order=None
        self.due_amount=None
        super().__init__(name, phone, email, address)
        
        
    @property
    def order(self,order):
        self.__order=order
        
        
    @order.setter
    def order(self,order):
        self.__order=order
        
    def place_order(self,order):
        self.order=order
        self.due_amount+=order.bill
        print(f'{self.name} placed an order with bill {order.bill}')
        
    def pay_for_order(self,amount):
        #TODO: submit the money to the manager
        pass
    
    def give_tips(self,tips_amount):
        pass
    
    def write_review(self,stars):
        pass
    