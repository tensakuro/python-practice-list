



""" task1


"""



students_data=['suresh','ramesh','rajesh','prakash','prashanth']

print(f"the first student is : {students_data[0].title()}")

print(f"the last student is : {students_data[len(students_data)-1]}")

students_data[2]="python_student"

print(f"the updated data is : {students_data}")


students_data.pop(1)

print(f"final data is : {students_data}")


""" task 2
"""

demotuple=('maths','physics','chem','biom')

newlist=list(demotuple)

print(newlist)


newlist.append('geom')

print(newlist)

newtuple=tuple(newlist)

print(f"the new tuple is {newtuple}")


"""task3

"""

demoset={1,1,5,5,10,10,7,7}

print(f"the set values are {demoset} ")

demoset |={1100,2500,1100}


print(f"the new set values are {demoset}")

demoset-={2500,10}

print(f"the updated data is {demoset}")

newset=list(demoset)

print(f"the set converted to list is  {newset}")

"""task 4"""

intern={
    "name":"durya",
    "age":19,
    "skills":['java','python','c']
}

intern["role"]="java developer intern"

intern["age"]=20

del intern["skills"][2]

print(intern)

print(f"the name of the intern is {intern['name']}")

print(f"the name of intern fetched using different way is : {intern.get('name')}")

"""task 5"""



student1={
    "name":"kyu",
    "city":"hyd",
    "address":"prasanth nagar"
}

student2={
    "name":"pyo",
    "city":"bangalore",
    "address":"koramangla"
}

student3={
    "name":"fyo",
    "city":"noida",
    "address":"nadik"
}

students=[student1,student2,student3]

print(students)

for student in students:
    print(f"the student {student['name']} is  from {student['city']}")

print(f"the address of first student is : {students[0]['address']}")