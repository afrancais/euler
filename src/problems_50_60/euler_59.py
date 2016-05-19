import itertools

f = open("cipher1.txt")

l = f.readline()

numbers = l.split(',')



for a in range(ord('a'), ord('z') + 1):
    for b in range(ord('a'), ord('z') + 1):
        for c in range(ord('a'), ord('z') + 1):
            i = 0
            acc = 0
            st = ''
            for l in itertools.cycle((a, b, c)):
                if i == len(numbers):
                    break
                r = int(numbers[i]) ^ l
                acc += r
                st += chr(r)
                i += 1

            if 'the' in st.lower():
                print st
                print acc
                toto = raw_input()
