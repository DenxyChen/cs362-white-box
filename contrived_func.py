def contrived_func(val):
    # This function serves no logical purpose
    # DO NOT try to make sense of it!
    # Just make sure your tests cover everything requested
    # val is a numerical value
    if 150 > val > 100:  # T: val in [101, 149], F: val >= 151 or val <= 99
        return True
    # 1: T if val <= 72
    # 2: T if val <= 48
    # Truth pairs: (T, T), (T, F), (F, T/F)
    elif val * 5 < 361 and val / 2 < 24:
        if val == 6:
            return False
        else:
            return True
    # 1-1: T if val > 75
    # 1-2: T if val < 80
    # 1: always T
    # 2: T if val == 5
    elif (val > 75 or val / 8 < 10) and val ** val % 5 == 0:
        return True
    else:
        return False
