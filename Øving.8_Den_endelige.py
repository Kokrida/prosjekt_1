# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:20:01 2021

@author: Kristin
"""

sporsmaal ="hva er hovedstaden i norge? "
alternativer= ["Oslo", "Tokyio","Amsterdam"] 
korrektsvar= 1

sporsmaal2= "hvilket tre skjelver? "
alternativer2= ["Lønn", "Osp", "Eik"]
korrektsvar2= 2



class Question():
    
    def __init__(self, sporsmaal, alternativer, korrektsvar):
        self.sporsmaal = sporsmaal
        self.alternativer=alternativer
        self.korrektsvar=korrektsvar
        
    def sjekk_svar(self, svar_avgitt):
        if svar_avgitt == self.korrektsvar:
            print("rett svar")
        else: 
            print("feil svar")
      
        
        
    def __str__(self):
        
        temp = self.sporsmaal
       
        
        for i in range(len(self.alternativer)):
            temp+= "\n" + str(i+1) + " " + self.alternativer[i]
        return temp
      
   

    
nytt_spørsmål= Question(sporsmaal,alternativer,korrektsvar)

print(nytt_spørsmål)

svar= input("skriv svaret: ")
svar= int(svar)
nytt_spørsmål.sjekk_svar(svar)

nytt2_spørsmål= Question(sporsmaal2,alternativer2,korrektsvar2)
print(nytt2_spørsmål)

svar2= input(" skriv svaret: ")
svar2= int(svar2)
nytt2_spørsmål.sjekk_svar(svar2)