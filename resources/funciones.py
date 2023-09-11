import math

#PLAYS =  Number.Round([T2I]+[T3I]+(0.44*[T1I])+[PP], 2)
def plays(t2i, t3i, t1i, pp):
    return round((int(t2i)+int(t3i))+(0.44*int(t1i))+int(pp),2)

#PPP =    Number.Round(if [Plays] = 0 then 0 else [Puntos]/[Plays], 2) 
def ppp(puntos, plays):
    if (plays == 0):
        return 0
    else:
        return round(int(puntos)/int(plays),2)

#EFG% =   Number.ToText(if [TCI]= 0 then 0 else ([TCC]+([T3C]*0.5))/[TCI], "P1")
def efg(tcc, t3c, tci):
    if (tci == 0):
        return 0
    else:
        return str(int(tcc)+(int(t3c)*0.5))/int(tci)

#PLAYS% = Number.ToText(if [Plays] = 0 then 0 else [Plays]/NUMERO TOTAL DE PLAYS, "P1")
def playsP(total, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(plays)/int(total))
    
#USG% =   Number.ToText (if [Min] = 0 then 0 else (([TCI]+[PP]+(0.44*[T1I]))*200)/((TCI-ToTales+PP-ToTales+(0.44*T1I-ToTales))*5*[Min]), "P1")
def usg(tci, pp, t1i, totales, min):
    if (min == 0):
        return 0
    else:
        return str((int(tci)+int(pp)+(0.44*int(t1i)))*200)/((int(tci)-int(totales)+int(pp)-int(totales)+(0.44*int(t1i))-int(totales))*5*int(min))
    
#TS% =    Number.ToText( if ([TCI]+(0.44*[T1I])) = 0 then 0 else [Puntos]/(2*([TCI]+(0.44*[T1I]))), "P1")
def ts(tci, t1i, puntos):
    if ((int(tci)+(0.44*int(t1i))) == 0):
        return 0
    else:
        return str(int(puntos)/(2*(int(tci)+(0.44*int(t1i)))))
    
#TO% =    Number.ToText( if [Plays]=0 then 0 else [PP]/[Plays], "P1")
def to(pp, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(pp)/int(plays))
    
#RTL% =   Number.ToText( if [Plays]=0 then 0 else [T1I]/[Plays], "P1")
def rtl(t1i, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(t1i)/int(plays))
    
#PPT1 =   Number.Round( if [T1I]=0 then 0 else [T1C]/[T1I], 2)
def ppt1(t1i, t1c):
    if (t1i == 0):
        return 0
    else:
        return round(int(t1c)/int(t1i),2)
    
#PPT2 =   Number.Round( if [T2I]=0 then 0 else [T2C]*2/[T2I], 2)
def ppt2(t2i, t2c):
    if (t2i == 0):
        return 0
    else:
        return round(int(t2c)*2/int(t2i),2)
    
#PPT3 =   Number.Round( if [T3I]=0 then 0 else [T3C]*3/[T3I], 2)
def ppt3(t3i, t3c):
    if (t3i == 0):
        return 0
    else:
        return round(int(t3c)*3/int(t3i),2)

#PPPT3 =  Number.ToText( if ([Plays]) = 0 or ([PPP]) = 0 then 0 else (([T3C])*3/([Plays]))/[PPP], "P1")
def pppt3(plays, ppp, t3c):
    if (plays == 0 or ppp == 0):
        return 0
    else:
        return str((int(t3c))*3/(int(plays)))/int(ppp)
    
#PPPT2 =  Number.ToText( if ([Plays]) = 0 or ([PPP]) = 0 then 0 else (([T2C])*2/([Plays]))/[PPP], "P1")
def pppt2(plays, ppp, t2c):
    if (plays == 0 or ppp == 0):
        return 0
    else:
        return str((int(t2c))*2/(int(plays)))/int(ppp)
    
#PPPT1 =  Number.ToText( if ([Plays]) = 0 or ([PPP]) = 0 then 0 else (([T1C])/([Plays]))/[PPP], "P1")
def pppt1(plays, ppp, t1c):
    if (plays == 0 or ppp == 0):
        return 0
    else:
        return str((int(t1c))/(int(plays)))/int(ppp)
    
#F1 T1 PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([T1I])*0.44/([Plays]), "P1")
def f1t1p(t1i, plays):
    if (plays == 0):
        return 0
    else:
        return str((int(t1i))*0.44/int(plays))
    
#F2 T2 PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([T2I])/([Plays]), "P1")
def f2t2p(t2i, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(t2i)/int(plays))
    
#F3 T3 PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([T3I])/([Plays]), "P1")
def f3t3p(t3i, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(t3i)/int(plays))
    
#F4 PP PLAYS% = Number.ToText( if ([Plays])  = 0 then 0 else ([PP])/([Plays]), "P1")
def f4ppp(pp, plays):
    if (plays == 0):
        return 0
    else:
        return str(int(pp)/int(plays))
    
#Posesiones Anotadoras = Number.Round([TCC] +((1 - Number.Power((1-[T1 %]), 2))*0.44*[T1I]),2)
def posesionesA(tcc, t1p, t1i):
    return round(int(tcc) +((1 - math.pow((1-int(t1p)), 2))*0.44*int(t1i)),2)

#Number.Round(if [TCC] = 0 then 0 else [TCC] +((1 - Number.Power((1-[T1 %]/100), 2))*0.44*[T1I]),2)
def posesionesA2(tcc, t1p, t1i):
    if (tcc == 0):
        return 0
    else:
        return round(int(tcc) +((1 - math.pow((1-int(t1p)/100), 2))*0.44*int(t1i)),2)
    
#POSSESIONES ANOTADORAS % = Number.ToText( if ([Plays]) = 0  then 0 else (([Posesiones Anotadoras])/([Plays])), "P1")
def posesionesAporc(plays, posesiones):
    if (plays == 0):
        return 0
    else:
        return str(int(posesiones)/int(plays))
    
#OE =                     Number.Round( if ([TCI]-[RO]+[AS]+[PP]) = 0 then 0 else ([TCC ]+[AS])/([TCI]-[RO]+[AS]+[PP]), 2)
def oe(tci, ro, asis, pp, tcc):
    if ((int(tci)-int(ro)+int(asis)+int(pp)) == 0):
        return 0
    else:
        return round((int(tcc)+int(asis))/(int(tci)-int(ro)+int(asis)+int(pp)),2)
    
#EPS =          [Puntos]*[OE]
def eps(puntos, oe):
    return int(puntos)*int(oe)

def callAllFunctions(t2i, t3i, t1i, pp, puntos, tcc, t3c, tci, min, totales, t1c, t2c, t1p, ro, asis):
    plays = int(plays(t2i, t3i, t1i, pp))
    data = ""
    data += "Plays: " + str(plays(t2i, t3i, t1i, pp)) + "\n"
    data += "PPP: " + str(ppp(puntos, plays)) + "\n"
    data += "EFG: " + str(efg(tcc, t3c, tci)) + "\n"
    data += "Plays%: " + str(playsP(plays, plays)) + "\n"
    data += "USG: " + str(usg(tci, pp, t1i, totales, min)) + "\n"
    data += "TS: " + str(ts(tci, t1i, puntos)) + "\n"
    data += "TO: " + str(to(pp, plays)) + "\n"
    data += "RTL: " + str(rtl(t1i, plays)) + "\n"
    data += "PPT1: " + str(ppt1(t1i, t1c)) + "\n"
    data += "PPT2: " + str(ppt2(t2i, t2c)) + "\n"
    data += "PPT3: " + str(ppt3(t3i, t3c)) + "\n"
    data += "PPPT3: " + str(pppt3(plays, ppp(puntos, plays), t3c)) + "\n"
    data += "PPPT2: " + str(pppt2(plays, ppp(puntos, plays), t2c)) + "\n"
    data += "PPPT1: " + str(pppt1(plays, ppp(puntos, plays), t1c)) + "\n"
    data += "F1 T1 PLAYS%: " + str(f1t1p(t1i, plays)) + "\n"
    data += "F2 T2 PLAYS%: " + str(f2t2p(t2i, plays)) + "\n"
    data += "F3 T3 PLAYS%: " + str(f3t3p(t3i, plays)) + "\n"
    data += "F4 PP PLAYS%: " + str(f4ppp(pp, plays)) + "\n"
    data += "Posesiones Anotadoras: " + str(posesionesA(tcc, t1p, t1i)) + "\n"
    data += "Posesiones Anotadoras2: " + str(posesionesA2(tcc, t1p, t1i)) + "\n"
    data += "Posesiones Anotadoras%: " + str(posesionesAporc(plays, posesionesA(tcc, t1p, t1i))) + "\n"
    data += "OE: " + str(oe(tci, ro, asis, pp, tcc)) + "\n"
    data += "EPS: " + str(eps(puntos, oe(tci, ro, asis, pp, tcc))) + "\n"
    return data

def sumarEstadisticas(game):
    t2i = 0
    t3i = 0
    t1i = 0
    pp = 0
    puntos = 0
    tcc = 0
    t3c = 0
    tci = 0
    min = 0
    totales = 0
    t1c = 0
    t2c = 0
    t1p = 0
    ro = 0
    rd = 0
    asis = 0
    for lp in game.local_players_stats:
        t2i = t2i + lp.field_goal_attempts
        t3i = t3i + lp.three_point_attempts
        t1i = t1i + lp.free_throw_attempts
        pp = pp + lp.turnovers
        puntos = puntos + lp.points
        tcc = tcc + lp.field_goals
        t3c = t3c + lp.three_pointers
        tci = tci + lp.free_throws
        min = min + lp.minutes_played
        totales = totales + lp.total_rebounds
        t1c = t1c + lp.free_throws
        t2c = t2c + lp.two_pointers
        t1p = t1p + lp.free_throw_percentage
        ro = ro + lp.offensive_rebounds
        rd = rd + lp.defensive_rebounds
        asis = asis + lp.assists
    
    game.local_team_stats.field_goal_attempts = t2i
    game.local_team_stats.three_point_attempts = t3i
    game.local_team_stats.free_throw_attempts = t1i
    game.local_team_stats.turnovers = pp
    game.local_team_stats.points = puntos
    game.local_team_stats.field_goals = tcc
    game.local_team_stats.three_pointers = t3c
    game.local_team_stats.free_throws = tci
    game.local_team_stats.minutes_played = min
    game.local_team_stats.total_rebounds = totales
    game.local_team_stats.free_throws = t1c
    game.local_team_stats.two_pointers = t2c
    game.local_team_stats.free_throw_percentage = t1p
    game.local_team_stats.offensive_rebounds = ro
    game.local_team_stats.defensive_rebounds = rd
    game.local_team_stats.assists = asis

    t2i = 0
    t3i = 0
    t1i = 0
    pp = 0
    puntos = 0
    tcc = 0
    t3c = 0
    tci = 0
    min = 0
    totales = 0
    t1c = 0
    t2c = 0
    t1p = 0
    ro = 0
    rd = 0
    asis = 0

    for vp in game.visitor_players_stats:
        t2i = t2i + vp.field_goal_attempts
        t3i = t3i + vp.three_point_attempts
        t1i = t1i + vp.free_throw_attempts
        pp = pp + vp.turnovers
        puntos = puntos + vp.points
        tcc = tcc + vp.field_goals
        t3c = t3c + vp.three_pointers
        tci = tci + vp.free_throws
        min = min + vp.minutes_played
        totales = totales + vp.total_rebounds
        t1c = t1c + vp.free_throws
        t2c = t2c + vp.two_pointers
        t1p = t1p + vp.free_throw_percentage
        ro = ro + vp.offensive_rebounds
        rd = rd + vp.defensive_rebounds
        asis = asis + vp.assists

    game.visitor_team_stats.field_goal_attempts = t2i
    game.visitor_team_stats.three_point_attempts = t3i
    game.visitor_team_stats.free_throw_attempts = t1i
    game.visitor_team_stats.turnovers = pp
    game.visitor_team_stats.points = puntos
    game.visitor_team_stats.field_goals = tcc
    game.visitor_team_stats.three_pointers = t3c
    game.visitor_team_stats.free_throws = tci
    game.visitor_team_stats.minutes_played = min
    game.visitor_team_stats.total_rebounds = totales
    game.visitor_team_stats.free_throws = t1c
    game.visitor_team_stats.two_pointers = t2c
    game.visitor_team_stats.free_throw_percentage = t1p
    game.visitor_team_stats.offensive_rebounds = ro
    game.visitor_team_stats.defensive_rebounds = rd
    game.visitor_team_stats.assists = asis

    return game
    
    

        
