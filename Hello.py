  if len(self.que) > 0:
            print(tc.Lane.is_last_free(self.lane) == True)
            if tc.Lane.is_last_free(self.lane) == True: 
                self.lane.enter(self.que[0])
                self.que.pop(0)
                self.que.append(vehicle)
        else:
                if tc.Lane.is_last_free(self.lane)== True and temp
                    self.lane.enter(vehicle)
                    self.que.append(vehicle)



        if temp_des != None:
            vehicle = tc.Vehicle(temp_des, self.time)
            self.vehicle_counter += 1

            if len(self.que) > 0:
                if tc.Lane.is_last_free(self.lane) == True and temp_des != None:
                    self.lane.enter(self.que[0])
                    self.que.pop(0)
                self.que.append(vehicle)
                self.que_count += 1 
            else:
                if tc.Lane.is_last_free(self.lane) == True and temp_des != None:
                    self.lane.enter(vehicle)
                else:
                    self.que.append(vehicle)
                    self.que_count += 1                    


        creator = self.destination.step()
        if creator != None:
            vehicle = tc.Vehicle(creator, self.time)
            self.vehicle_counter += 1
        if self.lane.is_last_free() == True:
            if self.que == []:
                if creator != None:
                    self.lane.enter(vehicle)
            else:                   
                self.lane.enter(self.que.pop(0))
                if creator != None:
                    self.que.append(vehicle)
                                     
        else:
            if creator != None:
                self.que.append(vehicle)
        
        if self.que != []:
            self.que_count += 1
            print(' this is self', self.que_count)