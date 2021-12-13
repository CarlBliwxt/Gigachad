
from statistics import mean, median
from time import sleep
import trafficComponents as tc
import destinations as d 
import numpy as np 


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):

        self.time = 0
        self.lane = tc.Lane(11)
        self.lane_west = tc.Lane(8)
        self.lane_south = tc.Lane(8)
        self.light_west = tc.Light(14,6)
        self.light_south = tc.Light(14,4)
        self.destination = d.Destinations()
        self.exit_west = 0
        self.exit_south = 0
        self.vehicle_counter = 0
        self.que = []
        self.blocked = 0
        self.que_count = 0
        self.exitedCars = []
        self.west_insystem_time = []
        self.south_insystem_time = []
        self.check_blocked = False

    def snapshot(self):
        if self.check_blocked: 
            print(self.check_blocked)
            print(f'{self.light_west},  {self.lane_west}, * {self.lane}, {self.que},') 
            print(f'{self.light_south}, {self.lane_south}')
        else: 
            print(self.check_blocked)
            print(f'{self.light_west}, {self.lane_west}, {self.lane}, {self.que},') 
            print(f'{self.light_south}, {self.lane_south}')
        

    def step(self):
        
        self.time += 1
        # Vehicle or None gets removed 
        if tc.Light.is_green(self.light_west):

            if tc.Lane.get_first(self.lane_west) != None:  # Check if Vehicle 
                self.exit_west += 1
                removed_vehicle = tc.Lane.get_first(self.lane_west)
                exit_time = tc.Vehicle.born_time(removed_vehicle)
                time = abs(self.time - exit_time)
                self.west_insystem_time.append(time)
            tc.Lane.remove_first(self.lane_west)
                
        
               
        if tc.Light.is_green(self.light_south): 
            if tc.Lane.get_first( self.lane_south) != None:
                self.exit_south += 1  
                removed_vehicle = tc.Lane.get_first(self.lane_south)
                exit_time = tc.Vehicle.born_time(removed_vehicle)
                time = abs(self.time - exit_time)
                self.south_insystem_time.append(time)
            tc.Lane.remove_first(self.lane_south)


        #Step of files    
        tc.Lane.step(self.lane_west)
        tc.Lane.step(self.lane_south)
        # Transform to get a string
        direction = str(tc.Lane.get_first(self.lane))
        # Two directions, two if-statements 
        if direction == "W" : 
            if tc.Lane.is_last_free(self.lane_west):
                bil = tc.Lane.remove_first(self.lane)
                self.lane_west.enter(bil)
                self.check_blocked = False
            else: 
                self.blocked += 1
                self.check_blocked = True
        if direction == "S" : 
            if tc.Lane.is_last_free(self.lane_south):
                bil = tc.Lane.remove_first(self.lane)
                self.lane_south.enter(bil)
                self.check_blocked = False
            else: 
                self.blocked += 1
                self.check_blocked = True



        # Stepping of the lane
        tc.Lane.step(self.lane)
        # Stepping the destination to get a "new" destination
        temp_des = self.destination.step()
        if temp_des != None: # check for None
            vehicle = tc.Vehicle(temp_des, self.time)
            self.vehicle_counter += 1

        # Handling the que
        if tc.Lane.is_last_free(self.lane): 
            if len(self.que) > 0:
                self.que_count += 1
                self.lane.enter(self.que.pop(0))
                if  temp_des != None:
                    self.que.append(vehicle)
                    self.que_count += 1
            else:
                if temp_des != None:
                    self.lane.enter(vehicle)
        else: 
            if temp_des != None:
                self.que.append(vehicle)
                self.que_count += 1
        

        # Stepping both lights 
        tc.Light.step(self.light_south)
        tc.Light.step(self.light_west)


    def in_system(self):
        # Everything that is in the system at the time
        in_lane = self.lane.number_in_lane()
        lane_west = self.lane_west.number_in_lane()
        lane_south = self.lane_south.number_in_lane()
        que = len(self.que) 
        sumof = in_lane + lane_west + lane_south + que 
        return sumof 
    

    def print_statistics(self):
        x = ' '
        # Everything needed for west 
        west_minimal_time = np.amin(self.west_insystem_time)
        west_maximal_time = np.amax(self.west_insystem_time)
        west_median = format(median(sorted(self.west_insystem_time)),".1f")
        west_time_average = round(mean(self.west_insystem_time),1)
        #Everything needed for south
        south_minimal_time = np.amin(self.south_insystem_time)
        south_maximal_time = np.amax(self.south_insystem_time)
        south_median = format(median(sorted(self.south_insystem_time)),".1f") 
        south_time_average = round(mean(self.south_insystem_time),1)

        #Blocked and queue: 
        blocked = round(self.blocked/self.time, 3 ) * 100
        queue = float(self.que_count/self.time) * 100
        queue = round(queue, 2)

    
        
        # Printout 
        print(f'Statistics after {self.time} timesteps:')

        print(f'Created vehicles:{self.vehicle_counter}')
        print(f'Cars in system:  {self.in_system()}')

        print(f'At exit: {x *6} West: {x * 6 } South:')
        print(f'Vehicles out: {x * 2} {self.exit_west} {x *11} {self.exit_south}')
        print(f'Minimal time: {x * 2} {west_minimal_time} {x * 11} {south_minimal_time}')
        print(f'Maximal time: {x * 2} {west_maximal_time} {x * 11} {south_maximal_time}')
        print(f'Mean time   : {x * 2} {west_time_average} {x * 8} {south_time_average}')
        print(f'Median time : {x * 2} {west_median} {x*8} {south_median}')
        print(f'Blocked : {x * 2}{blocked} % ')
        print(f'Queue   : {x * 2}{queue} % ')
        


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
