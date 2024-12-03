import csv
import time
from redBlackTree import RedBlackTree
from hashmap import HashMap


file_path = ["../Database/2023_Database.csv", "../Database/2022_Database.csv", "../Database/2021_Database.csv" ]

# Update the GameId based on the offense team
def update_id(gameID, offense_team):
    nfl_teams = {
        "ARI": "01",  # Arizona Cardinals
        "ATL": "02",  # Atlanta Falcons
        "BAL": "03",  # Baltimore Ravens
        "BUF": "04",  # Buffalo Bills
        "CAR": "05",  # Carolina Panthers
        "CHI": "06",  # Chicago Bears
        "CIN": "07",  # Cincinnati Bengals
        "CLE": "08",  # Cleveland Browns
        "DAL": "09",  # Dallas Cowboys
        "DEN": "10", # Denver Broncos
        "DET": "11", # Detroit Lions
        "GB": "12",  # Green Bay Packers
        "HOU": "13", # Houston Texans
        "IND": "14", # Indianapolis Colts
        "JAX": "15", # Jacksonville Jaguars
        "KC": "16",  # Kansas City Chiefs
        "LV": "17",  # Las Vegas Raiders
        "LAC": "18", # Los Angeles Chargers
        "LA": "19", # Los Angeles Rams
        "MIA": "20", # Miami Dolphins
        "MIN": "21", # Minnesota Vikings
        "NE": "22",  # New England Patriots
        "NO": "23",  # New Orleans Saints
        "NYG": "24", # New York Giants
        "NYJ": "25", # New York Jets
        "PHI": "26", # Philadelphia Eagles
        "PIT": "27", # Pittsburgh Steelers
        "SF": "28", # San Francisco 49ers
        "SEA": "29", # Seattle Seahawks
        "TB": "30", # Tampa Bay Bucs
        "TEN": "31", # Tennessee Titans
        "WAS": "32"  # Washington Commanders
    }

    if offense_team not in nfl_teams:
        raise ValueError(f"Unknown team abbreviation: {offense_team}")

    team_num = nfl_teams[offense_team]
    updated_gameID = gameID + team_num
    return updated_gameID


def redblackinsert(gameID1, gameID2):
    # Read and process the CSV data
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        print("Headers:", reader.fieldnames)
        tree = RedBlackTree()

        # Insert rows into the Red-Black Tree
        for row in reader:
            updated_game_id = update_id((row['GameId']), row['OffenseTeam'])
            tree.insert(
                int(updated_game_id),  # GameId as an integer
                row['OffenseTeam'],     # OffenseTeam as string
                row['DefenseTeam'],     # DefenseTeam as string
                int(row['Down']),       # First Down as integer
                int(row['Yards']),      # Yards as integer
                bool(int(row['IsRush'])),  # Rush as boolean
                bool(int(row['IsPass'])),  # Pass as boolean
                bool(int(row['IsIncomplete'])),  # Incomplete as boolean
                bool(int(row['IsTouchdown'])),   # Touchdown as boolean
                bool(int(row['IsSack'])),        # Sack as boolean
                bool(int(row['IsInterception'])), # Interception as boolean
                bool(int(row['IsFumble']))       # Fumble as boolean
            )

        # Search for a specific game ID in the tree
        start = time.perf_counter()
        mock = tree.search(gameID1)
        mock2 = tree.search(gameID2)
        end = time.perf_counter()
        elapsed_nano = (end - start) * 1e9
        print(elapsed_nano)
        return mock, mock2

def hashmapinsert(gameID1, gameID2):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        print("Headers:", reader.fieldnames)
        map = HashMap()

        # Insert rows into the Red-Black Tree
        for row in reader:
            updated_game_id = update_id((row['GameId']), row['OffenseTeam'])
            #print(f"Inserting gameID: {updated_game_id}")
            map.insert(
                updated_game_id,  # GameId as an integer
                row['OffenseTeam'],     # OffenseTeam as string
                row['DefenseTeam'],     # DefenseTeam as string
                int(row['Down']),       # First Down as integer
                int(row['Yards']),      # Yards as integer
                bool(int(row['IsRush'])),  # Rush as boolean
                bool(int(row['IsPass'])),  # Pass as boolean
                bool(int(row['IsIncomplete'])),  # Incomplete as boolean
                bool(int(row['IsTouchdown'])),   # Touchdown as boolean
                bool(int(row['IsSack'])),        # Sack as boolean
                bool(int(row['IsInterception'])), # Interception as boolean
                bool(int(row['IsFumble']))       # Fumble as boolean
            )

        # Search for a specific game ID in the tree
        start = time.perf_counter()
        mock = map.search(gameID1)
        mock2 = map.search(gameID2)
        end = time.perf_counter()
        elapsed_nano = (end - start) * 1e9
        print(elapsed_nano)
        return mock, mock2

def dictinsert(off, denf, date):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        print("Headers:", reader.fieldnames)
        game_data = {}

        # Insert rows into the dictionary
        for row in reader:
            updated_game_id = update_id((row['GameId']), row['OffenseTeam'])
            # Insert game data with a composite key
            game_data[(row['OffenseTeam'], row['DefenseTeam'], row['GameDate'])] = updated_game_id

        # Search for a specific game ID using the input keys
        search_key = (off, denf, date)

        if search_key in game_data:
            print(game_data[search_key])
            return game_data[search_key]
        else:
            print("Game ID not found.")

if __name__ == "__main__": 
    k = int(dictinsert("GB", "LA", "11/5/2023"))
    m = int(dictinsert("LA", "GB", "11/5/2023"))
    i, j = hashmapinsert(k, m)
    print(i)
    print(j)

