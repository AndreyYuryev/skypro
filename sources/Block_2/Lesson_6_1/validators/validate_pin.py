def validate_pin(pin_code):
    if len(pin_code) == 4 and pin_code.isdigit():
        return True
    return False