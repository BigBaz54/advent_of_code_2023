import calibration_value

if __name__ == "__main__":
    with open("my_input.txt", "r") as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        sum += calibration_value.calibration_value(line)
    print(sum)