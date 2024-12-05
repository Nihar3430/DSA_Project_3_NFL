#learned implementation from https://www.geeksforgeeks.org/hash-map-in-python/
import time

class HashMap:
    #create hashmap
    def __init__(self):
        self.size = 1000
        self.hashmap = [[] for _ in range(self.size)]

    #get hash of gameID using hashing function with powers of 31 of ASCII
    def get_hash(self, key):
        hash_num = 0
        key = str(key)
        for i, j in enumerate(key):
            hash_num += int(ord(j) * (31 ** i))
        return hash_num % self.size

    #insert into hashmap
    def insert(self, gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble):
        list_key = self.get_hash(gameID)
        #list_value = [gameID, [offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble, gameID]]
        #bucket = self.hashmap[list_key]

        for i in self.hashmap[list_key]:
            if i[0] == gameID:
                i[1][2] += first_down
                i[1][3] += yards
                i[1][4] += rush_attempts
                i[1][5] += passes
                i[1][6] += incomplete
                i[1][7] += touchdown
                i[1][8] += sack
                i[1][9] += interception
                i[1][10] += fumble
                return
        self.hashmap[list_key].append([gameID, [offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble, gameID]])

    #search hashmap with gameID as key
    def search(self, gameID):
        list_key = self.get_hash(gameID)
        #bucket = self.hashmap[list_key]
        for i in self.hashmap[list_key]:
            
            if i[0] == str(gameID):
                return i[1]
        return None


