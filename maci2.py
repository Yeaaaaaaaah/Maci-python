def macilelok(maci):
    for i in range(1,maci+1):
        print(str(maci)+" maci van az ágyban")
        for i in range(1,maci):
            if i < maci-1:
                print("a(z)"+str(i)+". maci odébblöki a(z)"+str(i+1)+". macit")
            else:
                print("a(z)"+str(i)+". maci odébblöki a(z)"+str(i+1)+". macit")
                maci -= 1
                print("a(z) "+str(i+1)+". maci kipottyant az ágyból")
                if maci == 1:
                    print("Az 1. maci olyan dagi volt, hogy a második maci")
                    print("Kipottyant az ágyból")
        
macilelok(100)