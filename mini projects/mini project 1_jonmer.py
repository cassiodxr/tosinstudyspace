# 500 pesos per gram 
# 5 grams minimum 
# for every 25g may 10% discount 
# if VIP, may 5% discount capped at 5000 pesos

itemqua = float(input("\nEnter the amount in grams that you wish to buy: "))
if itemqua < 5.0:
    print("5 grams is the minimum purchase.")
else:
    if itemqua >= 25:
        gramcheck = itemqua // 25 # check every 25 grams
        leftovergram = itemqua % 25 # the grams that aren't discounted 
        
        ogprice = itemqua * 500 # price kung walang 10% discount
        discountprice = gramcheck * 12500 * 0.9 # apply 10% discount, yung 12500 = price ng 25g
        leftoverprice = leftovergram * 500
        
        fullprice = discountprice + leftoverprice # add discounted price + leftover price 
        VIP = input("\nAre you a VIP customer????? (y/n) ")
        if VIP.lower() == "y":
            VIPcheck = fullprice * 0.05 # check muna discount if lalagpas 5000
            if VIPcheck >= 5000: # if lagpas 5000:
                fullprice -= 5000 # subtract fixed discount
            else:
                fullprice -= VIPcheck # if di lagpas 5000 ang discount, apply 5% discount
        
        print("\nPrice before the discount is applied for every 25g purchased:",ogprice,"pesos")
            
    else: # if purchase is less than 25 grams
        fullprice = itemqua * 500
        VIP = input("\nAre you a VIP customer????? (y/n) ")
        if VIP.lower() == "y":
            VIPcheck = fullprice * 0.05 # check muna discount if lalagpas 5000
            if VIPcheck >= 5000: # if lagpas 5000:
                fullprice -= 5000 # subtract fixed discount
            else:
                fullprice -= VIPcheck # if di lagpas 5000 ang discount, apply 5% discount
                
    print("Final price:",fullprice,"pesos")
