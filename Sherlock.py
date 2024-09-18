t = int(input(""))

counter = 0


while counter < t:
    inp = input("")
    inp = inp.split(" ")

    if int(inp[0]) <= int(inp[1]):
        sub = int(inp[0])

    else:
        sub = int(inp[1])

    sub = int((sub*(sub + 1)) / 2)

    counter += 1

    print(f'Case #{counter}: {sub}')



