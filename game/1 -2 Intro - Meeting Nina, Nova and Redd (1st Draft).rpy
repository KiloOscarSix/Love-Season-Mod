
label intro:
    if PeepedLake == 100:
        jump HeatherExtra
    scene whitescreen
    play ambient lessrainforest fadein 5
    play music dreaming fadeout 3 fadein 8
    tmp "{color=#b7b7b7}{i}Where... am I?{/i}{/color}"
    scene lake sunny with Dissolve(2.0)
    tmp "{color=#b7b7b7}{i}I'm by the lake... Fresh breeze, pure sun. I love it.{/i}{/color}"
    window hide
    scene mc intro with Dissolve(2.0)
    w ""
    tmp "{color=#b7b7b7}{i}Ah, it's so peaceful here! I wish every day was like this.{/i}{/color}"
    scene mc intro dark with Dissolve(2.0)
    "The sky darkens as soon as you finish your thought."
    play sound thunderdistant
    scene lake rainy with flashbulb
    play ambient rainforest fadeout 1
    tmp "{color=#b7b7b7}{i}Damn, I should have kept my mouth shut! I better go home before this rain gets worse. Can't have a nice day out, can I?{/i}{/color}"
    fem "Leaving so soon?"
    "You look for the source of the voice and see a nude woman beckoning you."
    scene mermaid intro with dissolve
    window hide
    w ""
    tmp "{color=#b7b7b7}{i}Wow... She's so beautiful...and hot! Who the hell is she? And why isn't she covering herself?{/i}{/color}"
    scene lake stormy with dissolve
    show mer neutral with dissolve
    play sound thunderloud
    with flashbulb
    play ambient rainforest
    "As the mermaid speaks, the skies open up and a storm begins. You are immediately soaking wet."
    tmp "{color=#b7b7b7}{i}Shit, she's a mermaid! Dad says they're bad luck... Maybe I should just go. But... she's so beautiful, I can't turn away.{/i}{/color}"
    mer "How long are you going to stand there?"
    tmp "..."
    show mer confused with Dissolve(0.1)
    mer confused "Hey, are you listening to me?"
    tmp "Oh... Uh, sorry... Um, hi..."
    mer "Don't be shy. This might be the first time you see me, but I've seen you before. You always come here alone... I'm curious to know why."
    tmp "I just like it out here... I can relax by myself."
    show mer neutral with Dissolve(0.1)
    mer neutral "Wouldn't you rather be with me, human? Instead of by yourself?"
    tmp "I don't know..."
    show mer confused with Dissolve(0.1)
    mer confused "Why are you so confused? Oh right. Yes, you strange things have your rituals don't you? I first ask for your name, isn't that right?"
    $ MC = renpy.input("What is your name?")
    $ MC = MC.strip()

    if not MC:
        $ MC = "Alex"
    mc "I'm [MC]. I don't mean to stare... It's just that... I have never seen a mermaid before, and you are so beautiful!"
    mc "{color=#b7b7b7}{i}That was a smooth line. Smooth like sandpaper. You sound like a rube, [MC].{/i}{/color}"
    mer neutral "Nice to meet you, [MC]. Why don't you come here, I have a gift for you!"
    play sound thunderloud
    show mer evil
    with flashbulb
    show mer neutral with dissolve
    "Another flash of lightning shoots across the sky. A huge boom of thunder soon follows."
    mc "{color=#b7b7b7}{i}Something tells me this isn't a great idea...{/i}{/color}"
    mc "Look, I'd love to, but the rain's picking up, and I need to get home."
    mer "Oh come on! Don't go! You don't need to worry about the rain, silly. Come with me, it's not raining underwater!"
    "You walk towards her and the storm picks up. She's right; as the sheets of rain drench you, you know that the water cannot possibly be worse. You move, no longer in control of your body. Thunder crashes nearby, but you don't care."
    "The lake is calling to you, and so is she."
    show lake stormy:
        crop (0,0,1280,720)
        size (1280,720)
        easein 3.0 crop (0, 0, 1210, 650)
    stop ambient fadeout 1
    stop ambient2 fadeout 1
    stop music fadeout 4
    play ambient drips fadein 8
    scene black with Dissolve(5.0, alpha=True)
    pause 2
    n "The cold of the water pierces your body. You fall slack and sink to the bottom, wondering why you did this in the first place."
    n "You can't breathe and that should bother you, yet it doesn't. Nothing does; you have to be somewhere. Somewhere important."


label SelenCastle:
    play music selena fadein 2
    scene selena dream 1 with Dissolve(2.0, alpha=True)
    stop ambient fadeout 1
    "And just like that you find yourself in the main hall of a castle, ancient and foreboding."
    "The hall is empty save for an oddly dressed woman sitting on a throne."
    sel "Welcome, [MC]. I've been wanting to talk to you."
    mc "Huh? Who are you? Where am I? Where'd the mermaid go?"
    sel "That's unimportant. I need your help. Come now, take the sword in front of you."
    mc "Sword?"
    scene selena dream 2 with dissolve
    sel "Yes. That sword was meant for you."
    mc "My help? With what? And why the sword?"
    sel "Those questions don't matter. Help me, and I will help you reach your potential."
    mc "I have no idea what you're talking about."
    scene selena dream 1 with dissolve
    sel "Tell me, are you happy?"
    mc "I guess?"
    sel "Trick question. I know you aren't."
    sel "You might think you are... but I can tell that's untrue."
    sel "You crave nothing but shallow simple pleasures. You are destined for so much more."
    sel "Take the sword. Learn what it means to lead a truly fulfilling life. Become the hero you were meant to be."
    scene selena dream 2 with dissolve
    "You look at the sword. It's driven several inches into the stone of the floor."
    mc "I... I... can't. I'm not strong enough. I don't know how to use a sword. I'm not a hero."
    sel "Is it hard to use a sword?"
    sel "I think not; it's merely a tool. A sword alone is inert; it has no will, no desires, nothing."
    sel "It can kill, cut meat, frighten someone or rust away in a basement. The wielder gives it purpose."
    sel "Become that wielder. Being a hero has nothing to do with strength, it's all about using potential. It's about shaping the world around you. All those with great power were once weak!"
    sel "Claim your power."
    show selena dream 2:
        crop (0,0,1280,720)
        size (1280,720)
        easein 3.0 crop (0, 0, 1210, 650)
    nvl clear
    n "Her words resonate within you, you walk toward the sword and feel its pull as you get closer to it."
    n "Your hand reaches out for its hilt."
    n "\"I... will..\""
    scene black with dissolve
    hide window
    scene titlecardCH1 with Dissolve(3)
    pause 1
    w ""
    scene black with dissolve

label HouseIntro:
    stop music
    play sound knock1
    pause 1
    nvl clear
    n "Some loud banging brings you into consciousness."
    scene farm bedroom with Dissolve(2)
    mc "Oh... I'm in my room."
    "You hear knocking again."
    play sound knock1
    pause 1
    mc "Dad, can you get that?"
    "There is no response. After a moment, the knocking continues."
    play sound knock1
    pause 1
    mc "Anyone??"
    "No response."
    mc "Ok! I'm coming!"
    mc "I have to do everything around here."
    play music morninghappy
    "You pull yourself out of bed and head to the front door."
    scene farm house interior with dissolve
    mc "What a weird dream..."
    "The knocking continues, louder this time."
    play sound knock2
    mc "I'M COMING! GEEZ!"
    hide window
    scene intro morning wood with Dissolve(2)
    "You stumble half awake to the front door and open it."
    play sound frontdoor
    mc "WHAT?"
    hide window
    scene wake up 2 with Dissolve(2)
    w ""
    nin "Well, good morning to you too, cranky!"
    mc "Hey Nina."
    nin "What took you so long? Were you still asleep?"
    mc "Uh... yeah... what do you think?"
    scene wake up 3 with vpunch
    nin "What the fuck, [MC]?"
    mc "I like to sleep in, so sue me."
    nin "You're in your underwear."
    mc "And? You shouldn't be shocked by that after all these years."
    nin "Well, excuse me for not being used to getting flashed by you."
    mc "What the hell are you talking about?"
    nin "Look down."
    scene intro morning wood with dissolve
    "You look down and see that you're at full mast, and poking out of your underwear."
    mc "Shit!"
    "Nina walks past you into the house as you frantically try to cover up."
    scene wake up 4 with dissolve
    mc "Shit! I'm sorry, Nina! I just ran straight to the door. I didn't have time to get dressed."
    nin "Seriously? Were you dreaming of every girl in the town at ONCE?"
    mc "No! I mean, I was dreaming, but not about..."
    nin "You were definitely dreaming of something!"
    scene farm house interior with Dissolve(2)
    show mc underwear neutral at left with Dissolve(0.1)
    show nina neutral at right with Dissolve(0.1)

menu DreamChoice:
    "About you, of course! [gr]\[NinaLove +1\]":
        hide mc
        show nina neutral at center with dissolve
        mc "About you. Could there be anyone else?"
        "You wink at her."
        nin "Yeah right! Nice one. You were dreaming about Sophie or Brooke again weren't you?"
        mc "Why would I have to be dreaming about them?"
        nin "I've seen how you look at them. Plus, I mean, look down. Don't be dense."
        mc "You're the one being dense! You know it's pretty common for guys to wake up like this, right? It doesn't mean anything."
        nin "Yeah, I bet."
        "Nina waits for a moment without saying another word."
        nin "Well, go put on some clothes then. Asshole!"
        $ NinaLove = NinaLove + 1
        jump NovaIntro
    "I wasn't dreaming about that":


        hide mc
        show nina neutral at center with dissolve
        mc "I wasn't dreaming about that, Nina."
        mc "You know it's pretty common for guys to wake up like this, right? It doesn't mean anything."
        nin "Yeah, I bet."
        "Nina waits for a moment without saying another word."
        nin "Well, go put on some clothes then. Asshole!"
        jump NovaIntro

label NovaIntro:
    play sound bedroomdoor
    "You hear a door open nearby."
    play music nova fadeout 1
    scene wake up 5 with dissolve
    hide window
    w ""
    tmp "You guys are way too loud, you know that?"
    tmp "A girl needs her beauty sleep."
    "You sigh and wave to your housemate."
    mc "{color=#b7b7b7}{i}Of course she does this now. She really has no sense of shame.{/i}{/color}"
    mc "{color=#b7b7b7}{i}She's been living with me and my dad for the last few years.{/i}{/color}"
    mc "{color=#b7b7b7}{i}She needed a place to stay and he took her in without a second thought. It took a little getting used to at first, but now we're as close as family.{/i}{/color}"
    mc "{color=#b7b7b7}{i}That doesn't stop her from teasing me incessantly, or running around in next to nothing.{/i}{/color}"

    python:
        Nova = renpy.input("What is her name?", default = "Nova")
        Nova = Nova.strip()

    if not Nova:
        $ Nova = "Nova"

    scene farm house interior with dissolve
    mc "Morning [Nova]."
    show nova bed neutral with dissolve
    nov "Morning! You're up early."
    show nina neutral at slightright:
        easein 0.5
    show nova bed neutral at slightleft with dissolve
    nin "Early?"
    nov "Ish. For him, anyway."
    mc "{color=#b7b7b7}{i}I hope they get along well enough today... I never can tell with these two.{/i}{/color}"
    nin angry "Does everyone in this house hate wearing clothes?"
    "[Nova] smiles at her."
    nov bed teasing "Just the sexy ones... wait, so yeah... everyone, right [MC]?"
    mc "You know it!"
    nin neutral "Don't encourage him, [Nova]."
    nov bed neutral "Ooh, are those apples?"
    "Nina lifts up a basket you hadn't noticed before."
    nin apples "Oh right, that's why I came. I brought these to thank your father for helping me last week! Not that [mc] noticed."
    mc "First, I didn't get a chance, and second... thanks."
    nov "Hey, those are thanks for Daddy, not you."
    nin neutral "Why do you keep calling him that? He's not your..."
    nov "It's what I call him in bed, sweetie."
    nin worried "What? You? What?"
    "She grabs an apple."
    nov bed teasing "Thanks for breakfast."
    "With that, [Nova] returns to her room."
    hide nova with moveoutleft
    stop music fadeout 1
    show nina worried at center with dissolve
    mc "You ok there, Nina? Don't let her get to you."
    nin "That was just... wrong..."
    mc "It's how she jokes."
    nin neutral "I swear, you'd think Redd would rub off more on the two of you."
    mc "Have you heard dad when he's had a couple of beers?"
    nin "Not recently."
    mc "She's not too far off from the old man."
    nin "Well, she's more like him than you are. I actually see her doing stuff around the farm."
    nin smiling "You, on the other hand... When was the last time you did anything Redd didn't force you to?"
    mc "Hey! I..."
    nin "Are lazy as hell. And you wonder why you don't have a girlfriend."
    mc "Low blow, Nina."
    nin neutral "I'm just saying girls like someone who gets stuff done."
    mc "Geez! You sound like dad! I get more than enough criticism from him, thank you."
    nin "You know I'm right!"
    mc "Shut up! I get it!"
    dad "That's no way to talk to a woman, son!"
    mc "Dad?"
    "You see your father at the doorway."
    nin "Good morning, Redd!"
    play music redd fadein 1
    show father neutral at slightleft
    show nina smiling at slightright
    dad "Good morning, Nina! Is this layabout giving you grief?"
    nin smiling "Nothing I can't handle! I came here to bring you some apples as a thank you for your help last week."
    dad "No need. But thank you, they look delicious, as always!"
    dad "[MC], why aren't you two an item? I mean, she keeps you in line! Every man needs a woman like that. You two should get married, son!"
    show nina worried
    "Nina blushes."
    mc "Dad! Stop it! You know we're just friends!"
    nin neutral "Right!"
    mc "Plus, she has a boyfriend."
    dad "You two are breaking my heart."
    nin smiling "Sorry Redd, but I'll help him find someone good. If he gets off his butt. What are friends for?"
    dad "Hah! If he gets off his butt! You might as well say never, Nina."
    mc "I'm right here, you know."
    nin "I know."
    dad "Well, speaking of getting off your butt. Did you get the water from the well yet?"
    mc "No... I just got up. I'll go get it now."
    dad "While you're at it, I need you to look around for our chickens."
    nin worried "What happened to them?"
    dad "Looks like someone tried to steal our eggs last night... and they broke the coop open. The chickens all escaped."
    mc "All six of them?"
    dad "Yep. It's not the first time these punks have tried something, but it's the first time they did so much damage."
    mc "Just let me get my hands on the asshole who did this. I'll make sure he never tries it again!"
    dad "I appreciate the candor, son, but don't get yourself hurt, just go get the chickens."
    nin "Come on, [MC]. You couldn't even take me in a fight."
    mc "I can handle it."
    dad "If you say so, son."
    nin neutral "I don't have to be home for a little while. I'll help you find them."
    dad "Thank you, Nina."
    mc "And no thanks for me?"
    dad "Finding them is your responsibility. She's helping out of the goodness of her heart."
    dad "Good luck, I'll be outside fixing the fence."
    nin "Well, we should probably get going."
    mc "Yeah. Dad was right though, thanks for the help."
    nin smiling "Like I said, what are friends for?"
    scene black with dissolve
    jump Slime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
