# User inputs a Jpanaese verb infinitive, outputs verb definition, Kanji characterization, as well as the present, negative, -te and -ta conjugation forms

import re
from os import system, name 
from time import sleep 
import sys

# Japanese Verb List(s)

verblist = ["kuru", "suru", "motozuku", "iku", "aku", "matsu", "tsuku", "medatsu", "yorokobu", "tsugu", "tasu", "kokorozasu"]

rulist = ["iru", "kaeru", "shaberu", "shiru", "hairu", "hashiru", "aseru", "kagiru", "keru", "suberu", "nigiru", "mairu", "majiru", "azakeru", "kutsugaeru", "saegiru", "nonoshiru", "nejiru", "hirugaeru", "meiru", "yomigaeru"]

ieruvlist = ["miru", "heru", "neru", "kiru", "taberu", "ureru", "kuwaeru", "mitomeru"]

ulist = ["machigau", "aru", "osou"]


# Definition dict:

defs = {

  "kuru": "来る, to come",
  "suru": "する, to do, make",
  "iku": "行く, to go",
  "aku": "開く, to open, become vacant",
  "matsu": "待つ, to wait", 
  "tsuku": "着く, to arrive",
  "medatsu": "目立つ, to attract attention, stand out",
  "yorokobu": "喜ぶ, to be glad, pleased",
  "tsugu": "次ぐ, to be next",
  "aru": "ある, is, exists",
  "tasu": "足す, to add",
  "kokorozasu": "志す, to aspire to",
  "osou": "襲う, to attack",
  "iru": "要る/いる, to need/to be",
  "kaeru": "帰る, to return, go home",
  "shaberu": "喋る, to chatter",
  "shiru": "知る, to know",
  "hairu": "入る, to enter",
  "hashiru": "走る, to run",
  "aseru": "焦る, to be in a hurry, panic",
  "kagiru": "限る, to limit",
  "keru": "蹴る, to kick",
  "suberu": "滑る, to slip",
  "nigiru": "握る, to grasp",
  "mairu": "参る, to come/go (humble)",
  "majiru": "混じる, to be mixed, get mingled with, join",
  "azakeru": "嘲る, to ridicule",
  "kutsugaeru": "覆る, to be overturned",
  "saegiru": "遮る, to block",
  "nonoshiru": "罵る, to abuse verbally, curse",
  "nejiru": "捩じる, to twist",
  "hirugaeru": "翻る, to turn over, wave",
  "meiru": "to feel depressed/mail(?)" ,
  "yomigaeru": "蘇る, to revive",
  "miru": "見る, to look/see",
  "heru": "減る, to decrease/be produced",
  "neru": "寝る, to sleep, go to bed",
  "kiru": "着る, to wear",
  "taberu": "食べる, to eat",
  "ureru": "売れる, to be sold",
  "kuwaeru": "加える, to add to, include",
  "mitomeru": "認める, to admit, recognize",
  "machigau": "間違う, to be mistaken, make a mistake",
  "motozuku": "基づく, to be based on"

}


# {vtwo}:

vtwo = {
  "suru": {
    "psuru": "shimasu",
    "nsuru": "shinai",
    "tesuru": "shite", 
    "tasuru": "shita"
  },

  "kuru": {
    "pkuru": "kimasu",
    "nkuru": "konai", 
    "tekuru": "kite",
    "takuru": "kita"
  }
}

# {ieru}:

ieru = {
  "pieru": "masu",   
  "nieru": "nai",
  "teieru": "te",
  "taieru": "ta"
}

# {u}:

u = {
  "pu": "imasu",
  "nu": "wanai",
  "teu": "tte",
  "tau": "tta"
}


# {ru}:

ru = {
  "pru": "rimasu",
  "nru": "ranai",
  "teru": "tte",
  "taru": "tta"
}

  # {tsu}:

tsu = {
  "ptsu": "chimasu", 
  "ntsu": "tanai", 
  "tetsu": "tte",
  "tatsu": "tta"
}

# {iku}:
iku = {
  "piku": "ikimasu",
  "niku": "ikanai",
  "teiku": "itte ",
  "taiku": "itta"
}
 
# {vone}:

vone = {

  "ku": {
    "pku": "kimasu", 
    "nku": "kanai", 
    "teku": "ite", 
    "taku": "ita"   
  },

  "gu": {
    "pgu": "gimasu",
    "ngu": "ganai",
    "tegu": "ide",
    "tagu": "ida"
  },

  "nu": {
    "pnu": "nimasu",
    "nnu": "nanai",
    "tenu": "nde",
    "tanu": "nda"
  },
    
  "bu": {
    "pbu": "bimasu",
    "nbu": "banai",
    "tebu": "nde",
    "tabu": "nda"
  },

  "mu": {
    "pmu": "mimasu",
    "nmu": "manai",
    "temu": "nde",
    "tamu": "nda"
  },

  "su": {
    "psu": "shimasu",
    "nsu": "sanai",
    "tesu": "shite",
    "tasu": "shita"
  }
}

###########################################################################################
###########################################################################################

# Fundamental Dunctions

###########################################################################################
###########################################################################################


# "Clear" function:

def clear(): 
  if name == 'nt': 
    _ = system('cls') 
     # for mac and linux(here, os.name is 'posix') 
  else: 
    _ = system('clear')         


def invld(inf):
      
    if len(inf) <= 2:
      print("Invalid response!")
      jpvcj()
    else:
      pass

# Main Program Function

def jpvcj():

  inf = input("Enter verb: ").lower()

  if len(inf) <= 2:
    clear()
    jpvcj()

  a = vone.keys()

  w = inf[0:-1]
  x = inf[0:-2]
  y = inf[0:-3]
  z = inf[0:1]
  xx = inf[-3:]
  yy = inf[-2:]
  zz = inf[-1]
  q = inf[-3]
  r = inf[-2]

  ovow = re.findall("[aeio]", inf)

  j = vone.items()
  k = ru.values()
  l = str("iru"), str("eru")
  m = ("kiru", "heru", "neru")
  n = u.values()

  a = defs.items()
  b = defs.values()
  

###########################################################################################

# Logic

###########################################################################################

# Reprint (inf)
     
  for k in defs:
    if inf == k:     

      def definv(inf):
  
        for k1,v in a:
          if inf == k1:
            print("Your verb:", inf, "||", v)
            print()
  
      definv(inf)


  # Check if inf == "iku":

      def iku_co(inf):

        if inf == str("iku"):
          for v in iku.values():
            print(v)

      iku_co(inf)



# Check if inf is a -u verb:

      def u_verbs(inf):

        if inf in ulist:
          for v in n:
            print(w + v)
            continue
        else:
          pass
    
      u_verbs(inf)


# Check if (inf) is either "kuru" or "suru":

      def ksuru(inf):
  
        if inf == str("kuru"):
          for v in vtwo["kuru"].values():
            print(v)
            continue
        elif inf == str("suru"):
          for v1 in vtwo["suru"].values():
            print(v1)
            continue
        else:
          pass

      ksuru(inf)


# Check if inf ends with -iru or -eru:

      def vieru(inf):

        if inf in ieruvlist:
          for va in ieru.values():
            print(x + va)
            continue
        else:
          pass

      vieru(inf)

# Check if inf is a -ru verb:

      def ruverbs(inf):

        if inf in rulist:
          for v2 in ru.values():
            print(x + v2)      
            continue
        else:
          pass

      ruverbs(inf)



# Check if (inf) ends with "tsu".

      def vtsu(inf):

        if inf.endswith("tsu"):
          for v3 in tsu.values():
            print(y + v3)
            continue

      vtsu(inf)


# Check if inf ends with -ku, -gu, -nu, -bu, -mu, or -su:

      def two_verbs(inf):   
        
        if q == str("t"):
          pass
        elif inf == str("iku"):
          pass
        elif inf in verblist:
          for k,v in j:
            if yy == k:
              for k1,v1 in v.items():
                if inf in verblist:
                  if len(inf) <=3:
                    print(z + v1)
                  else:
                    print(x + v1)
     
                  
      two_verbs(inf)

# Program reset:

  def loop_end(reset):

    if reset == str("y").capitalize:
      clear()
      jpvcj()
    elif reset == str("n").capitalize:
      clear()
      print("さようなら！ (Sayonara!)")
      return None
      


  while inf in defs:
    reset = input("\nWould you like to conjugate another Japanese verb? (y/n): ").capitalize
    loop_end(reset)
    break
  else:
    clear()
    print("Invalid response!")
    jpvcj()
    
 



jpvcj()


# 11/1/2020 @ 4:31p - JPVC v1.0 POC COMPLETED!!!!!!!!!!!!!!!!!!!!!!

# Things to add:

  # 1. Verb labels
  # 2. More verbs
  # 3. Conjugation - to - Infinitive lookups
  # 4. Example sentences (multiple ones per conjugation)
  # 5. 


