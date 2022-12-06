
list - []
with open(r"file.text") as file:
  for data in file.readlines():
    list.append(data.strip())

print(list)
