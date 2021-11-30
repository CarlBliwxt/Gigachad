
from statistics import mean, median
from time import sleep
import trafficComponents as tc
import destinations as d 


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):

        self.time = 0
        self.lane1 = tc.Lane(5)
        self.lane2 = tc.Lane(5)
        self.lights = tc.Light(10,8)
        self.destination = d.Destinations()
        self.vehicle_counter = 0
        self.que = []

    def snapshot(self):
        print(f'{self.lane1}, {self.lights}, {self.lane2}, {self.que}')
        

    def step(self):
        self.time += 1
        tc.Lane.remove_first(self.lane1)
        tc.Lane.step(self.lane1) # stepping first lane
        if tc.Light.is_green(self.lights) == True:
            if tc.Lane.is_last_free(self.lane1) == True: 
                if tc.Lane.get_first(self.lane2) != None: 
                    bil = tc.Lane.remove_first(self.lane2)
                    self.lane1.enter(bil)
        
        tc.Light.step(self.lights) # stepping lights
        tc.Lane.step(self.lane2) # stepping second lane

        temp_des= self.destination.step()
        if temp_des!= None:
            vehicle = tc.Vehicle(temp_des, self.time)
        
        if len(self.que) > 0:
            if tc.Lane.is_last_free(self.lane2) == True and temp_des != None:
                self.lane2.enter(self.que[0])
                self.que.pop(0)
            self.que.append(vehicle)
        else:
            if tc.Lane.is_last_free(self.lane2)== True and temp_des != None:
                self.lane2.enter(vehicle)
            else:
                self.que.append(vehicle)
            

    def in_system(self):
        pass

    def print_statistics(self):
        pass


def main():
    ts = TrafficSystem()
    for i in range(20):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
