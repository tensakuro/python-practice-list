# # # # x=4

# # # # print(x)

# # # # print(id(x))

# # # # x=5

# # # # print(id(x))


# # # # # primite data types:1.a single value can be assigned to a single variable
# # # # #  primitive data types are immutable
# # # # #primitive data types are stored in stack memory
# # # # #in primitive data type always assigned to new memory location
# # # # # 


# # # # # # 1. Immutable Nature
# # # # # As you noted, primitives are immutable. This means once a value is created in memory, it cannot be changed. If you "change" a variable, you aren't modifying the old value; you are creating a brand new one.

# # # # # Python

# # # # # x = 10    # Memory address A holds the value 10
# # # # # x = x + 1 # Memory address A is ignored; Memory address B now holds 11
# # # # # # 
# # # # # # 
# # # # # 

# # # # # 
# # # # # Pro-Tip: Checking Memory Locations
# # # # You can actually see this happening in Python using the id() function, which shows the memory address:

# # # # type of data we use for programming or storing information or manipulating information

# # # #based on data
# # # #text->str
# # # #numeric_types->int,float,complex
# # # #sequence types->list,tuple,range
# # # #mapping type->dict
# # # #set types->set,frozenset
# # # #boolean type->bool 
# # # #binary types->bytes,bytearray,memoryview
# # # #none type->None


# # # #based on how they stores

# # # #1.primitive types->stores single value int,float,bool,none,string
# # # #2.non-primitive types->stores multiple values list,tuple,dict,set,function,regex


# # # #primitives are immuatble at same place

# # # #non-primitives are mutable at same place
# # # #non-primitives are stored in heap memory
# # # #non-primitives are assigned to same memory location
# # # #non-primitives can store multiple values
# # # #non-primitives can be changed at same place
# # # #non-primitives are reference types
# # # #non-primitives store address of the value

# # # import time
# # # from typing import MutableMapping


# # # # list->[]
# # # # tuple->()
# # # # dict->{}
# # # # set->{}
# # # # #function->def function_name():
# # # # #regex-->r""
# # # # #none type->None
# # # # date time->datetime module


# # # list is a collection of heterogeneous/homogeneus data which is wrapped between the square brackets and separated by commas

# # # and each value can be called as element and each element can be separated with commas,
# # # list can be mutable,
# # # list is ordered and also allows duplicate vaules and every element in the list can be accessed  by index

# # # index start frim 0
# # # this is wil allow positive and negative indexing

# # # list is stored in heap memory but values in list are stored in stack memory

# # # len(list_name)->gives length of the list
# # # list_name.append(value)->adds value to the end of the list
# # students = ["anil", "sunil"]
# # students.extend(["vijay"]) 
# # # Result: ['anil', 'sunil', 'vijay']




# cart=["shirt","facewash","bodyspray","shoes"]

# print(f"the cart is: {cart}")

# cart[2]='perfume'

# print(f"the changed cart is: {cart} ")

# cart.append('watch')

# print(f"appended cart is:{cart}")

# cart.remove(cart[0])

# print(f"removed cart is :{cart}")


# print(f"length of cart is :{len(cart)}")



