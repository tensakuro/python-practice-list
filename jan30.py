# # # # # # # # # # # # # # # # # # # # name_for_userid={
# # # # # # # # # # # # # # # # # # # #     382:'Alice',
# # # # # # # # # # # # # # # # # # # #     950:'Bob',
# # # # # # # # # # # # # # # # # # # #     590:'Dilbert',
# # # # # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # # # # print(sorted(name_for_userid.items()))


# # # # # # # # # # # # # # # # # # # phonebook={
# # # # # # # # # # # # # # # # # # #     'bob':7387,
# # # # # # # # # # # # # # # # # # #     'alice':3719,
# # # # # # # # # # # # # # # # # # #     'jack':7052,
# # # # # # # # # # # # # # # # # # # }


# # # # # # # # # # # # # # # # # # person ={
# # # # # # # # # # # # # # # # # #     "name":"sohel",
# # # # # # # # # # # # # # # # # #     "age":22,
# # # # # # # # # # # # # # # # # #     "city":"hyderabad"
# # # # # # # # # # # # # # # # # # }  

# # # # # # # # # # # # # # # # # # #dictionary is  mapping

# # # # # # # # # # # # # # # # # # print(person.items())

# # # # # # # # # # # # # # # # # # list =["apple","banana","cherry"]

# # # # # # # # # # # # # # # # # # print(list[0])

# # # # # # # # # # # # # # # # # # marks={
# # # # # # # # # # # # # # # # # #     "maths":90,
# # # # # # # # # # # # # # # # # #     "physics":85
# # # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # # print(marks["maths"])


# # # # # # # # # # # # # # # # # # #keys are  always immutable


# # # # # # # # # # # # # # # # # # country_capital={
# # # # # # # # # # # # # # # # # #     "india":"New Delhi",
# # # # # # # # # # # # # # # # # #     "France":"paris"
# # # # # # # # # # # # # # # # # # }


# # # # # # # # # # # # # # # # # # d={
# # # # # # # # # # # # # # # # # #     "maths":90,
# # # # # # # # # # # # # # # # # #     "maths":85
# # # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # # print(d)

# # # # # # # # # # # # # # # # d={}

# # # # # # # # # # # # # # # # d["name"]="sohel"

# # # # # # # # # # # # # # # # d["age"]=22

# # # # # # # # # # # # # # # # d["address"]="guntur"

# # # # # # # # # # # # # # # # print(d)

# # # # # # # # # # # # # # # # del d["name"]

# # # # # # # # # # # # # # # # print(d)


# # # # # # # # # # # # # # # # print(d.get("name",0))

# # # # # # # # # # # # # # # # print(list(d))


# # # # # # # # # # # # # # # # print(sorted(d))

# # # # # # # # # # # # # # # # print("age" in d)


# # # # # # # # # # # # # # # # d={
# # # # # # # # # # # # # # # #     "x":1,
# # # # # # # # # # # # # # # #     "y":2,
# # # # # # # # # # # # # # # #     "z":3
# # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # print(list(d))

# # # # # # # # # # # # # # # # d={}

# # # # # # # # # # # # # # # # d["b"]=2
# # # # # # # # # # # # # # # # d["a"]=1
# # # # # # # # # # # # # # # # d["c"]=3

# # # # # # # # # # # # # # # # print(list(d))

# # # # # # # # # # # # # # # # d={
# # # # # # # # # # # # # # # #     "banana":2,
# # # # # # # # # # # # # # # #     "apple":5,
# # # # # # # # # # # # # # # #     "cherry":1
# # # # # # # # # # # # # # # # }


# # # # # # # # # # # # # # # # print(sorted(d))

# # # # # # # # # # # # # # # # d={"name":"sohel","age":22}

# # # # # # # # # # # # # # # # print("name" in d)

# # # # # # # # # # # # # # # # print("age" in d)

# # # # # # # # # # # # # # # # print("sohel" in d.values())

# # # # # # # # # # # # # # # d={}

# # # # # # # # # # # # # # # d[1]="one"

# # # # # # # # # # # # # # # d["1"]="string one"

# # # # # # # # # # # # # # # print(list(d))

# # # # # # # # # # # # # # # print(sorted(d,key=str))

# # # # # # # # # # # # # # # students=[
# # # # # # # # # # # # # # #     {"name":"A","age":20},
# # # # # # # # # # # # # # #     {"name":"B","age":21}
# # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # print(students)


# # # # # # # # # # # # # # points=[(1,2),(3,4),(5,6)]

# # # # # # # # # # # # # # print(points)

# # # # # # # # # # # # # from typing import Iterable


# # # # # # # # # # # # # resul

# # # # # # # # # # # # nums =[1,2,3,4]

# # # # # # # # # # # # squares =[x*x for x in nums]

# # # # # # # # # # # # print(squares)


# # # # # # # # # # # # summation_list=[x+1 for x in [1,2,3]]

# # # # # # # # # # # # print(f"summation_list for 1,2,3 is {summation_list}")


# # # # # # # # # # # from traceback import print_exception


# # # # # # # # # # # a=[1,2,3]
# # # # # # # # # # # b=a
# # # # # # # # # # # b.append(4)

# # # # # # # # # # # print(b)

# # # # # # # # # # # print(a)

# # # # # # # # # # nums =[1,2,3]
# # # # # # # # # # result=[x for x in nums]

# # # # # # # # # # print(result)

# # # # # # # # # nums=[1,2,3,4]

# # # # # # # # # result=[x*x for x in nums]

# # # # # # # # # print(result)

# # # # # # # # result=[ch.upper() for ch in 'hello']

# # # # # # # # print(result)

# # # # # # # nums=[1,2,3,4,5,6]

# # # # # # # res=[x for x in nums if x%2==0]

# # # # # # # print(res)

# # # # # # words=["hi","hello","sun","python"]

# # # # # # res=[w for w in words if len(w)>3]

# # # # # # print(res)

# # # # # nums=[1,2,3,4,5]

# # # # # result=[x*x for x in nums if x%2==0]

# # # # # print(result)

# # # # words=["apple","banana","cherry"]

# # # # result=[w[0] for w in words]

# # # # print(result)

# # # d={
# # #     "a":1,
# # #     "b":2,
# # #     "c":3
# # # }

# # # result=[x for x in d]

# # # print(result)

# # words=["hi","hello","world"]

# # res=[len(w) for w in words]

# # print(res)

# nums=[1,2,3]

