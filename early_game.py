from player_class import PlayerClass
from user_info import User
class EarlyGame:
    def early_game(self):
       userInfo = User()
       userInfo.get_info()
       player = PlayerClass()
       player.player_class()