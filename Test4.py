
def con_to_faren(celsius):
    return (celsius * 9/5) + 32
temps = [30, 40, 50, 60, 70, 80, 90, 100]
fer_temp = map(con_to_faren, temps)
print(list(fer_temp))

def is_above_100(fer):
    return fer>100
above_100 = filter(is_above_100, fer_temp)
print(list(above_100))