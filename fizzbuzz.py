num = input("number ")
newn = int(num)
def function(newn):
  return (newn)
if ((newn % 3 )) == 0 and ((newn % 5) == 0):
    print('FizzBuzz')
elif (newn % 3) == 0:
  print("Fizz")
elif (newn % 5) == 0:
  print("Buzz")
else:
  print("no :(")
