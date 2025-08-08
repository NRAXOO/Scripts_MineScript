import minescript as ms
import time

def mostrar_coords_entidad_vista():
    entidad = ms.player_get_targeted_entity()
    if entidad:
        pos = entidad.position
        if pos:
            ms.echo(f"Entidad vista en coords: X={pos.x:.2f}, Y={pos.y:.2f}, Z={pos.z:.2f}")
        else:
            ms.echo("Entidad sin posición disponible.")
    else:
        ms.echo("No estás mirando ninguna entidad.")

while True:
    mostrar_coords_entidad_vista()
    time.sleep(1)
