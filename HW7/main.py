#title 2022 Weekly Gas Prices
#Average Prices
#Weeks (by number)

import matplotlib.pyplot as plt
import csv
def main():
  
 
    X = []
    Y = []
 
    with open('/Users/natashapiedrabuena/Desktop/Python class/HW7/weekly_gas_averages_2022.txt', 'r') as datafile:
        for week_number, line in enumerate(datafile, start=1):  #I put start=1 so it wont append 0 since 0 weeks doesnt exist
            price = float(line.strip())  
            X.append(week_number)
            Y.append(price)
    plt.plot(X, Y)
    plt.title('2022 Weekly Gas Prices')
    plt.xlabel('Weeks (by number)') 
    plt.ylabel('Average Prices')  
    plt.xlim(1, 52)
    plt.show()
main()