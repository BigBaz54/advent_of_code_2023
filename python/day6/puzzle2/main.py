from ways_to_beat_record import ways_to_beat_record
import time

if __name__=="__main__":
    start = time.perf_counter()
    print(ways_to_beat_record(53916768, 250133010811025))
    end = time.perf_counter()
    print(end - start)