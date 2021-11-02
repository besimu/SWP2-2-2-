import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':    # add 명령
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except:
                print("parameter를 다시 입력하세요")
        elif parse[0] == 'del':    # del 명령 수정
            try:
                lst = []
                for p in scdb:
                    if p['Name'] == parse[1]:
                        i = scdb.index(p)
                        lst.append(i)
                lst.sort(reverse = True)
                for i in lst:
                    scdb.pop(i)
            except:
                print("parameter를 다시 입력하세요")
        elif parse[0] == 'show':    # show 명령
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':    # find 명령 추가
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)
            except:
                print("parameter를 다시 입력하세요")
        elif parse[0] == 'inc':    # inc 명령 추가
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        score = int(p['Score']) + int(parse[2])
                        p['Score'] = str(score)
            except:
                print("parameter를 다시 입력하세요")
        elif parse[0] == 'quit':    # quit 명령
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
