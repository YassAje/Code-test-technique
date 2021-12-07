try:
    with open('infos.txt', 'r') as f:
        for l in f.readlines():
            print(int(l.strip()))
except IOError as err:
    print("erreur de fichier", err)
except ValueError:
    print("erreur de conversion")
except:
    print("erreur inconnue ! Tous aux abris")
    
