# for loops problem
furniture = ["table", "chair", "cabinet", "desk", "couch"]
# Solution
for x in furniture:
    if x == "cabinet":
        continue
    print(x)

# While loop problem
i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15.")