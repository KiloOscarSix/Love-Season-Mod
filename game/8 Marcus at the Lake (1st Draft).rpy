label MarcusLake:
    "You turn to the opposite direction and begin looking around."
    play sound hit
    scene lake sunny with vpunch
    stop music
    "As you leave the glade, you bump into something. You trip and fall to the ground."
    '???' "OW!!!!"
    mc "{color=#b7b7b7}{i}What the hell was that?{/i}{/color}"
    show marcus neutral
    "You look up and see Marcus, an acquaintance of yours from town, on the ground next to you. "
    mar "What was that for?"
    "You stand up."
    mc "What? Where did you come from?"
    mar "I've been here the whole time."
    play music marcus
    mc "Bullshit. I was here with Mia and we didn't see you at all."
    mar "I know... She's quite the sight!"
    mc "So you saw everything?"
    mar "I will never divulge the secrets that my eyes have witnessed."
    mc "Uh huh."
    mar "I know not of what you speak, good sir."
    mc "How long were you spying on us, Marcus?"
    mar "Spying? I was on a personal quest... when I happened to see you two."
    mc "And you didn't say hello?"
    mar "Well, I saw you guys going into the glade... and I thought..."
    mc "You thought what?"
    mar "I might get another show."
    mc "Another?"
    mar "Um... I mean a show. The first... and only..."
    mc "Out with it."
    mar "Well, I might have followed Sophie and Toby out here one day..."
    mc "They did it in public?"
    mar "More like a small clearing..."
    mc "You're lucky they didn't see you!"
    mar "Yeah, well... I'm really good at hiding."
    mc "Yeah, how did you manage to hide from both me and Mia?"
    mar "Trade secret. I might tell you someday."
    mc "Yeah, ok."
    mc "{color=#b7b7b7}{i}Marcus is odd, as usual... I wonder if her really does have special skills?{/i}{/color}"
    mc "Well, you wasted your time though, no show for you."
    mar "Well, that wasn't why I came."
    mc "Why, then?"
    mar "I'm seeking a mermaid."
    mc "{color=#b7b7b7}{i}A mermaid... Could this be a coincidence?{/i}{/color}"
    mc "What are you talking about? What mermaid?"
    mar "I was out here a couple of days ago, and I was searching the woods around the lake..."
    mc "Sophie came up here again?"
    mar "No... Lisa."
    mc "You know if she caught you she'd LITERALLY stab you in the face, right?"
    mar "You want to hear the story or what?"
    mc "Yeah... Go ahead."
    "Marcus gets more excited as he talks."
    mar "Well, I lost track of her, and got a little turned around in the woods."
    mar "After a bit, I found a small path that lead towards the lake."
    mar "I followed it, and it lead to a little inlet that can't be seen from the other side."
    mar "When I got there, that's when I saw her... A dark haired beauty. Her back was to me, but she was naked from the waist up."
    mc "What happened, then?"
    mar "I tried to get closer, to see..."
    mar "But I screwed up, and stepped on a branch."
    mar "She turned around, and I ran away as fast as I could."
    mc "Yeah, but..."
    mar "I know... I just screwed up my hiding that time."
    mar "But I have to see her again."
    mc "Are you sure you just didn't catch someone skinny dipping?"
    mar "NO!"
    mc "And you want to see if one of the girls is bathing there again?"
    mar "I mean... It'd be nice. But I really saw a mermaid."
    mc "{color=#b7b7b7}{i}Marcus has always been a perv, I don't know if he's telling the truth or not.{/i}{/color}"
    mc "{color=#b7b7b7}{i}This is getting really weird, I dreamt about a mermaid, and now Marcus said he saw one... in this very lake.{/i}{/color}"
    mc "{color=#b7b7b7}{i}It's probably nothing... just an excuse to drag me into peeping.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Then again... peeping could be fun. And he could even be telling the truth.{/i}{/color}"
    mar "So, want to come along?"
    show mc neutral at left
    show marcus neutral at right

menu MarcusMermaidChoice:
    "Sure thing [gr]\[Marcus +1\] \[Corruption +1\] \[PeepedLake\]":
        hide mc
        hide marcus
        show marcus neutral
        mc "{color=#b7b7b7}{i}Well, peeping it is... Maybe on a mermaid.{/i}{/color}"
        mc "{color=#b7b7b7}{i}I have to see what's going on with this dream thing... I know they're supposed to be bad luck. But fuck it.{/i}{/color}"
        mc "Yeah. Lead the way!"
        mar "Awesome! You're the best!"
        $ MarcusFriend += 1
        $ Corruption += 1
        $ PeepedLake = 1
        jump LakeBath
    "Nah, it's a bad idea.":

        hide mc
        hide marcus
        show marcus neutral
        mc "Sorry, Marcus... I'm not going to risk getting caught to go peeping with you."
        mar "What, seriously?"
        mc "Look, it's not my game... ok?"
        mar "Fine... Just don't expect stories from me, later."
        mc "I'm sure I'll survive, somehow."
        "Marcus leaves you in the glade."
        $ MarcusFriend += 0
        $ Corruption += 0
        $ PeepedLake = 0
        jump MarcusLake2

label LakeBath:
    hide marcus
    stop music fadeout 3
    nvl clear
    scene forest_path with dissolve
    n "You follow Marcus through the woods until you eventually come across the path that leads to the inlet."
    n "Marcus wasn't wrong; at the end of this path, there is a perfect view of the area. You see a raven haired woman bathing in the lake ahead."
    play music dreaming
    n "\"{color=#b7b7b7}{i}Crap, is that the mermaid?{/i}{/color}\""
    n "You turn to look at Marcus, but he's nowhere to be seen."
    n "\"{color=#b7b7b7}{i}Perfect.{/i}{/color}\""
    n "You carefully step along the path, making sure to avoid any branches or animals that might be hiding nearby."
    mc "{color=#b7b7b7}{i}\"I need to see her to make sure.{/i}{/color}\""
    mc "\"{color=#b7b7b7}{i}If I just make it over to the edge there...{/i}{/color}\""
    "You make it to the edge, and look through the trees."
    scene brooke bath 1
    stop music fadeout 1
    "And it's most definitely not a mermaid."
    mc "{color=#b7b7b7}{i}I know her... I think that's Trevor's sister... Can't remember her name, though.{/i}{/color}"
    mc "{color=#b7b7b7}{i}I can't believe I got worked up over this. There are no mermaids in this lake... not really.{/i}{/color}"
    scene brooke bath 2
    mc "{color=#b7b7b7}{i}Well, at least this wasn't a total loss. She looks great!{/i}{/color}"
    "You spy on the girl for a little while, then slowly back away."
    mc "{color=#b7b7b7}{i}I should go... Don't want to push my luck.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Well, this will give me some good dreams in the future, at least.{/i}{/color}"
    mc "{color=#b7b7b7}{i}But where the fuck did Marcus get off to?{/i}{/color}"
    scene forest_path with dissolve
    "You follow the path back to the glade."
    scene forest path with vpunch
    play sound hit
    stop music
    mar "That was A-MA-ZING!"
    play music marcus fadein 1
    "You hear Marcus' voice come from behind you, and you scream in shock."
    mc "WHAAAA!"
    show marcus neutral
    mar "Oh, sorry to startle you."
    mc "Where the FUCK did you come from? I thought you left."
    mar "I was hiding."
    mc "Well, STOP!"
    mar "I did."
    mc "Yeah, yeah."
    mar "But what a sight! Did you see her tits? I just want to bury my head in them!"
    mc "One, yes, they were great. Two, that wasn't a mermaid, bro."
    mar "I know... But I know I saw one..."
    mc "You just saw her bathing man, that's all."
    mar "I guess you're right..."
    mc "I know I'm right."
    mar "These woods are the best place EVER for peeping."
    mar "I have to explore more."
    mc "Ok, buddy, you go do that. I'll see you around."
    hide marcus with dissolve
    "There is no response."
    mc "Marcus?"
    "You look around, and Marcus is nowhere to be seen."
    mc "Seriously?"
    jump MarcusLake2

label MarcusLake2:
    play music afternoon
    scene lake sunny with dissolve
    if PeepedLake == 0:
        mc "{color=#b7b7b7}{i}Well, this was an eventful trip. I can't believe I saw Mia's boob. I've never seen one in real life before.{/i}{/color}"
    else:
        mc "{color=#b7b7b7}{i}Well, this was an eventful trip. Saw more boobs in a day than I have... well, ever.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Unless you count [Nova]...{/i}{/color}"
    mc "{color=#b7b7b7}{i}WHICH I DON'T!{/i}{/color}"
    mc "{color=#b7b7b7}{i}Guess I should head home... It's getting late.{/i}{/color}"
    mc "{color=#b7b7b7}{i}However, I'm still short two chickens...{/i}{/color}"
    play sound chicken
    "You hear clucking nearby."
    mc "{color=#b7b7b7}{i}No way.{/i}{/color}"
    "You follow the sound and see one of your chickens sitting by the lake."
    show chicken:
        xalign 0.5 yalign 1.0
    mc "Well, I'll be damned."
    "You pick it up."
    mc "I can't believe I found you out here. What a lucky day!"
    play sound chicken
    "The chicken clucks happily."
    mc "If it wasn't for getting my hand burned... this would have been a good day, all things considered."
    play sound chicken
    "The chicken clucks again."
    mc "Yeah, it was a crazy fight. I would have had it... probably. Damn you, Trevor."
    hide chicken
    "You leave the lake and walk back home."
    scene black with Dissolve(3)
    jump Day1Dinner
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
