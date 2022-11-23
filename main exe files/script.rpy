# The script of the game goes in this file.
define you= Character("You")
define gen_1= Character("Informant")
define gen_2= Character("General Franz")
define sol_1= Character("Soldier")
define prisoner= Character("Prisoner")

#ATL
transform wiggle(x=950, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0


#CHARACTER MODELS
image gen_1= im.Scale("general_1.png",800,900)
image gen_2= im.Scale("general_2.png",800,900)
image sol_1= im.Scale("soldier_1.png",800,900)
image prisoner= im.Scale("prisoner.png",800,900)


#SCENE MODEL
image prison_1= im.Scale("prison_1.jpg",1920,1080)
image prison_2= im.Scale("prison_2.jpg",1920,1080)
image battle="battlefield.jpg"
image council="council_room.jpg"
image help_1=im.Scale("help_1_war.jpg",1920,1080)



# The game starts here!!


label start:

    $help=0
    $loyal=0
    $cruel=0

    scene black with dissolve
    pause 1
    show text"{size=+30} B.A.S.S presents{/size}" with dissolve
    pause 3.5
    show text"{size=+30}  1 September,1939, Britain... {/size}" with dissolve
    pause 2


    scene council with dissolve
    pause 1
    show gen_1 at center with dissolve
    gen_1 "COMMANDER!!! We just recieved new intel from Poland!"
    gen_1 "Germany has crossed into their territory with armed forces! They are quickly advancing into WARSAW!"
    gen_1 "France is on standby, waiting for the British' official call. We need your decision Commander!! "

    menu:
     "Send troops to Poland , breaking out a war against Germany":
         pause 0.5
         jump help_1_yes

     "Stay neutral, let Poland handle the situation":
         pause 1
         gen_1 "Wise choice commander!"
         jump help_1_no



#PART 2 START!!

    label part_2:
    scene council with dissolve
    pause 1


    show gen_1 at center with dissolve
    pause 1
    gen_1 "Phew.. That was ugly. German forces are too strong to battle right now. We need more time!"
    hide gen_1 with dissolve
    " Few days pass by... German regiment grows stronger"
    show gen_1 at left with dissolve
    " Sir! You have someone waiting to meet you. He says its urgent."
    hide gen_1 with dissolve
    show gen_2 at right with dissolve
    pause 1
    gen_2 " Sir we managed to take captive a GERMAN INTELLIGENCE AGENT.. he was a spy, RIGHT UNDER OUR NOSES!!"
    gen_2 " Your presence is urgent! Please follow me"
    scene prison_1 with dissolve
    show prisoner at right with dissolve
    pause 1.5
    show gen_2 at left with dissolve

    gen_2 " He can give us classified information of Germans which can CHANGE THE COURSE OF THE WAR.. But he isn't talking."
    gen_2 " DO what has to be done.."
    hide gen_2 with dissolve
    pause 0.5
    show prisoner at center with easeinleft

    prisoner "..."
    $pain=0

    label torture:

        if pain<=4:

            menu:
                "1.PUNCH IN THE STOMACH":
                    show prisoner at wiggle
                    pause 0.5
                    $pain+=1
                    prisoner "*grunts*"
                    jump torture


                "2.USE ELECTRIC SHOCK":
                    pause 0.5
                    show prisoner at wiggle
                    $pain+=2
                    prisoner "*aaggghhh*"
                    pause 0.5
                    jump torture

                "3.REMOVE A NAIL":
                    pause 0.5
                    show prisoner at wiggle
                    $pain+=3
                    prisoner "*aaaaaggghhhhhhhh"
                    pause 0.5
                    jump torture

                "4.TALK":
                    pause 0.5
                    prisoner"... heil Hitler!!"
                    jump torture

        else:
            prisoner" Okay okay please STOP!! What do you want from me..."
            pause 1

        you "Tell us what you know and we will spare you your life"
        prisoner" Colombia...der Fuhrer has already mobilized troops to attack Colombia, the troops are moving. THERE IS NOTHING YOU CAN DO! HEIL HITLER!!"
        show gen_2 at left with easeinleft
        gen_2 " He won't speak anymore..What should we do with him? "

        menu:
            "1.Kill him , he is a liability":
                pause 1


            "2.Imprison him for life":
                pause 1









    return


#SCENARIO CHOICES!!!!!

    label help_1_no:
        gen_1 "Wise choice commander!"
        pause 1


        define farright = Position(xpos=0.85)
        show gen_1 at farright with move
        gen_1 " On my way to convey the new orders!!"

        scene black with dissolve
        pause 1
        scene help_1 with dissolve
        pause 1
        "British troops kept on standby , Poland is fighting German forces with France"
        "Weeks pass by.. German forces overwhelm the Allies. Troops are retreating. We have LOST CONTROL OF WARSAW!!"


        scene battle with dissolve
        pause 1
        show sol_1 at left with dissolve
        pause 1

        sol_1 " Chief! The battle is not looking good, Polish forces have been crippled , Warsaw is under GERMAN SEIGE!"
        sol_1 " Hundreds dead... More injured."
        sol_1 " Helping casualties wont be easy. Will burn resources and time. But I need official orders SIR!"
        pause 1

        menu:
         "Help ALLY TROOP casualties , risk losing British lives":

             scene black with dissolve
             pause 1
             show text"{size=+30}  ALLY troops have been rescued from battlefield.. We lost few of our men{/size}" with dissolve
             pause 1.5


         "Save resources , dont get involved":

            scene black with dissolve
            pause 1
            show text"{size=+30} Poland has been greatly reduced in strength...Ally forces are weakened{/size}" with dissolve
            pause 1.5



        jump part_2









    label help_1_yes:
        gen_1 "Wise choice commander!"
        pause 1
        $help+=1
        $loyal+=1

        define farright = Position(xpos=0.85)
        show gen_1 at farright with move
        gen_1 " On my way to convey the new orders!!"

        scene black with dissolve
        pause 1
        scene help_1 with dissolve
        pause 1
        "Soldiers have been dispatched to Poland , war ensues against German forces..."
        "Weeks pass by.. German forces overwhelm the Allies. Troops are retreating"

        scene battle with dissolve
        pause 1
        show sol_1 at left with dissolve
        pause 1

        sol_1 " Chief! The battle is not looking good, we have to regroup and retaliate after further planning"
        sol_1 " Hundreds dead... More injured."
        sol_1 " Taking casualties back home wont be easy. Will burn resources and time. But I need official orders SIR!"
        pause 1

        menu:
         "Carry casualties back to Britain, risk losing more lives":
             pause 1
             scene black with dissolve
             pause 1
             show text"{size=+30}  ALLY troops have been rescued from battlefield.. We lost more men{/size}" with dissolve
             pause 2



         "Retreat immediately, leave injured behind":
             pause 1
             scene black with dissolve
             pause 1
             show text"{size=+30} ALLY forces have been greatly reduced in strength...{/size}" with dissolve
             pause 2



        jump part_2





    return
