label Slime:
    play music nina1 fadein 1
    "You and Nina begin your journey to the well."
    hide window
    scene village day 1 with dissolve
    w ""
    show nina neutral at center
    mc "Sorry about that stuff with dad."
    nin neutral "I know how he gets. I think he's just concerned you're becoming a late bloomer."
    nin "He wants to see you happy."
    mc "Yeah, everyone can get a date but me, it seems."
    nin "Well, maybe if you got out there more."
    mc "Come on! I'm not exactly popular around here. Word gets around."
    nin "Hey, come on! I wasn't popular either, and look at me... who would have thought I'd..."
    mc "Date the most popular guy in the village? This is gonna sound bad... but it's different for girls."
    mc "Guys are always all over you. It's easy."
    nin angry "Wow. You just love talking crap, don't you?."
    nin "Come on... let's just do this already."
    hide window
    scene village day 2 with dissolve
    play ambient town fadeout 1
    w ""
    nvl clear
    n "You don't have a response to that, and Nina doesn't push the issue."
    n "The two of you continue walking through the village. Everyone is starting their day."
    n "A group of miners whistle at some of the village girls as they walk to their daily grind."
    n "The same girls, seemingly annoyed at first, giggle at each other once the miners are out of sight."
    hide window
    nvl clear
    scene market with dissolve
    n "As you walk through the village's open air market, shop owners wave to you as they begin to set up for the morning rush."
    n "Your father often sells his goods at this very market, often dragging you and [Nova] to assist him. With the new harvest just weeks away, you aren't looking forward to doing it again."
    n "You still haven't responded to Nina, and the silence is getting to you. Finally, as you reach the bridge leading to the well, she speaks."
    stop ambient
    nvl clear
    scene well day with dissolve
    play sound bridge
    show nina crossing
    nin "They really need to fix this thing, it's getting more rickety every day."
    mc "It's fine. Just be careful in the middle, that's where the wood is the weakest."
    "You and Nina carefully cross the bridge. You take her by the hand to help her keep her balance."
    show nina neutral
    mc "You know, I was right before. Girls have it way easier. I'd be laughed out of town if some dude took my hand to help me cross the bridge."
    nin "Are you still on this? I think you're just jealous I found someone and you're looking for an excuse."
    mc "Jealous? Of Trevor? No way!"
    mc "I almost feel bad for the guy."
    nin moreangry "When I beat you up and throw you down the well, the village council will call it justified."
    play sound chicken
    "You're about to respond when you hear the sound of panicked clucking."
    mc "Is that?"
    hide nina
    nvl clear
    "You and Nina rush toward the source of the sound."
    show chicken:
        xalign 0.5 yalign 1.00
    play sound chicken
    "You see one of your chickens is being attacked by a slime!"
    hide chicken
    show nina worried
    nin worried "A slime? What's it doing this close to the village?"
    mc "I don't know... but it's definitely going after that chicken!"
    nin "I'll go get the guys!"
    mc "No! I've got this."
    nin neutral "You've got this? Are you crazy? You don't even have a weapon."
    mc "Sure I do!"
    play music battle1 fadeout 1
    "You pull out a knife."
    play sound slash
    mc "Slimes are slow and easy to kill. I'll be fine."
    nin angry "Look, just let me get someone! You can barely cut yourself with that thing."
    mc "By then it'll have killed the chicken."
    nin "Better the chicken than you."
    mc "Do you really think I'm that weak?"
    nin neutral "It's not about being weak... it's about..."
    nin "This isn't you. You're not a fighter."
    mc "Watch me."
    scene slime fight with dissolve:
        crop (0,0,667,375)
        size (1280,720)
        easein 0.3 crop (0, 0, 1280, 720)
    "You grip the hilt of your knife tightly and slowly advance toward the creature."
    "Its blue mass undulates before you, leaving part of itself behind as it advances. Slimes are barely considered a threat to anything other than livestock, and you are clearly smarter and more capable than that."
    "You slash at the slime with your knife. You think of the dream you had, and know that your foe must fall."
    play sound slash
    scene slime fight with vpunch:
        crop (0,0,1280,720)
        size (1280,720)
        crop (0, 0, 667, 375)
    play sound slime
    scene slime fight with flashbulb
    "The slime undulates out of the way and moves quicker than you expected."
    play sound slash
    "You slash again, and suddenly the slime is by your side!"
    scene slime fight with vpunch
    scene slime fight with flashbulb
    "It creates a small tentacle with its body and hits your arm."
    play sound hit
    scene slime fight with vpunch
    scene slime fight with flashbulb
    scene well day with vpunch:
    play sound acid
    mc "AAAAH!"
    "You feel your skin burn where the tendril has touched you. The pain causes you to reflexively drop the knife."
    play sound weapondrop
    show nina worried
    nin worried "I told you! Just get away!"
    mc "I..."
    play sound slime
    hide nina
    nvl clear
    n "The slime moves towards Nina, and you get in its way."
    n "It turns and starts chasing you, much faster than you thought possible."
    mc "{color=#b7b7b7}{i}Damn it. Where did my knife go?{/i}{/color}"
    n "You look for something, anything you can use to fight back. The creature, one you were so willing to pass off as weak, now seems quite dangerous."
    n "You continue running away as fast as you can, but the creature keeps up with you, and almost seems to be gaining ground."
    play sound stabby
    show well day with vpunch
    show well day with flashbulb
    n "The slime is about to strike you when you see a long sword pierce its center."
    n "It loses all cohesion and sinks into the ground."
    stop music
    show nina neutral
    nin "Oh thank the Maker!"
    play music trevor
    scene trevor intro with dissolve:
        crop (314,360,1280,720)
        size (1280,720)
        linear 1.0 crop (314, 0, 1280, 720)
        linear 1.0 crop (0,0,1920,1080)
    "You look up and see a tall, good looking (if you're into that) man sheathing his sword."
    "It's Trevor, Nina's boyfriend, leader of the town miltia, and all around most popular bachelor in the village."
    "While you have struggled socially and martially, Trevor never did. Quite the opposite, in fact. You aren't friends, but ever since he started dating Nina, he's been trying to hang out with you more."
    "Something you actively try to avoid."
    tre "You two ok?"
    nin "Yeah... thanks."
    tre "What about you, [MC]?"

menu TrevorReaction:
    "I'm good, thanks [gr]\[TrevorFriend +1\]":
        mc "Yeah. You saved my ass. Thanks."
        mc "{color=#b7b7b7}{i}Damn it. I look like a fucking weakling again.{/i}{/color}"
        $ TrevorFriend += 1
        jump Slime2
    "I had it handled [red]\[TrevorFriend -1\]":

        mc "I didn't need your help."
        mc "I was just biding my time."
        tre "Sure you were, buddy. Whatever you say."
        mc "{color=#b7b7b7}{i}Yeah... That made me look awesome.{/i}{/color}"
        $ TrevorFriend -= 1
        jump Slime2

label Slime2:
    scene well day with dissolve
    "Trevor walks over to Nina and embraces her. She hesitates before returning the hug."
    show trevor neutral at slightright
    show nina neutral at right
    nin "Thanks, Trevor."
    show trevor neutral at farright
    "Trevor moves in to kiss Nina, but she pushes him away."
    show nina worried at right
    show trevor annoyed at slightleft
    nin worried "I... You know I don't... Not in public."
    tre "Yeah, yeah."
    "Trevor pulls away, disappointed."
    show nina neutral at slightright
    tre neutral "So what happened here?"
    tre "You should have called me."
    nin neutral "Well, it just attacked. [MC] was trying to protect..."
    tre "Wow, really?"
    tre "Thanks [MC]. I mean, you still got your butt kicked, but good on you."
    if TrevorFriend == 0:
        mc "{color=#b7b7b7}{i}Is he trying to be an ass, or does it just come naturally to him?{/i}{/color}"
    else:
        mc "Yeah. Uh... Thanks."
    mc "{color=#b7b7b7}{i}Why is Nina covering for me?{/i}{/color}"
    tre "I'm just glad I could save my girl and her best friend."
    tre "But seriously, attacking with a knife?"
    tre "You suicidal?"
    mc "What?"
    tre "If the slime didn't get you... the splash would have burned you anyway."
    mc "I just thought it would be slow and easy to kill."
    tre "Well first, that's a baby, they don't do as much damage but they're a lot faster."
    tre "Second, you're not trained at all. Leave it to the professionals."
    mc "{color=#b7b7b7}{i}Professionals? Hah, they're barely official.{/i}{/color}"
    "Nina notices that you're about to say something snarky."
    nin "So! How about we finish getting that water?"
    mc "Nah, I'm fine. Your boyfriend's here... you two go. Have some fun."
    nin "Come on! You'll need some help with that burn."
    mc "I'm fine. Trust me. Go."
    tre "You heard the man, Nina. Let's go to the lake."
    "Nina looks concerned."
    nin "You sure?"
    mc "Yeah. I'm fine."
    nin "Ok, then."
    hide trevor with moveoutleft
    show nina smiling at center
    nin "Take care, ok?"
    "The pair leaves."
    hide nina with moveoutleft
    play music afternoon
    mc "{color=#b7b7b7}{i}Ow... this really hurts. But I'm not going to let it show in front of them.{/i}{/color}"
    mc "{color=#b7b7b7}{i}God damn it! A slime is like one step up from killing a rat. How can I be so weak?{/i}{/color}"
    mc "{color=#b7b7b7}{i}Guess that dream was full of it.{/i}{/color}"
    mc "{color=#b7b7b7}{i}I'm here... In pain... Alone. While my best friend goes off with her boyfriend. Probably getting ready to fuck like goblins.{/i}{/color}"
    "You search the area and eventually find your knife, but the chicken is gone."
    mc "{color=#b7b7b7}{i}So, great start to the day.{/i}{/color}"
    mc "Might as well get the water."
    "It takes you some time because of your burnt arm, but you attach the bucket to the well and lower it."
    "You pull the bucket back out and pick it up."
    mc "OW!"
    "You instinctively try to grab it and are overwhelmed with pain. The bucket clatters to the ground, spilling water all over your pants and shoes."
    mc "Yeah. Day just keeps getting better."
    show nova smirk
    stop music fadeout 1
    nov "You know you're supposed to bring the water back home... not spill it everywhere."
    play music nova2 fadeout 1
    mc "Just... Not today, [Nova]. Please."
    nov neutral "What happened to you?"
    mc "Got into a fight with a slime. It's dead now."
    nov "You killed it?"
    mc "Not so much."
    "You tell her the story."
    nov "Ouch. That is pathetic."
    mc "Thanks."
    nov "Hey... It happens. But seriously, what were you thinking?"
    mc "I don't know. I just..."
    nov "Don't tell me you were trying to impress Nina?"
    mc "Not you too..."
    nov "Look, there are easier girls to go after."
    mc "I'm not going after her!"
    nov "Uh huh. Look, I'm just saying... she might be your friend, but she's a total cock tease. You can tell Trevor's about to explode. Poor guy."
    mc "And you can tell this how?"
    nov smirk 2 "A girl knows..."
    mc "Sure she does."
    nov "Never doubt me."
    mc "Whatever. Look, I need to get this water home."
    nov neutral "What, with a fucked up arm? No way. I'll do it."
    mc "What?"
    nov "Your arm looks awful. Just let me carry this home."
    mc "I..."
    show mc neutral at left
    show nova neutral at right

menu WellChoice:
    "Let her do it":
        hide mc
        show nova neutral at center
        mc "Fine. Thanks."
        nov "Don't thank me too much. You're doing the dishes tonight."
        mc "You've got to be kidding me."
        nov "I never kid."
        "[Nova] takes the bucket."
        mc "At least let me help."
        "You grab the bucket with your good hand, and the two of you carry it home together."
        jump NovaBackHome
    "Protest [gr]\[NovaLove +1\]":

        hide mc
        show nova neutral at center
        mc "I'm the guy. I should do it."
        nov smirk "Well, guy. I already do more work than you around the house. So why should it change now?"
        mc "I can do it."
        nov "Fine. How about this, you grab it with your left hand, and we'll carry it together."
        nov "Deal?"
        mc "..."
        mc "Ok. Thanks."
        $ NovaLove += 1
        "You and [Nova] take the bucket back home together."
        jump NovaBackHome

label NovaBackHome:
    scene farm bedroom with dissolve
    "You return back home with [Nova] and she immediately takes you to your room."
    show nova neutral
    nov "Now wait there, I'm going to get something for that burn."
    mc "I said I'm ok. I'm already feeling better."
    nov smirk "[MC], we can argue about this, you can get all worked up, it can take a while, and you lose. Or we can save time and you can sit your happy ass down and wait for me."
    mc "I got it. I'll wait."
    nov "Good."
    "[Nova] leaves you sitting on your bed for a few minutes before returning with the ointment."
    nov "Got it!"
    mc "Ok, let's get this over with... I still have chickens to find."
    hide window
    scene nova ointment with dissolve
    w ""
    "[Nova] leans into you and takes your hand. You can feel her tits pressed up against you as she applies the ointment."
    mc "{color=#b7b7b7}{i}Man... is she doing that on purpose? I swear it's like she WANTS to see me squirm.{/i}{/color}"
    nov "There you go. You're all clear to resume your glorious quest."
    nov "But don't go choking you own chicken with this hand for at least a day or two. It'll still be tender."
    mc "Did you have to go there?"
    scene farm bedroom with dissolve
    "[Nova] stands up."
    show nova smirk 2
    nov "Come on, horndog. I know all about your magazines."
    mc "What? How?"
    nov smirk "I clean your damn room, [MC]. You don't hide them that well."
    mc "Oy."
    nov "Hey, don't get bent out of shape. It's not like I care. But I'd just give them a rest for a day or two."
    nov tease "Still, if the pressure gets to be too much... and you really need someone to give you a hand..."
    nov "There's an easy fix."
    mc "{color=#b7b7b7}{i}Wait, is she saying what I think she's saying?{/i}{/color}"
    mc "Yeah?"
    nov smirk "Just get Sophie drunk, a bit of rum and those panties hit the floor."
    mc "God damn it! You had me going for a second."
    nov "You never learn."
    nov neutral "Well, I've got work to do... and you've got chickens to find. So go!"
    mc "Yeah, yeah."
    "[Nova] leaves you alone in your room. You relax for a couple of minutes, grab your things and head out."
    scene black with dissolve
    pause 3
    jump EvelynTree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
