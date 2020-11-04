salary = float(input("Vad tjänar du i månaden: "))
res_cost = float(input("Vad kostar din bostad: "))
cash = float(input("Hur stor kontoinsats: "))
loan = res_cost - cash
pound_of_flesh = 0
shylock_rate = 0.0

if loan > salary*12 or loan > (res_cost*0.85):
    print("Tyvärr kan vi inte erbjuda ett lån")
else:
    if loan > res_cost*0.7:
        shylock_rate = 0.02 * loan / 12
    elif loan >= res_cost*0.5 and loan <= res_cost*0.7:
        shylock_rate = 0.01 * loan / 12
    
    print("Lånet blir:",loan)
        
    for i in range(1,13):
           
        pound_of_flesh = loan*0.015
        loan = loan - pound_of_flesh
            
        print("Du betalar:",'%.2f'%(pound_of_flesh+shylock_rate),"KR i ränta och amortering, månad:",i)