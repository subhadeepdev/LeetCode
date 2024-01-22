from bisect import bisect

class TimeMap:
    def __init__(self):
        self.dictionary = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = [(timestamp, value)]
        else:
            self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        # timestamps = sorted(self.dictionary[key])
        index = bisect(self.dictionary[key], timestamp, key = lambda x: x[0]) - 1
        if index < 0:
            return ""
        return self.dictionary[key][index][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
    
calls = ["TimeMap","set","set","get","get","get","get","get"]
parameters = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

for call, parameter in zip(calls, parameters):
    match call:
        case "TimeMap":
            obj = TimeMap()
        case "set":
            obj.set(parameter[0], parameter[1], parameter[2])
        case "get":
            print(obj.get(parameter[0], parameter[1]))
