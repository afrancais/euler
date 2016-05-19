def roman_to_int(inp):
    """"""
    if type(inp) != type(""):
        raise TypeError, "expected string, got %s" % type(inp)
    inp = inp.upper()
    nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    ints = [1000, 500, 100, 50,  10,  5,    1]
    places = []
    for c in inp:
        if not c in nums:
            raise ValueError, "inp is not a valid roman numeral: %s" % inp
    for i in range(len(inp)):
        c = inp[i]
        value = ints[nums.index(c)]
        # If the next place holds a larger number, this value is negative.
        try:
            nextvalue = ints[nums.index(inp[i +1])]
            if nextvalue > value:
                value *= -1
        except IndexError:
            # there is no next place.
            pass
        places.append(value)
    s = 0
    for n in places: s += n
    # Easiest test for validity...
    return s


def int_to_roman(inp):
    """"""
    if type(inp) != type(1):
        raise TypeError, "expected integer, got %s" % type(inp)
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,    5,  4,    1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = int(inp / ints[i])
        result += nums[i] * count
        inp -= ints[i] * count
    return result

d = 0
f = open('roman.txt')
for roman in f:
    roman = roman.strip()
    i = roman_to_int(roman)
    print roman, roman_to_int(roman), int_to_roman(i)
    d += len(roman) - len(int_to_roman(i))

print d
