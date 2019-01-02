#Do the following in order:
#       Create a list with the values ['x', 'y', 'z'], then create (cast) a tuple from that list.
#       Create a tuple with the values ('a', 'b', 'c'), then create (cast) a list from that tuple.
#       Add the values ‘d’ and ‘e’ to your list {note: append()}
#       Remove the values ‘a’ and ‘b’ from the list

listed = ["x","y","z"]

tuple(listed)
print(listed)

tupled = ("a","b","c")

listed2 = list(tupled)
listed2.append("d")
listed2.append("e")

listed2.remove("a")
listed2.remove("b")
print(tupled)
