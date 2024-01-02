from abc import ABC,abstractclassmethod
from datetime import datetime
class user(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        self.nid=nid
        # TO DO:set user id dynamically
        self.id=0
        self.wallet=0
        
    def __repr__(self) -> str:
        return f'{self.name} {self.email} {self.nid}'
        
class rider(user):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_location=current_location
        self.current_ride=None
        self.wallet=0
        super().__init__(name, email, nid)
        
    
    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        
    @abstractclassmethod
    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}')
        
    def request_ride(self,location,dest):
        if not self.current_ride:
            # TO DO:set ride property
            ride_req=None
            # TO DO:set current ride via ride
            self.current_ride=None
            
    
    def update_location(self,current_location):
        self.current_location=current_location
            
class driver(user):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_location=current_location
        super().__init__(name, email, nid)  
        
    def display_profile(self):
        print(f'Driver with name: {self.name} and email {self.email}')
        
    def accept_ride(self,ride):
        ride.set_driver(self)


class ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=None
        
    def set_driver(self,driver):
        self.driver=driver
        
    def start_ride(self):
        self.start_time=datetime.now()
        
    def end_ride(self,rider,amount):
        self.end_ride=datetime.now()
        self.rider.wallet-=self.estimated_fare
        self.driver.wallet+=self.estimated_fare



class ride_request:
    def __init__(self,rider,end_location) -> None:
        self.rider=rider
        self.end_location=end_location
        
class ride_matching:
    def __init__(self) -> None:
        self.drivers=[]
        
    def find_driver(self,ride_request):
        if len(self.avaiable_drivers) > 0:
            #TO DO Find the closest driver of the rider
            driver=self.avaiable_drivers[0]
            Ride=ride(ride_request.rider.current_location,ride_request.end_location)
            
        driver.accept_ride(Ride)
        return Ride
        

    

    
            
rahim=user('Alim khan','aa2@gmail.com',1122)
print(rahim)