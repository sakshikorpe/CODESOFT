import random
G=["rock","paper","scissor"]
while True1:
    pscore=0
    cscore=0
    tiescore=0
    pc=int(input('''
    START...
    ARE YOU READY?
    1 Yes
    2 No
    '''))
    if pc== 1:
        for a in range(1,6):
            playerInput=int(input('''
            1.Rock
            2.Paper
            3.Scissor
                 '''))
            if playerInput==1:
                pchoice="rock"
            elif playerInput==2:
                pchoice="paper"
            elif playerInput == 3:
                pchoice = "scissor"
            cchoice=random.choice(G)
            if cchoice==pchoice:
                print("Computer",cchoice)
                print(("Player",pchoice))
                tiescore=tiescore+1
            elif(pchoice=="rock"and cchoice=="scissor") or(pchoice=="paper" and cchoice=="rock")or(pchoice=="scissor" and cchoice=="paper"):
                print("Computer", cchoice)
                print(("Player", pchoice))
                pscore=pscore + 1
            else:
                print("Computer", cchoice)
                print(("Player", pchoice))
                cscore=cscore + 1
            if pscore==cscore:
                print("Match Draw")
                print("tie score",tiescore)
            elif pscore<cscore:
                print("Computer win the match")
                print("player score", pscore)
                print("computer score", cscore)
            else:
                print("Player win the match")
                print("player score", pscore)
                print("computer score", cscore)
        else:
            break
