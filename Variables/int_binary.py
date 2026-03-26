def binary_conversion(num):
     remainder = []
     while num>0:
     
          result = num%2
          remainder.append(result)
          num = num//2
     remainder.reverse()
     print(*remainder,sep="")  #tuple unpacking 

binary_conversion(4)
binary_conversion(12)
binary_conversion(1)

