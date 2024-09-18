
t = int(input(""))

counter = 0

while counter < t:

    total = 0
    line1 = input("")
    line2 = input("")

    line1 = line1.split(" ")
    line2 = line2.split(" ")

    for i in line2:
        total += int(i)

    result = (total % int(line1[1]))
    counter += 1
    print(f'Case #{counter}: {result}')

