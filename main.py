from time import sleep

import pygame
import os
from option import OptionButton
from button import Button
import script
import game_theory
import speech_recognition as sr
import pyttsx3
import sqlite3
from gtts import gTTS
import time

game_theory.imports()

# create game window
WIDTH, HEIGHT = 1600, 900  # <-- change this to your screen resolution
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Story Game")
pygame.font.init()
pygame.mixer.init(44100, -16, 2, 4096)


# load assets
START_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "start.png")), (250, 250))
QUIT_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "quit.png")), (225, 90))
NEXT_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "next2.png")), (50,50))
SUBMIT_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "submit.jpg")), (130,31))
SOUND_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "sound.png")), (50,50))
#SPEECH_ON_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "sound.png")), (64, 64))
#SPEECH_OFF_BT = pygame.transform.scale(pygame.image.load(os.path.join("assets/images", "no-sound.png")), (64, 64))

MAIN_MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "main_menu2.png")),
                                      (WIDTH-100, HEIGHT-50))
BLACK_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "black_ground.png")),
                                      (WIDTH-100, HEIGHT-50))

MAIN_MENU_MUSIC = pygame.mixer.Sound(os.path.join("assets/audios", "2.ogg"))
MAIN_MENU_MUSIC.set_volume(0.3)
GAMEPLAY_MUSIC = pygame.mixer.Sound(os.path.join("assets/audios", "game_audio.mp3"))
GAMEPLAY_MUSIC.set_volume(0.2)

# button
start_button = Button(START_BT, (WIDTH / 2, HEIGHT / 2))
quit_button = Button(QUIT_BT, (WIDTH - 300, 130))
next_button=Button(NEXT_BT, (WIDTH-240, HEIGHT/2))
submit_button=Button(SUBMIT_BT, (270, 470))
sound_button=Button(SOUND_BT, (250,130))
#speech_on_button = Button(SPEECH_ON_BT, (250, 130))
#speech_off_button = Button(SPEECH_OFF_BT, (250, 130))


input_rect = pygame.Rect(260, 200, 140, 32)
input_rect2= pygame.Rect(260, 280, 140, 32)
input_rect3= pygame.Rect(260, 360, 140, 32)

parts = [script.part_1, script.part_2]

current_part = 0
current_scene = 0
run = True
speech_on = False
current_footer_text=""
answers = list()
help=0 
mor=0 
loyt=0
dec=0
lead=0
var1=0
percnt_help=0
percnt_mor=0
percnt_loyt=0
percnt_dec=0
percnt_lead=0
#var2=0
#user_text=""
#color_active = pygame.Color('lightskyblue3')
# color_passive store color(chartreuse4) which is
# color of input box.
#color_passive = pygame.Color('chartreuse4')
#color = color_passive



# def play_audio(text):
#     tts = gTTS(text=text, lang='en')
#     # time to text
#     temp = time.time()
#     file_name = "assets/audios/speech/" + str(temp) + ".mp3"
#     tts.save(file_name)
#     pygame.mixer.music.load(file_name)
#     pygame.mixer.music.play()


#keeps track of the value of the traits
def behaviour(var1, var2):
    global help,mor, loyt, dec, lead
    #print("help initial", help)
    if var1=='1':
        if help!=0 and var2==1:
            help+=1
        elif help!=0 and var2==0:
            help-=1
        elif help==0 and var2==1:
            help+=1
    #print("help value",help)
    if var1=='2':
        if mor!=0 and var2==1:
            mor+=1
        elif mor!=0 and var2==0:
            mor-=1
        elif mor==0 and var2==1:
            mor+=1
    #print("mortality value", mor)
    if var1=='3':
        if loyt!=0 and var2==1:
            loyt+=1
        elif loyt!=0 and var2==0:
            loyt-=1
        elif loyt==0 and var2==1:
            loyt+=1
    #print("loyalty", loyt)
    if var1=='4':
        if dec!=0 and var2==1:
            dec+=1
        elif dec!=0 and var2==0:
            dec-=1
        elif dec==0 and var2==1:
            dec+=1
    #print("decision making", dec)
    if var1=='5':
        if lead!=0 and var2==1:
            lead+=1
        elif lead!=0 and var2==0:
            lead-=1
        elif lead==0 and var2==1:
            lead+=1
    #print("leadership", lead)


#calculates percentages
def calculate(help,moral,loyal,deci,leader):
    global percnt_help, percnt_mor,percnt_loyt,percnt_dec, percnt_lead
    percnt_help=int((help/3)*100)
    percnt_mor=int((moral/3)*100)
    percnt_loyt=int((loyal/3)*100)
    percnt_dec=int((deci/3)*100)
    percnt_lead=int((leader/3)*100)

    print(percnt_help, percnt_mor, percnt_loyt, percnt_dec, percnt_lead)
    if percnt_help<50:
        txt_hlp="You show relative less helpfulness towards others."
    else:
        txt_hlp="You are helpfull towards others."

    if percnt_mor<50:
        txt_mor="Tend to show a low sense of morality, you dont always think of better of others."
    else:
        txt_mor="Having a high sense of morality, you are always taking decisions for the best of others."

    if percnt_loyt<50:
        txt_loyt="You are prone to showing less loyalty towards your duty and peers."
    else:
        txt_loyt="Always loyal towards your duty and peers"

    if percnt_dec<50:
        txt_dec="Lack decision-making abilities, default at reading situations correctly. You take decisions that dont profit you in the long run."
    else:
        txt_dec="Have efficient decision-making abilities, you take decisions based on effective decuctions of situations and having a long-term goal in mind."

    if percnt_lead<50:
        txt_lead="Lack of leadership skills, you tend to perform well when there's someone to guide you."
    else:
        txt_lead="High leadership skills, you have the ability to lead your peers to success and beyond."
    
    txt=txt_hlp+" "+txt_mor+" "+txt_loyt+" "+txt_dec+" "+txt_lead
    return(txt)



#displaying footer texts
def display_footer(text, font):
    i = 0
    text_width, text_height = font.size(text)
    # if the text is too long, split it into multiple lines
    if text_width > 1200:
        # split the text into words
        words = text.split(" ")
        # create a new line
        new_line = ""
        # loop through each word
        for word in words:
            # if the new line is empty, add the word to it
            if new_line == "":
                new_line = word
            # if the new line is not empty, add the word to it and check if the line is too long
            else:
                # if the line is too long, display the line and start a new line
                if font.size(new_line + " " + word)[0] > 1200:
                    window.blit(font.render(new_line, True, (255, 255, 255)), (165, (HEIGHT - 180) + 30 * i))
                    i += 1
                    new_line = word
                # if the line is not too long, add the word to the line
                else:
                    new_line += " " + word
        # display the last line
        window.blit(font.render(new_line, True, (255, 255, 255)), (165, (HEIGHT - 180) + 30 * i))
    # if the text is not too long, display it
    else:
        window.blit(font.render(text, True, (255, 255, 255)), (165, (HEIGHT - 180) + 30 * i))




def display_para(text, font):
    i = 0
    text_width, text_height = font.size(text)
    # if the text is too long, split it into multiple lines
    if text_width > 1200:
        # split the text into words
        words = text.split(" ")
        # create a new line
        new_line = ""
        # loop through each word
        for word in words:
            # if the new line is empty, add the word to it
            if new_line == "":
                new_line = word
            # if the new line is not empty, add the word to it and check if the line is too long
            else:
                # if the line is too long, display the line and start a new line
                if font.size(new_line + " " + word)[0] > 1200:
                    window.blit(font.render(new_line, True, (255, 255, 255)), (WIDTH/2-530, (HEIGHT/2) + 35 * i))
                    i += 1
                    new_line = word
                # if the line is not too long, add the word to the line
                else:
                    new_line += " " + word
        # display the last line
        window.blit(font.render(new_line, True, (255, 255, 255)), (WIDTH/2 -530, (HEIGHT/2) + 35 * i))
    # if the text is not too long, display it
    else:
        window.blit(font.render(text, True, (255, 255, 255)), (WIDTH/2-530, (HEIGHT/2) + 35 * i))

# display options in the middle of the screen
def display_options(options, font):
    # loop through each option
    for i in range(len(options)):
        # create an option button
        if len(options) > 2:
            option=options[i]
            option = OptionButton(option[:len(option)-1], 100 * i + 175 - 125, WIDTH, font, pygame, window)
        else:
            option=options[i]
            option = OptionButton(option[:len(option)-1], 100 * i + 175, WIDTH, font, pygame, window)
        # draw the option
        option.draw(window)
        # if the option is clicked, set the chosen option to the current option
        if option.is_clicked():
            parts[current_part][current_scene].chosen = i
            answers.append(options[i])
            var=game_theory.predict(answers[len(answers)-1])
            l=var.tolist()
            # print(l[0])
            # if(l[0]==0):
            #     print(1)
            # else:
            #     print(type(l[0]))
            #print(len(answers))
            var1=answers[len(answers)-1][-1:]
            #print("trait", var1)
            #print("behaviour", l[0], answers[len(answers)-1])
            behaviour(var1,l[0])
            decide()







def decide():
    global current_scene, run, current_part, current_footer_text
    # if the current part is the last part, end the game
    if len(parts[current_part]) - 1 == current_scene:
        if current_part < len(parts) - 1:
            current_part += 1
            current_scene = -1
    # if the current part is not the last part, go to the next scene
    if current_part == 0:
        if parts[current_part][current_scene].chosen != -1:
            if parts[current_part][current_scene].chosen == 0:
                parts[current_part].extend(script.part_1_question_1_option_1)
            else:
                parts[current_part].extend(script.part_1_question_1_option_2)
            current_scene += 1
        else:
            if current_scene < len(parts[current_part]) - 1:
                current_scene += 1
    if current_part == 1:
        if current_scene < len(parts[current_part]) - 1:
            current_scene += 1
    current_footer_text = parts[current_part][current_scene].text
    # if speech_on:
    #     play_audio(current_footer_text)








# main loop
def main():
    FPS = 60
    TIMER = pygame.time.get_ticks() / 1000
    conn=sqlite3.connect('D-day_database.db')
    cursor=conn.cursor()
    started = False
    register=False
    user_text=''
    user_text2=''
    user_text3=''
    # redraw/refresh the screen
    def refresh_display():
        global var1, help, mor, loyt, lead, dec, text_box
        global percnt_help, percnt_mor,percnt_loyt,percnt_dec, percnt_lead
        #active=False
        font = pygame.font.SysFont("comicsans", 20)
        font2=pygame.font.SysFont("comicsans", 25)
        if started and register:
            # draw the background
            if current_scene==37 and var1==0:
                text_box=calculate(help,mor,loyt,dec,lead)
                entities=(user_text,user_text2,user_text3,percnt_help,percnt_mor,percnt_loyt,percnt_dec,percnt_lead)
                cursor.execute('''INSERT INTO user_details(Name,Age,Gender,Help,Morality,Loyal,Decision,Leader) VALUES (?,?,?,?,?,?,?,?)''', entities)
                conn.commit()
                conn.close()
                var1=1
                print(text_box)
            if current_scene==37:
                #window.blit(MAIN_MENU_BG, (0, 0))
                window.blit(BLACK_BG,(0,0))
                display_para(text_box, font)
                #pygame.draw.rect(window, (0, 0, 0, 128), (160, HEIGHT - 180, WIDTH, 120), 0, 10)
                #display_footer(text_box, font)
                #text_surface = font.render(text_box, True, (250,250,250))
                #window.blit(text_surface,(WIDTH / 2 , HEIGHT / 2))
                #pygame.display.update()

            else:
                window.blit(parts[current_part][current_scene].background, (0, 0))
            
            # draw the quit button
            quit_button.update(window)
            next_button.update(window)
            sound_button.update(window)
            # if speech_on:
            #     speech_on_button.update(window)
            # else:
            #     speech_off_button.update(window)


            # draw a rectangle in the bottom section of the screen to display text
            pygame.draw.rect(window, (0, 0, 0, 128), (160, HEIGHT - 180, WIDTH, 120), 0, 10)

            # display the parts[current_part] text in the bottom section of the screen in a specific width
            display_footer(parts[current_part][current_scene].text, font)
            #if current_scene==60:
            #  #   display_footer(text_box, font)
            #     white=(255,255,255)
            #     txtsurf = font.render("Hello, World", white)
            #     window.blit(txtsurf,(0,0))

            # display options
            display_options(parts[current_part][current_scene].options, font)
        elif register:
            # draw the background
            window.blit(MAIN_MENU_BG, (0, 0))
            # draw the start button
            start_button.update(window)
        #elif var2==0 and started==False:
        else:
            #window.fill((255,255,255))
            window.blit(MAIN_MENU_BG, (0, 0))
            color = pygame.Color('chartreuse4')
            text = font2.render('User Details', True, (255,255,255), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (250, 130)
            window.blit(text, textRect)

            name_text=font2.render('Name', True, (255,255,255))
            name_textRect=name_text.get_rect()
            name_textRect.center=(210,210)
            window.blit(name_text,name_textRect)

            name_age=font2.render('Age', True, (255,255,255))
            name_ageRect=name_age.get_rect()
            name_ageRect.center=(210,290)
            window.blit(name_age,name_ageRect)

            name_sex=font2.render('Gender', True, (255,255,255))
            name_sexRect=name_sex.get_rect()
            name_sexRect.center=(210,370)
            window.blit(name_sex,name_sexRect)


            pygame.draw.rect(window, color, input_rect)
            pygame.draw.rect(window, color, input_rect2)
            pygame.draw.rect(window, color, input_rect3)
            text_surface = font.render(user_text, True, (255, 255, 255))
            text_surface2 = font.render(user_text2, True, (255,255, 255))
            text_surface3 = font.render(user_text3, True, (255,255, 255))
            window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            window.blit(text_surface2, (input_rect2.x+5, input_rect2.y+5))
            window.blit(text_surface3, (input_rect3.x+5, input_rect3.y+5))
            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width()+10)
            input_rect2.w = max(100, text_surface2.get_width()+10)
            input_rect3.w = max(100, text_surface3.get_width()+10)
            quit_button.update(window)
            submit_button.update(window)
            pygame.display.update()
        #print(var2)


        pygame.display.update()

    global run #,user_text, color, color_passive, color_active, var2
    r=sr.Recognizer()
    while run:
        global current_scene, speech_on
        TIMER = pygame.time.get_ticks() / 1000
        if started:
            GAMEPLAY_MUSIC.play()
            MAIN_MENU_MUSIC.stop()
        else:
            MAIN_MENU_MUSIC.play()
            GAMEPLAY_MUSIC.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if the user clicks the mouse, go to the next scene
            if event.type == pygame.MOUSEBUTTONDOWN and next_button.checkForInput(pygame.mouse.get_pos()) and started and parts[current_part][current_scene].options == []:
                decide()
            # if the user clicks the mouse, start the game
            if event.type == pygame.MOUSEBUTTONDOWN and not started:
                if start_button.checkForInput(pygame.mouse.get_pos()):
                    started = True
                    #var2=2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.checkForInput(pygame.mouse.get_pos()):
                    #print(answers)
                    run = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if speech_on_button.checkForInput(pygame.mouse.get_pos()) and not speech_on:
            #         speech_on = True
            #         break
            #     elif speech_off_button.checkForInput(pygame.mouse.get_pos()) and speech_on:
            #         speech_on = False
            #         break
            if event.type== pygame.MOUSEBUTTONDOWN and sound_button.checkForInput(pygame.mouse.get_pos()):
                GAMEPLAY_MUSIC.stop()
                engine=pyttsx3.init()
                engine.say(parts[current_part][current_scene].text)
                engine.runAndWait()
                GAMEPLAY_MUSIC.play()
            
            #if event.type==pygame.MOUSEBUTTONDOWN: 
             #   if input_rect.collidepoint(event.pos):
              #      active=True
               # else:
                #    active=False
                #if active:
                 #   color=color_active
                #else:
            #         color=color_passive
            # pygame.draw.rect(window, color, input_rect)
            if input_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text=user_text[:-1]
                    else:
                        user_text +=event.unicode
            if input_rect2.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text2=user_text2[:-1]
                    else:
                        user_text2 +=event.unicode
            if input_rect3.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text3=user_text3[:-1]
                    else:
                        user_text3 +=event.unicode
            if event.type== pygame.MOUSEBUTTONDOWN and submit_button.checkForInput(pygame.mouse.get_pos()) and user_text!='' and user_text2!='' and user_text3!='' :
                #print(user_text)
                #print(user_text2)
                #print(user_text3)
                register=True
            #     var2=1
            #     print("user text", var2)
            


        refresh_display()

    pygame.quit()






if __name__ == "__main__":
    main()
