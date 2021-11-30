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