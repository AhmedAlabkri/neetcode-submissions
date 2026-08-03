class TimeMap:

    def __init__(self):

        self.my_dict = {} # {"key": [["value": timestamp]]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = []
        self.my_dict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.my_dict:
            return res 
        L = 0
        R = len(self.my_dict[key]) - 1

        while L <= R:
            mid = (L + R) // 2

            if self.my_dict[key][mid][1] <= timestamp:
                res = self.my_dict[key][mid][0]
                L = mid + 1
            else:
                R = mid - 1
            
        return res
            








        
