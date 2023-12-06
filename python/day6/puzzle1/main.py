from ways_to_beat_record import ways_to_beat_record

if __name__=="__main__":
    w = 1
    for race in [(53, 250), (91, 1330), (67, 1081), (68, 1025)]:
        w *= ways_to_beat_record(race[0], race[1])
    print(w)