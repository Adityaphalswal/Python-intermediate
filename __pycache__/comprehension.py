integer =[0,1,2,3,4]
binary = ["0","1","10","11","100"]

z= zip(integer, binary)
binary_dict ={integer:binary for integer,binary in z}

print(binary_dict)

integer=[1,-1,2,3,5,0,-7]
inverse =[-1*i for i in integer]
print(inverse)

integer= [1,-1,2,-2,3,-3]
set={i*i for i in integer}
print(set)