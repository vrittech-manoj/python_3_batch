# for i in "AB":
#     for j in "CD":
#         print(i,",",j)


# *
# **
# ***
# ****
# *****

# assignmen
# password generator "abcd" a,b,c,d,ab,ac,ad,ba,bb,bc,bd,ca,cb,cc,cd,da,db,dc,dd


for i in range(6,1,-1):
    for j in range(i):
        print("*",end="")
    
    print("")


