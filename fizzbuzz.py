for i in range(101):
    num=i+1
    if num%3==0:
        print('fizz')
    elif num%5==0:
        print('buzz')
    elif num%5==0 and num%3==0:
        print('fizzbuzz')
    else:
        print(num)
    
