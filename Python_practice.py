#
# Wow this this is pretty cool!!! 
# 
#  print("Hello World")

# print(type(3))
# help("keywords")

# # Making & Manipulating Lists

# my_list =  [1, "One", True , 0, "Zero" , False]
# print(my_list)
# print ( list([1, "None", 0, True]))

# print(my_list[0])

# print(len(my_list))

# list2 = list(my_list[1 : 3])
# print(list2)

# my_list

# print(type(my_list[1]))

# ##Example
# counties = ['Araphoe', 'Denver' , 'Jefferson']
# print(counties)

# counties.insert(2, 'El Paso')
# print(counties)

# counties.remove("Araphoe")
# print(counties)

# counties = counties[ 1 : ]
# print(counties)

# counties.append('Denver')
# print(counties)

# counties.append('Araphaho')
# print(counties)

# # Making and accessing Tuple data
# counties_tuple = ( 'arapahoe' , 'denver' , 'jefferson')
# print(counties_tuple)
# print(type(counties_tuple) , len(counties_tuple))

# print(counties_tuple[2]) #indexing

# # Making and accessing Dicitonaries

# counties_dict = {'Arapahoe': 422829 , 'Denver': 463353 , 'Jefferson': 432438}
# print(f"Dictionary = {counties_dict}")

# print(len(counties_dict))

# print(counties_dict.get('Arapahoe'))
# print(counties_dict['Arapahoe'])

# #list of dictionaries
# voting_data = [] #initialize as a list
# print(voting_data)
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829}) # add a dictinary to that list
# print(voting_data)
# voting_data.append({"county":"Denver", "registered_voters": 463353}) # add another dictionary
# print(voting_data)
# voting_data.append({"county":"Jefferson", "registered_voters": 432438}) # add another dictionary
# print(voting_data)

# voting_data.insert(2, {"county":"El Paso", "registered_voters": 461149}) #inset El Paso in second position
# print(voting_data)

# voting_data.remove({"county":"Arapahoe", "registered_voters": 422829}) #remove this dictionary from the list
# print(voting_data)

# voting_data.remove({"county":"Denver", "registered_voters": 463353}) #remove this dictionary from the list
# voting_data.append({"county":"Denver", "registered_voters": 463353}) # add it on to the end of the list
# print(voting_data)

# voting_data.append({"county":"Arapahoe", "registered_voters": 422829}) # add it on to the end of the list
# print(voting_data)

# # If statements
# counties = ["Arapahoe","Denver","Jefferson"] 
# print(counties)
# if counties[1] == 'Denver':
#     print(counties[1])

# #If Else Statements
# # if a>b :
# #     a = 6
# # else :
# #     b = 5

# # Temperature Example

# # temp = int(input("What is the temperature outside today?"))

# # if temp>80 :
# #     print("Turn on AC!")
# # else :
# #     print("Open the windows")

# # Grading Example
# # score = int(input("What is your test score? "))

# # # Determine the grade.
# # if score >= 90:
# #     print('Your grade is an A.')
# # elif score >= 80:
# #     print('Your grade is a B.')
# # elif score >= 70:
# #     print('Your grade is a C.')
# # elif score >= 60:
# #     print('Your grade is a D.')
# # else:
# #     print('Your grade is an F.')

# # Membership Operators

# # counties = ["Arapahoe","Denver","Jefferson"]

# # # if "El Paso" in counties :
# # #     print("El Paso is listed")
# # # else :
# # #     print( "El Paso is not listed")

# # # # while loop
# # # x = 0 
# # # while x<=5 :
# # #     print(x)
# # #     x = x + 1

# # For Loop
# # counties = ["Arapahoe","Denver","Jefferson"]

# # for county in counties :
# #     print(county)

# # for num in range(5) :
# #     print(num)

# # for i in range(len(counties)):
# #     print(counties[i])

# # print(list(range(1,5,1)))

# # print(list(range(1,10,2)))

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:  #print out the values in county
    print(county)

for county in counties_dict.keys():  #print out the keys
    print(county)

for voters in counties_dict.values():  #print out the values
    print(voters)

for county in counties_dict:  # prints the value associated with that key
    print(counties_dict[county])

for county in counties_dict: # prints the value associated with that key
    print(counties_dict.get(county))

for county, voters in counties_dict.items():  # prints both key & value
    print(f"{county} has {voters} registered voters")

#for loops and lists of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Nested for loop for values with in list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
