from lowest_location import parse_input_bis, lowest_location
import time

if __name__ == "__main__":
    start = time.time()
    with open('my_input.txt', 'r') as f:
        input_str = f.read()
    seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = parse_input_bis(input_str)
    ll = lowest_location(seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location)
    end = time.time()
    print(f"Time P2: {end-start}")
    print(ll)