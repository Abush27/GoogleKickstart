def split(word):
    return [char for char in word]

t = int(input(""))
counter = 0

while counter < t:
    list1 = input("")
    word = input("")
    

    list1 = list1.split(" ")
    word = split(word)
    

    questions = int(list1[1])
    count = 0
    passes = 0

    while count < questions:
        case = input("")
        case = case.split(" ")

        bot = int(case[0]) - 1 
        top = int(case[1]) 

        pal = word[bot:top]
        odd = 0

        for x in pal:
            num = pal.count(x)
            print(f'there are {num} of {x}')
            if (num % 2) != 0:
                odd += 1
                print('odd is now {odd}')
          
             
                if odd > 1:
                    print(f'breaking cause odd is {odd} and val is {x}')
                    break
     
            #pal = [value for value in pal if value != x]
            y = 0
            while y < num:
                pal.remove(x)
                print(pal)
                y += 1

           
     
     
        if odd <= 1:
            passes += 1
        
        count += 1
    counter += 1
    print(f'Case #{counter}: {passes}')