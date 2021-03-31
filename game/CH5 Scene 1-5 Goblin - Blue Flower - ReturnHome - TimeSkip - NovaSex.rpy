label CH5FightGoblins:
play music action
scene CH5Attack01 with Dissolve(2)
hide window
w ""
"You and Trevor stand between the goblins and the women. You put on your brave faces, but you're shaking as the small army run in your direction."
tre "[Nova], Mia, hide for fuck's sake!"
"[Nova] and Mia run off into the forest. As she hits the treeline, [Nova] turns to you."
nov "[MC]! Are you crazy? Get over here!"
mc "Just get out of here, both of you! I'll buy us some time with Trevor!"
tre "I don't know, [MC]... Maybe we should just run as well. I don't like our odds here."
mc "Well, too late now."
scene CH5Attack02 with Dissolve(2)
hide window
w ""
"A goblin approaches at full speed, but you can't move. You freeze in fear, unable to swing your axe. To your surprise, the goblin passes right beside you, ignoring your presence."
mc "{color=#b7b7b7}{i}What...? Is it going after the girls? No... It's going after the fairy!{/color}{/i}"
tre "Fuck! [MC], run! They're not here for us! That's our chance!"
scene CH5Attack03 with Dissolve(2)
hide window
w ""
mc "The fairy! We must help her!"
tre "Are you crazy?! FUCK THAT BITCH!"
"You run as fast as you can without thinking twice, trying to save the fairy from her sure death."
mc "{color=#b7b7b7}{i}I know she's a pain in the ass, but... she doesn't deserve this!{/color}{/i}"
scene CH5Attack04 with Dissolve(2)
hide window
w ""
mc "Aaah!"
"The spear cut through your flesh and you feel pain like you never did before. Your vision blurs and your legs start to shake. You're ashamed to admit, but the first thought in your mind after \"I'm going to die\" is \"This wasn't worth it\"."
mc "Damn it! I don't wanna die like this!"
"The goblin pulls its spear up and prepare for another blow. Your mind start to fade as you get ready to die."
mc "I just hope I don't suffer too much..."
tre "AAAAAAH!"
"You hear Trevor's scream getting louder as he comes to rescue you and adrenaline starts pumping into your body."
play sound blow
scene CH5Attack05 with Dissolve(1)
hide window
play sound stabby
tre "DIE!"
$ renpy.pause(1.0)
play sound goblindie
"Trevor kicks the goblin away from you and jumps on top of it, piercing its chest with his sword, using his weight and all the strength in his muscles to guarantee his first kill."
"You watch as a second goblin comes after Trevor from behind, ready to kill him."

menu WarnTrevor:
    "Warn Trevor":
        mc "Trevor! Behind you!"
        tre "What? Oh, damn!"
        "Trevor turns and tries to pull his sword off the goblin's dead body, but it's stuck. His only hope now is to dodge the attack, but it seems too late now."
        scene CH5Attack06-2 with Dissolve(2)
        hide window
        w ""
        "Out of nowhere, [Nova] jumps on top of the goblin, risking her life to keep you both safe."
        nov "AAAH! Fuck no, motherfucker!"
        "The goblin falls to the ground and [Nova] quickly jumps out of its back, running in Trevor's direction. She helps him pull his sword off and starts running in your direction."
        nov "There's a lot more of them coming, they're too many to fight! Retreat!"
        "You take the fairy in your hands and once [Nova] is right by your side you start running."
        mc "Follow me!"
        $ HelpTrevor = 0
    "Help him out [gr]\[Help Trevor\]":

        mc "Oh shit! Trevor, look out!"
        play sound stabby
        scene CH5Attack06 with Dissolve(2)
        hide window
        w ""
        "You groan as you get up off your knees and run towards the second goblin. You scream, swinging you axe with all you have into the goblin's chest."
        "You let go of your axe as the goblin falls to the ground - every second is valuable in this fight."
        mc "They're too many to fight! Retreat!"
        "You take the fairy in your hands and run towards the girls."
        mc "Trevor, follow me!"
        $ HelpTrevor = 1

label EscapeGoblins:
    scene CH5Attack07 with Dissolve(2)
    hide window
    w ""
    "You hide behind the trees, hoping you ran fast enough to make the goblins lose your track."
    tre "Guys, we need to keep running!"
    mc "Shhhh!"
    "You hear the goblins searching for you. It seems impossible that they won't find you at this point."
    nov "Now what?"
    mc "Now we pray..."
    play sound ice 
    "Your amulet begins to glow. The goblins keep getting closer and missing you as if you were invisible."
    tre "How is this possible?"
    stop music fadeout 3
    "Trevor grabs his sword, shaking. A goblin stands right by your side, looks around and keeps walking. Eventually, all goblins give up and go away."
    fai "Uh..."
    scene CH5Attack08 with Dissolve(2)
    hide window
    w ""
    mc "Oh, she's waking up!"
    fai "Humans are... trully useless..."
    play music fairy
    nov "Aaand she's back."
    mc "She saved us."
    nov "She saved herself. What's your deal with her?"
    "You sit down in pain on a nearby rock and Mia checks your wounds."
    scene forest path with Dissolve(2)
    show mia neutral adv with Dissolve(1)
    mia "Oh my... This is a big wound! Just let me see what I have to ease the pain."
    mc "That'd be nice..."
    mia "I know we need to keep moving, but I need to treat [MC] before it gets worse."
    mc "Do your thing, Mia."
    "You smile at her, and she smiles back."
    hide mia with Dissolve(1)
    "Mia pulls out some bandages and salves and treats you."
    show nova neutral with Dissolve(1)
    nov "Well... now what?"
    mc "Not sure... I have no idea where we are and we still don't have the flower."
    show nova annoyed with Dissolve(1)
    "[Nova] pokes at the fairy."
    nov "Hey, little cunt? You awake?"
    mc "Geez."
    nov "She tried to KILL us."
    mc "I really don't think so..."
    fai "Taboo Girl is really annoying... Ew, I don't want to rest in Scarfy's smelly hands any more than I need."
    "The fairy slowly floats out of your hands and stares at you."
    show nova neutral at slightright with easeinleft
    show fairy neutral at slightleft with Dissolve(1)
    fai "But fairies pay debts! Always... good and bad, and Scarfy helped me, I can't deny that. So, what was that you were looking for?"
    mc "The Azureola."
    fai "The human still wants that silly flower?"
    mc "Yes."
    "The fairy thinks for a moment."
    fai "Very well, but anything the fairy owes is now null and void."
    mc "Sure... yes."
    scene CH5BlueFlower with Dissolve(2)
    hide window
    "You see the fairy glow as she closes her eyes. The ground shakes for a second, and a large blue flower springs out from underneath the fairy."
    fai "There... done."
    mc "It's... Thank you!"
    fai "No thanking - payback. Fairy is done with [MC] now."
    fai "You didn't have to save the Fairy, so it's only fair. Good bye now."
    "The Fairy flies away."
    nov "Did she just say, \"you\"?"
    mc "I think she did..."
    nov "Weird. Well, good riddance. Never want to see her ever again!"
    "You pick up the flower."
    scene forest path with Dissolve(2)
    mc "We've got the Azureola now! It's still early, if we leave now we can make it back home before nightfall."
    "You pull out your compass."
    mc "It's working now..."
    tre "You sure?"
    mc "We'll know soon enough."
    tre "Lead the way."
    stop music fadeout 3
    scene blackout with Dissolve(2)
    hide window
    scene titlecardCH5 with Dissolve (3)
    pause 2
    scene blackout with Dissolve(2)
    play music evening
    "The four of you head down the path, following the compass back home."
    "Several hours later."
    play sound walkgrass
    scene village afternoon 1 with Dissolve(2)
    "The sun starts to set as you make it back to the village. Walking with dificulty after a long journey, the party heads back to your house."
    scene farm_fixed_afternoon with Dissolve(2)
    "Nina sits on your front steps with a worried expression. When she finally sees you, she smiles and runs in your direction."
    play music nina2
    scene CH5Return01 with Dissolve(2)
    hide window
    w ""
    nin "You're alive!"
    mc "Ouch! Be careful!"
    scene farm_fixed_afternoon with Dissolve(2)
    show nina surprised with Dissolve(1)
    nin "What happened? Are you OK?"
    mc "It's nothing. I'd be worse without Mia."
    show trevor neutral at offscreenleft
    show trevor neutral at farleft with easeinleft
    show nina surprised at slightright with easeinleft
    tre "And you don't even say hi to your boyfriend?"
    show nina neutral with Dissolve(0.2)
    nin "Sorry, Trevor!"
    show nina neutral at slightleft with easeinleft
    "She hugs him."
    show nova neutral at center with Dissolve(1)
    nov "So, how's Redd?"
    nin "He's stable... the elder is inside with him now."
    show mia neutral adv at offscreenright
    show mia neutral adv at slightright with Dissolve(1)
    mia "Oh, Silas is..."
    show elder neutral at offscreenright
    show elder neutral at farright with Dissolve(1)
    eld "Here? Yes, I am."
    "Silas stands in the front door looking over at you."
    eld "I just came to see what the commotion was about. I see you all made it back."
    mia "Elder..."
    eld "Did you find the flower?"
    "You nod."
    eld "Good. Give it to me."
    "You hand it to the elder."
    eld "Follow me inside. All of you."
    stop music fadeout 2
    play sound walkinside
    scene farm house interior with Dissolve(2)
    play music night
    "As you walk in you see that there are some alchemy bottles set up on your kitchen table."
    mc "What are those?"
    show elder neutral at center with Dissolve(1)
    eld "Well, I've been around a while. You kids are damnably foolish, but I wanted to have this ready when you returned."
    mc "Uh... Thank you, sir."
    show mia neutral adv at offscreenright
    show mia neutral adv at slightright with Dissolve(1)
    mia "Can I help?"
    eld "You just go and look after Redd - the potion will be ready soon."
    mia "Elder, I'm sorry I-"
    eld "Not now, Mia... I need to concentrate."
    mia "Yes... Yes, sir."
    scene farm house interior with Dissolve(2)
    "Mia looks a little dejected as she heads to Redd's room with [Nova] in tow."
    show nina neutral at slightleft with Dissolve(1)
    show trevor neutral at slightright with Dissolve(1)
    nin "I should get home, my dad's probably worried."
    tre "I'm heading out too. I'll walk you home."
    "Nina gives you a hug."
    nin "I'm glad you all got back safely. You'll have to tell me everything about it later!"
    mc "Sure. Thanks for looking after dad."
    nin "It was nothing. Let me know how it goes, OK?"
    "You walk Nina and Trevor to the front door."
    mc "See you later."
    tre "Yeah."
    scene farm kitchen with Dissolve(2)
    "You see them off and walk towards your father's room. On your way you see Silas with tears in his eyes, whispering to himself."
    show elder neutral at center with Dissolve(1)
    eld "Thank the Maker she's alright..."
    mc "{color=#b7b7b7}{i}I didn't even think about how much Silas would have worried about us.{/i}{/color}"
    mc "Elder..."
    eld "Oh, [MC], I didn't see you there."
    mc "I'm sorry I took the book, please don't blame Mia for it - this was all my idea."
    show mia neutral adv at offscreenright
    show mia neutral adv at farright with easeinright
    "Mia approaches silently and starts eavesdropping when she notices that you're talking about her."
    eld "I appreciate you stepping in for Mia."
    eld "How do I say this? [MC], you are lucky to be alive."
    eld "This quest of yours was foolish and it was too dangerous - it could have gotten you all killed."
    eld "Your father will be furious with you for going and he'll chastise you worse than I ever could when he wakes up."
    eld "As for Mia, she had no business being out there! She could very easily have died, but that silly girl... she just didn't care. She did everything she could to help a friend. She did it with no concern for her own life. That's just who she is."
    eld "If she hadn't, she wouldn't be the girl I watched grow up. I'm proud of her. As the town elder I'm proud of all of you."
    "Mia comes up, tears in her eyes."
    show elder neutral at slightleft with easeinright
    show mia neutral adv at center with easeinright
    mia "Elder..."
    "She and Silas embrace, without a word."
    mia "I'm sorry to have worried you."
    eld "I know you are, my dear. Now come, we have a potion to administer."
    scene blackout with Dissolve(2)
    stop music fadeout 2
    "Several hours later."
    play music nightambiance fadein 3
    scene farm fixed night with Dissolve(2)
    "You and Mia stand at the door to your house."
    show mia neutral adv with Dissolve(1)
    mia "He'll be fine... I'll come by to check on him tomorrow."
    mc "Thanks. [Nova] says thanks too."
    mia "I know. She hugged me so hard I thought I was gonna pass out."
    show mia smiling adv with Dissolve(0.2)
    mia "About the tent..."
    mc "Look, if-"
    "Mia seems to gather up all the courage she can before almost screaming when interrupting you."
    mia "I'm glad it was you! I..."
    mia "It was really special to me, [MC]. I'm glad we did it."
    mia "I'll see you later."
    stop music fadeout 2
    scene blackout with Dissolve(2)
    "Mia leaves without giving you much time to answer."
    $ renpy.pause(2.0)
    play music morningquiet
    scene farm fixed with Dissolve(2)
    nvl clear
    n "Over the next several days Redd seemed to recover. Your father would still sleep quite a bit, but when he was conscious he was himself."
    n "Mia came by each day to check on him. You wished she could stay longer, but with your father in stable condition she had to assist the elder with other tasks."
    n "[Nova] kept working on the farm and you continued with your work around town. Slowly but surely the town began to recover from the devastation the storm left behind."
    n "You still haven't discussed the events of that night in the woods, and your evenings together have been without any of the flirting you did before."
    n "On your way home you run into [Nova] as she is putting away her farming tools."
    hide window
    nvl clear
    show nova neutral with Dissolve(1)
    mc "Hey."
    nov "Hey."
    mc "Long day?"
    nov "Not too bad. The potatoes are actually coming along nicely."
    mc "That's good! What about the wheat?"
    nov "Look who's taking an interest in the farm, all of a sudden!"
    mc "Funny how life works. How's dad?"
    nov "He's good. I caught him trying to walk around lunchtime."
    mc "He wasn't!"
    nov "Yup. I had to fight with him for like fifteen minutes to get him back in bed."
    mc "I'm surprised you did."
    nov "Mia showed up..."
    "You laugh."
    mc "Say no more. Alright, I'll go see dad."
    nov "I'll be taking a bath if you want to peep."
    mc "Raincheck!"
    show nova smirk with Dissolve(1)
    nov "Oh, right, you have our friendly neighborhood nurse to go to now."
    mc "I'm not even sure it's a regular thing - I've barely seen her."
    show nova neutral with Dissolve(1)
    nov "Yeah, poor girl is frustrated but won't say it."
    mc "She's not the only one."
    mc "Can't believe I just said that."
    nov "Don't worry, I'll let her know."
    mc "I don't know, I'm not even sure we're a thing."
    nov "You might want to figure that out. You should take her to the party. I mean, two escorts in a row and it'll be official."
    mc "Yeah..."
    nov "And you don't have to worry about dinner, Nina dropped off some food."
    mc "Great! Saves some time."
    nov "Yup."
    nov "Go see Redd. I'll be in in a minute."
    "You nod and head over to Redd's room."
    play sound walkinside
    scene farm redd room with Dissolve(2)
    show father neutral with Dissolve(1)
    dad "Another busy day not farming?"
    mc "Odd jobs were your idea, dad."
    dad "Yes, they were. And you're doing well."
    mc "[Nova] told me that Nina brought dinner. So we won't have to deal with her cooking tonight."
    dad "Better hers than yours."
    mc "True."
    dad "So... you and Mia?"
    mc "Again, dad?"
    dad "She reminds me of your mother... You could do a lot worse."
    dad "And more importantly, SHE could do a lot better."
    mc "Not a conversation we're having."
    dad "Take the reigns, boy."
    mc "I'll think about it."
    mc "{color=#b7b7b7}{i}Do I even want a steady girlfriend right now? Mia is great, but...{/i}{/color}"
    if MCNinaLike == 1 and NinaLove > 5:
        mc "{color=#b7b7b7}{i}I can't stop thinking about Nina, which is a bad idea.{/i}{/color}"
    elif NovaLove > 5:
        mc "{color=#b7b7b7}{i}I can't get [Nova] out of my mind, and that's ALL sorts of wrong.{/i}{/color}"
    elif MiaLove > 5:
        mc "{color=#b7b7b7}{i}I don't even know if she really wants to. Whatever she said, we WERE affected by that spell.{/i}{/color}"
    else:
        mc "{color=#b7b7b7}{i}There are a lot of other girls out there right now.{/i}{/color}"
    dad "Stop thinking too hard son, you'll break your brain."
    dad "By the way, you need to tell [Nova] that I'm not an invalid."
    mc "You're staying in bed, dad."
    dad "But-"
    mc "No buts, not until the elder gives you the OK. You still need to rest."
    dad "Fine. I'll just walk around when you go to sleep."
    mc "Not if we tie you to the bed."
    dad "My family... what did I ever do to deserve this?"
    mc "I'll let you think about that. See you later."
    stop music fadeout 2
    scene blackout with Dissolve(2)
    "Later that night."
    hide window
label NovaSex1:
    play music nova2
    scene CH5NovaSex01 with Dissolve(2)
    hide window
    w ""
    "You return to your room and get ready for bed. [Nova] is already there, reading her book - you both have been reading before sleeping lately."
    nov "Took you long enough. Cranking one out before bed?"
    mc "No, with you here it seems like my cranking days are over."
    nov "Yeah, like that will ever happen."
    mc "Well, some of us aren't comfortable doing that in bed... next to someone."
    nov "Wait... you...?"
    mc "You're not a mistress of stealth, [Nova]."
    scene CH5NovaSex02 with Dissolve(2)
    hide window
    w ""
    nov "Well... Shit."
    mc "Yeah."
    nov "So why didn't you say anything?"
    mc "Things were awkward enough already, thank you. And after the tent..."
    nov "Seriously? Relax, [MC], we both have needs!"
    nov "We don't have anything to hide. If you want to take care of yourself, go for it."
    mc "Very funny."
    nov "I'm serious. It's not like we haven't seen each other in... positions. Just don't get it on me."
    mc "And what, you just sit and watch?"
    nov "No. But it would be fair."
    scene CH5NovaSex03 with Dissolve(2)
    hide window
    w ""
    nov "I can be a visual aid. Better than those books of yours anyway."
    "You feel your cock stir as you stare at [Nova]'s breasts."
    mc "[Nova], just stop it. We can't, OK? We've gone way too far already!"
    scene CH5NovaSex04 with Dissolve(2)
    hide window
    w ""
    "[Nova] climbs over you."
    nov "You weren't complaining back in the tent."
    mc "That was the spell..."
    nov "You and I both know that's not true."
    mc "..."
    scene CH5NovaSex05 with Dissolve(2)
    hide window
    w ""
    nov "Come on, you telling me this doesn't get you all frisky? I can feel it already... this thing pokes me every night."
    mc "[Nova], stop fucking around!"
    nov "Stop what? This is just a little fun."
    mc "{color=#b7b7b7}{i}Goddamn it! She has no idea what this is doing to me. What's her deal anyway? Is it OK for us to do this?{/i}{/color}"
    nov "You're so awkward! This is fun because you freak out and will never-"
    scene CH5NovaSex06 with Dissolve(2)
    hide window
    w ""
    mc "Do something like this?"
    mc "You can't play like this, [Nova]. I'm serious."
    scene CH5NovaSex07 with Dissolve(2)
    hide window
    w ""
    nov "Yeah, sure you are."
    stop music fadeout 2
    "Your heart pounds as you look down to [Nova], mounted on her belly, holding her wrists as she devilishly smiles at you."
    mc "{color=#b7b7b7}{i}Fuck! She's so beautiful... I want this... I want to fuck [Nova] so bad!{/i}{/color}"
    scene CH5NovaSex08 with Dissolve(2)
    hide window
    w ""
    "You quickly unmount [Nova], trying to control youself. She turns down and points her butt in your direction almost immediately."
    mc "[Nova]! You're messing with me."
    play music sexnova fadein 2
    "Hm, no, I'm not. Come on [MC], I'm allowing you to use my body as your jerk material. You can do watever you want to me."
    scene CH5NovaSex09 with Dissolve(2)
    hide window
    w ""
    mc "Whatever I want... Really?"
    "You go behind [Nova] and grab her butt with both hands. You feel her body shaking once you touch her, almost in disbelief of your actions."
    nov "Oh..."
    mc "You're as horny as I am, but you want to play it off."
    scene CH5NovaSex10 with Dissolve(2)
    hide window
    w ""
    mc "Well... I'm done playing."
    "You slide you thumb and start removing her panties, slowly revealing her pussy. You think she'll ask you to stop at some point, but [Nova] remains silent."
    scene CH5NovaSex11 with Dissolve(2)
    hide window
    w ""
    mc "You're drenched..."
    scene CH5NovaSex12 with Dissolve(2)
    hide window
    w ""
    nov "So? You think you have the balls to do something?"
    mc "If this is what you want, then fine."
    scene CH5NovaSex13 with Dissolve(2)
    hide window
    w ""
    "[Nova] shakes her hips as you remove her skirt and panties, still teasing you."
    mc "{color=#b7b7b7}{i}I can't believe I'm really undressing [Nova] like this!{/i}{/color}"
    nov "So, what are your plans from here? Will you really jerk off while looking at the butt of your own-"
    scene CH5NovaSex14 with Dissolve(2)
    hide window
    w ""
    mc "No way I'm doing just that. After all your teasing, I'm going all the way and I'll fuck your pussy."
    mc "{color=#b7b7b7}{i}No way she isn't stopping me now! I win.{/i}{/color}"
    nov "Hm... Really?"
    "You remain in silence. [Nova] waits a couple of seconds and grins at you.."
    nov "Fine..."
    scene CH5NovaSex15 with Dissolve(2)
    hide window
    w ""
    mc "Last chance to back out."
    mc "{color=#b7b7b7}{i}This is wrong, but I don't want to stop now. I'm just lying to myself at this point... I want to fuck [Nova]! I'm going all the way.{/i}{/color}"
    nov "What, you think I'm scared?"
    "[Nova] presses her wet pussy against your cock, defying you to continue."
    scene CH5NovaSex16 with Dissolve(2)
    hide window
    w ""
    "You don't think twice once she does that and, like a savage, you grab her hips and shove your cock all the way inside [Nova] in one stroke."
    nov "AAAH!!"
    mc "{color=#b7b7b7}{i}Oh my God! I did it! I'm finally fucking [Nova]!{/i}{/color}"
    nov "Damn, [MC]! Ow..."
    mc "You OK?"
    scene CH5NovaSex17 with Dissolve(2)
    hide window
    w ""
    nov "You're balls deep and NOW you ask if I'm OK?"
    mc "Sorry, I guess I got too excited."
    scene CH5NovaSex18 with Dissolve(2)
    hide window
    w ""
    nov "It's fine... Just let me get used to it."
    mc "Uh, yeah, sure thing."
    mc "{color=#b7b7b7}{i}She doesn't want me to stop... So we're really doing it.{/i}{/color}"
    "[Nova] starts adjusting herself, twerking on your cock as her pussy shapes around it."
    nov "God, if Redd were to walk in here right now..."
    mc "Can we not talk about dad, and by extension how wrong this is right now?"
    nov "Good idea."
    scene CH5NovaSex19 with Dissolve(2)
    hide window
    w ""
    nov "Hm... You can move now."
    "You slowly pump your hips back and forth. [Nova] groans as you do."
    nov "Fuck, that feels... nice. Can you go a little faster?"
    scene CH5NovaSex20 with Dissolve(2)
    hide window
    w ""
    "You move your hips faster. The wet friction of [Nova]'s insides grasp at your cock, making you groan."
    nov "MMM... like that... hah..."
    "[Nova]'s scent fills the air as she gets soaked from your cock."
    mc "Your body is amazing... and you're so tight, damn..."
    scene CH5NovaSex21 with Dissolve(2)
    hide window
    w ""
    nov "Ah... like that... holy shit [MC], this feels so good! If you keep doing me like that..."
    scene CH5NovaSex22 with Dissolve(2)
    hide window
    w ""
    nov "Oh!"
    mc "Well, before I continue, let's take this top out of the way. I want to play with your tits and watch them bounce as I fuck you."
    scene CH5NovaSex23 with Dissolve(2)
    hide window
    w ""
    "[Nova] raises her arms and lets you take off her top."
    nov "Damn [MC], you're acting so different right now... That's hot!"
    mc "Well, I have my cock inside you, so things are a bit different now."
    scene CH5NovaSex24 with Dissolve(2)
    hide window
    w ""
    nov "Mmm... Yes, touch it... you love my tits, don't you? I love when I catch you staring at them."
    mc "They're so firm... I can't believe I'm finally touching your tits."
    scene CH5NovaSex25 with Dissolve(2)
    hide window
    w ""
    mc "They just fit my hands so perfectly! All the times you teased me... I wanted to squeeze them like this so bad!"
    nov "I can't believe you're actually doing it... I'm letting [MC] play with my breasts!"
    scene CH5NovaSex26 with Dissolve(2)
    hide window
    w ""
    mc "Well, enough of that for now. Get on all fours again, I need to continue pounding your pussy!"
    nov "Ahh, yes... Do it! Fuck me hard, [MC]..."
    scene CH5NovaSex27 with Dissolve(2)
    hide window
    w ""
    mc "So, what were you saying was going to happen if I keept fucking you like this? Fucking you feels too damn good, I can't get enough of you pussy!"
    "You increase your speed and [Nova] seems to be getting close to her climax."
    scene CH5NovaSex28 with Dissolve(2)
    hide window
    w ""
    nov "Oh my God, [MC], you cock feels so good! It's going so deep inside me... I can't believe... [MC] is pounding me so hard from behind..."
    nov "Shit! Right... right there. Keep going... keep..."
    "[Nova] grabs the bed's headboard bars, making the entire bed shake and a lot of noise as you shove your cock inside her pussy. You start getting worried, but it seems like she doesn't mind it at all right now."
    scene CH5NovaSex29 with Dissolve(2)
    hide window
    w ""
    nov "AAAAAH!!!!"
    "[Nova] reaches for your head and cums on your cock as you thrust into her."
    mc "Shhh! [Nova]! You're gonna wake up dad!"
    scene CH5NovaSex30 with Dissolve(2)
    hide window
    w ""
    nov "Oh my God! [MC]! That felt so good..."
    "You give [Nova] a moment and she relaxes, laying down on the bed and hugging the pillow. You start to move again, but she tenses up as you do."
    nov "Ahh... Whoa..."
    scene CH5NovaSex31 with Dissolve(2)
    hide window
    w ""
    nov "Can you stop? I'm really sensitive right now."
    mc "Oh, shit. Sorry."
    mc "I'm not finished yet though..."
    scene CH5NovaSex32 with Dissolve(2)
    hide window
    w ""
    nov "Crap, I don't wan't to leave you with blue balls... Even if it would serve you right."
    nov "I just definitely didn't expect to have an orgasm from penetration only..."
    mc "It's fine."
    scene CH5NovaSex33 with Dissolve(2)
    hide window
    w ""
    nov "Relax, cowboy! There are other ways to make you cum. What would you like me to do?"
    jump NovaFinishMenu

menu NovaFinishMenu:
    "Ask to use her mouth":
        jump NovaBJFinish
    "Ask to use her ass.":

        jump NovaHotDog

label NovaBJFinish:
    mc "Maybe you could use your mouth?"
    "Nova looks up at you as she processes what you just said."
    nov "Yeah, sure... How hard could it be?"
    scene CH5NovaSex34_A_1 with Dissolve(2)
    hide window
    w ""
    "You feel a shock wave running through your body just from [Nova] putting the tip of your cock inside her mouth and feeling her tongue over it."
    mc "Oh, yeah... that's it!"
    mc "{color=#b7b7b7}{i}I can't believe [Nova] is sucking my dick right now!{/i}{/color}"
    "Nova starts to suck on you and she moves her tongue a lot, but she doesn't try to take it too deep inside her mouth. The blowjob is sloppy, but enthusiastic - not nearly as proficient as Elise was, but still extremely pleasurable."
    scene CH5NovaSex34_A_2 with Dissolve(2)
    hide window
    w ""
    "[Nova] grabs your cock and slowly tries to descend, taking it deeper inside her throat."
    mc "Keep going... just like that. This feels amazing."
    scene CH5NovaSex34_A_3 with Dissolve(2)
    hide window
    w ""
    "[Nova] takes your cock out of her mouth, drooling all over it and taking a big breath. She continues to move her tongue all around, teasing you as much as she can."
    nov "It's so big... I like the taste of it though..."
    mc "You don't have to go all the way to-"
    scene CH5NovaSex34_A_4 with Dissolve(2)
    hide window
    w ""
    "[Nova] starts another slow descend, taking your whole cock inside her mouth this time. She plays with your balls and makes some weird noises as she chokes trying to hold her position; the vibrations on your cock make it feel specially amazing."
    mc "Aaahh..."
    scene CH5NovaSex34_A_5 with Dissolve(2)
    hide window
    w ""
    nov "Ahh! I'm getting better at this!"
    mc "Yes, you are. If you keep doing it like this..."
    nov "OK... just warn me if you're about to cum."
    "You nod."
    scene CH5NovaSex34_A_6 with Dissolve(2)
    hide window
    w ""
    "You are lost in the sensation of [Nova]'s mouth as she once again sucks you. It doesn't take long for you to feel your balls tighten."
    mc "Now! I'm gonna..."

    menu CumNova:
        "Cum inside her mouth":
            scene CH5NovaSex_Finish_B1 with Dissolve(2)
            hide window
            w ""
            "[Nova] sucks harder and you explode into her mouth. Her eyes widen in surprise as her mouth is filled with your seed and she tries to hold as much as she can in it."
            scene CH5NovaSex_Finish_B2 with Dissolve(2)
            hide window
            w ""
            mc "AAAH!!! Goddess! That feels so good!"
            "[Nova] continues to hold your cum inside her mouth, playing with it with her tongue and deciding what to do with it."
            scene CH5NovaSex_Finish_B3 with Dissolve(2)
            hide window
            w ""
            "Nova swallows your semen and smiles at you."
            nov "That was a big load! Everything with you is too much, heh? It's not easy to handle you in bed, that's for sure! And I thought I was gonna be the one to give your trouble! Nice taste though."
        "Cum on her face":

            scene CH5NovaSex_Finish_C1 with Dissolve(2)
            hide window
            w ""
            "[Nova] pulls back and you fire all over her face."
            mc "AAAH!!!"
            scene CH5NovaSex_Finish_C2 with Dissolve(2)
            hide window
            w ""
            "[Nova] continues to get surprised by each shot of cum you land on her face, painting it white."
            nov "Damn... that was a lot."
            mc "Wow... I just couldn't stop cumming on you, that was way too hot!"
            scene CH5NovaSex_Finish_C3 with Dissolve(2)
            hide window
            w ""
            nov "Everything with you is too much, heh? It's not easy to handle you in bed, that's for sure! And I thought I was gonna be the one to give your trouble!"
            nov "Nice facial though, that was hot for me too! Do you like seeing my face covered in your semen?"
            mc "It's a nice view for sure!"

    jump Day10NovaBedEnd

label NovaHotDog:
    mc "{color=#b7b7b7}{i}Well, I can't use her pussy, so maybe...{/i}{/color}"
    mc "Maybe I could use your ass?"
    nov "What the fuck? No way! Exit only... I don't know what kind of freaky shit you're into but-"
    mc "{color=#b7b7b7}{i}Damn it.{/i}{/color}"
    mc "No! I meant... like that time when you rubbed your ass on me."
    nov "What? Oh, like... OH!"
    nov "Then sure, I guess."
    scene CH5NovaSex34_B_1 with Dissolve(2)
    hide window
    w ""
    "[Nova] bends over and you slide your cock on top of her ass cheeks."
    nov "I swear to the Maker, if you try to shove it in..."
    mc "I got it, relax."
    nov "..."
    mc "You have one hell of an ass, [Nova]."
    scene CH5NovaSex34_B_2 with Dissolve(2)
    hide window
    w ""
    "You slip your cock in between her ass cheeks and start to move back and forth."
    nov "Does that feel good?"
    mc "You have no idea."
    nov "Boys just want to rub their dicks on anything, don't they?"
    mc "Ffff... hah... Kinda."
    scene CH5NovaSex34_B_3 with Dissolve(2)
    hide window
    w ""
    "After some time you feel your climax approaching."
    mc "[Nova]! I'm gonna..."
    scene CH5NovaSex_Finish_A1 with Dissolve(2)
    hide window
    w ""
    "[Nova] shakes her butt, stroking your cock with her ass cheeks. You start releasing your seed all over her back."
    mc "Fuck!"
    nov "Wow! You're shooting so much cum on my back... it feels really warm and slimy."
    scene CH5NovaSex_Finish_A2 with Dissolve(2)
    hide window
    w ""
    nov "What a mess you made... he-he! I'm glad I made you cum so much using only my butt!"
    mc "{color=#b7b7b7}{i}Damn, she looks so sexy looking at me like that with my cum all over her back! I wish I could keep fucking her forever!{/i}{/color}"
    nov "Everything with you is too much, heh? It's not easy to handle you in bed, that's for sure! And I thought I was gonna be the one to give your trouble!"
    jump Day10NovaBedEnd

label Day10NovaBedEnd:
    stop music fadeout 2
    $ persistent.novasex1 = True
    $ renpy.end_replay()
    scene farm bedroom night with Dissolve(2)
    "Nova grabs one of your dirty shirts and wipes herself off."
    play music nova2
    mc "Hey!"
    show nova naked with Dissolve(1)
    nov "It's your mess! Only fair to use your shirt to clean up."
    mc "Grr..."
    nov "Don't give me that. Goes with the territory, right?"
    mc "Fine. At least you didn't use a clean one."
    nov "Oh, stop your bitching - It's not like you do the laundry around here anyway."
    "[Nova] gets into bed."
    nov "Well, I don't know about you, but that wore me out."
    mc "Yeah."
    nov "That was just some stress relief, OK? Nothing to be ashamed of... right?"
    mc "Right... No big deal, just a physical thing."
    "You crawl into bed."
    nov "Right. Only physical."
    stop music fadeout 2
    if NovaLove >= 6:
        scene CH5NovaSex35A with Dissolve(2)
        hide window
        w ""
        "As you climb into bed, [Nova] wraps her arms around you. You remain like this until you eventually fall asleep."
    else:
        scene CH5NovaSex35B with Dissolve(2)
        hide window
        w ""
        "You climb under the covers with [Nova]. Though you are both silent, it takes you what seems like an eternity to fall asleep."

jump Day11WakeUp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
