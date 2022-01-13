# interest rate = 12%
# stock growth rate = 12%
# tenure = 5 years
# loan amount = 2,50,000 Rs.

lnAmt = 250_000
intRate = 12
stockRate = 12
tenure = 0
emi = 5500
amtGiven = 0

while lnAmt > emi :
    lnAmt *= (1+intRate/12/100)
    lnAmt -= emi
    amtGiven += emi
    amtGiven *= (1+stockRate/100/12)
    tenure += 1



print("interest given: ", (tenure*emi)+lnAmt-250000)
print("stock interest lost: ", amtGiven-(tenure*emi))
