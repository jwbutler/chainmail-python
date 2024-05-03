from typing import Optional, List

from units import Unit

class Player:
    units: List[Unit]

    def __init__(self, units: List[Unit]):
        self.units = units

class Battle:
    player_1: Player
    player_2: Player
    
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2

    def find_unit(self, id: str) -> Optional[Unit]:
        for player in [self.player_1, self.player_2]:
            for unit in player.units:
                if unit.id == id:
                    return unit
        return None
    
    def print(self):
        print('Player 1:')
        for unit in self.player_1.units:
            print(unit)
        
        print('Player 2:')
        for unit in self.player_2.units:
            print(unit)