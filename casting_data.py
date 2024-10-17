#casting data integer
data_int = 10;
print ("data =", data_int, "type", type (data_int))

data_float =float (data_int)
print ("data =", data_float, "type", type (data_float))

#boolean akan false ketika int = 0
data_bool = bool(data_int)
print ("data =", data_bool, "type", type (data_bool))

data_str = str(data_int)
print ("data =", data_str, "type", type (data_str))

#casting data float
data_float = 10.3;
print ("data =", data_float, "type", type (data_float))

data_int=int (data_float)
print ("data =", data_int, "type", type (data_int)) #akan dibulatkan ke nilai terendah

#boolean akan false ketika int = 0
data_bool = bool(data_float)
print ("data =", data_bool, "type", type (data_bool))

data_str = str(data_float)
print ("data =", data_str, "type", type (data_str))
 
data_complex = complex (data_float)
print("data =", data_float,"type" , type(data_complex))

#casting data str
data_str = "5";
print("data =", data_str, "type", type(data_str))
data_bool = bool(data_str)
print("data =", data_bool, "type", type(data_bool))
data_int = int (data_str)
print("data =", data_int, "type", type(data_int))
data_complex = complex (data_str) 
print ( "data =", data_complex , "type ", type(data_complex))