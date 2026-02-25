# # """
# # {}->set and dictionaries
# # ()->tuple
# # []->list




# # """

# # # list1 = [1,2,3,4,5]

# # # print(list1)

# # # print(list1[1])

# # # list1[2]='hello'

# # # print(list1)

# # # del list1[2]

# # # print(list1)


# # """
# # lists are mutable
# # stores the ordered indexed values
# # lists are dynamic
# # lists are slower than tuples 
# # """

# # # ip=list([1,2,3,4])

# # # print(ip)


# """ 
# tuples are immutable

# to store the final data ,we use tuple
# tuples execute faster than lists

# tuples can accepts duplicatwe and heterogeneous data

# we can access the values from tuple using indeximg because it will store values in orderd collection

# tuples are only readable

# crud-> c and r only will applicable



# """
# # tuple1=(1,2,3,'hello','hi','welcome')

# # print(tuple1)

# # print(tuple1[-2])

# # # tuple1[2]='hi' we cant update

# # tuple2=([1,2],3,4)

# # print(tuple2[0][1])

# # tuple2[0][1]=4

# # print(tuple2)

# # from operator import delitem


# # tuple3=('hello','welcome','python','sql')

# # print(tuple3)

# # converted_list=list(tuple3)

# # print(converted_list)

# # converted_tuple3=tuple(converted_list)

# # print(converted_tuple3)

# # print(len(converted_tuple3))

# # new_tuple=converted_tuple3 + ('newn',)

# # print(new_tuple)

# """ 
# """


# """
# sets are used to store unique values as a unordered collection

# whenever we try to execute the set or print the set values,it always gives random order only especially for string values.
# in set every value has the hashing values for numbers-->number it self be the hashing value

# but for strng value

# | union

# - remove

# """

# # set1={1,2,3,'hello',4,3,2,'hello','hi'}

# # print(set1)

# # num1=1
# # value1='hello'
# # print(hash(num1))
# # print(hash(value1))

# # print(set1)

# # # set1|108

# # set1=set1 | {4,5,6}
# # print(set1)

# # set1=set1-{4}

# # print(set1)


# """
# lists/tuples/sets are used to store like 
# multiple persons,products,colors,books,students
#  """

# """ in dictionary key always should be in a string only
#     no duplicate keys


# """

# xs ={
#     'a':4,
#     'b':1,
#     'c':2,
#     'd':3
# }

# sorted(xs.items())


# all_stu

all_student_info = [
    {"name": "kishore", "city": "hyd"},
    {"name": "manohar", "city": "bnglr"},
    {"name": "ram", "city": "mumbai"},
    { # Added curly brace here
        "address": {
            'streetname': 'ambedkar nagar',
            'pincode': 500072
        }
    } # Added curly brace here
]

print(all_student_info[0])

