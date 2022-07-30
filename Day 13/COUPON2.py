# cook your dish here
t = int(input())
while t > 0:
    d,c = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    a_sum = sum(a)
    b_sum = sum(b)
    wo_coupon = a_sum + b_sum + 2*d
    coupon = a_sum + b_sum + c
    if(a_sum < 150 and b_sum < 150):
        coupon += 2*d
    elif(a_sum >=150 and b_sum < 150):
        coupon += d
    elif(a_sum  < 150 and b_sum >= 150):
        coupon += d
    
    if(wo_coupon > coupon):
        print("YES")
    else:
        print("NO")
    
    t = t-1