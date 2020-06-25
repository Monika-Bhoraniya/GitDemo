

#1) List is data type that allows multiple vales and can be different data type


# values([0])     # index 0,1,2,3.......


values = [1, 2, "Monika", 4, 5]


print(values[1])   #2
print(values[2])   #Monika
print(values[4])   #5
print(values[-1])   #5 (-1 value refer last value)

print(values[1:3])   #2 Monika
print(values[1:4])

#adding or inserting new data with the help of values.insert
values.insert(3, "Bhoraniya")
print(values)

values.append("End")    # we can add new value in last with the help of append
print(values)

values[2] = "MONIKA"  #updating  --> values = [1, 2, "Monika", 4, 5]
print(values)  #output [1, 2, 'MONIKA', 'Bhoraniya', 4, 5, 'End']

del values[0]    #delete the value
print((values))    #output  [2, 'MONIKA', 'Bhoraniya', 4, 5, 'End']
values.append("python")
print(values)         #end of list it will print or add new value 'python'


#2) Tuple  -- same as list dta type but immutable where updation is not possible

val = (1, 2, "Monika", 4.5)   #round bracket --Tuple

#print(val[1])
#val[2]="Monika"
print(val)

# 3) Dictionary   -key value

dic = {"a": 2, 4: "bcd", "c": "Hello world"}   #it should read key
print(dic[4])
print(dic["c"])    #where we use string we need to use "" double quots
print(dic["a"])

#
dict = {}
dict["firstname"] = "Monika"   #key value pair
dict["lastname"] = "Bhoraniya"
dict["gender"] = "Female"
print(dict)

print(dict["lastname"])
print(dict["gender"])

#loops in python

   #condition over here

#for loop



obj=[2,3,5,7,9]
for i in obj:
    print(i*2)

    #sum of fisrt natural numbers 1+2+3+4+5=15
#for i=0;i<5
summation = 0
for j in range(1, 6):
    summation = summation+j
    print(summation)










