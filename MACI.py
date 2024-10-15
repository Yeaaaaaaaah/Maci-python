cyclenum, cyclenum1, bears = 0, 0, 10
while cyclenum < 10:
    if cyclenum < 9:
        print(str(bears)+" maci van az ágyban")
        print("Az első panaszkodik, mert nem fér el. Odébbgurulás lesz...")
        while cyclenum1 < bears:
            if cyclenum1 < bears-2:
                print("a(z)"+str(cyclenum1+2)+". maci odébblöki a(z)"+str(cyclenum1+3)+". macit")
                cyclenum1 += 1
            else:
                bears -= 1
                cyclenum1 += 1
                if bears == 1:
                    print("Az 1. maci olyan dagi volt, hogy")
                print("a(z) "+str(bears+1)+". maci kipottyant az ágyból")
        cyclenum += 1
        cyclenum1 = 0
        print (" ")
    else:
        print("1 maci van az ágyban")
        cyclenum += 1