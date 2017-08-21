# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:09:09 2017

@author: umer
"""

print("hello")
a = 21
b = 10
c = 0
c = a + b
print ("Line 1 - Value of c is ", c)
c += a
print ("Line 2 - Value of c is ", c )
c *= a
print ("Line 3 - Value of c is ", c )
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")
    
amount=int(input("Enter amount: "))
if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print ("Discount",discount)
else:
    discount=amount*0.15
    print ("Discount",discount)
    print ("Net payable:",amount-discount)    
  
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
else:
    print("while endse")    
print ("Good bye!")    
no=int(input('any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num==no:
        print ('number found in list')
    break
else:
        print ('number not found in list')
