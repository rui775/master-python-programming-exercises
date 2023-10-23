#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
  # the modulus of the number of the day divide by 7 (days of a week) will result in the days that ramain to complete the week 
  # therefore will give us the day of the week. Plus 3 because the year started on thursday (1 -> Monday + 3 = 4 -> Thursday)
  return (k+3) % 7



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(46))