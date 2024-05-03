from random import randint
from math import floor
from typing import List

from units import Unit, UnitType

# TODO - assume no floating point errors
# Usage: number of dice rolled = DICE_ROLLED_TABLE[attacker_type][defender_type] * attacker_count 
DICE_ROLLED_TABLE = {
    UnitType.LIGHT_FOOT: {
        UnitType.LIGHT_FOOT: 1,
        UnitType.HEAVY_FOOT: 1/2,
        UnitType.ARMORED_FOOT: 1/3,
        UnitType.LIGHT_HORSE: 1/2,
        UnitType.MEDIUM_HORSE: 1/3,
        UnitType.HEAVY_HORSE: 1/4
    },
    UnitType.HEAVY_FOOT: {
        UnitType.LIGHT_FOOT: 1,
        UnitType.HEAVY_FOOT: 1,
        UnitType.ARMORED_FOOT: 1/2,
        UnitType.LIGHT_HORSE: 1/2,
        UnitType.MEDIUM_HORSE: 1/3,
        UnitType.HEAVY_HORSE: 1/4
    },
    UnitType.ARMORED_FOOT: {
        UnitType.LIGHT_FOOT: 1,
        UnitType.HEAVY_FOOT: 1,
        UnitType.ARMORED_FOOT: 1,
        UnitType.LIGHT_HORSE: 1,
        UnitType.MEDIUM_HORSE: 1/2,
        UnitType.HEAVY_HORSE: 1/3
    },
    UnitType.LIGHT_HORSE: {
        UnitType.LIGHT_FOOT: 1,
        UnitType.HEAVY_FOOT: 1,
        UnitType.ARMORED_FOOT: 1,
        UnitType.LIGHT_HORSE: 1,
        UnitType.MEDIUM_HORSE: 1/2,
        UnitType.HEAVY_HORSE: 1/3
    },
    UnitType.MEDIUM_HORSE: {
        UnitType.LIGHT_FOOT: 1,
        UnitType.HEAVY_FOOT: 1,
        UnitType.ARMORED_FOOT: 1,
        UnitType.LIGHT_HORSE: 1,
        UnitType.MEDIUM_HORSE: 1/2,
        UnitType.HEAVY_HORSE: 1/3
    },
    UnitType.HEAVY_HORSE: {
        UnitType.LIGHT_FOOT: 4,
        UnitType.HEAVY_FOOT: 3,
        UnitType.ARMORED_FOOT: 2,
        UnitType.LIGHT_HORSE: 2,
        UnitType.MEDIUM_HORSE: 1,
        UnitType.HEAVY_HORSE: 1
    }
}

MIN_DICE_VALUE_FOR_KILL_TABLE = {
    UnitType.LIGHT_FOOT: {
        UnitType.LIGHT_FOOT: 6,
        UnitType.HEAVY_FOOT: 6,
        UnitType.ARMORED_FOOT: 6,
        UnitType.LIGHT_HORSE: 6,
        UnitType.MEDIUM_HORSE: 6,
        UnitType.HEAVY_HORSE: 6
    },
    UnitType.HEAVY_FOOT: {
        UnitType.LIGHT_FOOT: 5,
        UnitType.HEAVY_FOOT: 6,
        UnitType.ARMORED_FOOT: 6,
        UnitType.LIGHT_HORSE: 6,
        UnitType.MEDIUM_HORSE: 6,
        UnitType.HEAVY_HORSE: 6
    },
    UnitType.ARMORED_FOOT: {
        UnitType.LIGHT_FOOT: 4,
        UnitType.HEAVY_FOOT: 5,
        UnitType.ARMORED_FOOT: 6,
        UnitType.LIGHT_HORSE: 6,
        UnitType.MEDIUM_HORSE: 6,
        UnitType.HEAVY_HORSE: 6
    },
    UnitType.LIGHT_HORSE: {
        UnitType.LIGHT_FOOT: 5,
        UnitType.HEAVY_FOOT: 6,
        UnitType.ARMORED_FOOT: 6,
        UnitType.LIGHT_HORSE: 6,
        UnitType.MEDIUM_HORSE: 6,
        UnitType.HEAVY_HORSE: 6
    },
    UnitType.MEDIUM_HORSE: {
        UnitType.LIGHT_FOOT: 4,
        UnitType.HEAVY_FOOT: 5,
        UnitType.ARMORED_FOOT: 6,
        UnitType.LIGHT_HORSE: 5,
        UnitType.MEDIUM_HORSE: 6,
        UnitType.HEAVY_HORSE: 6
    },
    UnitType.HEAVY_HORSE: {
        UnitType.LIGHT_FOOT: 5,
        UnitType.HEAVY_FOOT: 5,
        UnitType.ARMORED_FOOT: 5,
        UnitType.LIGHT_HORSE: 5,
        UnitType.MEDIUM_HORSE: 5,
        UnitType.HEAVY_HORSE: 6
    },
}

class MeleeResult:
    attacker_dice_rolls: List[int]
    defender_dice_rolls: List[int]
    attacker_casualties: int
    defender_casualties: int
    
    def __init__(
        self,
        attacker_dice_rolls: List[int],
        defender_dice_rolls: List[int],
        attacker_casualties: int,
        defender_casualties: int
    ):
        self.attacker_dice_rolls = attacker_dice_rolls
        self.defender_dice_rolls = defender_dice_rolls
        self.attacker_casualties = attacker_casualties
        self.defender_casualties = defender_casualties
        
    def __str__(self):
        return f'Attacker dice rolls: {self.attacker_dice_rolls}, Defender dice rolls: {self.defender_dice_rolls}, Attacker casualties: {self.attacker_casualties}, Defender casualties: {self.defender_casualties}'

def calculate_melee_result(attacker: Unit, defender: Unit) -> MeleeResult:
    attacker_dice_rolls = roll_dice(attacker, defender)
    defender_dice_rolls = roll_dice(defender, attacker)
    defender_casualties = get_kills(attacker_dice_rolls, attacker, defender)
    attacker_casualties = get_kills(defender_dice_rolls, defender, attacker)
    return MeleeResult(
        attacker_dice_rolls,
        defender_dice_rolls,
        attacker_casualties,
        defender_casualties
    )

def roll_dice(attacker: Unit, defender: Unit) -> List[int]:
    # TODO check rounding
    num_dice = floor(DICE_ROLLED_TABLE[attacker.type][defender.type] * attacker.count)
    return [randint(1, 6) for _ in range(num_dice)]

def get_kills(dice_rolled: List[int], attacker: Unit, defender: Unit) -> int:
    kills = 0
    for roll in dice_rolled:
        if roll >= MIN_DICE_VALUE_FOR_KILL_TABLE[attacker.type][defender.type]:
            kills += 1
    return kills