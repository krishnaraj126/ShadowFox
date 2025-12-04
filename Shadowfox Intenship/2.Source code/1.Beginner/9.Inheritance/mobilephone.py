class MobilePhone:
    def __init__(self,screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def make_call(self,number):
        print(f"Calling {number}...")
    
    def receive_call(self,caller):
        print(f"Call from {caller}...")
    
    def take_picture(self):
        print(f"Taking a picture with {self.rear_camera} camera.")
    
#child class for Apple
class Apple(MobilePhone):
    def __init__(self,model,front_camera,rear_camera,ram,storage):
        super().__init__("Touch Screen" , "5G" ,False,front_camera,rear_camera,ram,storage)
        self.model = model
    
    def show_info(self):
        print(f"Apple model :{self.model}")
        print(f"Front Camera : {self.front_camera}")
        print(f"Rear Camera : {self.rear_camera}")
        print(f"Ram: {self.ram}")
        print(f"Storage : {self.ram}")
        print()

#child class for Samsung
class Samsung(MobilePhone):
    def __init__(self,model,dual_sim,front_camera,rear_camera,ram,storage):
        super().__init__("Touch Screen" ,"4G/5G",dual_sim,front_camera,rear_camera,ram,storage)
        self.model = model
    
    def show_info(self):
        print(f"Samsung Model : {self.model}")
        print(f"Dual sim : {self.dual_sim}")
        print(f"Rear Camera : {self.rear_camera}")
        print(f"Ram: {self.ram}")
        print(f"Storage : {self.ram}")
        print()

#creating objects for apple
iphone13 = Apple("Iphone-13","12MP","48MP","4GB","128GB")
iphone15 = Apple("Iphone-15","12MP","48MP","6GB","256GB")

#creating objects for samsung
samsungA14 = Samsung("Samsung-A14",True,"16MP","48MP","4GB","128GB")
samsungS23 = Samsung("Samsung-S23",False,"12MP", "50MP", "8GB", "256GB")

#Test the Objects

iphone13.show_info()
iphone13.make_call("8667261217")
iphone13.take_picture()

print("\n-----------------------------------------------------------------\n")

samsungA14.show_info()
samsungA14.receive_call("Google")
samsungA14.take_picture()