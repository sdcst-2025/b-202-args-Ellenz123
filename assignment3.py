'''
Median, Mode, Midpoint
Create a function called centralTendency() that makes use of *args to receive a variable number of inputs.  The function will return 3 values, the median, mode and midpoints.  
You will need to google what these mean.

You will need to make use of list.sort() to help you with some of these

Use the assertion statments below to test your results:
```
assert CentralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (4.5,6,5.5)
assert centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5,5,6)
```
'''

def CentralTendency(*args):
    x=list(args)
    x.sort()
    count=0
    for _ in x:
        count+=1
    

    if count%2==0:
        median=(x[count//2-1] + x[count//2])/2
    else:
        median=x[count//2]
    print(median)

    mode=x[0]
    count1=0
    for num in x:
        t=0
        for a in x:
            if a==num:
                t+=1
        if t > count1:
            count1=t
            mode=num
    print(mode)

    midpoint=(x[0] + x[count-1])/2
    print(midpoint)

    return(median, mode, midpoint)

      
assert CentralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (6.0,6,5.5)
assert CentralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5.5,5,6)
print("All tests passed.")