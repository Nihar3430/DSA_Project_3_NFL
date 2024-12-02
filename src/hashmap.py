import time

class HashMap:
    class Pair:
        def __init__(self, gameID_new, offense, defense, first_down_new, yards_new, rush_attempts_new, passes_new, incomplete_new, touchdown_new, sack_new, interception_new, fumble_new):
            self.gameID = gameID_new
            self.offense = offense
            self.defense = defense
            self.first_down = first_down_new
            self.yards = yards_new
            self.rush_attempts = rush_attempts_new
            self.passes = passes_new
            self.incomplete = incomplete_new
            self.touchdown = touchdown_new
            self.sack = sack_new
            self.interception = interception_new
            self.fumble = fumble_new

    def __init__(self):
        self.size = 500
        self.hashmap = [[] for _ in range(self.size)]

    def get_hash(self, key):
        hash_num = 0
        for i, j in enumerate(key):
            hash_num += int(ord(j) * (31 ** i)) # sum of powers of 31 of ASCII values
        return hash_num % self.size

    def insert(self, gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble):
        new_node = self.Pair(gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble)
        list_key = self.get_hash(gameID)
        #list_value = [gameID, [offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble, gameID]]
        bucket = self.hashmap[list_key]

        for i in bucket:
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
        bucket.append([gameID, [offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble, gameID]])

    def search(self, gameID):
        list_key = self.get_hash(gameID)
        bucket = self.hashmap[list_key]
        for i in bucket:
            if i[0] == gameID:
                return i[1]
        return None



