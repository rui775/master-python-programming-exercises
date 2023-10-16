#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    #dollars to cents plus the cents multiplied by the number of items will result in the cost in cents, than we make a floor division by 100 to obtain the cost in dollars and than we get the remain in cents.
    return (((d*100) + c) * 4) // 100, (((d*100) + c) * 4) % 100
    # fast but wrong
    # return (d*n), (c*n) 
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(15,30,4)) # output 61,20
