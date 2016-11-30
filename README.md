## Time until next power-of-two birthday

Given your birthday and a base (e.g. 2 for binary),
compute the next date your age is an integral power of the base
when measured in days.

For instance, when run on November 30, 2016 by someone whose birthday is March 28, 1985:

```
$ python round.py 1985-03-28 10
You are 999648000 seconds old and will be 10**9 seconds on 2016-12-04
You are 999648000000000 microseconds old and will be 10**15 microseconds on 2016-12-04
You are 999648000000 milliseconds old and will be 10**12 milliseconds on 2016-12-04
You are 277680 hours old and will be 10**6 hours on 2099-04-25
You are 16660800 minutes old and will be 10**8 minutes on 2175-05-15
You are 1653 weeks old and will be 10**4 weeks on 2176-11-21
You are 11570 days old and will be 10**5 days on 2259-01-11
```
