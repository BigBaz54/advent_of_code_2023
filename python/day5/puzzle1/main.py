from lowest_location import parse_input, seed_to_location

if __name__ == "__main__":
    with open('my_input.txt', 'r') as f:
        input_str = f.read()
    seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = parse_input(input_str)
    seed_locations = seed_to_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location)
    print(min(seed_locations, key=lambda x: x[1])[1])