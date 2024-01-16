import pygame
import os

WIDTH, HEIGHT = 1600, 900  # <-- change this to your screen resolution

# load images
BLACK_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "black.jpg")), (WIDTH, HEIGHT))
COUNCIL_ROOM_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "council_room.jpg")),
                                         (WIDTH, HEIGHT))
COUNCIL_ROOM_BG_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "council_room_1.jpg")),
                                         (WIDTH, HEIGHT))
BATTLEFIELD_1_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "battlefield.jpg")),
                                          (WIDTH, HEIGHT))
BATTLEFIELD_2_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "battlefield_2.jpg")),
                                          (WIDTH, HEIGHT))
BATTLEFIELD_3_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "battlefield3.jpg")),
                                          (WIDTH, HEIGHT))
GERMAN_ROOM_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "german_room.jpg")),
                                        (WIDTH, HEIGHT))
WARPLAN_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "warplan.jpg")),
                                    (WIDTH, HEIGHT))
PRISON_1_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "prison_1.jpg")),
                                     (WIDTH, HEIGHT))
PRISON_2_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "prison_2.jpg")),
                                     (WIDTH, HEIGHT))
PLANE_CRASH_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "plane_crash.jpg")),
                                     (WIDTH, HEIGHT))
STALINGARD_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "stalingrad.jpg")),
                                     (WIDTH, HEIGHT))
USSR_BG_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "russia_room_3.jpg")),
                                     (WIDTH, HEIGHT))
USSR_BG_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "russia_room_2.jpg")),
                                     (WIDTH, HEIGHT))
PHARMACY_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "pharmacy_room.jpg")),
                                     (WIDTH, HEIGHT))
BATTLEFIELD_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "battlefield_1.jpg")),
                                     (WIDTH, HEIGHT))
FRENCH_ROOM_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "french_room.jpg")),
                                     (WIDTH, HEIGHT))
FRANCE_1= pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "france_17_20.jpg")),
                                     (WIDTH, HEIGHT))
FRANCE_2= pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "france_18.jpg")),
                                     (WIDTH, HEIGHT))
USA_1= pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "USA_1.jpg")),
                                     (WIDTH, HEIGHT))
USA_2= pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "USA_23.jpg")),
                                     (WIDTH, HEIGHT))
USA_3= pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "USA_24.jpg")),
                                     (WIDTH, HEIGHT))
ENDING_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "end.jpg")),
                                     (WIDTH-100, HEIGHT))
RESULTS_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "results.png")),
                                     (WIDTH, HEIGHT))

class Dialogue:
    def __init__(self, text, background=BLACK_BG, options=None, number=None):
        if options is None:
            options = []
        self.text = text
        self.background = background
        self.options = options
        self.chosen = -1
        self.number=number


# script
part_1 = [
    Dialogue("B.A.S.S presents "),
    Dialogue("1 September,1939, Britain..."),
    Dialogue("Germany has invaded Poland. Poland, France and us had already signed a treaty of mutual assistance which calls for an immediate retaliation.",
             COUNCIL_ROOM_BG_1),
    Dialogue("But going against the vast German army may start a world war. What to do now?",
             COUNCIL_ROOM_BG, ["Declare War on Germany and stop German aggression 1",
                               "Stay Neutral 1"]),
    Dialogue("Wise choice commander! ", COUNCIL_ROOM_BG_1),
]

part_1_question_1_option_1 = [
    Dialogue("Soldiers have been dispatched to Poland , war ensues against German forces...", BATTLEFIELD_2_BG),
    Dialogue("Chief! The battle is not looking good, we have to regroup and retaliate after further planning ",
             BATTLEFIELD_1_BG),
    Dialogue(
        'Taking casualties back home wont be easy. Will burn resources and time. But I need official orders "Sir!"',
        BATTLEFIELD_1_BG, ["Carry casualties back to Britain, risk losing more lives2",
                           "Leave them behind2"]),
    
]

part_1_question_1_option_2 = [
    Dialogue("British troops kept on standby , Poland is fighting German forces with France", BATTLEFIELD_1_BG),
    Dialogue("Weeks pass by.. German forces overwhelm the Allies. Troops are retreating", BATTLEFIELD_1_BG),
    Dialogue("Helping casualties wont be easy. Will burn resources and time. But I need official orders SIR!",
             BATTLEFIELD_1_BG, ["Carry casualties back to Britain, risk losing more lives2",
                                "Leave them behind2"]),
]

part_2 = [
    Dialogue("You are a soldier in the British army during World War 2, and you discover that one of your fellow soldiers is planning to desert", BATTLEFIELD_BG),
    Dialogue(
        'What do you do? ',
        BATTLEFIELD_BG, ["Report the soldier to your superior officer3",
                           " Keep quiet and let the soldier go3",
                           "Convince the soldier to stay and fight3"]),

    Dialogue("Meanwhile IN GERMANY...", GERMAN_ROOM_BG),
    # Dialogue("You are a commander during the Poland Campaign and have been given contradictory information about the movements of British and French armies", GERMAN_ROOM_BG),
    # Dialogue(
    #     'Do you? ',
    #     BATTLEFIELD_1_BG, ["Trust your intelligence sources and launch an attack4",
    #                        "Hold back and wait for further information, even though it may give the enemy an advantage4",
    #                        "Convince the soldier to stay and fight4"]),

    Dialogue("Führer, France and Britain have retaliated against our attack in Poland. An attack from the north will counter France's attacks and guarantee an early defeat…", WARPLAN_BG),
    Dialogue("But that requires an access through Belgium borders, who have remained neutral in this war so far", WARPLAN_BG, ["Find another solution2", "INVADE BELGIUM2"]),
    Dialogue("Just what I was thinking. Troops will be mobilized right away.", WARPLAN_BG),

    Dialogue("You are a pilot during the Battle of Britain and your plane has been hit", PLANE_CRASH_BG),
    Dialogue("Do you eject and risk being captured by the enemy or try to make a crash landing on friendly territory?", PLANE_CRASH_BG, ["Eject immediately to ensure your own safety4",
                                                                "Attempt a crash landing to preserve the plane and aid in the war effort4", "Stay with the plane and continue to fight, even though it may cost you your life4"]),
    
    # Dialogue("Few days pass by..."),
    # Dialogue("Führer! Our troops have overrun their defense. It is a VICTORY FOR GERMANY today!", GERMAN_ROOM_BG),
    # Dialogue("Also our soldiers have been able to capture some of the enemies alive , what should we do with them?",
    #          GERMAN_ROOM_BG,
    #          ["Send to Auschwitz labour camp2", "Send to Gas Chambers2"]),
    # Dialogue("", PRISON_2_BG),
    
    Dialogue("Meanwhile in the Soviet Union",USSR_BG_2),
    # Dialogue("Hitler has broken the treaty of peace and has declared war. Our armies were not prepared and the Germans have made sufficient progress.",COUNCIL_ROOM_BG),
    # Dialogue("We can sit down with Hitler for immediate cessation or can accept assistance from Allied powers of capitalist origin.",COUNCIL_ROOM_BG),
    # Dialogue("What should be our next step Mr. President.",
    #          COUNCIL_ROOM_BG, ["Try to reach an agreement for immediate cessation of hostility5",
    #                            "Take sides with the United States and join the Allied Powers5"]),
    
    Dialogue("Hitler has officially declared operation Barbarossa", USSR_BG_1),
    Dialogue("The German army's offense was unexpected and not something we were prepared for… They have acquired considerable land and are moving towards the capital", USSR_BG_1),
    Dialogue("Our intelligence report says that the German army is not prepared for the Soviet Winters and we can use that to our advantage. Although a defensive approach means a massive loss of manpower and innocent lives", USSR_BG_1),
    Dialogue("What should our counter response be?",
             USSR_BG_1, ["Defend the capital, and wait for the Winters5",
                               "Launch an immediate all out offense5"]),
    
    Dialogue("The city of Leningrad has been surrounded by the German Forces cutting off supply with the soviet main-land as well as the relief forces", STALINGARD_BG),
    Dialogue("As the local government, we can either wait for the central government support but that may be months away and may lead to disaster within the city or evacuate civilians out of the city but that would mean risking volunteer and civilian lives", STALINGARD_BG),
    Dialogue("What would your next step be?",
             STALINGARD_BG, ["You can either evacuate them to some safe place for their betterment4",
                               "Hold on till backing from the government4"]),
    
    Dialogue("You are a pharmacist in Leningrad, it is captured by German Forces and there's a shortage of day-to-day commodities", PHARMACY_BG),
    Dialogue("You have access to a limited supply of medicine. The medicine could be sold on the black market for a large profit.", PHARMACY_BG),
    Dialogue("What do you do?",
             PHARMACY_BG, ["Sell the medicine on the black market to benefit yourself and your family3",
                               "Distribute the medicine to those in need, even if it means sacrificing potential profit3"]),
    
    # Dialogue("During the Battle of Stalingrad, your unit is low on supplies and ammunition.", BATTLEFIELD_1_BG),
    # Dialogue("Do you?",
    #          BATTLEFIELD_2_BG, ["Sacrifice your own safety to bring back supplies for your fellow soldiers1",
    #                            "Prioritize your own survival1"]),
    
    Dialogue("Normandy Landings, June 6th, 1944 ...",FRENCH_ROOM_BG),
    Dialogue("As a commander of French troops during the D-Day invasion, you are faced with unfavorable weather conditions that could jeopardize the success of the mission", FRENCH_ROOM_BG),
    Dialogue("What do you do? ",
             FRENCH_ROOM_BG, ["Delay the invasion until weather conditions improve5",
                               "Launch the invasion as planned and hope for the best5",
                               "Modify the invasion plan to take advantage of the weather conditions5"]),
    # Dialogue("You are a member of the French Resistance and have just been captured by the Nazis", BATTLEFIELD_1_BG),
    # Dialogue("What do you do? ",
    #          BATTLEFIELD_2_BG, ["Refuse to give any information and face the consequences3",
    #                            "Hand over information in exchange for better treatment3"]),
    Dialogue("You are in charge of a unit of soldiers during the D-Day invasion", FRANCE_1),
    Dialogue("Do you?",
             FRANCE_1, ["lead from the front and risk your own life alongside your troops5",
                               "Remain in the rear and direct from a safe distance5"]),
    Dialogue("You are part of a group of soldiers who discover a group of Jewish refugees hiding from the Nazis", FRANCE_2),
    Dialogue("Do you?",
             FRANCE_2, ["Risk your own safety to help them escape1",
                               "Ignore and continue on your mission1"]),
    Dialogue("Meanwhile in America",USA_1),
    Dialogue("Recent German attacks on Colombie has led to a loss of a significant amount of their troops in their arsenal", USA_1),
    Dialogue("Colombia has been an exporter of Petroleum products to the Allied power. But helping Colombia at this stage will lead to a significant reduction of our forces in the warfronts of the UK, Japan, Australia, Argentina, France etc.", USA_1),
    Dialogue("Should we help them? But it would also mean a reduction in our troop forces",
             USA_1, ["They are a part of our coalition, send troops immediately4",
                               "We need the troops for our own expeditions4"]),
    Dialogue("You are an American soldier during World War II. You witness your fellow soldier commit a war crime against innocent civilians.", USA_2),
    #Dialogue("Colombia has been an exporter of Petroleum products to the Allied power. But helping Colombia at this stage will lead to a significant reduction of our forces in the warfronts of the UK, Japan, Australia, Argentina, France etc.", BATTLEFIELD_1_BG),
    Dialogue("Do you report the war crime and risk being punished, keep quiet and protect your own safety, or participate in the war crime and follow orders?",
             USA_2, ["Report the war crime and risk being punished3",
                               "Keep quiet and protect your own safety3",
                               "Participate in war crime and follow orders3"]),
    #Dialogue("Recent German attacks on Colombie has led to a loss of a significant amount of their troops in their arsenal", BATTLEFIELD_1_BG),
    Dialogue("You are a member of the American Red Cross and have been sent to Europe to provide aid to soldiers during the war. You come across a wounded German soldier", USA_3),
    Dialogue("What will you do?",
             USA_3, ["Provide aid to the German soldier, regardless of their nationality1",
                               "Deny aid to the German soldier due to their nationality1"]),
    Dialogue("You are a member of the US military and have just learned that a new weapon, the atomic bomb, is going to be dropped on Hiroshima.", BATTLEFIELD_1_BG),
    Dialogue("What do you do?",
             BATTLEFIELD_1_BG, ["Support the decision to drop the bomb and follow orders2",
                               "Oppose the decision to drop the bomb and refuse to participate in the attack2"]),
    Dialogue("The War has come to an end, and the world has changed forever",ENDING_BG),
    Dialogue("")
    
    

]
