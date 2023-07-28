# # you can use certain functions to manipulate the shape of an array to do the following  as np

# #  Import numpy 
print("hello world ")
# a= np.arange(10)
# a.dtype   # for choosing datatype

# a= np.arange (10, dtype='float64')

# a=np.arange( (3,3))
# d= np.zeros((2,3))
# i=np.ones(4)   # in Float form
# e= np.diag([2,3])   # diagonal matrix  have digonal no 2,3 
# f= np.eye(3,3)  # identity matrix 
# g= np.dim(d)

# # i) ---------->>>>  Different Datatypes <<<<-----------

#     #1. coomplex datatypes 
#     h= np.array([1+2j, 2+4j])

#     #2. boolean datatype 
#     b= np. array ([True, False, True, False ])
#     print (b.dtype)

# # ii) ----------------->>>> Indexing and Slicing <<<<----------------
# j=np. array(10)
# print (a[5])

# a[1,2]=7  # assigning the value at perticuler position

# # iii) ---------------->>>> diagonal  <<<<---------------------------
# a= np.diag([1,2,3])
# print ( [1,0,0],  # 0th Position
#         [0,2,0],  #1st Position
#         [0,0,3])
# print(a)      
# print (a[2,2])   # indexing Start From 0



# #slicing 

# a[1:8:2]  # [startindex: endindex (exclusive) :step ]

# # we can also combine assignment and slicing :
# g= np.arange(10)
# a[5:]= 10
# print (a)

# #assigning 
# b= np.arange(5)
# a[5:]= b[ : : -1]  
# print (a)

# # iv )------------------>>>>  Copies and Views  <<<< ------------------

# np.shares_memory(a,b)
# b[0]=10

# array([10,2,5,6,8])
#  print (a) # Eventhough  we modified b, it updated 'a', because both shares same Memory 
#             # to optimize space utilization we use Share_Memory
#  np.shares_memory(a,c)  # output-> False

# ''' Numpy arrays can be indexed withh slices , but also with boolean or integer arrays (Masks). This method is called fancy indexing 
# It creates Copies Not Views   '''

# #array([13,2,3,6,4,6,34,6,2,8,0])
# a= np.random.randint(0,20,17)
# mask = a(a%2==0)
# extract_from_a =a [mask]
# print (extract_from_a)

# a[mask]=-1

# #New values can be assigend at a same time 
# a[[9,3]]= -30

# # perticuler indexes ka Array Create kar sakte hai 
# a[[2,3,4,6]]



# #------------------>>>>>>  Element wise Operation  <<<<----------
# a=np.array([1,3,5])
# print (a+1)
# # -> array([2,4,7])

# # ----------->>>> Matrix Multiplication <<<<------------------
# c=np.diag([1 ,3,5 ,6])
# print (c*c)  # OR 
# print (c.dot(c))

# # ----------->>>> Comparision<<<<------------------
# a=np.array([1,3,5])
# b=np.array([1,3,5])
# -> o/p array([True, True, True])

# np.array_equal(a,b)
# -> o/p True


# # ----------->>>> Logical Operation <<<<------------------
# a=np.array([1,3,5], dtype=bool)
# b=np.array([1,3,5]), dtype=bool)
# np.logical_or(a,b)


# # ----------->>>> Transactional Funcction  <<<<------------------
# a=np.array([1,3,5])
# np.sin(a)
# np.log(a)
# np.exp(a)


# # ----------->>>> Basic Reductino <<<<------------------
# a=np.array([1,3,5])
# np.sum(x)


# # ----------->>>> Matrix Multiplication <<<<------------------


# # ----------->>>> Matrix Multiplication <<<<------------------