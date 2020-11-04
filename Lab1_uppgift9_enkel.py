salary = float(input("Vad tjänar du i månaden: "))
res_cost = float(input("Vad kostar din bostad: "))
cash = float(input("Hur stor kontoinsats: "))
loan = res_cost - cash
pound_of_flesh = 0

if loan > salary*12 or loan > (res_cost*0.85):
    print("Tyvärr kan vi inte erbjuda ett lån")
else:
    print("Lånet blir:",loan)
    
    for i in range(1,13):
        
        pound_of_flesh = loan*0.015
        loan = loan - pound_of_flesh
        
        print("Du betalar:",'%.2f'%pound_of_flesh,"KR i ränta, månad:",i)