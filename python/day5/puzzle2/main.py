from lowest_location import parse_input_bis, lowest_location

if __name__ == "__main__":
    with open('my_input.txt', 'r') as f:
        input_str = f.read()
    seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = parse_input_bis(input_str)
    ll = lowest_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location)
    print(ll)