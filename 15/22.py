import sys
from dataclasses import dataclass
from typing import Optional

@dataclass(unsafe_hash=True)
class Effect:
    dmg: int = 0
    armor: int = 0
    hp: int = 0
    mana: int = 0
    duration: int = 0

@dataclass
class Spell:
    cost: int
    instant: Optional[Effect] = None
    effect: Optional[Effect] = None

boss_hp, boss_atk = [int(l.split(': ')[1]) for l in sys.stdin]
spells = [
    Spell(53, Effect(dmg = 4)),
    Spell(73, Effect(dmg = 2, hp = 4)),
    Spell(113, None, Effect(armor = 7, duration = 6)),
    Spell(173, None, Effect(dmg = 3, duration = 6)),
    Spell(229, None, Effect(mana = 101, duration = 5))
]

def fight(moves, hard = False):
    b_hp, b_atk = boss_hp, boss_atk
    hp, mana = 50, 500
    armor = 0
    effects = {e: 0 for s in spells for e in (s.instant, s.effect) if e}
    turn = True

    while True:
        if hp <= 0 or mana < 0:
            return None

        for effect in effects:
            if not effects[effect]:
                continue
            b_hp -= effect.dmg
            mana += effect.mana
            if effect.armor:
                armor = effect.armor

            effects[effect] -= 1
            if effects[effect] == 0:
                if effect.armor:
                    armor = 0

        if b_hp <= 0:
            return True

        if turn:
            hp -= hard

            try:
                spell = spells[next(moves)]
            except:
                return False
            mana -= spell.cost

            if spell.instant:
                effect = spell.instant
                b_hp -= effect.dmg
                hp += effect.hp
            elif spell.effect:
                effect = spell.effect
                if effects[effect]:
                    return None
                effects[effect] = effect.duration
        else:
            hp -= max(1, b_atk - armor)

        turn = not turn

for hard in (False, True):
    good = [[s] for s in range(len(spells))]
    res = None
    while not res:
        new = []
        for prefix in good:
            for move in range(len(spells)):
                if move > 1 and move in prefix[-2 :]:
                    continue

                moves = prefix + [move]
                ret = fight(iter(moves), hard)
                if ret:
                    cost = sum(spells[m].cost for m in moves)
                    res = min(res, cost) if res else cost
                elif ret is False:
                    new.append(moves)
        good = new
    print(res)
