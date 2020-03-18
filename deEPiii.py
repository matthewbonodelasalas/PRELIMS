class Airplane:
    def __init__(self):
        self.speed = 0
    def set_speed(self,speed):
        self.speed = speed
    def get_speed(self):
        return self.speed

class Jet(Airplane):
    def __init__(self):
        self.MULTIPLIER = 2
    def set_speed(self,speed):
        super().set_speed(speed*self.MULTIPLIER)
    def get_speed(self):
        super().set_speed(self.get_speed*2)

class FlyTest():
    biplane = Airplane()
    biplane.set_speed(212)
    print(biplane.set_speed)
    boeing = Jet()
    boeing.set_speed(424)
    print(boeing.set_speed)
    x = 1
    while x == 0:
        biplane.accelerate()
        print(biplane.set_speed)
        if boeing.set_speed > 5000:
            boeing.set_speed(boeing.get_speed() * 2)
        else:
            boeing.accelerate()
        x += 1
        print(biplane.get_speed())

FlyTest()


