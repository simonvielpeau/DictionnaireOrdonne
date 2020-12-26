
class DictionnaireOrdonne:

  # on veut un dico ordonné - cad qu'on peut trier par clé
  # on a des clés et des valeurs : ex : {"prénom":"sim","age":"21","ville":"caen"} ✔
    # comment ?
    # on peut pas mettre dans un str qu'on split prce que ça limiterait un caractère
    # [clé,valeur],[clé,valeur],[clé,valeur]
  # on doit pouvoir y accéder en mode dico[clé] = .... ✔
  # on doit pouvoir set les valeurs en mode dico[clé] = ...  ✔
  # on doit pouvoir delete les éléments en mode del dico[clé] ✔
  # on doit pouvoir test la présence de clés en mode "simon" in dico ✔
  # on doit pouvoir connaître la taille du dico ✔
  # on doit pouvoir ajouter des dicos entre eux ✔
  # on doit pouvoir itérer sur les clés du dico ✔
  # on doit pouvoir trier par clé ✔
  # on doit pouvoir inverser l'ordre ✔
  # on doit pouvoir renvoyer les clés et/ou valeurs ✔


  # idées & implémentations:
    # peut-on stocker des objets dans notre dico ?

  # INIT
  # 3 possibilités:
  #    • vide : dico créé vide
  #    • copié : dico créé à partir d'un autre dico
  #    • pré-rempli : on fournit des clés et des valeurs - ex : constructeur(clé1=valeur1,clé2=valeur2,...)
  def __init__(self, dicoBase=None, **clval):
    self.cles = []
    self.valeurs = []
    if dicoBase != None:
      for key in dicoBase.cles:
        self.cles.append(key)
      for valeur in dicoBase.valeurs:
        self.valeurs.append(valeur)
    # clval = {"clé":"valeur","clé":"valeur"}
    for key in clval:
      self.cles.append(key)
      self.valeurs.append(clval[key])
    # on peut donc faire dico = DictionnaireOrdonne(dico,lieu="Caen") - cad combiner les deux dernières possibilités => bien ?



  # --- METHODES SPECIALES ---
  # représentation (comme dico de base : {cle1: valeur1, cle2: valeur2, …})
  def __repr__(self):
    display = "{"
    for i,element in enumerate(self.items()):
      display += (repr(element[0]) + ": " + repr(element[1]))
      if not i == len(self.items())-1:
        display += ", "
    display+="}"
    return display


  def __str__(self):
    return self.__repr__()

  # index (self[clé] ; self[clé] = ... ; del self[clé])
  def __getitem__(self,key):
    for k,v in self.items():
      if k == key:
        return v
    raise KeyError

  def __setitem__(self,key,valeur):
    try:
      self.__getitem__(key)
    except KeyError:
      self.cles.append(key)
      self.valeurs.append(valeur)
    else:
      for i,k in enumerate(self.keys()):
        if k == key:
          self.valeurs[i] = valeur


  def __delitem__(self,key):
    try:
      self.__getitem__(key)
    except KeyError:
      raise
    else:
      for i,k in enumerate(self.keys()):
        if k == key:
          del self.cles[i]
          del self.valeurs[i]

  # tester s'il y a une clé ou non dans notre dico ("simon" in self)
  def __contains__(self,k):
    if k in self.cles:
      return True
    return False

  # taille
  def __len__(self):
    return len(self.cles)

  # ajouter dicos entre eux
  def __add__(self,dic2):
    # self+dic2 et ça retourne un nv dico
    dic = DictionnaireOrdonne()
    for element in self.items():
      dic.cles.append(element[0])
      dic.valeurs.append(element[1])
    for element in dic2.items():
      if dic.__contains__(element[0]): # empêcher surcharge d'éléments
        continue
      dic.cles.append(element[0])
      dic.valeurs.append(element[1])
    return dic

  def __iadd__(self,dic2):
    # self+=dic2
    for element in dic2.items():
      if self.__contains__(element[0]): # empêcher surcharge d'éléments
        continue
      self.cles.append(element[0])
      self.valeurs.append(element[1])
    return self

  # itération (for ... in self):
  def __iter__(self): # avec yield
    # méthode avec yield
    index = 0
    while index < len(self.cles):
      yield self.cles[index]
      index+=1

  # def __iter__(self): # classique - avec class
  #   return IterDico(self)

  # --- METHODES PROPRES ---

  # trier par clé
  def sort(self):
    items = sorted(self.items(),key=lambda element: element[0])
    self.cles = []
    self.valeurs = []
    for item in items:
      self.cles.append(item[0])
      self.valeurs.append(item[1])

  # inverser
  def reverse(self):
    items = reversed(self.items())
    self.cles = []
    self.valeurs = []
    for item in items:
      self.cles.append(item[0])
      self.valeurs.append(item[1])

  # renvoyer les clés et/ou valeurs -- en tableau ?, on doit pouvoir itérer dessus
  def keys(self):
    return self.cles

  def values(self):
    return self.valeurs

  def items(self):
    items = []
    for i in range(len(self.cles)):
      items.append((self.cles[i],self.valeurs[i]))
    return items


# méthode d'itération classique, avec classes
class IterDico():
  def __init__(self,dico):
    self.objet = dico
    self.index = -1

  def __next__(self):
    self.index+=1
    if self.index >= len(self.objet.cles):
      raise StopIteration
    return self.objet.cles[self.index] # la clé
