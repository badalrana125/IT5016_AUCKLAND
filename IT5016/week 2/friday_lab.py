text= 'Hello world!'
a= text.upper()
b=text.lower()
c= text.capitalize()
d= text.title()

print(a,b)
print("Lower and upper funtion output is :",a,b)
print(c)
print(d)

student_id= 20240567
id="2024year567"
# print(student_id.isalpha())
# print(student_id.isdigit())


txt= "find  me if you can"
print(txt.rfind('i'))
print(txt.count('i'))

#strip
a="      hello    this    is test  "
print(a.strip())
text= a.lstrip()
text_2= a.rstrip()
print('the result of lstrip and r strip is', text,text_2)

#split funtion
test="Hey this is me"
a= test.split()
print(a)

#absolute value
a= 4+5j
print(abs(a))

x=100.30
y=50.60
print(round(y))

#ascending and descending or sorted
a= ('Hello', 'Aashis', 'ice-cream' , 'yak')
ace= sorted(a)
des= sorted(a,reverse=True)
print(ace,des)

#sum function
aas= (10,12,13,14,15)
r1= sum(aas)
print(r1)




