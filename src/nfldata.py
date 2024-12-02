import csv
from redBlackTree import RedBlackTree

class Nfldata:
    def __init__(self, game_id, game_date, quarter, offense_team, defense_team, down, to_go, yard_line, season_year, yards, is_rush, is_pass, is_incomplete, is_touchdown, is_sack, is_interception, is_fumble):
        self.game_id = int(game_id)
        self.game_date = game_date
        self.quarter = int(quarter)
        self.offense_team = offense_team
        self.defense_team = defense_team
        self.down = int(down)
        self.to_go = int(to_go)
        self.yard_line = int(yard_line)
        self.season_year = int(season_year)
        self.yards = int(yards)
        self.is_rush = int(is_rush)
        self.is_pass = int(is_pass)
        self.is_incomplete = int(is_incomplete)
        self.is_touchdown = int(is_touchdown)
        self.is_sack = int(is_sack)
        self.is_interception = int(is_interception)
        self.is_fumble = int(is_fumble)

    @staticmethod
    def store_NFL_Data(self, fileLocations):
       
        game_data_list = [] 
        self.tree = RedBlackTree()

        for file_path in fileLocations:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    game = Nfldata(
                        game_id=row["GameId"],
                        game_date=row["GameDate"],
                        quarter=row["Quarter"],
                        offense_team=row["OffenseTeam"],
                        defense_team=row["DefenseTeam"],
                        down=row["Down"],
                        to_go=row["ToGo"],
                        yard_line=row["YardLine"],
                        season_year=row["SeasonYear"],
                        yards=row["Yards"],
                        is_rush=row["IsRush"],
                        is_pass=row["IsPass"],
                        is_incomplete=row["IsIncomplete"],
                        is_touchdown=row["IsTouchdown"],
                        is_sack=row["IsSack"],
                        is_interception=row["IsInterception"],
                        is_fumble=row["IsFumble"]
                    )
                    #game_data_list.append(game)
                    self.new_id = self.update_id(game.game_id)
                    
                    self.tree.insert(self.new_id,game.offense_team, game.defense_team, game.down,  game.yards,  
                                     game.is_rush,  game.is_pass, game.is_incomplete, game.is_touchdown, game.is_sack, game.is_interception,
                                       game.is_fumble)
                    
        #return game_data_list
    
    def update_id(self, gameID):
        self.gameID = gameID

        self.nfl_teams = {
            "ARI": 1,  # Arizona Cardinals
            "ATL": 2,  # Atlanta Falcons
            "BAL": 3,  # Baltimore Ravens
            "BUF": 4,  # Buffalo Bills
            "CAR": 5,  # Carolina Panthers
            "CHI": 6,  # Chicago Bears
            "CIN": 7,  # Cincinnati Bengals
            "CLE": 8,  # Cleveland Browns
            "DAL": 9,  # Dallas Cowboys
            "DEN": 10, # Denver Broncos
            "DET": 11, # Detroit Lions
            "GB": 12,  # Green Bay Packers
            "HOU": 13, # Houston Texans
            "IND": 14, # Indianapolis Colts
            "JAX": 15, # Jacksonville Jaguars
            "KC": 16,  # Kansas City Chiefs
            "LV": 17,  # Las Vegas Raiders
            "LAC": 18, # Los Angeles Chargers
            "LA": 19, # Los Angeles Rams
            "MIA": 20, # Miami Dolphins
            "MIN": 21, # Minnesota Vikings
            "NE": 22,  # New England Patriots
            "NO": 23,  # New Orleans Saints
            "NYG": 24, # New York Giants
            "NYJ": 25, # New York Jets
            "PHI": 26, # Philadelphia Eagles
            "PIT": 27, # Pittsburgh Steelers
            "SF": 28, # San Francisco 49ers
            "SEA": 29, # Seattle Seahawks
            "TB": 30, # Tampa Bay Bucs
            "TEN": 31, # Tennessee Titans
            "WAS": 32  # Washington Commanders
        }

        self.team_num = self.nfl_teams[self.offense_team]
        self.gameID += self.team_num
        return self.gameID
        
