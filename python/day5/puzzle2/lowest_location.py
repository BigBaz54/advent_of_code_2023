import numpy as np

def parse_input_bis(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    seeds_ranges = [int(s) for s in lines[0].split(': ')[1].split(' ')]
    seeds = []
    for i in range(0, len(seeds_ranges), 2):
        seeds.append((seeds_ranges[i], seeds_ranges[i]+seeds_ranges[i+1]-1))

    current_line = 3

    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []

    for li in [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity]:
        while lines[current_line] != '':
            [dest, source, length] = [int(x) for x in lines[current_line].split(' ')]
            li.append((dest, dest + length - 1, source, source + length - 1))
            current_line += 1
        current_line += 2

    while current_line < len(lines):
        [dest, source, length] = [int(x) for x in lines[current_line].split(' ')]
        humidity_location.append((dest, dest + length - 1, source, source + length - 1))
        current_line += 1

    return seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location

def destination_value(map_, source_value):
    for dest_start, dest_end, source_start, source_end in map_:
        if source_value >= source_start and source_value <= source_end:
            return dest_start + source_value - source_start
    return source_value

def merge_maps(a_b, b_c):
    """
    WORKING BUT USELESS XDDDDDDDDDDDDEZIFNDbezofi
    a_b: [(dest_start, dest_end, source_start, source_end)]
    b_c: [(dest_start, dest_end, source_start, source_end)]
    """
    a_b_sorted = sorted(a_b, key=lambda x: x[0])
    b_c_sorted = sorted(b_c, key=lambda x: x[2])
    a_c = []
    for (a_b_start, a_b_end, a_a_start, a_a_end) in a_b_sorted:
            for (b_c_start, b_c_end, b_b_start, b_b_end) in b_c_sorted:
                if a_b_end > b_b_start and a_b_start < b_b_end:
                    # inclusion
                    if a_b_start >= b_b_start and a_b_end <= b_b_end:
                        a_c.append((destination_value(b_c, a_b_start), destination_value(b_c, a_b_end), a_a_start, a_a_end))
                    elif a_b_start <= b_b_start and a_b_end >= b_b_end:
                        a_c.append((destination_value(b_c, b_b_start), destination_value(b_c, b_b_end), a_a_start + (b_b_start - a_b_start), a_a_start + (b_b_end - a_b_start)))
                    # intersection
                    elif a_b_start >= b_b_start:
                        a_c.append((destination_value(b_c, a_b_start), destination_value(b_c, b_b_end), a_a_start, a_a_start + (b_b_end - a_b_start)))
                    else:
                        a_c.append((destination_value(b_c, b_b_start), destination_value(b_c, a_b_end), a_a_start + (b_b_start - a_b_start), a_a_end))
    return a_c

def lowest_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location):
    source_intervals = seeds
    for map_ in [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]:
        dest_intervals = []
        # print("\n")
        # print(map_)
        while len(source_intervals) > 0:
            # print(source_intervals)
            int_start, int_end = source_intervals.pop(0)
            no_intersection = True
            for dest_start, dest_end, source_start, source_end in map_:
                # Inclusion
                if int_start >= source_start and int_end <= source_end:
                    dest_intervals.append((destination_value(map_, int_start), destination_value(map_, int_end)))
                    no_intersection = False
                    break
                elif int_start < source_start and int_end > source_end:
                    dest_intervals.append((dest_start, dest_end))
                    source_intervals.append((int_start, source_start-1))
                    source_intervals.append((source_end+1, int_end))
                    no_intersection = False
                    break
                # Intersection
                elif int_start >= source_start and int_start <= source_end:
                    dest_intervals.append((destination_value(map_, int_start), dest_end))
                    source_intervals.append((source_end+1, int_end))
                    no_intersection = False
                    break
                elif int_end >= source_start and int_end <= source_end:
                    dest_intervals.append((dest_start, destination_value(map_, int_end)))
                    source_intervals.append((int_start, source_start-1))
                    no_intersection = False
                    break
            if no_intersection:
                dest_intervals.append((int_start, int_end))
        source_intervals = dest_intervals
    return min([x[0] for x in source_intervals])
                    


if __name__ == "__main__":
    input_str = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4"
    # input_str = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n60 59 43\n\nhumidity-to-location map:\n60 56 37\n56 93 4\n47 97 9"
    seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = parse_input_bis(input_str)
    print(lowest_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location))
