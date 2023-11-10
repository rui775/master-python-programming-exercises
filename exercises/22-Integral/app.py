def generate_dict(n):
    integer_dict = dict()
    for i in range(1, n+1):
        integer_dict[i] = i * i
    return integer_dict

print(generate_dict(4))