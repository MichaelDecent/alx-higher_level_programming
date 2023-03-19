#!/usr/bin/python3
def weight_average(my_list=[]):
    if (!my_list):
        return (0)
    tup_sum, tup_avg = 0, 0
    for tup in my_list:
        tup_sum += (tup[0] * tup[1])
        tup_avg += tup[1]

    return (tup_sum / tup_avg)
