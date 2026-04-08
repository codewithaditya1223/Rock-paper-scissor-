import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input(""" 
Game start
1yes
2No/exit
"""))
    if uc==1:
        for a in range(1,6):
            userInput=int(input("""
1Rock
2paper
3 scissor
"""))
            if userInput==1:
                unchoice="rock"
            elif userInput==2:
                unchoice="scissor"
            elif userInput==3:
                unchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==unchoice:
                print("computer value",Cchoice)
                print("user value",Cchoice)
                print("game draw")
            ucount=ucount+1
            ccount=ccount+1
    elif(unchoice=="rock" and Cchoice=="scissor") or (unchoice=="paper" and Cchoice=="rock") or(unchoice=="scissor" and Cchoice=="paper"):
        print("compuer value",Cchoice)
        print("user value",unchoice)
        print("you win")
        ucount=ucount+1
    else:
        print("compurt value",Cchoice)
        print("user value",unchoice)
        print("computer win")
        ccount=ccount+1
    if ucount==ccount:
        print("final game draw")
        print("user score",ucount)
        print("computer score",ccount)
    elif(ucount>ccount):
        print("final you win the draw")
        print("user score",ucount)
        print("computer score",ccount)
    else:
        print("computer win the game")
        print("user score",ucount)
        print("computer score",ccount)

        break