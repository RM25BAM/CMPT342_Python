""" def main():
    month = ["Janurary", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    with open ('steps.txt', 'r') as f:
            read = f.read()
            read = read.split("\n")
            n = len(read)
            num = 0
            for x in range(0, n, 28):
                if x + 27 < n:
                    num += int(read[x])
                    print(num)
                    
                    #Avg_num(sum)
                else:
                    f.close()
main() """
""" def Avg_num(sum):
    Avg = sum / 28
    Print(Avg)
def Print(Avg):   
   month = ["Janurary", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 
   for x in range (0,11):
       print(f'The average steps taken in {month[x]} was {Avg}')
   

 """


## first issues is not using the nextline to read files