# Traffic system components
from time import sleep
from statistics import mean, median


class Vehicle:
    """Represents vehicles in traffic simulations"""
    def __init__(self, destination, borntime):
        self.destination = destination
        self.borntime = borntime
    def __str__(self):
        return f'{self.destination}'
    def born_time(self):
        return self.borntime
    __repr__ = __str__
    
class Lane:
    "Represents a lane with (possible) vehicles"
    def __init__(self, length):
        self.lane = [None] * length
        
    def __str__(self):
        return f'{self.lane}' 

    def enter(self, vehicle):
    
        self.lane[-1] = vehicle

    def is_last_free(self):
        if self.lane[-1] == None :
            return True
        else:
            return False

    def step(self):
        for n in range(len(self.lane)- 1):
            if self.lane[n] == None:
                self.lane[n] = self.lane[n+1]
                self.lane[n+1] = None

    def get_first_string(self):
        if self.lane[0] == None:
            return None
        else: 
            return str(self.lane[0])

    def get_first(self):
        if self.lane[0] == None:
            return None
        else: 
            return self.lane[0]


    def remove_first(self):
        if self.get_first == None:
            return None
        else: 
            temp = self.lane[0]
            self.lane.pop(0)
            self.lane.insert(0, None)
        return temp

    def number_in_lane(self):
        return len(self.lane) - self.lane.count(None)

def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)
    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        self.period = period 
        self.green_period = green_period
        self.signal = True
        self.internal_time = 0
        self.red_period = period - green_period
        

    def __str__(self):
        
        """Report current state of the light."""
        if self.signal == True:
            color = str('G')
        else: 
            color = str('R')
        return color
      

    def step(self):
        """Take one light time step."""
        self.internal_time += 1 
        if (self.green_period > self.internal_time and self.signal == True):
            self.signal = True
        elif self.internal_time >= self.period and self.signal == False:
            self.internal_time = 0
            self.signal = True
        else: 
            self.signal = False
        return self.signal

    def is_green(self):
        """Return whether the light is currently green."""
        if self.signal == True: 
            return True
        else:
            return False
        

def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()
