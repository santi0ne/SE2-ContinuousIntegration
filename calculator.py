"""
Clase calculator
"""
def calculate_total_cost(plan, features, group_members=1):
    """metodo para calcular total de costos del plan

    Args:
        plan (String): plan escogido actual del cliente
        features (String): que ofrece el plan actual
        group_members (int, optional): Cuantos miembros hay en ese plan. Defaults to 1.

    Returns:
        _type_: _description_
    """    # === Requirement 3: Base Membership Cost ===
    base_cost = plan["base_cost"]

    # === Requirement 3: Additional Features Cost ===
    feature_cost = sum(plan["features"][f] for f in features)

    # === Requirement 3: Total Membership Cost (base + extras) ===
    subtotal = base_cost + feature_cost

    # === Requirement 6: Premium Membership Features surcharge (15%) ===
    # Applies only if the plan name includes "Premium"
    if "Premium" in plan.get("name", ""):
        subtotal *= 1.15

    # === Requirement 4: Group Membership Discount (10%) ===
    if group_members >= 2:
        subtotal *= 0.90  # 10% discount for 2 or more people

    # === Requirement 5: Special Offer Discounts ===
    if subtotal > 400:
        subtotal -= 50  # $50 discount if total > $400
    elif subtotal > 200:
        subtotal -= 20  # $20 discount if total > $200

    # === Requirement 9: Return a positive integer total ===
    return int(round(subtotal))  # Final amount rounded and returned as an integer
