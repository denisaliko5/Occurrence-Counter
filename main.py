string1 = "Vraponte Qaniu pas qerres së qumshtit / se qeni qimekuq i ishte qepur pas."
print(string1)

string2 = string1.casefold()
search1 = input("\nNote: Don't use capital letters when searching!\nSearch: ")
search2 = search1.casefold()
if search2 in string2:
  print(string2.count(search2))
else:
  print("Not found")