

cases = int(input())

count = 0

while count < cases:
    firstLine = input()
    firstList = firstLine.split(" ")
    length = int(firstList[0])
    runs = int(firstList[1])
    laps = 0
    oldData = []

    for i in range(runs):
        secondLine = input()
        secondLine = secondLine.split(" ")
        distance = int(secondLine[0])
        direction = secondLine[1]

        if i == 0:
            laps += int(distance / length)
            remainder = int(distance % length)

         
        
        else:
            if oldData[1] == direction:
                total = oldData[0] + distance

            else:
                total = abs(oldData[0] + distance) 

            laps += int(total / length)
            remainder = int(total % length)
            oldData = [remainder, direction]


    count += 1
    print(f'Case #{count}: {laps}')