label MiaPie:
    nvl clear
    n "Once that is done, you decide that the next logical place to go for information would be the elder's house. Silas is known for being a fair leader in the village and a kind person overall."
    n "The elder's home is the center of activity in the village. If someone found one of the chickens and returned it, they would likely have gone there."
    n "You try not to think about the other reason you're looking forward to going visiting."
    hide window
    w ""
    scene village 1 day with dissolve
    nvl clear
    mc "{color=#b7b7b7}{i}If I'm lucky, Mia might be there.{/i}{/color}"
    "You make it to the elder's home and see him sitting outside."
    show elder neutral
    eld "Hello, [MC] any luck with the chickens?"
    mc "I was just coming by to tell you about it. Looks like you're already in the know."
    eld "Yes. Nina stopped by and I heard the whole story."
    mc "So, you wouldn't have seen any of them, would you?"
    eld "As a matter of fact, I did. I sent it back to your house with James and Lisa."
    mc "Wow! Thanks."
    eld "None needed. We have to look after each other. You would have done the same."
    "While you speak with the elder, his front door opens and an attractive busty young woman holding a basket appears."
    play music afternoon2 fadeout 1
    show elder neutral at slightright
    show mia neutral at slightleft
    mia "Oh! Um... Hello [MC]! How are you today?"
    mc "Oh, hi, Mia!"
    mc "I'm doing alright."
    show mia behind elder
    eld "He came looking for that chicken."
    show elder behind mia
    mia "Oh, right! I was so sorry to hear about what happened."
    mia "Have you found any of the others?"
    mc "A couple."
    "Mia smiles."
    show mia behind elder
    eld "Well, I'll leave you two to chat. I'll be inside if you need me."
    mc "Thanks again, sir."
    hide elder with easeoutright
    show mia neutral at center
    mia "So... what's... new?"
    mc "Besides the case of the runaway chickens? Not a whole lot. What's with the basket?"
    mia "The basket...?"
    mia "Ah, I'm planning to bake a pie!"
    mc "... In a basket?"
    "Mia blushes."
    mia blushing 1 "No... No... I'm using this to collect black berries. They're elder Silas' favorite."
    mia "I'm baking him a pie, to say \"thank you\" for looking after me all these years."
    mc "That's really sweet."
    mia blushing 2 "Thank you... but it's really nothing. I just like to make something every once in a while."
    mc "I can barely make toast without burning the house down, so baking a pie is really impressive!"
    mia neutral "No, not at all, it's not that hard. And it's not like I'm very good at it…"
    mc "I'm sure you're a great cook!"
    mia blushing 1 "I... I'm really not."
    mc "Where are you getting the berries? Has the new store opened yet?"
    mia neutral "No. These... Well, they're a little different, they are a bit hard to find and only grow by the woods."
    mia blushing 2 "Would you... Would you like to go with me? It'd be fun to hang out with someone there for a change…"
    mc "{color=#b7b7b7}{i}That kinda sounds like she's asking me on a date…{color=#b7b7b7}{i}"
    mc "{color=#b7b7b7}{i}Yeah, right! Still, it's nice to dream.{/i}{/color}"
    "Mia looks at you expectantly."
    mc "{color=#b7b7b7}{i}Oh right... I need to say something.{/i}{/color}"
    show mc neutral at left
    show mia blushing 2 at right

menu MiaDateChoice:
    "Sure!":

        hide mc
        show mia neutral at center
        mc "Absolutely!"
        mia smiling "Really? I mean... Great! Do you... want to head out now?"
        mc "It's so cute how she gets all excited about something so simple..."
        mc "Of course! Let's go!"
        $ MiaLove += 0
        jump MiaPie2
    "So I'm just \"Someone\"? [gr]\[MiaLove +1\]":

        hide mc
        hide mia
        show mia neutral at center
        mc "So, anyone will do? I'm not special.. Is that what you're saying?"
        show mia blushing 1
        "Mia looks down at the ground."
        mia blushing 2 "... Forget it, it was stupid to ask..."
        mc "I'm just messsing around Mia, I'd love to go with you!"
        "Mia flashes you a gigantic smile."
        mia smiling "Really? I mean... Great! Do you... want to head out now?"
        mc "Of course! Let's go."
        $ MiaLove += 1
        jump MiaPie2

label MiaPie2:
    stop ambient
    scene forest path with dissolve
    nvl clear
    n "You and Mia head into the woods near the lake. Mia is humming happily and nearly skipping the whole time."
    n "You catch yourself staring at her as she bounces along. Every once in a while she looks back at you, blushes then turns back to the path."
    mc "{color=#b7b7b7}{i}It's so cute how she gets all excited about something so simple...{/i}{/color}"
    "You search the woods for a while but you don't find any berries."
    show mia neutral
    mia neutral "Hey, [MC]... Would you mind going to the lake for a bit? There are usually berries out there."
    mc "Sure."
    "You folow the path through the woods to the lake. The sun is out but no one is here today. Outside of Mia... it's empty"
    show lake sunny with dissolve
    mc "Here we are!"
    scene mermaid intro with flashbulb
    hide window
    pause 3
    scene lake sunny with flashbulb
    mc "{color=#b7b7b7}{i}This reminds me of that dream. Well, it's really nice out. I doubt it's going to turn into a storm out of nowhere. No mermaid either.{/i}{/color}"
    show mia smiling
    mia "I love it out here... It's so quiet, but there are so many pretty flowers and trees."
    "Mia slips off and sniffs a nearby flower happily."
    mc "I've never seen you so energetic! You're all smiles now!"
    mia blushing 1 "I didn't look happy before?"
    mc "It's not that... But you just look really happy now."
    mia blushing 2 "Is it too much? I should stop."
    mc "No, don't! It's cool being able to talk to you like this. It's been a while."
    mia neutral "I guess being out here makes me feel like a little girl again. I'd love to swim out here, and eat the apples that fall to the ground."
    mia "But then one day one of the boys told me that he saw mermaids swimming in the lake. I was so scared I stayed away for a long time."
    mc "What an asshole!"
    mia "Well, he's not so bad..."
    mc "Oh come on, he was probably just being a jerk."
    "Mia smiles."
    mia "You really don't remember, do you? It was you."
    mc "Really? Wow... Sorry. I guess I forgot."
    mia "Well... I didn't. You were a little meanie sometimes."
    mc "It was a long time ago... and you know boys like to tease the girls that they..."
    "You stop yourself."
    mc "Never mind."
    mia smiling "The girls that they what?"
    "You brush it off."
    mc "It's nothing."
    mia "Come on! Finish what you were saying... Don't be a meanie again."
    mc "Don't worry about it."
    mc "So tell me more about these black berries. I've never had them before, and none of the farmers around here grow them, as far as I know."
    mia neutral "They can be tricky to find. I've only seen them growing in the wild, it must be hard to grow them on a farm or something..."
    mc "Still, I never noticed any black berries growing by the lake before."
    mia "Don't feel bad. I just spend a lot of time in these woods... by myself... so I learned a lot. I've seen some near the glade, so we should check there."
    mc "Cool, let's go there then!"
    scene mia walk 1 with dissolve
    "You walk to the glade with Mia."
    mc "{color=#b7b7b7}{i}Mia... She's gorgeous! But she seems so innocent. But here I am, just thinking about all the nasty things I want to do to her. What's wrong with me?{/i}{/color}"
    scene mia walk 2 with dissolve
    mia "Hm, these red berries smell so good! There's all sorts of other things that grow nearby too!"
    mc "Do you have a favorite?"
    scene lake sunny with dissolve
    show mia neutral
    mia "There are these blue daisies, do you know the ones I'm talking about?"
    mc "Yeah. I pick them up sometimes."
    mia "They're my favorite color! They are really pretty. They just sit there looking beautiful, but they don't outshine the other flowers either..."
    mc "I wish they weren't so hard to find."
    mia "Well, they don't live for very long after they bloom. But that just makes them special."
    show mc neutral at left
    show mia neutral at right

menu MiaFlowerChoice:
    "They remind me of you [gr]\[MiaLove +1\]":

        hide mc
        show mia neutral at center
        mia "Wait, you think I won't live for very long?"
        mia blushing 1 "I know I'm clumsy... but..."
        mc "Not like that! It's just... I was trying to give you a compliment!"
        mia smiling "Hm... I know, thanks [MC]! I was just kidding. Did I go too far?"
        mc "Who's the meanie now?"
        mia "He-he!"
        $ MiaLove += 1
        jump MiaPie3
    "They're nowhere near as pretty as you are.":

        hide mc with moveoutleft
        show mia blushing 2 at center
        "Mia blushes, but she looks a little uncomfortable at the direct compliment."
        mia "Stop being weird..."
        jump MiaPie3

label MiaPie3:
    mc "So, the berries are around here, you said?"
    scene mia walk 3 with dissolve
    mia "Yes! I'll look over here, you can search over there."
    mc "I got nothing here, did you find something?"
    mia "Nothing yet, but I think I saw one... just... here!"
    scene lake sunny with dissolve
    show mia smiling at slightleft
    pause .1
    show mia smiling at slightright
    pause .1
    show mia smiling at slightleft
    pause .1
    show mia smiling at slightright
    pause .1
    show mia smiling at center
    mia "I found it! I found it!"
    mc "Ha-ha! OK, OK, calm down!"
    mc "Damn, she's jumping so much that her breasts are almost..."
    mc "... popping out!"
    show mia walk 4
    "Mia smiles, oblivious to her current situation."
    mia "Victory! I told you I could find... Why are you looking at me like that?"
    "You try to find the words to tell her, but you can't."
    mia "Oh God! This is so embarrassing..."
    mc "S-sorry!"
    mc "{color=#b7b7b7}{i}She saw right through my face... I couldn't play it cool, damn. What did I say sorry for?{/i}{/color}"
    scene lake sunny with dissolve
    show mia blushing 1
    mia "It's not your fault..."
    mc "Well... I... These things happen, I guess. Let's just pretend nothing happened, OK?"
    mia "... OK... So here, you hold the basket then, and I'll pick the berries..."
    hide mia with easeoutright
    nvl clear
    n "The pair of you pick berries in silence."
    n "\"{color=#b7b7b7}{i}Mia isn't even looking at me. She will probably get over it after a while...\"{/i}{/color}"
    n "The situation feels more than a little awkward, but soon enough Mia starts flittering about the area, grabbing berries with a smile on her face."
    nvl clear
    show mia neutral with easeinleft
    mia "Perfect! This is more than enough now to bake my pie. I might even have extra! Should we head back?"
    mc "Well, you go ahead. I still need to find my chickens, and I haven't searched the whole lake yet."
    mia blushing 1 "I can help!"
    mc "It's fine. Just go home and bake your pie. I might be a while."
    mia "You're sure?"
    mc "Of course I am."
    mia smiling "Well, thank you for the company."
    mia "This was fun. It was nice to come out here with someone else."
    mc "You don't come here with your friends?"
    mia blushing 1 "I don't really hang out with the other girls much..."
    mc "I like hanging out with you, we should do this again!"
    mia smiling "I'd like that."
    mia "Well, um, the pie should be ready tomorrow. If you come back then, you could try some if you like."
    mc "Sure!"
    mia "Just remember I'm not very good at it, so you might not like it..."
    mc "I'm sure it'll be great!"
    hide mia with moveoutleft
    "Mia waves goodbye and leaves you at the lake."
    jump MarcusLake
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
