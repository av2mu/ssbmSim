# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#invites
define mango = Character("Mango")
define amsa = Character("Amsa")
define wizz = Character("Wizzrobe")
define plup = Character("Plup")
define leff = Character("Leffen")
define axe = Character("Axe")
define hbox = Character("Hungrybox")

#commentators
define hugs = Character("Hugs")
define lovage = Character("Lovage")
define scar = Character("Scar")
define webs = Character("Webs")
define vish = Character("Vish")
define toph = Character("Toph")

#narrator
define narr = Character("Narrator")

#other random characters
define FDA = Character("Front Desk Agent")
# The game starts here.

label start:
    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0
    transform xflip:
     xzoom -1



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg fd:
        zoom 0.8

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    define pov = Character("[povname]")

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

    #Hotel Room
    narr "After a long flight and heavy traffic through LA, you finally arrive at the hotel you'll be staying at for the weekend."
    pov ".........."
    narr "You are a new face in the Melee community, and after dropping $1000 dollars in the BTS compendium store, you were invited as a VIP to Smash Summit 9."
    narr "The Summit is a chance for you to meet some people from the community, get a close look at the players, and maybe - just maybe - find love."
    pov "*sighs* (Finally, I've made it to LA... It was a grueling trip to make it here, but I'm sure it'll all be worth it!)"
    narr "You unpack rather quickly, and are left with a whole evening to yourself."
    narr "You decide to head to the hotel lobby to see how you might want to spend the rest of the evening"

    #Reception/Lobby area
    narr "You take the elevator down to the main floor and head to the lobby. As you approach the front desk, you see a familiar figure... Oh my god, it's Plup! Your heart instanly starts racing, but you muster up the courage and decide to walk over."
    pov "Excuse me..... Plup?"

    show plup happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    plup "Huh?... Oh hello."

    pov "(Oh god what do I say)"
    narr "You take too long to say anything, so Plup grabs his backpack and luggage."
    
    show plup happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    plup "I just landed and I'm super tired, uh, nice to meet you."

    narr "He walks away from the front desk, heading towards the elevator and your heart sinks into the pit of your stomach."
    FDA "Sir? Oh no, sire, you forgot your phone!"
    narr "The woman at the front desks waves to try and get Plup's attention, but fails."
    FDA "Hey do you know him? Could you run after him and give him back his phone? I have some other customers to help."
    pov "*sure* Oh yeah sure, I can give it to him"
    narr "You grab the phone and race towards the elevator doors. You see Plup pressing the elevator button, but just as you run up to him, he turns around suddenly and you crash into him."

    show plup happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    plup "Ah what the hell!"

    pov "Oh my god, I'm so sorry! You.. You forgot your phone at the front desk."
    narr "Plup's annoyance turns to relief, You hand him his phone"

    show plup happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    plup "*laughs* Oh shit, thanks, I nearly panicked because I didn't know where it was... Who were you again?"

    pov "(Don't fuck it up this time)"
    pov "I'm one of the VIP guests for Smash Summit. My name's [povname]."

    show plup happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    plup "Sick, nice to meet you. I gotta get going, but I'll see you tommorow for that VIP event thingy?"

    pov "Totally, see ya."
    narr "Plup gets into the elevator and gives you an awkward smile. You just stand there, dumbfounded, as the door closes."

    hide plup

    pov "(Now what do I do?)"
    narr "You look around the large lobby, see a neon sign for the hotel bar, and decide to check it out."

    #BAR

    narr "You step into the rather luxurious looking hotel bar, and awkwardly take a seat, gesturing to the barman that you'd like to order something."
    narr "Taking a sip of your beer, you scan the room, and before long your eyes lock on a particular pair, having an argument in the corner."

    show mango happy at bounce:
        xpos 10 ypos 0


    show leff happy at bounce, xflip:
        xpos 10 ypos 0

    leff "Mango, you DO NOT know what your're talking about!"
    leff "How could you even THINK Marth-Fox is anything besides 60-40! Let's be real, Marth is just a Spacie counterpick."

    show mango happy at bounce:
        xpos 10 ypos 160
    mango "Hey, wooooaaaah! Chill out, Leff... if that even is your real name!"

    narr "You can tell by the way the conversation is going they've been drinking quite a bit and have been at this for a while."
    narr "Always having wanted to meet them, though, you awkwardly made your way to their table, giving it your best efforts not to bump into other patrons of the bar."
    narr "Finally, having made it all the way to the corner of the bar, you see both players turn to you, awaying some kind of introduction."
    pov "Uh... hey guys. My name's [povname], I'm a VIP invite for the Summit tommorow. Nice to meet you two, I'm a big fan!"

    show leff happy at bounce, xflip:
        xpos 10 ypos 0

    leff "Oh... hey."

    show mango happy at bounce:
        xpos 10 ypos 160
    mango "Wasshup dawg!"

    narr "You smile at both players, and before you can add anything else, their conversation continues."

    show leff happy at bounce:
        xpos -1000 ypos 75

    leff "...So anyway, Marth is bullshit."

    narr "Mango roared with laughter"

    show mango happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    mango "Well, we can both agree that Zain is a dash-dancing little bitch, eh, Leff?"

    show leff happy at bounce:
        xpos -1000 ypos 75

    leff "... I'll cheers to that."

    narr "As the two players finish their drinks, you decide it'd be awkward to hang around any longer, so you pay tour tab and leave, heading back to the lobby."
    hide leff
    hide mango
    #----ROOF------
    narr "Now, where to next..."
    narr "You figure after a good beer there's nothing like some fresh air, so you decide to head to the hotel rooftop."
    narr "You make your way to the highest floor and gently open the heavy door leading to the roof"
    narr "..."
    narr "The view is amazing, and the crisp LA air fills your lungs."
    narr "Ouch."
    narr "As you cough, you suddenly notice a long haired gentleman taring out over the city skyline."
    narr "Not having noticed him before, you're caught aback, and decide to make contact."
    pov "...H...Hello"

    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "......."

    pov "Um... hello? Sir?"
    narr "Wizzrobe turns around and stares at you, his gaze visibly aloof."
    
    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "...Oh. Can I help you?"

    pov "Oh! Um, hi! You're... Wizzrobe, right?"

    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "..........."
    pov ".........."
    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "........."
    pov "........?"

    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "...Yeah. I am."

    pov "..Oh."
    pov "Well. I'm gonna be at Summit this weekend as one of the VIPs. Thought I'd introduce myself."
    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "....."
    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "...Cool...?"
    narr "Before you can actually give the player your name, Wizzrobe turns back around to look out over the city. You can fainly hear him mutter something to himself"
    show wizz happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    wizz "Even the smallest mouse can change the course of history."
    narr "..."
    narr "You decide to head back in and leave Wizzrobe to his contemplation"

    #------------GRIND ROOM----------------
    narr "On the way back from the root you hear the familiar sound of clicking and the faint hum of a CRT as you walk down the hotel hallway."
    narr "Out of curiousity you follow the sounds to a room, finding the dorr is slightly ajar."
    narr "You peek in and see a Melee setup where Zain, Amsa, and Axe are in a 3 man rotation playing friendlies."
    narr "You light up, excited to meet even more top players!"
    pov "Hey guys!"
    narr "Almost frightened, Zain and Axe turn your way and look at you with some confusion, while Amsa only gives you a quick glance and immediately goes back to playing."
    narr "Finally, having assessed what- or rather, who- he's seeing, Axe gives you a warm welcome."

    show axe happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    axe "Hey, man! What are you do--"

    show zain happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    zain "AXE, watch it!"
    narr "The Pikachu main turns back around just to see Amso has taken his last stock and won the game while he was busy greeting you."
    show amsa happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    amsa "かったー！٩(ˊᗜˋ*)و✧*｡"

    show axe happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    axe "What?! Dude, not fair!"

    show zain happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    zain "That was game 5 of the set, too!"

    narr "You can feel your heart sink deep in your chest."
    pov "...S-Sorry, didn't mean to interrupt."
    pov "I just thought I'd introduce myself. I-I'm [povname], one of the Smash Summit VIPs."

    show axe happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    axe "Oh dude, no problem! It's nice to meet you!"

    show amsa happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    amsa "こんばんわ！はじめました. ( ´ ▽ ` )ﾉ"

    show zain happy at boucne:
        xpos 10 ypos 160
        zoom 0.5
    zain "Cool. Zain, pleasure to meet you."

    narr "You sit down with the three players and, after asking if it's fine with them, decide to spectate the next match."
    narr "You maintain a pleasant small talk, not wanting to be the fourth wheel, before Axe looks down at his phone and gasps"

    show axe happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    axe "Oh dang, guys, look at the time! We should probably get some sleep for Summit tommorow."

    show zain happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    zain "*sighs* Truuue. GGs, Amsa."

    show amsa happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    amsa "どうも.じゃあまたね! (´・ω・)ﾉ"

    pov "Yeah, I guess I'll see you guys tommorow!"

    show axe happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    axe "Bye, [povname]!"

    show zain happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    zain "Yeah, see you around."

    narr "You head back towards your room smiling, satisfied that you've already gotten to hang out with so many Smash legends."

    #-------------------------PENTHOUSE--------------------------------
    narr "As you turn the corner though, you see a number of people pour out of one of the rooms."
    narr "It peaked your interest, so you decide to stop by before seeing Hungrybox step out of that very same room."
    narr "You saw him bid the people goodbye, turn, and... oh gosh, he's heading your way!"
    pov "Hey... You're Hungrybox"

    show hbox happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    hbox "In the flesh."

    narr "He gies you a big, warm smile and stops to stand across from you, waiting for you to say or do something. You feel nervous in his presence."
    pov "I-I'm [povname], I'm going to be at Summit tommorow... I'm, uh, I'm a VIP."
    show hbox happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    hbox "Oh yeah, cool. So, you play Melee at all?"
    pov "I go to locals-- I mean... I'm not amazing or anything, but... yeah"
    narr "HungryBox shifts his weight and puts his hands in his pockets. You're unsure if he's interested in talking or if he desperately wants to leave."
    pov "You.. uh, excited for Summit?"
    narr "You feel like a moron for asking such a basic question. HungryBox chuckles."
    show hbox happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    hbox "It's one of my favorite events. I'm gonna win it this time, though!"
    narr "He gives you a little charming wink."
    show hbox happy at bounce:
        xpos 10 ypos 160
        zoom 0.5
    hbox "I gotta head to my room and catch some sleep. See you tommorow?"
    pov "Of course!!"
    narr "You're worried yo say it a little to enthusiastically, but HungryBox smiles warmly, giving you a little wave goodbye, and then walks down the hall."
    #---------------------------------------------------------------------
    show mango happy:
        xpos 10 ypos 160
        zoom 0.5
    mango "what's up"


    show mango angry at bounce:
        xpos 10 ypos 160
        zoom 0.5
    mango "ay woah"



    # These display lines of dialogue.

    hide mango

    show wizz sweat at bounce:
        xpos -50 ypos 160
        zoom 0.5
    wizz "ok"

    # This ends the game.

    return
