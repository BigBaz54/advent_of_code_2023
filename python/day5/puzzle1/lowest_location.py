def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    seeds = [int(s) for s in lines[0].split(': ')[1].split(' ')]
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
            li.append([int(x) for x in lines[current_line].split(' ')])
            current_line += 1
        current_line += 2

    while current_line < len(lines):
        humidity_location.append([int(x) for x in lines[current_line].split(' ')])
        current_line += 1

    return seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location

def destination_value(map_, source_value):
    for i in range(len(map_)):
        if source_value >= map_[i][1] and source_value < map_[i][1] + map_[i][2]:
            return map_[i][0] + source_value - map_[i][1]
    return source_value

def seed_to_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location):
    locations = []
    for seed in seeds:
        soil = destination_value(seed_soil, seed)
        fertilizer = destination_value(soil_fertilizer, soil)
        water = destination_value(fertilizer_water, fertilizer)
        light = destination_value(water_light, water)
        temperature = destination_value(light_temperature, light)
        humidity = destination_value(temperature_humidity, temperature)
        location = destination_value(humidity_location, humidity)
        locations.append((seed, location))
    return locations


if __name__ == "__main__":
    input_str = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4"
    seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = parse_input(input_str)
    print(seed_to_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location))

