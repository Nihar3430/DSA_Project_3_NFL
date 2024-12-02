from redBlackTree import RedBlackTree
import ProjectUI
from hashmap import HashMap
from nfldata import Nfldata


files = ["Database/2023_Database.csv", "Database/2022_Database.csv", "Database/2021_Database.csv" ]

Nfldata.store_NFL_Data(files)



mock = Nfldata.tree.search(2022091126)

print(mock.game_id, mock.offense, mock.yards)



