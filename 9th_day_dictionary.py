'''1.  Various operations on Python Dicationaries '''

# Here we are replaced the values of the Dicationarys Value 😎🙂😮
# Its very important Topic Remember it

# std_dict={"mahesh":99, "akash":89, "suresh":80}
# dict={}
# for i in std_dict:
#     score=std_dict([i])
#     if score > 90:
#         dict([i])=="outstanding"
#     if score >80 :
#         dict([i])=="first class"
#     if score > 70:
#         dict([i])=="seconde Grade"
#     else:
#         dict([i])=="fail"

    
# ''' 2. In this we are going to study  About nesting of Dictionary '''
# # here we are created a list in dicatinory by taking so many values in one key valye by '{[]}' 🙂
# # {
# #     key:[list],
# #     key2:{Dict},
# # }

# travel_log={ "visited_place" : {["Mumbai","Gujrat", "keral"]}, "no_places":12 }   #key:[list]

# # This two are different 🤠🤓 Oberve Carefully🧐🥴🤪
# travel_log={"France":{"visited_places":["India","china","japan"],"no_visited":3}}  #key2:{Dict},

# ''' 3. Nesting Dictionary in list '''

# travel_log=[
#     {
#         "country":"France",
#         "cities_visited":["peris", "lilie", "Dijon"],
#         "total visits":12
#     },

#     {
#         "country":"germany",
#         "cities_visited":["Berlin", "Hamburge", "Sturtgart"],
#         "total visits":15
#     }
# ]

# #TODO: 3. write the function that will allow new counties 😎👀 
# # to be added to teh travel_log
# def add_new_country(country_visited , times_visited ,cities_visited):
#     new_country={}
#     new_country["country"]=country_visited
#     new_country["visits"]=times_visited
#     new_country["cities"]=cities_visited
#     travel_log.append(new_country)

# add_new_country("Russia",2,["Moscow","Saint petersburg"])
# print(travel_log)



















# travel_log=[
#     {
#         "country":"France",
#         "cities_visited":["peris", "lilie", "Dijon"],
#         "total visits":12
#     },

#     {
#         "country":"germany",
#         "cities_visited":["Berlin", "Hamburge", "Sturtgart"],
#         "total visits":15
#     }
# ]
# # a={}
# def countrys(visited, times, *cities_visited):
#     a={"visited":visited,
#     "times":times,
#     "cites visited":cities_visited }
#     print(a)
#     print(travel_log.append(a))

# countrys("India",3,"ma","he","sh")


# print("*******************")
# print(travel_log)
# print("mahesh")



# from tkinter.messagebox import YES


people=int(input("Enter the no of peoples are bedding:? "))
dict={}
for i in range (0,people):
    new_dict={}
    # opinion='type s if people of bedder are remaining and vice versa'
    def bed(name,bid ,opinion):
        
        new_dict["name"]=name
        new_dict["bid"]=bid
        new_dict["opinion"]=opinion

    n=input("Enter Your name..? ")
    b=int(input("Enter your bid.? "))
    op=input("Enter yes if bed wansts to continue..else enter no?")
    bed(n,b,op)
    dict.append(new_dict)
    if op=="yes":
        continue
    else:
        break
    # dict+=(new_dict)
print(new_dict)
