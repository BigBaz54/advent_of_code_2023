from predict_prev import predict_prev, parse_input
import time


with open('my_input.txt', 'r') as f:
    input_str = f.read()
start = time.perf_counter()
pi = parse_input(input_str)
s = 0
for seq in pi:
    s += predict_prev(seq)
print(time.perf_counter() - start)
print(s)