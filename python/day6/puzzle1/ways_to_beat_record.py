def final_distance(race_time, hold_time):
    return hold_time*(race_time-hold_time)

def ways_to_beat_record(race_time, race_record):
    min_hold_time = race_record + 1
    for hold_time in range(race_time + 1):
        if final_distance(race_time, hold_time) > race_record:
            min_hold_time = hold_time
            break
    return race_time - 2*min_hold_time + 1

if __name__=="__main__":
    print(ways_to_beat_record(7, 9))
    