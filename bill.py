
no_of_units = int(input('Enter the number of units used to calculate the bill or 0 to exit: '))


def calculate_bill(no_of_units):
    bill = 0
    rate_first_200_units = 21.8
    rate_next_800_units = 25.8
    rate_additional_units = 27.8

    if no_of_units <= 200:
        bill = rate_first_200_units * no_of_units

    elif no_of_units > 200 and no_of_units <= 1000:
        bill = (rate_first_200_units * 200) + (rate_next_800_units * (no_of_units - 200))
        
    else:
        bill = (rate_first_200_units * 200) + (rate_next_800_units * 800) + (rate_additional_units + (no_of_units - 1000))
    bill = int(round(bill, 0))
    print(f"Your bill for {no_of_units} units consumed is: {bill}")

    
while no_of_units != 0:
    if no_of_units < 0:
        print('Units cannot be negative, Please enter correct data: ')
        no_of_units = int(input('Enter the number of units used to calculate the bill or 0 to exit: '))
        continue

    calculate_bill(no_of_units)
    no_of_units = int(input('Enter the number of units used to calculate the bill or 0 to exit: '))
