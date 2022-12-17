# for loops iteration
color = ["purple", "red", "orange", "yellow"]
for x in color:
    print(x)

# loop on strings
for i in "orange":
    print(i)

# continue statement it will skip the value of the variable and proceeds with the rest of the items in the list.
gpu = ["irish XE", "RTX", "RX"]
for y in gpu:
    if y == "RTX":
      continue
    print(y)
# end

# break statement it will stop the loop completely
cpu = ["Intel", "AMD", "Snapdragon", "Mediatek"]
for c in cpu:
    print(c)
    if c == "AMD":
        break
# loop on strings
for i in "orange":
    print(i)