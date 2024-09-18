def main():
    try:
        sales = []
        daysWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        for i in range(0,len(daysWeek)):
            user = int(input(f'Enter the sales for {daysWeek[i]}: '))
            if(user < 0):
                continue
            else:
                sales.append(user)
        Sum = sum(sales)
        print(f'Total sales for the week: ${Sum:,.2f}')
    except ValueError:
        print('Has to be an number.')
main()