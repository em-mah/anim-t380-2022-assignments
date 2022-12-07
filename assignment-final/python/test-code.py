'''   chainList = []
    previousName = ''
    for j in allJoints:
        splitNC = j.split('_')
        if previousName == '':
            previousName = splitNC[2]
            splitNC[2] = dict(str(splitNC[2]):'')
            chainList.append(splitNC[2])
        elif splitNC[2] != previousName:
            previousName = splitNC[2]
            splitNC[2] = list()
            chainList.append(splitNC[2])
        else:
            pass
    print(chainList)


    for i in chainList:
'''