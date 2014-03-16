#!/usr/bin/env python

import random

# First step, construct a random ring of players
# The ring is a tuple of (killer, victim) that forms a single loop

with open('players.txt', 'r') as f:
    players = [l.strip() for l in f.readlines()]
random.shuffle(players)

ring = []
for i in range(len(players)):
    if i == len(players) - 1:
        ring.append((players[i], players[0]))
    else:
        ring.append((players[i], players[i+1]))

# Next, a location and item for each pair

with open('items.txt', 'r') as f:
    items = [l.strip() for l in f.readlines()]

with open('locations.txt', 'r') as f:
    locations = [l.strip() for l in f.readlines()]

game = [(p, random.choice(locations), random.choice(items)) for p in ring]

# Sort game to be alphabetical by killer for easier handout
game.sort(key=lambda g: g[0][0], reverse=True)

# Print the latex header

with open('murder-out.tex', 'w') as f:
    print(r"""
        \documentclass{article}
        \usepackage[cm]{fullpage}
        \usepackage{array}
        \makeatletter
        \newcommand{\thickhline}{%
            \noalign {\ifnum 0=`}\fi \hrule height 1pt
            \futurelet \reserved@a \@xhline
        }
        \newcolumntype{"}{@{\hskip\tabcolsep\vrule width 1pt\hskip\tabcolsep}}
        \makeatother
        \begin{document}
        \centering
        \renewcommand{\arraystretch}{3}
        \setlength{\tabcolsep}{10pt}
        \large
    """, file=f)

# Print the actual game

    while game:
        print(r"""
            \begin{tabular}{"c"}
            \thickhline
        """, file=f)
        print ("-"*120 + r"\\", file=f)
        for i in range(15):
            if game:
                g = game.pop()
                print(r"\thickhline", file=f)
                print (r"{{\tiny({})}} \textsc{{Target:}} {}, {} with {}\\".format(g[0][0], g[0][1], g[1], g[2]), file=f)

        print(r"""
            \thickhline
            \end{tabular}
        """, file=f)

# Print the latex footer

    print(r"""
        \end{document}
    """, file=f)
