import pygame
import time
import sys
from nltk.corpus import words
import random

from pygame.constants import QUIT

pygame.init()
width,height=1000,600
disp=pygame.display.set_mode((width,height))

black=(0,0,0)
fps=60
five_letter_words = [w for w in words.words() if len(w) <= 5]
health1=100
health2=100
name1="Player 1" #user input
name2="Player 2"
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
d = { '.-':'A','-...':'B','-.-.':'C', '-..':'D', '.':'E','..-.':'F', '--.':'G', '....':'H','..':'I', '.---':'J', '-.-':'K','.-..':'L', '--':'M', '-.':'N','---':'O', '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T','..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', '--..':'Z'}

#rules="1) A simple yet fun 2 player game to learn and practice morse code!\n 2) Words/ letters are randomly generated and both players are required to enter its morse form\n 3) Fastest person to complete the word correctly damages the other player with a small attack", "4) Words will be generated until one player loses all their health\n 5) BE WARNED: Any mistakes leads to your input being reseted. Player has to re-enter the morse code from the first letter\n 6) Have Fun!"
rules="Press W for player 1 and Press UP key for player 2"
axe=pygame.image.load("axe.jpeg")
axe=pygame.transform.scale(axe,(260,240))
sword=pygame.image.load("sword.jpeg")
sword=pygame.transform.scale(sword,(240,240))
h20=pygame.image.load("health2_0.jpeg")
h2100=pygame.image.load("health2_100.jpeg")
h275=pygame.image.load("health2_75.jpeg")
h225=pygame.image.load("health2_25.jpeg")
h250=pygame.image.load("health2_50.jpeg")
h10=pygame.image.load("health1_0.jpeg")
h1100=pygame.image.load("health1_100.jpeg")
h175=pygame.image.load("health1_75.jpeg")
h125=pygame.image.load("health1_25.jpeg")
h150=pygame.image.load("health1_50.jpeg")
h10=pygame.transform.scale(h10,(140,40))
h1100=pygame.transform.scale(h1100,(140,40))
h150=pygame.transform.scale(h150,(140,40))
h175=pygame.transform.scale(h175,(140,40))
h125=pygame.transform.scale(h125,(140,40))
h20=pygame.transform.scale(h20,(140,40))
h250=pygame.transform.scale(h250,(140,40))
h275=pygame.transform.scale(h275,(140,40))
h2100=pygame.transform.scale(h2100,(140,40))
h225=pygame.transform.scale(h225,(140,40))
p1die=pygame.image.load("p2_kill.jpeg")
p1die=pygame.transform.scale(p1die,(480,280))
p2die=pygame.image.load("p1_kill.jpeg")
p2die=pygame.transform.scale(p2die,(480,280))
axe=pygame.image.load("axe.jpeg")
axe=pygame.transform.scale(axe,(220,200))
sword=pygame.image.load("sword.jpeg")
sword=pygame.transform.scale(sword,(200,200))
axeattack=pygame.image.load("axeattack.jpeg")
axeattack=pygame.transform.scale(axeattack,(500,250))
swattack=pygame.image.load("swattack.jpeg")
swattack=pygame.transform.scale(swattack,(500,250))

def wordtomorse(word):
    wordmorse=""
    for letter in word:
        for k in d:
            if(d[k]==letter):
                wordmorse+=k+'/'
    return wordmorse


ti=0.5

def gameloop(diff):
    word=random.choice(five_letter_words).upper()
    if(diff==1):
        word=word[0]
    wordmorse=wordtomorse(word)
    print(wordmorse)
    score1=100;score2=100
    i1=0;prev1=0;a1="";h1=0
    i2=0;prev2=0;a2="";h2=0
    while(1):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    t1 = time.time()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    t1 = time.time() - t1
                    t1 = t1 % 60
                    if(t1<1*ti and wordmorse[i1]=='.'):
                        print("dot")
                        i1+=1
                        if(wordmorse[i1]=='/' and i1!=len(wordmorse)-1):
                            print("NEW LETTER")
                            a1+=d[wordmorse[prev1:i1]]
                            i1+=1
                            prev1=i1
                        
                    elif(t1>=1*ti and wordmorse[i1]=='-'):
                        print("dash")
                        i1+=1
                        if(wordmorse[i1]=='/' and i1!=len(wordmorse)-1):
                            print("NEW LETTER")
                            a1+=d[wordmorse[prev1:i1]]
                            i1+=1
                            prev1=i1
                    elif(wordmorse[i1]!='/'):
                        i1=0;prev1=0;a1=""
                    
                    if(i1==len(wordmorse)-1):
                        print("ATTACK!")
                        a1="ATTACK!"
                        score2-=25
                        h1+=1
                        word=random.choice(five_letter_words).upper()
                        if(diff==1):
                            word=word[0]
                        if word=='T' or word=='E':
                            word='Z'
                        print(word)
                        wordmorse=wordtomorse(word)
                        print(wordmorse)
                        i1=0
                        prev1=0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    t2 = time.time()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    t2 = time.time() - t2
                    t2 = t2 % 60
                    if(t2<1*ti and wordmorse[i2]=='.'):
                        print("dot")
                        i2+=1
                        if(wordmorse[i2]=='/' and i2!=len(wordmorse)-1):
                            print("NEW LETTER")
                            a2+=d[wordmorse[prev2:i2]]
                            i2+=1
                            prev2=i2
                        
                    elif(t2>=1*ti and wordmorse[i2]=='-'):
                        print("dash")
                        i2+=1
                        if(wordmorse[i2]=='/' and i2!=len(wordmorse)-1):
                            print("NEW LETTER")
                            a2+=d[wordmorse[prev2:i2]]
                            i2+=1
                            prev2=i2
                    elif(wordmorse[i2]!='/'):
                        i2=0;prev2=0;a2=""
                    
                    if(i2==len(wordmorse)-1):
                        print("ATTACK!")
                        a2="ATTACK!"
                        score1-=25 
                        h2+=1 
                        word=random.choice(five_letter_words).upper()
                        if(diff==1):
                            word=word[0]
                        if word=='T' or word=='E':
                            word='Z'
                        print(word)
                        wordmorse=wordtomorse(word)    
                        print(wordmorse)
                        i2=0
                        prev2=0
               

        clk=pygame.time.Clock()
        disp.fill(black)

        if(h1==1):
            disp.blit(h275,(840,80))
        elif(h1==2):
            disp.blit(h250,(840,80))
        elif(h1==3):
            disp.blit(h225,(840,80))
        elif(h1==4):
            disp.blit(h20,(840,80))
        else:
            disp.blit(h2100,(840,80))
        

        if(h2==1):
            disp.blit(h175,(30,80))
        elif(h2==2):
            disp.blit(h150,(30,80))
        elif(h2==3):
            disp.blit(h125,(30,80))
        elif(h2==4):
            disp.blit(h10,(30,80))
        else:
            disp.blit(h1100,(30,80))
        currd1=myfont.render(a1,False,(255,255,255))
        disp.blit(currd1,(150,450))
        currd2=myfont.render(a2,False,(255,255,255))
        disp.blit(currd2,(660,450))
        p1=myfont.render(name1,False,(255,255,255))
        p2=myfont.render(name2,False,(255,255,255))
        if(diff==1):
            text=myfont.render("Letter: "+word,False,(255,255,255))
            lmorse=myfont.render(wordmorse[:-1],False,(255,255,255))
        else:
            text=myfont.render("Word: "+word,False,(255,255,255))
        disp.blit(p1,(40,30))
        disp.blit(p2,(850,30))
        if(a1=="ATTACK!"):
            disp.blit(swattack,(210,200))
        elif(a2=="ATTACK!"):
            disp.blit(axeattack,(220,200))
        elif(score1==0):
            disp.blit(p1die,(190,200))
            win2=myfont.render("Player 2 wins",False,(255,255,255))
            disp.blit(win2,(400,100))

        elif(score2==0):
            disp.blit(p2die,(220,200)) 
            win1=myfont.render("Player 1 wins",False,(255,255,255))
            disp.blit(win1,(400,100))
        else:
            disp.blit(text,(420,70))
            disp.blit(sword,(190,200))
            disp.blit(axe,(590,200))
            if(diff==1): disp.blit(lmorse,(450,100))
        pygame.display.update()
        if(a1=="ATTACK!"):
            pygame.time.wait(1500)
            a1=""
            a2=""
        if(a2=="ATTACK!"):
            pygame.time.wait(1500)
            a2=""
            a1=""
        clk.tick(fps)
while(1):
    disp.fill(black)
    title=myfont.render("DASH DOT",False,(255,255,255))
    disp.blit(title,(400,100))
    text1=myfont.render("Enter 1 for learning/practice",False,(255,255,255))
    disp.blit(text1,(300,250))
    text2=myfont.render("Enter 2 for hard",False,(255,255,255))
    disp.blit(text2,(300,300))
    r=myfont.render(rules,False,(255,255,255))
    disp.blit(r,(180,390))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                gameloop(1)
            elif event.key == pygame.K_2:
                gameloop(2)