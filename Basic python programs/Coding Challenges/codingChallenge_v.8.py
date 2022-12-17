# Challenge 1
clothes = ["shirts", "socks", "pants", "glooves", "shoes"]
for x in clothes:
    print(x)
    if x == "pants":
        # solution
        break

# Challenge 2
t = 132
u = 151

# solution
if t > u:
    print("t is greater than u.")
elif t < u:
    print("t is less than u.")

# Challenge 3
people = ["doctor", "teacher", "neighbor"]
adjectives = ["friendly", "kind", "smart"]
for i in people:
    for j in adjectives:
        # Solution
        print(j, i)

# Challenge 4
for r in range(4):
    print(r)

# Challenge 5
for e in range(9):
    if e == 5:
        continue
    print(e)