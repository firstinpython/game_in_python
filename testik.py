def test(a,is_flag):
    flag = is_flag
    if a%2==0:
        flag== False
    else:
        flag == True
    return flag

a = 0
is_flag = True
while True:
    test(a,is_flag)
    print(a,is_flag)
    a+=1