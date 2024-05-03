from typing import Optional, List

from battle import Battle
from combat import calculate_melee_result
from orders import Orders, OrderType
from units import Unit

class Game:
    battle: Battle

    def __init__(self, battle: Battle):
        self.battle = battle
        
    def play_turn(self):
        self.battle.print()
        
        orders_list = []
        
        print('***** Player 1\'s turn *****')
        for unit in self.battle.player_1.units:
            orders = self.input_orders(unit)
            orders_list += orders

        self.battle.print()
        
        print('***** Player 2\'s turn *****')
        for unit in self.battle.player_2.units:
            orders = self.input_orders(unit)
            orders_list += orders
        
        print('***** Resolving melee *****')
        for orders in orders_list:
            if orders.type == OrderType.MELEE:
                result = calculate_melee_result(orders.unit, orders.target)
                print("Melee result:", result)

    def input_orders(self, unit: Unit) -> List[Orders]:
        print(unit)
        order_type = Game.input_order_type()
        
        target: Optional[Unit] = None
        if order_type in [OrderType.MELEE, OrderType.MISSILE]:
            while target is None:
                enemy_unit_id = input('Enter target unit:\n> ')
                target = self.battle.find_unit(enemy_unit_id)
    
        return [Orders(unit=unit, type=order_type, target=target)]

    @staticmethod
    def input_order_type() -> OrderType:
        while True:
            order_type = input(f'Enter an order: [move, melee, missile]\n> ')
            try:
                enum_value = OrderType[order_type.upper()]
                if enum_value is not None:
                    return enum_value
            except KeyError:
                pass