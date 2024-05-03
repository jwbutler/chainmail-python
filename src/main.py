from battle import Battle, Player
from game import Game
from units import Unit, UnitType

player_1 = Player(units=[
    Unit(id='1', type=UnitType.LIGHT_FOOT, count=10),
    Unit(id='2', type=UnitType.HEAVY_FOOT, count=5)
])

player_2 = Player(units=[
    Unit(id='3', type=UnitType.LIGHT_HORSE, count=5),
    Unit(id='4', type=UnitType.HEAVY_HORSE, count=5)
])

battle = Battle(player_1, player_2)
game = Game(battle)
game.play_turn()