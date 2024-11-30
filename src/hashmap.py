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
            hash_num += ord(j) * (31 ** i) # sum of powers of 31 of ASCII values
        return hash_num % self.size

    def insert(self, gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble):
        new_node = self.Pair(gameID, offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble)
        list_key = self.get_hash(gameID)
        list_value = [gameID, [offense, defense, first_down, yards, rush_attempts, passes, incomplete, touchdown, sack, interception, fumble]]

        bucket = self.hashmap[list_key]
        for i, j in enumerate(bucket):
            k, v = j
            if k == gameID:
                bucket[i][2] += first_down
                bucket[i][3] += yards
                bucket[i][4] += rush_attempts
                bucket[i][5] += passes
                bucket[i][6] += incomplete
                bucket[i][7] += touchdown
                bucket[i][8] += sack
                bucket[i][9] += interception
                bucket[i][10] += fumble
                return
        bucket.append(list_value)

    def search(self, gameID):
        list_key = self.get_hash(gameID)
        bucket = self.hashmap[list_key]
        for k, v in bucket:
            if k == gameID:
                return v
        return None

