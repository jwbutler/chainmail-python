from enum import Enum
from typing import Optional
from units import Unit

class OrderType(Enum):
    MOVE = 'MOVE'
    MELEE = 'MELEE'
    MISSILE = 'MISSILE'

class Orders:
    unit: Unit
    type: OrderType
    target: Optional[Unit]
    
    def __init__(self, unit: Unit, type: OrderType, target: Optional[Unit]):
        self.unit = unit
        self.type = type
        self.target = target
        
    def __str__(self):
        return f'{self.unit.id}: {self.type.name} -> {self.target.id if self.target else None}'