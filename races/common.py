from __future__ import annotations

from races import Fighter


class Player(Fighter):
    name = "You"
    char = ord("@")
    color = (255, 255, 255)

    hp = 30
    power = 5
    defense = 2


class Orc(Fighter):
    name = "Orc"
    char = ord("o")
    color = (63, 127, 63)

    hp = 10
    power = 3
    defense = 0


class Troll(Fighter):
    name = "Troll"
    char = ord("T")
    color = (0, 127, 0)

    hp = 16
    power = 4
    defense = 1
