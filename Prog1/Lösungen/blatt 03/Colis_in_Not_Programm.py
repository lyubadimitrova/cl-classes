#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on Fri Nov 11 22:59:00 2016
# author: Lyuba Dimitrova & Martina Brauchler
# Aufgabe 10: Colis in Not

# verwendete Module
import random  # für den Zufall


# Variablen
name_coli = ['Coli1', 'Coli2', 'Coli3', 'Coli4', 'Coli5', 'Coli6', 'Coli7']
group_1 = ['Coli1', 'Coli2', 'Coli3', 'Coli4', 'Coli5', 'Coli6', ]
group_2 = ['Coli7']
closed = True
openn = False
state_box = closed  # Startzustand der Truhe
changed_state = []  # Liste wer den Zustand der Truhe bereits geändert hat
saw_changed_states = 0  # Startwert für den zählenden Coli
picked_coli = 'Coli'

# Funktionen


def pick_Coli():
    i = random.randint(0, 6)  # Index von name_coli
    picked_coli = name_coli[i]
    return picked_coli

# Programmablauf
while True:
    picked_coli = pick_Coli()
    print(picked_coli)
    # Prüfe welcher Gruppe der gezogene Coli angehört
    if picked_coli in group_1:
        # Prüfe ob Coli aus Gruppe 1 Zustand der Truhe schon verändert hat
        # Wähle davon abhängig ob er etwas tut
        if picked_coli not in changed_state:
            if state_box == closed:
                state_box = openn
                changed_state.append(picked_coli)
    else:
        # Beobachte und Zähle Zustandsveränderungen der Truhe
        if state_box == openn:
            state_box = closed
            saw_changed_states += 1
    # Endbedingung für while-Schleife, Ausgabe während Durchlauf
    if saw_changed_states == 6:
        break
    elif state_box == closed:
        print("closed", "\n")
    else:
        print("open", "\n")

print("Spiel gewonnen! Colis frei!")
