label Day2Start:
    "You toss and turn at night."
    play music dreaming
    play sound thunderdistant
    play ambient rainforest
    scene lake rainy with flashbulb
    "You dream again; the images are familiar and haunting."
    play sound thunderloud
    show mer neutral with flashbulb
    mc "Bad luck..."
    play sound thunderloud
    show selena dream 2 with flashbulb
    sel "What do you want?"
    scene black with Dissolve(2)
    show mia neutral with flashbulb
    pause 1
    sel "Innocence?"
    hide mia neutral with dissolve
    pause .5
    show sophie neutral with flashbulb
    pause 1
    sel "Liberation?"
    hide sophie neutral with dissolve
    pause .5
    show evelyn neutral with flashbulb
    pause 1
    sel "Understanding?"
    hide evelyn
    pause .5
    show nova neutral with flashbulb
    pause 1
    sel "Adventure?"
    hide nova neutral with dissolve
    pause .5
    show nina neutral with flashbulb
    pause 1
    sel "Friendship?"
    hide nina neutral with dissolve
    pause .5
    sel "Why choose? They can all be yours... And many more... Fulfill your potential..."
    "You wake up in a sweat."
    stop ambient fadeout 1
    show farm bedroom with Dissolve(3)
    play music morninghappy
    show nova bed neutral
    nov "Well, good morning to you too, [MC]"
    nov "Did I startle you?"
    "You take a moment to get your bearings."
    mc "I... Uh, yeah."
    nov "Well, breakfast is on the table. Redd wants us outside ASAP."
    mc "Right."
    nov "I'm going to go change."
    hide nova with easeoutleft
    scene farm house interior with Dissolve(2)
    "You get dressed and grab breakfast. By the time you're done, [Nova] is waiting for you."
    show nova neutral
    nov "Let's go."
    show farm_fixed behind nova with Dissolve(2)
    "The two of you walk outside; Redd is waiting."
    show nova neutral at slightright
    show father neutral at slightleft
    dad "Good morning!"
    dad "You're up on time... I assume we can thank [Nova] for that."
    nov "You got that right."
    mc "You should be surprised she's up. She usually sleeps in more than I do."
    dad "You have a point, son."
    nov "Maybe. But I still do more work around here than you do."
    dad "She also has a point, son."
    nov smirk "Hah!"
    "[Nova] sticks her tongue out at you."
    dad "Ok, let's get serious. Today we need to till the fields and get them ready for planting tomorrow."
    dad "But first I'll be fixing the doors to the barn. I don't want another repeat of last night. I'll need your help."
    "You shrug."
    mc "Well, the sooner we start, the sooner we're done."
    dad "That's the spirit."
    play ambient fixing
    scene barn day with Dissolve(2)
    show nova neutral at slightleft
    show father neutral at slightright
    "You, Redd and [Nova] begin working on the barn."
    dad "This is in worse shape than I thought."
    mc "Well, it's almost as old as I am."
    dad "Yeah. I'm looking around here, and there are lots of beams that have to be replaced."
    nov "To say the least."
    dad "I don't have enough wood to fix this."
    dad "I'll go cut some down; that will save me some money with Darius."
    dad "We'll leave most of the work for tomorrow. You two clean up here, and get to work on the fields."
    dad "Can you two handle that?"
    nov "Absolutely, Redd."
    mc "What she said."
    dad "Glad to hear it!"
    hide father with moveoutright
    "Redd leaves for the forest."
    stop ambient
    show nova neutral at center with dissolve
    nov "Come on, let's clean up."
    mc "We could always just slack off."
    nov "No way! If we work together... we can get this place cleaned in no time."
    mc "Ok, ok."
    "You and [Nova] spend the next couple of hours cleaning the barn."
    nov "So she invited you over for pie?"
    mc "Yeah."
    nov "And you're here cleaning, why?"
    mc "Because we've got work to do?"
    nov smirk "If I were you I would have snuck off."
    mc "It's tempting. But you were right... I don't want to deal with dad if we don't finish this."
    mc "Plus working with you isn't so bad..."
    nov neutral "Quite the endorsement."
    mc "You know what I mean."
    scene black with Dissolve(2)
    "The two of you finish cleaning."
    scene farm fixed with Dissolve(2)
    show nova neutral
    mc "Well, that's done. Time to till the fields. Whee."
    nov "It'll go fast... Trust me."
    "You and [Nova] head to the field and get to work."
    mc "I don't know how dad loves this so much."
    nov "I think it just suits him."
    mc "I guess. Boring monotonous work."
    nov "Well, without us... a lot of people here wouldn't be able to eat."
    mc "There are other farms."
    nov "Right, but they're all for delivery to the city, we supplement the whole town."
    mc "You really follow all of this don't you?"
    nov "Yeah. I do like the work... even if I like sleeping in just a little bit more."
    mc "I get that... I guess."
    "After a while..."
    nov smirk "So... Are you taking anyone to the party?"
    mc "What, no... Just going stag, I guess."
    nov "See, that's your problem. You're cute, but you come off as lazy."
    mc "What? I mean..."
    nov "Girls like a guy who's active. You're clearly not even trying. It shows."
    nov neutral "Look, isn't there anyone in town you're interested in?"
    mc "Uh..."
    show mc neutral at left
    show nova neutral at right
menu InterestedMenu:
    "Mia [gr]\[MiaLike\]":

        hide mc with moveoutleft
        show nova neutral at center
        mc "Well, Mia's really sweet. And she's hot, too."
        nov tease "You like the milk jugs... I get it."
        "[Nova] sighs."
        nov "I think she might be a bit of a challenge, though."
        nov smirk "I don't think she's let a lot of people taste her pie."
        nov "Probably no one."
        mc "You're not letting that pie thing go, are you?"
        $ MCMiaLike = 1
        jump Day2Start2
    "Evelyn [gr]\[EvelynLike\]":

        hide mc with moveoutleft
        show nova neutral at center
        mc "Evelyn seems really down to earth."
        nov smirk "And her tight pants don't hurt either, right?"
        mc "Right."
        nov "I know you too well."
        nov "Well, good luck there."
        $ MCEvelynLike = 1
        jump Day2Start2
    "Sophie [gr]\[SophieLike\]":

        hide mc with moveoutleft
        show nova neutral at center
        mc "I mean, Sophie is smoking hot!"
        nov "She'd eat you alive."
        mc "What do you..."
        nov "Look, I know you're still not over her breaking your heart..."
        mc "That was a long time ago."
        nov "She shot you down hard."
        mc "Yeah, I know."
        nov smirk "Plus, her boyfriend could whoop you."
        mc "I know."
        nov "Also, she's a bitch."
        mc "Trust me, I know that firsthand."
        nov neutral "So why?"
        mc "She's really, really hot."
        "[Nova] laughs."
        nov smirk "At least you're honest."
        $ MCSophieLike = 1
        jump Day2Start2
    "Nina [gr]\[NinaLike\]":

        hide mc with moveoutleft
        show nova neutral at center
        mc "Nina."
        nov "Pull the other one."
        mc "What?"
        nov "If you were interested in her... no way you would admit it."
        mc "Why?"
        nov "Because then you'd be admitting you fucked up when she got with Trevor."
        nov "Plus, she's more like a sister to you, right?"
        mc "YOU'RE like a sister to me."
        nov "Exactly."
        $ MCNinaLike = 1
        jump Day2Start2
    "[Nova] [gr]\[NovaLike\]":

        hide mc with moveoutleft
        show nova neutral at center
        mc "Well, we could always just become a couple ourselves."
        nov "Wow! I've been waiting for you to say that."
        nov smirk "Come on! To the bedroom, we need to consummate this now!"
        mc "WHAT?"
        nov "Gotcha! Hah, you forget that I can joke around too."
        $ MCNovaLike = 1
        jump Day2Start2

label Day2Start2:
    show nova neutral
    nov "Here's the thing. It doesn't matter who you're interested in if you don't DO anything about it."
    mc "It's not like I can just walk up to someone and say \"Hey! Wanna fuck?\""
    nov "Oh god! Please do! I want to see that reaction!"
    mc "You know what I mean."
    nov "Yes, I do. But you're looking at it the wrong way."
    nov "You need to get some experience under your belt."
    mc "Wow! Why didn't I think of that?"
    nov "I meant dating."
    if MCMiaLike == 1:
        nov "Look, you already said you liked her."
    nov "So, like, why don't you ask Mia to the party?"
    mc "She's not a party kind of girl."
    nov "Maybe not... But she's into you."
    mc "How do you know that?"
    nov "She invited you back to her house to..."
    mc "Will you drop the pie thing?"
    nov "Some girls just need to come up with an excuse."
    mc "Ok... Fine... If it was anyone else. But this is Mia."
    nov "Yeah, it's Mia. She's not asking you to go diving for clams... But come on... She's into you."
    nov "Plus she's low risk."
    mc "What do you mean, low risk?"
    nov "She probably won't say no. I mean, if you asked someone like Brooke or Sophie, you'd be just asking to be crushed."
    mc "I wasn't going to ask them. I barely even know Brooke."
    nov "That's not the point."
    mc "Well, I have to finish it here, anyway."
    nov "Look, I can take care of the rest. Go to Mia, try the pie. Ask her to the party."
    if MCMiaLike == 0:
        mc "I mean, she's cute, but..."
        nov "But what? You're asking her out to a party, not exchanging promise wreaths."
        nov "You won't be attached at the hip."
        nov "Plus, it'll look better to the other girls if you show up with someone."
    nov "You really don't have anything to lose."
    mc "You'll finish it up here?"
    nov "I said I would. Now go."
    mc "Ok, thanks."
    nov "Good luck."
    "You leave [Nova] working in the fields and head to Mia's house."
    jump Day2MiaPieTasting
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
