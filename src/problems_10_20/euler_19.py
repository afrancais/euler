from datetime import datetime


def run():
    cpt = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if m < 10:
                m = '0%d' % m
            d = datetime.strptime('01/%s/%s' % (m, y), '%d/%m/%Y')

            if d.weekday() == 6:
                print(d.strftime('%d/%m/%Y'))
                print(d.strftime('%a'))
                cpt += 1

    print(d.strftime('%d/%m/%Y'))
    print(cpt)
