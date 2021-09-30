import pickle

dbfilename = 'assignment3_20212980.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
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
        try:
            inputstr = (input("Score DB > "))
            if inputstr == "": continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                scdb += [record]
            elif parse[0] == 'del':
                i = 0
                while i < len(scdb):
                    if scdb[i]['Name'] == parse[1]:
                        scdb.remove(scdb[i])
                    else:
                        i += 1
            elif parse[0] == 'show':
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'find':
               for p in scdb:
                   if p['Name'] == parse[1]:
                       for attr in sorted(p):
                           print(attr + "=" + str(p[attr]), end=' ')
                       print()
            elif parse[0] == 'inc':
                for p in scdb:
                   if p['Name'] == parse[1]:
                       p['Score'] += int(parse[2])

            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])
        except ValueError:
            print("숫자를 쓰세요")
        except:
            print("오류가 발생함")
        else:
            print("Done")

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)