def final_distance(race_time, hold_time):
    return hold_time*(race_time-hold_time)

def ways_to_beat_record(race_time, race_record):
    a = 0
    b = race_time//2
    while a < b:
        m = (a + b)//2
        if final_distance(race_time, m) > race_record:
            b = m
        elif final_distance(race_time, m) < race_record:
            a = m + 1
        else:
            break
    min_hold_time = a
    return race_time - 2*min_hold_time + 1

if __name__=="__main__":
    print(ways_to_beat_record(7, 9))
    