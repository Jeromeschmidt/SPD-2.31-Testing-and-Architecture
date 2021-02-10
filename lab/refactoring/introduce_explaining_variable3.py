# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):

    state_value = time * temperature * pressure * COOKED_CONSTANT

    if desired_state == 'well-done' and state_value >= WELL_DONE:
        return True
    if desired_state == 'medium' and state_value >= MEDIUM:
        return True
    return False

print(is_cookeding_criteria_satisfied(100, 300, 500, 'well-done'))
