ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# Lists are mutable sequences
ft_list[1] = "World!"

# Tuples are immutable sequences
ft_tuple = ("Hello", "France!")

# A set is an unordered collection with no duplicate elements
ft_set.remove("tutu!")
ft_set.add("Angouleme!")

# Dict is standard mapping type and mapping are mutable objects that associates hashable values with arbitrary objects
ft_dict["Hello"] = "42Angouleme!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)