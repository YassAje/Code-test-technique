try:
    f = open('infos.txt', 'r')
    for l in f.readlines():
        print(int(l.strip()))
except:
    print("erreur")
finally:
    f.close
    
