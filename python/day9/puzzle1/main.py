from predict_next import predict_next, parse_input


with open('my_input.txt', 'r') as f:
    input_str = f.read()
pi = parse_input(input_str)
s = 0
for seq in pi:
    s += predict_next(seq)
print(s)