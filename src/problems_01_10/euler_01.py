
def is_multiple_of(value, *possibles):
    return any(value % p == 0 for p in possibles)


def run(m):
    return sum(i for i in range(1, m) if is_multiple_of(i, 3, 5))

if __name__ == '__main__':
    run(1000)
