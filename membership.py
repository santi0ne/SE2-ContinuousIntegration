"""Membership Management System
This module defines membership plans and their features for a gym management system.
"""

# === Requirement 1: Membership Selection ===
# Esta estructura muestra los distintos planes, beneficios y costos.
MEMBERSHIP_PLANS = {
    "Basic": {
        "base_cost": 50,
        "features": {  # === Requirement 2: Additional Features per Membership ===
            "Group Classes": 20
        }
    },
    "Premium": {
        "base_cost": 100,
        "features": {  # === Requirement 2 ===
            "Personal Trainer": 50,
            "Spa Access": 40
        }
    },
    "Family": {
        "base_cost": 150,
        "features": {  # === Requirement 2 ===
            "Kids Zone": 30,
            "Group Classes": 20
        }
    }
}
# === Requirement 7: Membership Availability Validation ===
def is_valid_plan(plan_name):
    """Checks if the plan name exists among the available options."""
    return plan_name in MEMBERSHIP_PLANS

# === Requirement 7: Membership Availability Validation ===
def is_valid_feature(plan_name, feature):
    """Checks if a feature is available for a specific plan."""
    return feature in MEMBERSHIP_PLANS[plan_name]["features"]

# === Requirement 1 and 2: Get details of the selected plan and its extras ===
def get_plan_details(plan_name):
    """Returns the plan details if it exists, None if it does not exist (for validation)."""
    if is_valid_plan(plan_name):
        return MEMBERSHIP_PLANS[plan_name]
    return None
