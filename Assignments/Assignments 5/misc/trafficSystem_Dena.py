
from statistics import mean, median
from time import sleep
import destinations
import trafficComponents_Dena as tc


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self, lane1 = 5, lane2 = 5, period = 10, greenPeriod = 8):
        self.time = 0
        self.lane1 = tc.Lane(lane1)
        self.lane2 = tc.Lane(lane2)
        self.light = tc.Light(period, greenPeriod)
        self.destionation = destinations.Destinations()
        self.que = []
        
    def snapshot(self):
        print(f'Time step {self.time}')
        print(f'{self.lane1}, {self.light}, {self.lane2}'
                f'{[x.destination for x in self.que]}')

    def step(self):
        self.time += 1
        
        self.lane1.remove_first()
        self.lane1.step()
        
        
        if self.light.is_green():
            v = self.lane2.remove_first()
            self.lane1.enter(v)
        
        self.light.step()
        self.lane2.step()
         
        dest = self.destionation.step()
        if dest != None: # check for None
            vehicle = tc.Vehicle(dest, self.time)

 
        
        
        if  len(self.que) > 0:
            if self.lane2.is_last_free()==True and dest != None:
                self.lane2.enter(self.que[0])
                self.que.pop(0)
            self.que.append(vehicle)
            
        else: 
            if self.lane2.is_last_free()==True and dest != None:
                self.lane2.enter(vehicle)
            else:
                self.que.append(vehicle)


    def in_system(self):
        pass

    def print_statistics(self):
        pass


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()

