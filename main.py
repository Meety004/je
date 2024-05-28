#IMPORTS
from tkinter import *
import random


#GLOBALES

#On crée les clés des différentes salles et on met leurs valeurs à False
global key_verbal_memory 
global key_images_memory 
global key_number_memory

key_verbal_memory = False
key_images_memory = False
key_number_memory = False

#On crée les variables des meilleurs scores de chaque salle et on les met à zéro
global MVHighestScore
global MIHighestScore
global MPHighestScore
global MNHighestScore

MVHighestScore = 0
MIHighestScore = 0
MPHighestScore = 0
MNHighestScore = 0

#On crée les coordonnées de notre sprite (personnage) et on les définit à l'origine
global coords
coords = (400, 300)

global difficulte
difficulte = None

#SCRIPT GENERAL
def script():

  #On remet les coordonnées à 0
  def reset_coords():
    coords = (400, 300)

  #FONCTION DE LA MEMOIRE VERBALE
  def verbal_memory_start():
    #On met les coordonnées à zéro
    reset_coords()
    #On crée une liste vide qui va contenir les mots déjà vus
    SeenWords = []

    #Fonction pour gérer la fin de la mémoire verbale
    def restart_mv():

      #Fonction qui relance la mémoire verbale
      def mvrestart():
        MVRestartFrame.destroy()
        verbal_memory_start()

      #Fonction qui ferme la mémoire verbale et réouvre la fenêtre principale
      def mv_quit():
        MVRestartFrame.destroy()
        script()

      #Fenêtre de fin de partie de mémoire verbale
      MVFrame.destroy()
      MVRestartFrame = Tk()
      MVRestartFrame.title("Partie Terminée | Mémoire Verbale")
      MVRestartFrame.geometry("600x350")
      MVRestartFrameTitle = Frame(MVRestartFrame, relief=GROOVE)
      MVRestartFrameTitle.pack(side=TOP)
      MVRestartTitleLabel = Label(MVRestartFrameTitle, text="Partie Terminée !", font=("Arial", 20))
      MVRestartTitleLabel.pack()
      MVRestartMainFrame = Frame(MVRestartFrame, relief=GROOVE)
      MVRestartMainFrame.pack(side=TOP)
      score = mvscore.get()
      if difficulte == True:

        #Si le joueur a gagné (au moins 50 points )
        if score >= 50:
          MVWinLab = Label(MVRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
          MVWinLab.pack(side=TOP)
          MVWinLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore} !\n Vous obtenez la clé de la Mémoire Verbale !"), font=("Arial", 10))
          MVWinLabSubLab.pack(side=TOP, pady=30)
          cle_verbal_memory = PhotoImage(file="textures/cles/cle_verbal_memory.png")
          CanvaCle = Canvas(MVRestartMainFrame, width=80, height=80)
          CanvaCle.pack(side=TOP)
          CanvaCle.create_image(0, 0, anchor=NW, image=cle_verbal_memory)
          CanvaCle.image = cle_verbal_memory

        #Si le joueur a perdu (moins de 50 points)
        else:
          MVLoseLab = Label(MVRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
          MVLoseLab.pack(side=TOP)
          diff = (50 - score)
          if diff > 1:
            MVLoseLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire Verbale"), font=("Arial", 10))
          else:
            MVLoseLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} point pour obtenir la clé de Mémoire Verbale"), font=("Arial", 10))
          MVLoseLabSubLab.pack(side=TOP, pady=30)
      else:
        #Si le joueur a gagné (au moins 25 points)
        if score >= 25:
          MVWinLab = Label(MVRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
          MVWinLab.pack(side=TOP)
          MVWinLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore} !\n Vous obtenez la clé de la Mémoire Verbale !"), font=("Arial", 10))
          MVWinLabSubLab.pack(side=TOP, pady=30)
          cle_verbal_memory = PhotoImage(file="textures/cles/cle_verbal_memory.png")
          CanvaCle = Canvas(MVRestartMainFrame, width=80, height=80)
          CanvaCle.pack(side=TOP)
          CanvaCle.create_image(0, 0, anchor=NW, image=cle_verbal_memory)
          CanvaCle.image = cle_verbal_memory

        #Si le joueur a perdu (moins de 25 points)
        else:
          MVLoseLab = Label(MVRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
          MVLoseLab.pack(side=TOP)
          diff = (25 - score)
          if diff > 1:
            MVLoseLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire Verbale"), font=("Arial", 10))
          else:
            MVLoseLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} point pour obtenir la clé de Mémoire Verbale"), font=("Arial", 10))
          MVLoseLabSubLab.pack(side=TOP, pady=30)

      MVRestartButtons = Frame(MVRestartFrame, relief=GROOVE)
      MVRestartButtons.pack(side=TOP, pady=10)
      MVRestartButton = Button(MVRestartButtons, text="Recommencer", command=mvrestart, background="aquamarine1")
      MVRestartButton.pack(side=LEFT, padx=20, pady=10)
      MVQuitButton = Button(MVRestartButtons, text="Quitter", command=mv_quit, background="aquamarine1")
      MVQuitButton.pack(side=RIGHT, padx=20, pady=10)


    #Fonction qui met à jour le nombre de coeur en fonction du nombre de vies restantes
    def MVcheck_vie():
      global mvvies
      if mvvies == 2:
        CanvaVie3.delete(ThreeHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=TwoHearts)
        CanvaVie3.pack(side=BOTTOM)
      elif mvvies == 1:
        CanvaVie3.delete(TwoHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=OneHeart)
        CanvaVie3.pack(side=BOTTOM)
      elif mvvies == 0:
        restart_mv()


    #Lancement du jeu de mémoire verbale
    def VerbalMemoryStart():
      global mvvies
      global mvcoup
      mvvies = 3
      mvcoup=0
      StartBTN.destroy()
      FrameWord.pack(side=TOP)
      nouveaumotBTN.pack(side=RIGHT, padx=20)
      dejavuBTN.pack(side=LEFT, padx=20)
      mot = choice_mot()
      motVar.set(mot)

    #Fonction pour choisir un mot
    def choice_mot():
      with open("ressources/liste_francais.txt", "r", encoding='utf-8') as fichier:
        dico_FR = fichier.read().splitlines()
        chosen_word = random.choice(dico_FR)
      return chosen_word

    #Fonction si le joueur a cliqué sur le bouton déjà vu
    def check_dejavu ():
      global mvvies
      global mvcoup
      global MVHighestScore
      if mvcoup>0:
        randomizer = random.randint(0,11)
        if motVar.get() in SeenWords:
          score = mvscore.get()
          score += 1
          mvscore.set(score)
          if score >= MVHighestScore:
            MVHighestScore = score
            mvHighestScore.set(score)
          MVcheckScore()
        else:
          SeenWords.append(motVar.get())
          mvvies -= 1
          MVcheck_vie()

        if randomizer <= 5 or len(SeenWords)<=1:
          mot = choice_mot()
          motVar.set(mot)
        else:
          verif=False
          while verif==False:
            mot = random.choice(SeenWords)
            mot2 = motVar.get()
            if mot!=mot2:
              verif=True
          motVar.set(mot)
        mvcoup+=1
      else:
        mvvies -= 1
        MVcheck_vie()
        mot = choice_mot()
        motVar.set(mot)
        mvcoup+=1

    #Fonction si le joueur a cliqué sur nouveau mot
    def check_nouveau_mot ():
      global mvcoup
      global mvvies
      global MVHighestScore
      if mvcoup>0:
        randomizer = random.randint(0,11)
        if motVar.get() in SeenWords:
          mvvies -= 1
          MVcheck_vie()
        else:
          score = mvscore.get()
          score += 1
          if score >= MVHighestScore:
            MVHighestScore = score
            mvHighestScore.set(score)
          mvscore.set(score)
          SeenWords.append(motVar.get())
          MVcheckScore()
        if randomizer <= 5 or len(SeenWords)<=1:
          mot = choice_mot()
          motVar.set(mot)
        else:
          verif=False
          while verif==False:
            mot = random.choice(SeenWords)
            mot2 = motVar.get()
            if mot!=mot2:
              verif=True
          motVar.set(mot)
        mvcoup+=1
      else:
        mot = choice_mot()
        motVar.set(mot)
        mvcoup+=1
        score = mvscore.get()
        score += 1
        if score >= MVHighestScore:
          MVHighestScore = score
          mvHighestScore.set(score)
        mvscore.set(score)
        MVcheckScore()

    #Affiches les règles de la mémoire verbale dans une nouvellle fenêtre
    def MVreglesPrint():
      def MVregles_quit():
        MVregles.destroy()
      MVregles = Tk()
      MVregles.title("Règles | Mémoire Verbale")
      MVregles.geometry("250x200")
      MVreglesText = Label(MVregles, text="Bienvenue dans le jeu Mémoire Verbale \n Les règles de ce jeu sont simples: \n Vous devez indiquer si vous avez déjà \n vu le mot qui apparait grâce \n aux boutons 'Déjà Vu' et \n 'Nouveau Mot'. Vous devez obtenir \n 50 poits pour récupérer la \n clé de l'épreuve. \n Vous pouvez obtenir un \neaster egg si vous parvenez à \nun certain nombre de points. \n Bonne chance !")
      MVreglesText.pack(side=TOP, padx=10, pady=10)
      MVreglesButton = Button(MVregles, text="OK", command=MVregles_quit, background="aquamarine1")
      MVreglesButton.pack(side=BOTTOM, padx=10, pady=10)
      MVregles.mainloop()

    #Fonction qui compare le score de mémoire verbale avec certaines valeurs (victoire et easter egg)
    def MVcheckScore():
      if difficulte == True:
        if mvscore.get() == 50:
          key_verbal_memory = True
          verbal_memory_reussi()
        elif mvscore.get() == 75:
          verbal_memory_hint()
      else:
        if mvscore.get() == 25:
          key_verbal_memory = True
          verbal_memory_reussi()
        elif mvscore.get() == 50:
          verbal_memory_hint() 

    #Fonction pour donner un indice sur un easter egg si le joueur atteint 75 points dans la mémoire verbale dans une nouvelle fenêtre
    def verbal_memory_hint():

      #Fonction pour quitter la fenêtre d'indice
      def mvindice_quit():
        MVIndice.destroy()

      MVIndice = Tk()
      MVIndice.title("INDICE N°1 |Mémoire Verbale")
      MVIndice.geometry("400x200")
      MVIndiceMainFrame = Frame(MVIndice, borderwidth=1, relief=GROOVE)
      MVIndiceMainFrame.pack(side=TOP)
      if difficulte == True:
        MVIndiceText = Label(MVIndiceMainFrame, text="Bravo pour avoir atteint 75 points dans le jeu de mémoire verbale,\n voici un indice pour accéder a une salle secrète:")
      else:
        MVIndiceText = Label(MVIndiceMainFrame, text="Bravo pour avoir atteint 50 points dans le jeu de mémoire verbale,\n voici un indice pour accéder a une salle secrète:") 
      MVIndiceText.pack(side=TOP, padx=5)
      MVIndiceIndice = Label(MVIndiceMainFrame, text="w Iecnozasax etpoq alfltymir ...")
      MVIndiceIndice.pack(side=BOTTOM, padx=5, pady= 10)
      MVIndiceButton = Button(MVIndice, text="Quitter", command=mvindice_quit, background="aquamarine1")
      MVIndiceButton.pack(side=BOTTOM)
      MVIndice.mainloop()

    #Fonction qui donne la clé de mémoire verbale si le joueur atteint 50 points dans une nouvelle fenêtre
    def verbal_memory_reussi():
      #Fonction pour quitter la fenêtre d'annonce de victoire
      def mvreussi_quit():
        MVReussi.destroy()

      MVReussi = Tk()
      MVReussi.title("Réussite | Mémoire Verbale")
      MVReussi.geometry("400x150")
      MVReussiText = Label(MVReussi, text="Bravo, vous avez réussi l'épreuve de mémoire \n verbale et avez obtenu une clé !")
      MVReussiText.pack(side=TOP, padx=15, pady=25)
      MVReussiButton = Button(MVReussi, text="OK", command=mvreussi_quit, background="aquamarine1")
      MVReussiButton.pack(side=BOTTOM, padx=15, pady=15)
      MVReussi.mainloop()


    #TKINTER MEMOIRE VERBALE

    #On crée notre fenêtre de mémoire verbale
    MVFrame = Tk()

    #On crée les variables Tkinter de mémoire verbale
    mvHighestScore = IntVar()
    motVar = StringVar()
    mvscore = IntVar()
    MVFrame.title("Mémoire Verbale | Memory Game")
    MVFrame.geometry("600x500")

    #On crée les différents éléments de la fenêtre
    FrameInfos = Frame(MVFrame, relief=GROOVE, borderwidth=1)
    FrameInfos.pack(side=TOP, padx=5)
    MemoireVerbaleLabel = Label(FrameInfos, text="Mémoire Verbale", font=("Arial",30))
    MemoireVerbaleLabel.pack(padx=5, pady=5)

    MVReglesBTN = Button(FrameInfos, text="Règles", font=("Arial", 10), command=MVreglesPrint, background="aquamarine1")
    MVReglesBTN.pack(side=RIGHT)

    MVScoreLabelTxt = Label(FrameInfos, text="Score :", font=("Arial", 10))
    MVScoreLabelTxt.pack(side=LEFT)
    MVScoreLabel = Label(FrameInfos, textvariable=mvscore, font=("Arial", 10))
    MVScoreLabel.pack(side=LEFT)
    MVHighestScoreLabelTxt = Label(FrameInfos, text="Meilleur Score :", font=("Arial", 10))
    MVHighestScoreLabelTxt.pack(side=LEFT)
    MVHighestScoreLabel = Label(FrameInfos, textvariable=mvHighestScore, font=("Arial", 10))
    MVHighestScoreLabel.pack(side=LEFT)

    FrameJeu = Frame(MVFrame, borderwidth=1, relief=GROOVE)
    FrameJeu.pack(pady=50, padx=10, side=TOP)
    StartBTN = Button(FrameJeu, command=VerbalMemoryStart, text="Commencer")
    StartBTN.pack(side=TOP)

    FrameWord = Frame(FrameJeu, relief=GROOVE)
    CurrentWord = Label(FrameWord, textvariable=motVar, font=("Arial", 15))
    CurrentWord.pack(side=TOP, pady=20)

    dejavuBTN = Button(FrameJeu, text="Déjà Vu", command=check_dejavu, background="azure", font=("Arial", 10))
    nouveaumotBTN = Button(FrameJeu, text="Nouveau Mot", command=check_nouveau_mot, background="azure", font=("Arial",10))

    LicenseLabel = Label(MVFrame, text="Memory Game, Thomas KELEMEN & Gabriel CADEAU-FLAUJAT \n © Tous droits réservés. 2024 ")
    LicenseLabel.pack(side=BOTTOM)

    FrameVie = Frame(MVFrame, borderwidth=1, relief=GROOVE)
    FrameVie.pack(side=BOTTOM, pady=60)
    ThreeHearts = PhotoImage(file="textures/vie/3hearts.png")
    TwoHearts = PhotoImage(file="textures/vie/2hearts.png")
    OneHeart = PhotoImage(file="textures/vie/1heart.png")
    CanvaVie3 = Canvas(FrameVie, width=ThreeHearts.width(), height=ThreeHearts.height())
    CanvaVie3.create_image(0, 0, anchor=NW, image=ThreeHearts)
    CanvaVie3.pack(side=BOTTOM)

    #On donne la valeur du meilleur score de mémoire verbale à la variable tKinter de même nom
    mvHighestScore.set(MVHighestScore)

    #On lance l'éxécution de la fenêtre de mémoire verbale
    MVFrame.mainloop()

  #FONCTION MEMOIRE IMAGES
  def images_memory_start():
    #On remet les coordonnées à zéro
    reset_coords()
    #On crée on liste vide qui contiendra les images qui sont déjà apparues
    global SeenPics
    SeenPics = []
    #On crée les variables globales current_image et current_image_id qui vont contenir et afficher les images
    global current_image, current_image_id
    current_image = None
    current_image_id = None

    #Fonction pour gérer la fin de mémoire des images
    def restart_mi():
      #Fonction pour relancer une partie de mémoire des images
      def mirestart():
        MIRestartFrame.destroy()
        images_memory_start()
      #Fonction pour quitter la mémoire des images et relancer le script principal
      def mi_quit():
        MIRestartFrame.destroy()
        script()

      #Fenêtre de fin de partie de mémoire des images
      MIFrame.destroy()
      MIRestartFrame = Tk()
      MIRestartFrame.title("Partie Terminée | Mémoire des Images")
      MIRestartFrame.geometry("600x350")
      MIRestartFrameTitle = Frame(MIRestartFrame, relief=GROOVE)
      MIRestartFrameTitle.pack(side=TOP)
      MIRestartTitleLabel = Label(MIRestartFrameTitle, text="Partie Terminée !", font=("Arial", 20))
      MIRestartTitleLabel.pack()
      MIRestartMainFrame = Frame(MIRestartFrame, relief=GROOVE)
      MIRestartMainFrame.pack(side=TOP)
      score = miscore.get()
      #Si le joueur a gagné la partie (au moins 50 points)
      if difficulte == True:
        if score >= 50:
          MIWinLab = Label(MIRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
          MIWinLab.pack(side=TOP)
          MIWinLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore} !\n Vous obtenez la clé de la Mémoire des Images !"), font=("Arial", 10))
          MIWinLabSubLab.pack(side=TOP, pady=30)
          cle_images_memory = PhotoImage(file="textures/cles/cle_images_memory.png")
          CanvaCle = Canvas(MIRestartMainFrame, width=80, height=80)
          CanvaCle.pack(side=TOP)
          CanvaCle.create_image(0, 0, anchor=NW, image=cle_images_memory)
          CanvaCle.image = cle_images_memory

        #Si le joueur a perdu la partie (moins de 50 points)
        else:
          MILoseLab = Label(MIRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
          MILoseLab.pack(side=TOP)
          diff = (50 - score)
          if diff > 1:
            MILoseLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore}!\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire des Images"), font=("Arial", 10))
          else:
            MILoseLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore}!\n Encore un petit effort, il vous manquait\n {diff} point pour obtenir la clé de Mémoire des Images"), font=("Arial", 10))
          MILoseLabSubLab.pack(side=TOP, pady=30)

      #Si le joueur a gagné la partie (au moins 25 points)
      else:
        if score >= 25:
          MIWinLab = Label(MIRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
          MIWinLab.pack(side=TOP)
          MIWinLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore} !\n Vous obtenez la clé de la Mémoire des Images !"), font=("Arial", 10))
          MIWinLabSubLab.pack(side=TOP, pady=30)
          cle_images_memory = PhotoImage(file="textures/cles/cle_images_memory.png")
          CanvaCle = Canvas(MIRestartMainFrame, width=80, height=80)
          CanvaCle.pack(side=TOP)
          CanvaCle.create_image(0, 0, anchor=NW, image=cle_images_memory)
          CanvaCle.image = cle_images_memory

        #Si le joueur a perdu la partie (moins de 25 points)
        else:
          MILoseLab = Label(MIRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
          MILoseLab.pack(side=TOP)
          diff = (25 - score)
          if diff > 1:
            MILoseLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore}!\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire des Images"), font=("Arial", 10))
          else:
            MILoseLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore}!\n Encore un petit effort, il vous manquait\n {diff} point pour obtenir la clé de Mémoire des Images"), font=("Arial", 10))
          MILoseLabSubLab.pack(side=TOP, pady=30)
      MIRestartButtons = Frame(MIRestartFrame, relief=GROOVE)
      MIRestartButtons.pack(side=TOP, pady=10)
      MIRestartButton = Button(MIRestartButtons, text="Recommencer", command=mirestart, background="aquamarine1")
      MIRestartButton.pack(side=LEFT, padx=20, pady=10)
      MIQuitButton = Button(MIRestartButtons, text="Quitter", command=mi_quit, background="aquamarine1")
      MIQuitButton.pack(side=RIGHT, padx=20, pady=10)


    #Fonction qui met à jour les coeurs et ferme le jeu si la vie arrive à 0
    def MIcheck_vie():
      global mivies
      if mivies == 2:
        CanvaVie3.delete(ThreeHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=TwoHearts)
        CanvaVie3.pack(side=BOTTOM)
      elif mivies == 1:
        CanvaVie3.delete(TwoHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=OneHeart)
        CanvaVie3.pack(side=BOTTOM)
      elif mivies == 0:
        restart_mi()


    #Lancement du jeu de mémoire des images
    def ImagesMemoryStart():
      global mivies, micoup
      mivies = 3
      micoup=0
      StartBTN.destroy()
      FrameCanvaPic.pack(side=TOP)
      nouvelleimageBTN.pack(side=RIGHT, padx=20)
      dejavuBTN.pack(side=LEFT, padx=20)
      CanvaPic.delete("all")
      current_image_id = CanvaPic.create_image(0, 0, image=current_image, anchor=NW)
      SeenPics = []



    #Fonction pour choisir une image
    def choice_image():
      global micoup, SeenPics, current_image_indice
      randomizer = random.randint(0,11)
      if (randomizer <= 5) and len(SeenPics)>1:
        verif = False
        while verif == False:
          indice = random.choice(SeenPics)
          if indice != current_image_indice:
            verif = True
        current_image = PhotoImage(file=image_chemin[indice])
        current_path = image_chemin[indice]
        for i in range(len(image_chemin)):
          if image_chemin[i] == current_path:
            current_image_indice = i
      else:
        current_path = random.choice(image_chemin)
        for i in range(len(image_chemin)):
          if image_chemin[i] == current_path:
            current_image_indice = i
        current_image = PhotoImage(file=current_path)
      CanvaPic.delete("all")
      current_image_id = CanvaPic.create_image(0, 0, image=current_image, anchor=NW)
      CanvaPic.image = current_image

    #Fonction si le joueur a cliqué sur le bouton déjà vu
    def micheck_dejavu ():
      global mivies, micoup, MIHighestScore, SeenPics, current_image_indice
      if micoup > 0:
        if current_image_indice in SeenPics:
          score = miscore.get()
          score += 1
          miscore.set(score)
          if score >= MIHighestScore:
            MIHighestScore = score
            miHighestScore.set(score)
          MIcheckScore()
        else:
          SeenPics.append(current_image_indice)
          mivies -= 1
          MIcheck_vie()
        choice_image()
      else:
        mivies -= 1
        MIcheck_vie()
        micoup += 1
        choice_image()

    #Fonction si le joueur a cliqué sur nouvelle image
    def check_nouvelle_image ():
      global micoup, mivies, MIHighestScore, SeenPics, current_image_indice
      if micoup > 0:
        if current_image_indice in SeenPics:
          mivies -= 1
          MIcheck_vie()
        else:
          score = miscore.get()
          score += 1
          miscore.set(score)
          SeenPics.append(current_image_indice)
          if score >= MIHighestScore:
            MIHighestScore = score
            miHighestScore.set(score)
          MIcheckScore()
        choice_image()
      else:
          score = miscore.get()
          score += 1
          micoup += 1
          SeenPics.append(current_image_indice)
          choice_image() 
          miscore.set(score)
          if score >= MIHighestScore:
            MIHighestScore = score
            miHighestScore.set(score)
          MIcheckScore()

    #Affiches les règles de la mémoire des images dans une nouvellle fenêtre
    def MIreglesPrint():
      def MIregles_quit():
        MIregles.destroy()
      MIregles = Tk()
      MIregles.title("Règles | Mémoire des Images")
      MIregles.geometry("250x200")

      MIreglesText = Label(MIregles, text="Bienvenue dans le jeu Mémoire des Images \n Les règles de ce jeu sont simples: \n Vous devez indiquer si vous avez déjà \n vu l'image qui apparait grâce \n aux boutons 'Déjà Vu' et \n 'Nouvelle Image'. Vous devez obtenir \n 50 poits pour récupérer la \n clé de l'épreuve. \n Vous pouvez obtenir un \neaster egg si vous parvenez à \nun certain nombre de points. \n Bonne chance !")
      MIreglesText.pack(side=TOP, padx=10, pady=10)

      MIreglesButton = Button(MIregles, text="OK", command=MIregles_quit, background="aquamarine1")
      MIreglesButton.pack(side=BOTTOM, padx=10, pady=10)

      MIregles.mainloop()

    #Fonction qui s'active si on a 50 ou 75 points
    def MIcheckScore():
      if difficulte == True:
        if miscore.get() == 50:
          key_images_memory = True
          images_memory_reussi()
        elif miscore.get() == 75:
          images_memory_hint()
      else:
        if miscore.get() == 25:
          key_images_memory = True
          images_memory_reussi()
        elif miscore.get() == 50:
          images_memory_hint()


    #Fonction qui donne un indice un easter egg si on a 75 points dans une nouvelle fenêtre
    def images_memory_hint():
      #Fonction pour quitter la fenêtre d'indice
      def miindice_quit():
        MIIndice.destroy()

      MIIndice = Tk()
      MIIndice.title("INDICE N°2 |Mémoire des Images")
      MIIndice.geometry("400x200")
      MIIndiceMainFrame = Frame(MIIndice, borderwidth=1, relief=GROOVE)
      MIIndiceMainFrame.pack(side=TOP)
      if difficulte == True:
        MIIndiceText = Label(MIIndiceMainFrame, text="Bravo pour avoir atteint 75 points dans le jeu de mémoire des images,\n voici un indice pour accéder a une salle secrète:")
      else:
        MIIndiceText = Label(MIIndiceMainFrame, text="Bravo pour avoir atteint 50 points dans le jeu de mémoire des images,\n voici un indice pour accéder a une salle secrète:")
      
      MIIndiceText.pack(side=TOP, padx=5)
      MIIndiceIndice = Label(MIIndiceMainFrame, text="... ijcnsjrguvy togkt zshmifhdg,a ...")
      MIIndiceIndice.pack(side=BOTTOM, padx=5, pady= 10)
      MIIndiceButton = Button(MIIndice, text="Quitter", command=miindice_quit, background="aquamarine1")
      MIIndiceButton.pack(side=BOTTOM)
      MIIndice.mainloop()

    #Fonction qui donne la clé de mémoire des images si on a 50 points dans une nouvelle fenêtre
    def images_memory_reussi():
      #Fonction qui ferme la fenêtre de victoire de mémoire des images
      def mireussi_quit():
        MIReussi.destroy()

      MIReussi = Tk()
      MIReussi.title("Réussite | Mémoire des Images")
      MIReussi.geometry("400x150")
      MIReussiText = Label(MIReussi, text="Bravo, vous avez réussi l'épreuve de mémoire \n des images et avez obtenu une clé !")
      MIReussiText.pack(side=TOP, padx=15, pady=25)
      MIReussiButton = Button(MIReussi, text="OK", command=mireussi_quit, background="aquamarine1")
      MIReussiButton.pack(side=BOTTOM, padx=15, pady=15)
      MIReussi.mainloop()


    #TKINTER MEMOIRE DES IMAGES

    #On crée la fenêtre de mémoire des images
    MIFrame = Tk()

    #On crée les variables Tkinter de mémoire des images
    miHighestScore = IntVar()
    miscore = IntVar()

    #On crée une liste vide qui va contenir le chemin de toutes les images de la mémoire des images
    image_chemin = []

    #On met dans une liste le chemin de toutes les images de la mémoire des images
    for i in range(150):
      image_chemin.append(f"ressources/images/image_{i}.png")

    #On défini le chemin de l'image actuel comme un élément aléatoire de al liste des chemins
    current_path = random.choice(image_chemin)
    for i in range(len(image_chemin)):
      if image_chemin[i] == current_path:
        global current_image_indice
        current_image_indice = i


    #On charge l'image qui a pour chemin current_path
    current_image = PhotoImage(file=current_path)


    MIFrame.title("Mémoire des Images | Memory Game")
    MIFrame.geometry("600x500")

    #On crée les différents éléments Tkinter de la mémoire des images
    FrameInfos = Frame(MIFrame, relief=GROOVE, borderwidth=1)
    FrameInfos.pack(side=TOP, padx=5)
    MemoireImagesLabel = Label(FrameInfos, text="Mémoire des Images", font=("Arial",30))
    MemoireImagesLabel.pack(padx=5, pady=5)
    MIReglesBTN = Button(FrameInfos, text="Règles", font=("Arial", 10), command=MIreglesPrint, background="aquamarine1")
    MIReglesBTN.pack(side=RIGHT)

    MIScoreLabelTxt = Label(FrameInfos, text="Score :", font=("Arial", 10))
    MIScoreLabelTxt.pack(side=LEFT)
    MIScoreLabel = Label(FrameInfos, textvariable=miscore, font=("Arial", 10))
    MIScoreLabel.pack(side=LEFT)
    MIHighestScoreLabelTxt = Label(FrameInfos, text="Meilleur Score :", font=("Arial", 10))
    MIHighestScoreLabelTxt.pack(side=LEFT)
    MIHighestScoreLabel = Label(FrameInfos, textvariable=miHighestScore, font=("Arial", 10))
    MIHighestScoreLabel.pack(side=LEFT)

    FrameJeu = Frame(MIFrame, borderwidth=1, relief=GROOVE)
    FrameJeu.pack(pady=50, padx=10, side=TOP)
    StartBTN = Button(FrameJeu, command=ImagesMemoryStart, text="Commencer")
    StartBTN.pack(side=TOP)



    FrameCanvaPic = Frame(FrameJeu, relief=GROOVE)
    CanvaPic = Canvas(FrameCanvaPic, width=80, height=80)
    CanvaPic.pack(side=TOP, pady=20)
    dejavuBTN = Button(FrameJeu, text="Déjà Vu", command=micheck_dejavu, background="azure", font=("Arial", 10))
    nouvelleimageBTN = Button(FrameJeu, text="Nouvelle Image", command=check_nouvelle_image, background="azure", font=("Arial",10))

    FrameVie = Frame(MIFrame, relief=GROOVE, borderwidth=1)
    FrameVie.pack(side=TOP, pady=25)
    ThreeHearts = PhotoImage(file="textures/vie/3hearts.png")
    TwoHearts = PhotoImage(file="textures/vie/2hearts.png")
    OneHeart = PhotoImage(file="textures/vie/1heart.png")
    CanvaVie3 = Canvas(FrameVie, width=ThreeHearts.width(), height=ThreeHearts.height())
    CanvaVie3.create_image(0, 0, anchor=NW, image=ThreeHearts)
    CanvaVie3.pack(side=BOTTOM)

    LicenseLabel = Label(MIFrame, text="Memory Game, Thomas KELEMEN & Gabriel CADEAU-FLAUJAT \n © Tous droits réservés. 2024 ")
    LicenseLabel.pack(side=BOTTOM)
    

    #On donne la valeur du meilleur score de mémoire des images à la variable tKinter de même nom
    miHighestScore.set(MIHighestScore)

    #On fait tourner la fenêtre de mémoire des images
    MIFrame.mainloop()

  #FONCTION MEMOIRE NOMBRES
  def MN_start():
    #On remet les coordonnées à 0
    reset_coords()

    #Fin de partie
    def restart_mn():

      #Relance la frame
      def mnrestart():
        MNRestartFrame.destroy()
        MN_start()
      
      #Réouvre la fenêtre principale
      def mn_quit():
        MNRestartFrame.destroy()
        script()
      
      #Fenêtre de fin de partie
      MNFrame.destroy()
      MNRestartFrame = Tk()
      MNRestartFrame.title("Partie Terminée | Mémoire des Nombres")
      MNRestartFrame.geometry("600x350")
      MNRestartFrameTitle = Frame(MNRestartFrame, relief=GROOVE)
      MNRestartFrameTitle.pack(side=TOP)
      MNRestartTitleLabel = Label(MNRestartFrameTitle, text="Partie Terminée !", font=("Arial", 20))
      MNRestartTitleLabel.pack()
      MNRestartMainFrame = Frame(MNRestartFrame, relief=GROOVE)
      MNRestartMainFrame.pack(side=TOP)
      score = mnscore.get()
      if difficulte == True:

        if score >= 10:
          MNWinLab = Label(MNRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
          MNWinLab.pack(side=TOP)
          MNWinLabSubLab = Label(MNRestartMainFrame, text=(f"Votre meilleur score est {MNHighestScore} !\n Vous obtenez la clé de la Mémoire des Nombres!"), font=("Arial", 10))
          MNWinLabSubLab.pack(side=TOP, pady=30)
          cle_number_memory = PhotoImage(file="textures/cles/cle_number_memory.png")
          CanvaCle = Canvas(MNRestartMainFrame, width=80, height=80)
          CanvaCle.pack(side=TOP)
          CanvaCle.create_image(0, 0, anchor=NW, image=cle_number_memory)
          CanvaCle.image = cle_number_memory
          
        else:
          MNLoseLab = Label(MNRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
          MNLoseLab.pack(side=TOP)
          diff = (10 - score)
          if diff > 1:
            MVLoseLabSubLab = Label(MNRestartMainFrame, text=(f"Votre meilleur score est {MNHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire des Nombres"), font=("Arial", 10))
          else:
            MVLoseLabSubLab = Label(MNRestartMainFrame, text=(f"Votre meilleur score est {MNHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} point pour obtenir la clé de Mémoire des Nombres"), font=("Arial", 10))
          MVLoseLabSubLab.pack(side=TOP, pady=30)
      else:
        if score >= 7:
          MNWinLab = Label(MNRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
          MNWinLab.pack(side=TOP)
          MNWinLabSubLab = Label(MNRestartMainFrame, text=(f"Votre meilleur score est {MNHighestScore} !\n Vous obtenez la clé de la Mémoire des Nombres !"), font=("Arial", 10))
          MNWinLabSubLab.pack(side=TOP, pady=30)
          cle_number_memory = PhotoImage(file="textures/cles/cle_number_memory.png")
          CanvaCle = Canvas(MNRestartMainFrame, width=80, height=80)
          CanvaCle.pack(side=TOP)
          CanvaCle.create_image(0, 0, anchor=NW, image=cle_number_memory)
          CanvaCle.image = cle_number_memory

        else:
          MNLoseLab = Label(MNRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
          MNLoseLab.pack(side=TOP)
          diff = (7 - score)
          if diff > 1:
            MVLoseLabSubLab = Label(MNRestartMainFrame, text=(f"Votre meilleur score est {MNHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire des Nombres"), font=("Arial", 10))
          else:
            MVLoseLabSubLab = Label(MNRestartMainFrame, text=(f"Votre meilleur score est {MNHighestScore} !\n Encore un petit effort, il vous manquait\n {diff} point pour obtenir la clé de Mémoire des Nombres"), font=("Arial", 10))
          MVLoseLabSubLab.pack(side=TOP, pady=30)

      MNRestartButtons = Frame(MNRestartFrame, relief=GROOVE)
      MNRestartButtons.pack(side=TOP, pady=10)
      MNRestartButton = Button(MNRestartButtons, text="Recommencer", command=mnrestart, background="aquamarine1")
      MNRestartButton.pack(side=LEFT, padx=20, pady=10)
      MNQuitButton = Button(MNRestartButtons, text="Quitter", command=mn_quit, background="aquamarine1")
      MNQuitButton.pack(side=RIGHT, padx=20, pady=10)

    #Fonction qui compare le score de mémoire des nombres avec certaines valeurs (victoire et easter egg)
    def MNcheckScore():
      if difficulte == True:
        if mnscore.get() == 10:
          key_number_memory = True
          number_memory_reussi()
        elif mnscore.get() == 12:
          number_memory_hint()
      else:
        if mnscore.get() == 7:
          key_number_memory = True
          number_memory_reussi()
        elif mnscore.get() == 10:
          number_memory_hint()
    
    #Fonction pour donner un indice sur un easter egg si le joueur atteint 12 points dans la mémoire des nombres dans une nouvelle fenêtre
    def number_memory_hint():

      #Fonction pour quitter la fenêtre d'indice
      def mnindice_quit():
        MNIndice.destroy()

      MNIndice = Tk()
      MNIndice.title("INDICE N°3 |Mémoire des Nombres")
      MNIndice.geometry("400x200")
      MNIndiceMainFrame = Frame(MNIndice, borderwidth=1, relief=GROOVE)
      MNIndiceMainFrame.pack(side=TOP)
      if difficulte == True:
        MNIndiceText = Label(MNIndiceMainFrame, text="Bravo pour avoir atteint 12 points dans le jeu de mémoire des nombres,\n voici un indice pour accéder a une salle secrète:")
      else:
        MNIndiceText = Label(MNIndiceMainFrame, text="Bravo pour avoir atteint 10 points dans le jeu de mémoire des nombres,\n voici un indice pour accéder a une salle secrète:") 
      MNIndiceText.pack(side=TOP, padx=5)
      MNIndiceIndice = Label(MNIndiceMainFrame, text="... imtyamahl ggcjqlsdfcaphxu dbfgijo ...")
      MNIndiceIndice.pack(side=BOTTOM, padx=5, pady= 10)
      MNIndiceButton = Button(MNIndice, text="Quitter", command=mnindice_quit, background="aquamarine1")
      MNIndiceButton.pack(side=BOTTOM)
      MNIndice.mainloop()

    #Fonction qui donne la clé de mémoire des nombres si le joueur atteint 10 points dans une nouvelle fenêtre
    def number_memory_reussi():
      #Fonction pour quitter la fenêtre d'annonce de victoire
      def mnreussi_quit():
        MNReussi.destroy()

      key_number_memory = True
      MNReussi = Tk()
      MNReussi.title("Réussite | Mémoire des Nombres")
      MNReussi.geometry("400x150")
      MNReussiText = Label(MNReussi, text="Bravo, vous avez réussi l'épreuve de Mémoire \n des Nombres et avez obtenu une clé !")
      MNReussiText.pack(side=TOP, padx=15, pady=25)
      MNReussiButton = Button(MNReussi, text="OK", command=mnreussi_quit, background="aquamarine1")
      MNReussiButton.pack(side=BOTTOM, padx=15, pady=15)
      MNReussi.mainloop()

    #Affichage des règles
    def MNregles():
      print("coucou")

    #Lancement
    def NumberMemoryStart():
      global mncoup
      mncoup = 1
      StartBTN.destroy()
      FrameNumber.pack(side=TOP, pady=20)
      #MNentry.pack()
      MNcontinuerBTN.pack(pady=20)
      global nb
      nb = str(random.randint(0, 9))
      mnNb.set(nb)
      global mnverif
      mnverif = True

    #L'utilisateur appuie sur continuer
    def continuer():
      global mnverif
      global nb
      global mot
      global mncoup
      global MNHighestScore
      mot = mntexte.get()
      MNentry.delete(0, 'end')
      if mnverif == False:
        MNentry.pack_forget()
        if not mot:
          def quiterror():
            Frameerreur.destroy()
          Frameerreur = Tk()
          Frameerreur.title("Skill Issue ?")
          Frameerreur.geometry("300x100")
          erreurlabel = Label(Frameerreur, text="Veuillez entrer un nombre", font=("Arial", 15))
          erreurlabel.pack()
          erreurboutton = Button(Frameerreur, text='OK', command=quiterror, bg="aquamarine1")
          erreurboutton.pack(side=BOTTOM, pady=10)
          MNentry.pack()
          Frameerreur.mainloop()
        else:
          if mot==nb:
            score = mnscore.get()
            score+=1
            mnscore.set(score)
            if score > MNHighestScore:
              MNHighestScore = score
              mnHighestScore.set(score)
            nb = ""
            mncoup+=1
            for it in range(mncoup):
              nb+=str(random.randint(0, 9))
            mnNb.set(nb)
            mnverif = True
            MNcheckScore()
          else:
            restart_mn()
      else:
        MNentry.pack()
        mnNb.set("?")
        mnverif = False

    #création de la fenêtre
    MNFrame = Tk()

    #création des variables
    mnHighestScore = IntVar()
    mnscore = IntVar()
    mnNb = StringVar()
    mntexte = StringVar()
    MNFrame.title("Mémoire des Nombres | Memory Game")
    MNFrame.geometry("700x400")

    #création des éléments
    FrameInfos = Frame(MNFrame, relief=GROOVE, borderwidth=1)
    FrameInfos.pack(side=TOP, padx=5)
    MemoireNombreLabel = Label(FrameInfos, text="Mémoire des Nombres", font=("Arial",30))
    MemoireNombreLabel.pack(padx=5, pady=5)

    MNreglesBTN = Button(FrameInfos, text='Règles', font=("Arial", 10), command=MNregles, background="aquamarine1")
    MNreglesBTN.pack(side=RIGHT)

    MNScoreLabelTxt = Label(FrameInfos, text="Score :", font=("Arial", 10))
    MNScoreLabelTxt.pack(side=LEFT)
    MNscoreLabel = Label(FrameInfos, textvariable=mnscore, font=("Arial", 10))
    MNscoreLabel.pack(side=LEFT)
    MNHighestScoreLabelTxt = Label(FrameInfos, text="Meilleur Score :", font=("Arial", 10))
    MNHighestScoreLabelTxt.pack(side=LEFT)
    MNHighestScoreLabel = Label(FrameInfos, textvariable=mnHighestScore, font=("Arial", 10))
    MNHighestScoreLabel.pack(side=LEFT)

    StartBTN = Button(MNFrame, command=NumberMemoryStart, text="Commencer")
    StartBTN.pack(side=TOP, pady=50)

    FrameNumber = Frame(MNFrame, relief=GROOVE)
    CurrentNb = Label(FrameNumber, textvariable=mnNb, font=("Arial", 30))
    CurrentNb.pack(side=TOP, pady=20)

    MNentry = Entry(MNFrame, textvariable=mntexte, width=15)
    MNcontinuerBTN = Button(MNFrame, text="Continuer" ,command=continuer, background="azure", font=("Arial", 10))

    LicenseLabel = Label(MNFrame, text="Memory Game, Thomas KELEMEN & Gabriel CADEAU-FLAUJAT \n © Tous droits réservés. 2024 ")
    LicenseLabel.pack(side=BOTTOM)
    
    #On donne la valeur du meilleur score de la mémoire des nb
    mnHighestScore.set(MNHighestScore)

    #loop
    MNFrame.mainloop()

  #FONCTION MEMOIRES MP
  def MP_start():

    #Si le joueur possède les trois clés, on lance le jeu des mémoires MP
    if (key_images_memory == True) and (key_number_memory == True) and (key_verbal_memory == True):
      mainFrame.destroy()
      MPFrame = Tk()
      MPFrame.mainloop()
      MPFrame.title("Mémoire de Patterns | Memory Game")
      MPFrame.geometry("800x600")
    #Si le joueur ne possède pas toutes les clés, on crée une fenêtre qui affiche les scores à faire pour obtenir toutes les clés
    else:
      #Fonction qui ferme la fenêtre d'erreur
      def error_quit():
        Error.destroy()
      Error = Tk()
      
      IntMVHighestScore = IntVar(Error)
      IntMVHighestScore.set(MVHighestScore)
      IntMIHighestScore = IntVar(Error)
      IntMIHighestScore.set(MIHighestScore)
      IntMNHighestScore = IntVar(Error)
      IntMNHighestScore.set(MNHighestScore)

      Error.title("Erreur | Mémoires MP")
      Error.geometry("450x200")
      ErrorFrame = Frame(Error, borderwidth=1, relief=GROOVE)
      ErrorFrame.pack(side=TOP)
      ErrorLabel = Label(ErrorFrame, text="Erreur, il vous manque au moins une clé pour accéder \n à la salle des épreuves de Mémoire des Patterns.\n Complétez les objectifs suivants pour \n débloquer l'accès à la dernière épreuve:")
      ErrorLabel.pack(padx=10)
      ErrorMessagesFrame = Frame(Error, borderwidth=1, relief=GROOVE)

      if difficulte == True:

        ErrorFrameMV = Frame(ErrorMessagesFrame, relief=GROOVE)
        ErrorMVLabel1 = Label(ErrorFrameMV, text="Objectif à compléter pour obtenir la clé de mémoire verbale: (")
        ErrorMVLabel1.pack(side=LEFT)
        ErrorMVLabel2 = Label(ErrorFrameMV, textvariable=IntMVHighestScore)
        ErrorMVLabel2.pack(side=LEFT)
        ErrorMVLabel3 = Label(ErrorFrameMV, text="/ 50 )")
        ErrorMVLabel3.pack(side=LEFT)
        ErrorFrameMV.pack(side=TOP)

        ErrorFrameMI = Frame(ErrorMessagesFrame, relief=GROOVE)
        ErrorMILabel1 = Label(ErrorFrameMI, text="Objectif à compléter pour obtenir la clé de mémoire des images: (")
        ErrorMILabel1.pack(side=LEFT)
        ErrorMILabel2 = Label(ErrorFrameMI, textvariable=IntMIHighestScore)
        ErrorMILabel2.pack(side=LEFT)
        ErrorMILabel3 = Label(ErrorFrameMI, text="/ 50 )")
        ErrorMILabel3.pack(side=LEFT)
        ErrorFrameMI.pack(side=TOP)

        ErrorFrameMN = Frame(ErrorMessagesFrame, relief=GROOVE)
        ErrorMNLabel1 = Label(ErrorFrameMN, text="Objectif à compléter pour obtenir la clé de mémoire des nombres: (")
        ErrorMNLabel1.pack(side=LEFT)
        ErrorMNLabel2 = Label(ErrorFrameMN, textvariable=IntMNHighestScore)
        ErrorMNLabel2.pack(side=LEFT)
        ErrorMNLabel3 = Label(ErrorFrameMN, text="/ 10 )")
        ErrorMNLabel3.pack(side=LEFT)
        ErrorFrameMN.pack(side=TOP)

      else:
        ErrorFrameMV = Frame(ErrorMessagesFrame, relief=GROOVE)
        ErrorMVLabel1 = Label(ErrorFrameMV, text="Objectif à compléter pour obtenir la clé de mémoire verbale: (")
        ErrorMVLabel1.pack(side=LEFT)
        ErrorMVLabel2 = Label(ErrorFrameMV, textvariable=IntMVHighestScore)
        ErrorMVLabel2.pack(side=LEFT)
        ErrorMVLabel3 = Label(ErrorFrameMV, text="/ 25 )")
        ErrorMVLabel3.pack(side=LEFT)
        ErrorFrameMV.pack(side=TOP)

        ErrorFrameMI = Frame(ErrorMessagesFrame, relief=GROOVE)
        ErrorMILabel1 = Label(ErrorFrameMI, text="Objectif à compléter pour obtenir la clé de mémoire des images: (")
        ErrorMILabel1.pack(side=LEFT)
        ErrorMILabel2 = Label(ErrorFrameMI, textvariable=IntMIHighestScore)
        ErrorMILabel2.pack(side=LEFT)
        ErrorMILabel3 = Label(ErrorFrameMI, text="/ 25 )")
        ErrorMILabel3.pack(side=LEFT)
        ErrorFrameMI.pack(side=TOP)

        ErrorFrameMN = Frame(ErrorMessagesFrame, relief=GROOVE)
        ErrorMNLabel1 = Label(ErrorFrameMN, text="Objectif à compléter pour obtenir la clé de mémoire des nombres: (")
        ErrorMNLabel1.pack(side=LEFT)
        ErrorMNLabel2 = Label(ErrorFrameMN, textvariable=IntMNHighestScore)
        ErrorMNLabel2.pack(side=LEFT)
        ErrorMNLabel3 = Label(ErrorFrameMN, text="/ 7 )")
        ErrorMNLabel3.pack(side=LEFT)
        ErrorFrameMN.pack(side=TOP)

      ErrorMessagesFrame.pack(pady=15)
      ErrorQuitButton = Button(Error, text="OK", command=error_quit, background="aquamarine1")
      ErrorQuitButton.pack(side=BOTTOM, pady=5)

      #On lance la fenêtre d'erreur
      Error.mainloop()

  #FONCTION DE DEPLACEMENT
  def deplacement(event):
    #On définit en global les coordonnées du rectangle
    global coords
    #On définit la variable touche qui prend pour valeur la touche du clavier appuyée
    touche = event.keysym

    #Si la touche est la flèche du haut et que le sprite n'a pas déjà atteint le mur du haut, on monte de 20 pixels
    if touche == "Up" and coords[1] > 40:
        coords = (coords[0], coords[1] - 20)
        canva_tableau.coords(rectangle, coords[0], coords[1])
    #Si la touche est la flèche du bas et que le sprite n'a pas déjà atteint le mur du bas, on descend de 20 pixels
    elif touche == "Down" and coords[1] < 540:
        coords = (coords[0], coords[1] + 20)
        canva_tableau.coords(rectangle, coords[0], coords[1])
    #Si la touche est la flèche de droite et que le sprite n'a pas déjà atteint le mur de droite, on se déplace de 20 pixels à droite
    elif touche == "Right" and coords[0] < 740:
        coords = (coords[0] + 20, coords[1])
        canva_tableau.coords(rectangle, coords[0], coords[1])
    #Si la touche est la flèche de gauche et que le sprite n'a pas déjà atteint le mur de gauche, on se déplace de 20 pixels à gauche
    elif touche == "Left" and coords[0] > 40:
        coords = (coords[0] - 20, coords[1])
        canva_tableau.coords(rectangle, coords[0], coords[1])

    #Si la touche est "e", et que les coordonnées du sprite correspondent aux coordonnées des portes,
    #On appelle les différentes fonctions des jeux de mémoires et on remet les coordonnées à 0

    elif touche == "e":
        if (coords[0] == 40 and coords[1] == 300) or (coords[0] == 40 and coords[1] == 280):
            coords = (400,300)
            mainFrame.destroy()
            verbal_memory_start()
        elif (coords[0] == 740 and coords[1] == 300) or (coords[0] == 740 and coords[1] == 280):
            coords = (400, 300)
            mainFrame.destroy()
            MN_start()
        elif (coords[0] == 400 and coords[1] == 540) or (coords[0] == 380 and coords[1] == 540):
            coords = (400, 300)
            mainFrame.destroy()
            images_memory_start()
        elif (coords[0] == 400 and coords[1] == 40) or (coords[0] == 380 and coords[1] == 40):
            coords = (400, 300)
            MP_start()
    elif (touche == "a") and (coords[0] == 740) and (coords[1] == 40):
      coords = (400,300)
      mainFrame.destroy()
      easter_egg()

  def easter_egg():

    def deplacementEaster(event):
      global easterCoords, MapPixelArtEasterNoGaster, rectangleEaster

      linkCoords = [
        (100, 120),
        (120, 120),
        (140, 120),
        (160, 120),
        (100, 140),
        (120, 140),
        (140, 140),
        (160, 140),
        (100, 160),
        (120, 160),
        (140, 160),
        (160, 160),
        (100, 180),
        (120, 180),
        (140, 180),
        (160, 180)]

      pacmanCoords = [
        (480, 180),
        (500, 180),
        (520, 180),
        (540, 180),
        (480, 200),
        (500, 200),
        (520, 200),
        (540, 200),
        (480, 220),
        (500, 220),
        (520, 220),
        (540, 220),
        (480, 240),
        (500, 240),
        (520, 240),
        (540, 240)]

      marioCoords =  [
        (100, 540),
        (80, 540),
        (60, 540),
        (40, 540),
        (100, 520),
        (80, 520),
        (60, 520),
        (40, 520),
        (100, 500),
        (80, 500),
        (60, 500),
        (40, 500),
        (100, 480),
        (80, 480),
        (60, 480),
        (40, 480)]

      gasterCoords = [
        (680, 480),
        (700, 480),
        (720, 480),
        (740, 480),
        (680, 500),
        (700, 500),
        (720, 500),
        (740, 500),
        (680, 520),
        (700, 520),
        (720, 520),
        (740, 520),
        (680, 540),
        (700, 540),
        (720, 540),
        (740, 540),
      ]

      touche = event.keysym

        #Si la touche est la flèche du haut et que le sprite n'a pas déjà atteint le mur du haut, on monte de 20 pixels
      if touche == "Up" and easterCoords[1] > 40:
        easterCoords = (easterCoords[0], easterCoords[1] - 20)
        grid_easter.coords(rectangleEaster, easterCoords[0], easterCoords[1])
      #Si la touche est la flèche du bas et que le sprite n'a pas déjà atteint le mur du bas, on descend de 20 pixels
      elif touche == "Down" and easterCoords[1] < 540:
        easterCoords = (easterCoords[0], easterCoords[1] + 20)
        grid_easter.coords(rectangleEaster, easterCoords[0], easterCoords[1])
      #Si la touche est la flèche de droite et que le sprite n'a pas déjà atteint le mur de droite, on se déplace de 20 pixels à droite
      elif touche == "Right" and easterCoords[0] < 740:
        easterCoords = (easterCoords[0] + 20, easterCoords[1])
        grid_easter.coords(rectangleEaster, easterCoords[0], easterCoords[1])
      #Si la touche est la flèche de gauche et que le sprite n'a pas déjà atteint le mur de gauche, on se déplace de 20 pixels à gauche
      elif touche == "Left" and easterCoords[0] > 40:
        easterCoords = (easterCoords[0] - 20, easterCoords[1])
        grid_easter.coords(rectangleEaster, easterCoords[0], easterCoords[1])
      elif touche == "e":
        if (easterCoords[0] == 400 and easterCoords[1] == 40) or (easterCoords[0] == 380 and easterCoords[1] == 40):
          easterFrame.destroy()
          script()
        elif (easterCoords in linkCoords):
          def link_quit():
            LinkFrame.destroy()
          LinkFrame = Toplevel()
          LinkFrame.title("Link")
          LinkFrame.geometry("200x100")

          LinkLabel = Label(LinkFrame, text="Je voulais retrouver Zelda \nmais je me suis perdu !", font=("Arial", 10))
          LinkLabel.pack(padx=10)
          LinKQuitBtn = Button(LinkFrame, text="OK", command=link_quit, background="aquamarine1")
          LinKQuitBtn.pack(side=BOTTOM, pady=10)

          LinkFrame.mainloop()

        elif (easterCoords in pacmanCoords):
          def pacman_quit():
            pacmanFrame.destroy()
          pacmanFrame = Toplevel()
          pacmanFrame.title("Pac Man")
          pacmanFrame.geometry("200x100")

          pacmanLabel = Label(pacmanFrame, text="J'ai faim mais les \nfantômes n'existent plus !", font=("Arial", 10))
          pacmanLabel.pack(padx=10)
          pacmanQuitBtn = Button(pacmanFrame, text="OK", command=pacman_quit, background="aquamarine1")
          pacmanQuitBtn.pack(side=BOTTOM, pady=10)

          pacmanFrame.mainloop()


        elif (easterCoords in marioCoords):
          def mario_quit():
            marioFrame.destroy()
          marioFrame = Toplevel()
          marioFrame.title("Mario")
          marioFrame.geometry("200x100")

          marioLabel = Label(marioFrame, text="'Woohaaaa' \n(en italien)", font=("Arial", 10))
          marioLabel.pack(padx=10)
          marioQuitBtn = Button(marioFrame, text="OK", command=mario_quit, background="aquamarine1")
          marioQuitBtn.pack(side=BOTTOM, pady=10)

          marioFrame.mainloop()

        elif (easterCoords in gasterCoords):
          grid_easter.delete("all")
          grid_easter.create_image(0, 0, anchor=NW, image=MapPixelArtEasterNoGaster)
          rectangleEaster = grid_easter.create_image(easterCoords[0], easterCoords[1], image=sprite, anchor=NW)
          grid_easter.pack()

        
          
        
      
    #TKINTER SALLE EASTER EGGS#
    
    global easterCoords, MapPixelArtEasterNoGaster, rectangleEaster, sprite
    easterCoords = (400,300)

    #On crée la fenêtre principale
    easterFrame = Tk()
    easterFrame.title("Easter Egg | Memory Game")
    easterFrame.geometry("800x600")
    #On crée un tableau dans lequel le sprite se déplace
    FrameGrid = Frame(easterFrame)
    FrameGrid.pack(side=TOP)
    grid_easter = Canvas(FrameGrid, width=800, height=600)

    #On charge et importe les textures de la map
    MapPixelArtEaster = PhotoImage(file="textures/map_easter_gaster.png")
    MapPixelArtEasterNoGaster = PhotoImage(file="textures/map_easter.png")
    MapEasterGCast = grid_easter.create_image(0, 0, anchor=NW, image=MapPixelArtEaster)
    

    #On charge et importe les textures du sprite
    sprite = PhotoImage(file="textures/sprite.png")
    rectangleEaster = grid_easter.create_image(400, 300, image=sprite, anchor=NW)

    #On ajoute un écouteur d'évènement sur les touches du clavier, activant la fonction deplacement
    grid_easter.focus_set()
    grid_easter.bind("<Key>", deplacementEaster)

    grid_easter.pack()



    #On ouvre la fenêtre d'easter eggs
    easterFrame.mainloop()

  #TKINTER SALLE PRINCIPALE#

  #On crée la fenêtre principale
  mainFrame = Tk()
  mainFrame.title("Memory Game | Thomas & Gabriel")
  mainFrame.geometry("800x600")

  #On crée un tableau dans lequel le sprite se déplace
  canva_tableau = Canvas(mainFrame, width=800, height=600)

  #On charge et importe les textures de la map
  MapPixelArt = PhotoImage(file="textures/map_pixelart.png")
  canva_tableau.create_image(0, 0, anchor=NW, image=MapPixelArt)

  #On charge et importe les textures de l'ordinateur
  computer = PhotoImage(file="textures/map_elements/computer.png")
  canva_tableau.create_image(40, 40, image=computer, anchor=NW)

  #On charge et importe les textures du parchemin
  scroll = PhotoImage(file="textures/map_elements/scroll.png")
  canva_tableau.create_image(700, 160, image=scroll, anchor=NW)

  #On charge et importe les textures du sprite
  sprite = PhotoImage(file="textures/sprite.png")
  rectangle = canva_tableau.create_image(400, 300, image=sprite, anchor=NW)



  #On ajoute un écouteur d'évènement sur les touches du clavier, activant la fonction deplacement
  canva_tableau.focus_set()
  canva_tableau.bind("<Key>", deplacement)

  canva_tableau.pack()

  #On ouvre la fenêtre pincipale
  mainFrame.mainloop()

#FONCTION DU DEMARRAGE
def startGame():
  #Fonction qui affiche les credits du jeu dans une nouvelle fenêtre
  def credits():
    #Fonction qui ferme la fenêtre des crédits du jeu
    def credits_quit():
      credits.destroy()
    #On crée la fenêtre des crédits, ainsi que tous ses éléments
    credits = Tk()
    credits.title("Crédits | Memory Game")
    credits.geometry("400x300")
    creditsTitleFrame = Frame(credits, relief=GROOVE)
    creditsTitleFrame.pack(side=TOP)
    creditsTitleLabel = Label(creditsTitleFrame, text="Memory Game \n Crédits", font=("Arial", 15))
    creditsTitleLabel.pack()
    creditsTextFrame = Frame(credits, relief=GROOVE)
    creditsTextFrame.pack(fill=BOTH, expand=True)
    creditsText = Text(creditsTextFrame,   font=("Arial", 10), wrap=WORD)
    creditsText.pack(side=LEFT, fill=BOTH, expand=True, pady=10, padx=5)
    scrollbarCredits = Scrollbar(creditsTextFrame, orient=VERTICAL, command=creditsText.yview)
    scrollbarCredits.pack(side=RIGHT, fill=Y)
    
    creditsText.tag_configure("center", justify='center')
    creditsText.insert(END, "Le jeu 'Memory Game' a été réalisé par\nThomas KELEMEN & Gabriel CADEAU-FLAUJAT,\ndeux élèves de première NSI, passionnés par coder les idées de programmes leur passant par la tête.\nLe jeu 'Memory Game' a été inspiré de la plateforme de jeu 'Human Benchmark'.\n\n Développement :\n'Memory Game' a été développé entierement par Thomas KELEMEN et Gabriel CADEAU-FLAUJAT.\n\nTextures :\nLes texture de la map et des clés ont été réalisées par\n Gabriel CADEAU-FLAUJAT.\nCertaines textures, libres de droits vienent du site de ressources 'OpenGameArt'.\n\nRemerciements :\nUn grand merci à Cédric ESCOUTE, professeur de NSI, sans qui le projet n'aurait pas pu voir le jour.\nMerci à Quentin PLADEAU, qui a aidé sur l'aspect programmation du projet.\n\nInformations supplémentaires :\n'Memory Game' est un jeu programmé entièremment dans le language de programmation Python.\nL'aspect graphique du jeu a été assuré par al librairie Tkinter, native à Python\n\n'Memory Game' est un jeu soumis aux droits d'auteurs et est soumis à la propriété intellectuelle de\nThomas KELEMEN et Gabriel CADEAU-FLAUJAT\nCe jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.\nEn utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.\n \n","center")
    creditsText.config(state=DISABLED)
    creditsQuitButton = Button(creditsText, text="OK", command=credits_quit, background="aquamarine1")

    #Fonction qui fait défiler les éléments de creditsText
    def check_scroll(*args):
      creditsText.update_idletasks()
      # Obtenir la position actuelle de la scrollbar
      position = creditsText.yview()
      # Si la scrollbar est tout en bas (pos[1] == 1.0)
      if position[1] == 1.0:
          # Insérer le bouton si ce n'est pas déjà fait
          if not creditsQuitButton.winfo_ismapped():
              creditsQuitButton.pack(side=BOTTOM, anchor=S, pady=5)
      else:
          # Supprimer le bouton si la scrollbar n'est pas tout en bas
          if creditsQuitButton.winfo_ismapped():
              creditsQuitButton.pack_forget()

    creditsText.config(yscrollcommand=lambda *args: (scrollbarCredits.set(*args), check_scroll(*args)))

    #On lance la fenêtre des crédits
    credits.mainloop()

  #Fonction qui affiche les règles du jeu dans une nouvelel fenêtre 
  def regles():
    #Fonction qui ferme la fenêtre des règles du jeu
    def regles_quit():
      regles.destroy()
    #On crée la fenêtre ainsi que les différents éléments des règles du jeu
    regles = Tk()
    regles.title("Règles | Memory Game")
    regles.geometry("400x300")
    reglesTitleFrame = Frame(regles, relief=GROOVE)
    reglesTitleFrame.pack(side=TOP)
    reglesTitleLabel = Label(reglesTitleFrame, text="Memory Game \n Règles", font=("Arial", 15))
    reglesTitleLabel.pack()
    reglesTextFrame = Frame(regles, relief=GROOVE)
    reglesTextFrame.pack(fill=BOTH, expand=True)
    reglesText = Text(reglesTextFrame,   font=("Arial", 10), wrap=WORD)
    reglesText.pack(side=LEFT, fill=BOTH, expand=True, pady=10, padx=5)
    scrollbarRegles = Scrollbar(reglesTextFrame, orient=VERTICAL, command=reglesText.yview)
    scrollbarRegles.pack(side=RIGHT, fill=Y)
    
    reglesText.tag_configure("center", justify='center')

    reglesText.insert(END, "Le jeu 'Memory Game' a été réalisé par\nThomas KELEMEN & Gabriel CADEAU-FLAUJAT,\ndeux élèves de première NSI, passionnés par coder les idées de programmes leur passant par la tête.\n\nRègles générales :\n'Memory Game' est un jeu composé de quatre salles, chacune d'elle représentant une épreuve.\n\nCes épreuves sont :\n -La Mémoire Verbale (à gauche)\n -La Mémoire des Images (en bas)\n -La Mémoire des Nombres (à droite)\n -La Mémoire des Patterns (en haut).\nLes règles de chacune de ses épreuves sont disponibles quand vous y accédez.\n\nSalle Principale :\nLa salle principale est une salle libre dans laquelle vous pouvez vous déplacer pour accéder aux différentes épreuves.\nChacune des portes correspond à une épreuve différente.\n\nContrôles :\nAfin de vous déplacer dans la salle principale, utilisez les flèches de votre clavier.\nPour entrer dans les différentes salles, utilisez la touche 'e'.\nDans les salles d'épreuves, utilisez la souris pour vous déplacer et le clique gauche pour intéragir avec les différents éléments\n\nEaster Egg :\nDes Easter Eggs sont dissimulés dans le jeu, soyez attentifs pour essayer de tous les trouver.\nNote: Vous pouvez utiliser les différents fichiers Python mis à votre disposition\n\nAccès à la salle de Mémoire des Patterns:\nAfin d'accéder à la salle finale du jeu, vous aurez besoin d'obtenir un certain score dans les trois autres épreuves:\n-Mémoire Verbale: 25 Points en mode facile/ 50 Points en mode difficile\n -Mémoire des Images: 25 Points en mode facile/ 50 Points en mode difficile\n -Mémoire des Nombres: 7 Points en mode facile/ 10 Points en mode difficile \n \n \n","center")
    
    reglesText.config(state=DISABLED)
    reglesQuitButton = Button(reglesText, text="OK", command=regles_quit, background="aquamarine1")

    #Fonction qui fait défiler les éléments de reglesText en même temps que la scrollbar
    def check_scroll(*args):
      reglesText.update_idletasks()
      # Obtenir la position actuelle de la scrollbar
      position = reglesText.yview()
      # Si la scrollbar est tout en bas (pos[1] == 1.0)
      if position[1] == 1.0:
          # Insérer le bouton si ce n'est pas déjà fait
          if not reglesQuitButton.winfo_ismapped():
             reglesQuitButton.pack(side=BOTTOM, anchor=S, pady=10)
      else:
          # Supprimer le bouton si la scrollbar n'est pas tout en bas
          if reglesQuitButton.winfo_ismapped():
              reglesQuitButton.pack_forget()

    reglesText.config(yscrollcommand=lambda *args: (scrollbarRegles.set(*args), check_scroll(*args)))

    #On lance la fenêtre des règles
    regles.mainloop()

  #Fonction qui appelel la fonction script()
  def launcher():
    StartFenetre.destroy()
    script()

  #Fonction qui définit la difficulté sur facile
  def easyMode():
    global difficulte
    EasyBtn.destroy()
    HardBtn.destroy()
    DifficultyLab.destroy()
    difficulte = False
    StartBtn.pack()
    ChangeDifficultyBtn.pack(side=BOTTOM, anchor=CENTER, pady=10)

  #Fonction qui définit la difficulté sur difficile
  def hardMode():
    global difficulte
    EasyBtn.destroy()
    HardBtn.destroy()
    DifficultyLab.destroy()
    difficulte = True
    StartBtn.pack()
    ChangeDifficultyBtn.pack(side=BOTTOM, anchor=CENTER, pady=10)

  #Fonction qui permet de gérer le changement de difficulté
  def changeDifficulty():
    global difficulte
    StartFenetre.destroy()
    startGame()
    difficulte = None




  #On crée la fenêtre et les différents éléments du menu de démarrage du jeu
  StartFenetre = Tk()
  StartFenetre.title("Memory Game | Thomas & Gabriel")
  StartFenetre.geometry("750x400")

  StartTitleFrame = Frame(StartFenetre, borderwidth=1, relief=GROOVE)
  StartTitleFrame.pack(side=TOP,padx=10, pady=10)
  StartTitleLabel = Label(StartTitleFrame, text="Bienvenue dans le jeu \n 'Memory Game'", font=("Arial", 20))
  StartTitleLabel.pack(side=TOP)
  StartSubtitleLabel = Label(StartTitleFrame, text="Un jeu par Thomas KELEMEN et Gabriel CADEAU-FLAUJAT", font=("Arial", 15))
  StartSubtitleLabel.pack(side=TOP)

  LicenseLabel = Label(StartFenetre, text="Memory Game, Thomas KELEMEN & Gabriel CADEAU-FLAUJAT \n © Tous droits réservés. 2024 ")
  LicenseLabel.pack(side=BOTTOM)
  StartButtonsFrame = Frame(StartFenetre, borderwidth=1, relief=GROOVE)
  StartButtonsFrame.pack(padx=10, pady=10)
  StartButtonsFrameTop = Frame(StartButtonsFrame, relief=GROOVE)
  StartButtonsFrameTop.pack(side=TOP, padx=5, pady=5)
  StartButtonsFrameBottom = Frame(StartButtonsFrame, relief=GROOVE)
  StartButtonsFrameBottom.pack(side=BOTTOM, padx=5, pady=5)

  StartBtn = Button(StartButtonsFrameBottom, text="COMMENCER", font=("Arial", 10), command=launcher, background="aquamarine1")
  ChangeDifficultyBtn = Button(StartButtonsFrameBottom, text="Changer de difficulté", font=("Arial", 10), background="aquamarine1", command=changeDifficulty)

  DifficultyLab = Label(StartButtonsFrameBottom, text="Choisissez la difficulté du jeu.", font=("Arial", 15))
  DifficultyLab.pack(side=TOP, anchor=CENTER)
  EasyBtn = Button(StartButtonsFrameBottom, text="FACILE", font=("Arial", 10), command=easyMode, background="green1")
  HardBtn = Button(StartButtonsFrameBottom, text="DIFFICILE", font=("Arial", 10), command=hardMode, background="red1")
  EasyBtn.pack(side=TOP, pady=10)
  HardBtn.pack(side=TOP, pady=10)


  CreditsBtn = Button(StartButtonsFrameTop, text="Crédits", command=credits, font=("Arial", 10), background="aquamarine3")
  CreditsBtn.pack(side=LEFT, pady=10, padx=25)

  ReglesBtn = Button(StartButtonsFrameTop, text="Règles", command=regles, font=("Arial", 10), background="aquamarine3")
  ReglesBtn.pack(side=RIGHT, pady=10, padx=25)

  #On lance la fenêtre du menu de démarrage
  StartFenetre.mainloop()

startGame()