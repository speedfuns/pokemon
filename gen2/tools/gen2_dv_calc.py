from math import sqrt

base = {
   'hp'     : 50,
   'attack' : 65,
   'defense': 64,
   'spatk'  : 44,
   'spdef'  : 48,
   'speed'  : 43
}

level = int(input('Level: '))
have_ev = input('EVs? (Y/N) ')

ev = {
   'hp'     : 0,
   'attack' : 0,
   'defense': 0,
   'spatk'  : 0,
   'spdef'  : 0,
   'speed'  : 0
}

if have_ev.lower() == 'y':
   ev['hp']       = int(input('         HP: '))
   ev['attack']   = int(input('     Attack: '))
   ev['defense']  = int(input('    Defense: '))
   ev['spatk']    = int(input(' Sp. Attack: '))
   ev['spdef']    = int(input('Sp. Defense: '))
   ev['speed']    = int(input('      Speed: '))

def get_stats (dv):
   hp       = ((((base['hp'] + dv) * 2 + (int(sqrt(ev['hp']) / 4))) * level) / 100) + level + 10
   attack   = ((((base['attack']    + dv) * 2 + (sqrt(ev['attack'])  / 4)) * level) / 100) + 5
   defense  = ((((base['defense']   + dv) * 2 + (sqrt(ev['defense']) / 4)) * level) / 100) + 5
   spatk    = ((((base['spatk']     + dv) * 2 + (sqrt(ev['spatk'])   / 4)) * level) / 100) + 5
   spdef    = ((((base['spdef']     + dv) * 2 + (sqrt(ev['spdef'])   / 4)) * level) / 100) + 5
   speed    = ((((base['speed']     + dv) * 2 + (sqrt(ev['speed'])   / 4)) * level) / 100) + 5

   hp       = str(int(hp))
   attack   = str(int(attack))
   defense  = str(int(defense))
   spatk    = str(int(spatk))
   spdef    = str(int(spdef))
   speed    = str(int(speed))

   print('%s    %s   %s    %s    %s        %s        %s' % (dv, hp, attack, defense, spatk, spdef, speed))

print('DV   HP   ATK   DEF   SP.ATK   SP.DEF   SPD')

d = 0
while d <= 15:
   get = get_stats(d)
   d += 1