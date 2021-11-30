
from statistics import mean, median
from time import sleep
import trafficComponents as tc
import destinations as d 


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):

        self.time = 0
        self.lane = tc.Lane(11)
        self.lane_west = tc.Lane(8)
        self.lane_south = tc.Lane(8)
        self.light_west = tc.Light(14,6)
        self.light_south = tc.Light(10,4)
        self.destination = d.Destinations()
        self.exit_west = 0
        self.exit_south = 0
        self.vehicle_counter = 0
        self.que = []
        self.blocked = 0
        self.exitedCars = []

    def snapshot(self):
        print(f'{self.light_west}, {self.lane_west}, {self.lane}, {self.que}, {self.blocked}, {self.vehicle_counter}')
        print(f'{self.light_south}, {self.lane_south}')
        

    def step(self):
        
        self.time += 1

        if tc.Light.is_green(self.light_west):
            vehicleRemoved = tc.Lane.remove_first(self.lane_west)
            if vehicleRemoved != None:
                self.exit_west += 1
                timeBorn = vehicleRemoved.borntime
                vehicleRemoved.timeInSystem = abs(self.time - timeBorn)
                self.exitedCars.append(vehicleRemoved)
                
            # if tc.Lane.get_first(self.lane_west):
            #     
               
        if tc.Light.is_green(self.light_south):
            vehicleRemoved = tc.Lane.remove_first(self.lane_south)
            if vehicleRemoved != None:
                self.exit_south += 1
                current = self.lane_west.get_first()
                temp = tc.Vehicle.born_time(self.lane_west)

                print(temp)
                #vehicleRemoved.timeInSystem = abs(self.time - timeBorn)
                #self.exitedCars.append(vehicleRemoved)
                
        tc.Lane.step(self.lane_west)
        tc.Lane.step(self.lane_south)

        if tc.Lane.get_first_string(self.lane) == "W" : 
            if tc.Lane.is_last_free(self.lane_west) == True:
                bil = tc.Lane.remove_first(self.lane)
                self.lane_west.enter(bil)
            else: 
                self.blocked += 1
        
        
        if tc.Lane.get_first_string(self.lane) == "S" : 
            if tc.Lane.is_last_free(self.lane_south) == True:
                bil = tc.Lane.remove_first(self.lane)
                self.lane_south.enter(bil)
            else: 
                self.blocked += 1
        tc.Lane.step(self.lane)

        temp_des= self.destination.step()
        if temp_des != None:
            vehicle = tc.Vehicle(temp_des, self.time)
            self.vehicle_counter += 1

            if len(self.que) > 0:
                if tc.Lane.is_last_free(self.lane) == True and temp_des != None:
                    self.lane.enter(self.que[0])
                    self.que.pop(0)
                self.que.append(vehicle)
            else:
                if tc.Lane.is_last_free(self.lane) == True and temp_des != None:
                    self.lane.enter(vehicle)
                else:
                    self.que.append(vehicle)
        tc.Light.step(self.light_south)
        tc.Light.step(self.light_west)


    def in_system(self):
        
        pass

    def print_statistics(self):
        for vehicle in self.exitedCars:
            print(f'{vehicle.destination}, {vehicle.timeInSystem}')
        


def main():
    ts = TrafficSystem()
    for i in range(200):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
