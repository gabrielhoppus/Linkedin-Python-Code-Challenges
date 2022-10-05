"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures. """


def make_readable(seconds):
    hh = 0
    mm = 0
    ss = 0
    if seconds > 359999:
        raise Exception
    else:
        if seconds >= 3600:
            hh = (seconds//3600)
            if (seconds%3600) >= 60:
                seconds = (seconds%3600)
                mm = (seconds//60)
                ss = (seconds%60)
            else:
                ss = (seconds%3600)
        elif seconds >= 60:
            hh = 0
            mm = (seconds//60)
            ss = (seconds%60)
        else:
            hh = 0
            mm = 0
            ss = seconds
        
        return "{}:{}:{}".format(str(hh).zfill(2), str(mm).zfill(2), str(ss).zfill(2))



