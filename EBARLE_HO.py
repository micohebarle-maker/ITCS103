m = len(input("Input your name? "))

i = []
for c in range(m):
    o = int(input(f"Input number {c+1}: "))
    i.append(o)

print(i)
print("The length of your name is", m)

average = sum(i) / len(i)
print("The average is", average)

if average <= m:
    print("The average is less than or equal to the length of your name.")
else:
    print("The average is greater than the length of your name.")
