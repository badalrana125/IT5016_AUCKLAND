class Device:
    def turn_on(self):
        pass

class TV(Device):
    def turn_on(self):
        return "TV is on Now"
    
class Fan(Device):
    def turn_on(self):
        return "Fan is on Now"

class Light(Device):
    def turn_on(self):
        return "Light is on Now"
    
def activate_device(device):
    print(device.turn_on())

tv= TV()
fan=Fan()
light= Light()

activate_device(tv)
activate_device(fan)
activate_device(light)