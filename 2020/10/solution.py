input_file = '2020/10/input.txt'

adapters = [int(n) for n in open(input_file).readlines()]

def solve_part_one(adapters):
    adapter_copy = adapters.copy()
    adapter_copy.append(0)
    adapter_copy = sorted(adapter_copy)
    jolt_differences = []
    for i in range(0,len(adapter_copy)-1):
        jolt_differences.append(adapter_copy[i+1]-adapter_copy[i])
    jolt_differences.append(3)
    return jolt_differences.count(1) * jolt_differences.count(3)

def solve_part_two(adapters):
    pass

print('Part one. The number is: {}.'.format(solve_part_one(adapters)))
print('Part two. The valid number of arrangements is: {}.'.format(solve_part_two(adapters)))
