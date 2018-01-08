def computepay(h,r):
    if int(h) <= int(40):
        return int(h) * float(r)
    elif int(h) >= int(40):
        ot = (int(h) - int(40)) * (float(r) * 1.5)
        return ot + int(40) * float(r)

hrs = input('Enter Hours: ')
hrs = float(hrs)
rate = input('Enter Rate: ')
rate = float(rate)
p = computepay(hrs,rate)
print(p)
