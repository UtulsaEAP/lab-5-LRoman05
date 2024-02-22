"""

Name: Logan Roman
Lab Time: 2:00 Thurs

"""

def fibonacci(n):
    #write your code here
    fn2=0
    fn1=1
    if (n>1):
        for x in range(0,n-1,1):
            fn=fn1+fn2
            fn2=fn1
            fn1=fn
        return(fn)
    elif (n==1):
        return(fn1)
    elif (n==0):
        return(fn2)
    else:
        return(-1) 
    """
    Fun fact: the most logical continuation of the fibonacci sequence into the negatives essentially mirrors the values,
    but every other is negative. Essentially, for a fibonacci number with index -n, the value is:
    the fibonacci number n times (-1)^(n+1). In other words, it alternates negative to positive, with odd numbers being positive.
    """

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')