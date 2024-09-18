import random
def main():
    lotteryNum = []
    for i in range(0,7):
        lotteryNum.append(random.randint(0,9))
    print('The lottery winning Numbers are: ')
    for i in range(0,len(lotteryNum)):
        print(lotteryNum[i], end =" ")
    print("\n")
main()