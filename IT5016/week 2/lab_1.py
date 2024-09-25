"""
The total wholesale cost for 60 copies
Author= Aashish
"""

cost = 24.95
discount = 0.40
shipping_cost_for_first_copy= 3
shipping_cost_for_additional_copy= 0.75
copies= 60
 
discount_price = cost*discount #Discount per book

#discount cost
cost_after_discount= cost- discount_price #per book
total_cost_after_discount = cost_after_discount* copies
 #calculating shipping cost
total_shipping_cost= shipping_cost_for_first_copy + shipping_cost_for_additional_copy* (copies-1)  

#Calculating wholesale cost
wholecost= total_cost_after_discount+ total_shipping_cost

print("Total wholecost cost for 60 copies is $", wholecost, sep="")

#LEN FUNCTION

length1=len("aashish")
length2= len("98 00 987843 373   2")
#length3= len(world1)

print(length1,length2)
 

item1= 5
item2= 7
item3= item2
item2= item1

print(item1, item2, item3)

#inbuild check the data type or function

num1 = 7
num2 = 26.7
word= "aashish"

print(type(num1))
print(type(num2))
print(type(word))
print(1, '\'super\' man')
# print(, "/"Super/"Man")


