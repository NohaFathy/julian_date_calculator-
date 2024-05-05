import datetime

def get_julian_datetime(date):
    """
    Convert a datetime object into Julian float.
    Args:
        date: datetime-object of date in question

    Returns: float - Julian calculated datetime.
    Raises: 
        TypeError : Incorrect parameter type
        ValueError: Date out of range of equation
    """
    # Ensure correct format
    if not isinstance(date, datetime.datetime):
        raise TypeError('Invalid type for parameter "date" - expecting datetime')
    elif date.year < 1801 or date.year > 2099:
        raise ValueError('Datetime must be between year 1801 and 2099')

    # Perform the calculation
    j0 = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int(
        (275 * date.month) / 9.0) + date.day + 1721013.5 
    t0 = (j0 - 2451545) / 36525
    θG0 = 100.4606184 + 36000.77004 * t0 + 0.000387933 * t0**2 - 2.583e-8 * t0**3
    UT = 4 + (30 / 60) + (0 / 3600)  # Given time 4:30:00
    θG = θG0 + (360 * UT / 24)
    longitude_tokyo = 139.80
    θ = θG + longitude_tokyo
    θ = θ % 360  # Ensure θ is within the range [0, 360)

    if θ >= 360:
        θ -= 360

    return θ

def main():
    # Example usage
    input_date = datetime.datetime(2004, 3, 3, 0, 0, 0)  # March 3, 2004
    try:
        result = get_julian_datetime(input_date)
        print("Local Sidereal Time in Tokyo:", result)
    except (TypeError, ValueError) as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

