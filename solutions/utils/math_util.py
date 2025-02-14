# copied from https://github.com/RichRat/pyxercise/blob/master/util/vector.py

def greatest_common_divisor(a, b):
    if a == 0: return b
    if b == 0: return a
    if a < b:
        return greatest_common_divisor(b, a)
    return greatest_common_divisor(b, a % b)



def reversed_en(inp: list):
    for i in range(len(inp) - 1, -1, -1):
        yield i, inp[i]





# for i, n in reversed_en(['a','b','c']):
#     print(str(i) + " " + n)