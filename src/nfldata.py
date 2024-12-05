import csv
import time
from redBlackTree import RedBlackTree
from hashmap import HashMap


file_path = "../Database/NFLdata.csv"

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

#read data from CSV file and call red-black tree insert
def redblackinsert(gameID1, gameID2):
    # Read and process the CSV data
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
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
        return mock, mock2, elapsed_nano

#read data from CSV file and call hashmap insert
def hashmapinsert(gameID1, gameID2):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
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
        return mock, mock2, elapsed_nano

#insert nodes into a dictionary so we can find the gameID with both the teams and game date as a keyd
def dictinsert(off, denf, date):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        game_data = {}

        # Insert rows into the dictionary
        for row in reader:
            updated_game_id = update_id((row['GameId']), row['OffenseTeam'])
            # Insert game data with a composite key
            game_data[(row['OffenseTeam'], row['DefenseTeam'], row['GameDate'])] = updated_game_id

        # Search for a specific game ID using the input keys
        search_key = (off, denf, date)

        if search_key in game_data:
            return game_data[search_key]
        else:
            print("Game ID not found.")
            return 1

if __name__ == "__main__":
    while True:
        print("Welcome to the NFL Matchup Statistics Visualizer by The Krewe")
        print("This tool allows you to see the statistics of both teams of the past games they played from 2021, 2022, or 2023")
        print("Select two NFL teams by using their abbreviations below and a enter the date they played\n")


        print("Arizona Cardinals = ARI\nAtlanta Falcons = ATL\nBaltimore Ravens = BAL\nBuffalo Bills = BUF\nCarolina Panthers = CAR\nChicago Bears = CHI\nCincinnati Bengals = CIN\nCleveland Browns = CLE\nDallas Cowboys = DAL\nDenver Broncos = DEN\nDetroit Lions = DET\nGreen Bay Packers = GB\nHouston Texans = HOU\nIndianapolis Colts = IND\nJacksonville Jaguars = JAX\nKansas City Chiefs = KC\nLas Vegas Raiders = LV\nLos Angeles Chargers = LAC\nLos Angeles Rams = LA\nMiami Dolphins = MIA\nMinnesota Vikings = MIN\nNew England Patriots = NE\nNew Orleans Saints = NO\nNew York Giants = NYG\nNew York Jets = NYJ\nPhiladelphia Eagles = PHI\nPittsburgh Steelers = PIT\nSan Francisco 49ers = SF\nSeattle Seahawks = SEA\nTampa Bay Bucs = TB\nTennessee Titans = TEN\nWashington Commanders = WAS\n\n")

        team_one = input("Enter the abbreviation for Team One: ")
        team_two = input("Enter the abbreviation for Team Two: ")
        date = input("Enter the date of playing in the format \"Month, Day, Year\" Example: 10/2/2022: ")

        k = int(dictinsert(team_one, team_two, date))
        m = int(dictinsert(team_two, team_one, date))

        print("\nNext choose whether you want to load the data from a red-black tree or hashmap.\nEnter r for red-black tree or h for hashmap:")
        data_structure = input()
        if data_structure == "r":
            i, j, time_taken = redblackinsert(k, m)
        if data_structure == "h":
            i, j, time_taken = redblackinsert(k, m)

        print(f"\n\n{team_one} Stats")
        print(f"Total Offensive Yards: {i[3]}\nTotal Rush Attempts: {i[4]}\nTotal Pass Attempts: {i[5]}\nTotal Incompletions: {i[6]}\nTotal Touchdowns: {i[7]}\nTotal Sacks: {i[8]}\nTotal Interceptions: {i[9]}\nTotal Fumbles: {i[10]}")

        print(f"\n{team_two} Stats")
        print(f"Total Offensive Yards: {j[3]}\nTotal Rush Attempts: {j[4]}\nTotal Pass Attempts: {j[5]}\nTotal Incompletions: {j[6]}\nTotal Touchdowns: {j[7]}\nTotal Sacks: {j[8]}\nTotal Interceptions: {j[9]}\nTotal Fumbles: {j[10]}")


        if data_structure == "r":
            print(f"\nTime taken to load data from red-black tree: {int(time_taken)} nanoseconds")
        if data_structure == "h":
            print(f"\nTime taken to load data from hashmap: {int(time_taken)} nanoseconds")

        decision = input("\nEnter \"q\" to quit or any other character to continue and selct another game: ")

        if decision == "q":
            break
