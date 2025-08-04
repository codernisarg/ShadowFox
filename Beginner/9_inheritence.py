#1. Create inheritance using MobilePhone as base class and Apple & Samsung as child class
#1. The base class should have properties:
#   a. ScreenType = Touch Screen
#   b. NetworkType = 4G/5G
#   c. DualSim = True or False
#   d. FrontCamera = (5MP/8MP/12MP/16MP)
#   e. rearCamera = (8MP/12MP/16MP/32MP/48MP)
#   f. RAM = (2GB/3GB/4GB)
#   g. Storage = (16GB/32GB/64GB)
#2. Create basic mobile phone functionalities in the classes like: make_call, recieve_call, take_a_picture, etc.
#3. Use super() constructor for calling parent class’s constructor
#4. Make some objects of Apple class with different properties
#5. Make some objects of Samsung class with different properties


class MobilePhone:
    def __init__(self, brand, dual_sim, front_camera, rear_camera):
        self.brand = brand
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera

    def make_call(self, number):
        print(f"{self.brand}: Calling {number}...")

    def receive_call(self):
        print(f"{self.brand}: Receiving a call...")

    def take_a_picture(self):
        print(f"{self.brand}: Clicked a photo with {self.rear_camera} camera.")

    def show_info(self):
        print(f"{self.brand} Phone Info:")
        print(f"  Screen: {self.screen_type}")
        print(f"  Network: {self.network_type}")
        print(f"  Dual SIM: {self.dual_sim}")
        print(f"  Front Camera: {self.front_camera}")
        print(f"  Rear Camera: {self.rear_camera}")

class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera):
        super().__init__("Apple", dual_sim=False, front_camera=front_camera, rear_camera=rear_camera)


class Samsung(MobilePhone):
    def __init__(self, dual_sim, front_camera, rear_camera):
        super().__init__("Samsung", dual_sim=dual_sim, front_camera=front_camera, rear_camera=rear_camera)



iphone = Apple("12MP", "50MP")
iphone.show_info()
iphone.make_call("**********0")
iphone.take_a_picture()
print("----------------------------------------------------------------------------")

samsung_phone = Samsung(True, "8MP", "48MP")
samsung_phone.show_info()
samsung_phone.receive_call()
samsung_phone.take_a_picture()

