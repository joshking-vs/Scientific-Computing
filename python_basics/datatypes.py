my_int = 5
my_float = 5.5
my_int2 = int(my_float)
my_float2 = float(my_int)
my_bool = True
my_complex = 5 + 1j
my_complex2 = complex(my_int)
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_dict = {
    "name":"josh",
    "age":10,
    "course":"Computer Science",
}
my_set = {1,2,3,4}

my_data_types = [my_int,my_int2,my_float,my_float2,my_bool,my_complex,my_complex2,my_list,my_tuple,my_dict,my_set]

for x in my_data_types:
    print(x,type(x))



