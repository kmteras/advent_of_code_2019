import os


def int_code_run(code):
    index = 0

    while code[index] != 99:
        if code[index] == 1:
            l = code[index + 1]
            r = code[index + 2]
            p = code[index + 3]
            code[p] = code[l] + code[r]
        elif code[index] == 2:
            l = code[index + 1]
            r = code[index + 2]
            p = code[index + 3]
            code[p] = code[l] * code[r]
        else:
            break
        index += 4
    return code


assert int_code_run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert int_code_run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert int_code_run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert int_code_run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
assert int_code_run([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

wd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(wd, 'program.txt'), 'r') as f:
    program = list(map(int, f.read().strip().split(",")))
    program[1] = 12
    program[2] = 2
    print(program)
    print(",".join(list(map(str, int_code_run(program)))))
