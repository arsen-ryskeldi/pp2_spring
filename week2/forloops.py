#ex 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Answer: "for x in fruits:"

#ex 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Answer: "continue"

#ex 3
for x in range(6):
  print(x)

#Answer: "range(6)"

#ex 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Answer: "break"