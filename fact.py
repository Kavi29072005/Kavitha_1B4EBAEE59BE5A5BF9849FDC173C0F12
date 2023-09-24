def factp(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factp(n-1)

num=int(input("Enter the Value :"))
result = factp(num)
print("The {}! value is {}".format(num,result))
  