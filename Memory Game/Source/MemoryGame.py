import pygame, sys, random
from pygame import *
from random import *

init()

size = width,height = 800,600

screen = display.set_mode(size) # makes the screen

best_time = [0, 4, 8, 12, 18, 20]

best_update = ""
frame_count = 0
frame_rate = 20
clock=pygame.time.Clock()
cards = []
card_types = []
sb = 0
length = 0
breadth = 0
bg1 = image.load('Pictures/menu_page.jpg').convert()          # loading images
question_mark = image.load('Pictures/question.jpg').convert()
empty = image.load('Pictures/empty.jpg').convert()
card_images = [image.load('Pictures/boy.jpg').convert(),\
                image.load('Pictures/bee.jpg').convert(),\
                image.load('Pictures/dog.jpg').convert(),\
                image.load('Pictures/duck.jpg').convert(),\
                image.load('Pictures/hunter.jpg').convert(),\
                image.load('Pictures/jackal.jpg').convert(),\
                image.load('Pictures/jerry.jpg').convert(),\
                image.load('Pictures/kitty.jpg').convert(),\
                image.load('Pictures/mario.jpg').convert(),\
                image.load('Pictures/popey.jpg').convert(),\
                image.load('Pictures/rabbit_girl.jpg').convert(),\
                image.load('Pictures/scooby.jpg').convert(),\
                image.load('Pictures/tweety.jpg').convert(),\
                image.load('Pictures/mickey.jpg').convert()]
chosen_cards = []

class card():   # the individual cards

    def __init__(self,c_type):

        self.c_type = c_type    # the type of card
        self.image = chosen_cards[c_type - 1]    # this means that the image will be a normal image
        self.matched = 0    # this is if the card has been matched up already

    def get_c_type(self):

        return self.c_type  # gets the type of card

    def get_image(self):
        return self.image   # gets the cards image

    def set_matched(self):
        self.matched = 1    # this sets the card to being matched

    def get_matched(self):
        return self.matched # reads if the card is matched

    
def no_of_cards(level):
        if level == 1:
            return 3
        elif level == 2:
            return 4
        elif level == 3:
            return 5
        elif level == 4:
            return 6
        elif level == 5:
            return 7

def make_level(level):
        nof_cards = no_of_cards(level)
        
        for i in range(len(cards)):
            cards.pop()
        for i in range(len(card_types)):
            card_types.pop()
        for i in range(1, nof_cards + 1):
            card_types.append(i)
            card_types.append(i)
        
        for i in range(len(chosen_cards)):
            chosen_cards.pop()
            
        c = card_images
               
        for i in range(nof_cards):
            ind = randint(0,len(c)-1)
            chosen_cards.append(c[ind])
            c.remove(c[ind])
        for i in range(len(chosen_cards)):
            card_images.append(chosen_cards[i])
        if(level == 1):
            row = 3
            col = 2
        elif(level == 2):
            row = 3
            col = 3
        elif(level == 3):
            row = 4
            col = 3
        elif(level == 4):
            row = 4
            col = 3
        elif(level == 5):
            row = 4
            col = 4
        for i in range(row): # this makes all the cards
            card_row = []
            for j in range(col):
                if level == 2 and i == 0 and j == 1:
                    card_row.append(empty)
                    continue
                if level == 3 and i == 0 and j == 0:
                    card_row.append(empty)
                    continue
                if level == 3 and i == 0 and j == 2:
                    card_row.append(empty)
                    continue
                if level == 5 and i == 0 and j == 1:
                    card_row.append(empty)
                    continue
                if level == 5 and i == 0 and j == 2:
                    card_row.append(empty)
                    continue
                rand_card = card_types[randint(0,len(card_types)-1)] # picks a random spot in card_types
                card_row.append(card(rand_card))   # makes the card and appends it to cards
                card_types.remove(rand_card)    # removes the number from card_types
            cards.append(card_row)
        

# more variables

choice = [0,0]
level = 1
screentype = 'main'     # this determines what screen the user is on

font1 = font.Font('Fonts/BOOKOS.ttf',40)
font2 = font.Font('Fonts/BOOKOS.ttf',16)
font3 = font.Font('Fonts/BOOKOS.ttf',60)

correct_pick = 0
    

while level <= 5:
    
    event.pump()
    k = key.get_pressed() 
    if k[K_ESCAPE]:
        break
    m = mouse.get_pressed()

    mx,my = mouse.get_pos()

    if screentype == 'main':    # runs the main screen

        screen.blit(transform.scale(bg1,size),(0,0))    # blits a scaled background

        if m[0] and 250 < mx < 550 and 150 < my < 250:  # button for playing
            make_level(level)
            screentype = 'game'
            time.wait(1000) # delays so that you don't automatically hit a card when it starts playing

        if m[0] and 200 < mx < 600 and 250 < my < 350:  # button for instructions
            screentype = 'instructions'

    elif screentype == 'instructions':  # instructions page

        screen.fill((128,0,255))

        intro1 = font1.render('Welcome to the matching game',1,(255,255,255))
        intro2 = font1.render('In this game players take turns flipping cards to',1,(255,255,255))
        intro3 = font1.render('try to get matches.',1,(255,255,255))

        intro4 = font1.render('Watch out, there are 5 cards that have no match!',1,(255,255,255))
        intro5 = font1.render('Click here to go back.',1,(255,255,255))

        screen.blit(intro1,(50,50))     # all the messages are drawn
        screen.blit(intro2,(50,100))
        screen.blit(intro3,(50,150))
        screen.blit(intro4,(50,200))
        screen.blit(intro5,(300,500))

        if m[0] and 300 < mx < 700 and 500 < my < 550:  # button to go back to the main screen
            screentype = 'main'
    elif screentype == 'next_level': # next level page
        screen.fill((128,0,255))
        best = font3.render('BEST : ' + str(best_time[level]) ,3,(255,255,255))
        your = font3.render("YOUR'S : " + str(total_seconds)  ,3,(255,255,255))
        Back = font1.render('BACK',1,(255,255,255))
        Next = font1.render('NEXT',1,(255,255,255))
        Main = font1.render('MAIN MENU',1,(255,255,255))

        screen.blit(Back,(50,500))     # all the messages are drawn
        screen.blit(Main,(275,500))
        screen.blit(Next,(620,500))
        screen.blit(best,(50,150))
        screen.blit(your,(50,300))
        if m[0] and 275 < mx < 500 and 500 < my < 550:
            screentype = 'main'
        elif m[0] and 50 < mx < 150 and 500 < my < 550:
            frame_count = 0
            frame_rate = 20
            correct_pick = 0
            make_level(level)
            screentype = 'game'
            if(best_time[level] > total_seconds):
                best_time[level] = total_seconds
            time.wait(1000)
        elif m[0] and 620 < mx < 720 and 500 < my < 550:
            frame_count = 0
            frame_rate = 20
            level += 1
            if level > 5 :
                screentype = 'main'
            correct_pick = 0
            make_level(level)
            screentype = 'game'
            if(best_time[level] > total_seconds):
                best_time[level] = total_seconds
            time.wait(1000)
        

    elif screentype == 'game':  # the game screen

        screen.fill((255,255,255))
        n = no_of_cards(level)
        
        if(level == 1):
            sb = 200
            length = 200
            breadth = 200
            row = 3
            col = 2
        elif(level == 2):
            sb = 100
            length = 200
            breadth = 200
            row = 3
            col = 3
        elif(level == 3):
            sb = 100
            length = 200
            breadth = 150
            row = 4
            col = 3
        elif(level == 4):
            sb = 100
            length = 200
            breadth = 150
            row = 4
            col = 3
        elif(level == 5):
            sb = 50
            length = 150
            breadth = 150
            row = 4
            col = 4
        for x in range(row):      # this goes through every card
            for y in range(col):
                if level == 2 and x == 0 and y == 1:
                    draw.rect(screen,(0,0,0),(sb+y*length,x*breadth,length,breadth),3)
                    screen.blit(transform.scale(empty,(length,breadth)),(sb+y*length,x*breadth))
                    continue
                if level == 3 and x == 0 and y == 0:
                    draw.rect(screen,(0,0,0),(sb+y*length,x*breadth,length,breadth),3)
                    screen.blit(transform.scale(empty,(length,breadth)),(sb+y*length,x*breadth))
                    continue
                if level == 3 and x == 0 and y == 2:
                    draw.rect(screen,(0,0,0),(sb+y*length,x*breadth,length,breadth),3)
                    screen.blit(transform.scale(empty,(length,breadth)),(sb+y*length,x*breadth))
                    continue
                if level == 5 and x == 0 and y == 1:
                    draw.rect(screen,(0,0,0),(sb+y*length,x*breadth,length,breadth),3)
                    screen.blit(transform.scale(empty,(length,breadth)),(sb+y*length,x*breadth))
                    continue
                if level == 5 and x == 0 and y == 2:
                    draw.rect(screen,(0,0,0),(sb+y*length,x*breadth,length,breadth),3)
                    screen.blit(transform.scale(empty,(length,breadth)),(sb+y*length,x*breadth))
                    continue
                if cards[x][y].get_matched() == 0: # only does anything if this card hasn't been matched yet

                    if sb+y*length < mx < sb+length+y*length and x*breadth < my < breadth+x*breadth:   # this means you're hovering over the current card

                        draw.rect(screen,(0,255,0),(sb+y*length,x*breadth,length,breadth),3) # draws rect around the card

                        if m[0]:    # if the card is clicked it will try and make it one of the choices

                            if choice[0] == 0:
                                choice[0] = cards[x][y]

                            elif choice[1] == 0 and choice[0] != cards[x][y]:
                                choice[1] = cards[x][y]

                    else:
                        draw.rect(screen,(0,0,0),(sb+y*length,x*breadth,length,breadth),3)

                    screen.blit(transform.scale(question_mark,(length,breadth)),(sb+y*length,x*breadth)) # draws the question mark

                    if choice[0] == cards[x][y]:   # draws the card only if you have it picked
                        screen.blit(transform.scale(choice[0].get_image(),(length,breadth)),(sb+y*length,x*breadth))

                    if choice[1] == cards[x][y]:   # draws the card only if you have it picked
                        screen.blit(transform.scale(choice[1].get_image(),(length,breadth)),(sb+y*length,x*breadth))

        if choice[0] != 0 and choice[1] != 0:   # if two cards have been picked

            display.flip()
            time.wait(2000) # delay so that the players can see the second picked card

            if choice[0].get_c_type() == choice[1].get_c_type():    # if both cards are the same type
                correct_pick += 1
                choice[0].set_matched() # make the cards matched up so that they wont be shown again
                choice[1].set_matched()

            choice = [0,0]  # finally resets the choices
        # Calculate total seconds
        total_seconds = frame_count // frame_rate
     
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
        # Limit to 20 frames per second
        clock.tick(frame_rate)
        if correct_pick == n:
            screentype = 'next_level'   
    
    display.flip()

    time.delay(20)  # delay 20 milliseconds for each frame

quit()
