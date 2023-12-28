class RandomizedSet:

    def __init__(self):
        # declares an empty dict and list
        self.random_dict = {}
        self.random_list = []

    def insert(self, val: int) -> bool:
        #check if val in dict
        if(val in self.random_dict):
            return False
        self.random_list.append(val)
        self.random_dict[val] = len(self.random_list) - 1
        return True

    def remove(self, val: int) -> bool:
        #check if val in dict
        if(val in self.random_dict):
            #swaps end element to deleted element position as it deletes element (since list remove is O(N) but pop is O(1))
            temp = self.random_dict[val]
            self.random_dict[self.random_list[len(self.random_list) - 1]] = temp
            self.random_list[temp] = self.random_list[len(self.random_list) - 1]
            self.random_list.pop()
            if(val in self.random_dict):
                del self.random_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        #random choice picks in O(1) runtime from a list
        return random.choice(self.random_list)