#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  my_str = str(num)
  for i in range(len(my_str)):
    if my_str[i] == ".":
      return my_str[i+1]

#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))