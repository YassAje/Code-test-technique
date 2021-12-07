class SerieTele:
    def diffuser(self):
        print("désolé, je n'ai pas la télé !")

class EpisodeDrWho(SerieTele):
    """
    Un épisode du Docteur Who
    """

    def __init__(self, saison, episode):
        self.saison  = saison
        self.episode = episode

    def attaque_dalek(self):
        print("au secours ! Attaque de Dalek dans l'épisode",self.saison,self.episode)


ep = EpisodeDrWho(7, 5)

#ep.saison = 7
#ep.episode = 5

#print(ep.saison) 

ep.attaque_dalek()
ep.diffuser()
