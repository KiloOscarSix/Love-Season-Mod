label PartyIntro:
    play music evening
    scene woodpile with dissolve
    "As you near the clearing by the lake, it's still pretty quiet."
    mc "It looks like we're a little early."
    "You both enter the clearing and see Nina and a few militia members setting up."
    show nina neutral with Dissolve(0.1)
    nin "Perfect! I was hoping you'd get here!"
    mc "Hi, Nina."
    show nina neutral at slightright
    show mia neutral at slightleft
    mia "Hello. Nice to see you again."
    nin "Oh, same to you."
    nin smiling "So, [MC], you know how you're my bestest friend in the whole wide world?"
    mc "What do you need, Nina?"
    nin neutral "That obvious?"
    mc "That obvious."
    nin "Can you help the guys get the bonfire started? Trevor's having trouble."
    mc "Wait, so there's stuff Trevor can't do? I'm shocked."
    nin "Don't start."
    mia "Are you good at building fires, [MC]?"
    nin "He's really good."
    mc "I guess, it's not really that hard."
    nin "Tell that to my boyfriend."
    "You call over to Trevor."
    mc "It's not that hard!"
    "Trevor shouts back."
    if TrevorFriend > 0:
        tre "I know! I've got this!'"
    else:
        tre "Yeah? Fuck you too!"
    tre "I just need a minute. Damn this flint!"
    nin "[MC], can you please help them before he sets himself, or worse, someone else, on fire?"
    mc "Fine, but one day, Nina, I may ask a boon of you. That day may never..."
    nin moreangry "Shut it and go!"
    mia "Be careful!"
    hide nina with Dissolve(1)
    hide mia with Dissolve(1)
    "You walk to the wood pile."
    show trevor neutral with Dissolve(1)
    tre "I said I can handle this."
    mc "Well, Nina begs to differ. Plus, it's not like she'll take no for an answer."
    "Trevor sighs."
    tre "Yeah, you've got a point."
    show trevor neutral at slightright
    "You examine the stack of wood."
    mc "Well, there's your problem right here. The structure is all wrong, we need to cross the branches and what are we using as kindling?"
    tre "We just piled stuff up in a pyramid. Some of it burns for a little bit, but it dies down quickly."
    mc "Ok. Look, Trevor, I need you to get me a bunch of branches, different sizes, but DRY. As dry as you can find."
    mc "Can anyone else help?"
    tre "Lisa, where are Toby and Luke?"
    show trevor at slightright
    show lisa neutral at slightleft
    lis "I think they're out in the forest, gathering wood."
    mc "That's a waste, we have enough fuel, we just need kindling, and tinder to get things started."
    lis "You know guys, all about the big hunks of wood."
    mc "Yeah, well. Lisa... Go get some tinder; I'm talking about dried leaves, mainly. But dead twigs will work too."
    "Lisa sighs."
    lis "Luke and Toby owe me for this."
    nvl clear
    hide lisa
    hide trevor
    n "You turn to the remaining militia member."
    mcn "Ok... Uh, guy... Help me stack these correctly."
    n "You both move the fuel around, stacking it on the outside of the pile."
    mcn "So, where is the wind coming from today?"
    n "You wet your finger and hold it up."
    mcn "Oh, it's from the west."
    nvl clear
    n "You draw an arrow on the ground to remind youself where the wind is coming from."
    n "You create a little opening at the base of the arrow, and soon you finish stacking the wood."
    n "Soon, Lisa and Trevor return."
    mcn "Great. Ok. Let's see."
    n "You place the tinder inside the opening, and put the kindling on top."
    "Trevor looks it over."
    show trevor neutral with Dissolve(0.1)
    tre "So are we good?"
    mc "We should be. You grab a torch and light it."
    mc "Now... stand back."
    hide trevor
    "You thrust the torch into the wood pile and the tinder catches. Soon the entire pile is a large, perfectly shaped bonfire."
    hide window
    scene bonfire with dissolve
    play ambient fire
    w ""
    mc "There we go. See? Easy."
    show trevor neutral at slightright
    show lisa neutral at slightleft
    tre "Not bad."
    lis "Seriously."
    tre "Come on, Lisa, let's get the drinks!"
    hide trevor
    hide lisa
    "The sun has finally set, but the fire lights the area. You see more and more people arrive for the party."
    "You look around and see Mia sitting by herself."
    show mia smiling with Dissolve(1)
    play music afternoon2 fadein 1
    mia "You did an amazing job with that fire! I'm impressed!"
    mc "Thanks! Sorry for leaving you on your own, you must've been bored!"
    mia "Oh no! It was nice to see someone else doing all the hard work for a change!"
    mc "Silas can't be that bad..."
    mia neutral "He's not... I'm just joking. I like helping him out, and he's teaching me a lot too."
    mia "I also get to read a lot. It's nice."
    mia "But he's getting older, and I don't know how he has the energy for it all."
    mc "Well, there are your pies!"
    "Mia laughs."
    mia blushing 2 "I... Yes... Maybe I should make them more often."
    mc "{color=#b7b7b7}{i}Too many and I think the elder's heart will stop.{/i}{/color}"
    mc "I'm sure he'd like that."
    mia blushing 1 "I feel bad about leaving him alone... He's done so much for me."
    mia "I'm so lucky he took me in, not just him. But I really love this village."
    mc "Yeah. And he keeps everything going too. It's crazy."
    mia "I just wonder sometimes... He's getting so old."
    mia "I don't think anyone could replace him when he..."
    mc "Well..."
    show mc neutral at left with Dissolve(1)
    show mia blushing 1 at farright

menu ReplaceElder:
    "You could":
        hide mc
        show mia blushing 1 at center
        mc "You could do it! He's teaching you everything he knows and you know his job better than anyone else in the village."
        "Mia smiles."
        mia neutral "That's nice of you to say that... But I'm not leader material. I can... barely talk to strangers sometimes."
        mc "Guess I'm not strange, than."
        mia "Only a little."
        mia "I just don't think people would respect a woman in the role. It's not how things work around here."
        mia smiling "But it's a nice thought."
        jump Party1
    "I could.":

        hide mc
        show mia blushing 1 at center
        mc "I could do it."
        mia neutral "Maybe, you're a hard worker!"
        mc "Are you sure you have the right guy??"
        "Mia smiles."
        mia "Yes. Silly."
        mia smiling "Look at the work you did just now..."
        mia "But I don't think anyone's ready for the job yet."
        mc "Well, Silas isn't going anywhere."
        mia "Not for a long time, I hope."
        jump Party1
    "Trevor probably will":

        hide mc
        show mia blushing 1 at center
        mc "Honestly, it'll probably be Trevor. He's already running the militia."
        mia "Yeah, but he seems very young to be in charge of something like that."
        mc "People like him, for some reason. And he is the best fighter in the village."
        mia neutral "That doesn't mean he'll be a good elder though."
        mc "Yeah, I'm not saying I'd be happy with it, I just think it's the most likely scenario."
        mc "People care more about whether or not you can kill things instead of how smart you are."
        mia "Do you think so? I think you're a lot more interesting than he is."
        mia blushing 2 "I mean... Forget I said that."
        mc "Uh, sure thing."
        jump Party1

label Party1:
    "You look around and realize the party is now in full swing."
    mc "Want to walk around?"
    mia smiling "No... Thank you. I like being by the fire."
    mc "Oh, OK."
    "You get ready to sit next to her."
    mia "But don't let me stop you. Go out and have fun..."
    mia neutral "I'll join you later."
    mc "Are you sure?"
    mia "Yes."
    mc "OK, then. I'll be back soon."
    hide mia
    nvl clear
    n "You leave Mia by the fire and go exploring for a while. "
    play sound walkgrass
    n "On the other side of the fire, you see Evelyn sitting by herself. She seems to be lost in thought, staring at the fire."
    nvl clear
    mc "Hey! How's Beanie?"
    play music evelyn fadein 1
    show evelyn neutral with Dissolve(0.1)
    "Evelyn looks up at you and smiles."
    eve "She's doing pretty well; I scolded her pretty badly after you left."
    mc "How'd she take it?"
    eve "She's a cat, [MC], I don't think she cared too much."
    mc "So, here by yourself, then?"
    eve "Yes. The fresh air is nice, and you've built a great fire here."
    mc "Thank you."
    eve "Building fires, rescuing cats... herding chickens. You're just a regular handyman."
    mc "Do you think I should make that my job? I could run around town, fixing whatever needs fixing."
    "Evelyn smiles."
    eve smiling "Sure, I could use some help around the pub, you know."
    mc "Well, what's in it for me?"
    eve "I'm sure I can think of something."
    mc "Yeah, well. I doubt dad's going to let me do anything not farm related."
    mc "We're just about ready to harvest."
    eve "Well, that's a shame. But not unexpected. We all get caught up in our family businesses around here."
    mc "Yeah. Not a whole lot of options unless you want to leave."
    eve neutral "Tempting, but no."
    "You hear a loud WHOOOP! and see some of the militia members partying pretty hard while drinking."
    mc "Looks like the drinks are ready."
    eve "Looking to get drunk tonight, [MC]?"

menu EvelynDrinking:
    "[gr]Nah, not much of a drinker.":
        jump NotDrink
    "Hell yes I am!":

        jump GonnaDrink

label NotDrink:
    mc "Nah, I'm not a big drinker, really."
    eve "Really? I mean, it is a party. If there was a time for it, now would be it."
    mc "You're right."
    eve "Do you mind if I ask why?"
    mc "Good question. I guess..."

menu WhyNoDrink:
    "I'm just not in the mood. [gr]\[EveLove +1\]":
        mc "I'm just not feeling it at all, really."
        eve "Must not be much for parties then..."
        mc "It's not that..."
        mc "I just have a weird feeling tonight."
        mc "Don't know how else to explain it."
        eve "Huh. Well, whatever works for you."
        eve "It'll be nice not being the only sober person here, in either case."
        $ EveLove += 1
        jump EvelynSober
    "I don't like losing control. [gr]\[EveLove +1\]":

        mc "I like to be in control. When you drink it's way too easy to lose yourself in it."
        eve excited "Oooh. Nice answer."
        eve "It's deeper than I expected, too."
        mc "Well, not too deep. I'm speaking from personal experience."
        eve smiling "Are you now?"
        mc "Let's just say that [Nova] snuck out a bottle of rum one night, and things got out of hand."
        eve "What did you do?"
        mc "Story's over. Not gonna talk about it."
        eve "Ok. Either way, it'll be nice not being the only sober person here."
        $ EveLove += 1
        jump EvelynSober

label GonnaDrink:
    mc "It's a party! It's the perfect time."
    eve excited "Hah! I guess you're right."
    mc "What about you?"
    eve neutral "I'll be the only sober person here, probably."
    mc "Really?"
    jump EvelynSober

label EvelynSober:
    mc "Why's that?"
    eve neutral "Well, I don't like drinking, at all, really."
    eve "I don't mind people who do. And they can be really fun to chat with, but it's not for me."
    mc "So, hold on, your family runs the pub, pretty much all the alcohol in town flows through your doors, and you don't drink at all?"
    eve "Yeah, it sounds a little weird when you put it like that."
    mc "Not that weird, I guess. You probably have to deal with bad drunks all the time."
    eve "Sometimes, that's true. But I don't think that's it."
    eve "I just don't like it... Not much more to it than that."
    mc "I get it."
    "Evelyn stands up."
    eve "Well, I'm going to go see what we have that isn't filled with alcohol."
    eve "I'll see you around the party, [MC]."
    mc "Yup! See you around."
    hide evelyn
    "As you get up from the fire, you see Nina off by herself. She walks up to you."
    play music nina1 fadein 1
    show nina smiling with Dissolve(0.1)
    nin "Hey! Great job on the fire!"
    mc "You say that like you're not the one who conscripted me into service."
    nin "Well, we needed the help."
    mc "Yeah, yeah."
    nin "So..."
    mc "What?"
    nin "Where's Mia?"
    "You point to Mia."
    mc "She's sitting over there. She wanted to relax."
    nin angry "You shouldn't leave your date alone like that."
    mc "We... We're just friends."
    nin "Really?"
    mc "I took her along to get her out of Silas' house."
    nin neutral "Oh, I see. I thought..."
    mc "Oh. Hmm..."
    mc "Is it a date?"
    "Nina gives you an umbelieving look."
    nin moreangry "Shouldn't you know?"
    mc "Yeah... I probably should."
    nin "Well, either if it is or isn't, she's a nice girl..."
    mc "I know."
    nin neutral "Maybe I'll keep her company when you're out getting wasted."
    mc "I'm not going to get wasted."
    mc "Probably."
    mc "And speaking of leaving your date all alone..."
    "Before Nina can respond you hear a woman's voice from behind you."
    '???' "There you are, Nina!"
    "A slightly tanned brunette you've never met before comes up from behind you."
    show laura neutral at slightleft
    show nina smiling at slightright
    nin "Laura! You're late!"
    "The two girls hug."
    lau "Come on, the party's just starting, I just skipped the boring parts!"
    "Laura takes a sip from the cup in her hand."
    nin worried "How much have you had to drink already?"
    lau smiling "It's a party, Nina!"
    mc "And this is?"
    "Laura holds out her hand."
    lau "You must be [MC]. "
    mc "Yeah."
    "Laura turns to Nina."
    lau neutral "This one kept telling me I had to meet you."
    nin "I just..."
    mc "I think she mentioned you too."
    nin neutral "So, yeah. This is Laura. She just moved in to the old shop."
    mc "You bought the place?"
    lau "My dad, actually. But yeah. I left life in the city for this little backwater."
    lau "No offense."
    mc "Uh... You're not wrong."
    "You see Trevor walk up to you, all swagger as always."
    show trevor neutral with Dissolve(0.1)
    show laura neutral at farleft
    show nina neutral at farright
    tre "There you are. I was looking all over for you."
    nin "I've been here the whole time."
    tre "Well, I, uh, wanted to talk about some stuff..."
    "Laura turns to Nina."
    lau smiling "I'm gonna get another drink with this guy... We'll leave you two alone."
    nin "Oh, uh, thanks..."
    mc "Yeah... Right, see you later, Nina."
    hide trevor
    hide nina
    "The two of you walk away from Nina and Trevor and wander around the party."
    show laura neutral at center:
        linear 0.5
    play music laura fadein 1
    lau "Damn, they moved the rum."
    mc "Little early in the night anyway."
    lau "No such thing. Parties should start early and run late. Anyone who disagrees is a loser."
    mc "You're pretty open, aren't you?"
    lau smiling "Why shouldn't I be? I mean, it's nice out here, sort of, if you can ignore the smell of animal shit everywhere, but you guys need to loosen up."
    mc "Hah, well, you're probably not wrong. But we're looser around here than you might think."
    lau "Then someone's been holding out on me."
    lau "By the way, you know Nina's been trying to hook us up, right?"
    mc "Yeah, I got that impression."
    lau "Part of the reason I came here late is because I was hoping to avoid you. Nina didn't paint a great picture."
    mc "What did she say?"
    lau "She said you were a great friend, and really funny."
    mc "She called me funny? Oh Goddess!"
    lau "I know, I came in here expecting you to have one eye and weigh like 20 stones."
    mc "Ha! She talked about how 'nice' you were."
    lau surprised "Goddesss, she didn't! You must have expected a goblin."
    mc "Troll actually, but you're close!"
    lau smiling "Well, you're definitely not a one-eyed glutton."
    mc "If you're into that... there's this dirty old man who lives just outside of the village..."
    "Laura laughs."
    lau "No... I think I'm good, thanks."
    mc "Your loss."
    lau neutral "You know, you're right. How far outside the village did you say this sex machine lived?"
    tob "What are you doing here, loser?"
    "The voice rings out from nearby."
    mar "I... was just coming to the party!"
    tob "You weren't invited."
    mc "Crap."
    lau surprised "What is it?"
    mc "I've got to save someone from getting their ass kicked."
    "You sigh."
    mc "I'll see you around."
    lau "No way. This I have to see."
    play music militia1 fadein 1
    scene bonfire forest
    nvl clear
    play sound walkgrass
    n "You head towards the sounds of the argument."
    n "When you get there, Marcus is on the ground. Toby, Sophie's boyfriend, is standing over him."
    show toby neutral with Dissolve(0.1)
    tob "You lost your party privileges, Marcus."
    show marcus neutral at slightright
    show lisa neutral behind toby at slightleft
    mar "I just..."
    tob "Why were you following me into the woods?"
    mar "I wasn't! I just wanted to come to the..."
    tob "Bullshit!"
    lis "Toby, relax!"
    tob neutral "You don't come to a party by sneaking around."
    mar "I..."
    show marcus neutral behind toby at farright
    tob "Were you spying on me?"
    mar "No! Well... I mean... Yes. Just a bit."
    tob "You little..."
    show toby neutral at slightright
    "Toby grabs Marcus by the collar."
    mc "Hey man! That's enough. He didn't hurt anyone."
    show toby neutral at center
    show lisa neutral at farleft
    tob "Stay out of this!"
    tob "This doesn't concern you!"
    tob "He needs to learn a lesson. That losers needs to stay the fuck away from normal people!"
    show toby neutral with Dissolve(0.1)
    show marcus neutral at farright
    show lisa neutral behind toby at slightright
    show mc neutral at offscreenleft
    show mc neutral at farleft
    show laura neutral behind toby at slightleft
menu SaveMarcus:
    "Punch Toby [gr]\[LauraLove +1\] \[Marcus +1\]":
        hide mc with dissolve
        hide marcus with dissolve
        hide lisa with dissolve
        hide laura with dissolve
        show toby neutral at center with vpunch
        play sound hit
        $ LauraLove += 1
        $ MarcusFriend += 1
        mc "I know you're in love with him, but there are better ways to..."
        "Hoping the insult caught him off guard, you rush towards Toby and punch him in the face."
        "Or try to; you whiff pretty badly."
        tob "Are you fucking serious? Ok, [MC], I'm going to kick your ass!"
        "Toby grabs you by the collar and pulls you towards him."
        jump Party2
    "Talk it out [gr]\[LauraLove +1\] \[SophieLove +1\]":

        $ LauraLove += 1
        $ SophieLove += 1
        hide mc with dissolve
        hide lisa with dissolve
        hide marcus with dissolve
        hide laura with dissolve
        show toby neutral at center
        mc "Come on Toby! I know you're crushing on him, but there are healthier ways to show it."
        "Toby turns to you..."
        tob "What did you say?"
        mc "I said that your attack on Marcus is a result of deep seated issues with your denial of your attraction to him."
        tob "I am going to kick your ass!"
        "Toby grabs you by the collar."
        jump Party2

label Party2:
    show lisa neutral at offscreenright
    show lisa neutral at farright
    lis "Toby! Come on! Stop this!"
    tob "He..."
    sop "What did this idiot do this time?"
    "Sophie enters the clearing."
    show sophie neutral at offscreenleft
    show sophie neutral at farleft
    tob "He said I was..."
    sop angry "He said something? That's it?"
    sop "Did he at least insult me?"
    tob "No..."
    sop "Then stop with the crap!"
    sop "You always do this."
    "Sophie looks down and sees empty beer mugs on the ground."
    sop "How much have you drunk?"
    tob "I..."
    sop "Drop him."
    "Toby lets you go; you fall to the ground, and back up before standing again."
    sop neutral "Come on... we're here to party. Why waste your time with losers?"
    "Sophie turns to you."
    sop "No offense."
    mc "Taken."
    sop "Who's the new girl?"
    hide lisa with moveoutright
    show laura neutral at offscreenright
    show laura neutral at farright
    show sophie at farleft
    lau "Laura... I guess you're the head bitch around here?"
    sop "You learn fast. You probably shouldn't be hanging out with [MC] though. Just so you know."
    lau "I'll take it under advisement."
    sop "Come on, Toby, let's go somewhere a little more private."
    show sophie behind toby
    tob "What for?"
    show toby behind sophie
    sop angry "Oh for goddess' sake... What do you think for?"
    "Sophie grabs Toby by the arm and takes a path into the woods."
    hide sophie with dissolve
    hide toby with dissolve
    show lisa neutral with Dissolve(0.1)
    lis "You're an interesting dude, [MC]."
    "Lisa heads off as well."
    hide lisa with dissolve
    show laura neutral:
        linear 0.5 xalign 0.5
    play music laura fadein 1
    lau "Well, he was a barrel of laughs."
    mc "Yeah..."
    lau "You see his kind everywhere."
    lau "But you stepped up. So that's something, at least."
    "Marcus groans."
    mc "Are you still on the ground?"
    mar "I like the view."
    "You notice he's staring at Laura's legs."
    lau "Do you, now?"
    mar "I..."
    lau "You have a seriously pervy friend."
    "You sigh."
    "Laura laughs."
    lau "That says it all."
    mc "I guess it does."
    lau "Well, I'm going to track down Nina, save her from Sir-Giant-Pecs."
    lau "Look for me later."
    mc "Sure."
    "Laura walks back to the bonfire."
    hide laura with dissolve
    stop music fadeout 1
    mc "Come on Marcus, let's go."
    "You look around. Marcus is nowhere to be seen."
    mc "Of course."
    play sound walkgrass
    "You wander around the party some more until you come upon Brooke, Trevor's sister."
    scene brooke party 1 with dissolve
    play music brooke fadein 1
    mc "{color=#b7b7b7}{i}Eh... I wonder if I should bother with them. Brooke is hot as hell, but she hangs with a rough crowd.{/i}{/color}"
    bro "Hey! [MC]! That's your name right? Come here a second!"
    "You think about it for a second, then head over."
    mc "Hey."
    bro "Why are you by yourself? Did you get lost out there?"
    mc "How would I get lost? The fire's right over there."
    bro "You have a point."
    scene bonfire forest with dissolve
    show keith neutral at slightleft
    show brooke neutral at slightright
    'Blond Friend.' "Sit down! Grab a drink."
    mc "Uh, sure."
    bro "You sure you're up for this? I mean, we don't have any milk around."
    mc "Ha. Ha. So very funny."
    bro "Hey, just checking. I don't want to waste this stuff."
    'Blond Friend' "It's hella strong."
    bro "This shit will fuck you up!"
    mc "How bad could it be?"
    bro "Oooh. We got a badass over here?"
    mc "{color=#b7b7b7}{i}Should I drink some?{/i}{/color}"
    hide keith
    show mc neutral at offscreenleft
    show mc neutral at farleft
    show brooke neutral at farright
menu BrookeDrink:
    "Fuck it! You only live once! [gr]\[BrookeLove +1\] \[DrinkOn\]":
        scene brooke party 2
        "You take a seat next to Brooke."
        mc "Pass the bottle!"
        bro "Nice! Here you go."
        mc "How bad could it be?"
        "You take a long swig, and the taste is stronger than you expected. The alcohol burns on its way down your throat."
        "You find yourself coughing violently for a second."
        'Blond Friend' "There he goes! Keep it down bro."
        bro "Damn, one hell of a swig there, [MC]."
        "You keep coughing, and Brooke laughs."
        bro "There you go!"
        bro "Feel it!"
        $ DrinkOn = 1
        $ BrookeLove += 1
        jump Party3
    "Fuck that! You only live once!":
        mc "Nah... not in the mood to pass out just yet."
        bro "Still a kid, huh? Well at least you know your limits."
        bro "This is strong fucking shit though. I'll give you that."
        bro "Sit down, let's talk."
        "You take a seat next to Brooke."
        scene brooke party 2
        $ BrookeLove += 0
        jump Party3

label Party3:
    mc "What is that stuff anyway?"
    bro "It's from dad's special reserve. And by special reserve I mean it's his own wormwood alcohol."
    mc "What?"
    bro "You've got to build up a tolerance."
    bro "Dad drinks this like water."
    mc "How is he not dead?"
    bro "Our bloodline is strong!"
    mc "Ha!"
    bro "So what brings you out here to hang with the undesirables?"
    mc "Just seeing the sights."
    bro "Uh-huh."
    if PeepedLake == 1:
        scene brooke bath 2 with flashbulb
        pause .5
        scene brooke bath 1 with flashbulb
        pause .5
        "The image of Brooke bathing at the lake flashes through your mind."
        mc "{color=#b7b7b7}{i}God how is it all the girls in this village are so hot?{/i}{/color}"
        scene brooke party 2 with dissolve:
            crop (0,0,1280,720)
            size (1280,720)
            easein 1.0 crop (284, 398, 572, 322)
        hide window
        w ""
        "You find yourself staring at her tits."
        mc "{color=#b7b7b7}{i}What would I give to see those funbags again?.{/i}{/color}"
        scene brooke party 2 with dissolve
        bro "Eyes up here, asshole."
        mc "Oh... Uh..."
        bro "Didn't you get enough of a look yesterday?"
        mc "What?"
        bro "You heard me. You suck at hiding, by the way."
        mc "I, um... Sorry."
        bro "So it really was you? Thanks for the confirmation."
        mc "Shit."
        bro "Got you!"
        if DrinkOn == 1:
            mc "Damn you alcohol!"
            bro "Don't blame the liquor for your being a creeper."
        mc "Uh... Sorry."
        bro "I could have my little brother kick your butt... But eh, it's not a big."
        bro "In the grand scheme of the universe, what's a little skin?"
        mc "Well if that's the case..."
        bro "Don't push it."
        mc "Point taken."
        jump Party4
    else:

        bro "Bah, that's boring."
        mc "As opposed to sitting off by yourself getting plastered?"
        bro "Exactly."
        jump Party4

label Party4:
    bro "Anyway kid. Get going, we have some serious drinking to do. And you're not ready."
    mc "I..."
    "Brooke gives you a hard stare."
    mc "Am totally not."
    bro "See. It's good to know your limits, [MC]."
    bro "See you around."
    scene bonfire forest
    play music nina2 fadein 1
    "You walk back to the main party, and on your way you hear Nina's voice."
    mc "{color=#b7b7b7}{i}Wonder what she's up to?'{/i}{/color}"
    "The conversation sounds rather heated."
    mc "{color=#b7b7b7}{i}Oh, that sounds like Trevor.{/i}{/color}"
    show trevor neutral at slightleft
    show nina neutral at slightright
    tre annoyed "Are you my girlfriend or what?"
    nin "Of course I am!"
    tre "So... why don't you act like it?"
    tre "You won't even kiss me in public."
    nin worried "I'm just a little shy about that stuff."
    tre angry "Yeah, whatever."
    nin "Why is this such a big deal?"
    tre annoyed "Look, can we just go to the grove or something? We can be alone there."
    nin neutral "I don't want to leave Laura alone for too long."
    tre "She's off with [MC], she'll be fine..."
    nin "Right... Okay... just for a bit."
    tre neutral "See... It'll be fun, and we'll have privacy."
    scene bonfire forest
    nvl clear
    n "Suddenly, Sophie and Toby loudly appear. Sophie is hanging on Toby and kissing his neck. They are drunk off their asses."
    n "About one hundred feet behind them you see Marcus, following them as stealthily as he can."
    nvl clear
    show sophie neutral at offscreenright
    show sophie neutral at farright
    show toby neutral at offscreenright
    show toby neutral behind sophie at slightright
    show trevor neutral at offscreenleft
    show trevor neutral at farleft
    show nina neutral behind trevor at slightleft
    sop "Oh, sorry! Don't mind us. Just heading out to the grove."
    tre annoyed "Yeah, stop right there. Nina and I have dibs."
    sop "Well, why not make it a party? Not like it would be the first time?"
    sop "Uh, you don't mind do you, Nina?"
    nin "Hey, I mean... Why don't we just let you guys go first?"
    sop "Come on! It'll be fun. If you're hanging with us, you're gonna have to get used to it sooner or later."
    sop "Already seen your boyfriend's junk, so where's the harm?"
    nin "Uh, yeah. I appreciate the offer, but I really don't like the whole public thing..."
    sop "Your loss!"
    "Sophie grabs Toby by the crotch."
    tob "Sophie! They were already headed there. We could let them go first..."
    sop "NO WAY! I've been waiting to get you alone all night. And she offered."
    "Sophie pulls Toby away and he shrugs at Trevor as she leaves."
    hide sophie with moveoutright
    hide toby with moveoutright
    show nina neutral at slightright
    show trevor annoyed at slightleft
    tre angry "Really, Nina?"
    nin "I..."
    nin "Come on, let's go back to the party, ok?"
    show trevor neutral with Dissolve(0.1)
    tre "Fine."
    "Trevor sighs, and they both leave. They pass by you."
    tre neutral "Hey, man."
    mc "Uh, hi."
    nin "We're heading back... Um, I wouldn't go to the grove for a bit... Sophie just took it over."
    tre "Come on, he's alone right now... is he just gonna go there to stare like a creeper?"
    nin "Oh, right..."
    "Nina smiles at you and walks away."
    hide nina with dissolve
    hide trevor with dissolve
    stop music fadeout 1
    mc "{color=#b7b7b7}{i}She was going to go out to the grove with Trevor, now? Just how far have they gone?{/i}{/color}"
    mc "{color=#b7b7b7}{i}Just don't focus on it, let's see what else is going on.{/i}{/color}"
    "You decide to go look for Mia or Laura when you spot Marcus out of the corner of you eye."
    "He has a shit eating grin on his face as he follows the path Sophie took."
    mc "{color=#b7b7b7}{i}That idiot is going to get murdered for real this time.{/i}{/color}"
    mc "{color=#b7b7b7}{i}I should let him...{/i}{/color}"
    mc "{color=#b7b7b7}{i}Nah... I can't do that...'{/i}{/color}"
    hide window
    scene hut night with dissolve
    w ""
    nvl clear
    n "You follow Marcus, and pray that you don't make much noise. Soon, you arrive at the grove, a small clearing near the lake with an abandoned house in it."
    n "The house has seen more than its fair share of private parties, loving couples, and you assume more than one encounter that has led to a broadsword wedding."
    n "You see him stop, and walk up next to him. You tap on his shoulder. He turns to you and puts his fingers up to his mouth."
    mcn "{color=#b7b7b7}{i}He's not leaving... What am I going to do with him?{/i}{/color}"
    n "He motions towards the window and you look inside. There are bits of discarded clothing, likely from couples who went there earlier in the night and missed some of it while getting dressed again."
    mcn "{color=#b7b7b7}{i}First time here, and the person with me is Marcus. This is my life...{/i}{/color}"
    nvl clear
    play music sophie fadein 1
    scene sophie grove 1
    sop "Come on Toby, you're drunk, I'm drunk. All this alcohol has me horny as hell!"
    "Sophie starts undressing."
    tob "Sophie..."
    sop "It's been forever since we last fucked! You're not getting away from me tonight."
    mc "{color=#b7b7b7}{i}Toby sounds fucking wasted.{/i}{/color}"
    tob "Ok, ok. Just give me a sec to...."
    "Sophie looks up and sees you staring through the window."
    scene sophie grove 2
    sop "Toby? Someone is peeping on us. Should we give them a show? maybe Trevor and Nina changed their minds after all."
    mc "Uh..."
    sop "Toby?"
    tob "Zzz..."
    mc "{color=#b7b7b7}{i}Ok, time to use this awkward moment to run as fast as I can{/i}{/color}"
    "You turn and start to run off, but you hear the door open behind you."
    scene sophietits angry
    sop "Stop right there you pervert!"
    sop "Unless you want me telling everyone about this."
    mc "Look, I was just trying to stop, M..."
    "Your eyes are immediately drawn to Sophie's chest. She's covering herself, but not very well."
    scene sophietits
    sop "What?"
    mc "Never mind."
    "Sophie looks down, and in her drunken state takes a moment to realize what exactly you were staring at. She tries to cover herself more, but you can still see a stray nipple poking out from behind her arms."
    sop "Stop staring, loser!"
    mc "I, uh... Sorry."
    scene sophietits angry
    sop "You think sorry is gonna cut it? I'm telling you right now. You tell ANYONE about this, I'll make sure the only time you'll ever get your dick wet in this town is with one of your own chickens."
    mc "I won't tell anyone I saw your tits."
    sop "Fuck that! I mean the shit with Toby!"
    mc "That you couldn't get him up?"
    scene sophietits annoyed
    sop "He would have gotten up just fine if he didn't pass the fuck out! Again!"
    "As if on cue, a loud snore echoes from the abandoned house."
    mc "This happens often?"
    scene sophietits angry
    sop "Not another word!"
    scene sophietits neutral
    sop "Hm... But you know what would show that drunk idiot? If I sucked the dick of the next boy I see!"
    mc "{color=#b7b7b7}{i}Is she serious? Maybe...{/i}{/color}"
    scene sophietits
    sop "Oh, gross! Not happening. I didn't mean you! I was thinking out loud! Creep."
    mc "I didn't say shit!"
    sop "Yeah, your pervy leer said it all."
    mc "Well excuse me, princess!"
    scene sophietits annoyed
    sop "Whatever."
    sop "At least I know I still have it."
    sop "I can't believe it! Losers like you would fucking KILL to see my tits and this asshole just falls asleep."
    mc "Can you stop with the loser bullshit?"
    mc "{color=#b7b7b7}{i}Starting to get a little pissed off here.{/i}{/color}"
    sop "Just get the fuck out of here..."
    "You nod and turn around."
    if SophieLove >= 1:
        sop "Wait."
        mc "What?"
        sop "I need to ask you something."
        mc "Uh... Ok."
        scene sophietits flirty
        "Sophie squeezes her arms slightly to draw attention to her bust. You make every effort to not stare, but let's be honest, that was a losing proposition."
        mc "Wha...?"
        sop "You like me, right? I mean, it was dumb of you to ask me out last year because, look at you... but..."
        sop "You do think I have great tits, right?"
        "You nod, though your eyes never leave her cleavage. Sophie smiles and continues."
        scene sophietits annoyed
        sop "Say it."
        mc "I..."
        sop "You want to see them?"
        mc "Yes!"
        sop "So tell me how much you want me. Beg me to see them, and I'll let you."
        mc "{color=#b7b7b7}{i}She's playing me like a lute and she knows it. I hate her attitude. On the other hand...{/i}{/color}"
        mc "{color=#b7b7b7}{i}Should I give in? Maybe she'll show me more if I do.{/i}{/color}"
        jump SophieWant

menu SophieWant:
    "Beg her! [gr]\[BeggedSophie\]":
        mc "They are amazing, show them to me! Please!"
        scene sophietits neutral
        sop "Well, you never will again, loser. Goddess! You actually said it!"
        $ BeggedSophie = 1
        jump PartyAfterSophie
    "Don't say it. [gr]\[SophieLove +2\] \[Honor +1\]":

        mc "..."
        sop "Say it."
        mc "..."
        scene sophietits angry
        sop "What the fuck? I can still see you staring! Say it."
        mc "I'm not a beggar."
        scene sophietits annoyed
        sop "Ugh! Whatever. Well played, I guess."
        $ Honor += 1
        $ SophieLove += 2
    "Eh, there are better ones out there. [gr]\[SophieLove +1\] \[Corruption +1\] \[BetterTitsSophie\]":

        mc "Eh, I've seen better."
        scene sophietits angry
        sop "Horseshit!"
        mc "What? Are you offended? I mean, they are nice."
        mc "{color=#b7b7b7}{i}I can't believe I'm saying this. What the hell?{/i}{/color}"
        mc "But, like I said, I've seen better."
        scene sophietits
        sop "Better? Whose?"
        mc "Show me, and I'll tell you."
        scene sophietits angry
        sop "Ugh! Asshole! Keep dreaming!"
        "Sophie looks at you a little differently than before."
        mc "{color=#b7b7b7}{i}Huh, I figured she'd go ballistic.{/i}{/color}"
        scene sophietits flirty
        sop "I know you're just trying to look big."
        $ SophieLove += 1
        $ Corruption += 1
        $ BetterTitsSophie = 1

label PartyAfterSophie:
    "Sophie backs up and lets go."
    sop "You can go now."
    mc "But..."
    scene sophietits annoyed
    sop "Go now. Not saying it again."
    mc "Yeah, sure."
    sop "And remember what I said about the chickens."
    mc "How could I forget?"
    "You leave Sophie with her passed out boyfriend and walk back to the party."
    play music nova2 fadein 1
    scene mianovafire with dissolve
    "The party is in full swing when you return."
    mc "I wonder how Mia's doing?"
    "You walk back to the bonfire and see that Mia is sitting next to [Nova], who is handing her a cup."
    mc "{color=#b7b7b7}{i}Mia's there with [Nova], I'm wondering if I should be glad she's making friends or worried because... [Nova]?{/i}{/color}"
    "You walk up the two."
    nov "Come on Mia! It's just a little wine."
    "Mia is blushing a bit. It seems she's a little tipsy."
    mia "That's... That's what you said last time..."
    mia "But I know that alcohol reduces inhibitions, and while it can be used medically and in cooking, when you drink too much of it it can be bad. The elder says to be careful so that I don't get taken advantage of."
    mia "You're not trying to take advantage of me, are you, [Nova]?"
    nov "Not at all! We're just having fun."
    mia "I don't know how well you could take advantage of me though... I think I'm a little too dizzy to cook or clean right now."
    nov "Oh my god, you're the sweetest thing. I mean, you've only had a few so far. You're in great shape."
    mia "I don't know..."
    "Mia looks up and sees you."
    scene bonfire with dissolve
    show mia smiling at center
    mia "[MC]!"
    mc "Um... Hi."
    mia "I've been making friends!"
    show mia smiling at slightleft
    show nova smirk at slightright
    nov "She doesn't shut up when she starts talking."
    "Mia hugs you."
    mia "I like talking!"
    nov smirk "I think she likes you."
    mia smiling "I like you too [Nova]!"
    "Mia hugs [Nova]."
    nov "Ok! Ok!"
    nov "Wow."
    mc "How much did you give her?"
    nov "Too much, apparently."
    mia "Are you talking about me?"
    nov "Yes."
    mia blushing 2 "Well... Ok."
    nov "She's a trip."
    mc "Apparently."
    nov "You missed a lot."
    mia "Nina came by with her new friend. We talked for a while!"
    mc "I'm glad to see you making friends. See? It wasn't that hard."
    mia "Your sister is my friend now, too!"
    nov "He's not my..."
    mc "She just stays with us, Mia."
    mia blushing 1 "Right... I don't know why I thought you were related..."
    mia "I'm an only child... And you guys act like I think siblings should."
    mc "No big deal..."
    nov neutral "We're not, though.'"
    mia "I'm sorry, did I say something bad?"
    nov "It's fine, babe, don't worry."
    mc "Seriously, how much, [Nova]?"
    nov "Only a couple of glasses."
    mia "Uh huh... and Laura gave me like three earlier."
    nov "I did not know that. I swear!"
    nov "It does explain a whole lot."
    mia smiling "Laura's nice. She and I talked about [MC]!"
    mc "What?"
    "[Nova] laughs."
    nov smirk "You heartbreaker, you!"
    mia blushing 1 "He's nice, you take that back!"
    nov "Ok, ok!"
    mia smiling "Good. Now I'm tired... so I'm going to lie down."
    mc "Mia, that's probably not a good idea."
    mc "Maybe you should go home and sleep there?"
    mia "OK!!!"
    "Mia smiles and clings on to your arm."
    nov "Looks like you've been drafted."
    nov "I'll say bye to people for you, [MC], better get going before she passes out."
    mc "Yeah. I'll see you later."
    hide mia
    hide nova
    nvl clear
    n "You walk Mia out of the party. As you leave, you see Nina chatting with Trevor. She doesn't take her eyes off you as you lead a drunk Mia home."
    jump AfterParty
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
