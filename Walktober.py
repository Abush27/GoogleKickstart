

t = int(input())
testCount = 0;

while testCount < t:
    inp = input()
    inpList = inp.split()
    participants = int(inpList[0])   
    johnID = int(inpList[2])
    days = int(inpList[1])
    stepsNeeded = 0
    johnSteps = [0] * days
    maxSteps = [0] * days 
    

    for i in range(participants):

        stepInp = input()
        holder = stepInp.split()
        holder = list(map(int, holder))



        if johnID == (i +1):
            johnSteps = holder
        else:
            for j in range(len(maxSteps)):
                if (maxSteps[j] < holder[j]):
                    maxSteps[j] = holder[j]


   
    for x in range(len(maxSteps)):
        if (johnSteps[x] < maxSteps[x]):
            stepsNeeded += (maxSteps[x] - johnSteps[x])

    testCount += 1
    print(f'Case #{testCount}: {stepsNeeded}')
    
