class TimeMap:

    def __init__(self):
        self.my_dict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_dict:
            self.my_dict[key].append((timestamp, value))
        else:
            self.my_dict[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        i = 0
        j = len(self.my_dict[key])
        timestamp_prev_I = ""

        while i <j:
            mid = (i+j) // 2

            if self.my_dict[key][mid][0] == timestamp:
                return self.my_dict[key][mid][1]

            elif self.my_dict[key][mid][0] < timestamp:
                if timestamp_prev_I == "":
                    timestamp_prev_I = mid
                else:
                    timestamp_prev_I = max(timestamp_prev_I, mid)
                i = mid + 1

            elif self.my_dict[key][mid][0] > timestamp:
                j = mid
        if timestamp_prev_I == "":
            return ""
        return self.my_dict[key][timestamp_prev_I][1]




        
