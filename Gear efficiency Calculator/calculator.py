
max_att_def_eff = 48
max_critr = 30
max_critc = 42
max_spd = 24
modifiers = ["att_def_eff", "critr", "critc","spd"]
max_values = [max_att_def_eff, max_critc, max_critr, max_spd]
commonstats = "HP/Def/Eff/Eff-res/Atk"
crit_d = "Crit Damage"
crit_c = "Crit Chance"
spd = "Speed"
def gearScore (modifier_list):
    score = 0
    for modifier in modifier_list:
        if modifier[0] == commonstats:
            score += modifier[1]/max_att_def_eff * 100
        elif modifier[0] == crit_d :
            score += modifier[1]/max_critr * 100
        elif modifier[0] == crit_c :
            score += modifier[1]/max_critc * 100
        else:
            score += modifier[1]/max_spd * 100
    return score

