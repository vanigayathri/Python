def maxTrailing(b, d, a):
    # b : price of each doodad in cents
    # d : desired trailing digit
    # a : Maximum price of bundle
    maxMultiplier = int(a / b); 
    maxcount = 0
    k = 1
    while (k <= maxMultiplier):
        result = b * k
        if str(d) in str(result):
            count = trailing(d, result)
            if maxcount < count:
                maxcount = count
        k += 1
    return maxcoundef maxTrailing(b, d, a):
    # b : price of each doodad in cents
    # d : desired trailing digit
    # a : Maximum price of bundle
    maxMultiplier = int(a / b);
    maxcount = 0
    k = 1
    while (k <= maxMultiplier):
        result = b * k
        if str(d) in str(result):
            count = trailing(d, result)
            if maxcount < count:
                maxcount = count
        k += 1
    return maxcount