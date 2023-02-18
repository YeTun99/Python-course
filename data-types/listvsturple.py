list_setup="""coordinates_list=[[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4]]"""
tuple_setup="""coordinates_tuple=((3,4),(3,4),(3,4),(3,4),(3,4),(3,4),(3,4))"""
list_time= timeit.timeit(list_setup)
tuple_time= timeit.timeit(tuple_setup)
print(f"list time is {list_time}")
print(f"tuple time is {tuple_time}")

