import math

#PLAYS =  Number.Round([T2I]+[T3I]+(0.44*[T1I])+[PP], 2)
def Plays(t2i, t3i, t1i, pp):
    return round((int(t2i)+int(t3i))+(0.44*int(t1i))+int(pp),2)

#PPP =    Number.Round(if [Plays] = 0 then 0 else [Puntos]/[Plays], 2) 
def PPP(puntos, plays):
    if (plays == 0):
        return 0
    else:
        return round(int(puntos)/int(plays),2)

#EFG% =   Number.ToText(if [TCI]= 0 then 0 else ([TCC]+([T3C]*0.5))/[TCI], "P1")
def EFG(tcc, t3c, tci):
    if (tci == 0):
        return 0
    else:
        return str(int(tcc)+(int(t3c)*0.5))/int(tci)

#PLAYS% = Number.ToText(if [Plays] = 0 then 0 else [Plays]/NUMERO TOTAL DE PLAYS, "P1")
def PlaysP(total, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(plays)/int(total))
    
#USG% =   Number.ToText (if [Min] = 0 then 0 else (([TCI]+[PP]+(0.44*[T1I]))*200)/((TCI-ToTales+PP-ToTales+(0.44*T1I-ToTales))*5*[Min]), "P1")
def USG(tci, pp, t1i, totales, min):
    if (min == 0):
        return 0
    else:
        return str((int(tci)+int(pp)+(0.44*int(t1i)))*200)/((int(tci)-int(totales)+int(pp)-int(totales)+(0.44*int(t1i))-int(totales))*5*int(min))
    
#TS% =    Number.ToText( if ([TCI]+(0.44*[T1I])) = 0 then 0 else [Puntos]/(2*([TCI]+(0.44*[T1I]))), "P1")
def TS(tci, t1i, puntos):
    if ((int(tci)+(0.44*int(t1i))) == 0):
        return 0
    else:
        return str(int(puntos)/(2*(int(tci)+(0.44*int(t1i)))))
    
#TO% =    Number.ToText( if [Plays]=0 then 0 else [PP]/[Plays], "P1")
def TO(pp, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(pp)/int(plays))
    
#RTL% =   Number.ToText( if [Plays]=0 then 0 else [T1I]/[Plays], "P1")
def RTL(t1i, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(t1i)/int(plays))
    
#PPT1 =   Number.Round( if [T1I]=0 then 0 else [T1C]/[T1I], 2)
def PPT1(t1i, t1c):
    if (t1i == 0):
        return 0
    else:
        return round(int(t1c)/int(t1i),2)
    
#PPT2 =   Number.Round( if [T2I]=0 then 0 else [T2C]*2/[T2I], 2)
def PPT2(t2i, t2c):
    if (t2i == 0):
        return 0
    else:
        return round(int(t2c)*2/int(t2i),2)
    
#PPT3 =   Number.Round( if [T3I]=0 then 0 else [T3C]*3/[T3I], 2)
def PPT3(t3i, t3c):
    if (t3i == 0):
        return 0
    else:
        return round(int(t3c)*3/int(t3i),2)

#PPPT3 =  Number.ToText( if ([Plays]) = 0 or ([PPP]) = 0 then 0 else (([T3C])*3/([Plays]))/[PPP], "P1")
def PPPT3(plays, ppp, t3c):
    if (plays == 0 or ppp == 0):
        return 0
    else:
        return str((int(t3c))*3/(int(plays)))/int(ppp)
    
#PPPT2 =  Number.ToText( if ([Plays]) = 0 or ([PPP]) = 0 then 0 else (([T2C])*2/([Plays]))/[PPP], "P1")
def PPPT2(plays, ppp, t2c):
    if (plays == 0 or ppp == 0):
        return 0
    else:
        return str((int(t2c))*2/(int(plays)))/int(ppp)
    
#PPPT1 =  Number.ToText( if ([Plays]) = 0 or ([PPP]) = 0 then 0 else (([T1C])/([Plays]))/[PPP], "P1")
def PPPT1(plays, ppp, t1c):
    if (plays == 0 or ppp == 0):
        return 0
    else:
        return str((int(t1c))/(int(plays)))/int(ppp)
    
#F1 T1 PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([T1I])*0.44/([Plays]), "P1")
def F1T1P(t1i, plays):
    if (plays == 0):
        return 0
    else:
        return str((int(t1i))*0.44/int(plays))
    
#F2 T2 PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([T2I])/([Plays]), "P1")
def F2T2P(t2i, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(t2i)/int(plays))
    
#F3 T3 PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([T3I])/([Plays]), "P1")
def F3T3P(t3i, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(t3i)/int(plays))
    
#F4 PP PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([PP])/([Plays]), "P1")
def F4PPP(pp, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(pp)/int(plays))
    
#Posesiones Anotadoras = Number.Round([TCC] +((1 - Number.Power((1-[T1 %]), 2))*0.44*[T1I]),2)
def PosesionesA(tcc, t1p, t1i):
    return round(int(tcc) +((1 - math.pow((1-int(t1p)), 2))*0.44*int(t1i)),2)

#Number.Round(if [TCC] = 0 then 0 else [TCC] +((1 - Number.Power((1-[T1 %]/100), 2))*0.44*[T1I]),2)
def PosesionesA2(tcc, t1p, t1i):
    if (tcc == 0):
        return 0
    else:
        return round(int(tcc) +((1 - math.pow((1-int(t1p)/100), 2))*0.44*int(t1i)),2)
    
#POSSESIONES ANOTADORAS % = Number.ToText( if ([Plays]) = 0  then 0 else (([Posesiones Anotadoras])/([Plays])), "P1")
def PosesionesAP(plays, posesiones):
    if (plays == 0):
        return 0
    else:
        return str(int(posesiones)/int(plays))
    
#OE =                     Number.Round( if ([TCI]-[RO]+[AS]+[PP]) = 0 then 0 else ([TCC ]+[AS])/([TCI]-[RO]+[AS]+[PP]), 2)
def OE(tci, ro, asis, pp, tcc):
    if ((int(tci)-int(ro)+int(asis)+int(pp)) == 0):
        return 0
    else:
        return round((int(tcc)+int(asis))/(int(tci)-int(ro)+int(asis)+int(pp)),2)
    
#EPS =          [Puntos]*[OE]
def EPS(puntos, oe):
    return int(puntos)*int(oe)