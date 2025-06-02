from membership import get_plan_details
from calculator import calculate_total_cost


def main():
    # === Requisito 8: User Confirmation ===
    plan_name = input("Seleccione plan (Basic, Premium, Family): ")
    plan = get_plan_details(plan_name)

    # === Requisito 10: Error Handling (plan inválido) ===
    if not plan:
        print("Plan no válido.")
        return -1  # === Requisito 9: Return -1 si la entrada no es válida ===

    selected_features = []
    print("Características disponibles:")
    for f in plan["features"]:
        ans = input(f"¿Desea añadir '{f}' por ${plan['features'][f]}? (s/n): ")
        if ans.lower() == 's':
            selected_features.append(f)

    # === Requisito 10: Error Handling (entrada no es numérica) ===
    try:
        group_members = int(input("¿Cuántas personas se registran juntas?: "))
    except ValueError:
        print("Número no válido.")
        return -1  # === Requisito 9: Return -1 si hay error de entrada ===

    plan["name"] = plan_name  # necesario para aplicar lógica de premium
    total = calculate_total_cost(plan, selected_features, group_members)

    # === Requisito 8: Mostrar resumen de selección al usuario ===
    print(f"\nResumen del plan:")
    print(f"Plan: {plan_name}")
    print(f"Características: {', '.join(selected_features) if selected_features else 'Ninguna'}")
    print(f"Miembros: {group_members}")
    print(f"Total a pagar: ${total}")

    confirm = input("¿Desea confirmar su membresía? (s/n): ")
    if confirm.lower() == 's':
        print("¡Membresía registrada con éxito!")
        return total  # === Requisito 9: Return de costo si se confirma
    else:
        print("Membresía cancelada.")
        return -1  # === Requisito 9: Return -1 si se cancela
    