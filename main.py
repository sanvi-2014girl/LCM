def compute_lcm(x,y):
    if x > y:
        greater = x
    else: greater = y
    while(True):
        if ((greater%x == 0)and(greater%y == 0)):
            lcm = greater
            break
        greater +=1
        return lcm
    number = 2
    number2 = 4
    print("The LCM is",compute_lcm(number,number2))