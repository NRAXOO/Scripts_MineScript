import minescript as ms
import time
import math

# Ajusta este valor según el alcance que quieras permitir (en bloques).
ATTACK_RANGE = 3.0

def tiene_hacha():
    hands = ms.player_hand_items()
    if hands and hands.main_hand and hands.main_hand.item:
        return "axe" in hands.main_hand.item.lower()
    return False

def distancia(a, b):
    """Calcula distancia euclidiana entre dos tuplas/listas (x,y,z)."""
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def playerAttack():
    try:
        entity = ms.player_get_targeted_entity(max_distance=20)
        if not entity:
            ms.player_press_attack(False)
            return

        # Solo nos interesan otros jugadores
        if entity.type != "entity.minecraft.player":
            ms.player_press_attack(False)
            return

        # Obtener posición del jugador local y del objetivo
        local = ms.player()
        if not local or not hasattr(local, "position") or not entity.position:
            ms.player_press_attack(False)
            return

        dist = distancia(local.position, entity.position)

        # Solo atacar si dentro del rango definido y tenemos un hacha
        if dist <= ATTACK_RANGE and tiene_hacha():
            # Primer clic
            ms.player_press_attack(True)
            time.sleep(0.05)

            # Seleccionar slot 3 (índice 2)
            ms.player_inventory_select_slot(2)

            # Segundo clic
            ms.player_press_attack(True)
            time.sleep(0.05)
            ms.player_press_attack(False)

            ms.echo(f"Atacado {entity.name} a distancia {dist:.2f}")
            # pequeño retardo tras la acción para evitar spam/overlap
            time.sleep(0.1)
        else:
            ms.player_press_attack(False)

    except Exception as e:
        ms.log("Error en playerAttack:", e)
        ms.player_press_attack(False)

if __name__ == "__main__":
    ms.echo("Auto-attack por distancia iniciado (rango = " + str(ATTACK_RANGE) + " bloques)")
    while True:
        playerAttack()
