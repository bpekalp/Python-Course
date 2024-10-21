def convertToCm(_feet, _inches):
    """Converts feet inches to centimeters.

    Args:
        feet (float): Feet.
        inches (float): Inches.

    Returns:
        float: Returns feet inches in centimeters.
    """
    cm = _feet * 30.48 + _inches * 2.54
    return cm
