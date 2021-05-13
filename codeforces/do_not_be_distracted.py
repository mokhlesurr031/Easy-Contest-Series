test = int(input())


while test:
    num= int(input())
    sentence = input()

    for i in range(0, (len(sentence)-1)):
        word = sentence[i]
        if sentence[i+1]==word:
            word = sentence[i+1]
        else:
            word = sentence[i+1]

    test-=1 