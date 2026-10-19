""" """

COLORS_GROUP = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet","grey", "white"]

def value(colors):
    
    res = ""
    for i in colors:
        number = COLORS_GROUP.index(i)
        res += str(number)
        res = res[:2]
        final_res = int(res)
    return final_res
