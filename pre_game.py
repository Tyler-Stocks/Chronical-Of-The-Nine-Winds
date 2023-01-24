from player_class import PlayerClass
from user_info import User
from tavern import Tavern

class EarlyGame:
    def early_game(self):
       userInfo = User()
       userInfo.get_info()
       player = PlayerClass()
       player.player_class()
       tavern = Tavern()
       tavern.tavern()

earlygame = EarlyGame()

earlygame.early_game