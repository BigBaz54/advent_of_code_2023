def calibration_value_extended(line: str) -> int:
    """
    Returns the calibration value from the given line, acceping also the digits as letters.
    :param line: The line to parse.
    """
    used_letters = "onetwhrfuivsxg"
    digits_as_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    buffer = ""

    first_digit = -1
    last_digit = -1

    for c in line:
        if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if first_digit == -1:
                first_digit = int(c)
            last_digit = int(c)
            buffer = ""
        else:
            if c not in used_letters:
                buffer = ""
            else:
                buffer += c
                for s in digits_as_letters:
                    if buffer.endswith(s):
                        if first_digit == -1:
                            first_digit = digits_as_letters.index(s) + 1
                        last_digit = digits_as_letters.index(s) + 1
                        buffer = buffer[-1]
                        break
    
    return 10 * first_digit + last_digit

if __name__ == "__main__":
    assert(calibration_value_extended("1oujgi0one") == 11)
    assert(calibration_value_extended("two") == 22)
    assert(calibration_value_extended("two2") == 22)
    assert(calibration_value_extended("aztzthreeaz23a5eighthreeaa") == 33)
