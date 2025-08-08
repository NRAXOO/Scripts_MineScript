import minescript as ms
import time

def spamBow():
    entity = entity = ms.player_get_targeted_entity(max_distance=2)
    if entity and entity.type == "entity.minecraft.player" and tiene_bow():
        ms.player_press_use(True)
        time.sleep(0.130)
        ms.player_press_use(False)
def tiene_bow():
    hands = ms.player_hand_items()
    if hands and hands.main_hand and hands.main_hand.item:
        return "bow" in hands.main_hand.item.lower()
    return False
while True:
    spamBow()
    time.sleep(0.1)  # Prevent busy loop