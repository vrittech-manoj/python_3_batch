cp = int(input("Enter cost price#>>>"))
sp = int(input("Enter shelling price#>>>"))

def calculate_bonus(percentage_number,cost_price):
    bonus = percentage_number/100*cost_price 
    return bonus
#if profit then return 5 % of cp as bonus
#if loss then must add 20% of cp as bonus
if sp>cp:
    profit = sp-cp 
    bonus = calculate_bonus(5,cp)
    total_ammount = profit +  bonus
elif cp>sp:
    loss = cp - sp
    bonus = calculate_bonus(20,cp)
    total_ammount = loss +  bonus

print("total ammount becomes : ",total_ammount)





