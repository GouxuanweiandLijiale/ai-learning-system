for a in range(1,11):
    print(a)
for b in range(1,21):
    if b % 2 == 0:
        print(b)
add = 0
for c in range(1,101):
    add = add + c
print(add)
d = 1
e = 0
sum = 0
while d != 0:
    d = int(input("enter a number: "))
    if d == 0:
        break
    e += 1
    sum += d
print(e)
print(sum)
f = 0
for f in range(1,21):
    if f == 7:
        continue
    elif f == 13:
        break
    print(f)
word = input("enter a character: ")
g = 0
for char in word:
    print(char)
    g += 1
print("the length of the word is: ", g)