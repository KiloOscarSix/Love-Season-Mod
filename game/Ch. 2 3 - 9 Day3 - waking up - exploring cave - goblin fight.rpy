
label StartDay3:
    scene black with Dissolve(4)
    play ambient caverain fadein 1
    play ambient2 fire fadein 1
    play music nina1 fadein 1
    "You wake up to the sound of rain. You're surprisingly warm this morning."
    mc "I... Oww..."
    mc "{i}My arm hurts...{/i}"
    "Those were the first thoughts that entered your head as you woke from your sleep."
    mc "{i}Something's on top of it...{/i}"

    hide window
    scene cave morning 1 with Dissolve(2)
    w ""
    mc "{i}Wait... Nina? Naked?{/i}"
    mc "{i}What the hell? Why are we...{/i}"
    "Memories of the previous night flood your mind."
    mc "Oh, Right..."
    "You look over to the cave entrance."
    mc "The storm's still going? Well, at least it's not as cold as it was last night..."
    "Nina stirs and hugs you closer."
    mc "She..."

    hide window
    scene cave morning 2 with Dissolve(2)
    w ""
    mc "{i}Oh, this isn't...{/i}"
    "You feel Nina's stomach rubbing against your cock, which is, as always in the mornings, quite erect."
    mc "{i}She's so warm... and she's...{/i}"
    mc "{i}Not the time! Just... let me get up and check the fire...{/i}"
    "You try to roll away from Nina, but she grabs on to you and hugs you tightly."
    mc "{i}Well... Ok, let me try to...{/i}"
    "You try to slip your arm out from under Nina."
    "She stirs."
    nin "Huh?"

    hide window
    scene cave morning 3 with Dissolve(2)
    w ""
    "Nina blinks and opens her eyes. She hums as she shifts her stomach and presses into you."
    nin "[MC]... That was such a weird dream... You saved me..."
    mc "Uh... Good morning."
    nin "Good... Wait a second!"
    nin "How did we end up like this? What are you doing?"
    mc "Nothing! I just woke up! We must have shifted during the night..."
    nin "I... guess that makes sense."
    mc "At least we're warm."
    nin "Did the storm stop?"
    mc "Nope. Still going strong. It doesn't seem as cold today, though."
    nin "You're pretty warm. But yeah... the cave seems warmer too."
    "Nina moves to get up and rubs her stomach against your crotch as she does so."
    mc "{i}Please don't do that again... Or do... It felt great, but this is not the time...{/i}"
    "Nina pauses."
    hide window
    scene cave morning 3-2 with Dissolve(2)
    w ""
    nin "Wait... What's poking me?"
    mc "Uh..."
    hide window
    scene cave morning 3-3 with Dissolve(1)
    w ""
    nin "Oh my god!"
    "Nina pushes herself away and stands up as fast as she can."
    scene cave campsite with Dissolve(2)
    show nina topless covering with dissolve
    nin "What's wrong with you? What were you doing?"
    mc "Nina, relax, it's..."
    show mc underwear neutral at left with Dissolve(0.1)
    show nina topless covering at farright

menu NinaHardOn:
    "I can't control it.":
        hide mc
        show nina topless at center with Dissolve(0.5)
        mc "I'm sorry, it looks like it happens in the mornings even in survival situations..."
        mc "It doesn't mean anything."
        nin "I-I guess you're right, but..."
        mc "It's not like I can control it... Nothing to do with your boobs, I swear!"
        nin "My? Oh, crap!"
        show nina topless covering with Dissolve(0.1)
        mc "Sorry!"
        jump HardOnTalk
    "[gr]I'm sleeping next to a naked girl...":

        hide mc
        show nina topless at center with Dissolve(0.5)
        mc "What do you expect to happen? I wake up snuggling up to a cute girl."
        mc "Dressed like you are... How am I NOT supposed to get hard?"
        nin "Dressed like..."
        nin "Oh! Right..."
        show nina topless covering with Dissolve(0.2)
        "Nina covers her breasts."
        if NinaLove > 2:
            nin topless covering "I'm... I just didn't think it would be a problem."
            mc "I know, I didn't either, but..."
            nin "What is it with you saying stuff like that lately?"
            nin "You're being so weird..."
            mc "I'm just-"
            nin "So... Can you maybe handle it... or something?"
            "Nina catches herself staring at your hard on."
            $ NinaLove += 1
            jump HardOnTalk
        else:
            nin "I guess it'll happen even with someone like me..."
            nin "Does it weird you out?"
            show mc underwear neutral at left with Dissolve(0.1)
            show nina topless covering at farright
            jump WeirdMenu

menu WeirdMenu:
    "A little bit.":
        hide mc
        show nina topless covering at center with Dissolve(0.5)
        mc "I mean... a bit. We've been friends for so long... It's strange thinking of you that way sometimes."
        nin "Hm... OK."
        mc "Don't read too much into it, OK?"
        nin "I won't. It's just a natural thing."
        mc "Exactly."
        jump HardOnTalk
    "No, it doesn't [gr]\[NinaLove +1\]":

        hide mc
        show nina topless covering at center with Dissolve(0.5)
        mc "It's a little strange, but it doesn't bother me. You look good. What else can I say?."
        nin "Different stuff."
        mc "What do you mean?"
        nin "Stuff that isn't... I don't know... wrong coming from you."
        mc "I know..."
        nin "Because we're friends. It's not normal... right?"
        mc "Yeah, just... friends. Forget I said anything, OK?"
        nin "No... I mean. It's nice to hear..."
        mc "I'll never do it again."
        nin "I mean, never's a long time. It wasn't bad to hear, I just got caught off guard."
        mc "So... More compliments or less?"
        nin "Just... Let me take the compliment and move on."
        $ NinaLove += 1

label HardOnTalk:
    "You follow Nina's gaze down to your erection."
    nin "Isn't that uncomfortable?"
    mc "Uh... Sometimes."
    "Nina catches herself staring and looks away, blushing."
    nin "Shit! Sorry..."
    mc "It's ok. I was kinda staring at your boobs earlier. Fair play."
    nin "Did you just... You really have no game at all, do you?"
    "Nina laughs."
    mc "I was just trying to make you feel better."
    show nina topless with dissolve
    nin "It... worked. So thank you."
    mc "You're welcome."
    "Nina looks down at you again."
    mc "Do you just want me to pull it out at this point? You're starting to make me feel self-conscious."
    show nina topless covering with dissolve
    nin "No."
    "Nina looks away."
    nin "How about we get dressed so we don't have to stare."
    mc "{i}Have to?{/i}"
    "Nina walks over to where you both set out your clothes to dry."
    nin "They're still soaked... Damn it."
    mc "Oh... What happened?"
    nin "I don't know. We kept them by the fire..."
    "You look at the ground."
    mc "Oh... Wow."
    nin "What?"
    mc "Looks like they soaked up some of the water coming in from the outside."
    nin "Damn it!"
    mc "Well, on the bright side, it stopped the water from getting to the fire... or us. Kind of like a dam."
    nin "So what are we supposed to do now?"
    mc "Well, I don't know why, but the cave seems a lot warmer now... Especially compared to last night."
    nin "You're right. I mean the fire's still going, but I don't feel like my nipples are going to break off."
    mc "{i}Thanks, Nina... Because why not make it harder to ignore your tits?{/i}"
    mc "..."
    show nina topless covering with dissolve
    nin "You're staring again."
    mc "Sorry!"
    nin "I wish I just had a shirt or something."
    mc "Hold on... Maybe there is something by that old cart."
    "You go back to the cart and look around the area."
    nin "Actually, I have a better idea."
    hide nina with Dissolve(1)
    play sound walkgrass
    "Nina walks behind you and picks something up off the ground."
    nin "Think this might just be big enough..."
    nin "I'm gonna borrow this."
    mc "Borrow what?"
    play sound clothes

    hide window
    scene cave morning 4 with Dissolve(2)
    w ""
    "You turn to see that Nina has grabbed your scarf and is wrapping it around her chest. She struggles as she tries to tie a knot in the back."

menu HelpTie:
    "Offer to help her. [gr]\[NinaLove +1\]":
        mc "Here, let me help you with that."
        "Nina blushes and nods."
        nin "Ok..."

        hide window
        scene cave morning 5 with Dissolve(2)
        w ""
        "You walk around behind her and tie a knot with the ends of the bandana."
        mc "Is that tight enough?"
        nin "Yeah, perfect. Thanks!"
        $ NinaLove += 1
        jump Explore
    "Watch her struggle":

        nin "Damn it. How am I supposed to do this?"
        mc "Is it too small?"
        nin "No, it's fine... But I think we'd be in trouble if I was built like Laura."
        mc "Maybe if you tie it around the front and then turn it around?"
        nin "You're just trying to see my tits again, aren't you?"
        mc "Maybe. Doesn't make it a bad idea, though."
        nin "Well, it's not like you haven't seen them like a thousand times already. And it should work..."

        hide window
        scene cave morning 6 with Dissolve(2)
        w ""
        "Nina puts the top on backwards and ties the knot just above her tits, giving you a perfect view."
        mc "{i}Don't stare. Do not... stare.{/i}"
        "She then turns her top around so the knot is on her back and the loose fabric covers her breasts."
        nin "That wasn't so hard!"
        jump Explore

label Explore:
    scene cave campsite with Dissolve(2)
    show nina scarf smiling with Dissolve(0.5)
    nin scarf smiling "So, how do I look?"
    mc "That's really..."
    "Your words catch in your throat."
    nin scarf worried "What? Is it not covering right?"
    mc "No! It's just..."
    mc "Sexy."
    "Nina blushes."
    mc "{i}I said that out loud, didn't I?{/i}"
    nin "Um... Thanks I guess, but I'm not going for that."
    mc "Doesn't matter."
    if NinaLove <= 2:
        show nina scarf smiling with Dissolve(0.5)
        nin "I think this whole situation has you delirious."
        mc "Yeah, you're probably right..."
    show nina scarf neutral with Dissolve(0.5)
    nin scarf neutral "So... We've got some time until our clothes are dry."
    mc "And that's assuming this storm ever stops."
    nin "It has to eventually, right?"
    mc "Unless it's a repeat of Kya's Flood we're probably safe."
    nin "So we're safe, but stuck."
    mc "Pretty much."
    nin "Um, so any of that survival knowledge of yours let you know where to find water?"
    mc "Now that you mention it, yeah. A lot of caves around here have underground springs."
    mc "There could be monsters in there."
    nin "Are you scared? Don't worry... I'll protect you if anything happens."
    nin "Come on! It's better we know what's around us than not, right?"
    mc "I don't know, I'm tired... Let's just relax here."
    nin "We just got up!"
    mc "You had a pillow, I had my arm crushed into the stone floor by a heavy-"
    nin scarf worried "Heavy?"
    mc "I... Shit, I didn't mean it."
    show nina scarf neutral with Dissolve(0.2)
    nin "So do I kick your butt for being insensitive, or will you come along with me?"
    mc "This is extortion."
    show nina scarf smiling with Dissolve(0.2)
    nin "Yes, it is. You have no one to blame but yourself."
    mc "Let's go then."
    nin scarf smiling "It'll be fun!"
    mc "You're right. Just because we're stuck here... it doesn't mean it has to suck."
    nin "Exactly."
    jump Explore2

label Explore2:
    scene cave paths with Dissolve(2)
    stop ambient fadeout 1
    stop ambient2 fadeout 1
    hide window
    w ""
    nvl clear
    n "You and Nina explore the area around your makeshift camp. There are three pathways into the cavern, not counting the way you came in."
    n "You feel a warm breeze coming from the pathway to the right."
    n "You hear what sounds like running water coming from the pathway to the left."
    n "You hear silence coming from the pathway in the middle."
    nin "So which way should we go?"

menu CaveEntrance:

    "Go to the right" if CrystalCave == 0:
        jump CrystalCave1

    "Go to the left" if Lake == 0:
        jump Lake1

    "Go down the middle" if Mushrooms == 0:
        jump Mushrooms1

label CrystalCave1:
    scene cave passage with Dissolve(2)
    play music mysterious fadein 1
    "You and Nina take the pathway to the right."
    mc "This whole thing is funny when I think about it."
    nin "What is?"
    mc "I thought I might wake up with a hangover today. Instead I wake up in a cave in my underwear."
    mc "Though I guess waking up in a cave WITH a hangover, that would be in the cards. So not that crazy."
    show nina scarf neutral with Dissolve(0.1)
    nin "Well... I don't know what I expected, but waking up next to you... Definitely not the plan."
    mc "Jeez... Harsh."
    nin "But I think Laura would say that waking up naked next to a boy just meant it was a good night. So not that crazy, either."
    if FuckedLaura == 1:
        mc "As for Laura... I don't think she's the \"wake up next to a guy type.\" More the \"push you out the door and hope you didn't leave your underwear there\" type."
        show nina scarf suspicious with Dissolve(0.1)
        nin "And just how would you know that?"
        mc "I wouldn't... just..."
        show nina scarf surprised with Dissolve(0.1)
        nin "Goddess! That {i}was{/i} her perfume I smelled. You hooked up with her!"
        mc "What? No! That's crazy talk!"
        show nina scarf neutral with Dissolve(0.1)
        nin "... spill."
        mc "Nothing happened."
        nin "You know she'll tell me later."
        mc "Ok, yeah, she probably will."
        show nina scarf smiling with Dissolve(0.1)
        nin "You are such a dog!"
        mc "Hold on! You were TRYING to hook us up!"
        show nina scarf neutral with Dissolve(0.1)
        nin "I thought you guys would get along."
        mc "Well... Mission accomplished. We got along really really well. How does that make me a dog?"
        show nina scarf suspicious with Dissolve(0.1)
        nin "Anyway, that went out the door when I found out you came to the party with Mia. Though I suppose Laura didn't get that raven."
        mc "Ok, point. But it wasn't exactly a date."
        nin "Whatever it was, you still ended up getting together with Laura."
        mc "Also point. In my defense, I didn't ditch Mia or anything. I even took her home. Laura happened after."
        show nina scarf angry with Dissolve(0.1)
        nin "Still a dog. My opinion hasn't changed."
    else:
        mc "She's a wild one for sure."
        show nina scarf suspicious with Dissolve(0.1)
        nin "Wait... Did something happen?"
        mc "After that smooth move you made to hook us up? Sorry to disappont, but no, not really."
        show nina scarf neutral with Dissolve(0.1)
        nin "You should have made a move. That's your problem."
        mc "I was already on a date with Mia. Kind of."
        nin "How did that go?"
        nin "You probably didn't even get a kiss on the cheek."
        mc "Yes I did, thank you. It went fine. She's just shy."
        show nina scarf smiling with Dissolve(0.1)
        nin "Well, I like her. She's really sweet."
        mc "But?"
        show nina scarf suspicious with Dissolve(0.1)
        nin "No buts."
        mc "Uh huh..."
        nin "I said she's nice."
        "You look at Nina with exasperation."
        show nina scarf surprised with Dissolve(0.1)
        nin "What?"
    hide nina with dissolve
    "A little while later..."
    play sound walkgrass
    mc "Is it getting hot in here? Because I'm sweating like crazy."
    show nina scarf neutral with Dissolve(0.1)
    nin "It's not just you..."
    mc "Well, I'm not complaining. After last night... this is a welcome change."
    nin "But what's keeping us warm?"
    mc "I think that just might answer your question."
    scene cave crystal 1 with Dissolve(2)
    play music dreaming fadein 1
    "You and Nina enter a chamber filled with glowing red crystals."
    hide window
    w ""
    mc "Whoa!"
    show nina scarf surprised with Dissolve(0.5)
    nin "Are these...?"
    mc "Fire crystals. Big ones."
    "Nina reaches out to touch one of the large crystals. As she does, she quickly pulls her hand back."
    nin "Ow! That's really hot."
    mc "You ok?"
    show nina scarf worried with Dissolve(0.1)
    nin "I nearly burned myself..."
    if Lake == 1:
        mc "These crystals seem to be warming up the entire cave right now. Even the lake."
    "The crystals grow brighter and dimmer, as if they were pulsing in sync with an unknown force. It's as if the cave has its own heartbeat."
    mc "I've never heard of anything like this before. They get warm... But..."
    show nina scarf neutral with Dissolve(0.1)
    nin "Me neither, but I don't know much about fire cyrstals."
    mc "I can feel the energy build up here... It's crazy."
    scene cave crystal 2 with Dissolve(2)
    show nina scarf neutral with Dissolve(0.1)
    "You head further into the chamber."
    mc "And it's in all of them..."
    nin "Well, at least we know what's warming up the cave."
    mc "Yeah. But..."
    nin "What is it?"
    mc "I was just thinking about something the Elder once said in class."
    show nina scarf smiling with Dissolve(0.1)
    nin "You did something in class other than sleep?"
    mc "Yeah, I liked his magic talks."
    nin "So?"
    mc "Right... So elemental crystals absorb and amplify the natural mana in the area. Caves like this are full of it. "
    show nina scarf suspicious with Dissolve(0.1)
    nin "So are they supposed to be glowing like this all the time?"
    mc "I don't think so. Usually they give off some light, but this... is different."
    nin "On the other hand... these things are nice and warm. Maybe we should stay here tonight?"
    mc "I wouldn't."
    nin "Why not?"
    mc "Fire crystals are volatile normally. You saw how I lit the fire just by throwing it hard... And that crystal was tiny."
    mc "These look like they're ready to burst... And if they do... I don't want to be here. Do you?"
    show nina scarf worried with Dissolve(0.1)
    nin "No."
    mc "Me neither."
    "You explore the crystal cave a little more, but don't see anything else of note."
    if Lake == 1 and Mushrooms == 1:
        mc "Guess that's it. Or at least the immediate area."
        nin "Yeah, I don't think going deeper is a good idea."
        nin "So..."
        mc "You want to go take that bath, don't you?"
        show nina scarf smiling with Dissolve(0.1)
        nin "Well, duh!"
        mc "So go. I'll stay around here, unless you need some help with the back scrubbing..."
        show nina scarf neutral with Dissolve(0.1)
        nin "I'm good, thank you. I think you've seen my boobs enough for one lifetime."
        mc "There are never enough boobs."
        nin "Well, we could do that... Or instead your pervy butt could go get some mushrooms. I'll try to cook them up when I'm done."
        mc "Boobs vs Food, the eternal debate."
        show nina scarf laughing with Dissolve(0.1)
        nin "Just go already."
        "You grab a few small fire crystals and head back to the main cave with Nina. From there she leaves to bathe."
        $ CrystalCave == 1
        jump NinaCampTrouble
    nin "We should head back..."
    mc "I'm going to grab a couple of these tiny ones, it can't hurt to be prepared."
    nin "Good idea."
    "You grab a few smaller fire crystals. They are hot to the touch, but not enough to burn your hand."
    nin "Ok... Let's go."
    "You and Nina make more small talk as you return to the forked entrance chamber."
    $ CrystalCave = 1
    stop music fadeout 1
    play sound walkgrass
    scene cave paths with Dissolve(2)
    jump CaveEntrance

label Lake1:
    play music mysterious fadein 1
    scene cave passage with Dissolve(2)
    "You and Nina walk down the left pathway."
    show nina scarf neutral with Dissolve(0.1)
    nin "We kind of lucked out here with these glowing bits of the wall..."
    mc "Yeah... Without them this would be a nightmare."
    nin "Can you imagine? Cold, no fire... and total darkness."
    mc "At least the company would still be good."
    show nina scarf smiling with Dissolve(0.1)
    "Nina smiles."
    nin "There are worse people to be stuck with..."
    mc "I try."
    "As you and Nina walk through the pathway you notice a small chamber off to the right."
    mc "Huh..."
    nin "What is it?"
    mc "Another abandoned camp."
    show nina scarf suspicious with Dissolve(0.1)
    nin "From the old miners?"
    mc "Probably. With all the light in this cave it'd be easy to work late into the night and leave in the morning to head to the city."
    nin "But ever since the monster sightings increased..."
    mc "Yeah... No one bothers anymore."
    show nina scarf neutral with Dissolve(0.1)
    nin "Well, the place is empty. Let's keep going."
    "You and Nina follow the passage further until your come upon a pool of water."
    hide window
    scene cave indoor pool with Dissolve(2)
    w ""
    play music romance2 fadein 1
    mc "Well this is lucky."
    show nina scarf neutral with Dissolve(0.1)
    nin "Wow... It's huge."
    mc "That's what she said!"
    show nina scarf angry with Dissolve(0.1)
    "Nina smacks you on the back of the head."
    nin "Stupid! I meant the lake."
    mc "You're so violent! I don't know how Trevor puts up with you."
    nin "I'm only violent with you."
    mc "OK then. I don't know how {i}I{/i} put up with you."
    show nina scarf smiling with Dissolve(0.1)
    nin "Because you love me... That's why."
    mc "After getting socked in the head, I'm not so sure about that."
    show nina scarf angry with Dissolve(0.1)
    nin "I didn't even hit you that hard, you big baby."
    mc "You broke something. I'm sure of it."
    nin "Keep it up and I just might."
    "Nina walks to the edge of the lake."
    show nina scarf neutral with Dissolve(0.1)
    nin "Even in this light the water looks really clear."
    mc "A lot of these underground lakes are essentially big wells. The water gets filtered by the stones."
    nin "So is it safe to drink?"
    mc "Probably..."
    "Nina puts her hand in the water."
    nin "It's... warm?"
    if CrystalCave == 1:
        mc "The fire crystals. Has to be."
    show nina scarf smiling with Dissolve(0.1)
    nin "This makes me want to just jump in and relax. Get all this dirt off of me."
    mc "A bath, right now?"
    nin "I feel gross. We're covered up in dirt and other crap. We slept on a dusty old tarp..."
    nin "So yes, washing up would be great."
    mc "Well, don't let me stop you."
    nin "Maybe once we've finished exploring the cave."
    if Mushrooms == 1 and CrystalCave == 1:

        mc "We're basically done now, so go ahead."
        show nina scarf neutral with Dissolve(0.1)
        nin "Alright then... Why don't you go and get some mushrooms so we have something to eat tonight? I'll wash up in the meantime."
        mc "Well, how about I help you take that bath, and we go get mushrooms together?"
        show nina scarf angry with Dissolve(0.1)
        nin "Very funny. I think you've seen my boobs enough for one day. Now go, I'll meet up with you at the camp, then you can clean up while I cook up the mushrooms."
        mc "Boobs? Enough? Heresy.{w} But alright, have your bath. See you at camp."
        $ Lake += 1
        jump NinaCampTrouble

    mc "We should hurry then, seeing as you're all gross and stuff."
    show nina scarf angry with Dissolve(0.1)
    nin "Hey!"
    mc "You're the one who said it."
    nin "You're not supposed to agree."
    mc "I calls it as I sees it."
    show nina scarf neutral with Dissolve(0.1)
    nin "Like you're one to talk!"
    mc "I'm not gross, I'm ruggedly filthy."
    nin "I'll give you the filthy."
    play sound walkgrass
    scene black with Dissolve(2)
    nin "And now your filthy outside matches your filthy mind."
    "You and Nina walk back to the forked chamber."
    $ Lake += 1
    scene cave paths with Dissolve(2)
    stop music fadeout 1
    jump CaveEntrance

label Mushrooms1:
    play music nina2 fadein 1
    scene cave passage with Dissolve(2)
    "You take the center pathway and Nina follows you. The pathway goes on for quite some time."
    mc "This cave... I wonder how deep it goes?"
    show nina scarf neutral with Dissolve(0.1)
    nin "I don't know, it seems like we've been walking for a long time."
    mc "Yeah..."
    nin "Do you think it's dangerous to walk this far away from the camp?"
    mc "I don't think so. Despite everything, I have a good feeling about going in this direction..."
    show nina scarf suspicious with Dissolve(0.1)
    nin "A good feeling? That's it?"
    mc "Yeah..."
    nin "Well, {i}that{/i} makes me feel safer now."
    mc "Nothing's tried to kill us so far. Trust me."
    if NinaLove >= 2:
        show nina scarf smiling with Dissolve(0.1)
        nin "Ok. I just feel like someone's watching me. But that's just you staring at my butt, isn't it?"
    else:
        nin "I do..."
    "Nina looks at you for a moment. She starts to say something, but thinks better of it. The pair of your walk in silence for a while."
    mc "So..."
    nin "Yeah?"
    mc "Did you have fun at the party?"
    show nina scarf worried with Dissolve(0.1)
    nin "The party? Why are you bringing that up now?"
    mc "To pass the time I guess. I mean... We didn't hang out that much there."
    nin "If this is going to be more giving me crap about Trevor... Can we not do that again?"
    mc "No crap giving, I promise."
    show nina scarf neutral with Dissolve(0.1)
    nin "Ok, I guess. After you left I talked with Laura for a little while."
    nin "Then Trevor showed up..."
    nin "We had a few drinks... ran into Mia..."
    "Nina shrugs."
    nin "I stopped Laura from giving that girl booze under the table..."
    mc "It might have worked too, if [Nova] didn't have the same idea."
    show nina scarf angry with Dissolve(0.1)
    nin "That explains it, then."
    nin "What was she thinking? Mia barely comes out, if someone less... well {i}you,{/i} had gone out with her that night, they might have taken advantage of her."
    mc "Nobody did though, and I think both she and Mia had fun. And that's just how [Nova] rolls."
    nin "I know. That's the problem."
    mc "Nina, can you not do that?"
    show nina scarf neutral with Dissolve(0.1)
    nin "Do what?"
    mc "Just... I don't know, [Nova]'s like family..."
    nin "I know that. But what does that have to do with the price of apples?"
    mc "Now I say this in the full knowledge that if you two combined your powers I'd be truly helpless, but can you try getting along more?"
    mc "You guys actually have a lot in common."
    show nina scarf suspicious with Dissolve(0.1)
    nin "I don't see it, honestly. Anyway, it's not like I hate her or anything."
    mc "You know what, just forget I said anything."
    nin "So why even bring it up?"
    mc "Like I said... Nevermind."
    "Nina stops."
    show nina scarf smiling with Dissolve(0.1)
    nin "Is this what it sounds like when I tell you to try and be better friends with Trevor?"
    "You laugh."
    mc "Yeah, probably."
    if TrevorFriend >= 2:
        nin "Well, you're trying. So, no promises, but I will too."
    else:
        nin "Well, since I'm the mature one here, I should lead by example. So I'll try, ok?"
    mc "Thanks."
    show nina scarf suspicious with Dissolve(0.1)
    nin "So where was I? Oh right, I ran into Trevor again and Laura flirted with him."
    mc "Really?"
    nin "She wasn't serious... But when she saw me annoyed she left me alone again. And what else?"
    nin "Toby got smashed."
    mc "Yeah, I saw!"
    show nina scarf neutral with Dissolve(0.1)
    nin "He was all making out with Sophie and it made me uncomfortable."
    mc "I figured you'd be used to that by now."
    nin "I try to avoid him... and I mean, Sophie's ok, but..."
    nin "Well, that's when I left. You saw the rest."
    mc "You mean when you were on the way to the grove?"
    show nina scarf angry with Dissolve(0.1)
    nin "Are we doing this again? Look, we weren't going to have sex..."
    mc "You say that, but those panties tell a different story."
    show nina scarf surprised with Dissolve(0.1)
    nin "What do my panties have to do with anything?"
    "Nina is taken aback. It seems you hit on something."
    mc "What, indeed?"
    nin "I like these panties..."
    mc "So you wear stuff like that every day?"
    nin "No! I mean... It was a party. I got dressed up."
    mc "Your overalls are dressed up?"
    "Nina sighs."
    show nina scarf angry with Dissolve(0.1)
    nin "You're not going to let this go are you? First, Laura gave these to me, \"just in case\". "
    nin "But I wasn't planning on doing it that night. It's just... if and when it happens..."
    nin "I don't want to be wearing something that looks frumpy."
    show nina scarf sad with Dissolve(0.1)
    nin "Not knowing what I'm doing when I know he's had girlfriends before? Do you have any idea how that makes me feel?"
    mc "I..."
    show nina scarf angry with Dissolve(0.1)
    nin "There, it's all out in the open. Are you happy now?"
    mc "Ok, sorry. Just... I never thought you'd worry about stuff like that."
    show nina scarf sad with Dissolve (0.1)
    nin "Because you're a big old dummy. That's why."
    mc "Nina..."
    nin "Yeah?"
    show mc underwear neutral at left with Dissolve(0.1)
    show nina scarf sad at farright

menu PantyReassure:
    "I wouldn't care [gr]\[NinaLove +1\]":
        hide mc with easeoutleft
        show nina scarf sad at center with Dissolve(0.3)
        mc "Hey, if it was me I wouldn't care if your were wearing sackcloth."
        mc "I'd just be psyched to be with an awesome girl like you."
        show nina scarf laughing with Dissolve(0.1)
        "Nina muses on what you said before breaking out into laughter."
        mc "What?"
        nin "Sackcloth panties? Do you have any idea how much that would chafe?"
        mc "I..."
        show nina scarf neutral with Dissolve(0.1)
        nin "I'd be better off not wearing panties at all. And with my denim overalls. Let me tell you, it wouldn't be pleasant."
        mc "Forget it, see if I'll try to be nice again!"
        nin "I appreciate it, but sackcloth panties! Seriously... Ouch."
        "Nina smiles at you."
        nin "Thank you. I feel better now."
        $ NinaLove += 1
        jump Mushrooms2
    "Trevor would be thrilled no matter what. [purp]\[NinaTrevor +1\]":

        hide mc with easeoutleft
        show nina scarf sad at center with Dissolve(0.3)
        mc "I don't think it matters, honestly. Even someone like Trevor wouldn't think less of you if you had regular panties on."
        nin "I just want to feel sexy sometimes... but I know I'm not..."
        mc "Sure you are!"
        nin "You really think so?"
        mc "Super sexy... And I'm sure he thinks so too."
        show nina scarf smiling with Dissolve(0.1)
        nin "Thanks... That made me feel better."
        $ NinaTrevor += 1
        jump Mushrooms2

label Mushrooms2:

    scene cave mushrooms with Dissolve(2)
    play music evening fadein 1
    hide window
    w ""
    "You reach the end of the pathway and come across a patch of large mushrooms."
    show nina scarf surprised with Dissolve(0.1)
    nin "Wow! That's a lot of them."
    mc "Yeah."
    "Nina's stomach grumbles so loud you swear it causes an echo."
    mc "Wow. That was..."
    show nina scarf angry with Dissolve(0.1)
    nin "Say another word. I dare you."
    mc "I'm hungry too, Nina."
    nin "Please tell me these aren't poisonous."
    "You examine the mushrooms closely, looking for telltale signs of the poisonous ones in the area."
    mc "These should be safe."
    show nina scarf suspicious with Dissolve(0.1)
    nin "Should be?"
    mc "Well, I know just about every poisonous mushroom around here and I don't recognize these."
    nin "How do you know so much about this outdoor survival stuff?"
    mc "Well, you know how I'd run away from home into the woods after [Nova] showed up for the first time?"
    show nina scarf neutral with Dissolve(0.1)
    nin "How could I forget? Your dad was livid..."
    mc "Well I got a taste for camping out in the woods whenever things got too hectic."
    show nina scarf suspicious with Dissolve(0.1)
    nin "Hectic? Our village is never hectic."
    mc "Ok... Annoying, then."
    mc "Whatever you want to call it. I just had to get away sometimes."
    show nina scarf neutral with Dissolve(0.1)
    nin "And I remember Redd eventually came to terms with that."
    mc "Yeah, after one too many times he found me sleeping under a tree, he broke down and bought me a book on survival."
    nin "And that's why you know how to build fires and stuff so well?"
    mc "Yup. I must have read that book a hundred times."
    nin "Well, in that case... I'm starving!"
    mc "Wait!"
    "Nina grabs a mushroom and takes a bite out of it."
    "She immediately spits it out."
    show nina scarf angry with Dissolve(0.1)
    nin "Bleh! It tastes like goblin butt."
    mc "I said they were edible, but you're going to want to cook them. And wash them too."
    show nina scarf worried with Dissolve(0.1)
    nin "Are you sure they aren't poisonous? Something this bad HAS to be poisonous."
    mc "Is your tongue puffing up?"
    nin "No..."
    mc "Is my face melting?"
    nin "No."
    mc "Then you're fine. Anyhow... We roast them up, they'll be better."
    show nina scarf neutral with Dissolve(0.1)
    nin "I'll take your word for it. And you taste first next time."
    mc "Deal. {w} Also, I'm serious, if my face starts to melt in the next few mintues, let me know."
    if CrystalCave == 1 and Lake == 1:
        mc "I guess that's it. Nowhere else to see."
        nin "Well... I think I'm going to take that bath then."
        mc "Want some help?"
        show nina scarf smiling with Dissolve(0.1)
        nin "Very funny. How about you grab some of these mushrooms and make sure the fire is ready?"
        nin "That roasting thing better work."
        mc "It should, but no promises."
        nin "If not I just might have to eat you to survive. See you soon."
        $ Mushrooms = 1
        jump NinaCampTrouble
    else:
        scene black with Dissolve(2)
        nvl clear
        stop music fadeout 1
        n "You and Nina head back to explore the other paths."
        $ Mushrooms += 1
        scene cave paths with Dissolve(2)
        jump CaveEntrance

label NinaCampTrouble:

    play ambient fire
    play ambient2 caverain
    stop music fadeout 1
    scene cave campsite with Dissolve(2)
    "After a while you return to the camp with some mushrooms. You place them down on the tarp and add some wood to the fire."
    mc "Glad it's still going."
    "You spend some time checking on your clothes and taking the dust off of them."
    mc "{i}*Well, they're finally dry.*{/i}"
    mc "{i}I'm gonna miss seeing Nina in my scarf...{/i}"
    mc "{i}But seriously, I need to stop. She's a friend... and I came to terms with that a long time ago.{/i}"
    "You hear a woman's scream coming from the direction of the pool."
    mc "Nina!"
    play music action fadein 1
    nvl clear
    n "You run through the cave as fast as you can."
    mcn "What's going on? Did she hurt herself?"
    n "You follow the scream to the underground lake. Nina screams again, and you pray with each step you get there on time."
    scene goblin 1 with Dissolve(2)
    "You turn and see a grotesque green humanoid menacing Nina. She stands naked in front of it as it advances, a cruel blade filling its hand."
    gob "The other human is gone... Ether has been so lonely... So hungry."
    gob "Ether is supposed to eat meat... Ether is supposed to be with his own people."
    gob "Human girl will keep Ether company, no... then fill Ether's belly?"
    nin "NO! Get off of me!"
    gob "Human girl is loud... talks too much. Maybe Ether should use her tongue as an appetizer. Then human girl talk less."
    "The goblin talks to himself more than to Nina as he grabs her roughly."
    gob "But then she scream more."


    nvl clear
    n "Nina tries to use her size advantage to push the goblin away from her, but she has no leverage, and it's stronger than her, despite its size."
    mcn "Nina!"
    gob "Ether wanted to deal with the human boy later... Go away."
    mc "Get away from her!"
    scene goblin 3 with Dissolve(1)
    gob "Ether is BUSY!"
    "The goblin turns to you and roars."
    "You are shaken in fear for a moment. But then you look at Nina, helpless, afraid and naked. Your vision starts to cloud and you see red. Adrenaline courses through your veins."
    mc "I said GET THE FUCK AWAY FROM HER!"
    gob "Ether was going to let other human live until it was time for eating."
    gob "But you changed Ether's mind on it. Ether eat boy first... have company for longer..."
    nin "[MC]! Leave me! Just RUN! He's stronger than he looks!"
    mc "I'm going to kill you, you green piece of shit!"
    "The goblin roars and lets go of Nina. It's staring right at you."
    nvl clear
    n "You rush at the goblin while brandishing your knife."
    n "You aim for Ether's head, but he dodges at the last second and punches you in the stomach. You double over and fall to the ground, holding on to your knife by sheer force of will."
    scene goblin 4 with Dissolve(2)
    gob "Dagger is pretty. Ether will add it to his collection."
    "The goblin wrestles you to the ground with a free hand holding your dagger down."
    "He raises his cleaver over his head and prepares to strike as you try to push him off with your other arm."
    "The cleaver begins its downward arc. You want to close your eyes, but can't. You death approaches as if in slow motion."
    mc "{i}*Sorry Nina.*{/i}"
    scene black with Dissolve(2)
    play sound blow
    scene goblin 5 with vpunch
    nin "Get the FUCK off of him!"
    "You hear a thud and see the swing go wide. You look up to see Nina holding a rock in her hand."
    gob "That's it. Ether kill both... have fun with dead bod..."
    "His attention diverted, you are able to wrestle your arm free from his grip. You stab the goblin in the stomach and he screams."
    scene goblin 3 with Dissolve(1)
    gob "Ether will eat you while you are still alive."
    mc "What does it take to kill you?"
    mc "{i}I don't have a weapon... I don't have anything... but I have to keep her safe...{/i}"
    mc "{i}On the bright side... I have his full attention.{/i}"
    mc "{i}With any luck he'll be so busy eating me and raping my corpse that he'll forget about Nina long enough for her to escape.{/i}"
    mc "{i}Stop it! Don't think about your imminent death... just think about keeping Nina away from this monster!{/i}"
    mc "Hey... Shit brick! You going to keep roaring or are you going to kill me already?"
    "Ether charges you with his cleaver in hand! You turn around and run as fast as you can."
    gob "KILL YOU!"
    "And with that the chase begins."
    jump CatchMeIfYouCan


label CatchMeIfYouCan:
    scene cave passage with dissolve
    nvl clear
    n "You run as if possessed through the cave pathways."
    mcn "He has to be slowed down because of that wound, right?"
    n "You look behind you and see that the enraged goblin is right on your tail."
    n "He's bleeding profusely from his wound, but still moving faster than you would have thought possible."
    mcn "{i}If this is how fast he is when wounded... I'd be dead already if he wasn't{/i}"
    gob "RAAAAAAH!!"
    "Ether's voice echoes in the cave. You want to curl up into a ball and die, but somehow you find the strength to keep running despite your fear."
    mc "Follow me!"
    mc "{i}Ok... I think I have one chance to kill this guy before he eats my entrails.{/i}"
    mc "{i}But chances are...{/i}"
    mc "{i}It'll probably kill me too.{/i}"
    mc "{i}Thanks for nothing, brain.{/i}"
    scene cave paths with dissolve
    "You exit the pathway and make a left. You skip the next passage then make another left."
    "You immediately feel the warmth in the pathway."
    gob "Run all human wants. Ether will stop never."
    mc "{i}For this to work I need to get further ahead of him.{/i}"
    "You will yourself to sprint even faster. You can feel the muscles of your legs burning and you know you're gasping for air, but you don't care."
    mc "{i}Here we go.{/i}"
    mc "You're too slow Weak-er!"
    mc "{i}Oh... that was a HORRIBLE pun.{/i}"
    "You hear Ether scream from the pathway."
    gob "We see who weak, human."
    scene cave crystal 1 with Dissolve(2)
    "The crystals in the chamber seem to be glowing even brighter than they were the last time you were here. The room is now lit, almost as if it was day."
    mc "{i}Ok... Breathe. No shadows to hide in... Just use the crystals as cover.{/i}"

    scene cave crystal 2 with Dissolve(2)
    nvl clear
    n "You hide behind one of the large crystals just as Ether enters the cavern."
    n "He hisses as he squints his eyes at the bright light coming from the fire crystals."
    n "You wait for him to pass you, then make a dash out the entrance."
    n "Ether hears you and turns around roaring again."
    scene goblin 8 with Dissolve(2)
    mc "{i}Well... Now or never...{/i}"
    "You exit from you hiding spot and Ether turns towards you, vocalizing a screech of pure rage."
    "You throw a fire crystal at one of the formations near the goblin with all the force you can muster."
    gob "Wha?"
    scene whitescreen with Dissolve(3)
    stop music fadeout 1
    "When the crystal connects with the larger formation, it explodes into a ball of fire that instantly consumes the goblin."
    play sound boom
    play ambient ringing
    "You hear a loud bang, then nothing but a ringing in your ears."
    mc "Holy Goddess... I'm... alive. That worked."
    stop ambient fadeout 2.0
    "The goblin is nowhere to be seen. However..."
    mc "Oh no..."
    scene black with Dissolve(0.5)
    scene whitescreen with Dissolve(0.5)
    scene black with Dissolve(0.5)
    scene whitescreen with Dissolve(0.5)
    scene black with Dissolve(0.5)
    scene cave crystal 1 with Dissolve(2)
    nvl clear
    n "You feel a low hum seep through the floor. You don't hear it as much as you feel it though your bones. The fire crystals that surround you are pulsing, brighter, the heat they give off is scorching."
    n "The slow and steady heartbeat of the cave is now becoming faster, more erratic."
    mcn "I did not think this through."
    n "You begin to run towards the exit. As you do the low hum begins to fade, leaving only the high pitched ringing in your ears. There is no more heartbeat, and the crystals are now so bright as to be blinding. "
    n "The exit to the room disappears in the glare."
    nvl clear
    n "Hoping that you are still oriented correctly you rush into what is now a fog of light. Countless steps later, you pierce through the blinding fog into blackness."
    mcn "Don't stop! Do not..."
    scene cave passage with Dissolve(2)
    n "All you can focus on is each step you take in the darkness. You run as far and as fast as you can, but know instinctively that it is not far enough."
    n " Then your running stops, not from exhaustion but because your feet are no longer touching the ground."

    hide window
    scene whitescreen with Dissolve(2)
    n "You're in the air, flying towards the cave wall, which is coming at you at alarming speed."
    n "A muffled boom cuts through the ringing in your ears. Then there is darkness, and nothing else"
    play sound boom
    stop music
    stop ambient fadeout 1
    scene black with Dissolve(5)
    jump NinaAid
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
