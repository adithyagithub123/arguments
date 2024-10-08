def total_calc(bill_amount , tip_perc):
    total = bill_amount * ( 1 + 0.01 * tip_perc )
    total = round(total , 2)
    print(f"pls pay ${total}")

x = float(input("Enter the bill amount : "))
y = float(input("Enter the tip percentage : "))

total_calc( x , y )