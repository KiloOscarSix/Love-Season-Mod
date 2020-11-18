label EliseSophieGarden:
    scene village 1 day with Dissolve(2)
    mc "{color=#b7b7b7}{i}OK, where to next?{/i}{/color}"
    "You explore the town in your search for the next chicken. You hear a mixture of clucking and shouting from a nearby house."
    play sound chicken
    mc "{color=#b7b7b7}{i}Sounds like that's coming from Sophie's place.{/i}{/color}"
    scene elises garden with Dissolve(2)
    play music elise fadein 1
    "A pair of blond women, one older and one younger, is trying to shoo away a chicken in their garden."
    show elise neutral at center with Dissolve(0.1)
    eli "Shoo! Get away from my cucumbers!"
    show sophie neutral at slightleft with Dissolve(0.1)
    show elise neutral at slightright
    sop "God, this is gross! Get out of here!"
    eli "I'm just about ready to pick these vegetables. I'm not letting you have them."
    "The women keep themselves in front of the chicken, blocking it from the food it wants."
    play sound chicken
    'Chicken' "BAKAWWW!"
    mc "{color=#b7b7b7}{i}There it is. It's bothering Sophie, good.{/i}{/color}"
    mc "{color=#b7b7b7}{i}It's a nice turn around for all the times she's made fun of me over the years.{/i}{/color}"
    "The chicken startles Sophie and she falls into the dirt. She looks down at herself, and her outfit is covered in dirt and mud."
    sop "Oh you fucking...."
    mc "{color=#b7b7b7}{i}Damn. The chicken hit her where it hurts.{/i}{/color}"
    sop "That's it!"
    show sophie neutral at left:
        linear 0.5
    sop "Mom, just wait here. I'll go call Toby. He can kill this stupid thing, and we'll eat it for dinner."
    eli "I don't think my garden will survive if you go, Sophie."
    sop "Fuck the garden! It killed my skirt! If you won't let me get Toby I'll break its neck myself!"
    mc "{color=#b7b7b7}{i}Shit. If she calls her meathead boyfriend over, I might lose the chicken. Better step in.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Besides, Elise has always been nice to me. If the chicken messed up her garden... I'd probably feel bad.{/i}{/color}"
    mc "Don't do that, Sophie. Hold on."
    "You walk into Elise's garden."
    show sophie at slightleft
    show elise at slightright
    sop "What are you doing here, weirdo?"
    mc "Someone broke our coop open. So the chickens escaped. I'm collecting them. Just move aside and I'll get her out of the way."
    eli "Thank you!"
    mc "Sure."
    sop "I should have known it was your fault!"
    eli "Honey, don't be rude."
    sop "Rude? This thing is a menace!"
    "You walk up to the chicken and calm it down. Once it has relaxed, you pick it up."
    mc "She's not a menace, she was just panicking and hungry."
    eli "Wow. You really know how to handle that."
    eli "Thank you for saving my garden, [MC]."
    mc "No problem."
    "Elise looks over her vegetables."
    eli "Well, it didn't do much damage. So that's good."
    eli "It's nice to see such a responsible young man like yourself nowadays."
    sop "Are you kidding, Mom?"
    sop "This was all his fault. And he's not even apologizing."
    eli "Sophie!"
    sop "What? All of this is his fault."
    mc "Look..."
    sop "If you're not apologizing, I'm not hearing it!"
    sop "Now I have nothing to wear for the party!"
    eli "What about your other..."
    sop "Hey! [MC]!"
    sop "What are you going to do to make up for it?"
    mc "{color=#b7b7b7}{i}Yep, that's Sophie all right. Single minded, shallow... and someone I can't believe I've had a crush on. What should I do?{/i}{/color}"
    hide elise
    show mc neutral at left
    show sophie neutral at right

menu SophieApology:
    "Apologize [gr]\[SophieApologized\]":
        hide mc
        show sophie neutral at slightleft
        show elise neutral at slightright
        mc "Fine. Sorry about your skirt, Sophie."
        sop "See, was that so hard?"
        mc "No."
        sop "Just... God... Weird shit always follows you."
        sop "I guess it didn't do too much damage... But you owe me one."
        $ SophieApologized = 1
        $ SophieLove += 0
        jump EliseSophieGarden2
    "Fuck that [gr]\[SophieLove +1\]":

        hide mc
        mc "Well, I guess I'll get going then."
        eli "Bye! Thank you for the help!"
        show sophie neutral at slightleft
        show elise neutral at slightright
        sop "Wait, you're not going to apologize?"
        mc "Look, it sucks about your skirt. But it's not like I let her out."
        mc "Plus. I'm not going say sorry just because you demand it."
        sop "You little..."
        mc "You want to boss someone around? That's what Toby's for."
        sop "Whatever."
        $ SophieLove += 1
        $ SophieApologized = 0
        jump EliseSophieGarden2

label EliseSophieGarden2:
    mc "See you later Elise."
    eli "See you. If you want. Come by sometime, I'll give you some vegetables."
    mc "Sounds good!"
    sop "Mom, why are inviting him over?"
    eli "Why not?"
    sop "It's just weird. He's like a complete loser, and if people see him coming over... they'll spread rumors."
    eli "You take these things way too seriously, Soph."
    sop "Whatever."
    mc "Goodbye you two."
    sop "Yeah. Get out of here. And don't forget, you owe me!"
    "Sophie storms off "
    hide sophie with moveoutleft
    show elise neutral at center with Dissolve(0.1)
    eli "Just ignore her. She's really not that bad..."
    eli "Most of the time."
    eli "She was in the middle of trying on her new outfit when she heard me screaming. So she ran right out."
    mc "Yeah. Look, [Nova] has a little concoction that gets dirt right out of your clothes."
    "You give Elise the recipe."
    eli "Thanks. It'd better get this to my daughter before she decides to murder someone."
    mc "Yeah. I gotta go too."
    eli "Good luck finding your other chickens!"
    scene farm fixed with Dissolve(2)
    "You take the chicken back home and return it to the coop."
    play sound chicken
    scene black with Dissolve(3)
    jump MiaPie
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
