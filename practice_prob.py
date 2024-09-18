# what if i use rand seed then set for range 0-100
""" import random
def main():
    num0, num1, num2, num3, num4, num5, num6, num7, num8, num9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    int_list = []
    for i in range (0,100):
        int_list.append(random.randint(0,9))
    for i in range(len(int_list)):
        if int_list[i] == 0:
            num0 += 1
        elif int_list[i] == 1:
            num1 += 1
        elif int_list[i] == 2:
            num2 += 1
        elif int_list[i] == 3:
            num3 += 1
        elif int_list[i] == 4:
            num4 += 1
        elif int_list[i] == 5:
            num5 += 1  
        elif int_list[i] == 6:
            num6 += 1
        elif int_list[i] == 7:
            num7 += 1
        elif int_list[i] == 8:
            num8 += 1
        elif int_list[i] == 9:
            num9 += 1
    occurance = [num0,num1,num2,num3,num4,num5,num6,num7,num8,num9]
    for i in range(0,9):
        print(f"{i} appears {occurance[i]} times") 

main() """