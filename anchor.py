import minescript as ms
import time

def anchor():
    block = ms.player_get_targeted_block(4)
    if block and block.type == "minecraft:respawn_anchor[charges=0]":
        ms.player_inventory_select_slot(6)
        ms.player_press_use(True)
        time.sleep(0.1)
        ms.player_press_use(False)

while True:
    anchor()