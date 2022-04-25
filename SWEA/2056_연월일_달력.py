
t = int(input())

for i in range(1, t+1):
    s = input()
    month = int(s[4:6])
    day= int(s[6:8])
    if (month>12 or month<1) or (day>31 or day<1) or ((month==1 or month==3 or month==5 or month==7 
    or month==8 or month==10 or month==12) and day>31) or ((month==9 or month==11 or month==4 or month==6) and day>30) or (month==2 and day>28):
        print(f"#{i} -1")
    else:
        print(f"#{i} {s[:4]}/{s[4:6]}/{s[6:]}")
