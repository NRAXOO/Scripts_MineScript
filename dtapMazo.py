import minescript as ms
import time

def cyrstal():
    entity = entity = ms.player_get_targeted_entity(max_distance=3)
    if entity and entity.type == "entity.minecraft.player" and tiene_Mazo():
        ms.player_press_use(True)
        time.sleep(0.130)
        ms.player_press_use(False)

#funcion a usar player_inventory_select_slot
def tiene_Mazo():
    hands = ms.player_hand_items()
    if hands and ms.player_inventory_slot() == 8 and hands.main_hand and hands.main_hand.item:
        ms.echo(f"Item in main hand: {hands.main_hand.item}")
        return "mace" in hands.main_hand.item.lower()
    return False
while True:
    cyrstal()
    time.sleep(0.1)  # Prevent busy loop