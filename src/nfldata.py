import csv

class Nfldata:
    def __init__(self, game_id, game_date, quarter, offense_team, defense_team, down, to_go, yard_line, season_year, yards, is_rush, is_pass, is_incomplete, is_touchdown, is_sack, is_interception, is_fumble):
        self.game_id = game_id
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
    def store_NFL_Data(fileLocations):
       
        game_data_list = [] 

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
                    game_data_list.append(game)

        return game_data_list
