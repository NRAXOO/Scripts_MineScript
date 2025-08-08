import minescript as ms
import time

def cyrstal():
    block = ms.player_get_targeted_block(2)
    if block and block.type == "minecraft:obsidian" and tiene_crystal():
        ms.player_press_use(True)
        time.sleep(0.05)
        ms.player_press_use(False)
        ms.player_press_attack(True)
        time.sleep(0.05)
        ms.player_press_attack(False)

def tiene_crystal():
    hands = ms.player_hand_items()
    if hands and hands.main_hand and hands.main_hand.item:
        return "end_crystal" in hands.main_hand.item.lower()
    return False
while True:
    cyrstal()
    time.sleep(0.1)  # Prevent busy loop