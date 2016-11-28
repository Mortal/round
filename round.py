import argparse
from math import log, ceil
from datetime import date, datetime, timedelta


def parse_date(s):
    """
    >>> print(parse_date('1991-11-15'))
    1991-11-15 00:00:00
    """
    return datetime.strptime(s, '%Y-%m-%d').date()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date', type=parse_date)
    parser.add_argument('base', type=float)
    args = parser.parse_args()

    units = ['days', 'seconds', 'microseconds', 'milliseconds', 'minutes',
             'hours', 'weeks']

    now = date.today()

    td = now - args.date
    base = [timedelta(**{u: 1}) for u in units]
    age = [td / b for b in base]
    exponent = [ceil(log(v, args.base)) for v in age]
    dt = [args.date + args.base ** e * b for e, b in zip(exponent, base)]
    for i in sorted(range(len(units)), key=lambda i: dt[i]):
        if dt[i] == now:
            print("You are %.0f %s old. " % (age[i], units[i]) +
                  "Happy birth%s!" % units[i][:-1])
        else:
            print("You are %.0f %s old " % (age[i], units[i]) +
                  "and will be %g**%d " % (args.base, exponent[i]) +
                  "%s on %s" % (units[i], dt[i]))


if __name__ == "__main__":
    main()
