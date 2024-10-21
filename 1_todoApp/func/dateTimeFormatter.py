import time

# %Y  Year with century as a decimal number.
# %m  Month as a decimal number [01,12].
# %d  Day of the month as a decimal number [01,31].
# %H  Hour (24-hour clock) as a decimal number [00,23].
# %M  Minute as a decimal number [00,59].
# %S  Second as a decimal number [00,61].
# %z  Time zone offset from UTC.
# %a  Locale's abbreviated weekday name.
# %A  Locale's full weekday name.
# %b  Locale's abbreviated month name.
# %B  Locale's full month name.
# %c  Locale's appropriate date and time representation.
# %I  Hour (12-hour clock) as a decimal number [01,12].
# %p  Locale's equivalent of either AM or PM.


def formatDateTime():
    """Calculates current date and time and returns a formatted string.

    Returns:
        str: Returns a formatted string to greet the users.
    """
    dateTime = time.strftime("%B %d, %Y - %H:%M:%S")
    message = f"Hello! It's {dateTime}"
    return message
