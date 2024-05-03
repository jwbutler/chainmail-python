from enum import Enum

class UnitType(Enum):
    LIGHT_FOOT = 'LIGHT_FOOT'
    HEAVY_FOOT = 'HEAVY_FOOT'
    ARMORED_FOOT = 'ARMORED_FOOT'
    LIGHT_HORSE = 'LIGHT_HORSE'
    MEDIUM_HORSE = 'MEDIUM_HORSE'
    HEAVY_HORSE = 'HEAVY_HORSE'

class Unit:
    id: str
    type: UnitType
    count: int

    def __init__(self, id: str, type: UnitType, count: int):
        self.id = id
        self.type = type
        self.count = count

    def __str__(self):
        return f'{self.id}: {self.type.name} ({self.count})'