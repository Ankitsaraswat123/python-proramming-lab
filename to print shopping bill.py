if x>=25000:
    a=x-(x*0.25)
    print("__________________________________________")
    print("            CATEGORY: GOLD.        \n")
    print("25% DISCOUNT RECIEVED=",(x*0.25))
    print(" Total amount to pay =", a, '\n')
    print(" Thank you.")
    print("___________________________________________")



elif x>=10000 and x<25000:
    a=x-(x*0.1)
    print("__________________________________________")
    print("            CATEGORY: SILVER.        \n")
    print(" 10% DISCOUNT RECIEVED=",(x*0.1))
    print(" Total amount to pay =", a, '\n')
    print(" Thank you.")
    print("___________________________________________")

else: 
    a=x-(x*0.05)
    print("__________________________________________")
    print("            CATEGORY: BRONZE.        \n")
    print("5% DISCOUNT RECIEVED=",(x*0.05))
    print(" Total amount to pay =", a, '\n')
    print(" Thank you.")
    print("___________________________________________")   
