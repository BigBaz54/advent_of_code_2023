def calibration_value(line: str) -> int:
    """
    Returns the calibration value from the given line.
    :param line: The line to parse.
    """
    first_digit = -1
    last_digit = -1
    for c in line:
        if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if first_digit == -1:
                first_digit = c
            last_digit = c
    return 10 * int(first_digit) + int(last_digit)

if __name__ == "__main__":
    print(calibration_value("1oujgi0"))
    print(calibration_value("1"))
    print(calibration_value("22"))
    print(calibration_value("33a"))
