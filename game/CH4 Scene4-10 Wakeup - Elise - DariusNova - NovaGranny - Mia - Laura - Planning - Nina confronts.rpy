label Day7Start:
    stop music fadeout 1
    scene black with Dissolve(3)
    "A few minutes later you fall asleep."
    pause 3
    scene farm bedroom with Dissolve(2)
    "You wake up to the sun shining through your windows."
    "You stretch and look around. You don't see [Nova] anywhere."
    if NovaBlanket == 2:
        mc "{color=#b7b7b7}{i}Did she go back to dad's room?{/i}{/color}"
    elif NovaBlanket == 1:
        "You shiver as you wake up."
        mc "{color=#b7b7b7}{i}OK, remind me not to sleep here without a blanket again. Man, it's cold this morning!{/i}{/color}"
        mc "{color=#b7b7b7}{i}I wonder if [Nova]'s up yet?{/i}{/color}"
    else:
        mc "{color=#b7b7b7}{i}Weird, it's not like [Nova] to get up early. Where is she?{/i}{/color}"
    "You roll out of bed and put on your clothes. You notice a faint smell of fish coming from the kitchen."
    scene kitchen with Dissolve(2)
    "You walk out of your room and the smell is stronger. When you arrive there you see [Nova] hard at work over a soup pot."
    show nova neutral with Dissolve(1)
    play music nova
    nov "Finally up?"
    mc "Yeah. What are you doing?"
    show nova smirk 2 with Dissolve(0.2)
    nov "Making breakfast. I mean, what else would I be doing?"
    mc "Making a witch's brew that will enslave the whole town?"
    nov "Yeah, not in the mood today. Maybe next week!"
    if NovaBlanket == 1:
        show nova blushing with Dissolve(0.2)
        nov "Um... I guess you dropped off a blanket last night."
        mc "Yeah, it looked like you were freezing."
        nov "I just wanted to spend some time with him, you know."
        mc "You don't need to explain."
    elif NovaBlanket == 2:
        show nova annoyed with Dissolve(0.2)
        nov "I can't believe you carried me to bed last night."
        mc "Yeah, I threw out my back because you were so heavy."
        show nova angry with Dissolve(0.2)
        nov "I'm not heavy, you just have the arms of a 5 year old."
        mc "Well, excuse me for caring."
        show nova blushing with Dissolve(0.2)
        nov "I didn't say it wasn't nice."
    nov "Anyway, after I did the inventory last night I just wanted to see how Redd was doing. And he seemed so weak..."
    nov "He was tossing and turning, I just meant to stay with him until he fell asleep. I guess I did first."
    mc "I'm sure he appreciated you being there."
    show nova worried with Dissolve(0.2)
    nov "I don't even think he knew I was."
    nov "Before he calmed down he grabbed my hand and begged me to help him and his wife have a child."
    nov "I didn't know how to react. He was somewhere else."
    mc "The fever's getting worse, then?"
    show nova sad with Dissolve(0.2)
    nov "Yeah. You think we should just say \"Fuck it\" and go now?"
    mc "We need to do this right. I want to go now too, but..."
    "[Nova] shakes her head."
    nov "I know."
    nov "Now go sit down, the soup's almost done."
    nvl clear
    hide nova with Dissolve(1)
    n "You sit at the kitchen table as instructed and a few minutes later [Nova] comes out with a couple of bowls of fish soup."
    n "She sets one down in front of you and sits down at the table."
    n "The soup smells great."
    mcn "Wow!"
    novn "Not the best I've ever done, but it should keep us going today."
    mcn "Yeah."
    nvl clear
    show nova neutral with Dissolve(1)
    nov "Ok, now I did an inventory on our supplies..."
    mc "And?"
    nov "Worse than I thought in some ways. Better in others."
    mc "That's not telling me much."
    nov "We've got no tents. No sleeping bags. Absolutely zero dried foods."
    nov "So that's the bad news."
    nov "The good news is that your flint set still works. We've got a hand axe, your dagger and a cast iron pot. Which I'm using right now."
    mc "And I have my fishing pole too. Just in case."
    nov "Yeah. I don't think we'll be gone that long, and if we are..."
    mc "{color=#b7b7b7}{i}We're probably not coming back.{/i}{/color}"
    show nova worried with Dissolve(0.2)
    nov "So how is it?"
    mc "What?"
    show nova annoyed with Dissolve(0.2)
    nov "The soup?"
    mc "Oh, right."
    "You take a spoonful of the soup. It's the best warm meal you've had in recent memory. Not that you've had a lot."
    mc "It's great."
    show nova smirk with Dissolve(0.2)
    nov "Good! I hope Redd likes it. I read that if he takes his medicine with food it might help it work better."
    mc "It can't hurt to try."
    "[Nova] sighs."
    show nova neutral with Dissolve(0.2)
    nov "So, when is Elise expecting you?"
    mc "She didn't set a time. But I figure the sooner the better."
    nov "Yeah."
    mc "The elder usually has soke work that needs doing too, so I'll go there after."
    nov "Ater your trip to the MILF's house can you check with Mia? I don't like leaving Redd alone right now. But I need to get paid too."
    mc "Don't stress out over it, I'll get the stuff we need."
    nov "The question is, when? If we both work, we'll go twice as fast."
    nov "And there's more then enough work out there. I'll scrounge up something."
    if NovaDarius == 1:
        nov "I don't like the idea much. But Darius said there was more work."
        nov "He's starting to creep me out a bit, though."
        jump NovaDariusLastChance
    jump Day7Start2

menu NovaDariusLastChance:
    "Don't say anything.":
        jump Day7Start2
    "You know what, don't bother with him. [gr]\[Nova\]":
        mc "[Nova], just forget Darius. He's a creep. And as crazy as things are..."
        nov "You were all for it before."
        mc "You don't trust him, and I trust your instincts. If you think he's going to try something, why take the risk?"
        nov "Was that almost a compliment?"
        mc "Almost. Don't tell anyone."
        nov "OK, then. No Darius. I'll see what else I can drum up."
        $ NovaDarius = 0
        jump Day7Start2

label Day7Start2:
    "You finish your soup and once she has done the same, [Nova] goes to check on Redd. You follow her."
    "The shades in Redd's room are still drawn; Silas said that, in his condition, the sunlight would bother him."
    play sound bedroomdoor
    play music reddsick fadein 1
    scene farm redd room with Dissolve(2)
    dad "Oh, there you are!"
    nov "Hi, Redd!"
    mc "Hi, dad!"
    scene redd sick 7 with Dissolve(2)
    dad "Please tell me whatever smells so good is almost ready."
    nov "I made some soup, Redd. I'll bring it to you in a sec."
    nov "But it's great to see you in high spirits! You seem a lot better than last night."
    dad "I don't even remember last night, really. Was I asleep?"
    nov "Mostly."
    dad "Well, I feel fine now. I'll be up and about in no time."
    "[Nova] smiles."
    mc "That's great to hear, dad!"
    "Redd seems to ignore you. He focuses on [Nova]."
    dad "Now, before I eat, we need to have a serious discussion. I just don't think she'll be willing to help us."
    nov "Mia? She'll be here later."
    dad "No, who's Mia? I meant Sel..."
    "Redd stops for a moment. He looks around at you, confused."
    dad "[MC], [Nova]?"
    dad "There you are! What's for breakfast? Whatever it is it smells great."
    "You and [Nova] look at each other for a moment. She looks heartbroken."
    dad "Kids, relax. I know I'm a little under the weather, but we'll pull through."
    nov "Yeah... you're right, Redd. Let me get your soup."
    dad "Thank you, honey."
    "[Nova] gets up and heads out of the room."
    scene redd sick neutral with Dissolve(2)
    mc "{color=#b7b7b7}{i}I didn't think that this poison would mess with his mind so much. This is awful. How do I even respond?{/i}{/color}"
    dad "Any plans for the day, son?"
    mc "Um... Yeah. I'm going to visit Elise; she still has some work for me to do."
    scene redd sick joking with Dissolve(1)
    dad "Oh! You sly dog! You're using it as an excuse to confess to Sophie, aren't you?"
    mc "Dad! She shot me down already, you know that!"
    scene redd sick serious with Dissolve(1)
    dad "Oh, right... sorry, I forgot."
    mc "No big deal, dad."
    "You hear the door open behind you."
    play sound bedroomdoor
    nov "Just go, [MC]. I've got this."
    "[Nova] has a bowl of soup in her hand. She forces as smile as she walks up to Redd."
    mc "But he's..."
    "You nod."
    mc "I'll be home soon, then."
    mc "Take care, dad."
    "[Nova] looks at you with watery eyes. You don't say another word and head out to see Elise."
    stop music fadeout 1
    scene black with Dissolve(2)
    play sound knock1
    scene elises house with Dissolve(2)
    "Once you arrive there you knock on the door. A few moments later Elise opens up for you."
    play sound frontdoor
    show elise neutral with Dissolve(2)
    play music elise fadein 1
    eli "Oh, you made it! Great!"
    mc "Good morning."
    eli "Come on in."
    "Elise invites you in and you follow her to the kitchen."
    eli "Did you eat breakfast?"
    mc "Yeah, [Nova] made some fish soup."
    eli "Oh! Did the roads to town open up?"
    mc "No, I caught some yesterday."
    eli "You really are a handy one! I could use a man like you around the house."
    mc "Well, I'm here now."
    mc "{color=#b7b7b7}{i}Wouldn't it be great if she wanted some more \"lotion\"? I'd love to take out my mind from everything else for a while.{/i}{/color}"
    eli "Yes you are! And not a moment too soon."
    "Elise grabs you by the hand and takes you to a secluded area of her kitchen."
    mc "{color=#b7b7b7}{i}Come on! PLEASE!{/i}{/color}"
    eli "It's been a few days and my garden is still completely waterlogged. I spoke with Silas and he says it could be days or more before the ground is ready for gardening again."
    mc "Oh, you need help with your garden. Yeah. OK."
    mc "{color=#b7b7b7}{i}Damn it.{/i}{/color}"
    eli "Apparently I should have built it on a slope. But I was thinking..."
    eli "The storm took out most of the plants I had there anyway. Maybe I could transplant them inside."
    mc "Will they get enough sun?"
    eli "Yes. I can keep them by the window. I'll water them myself."
    mc "It should be doable."
    eli "I'll pay you, of course. It's a bit too much for me to do on my own, and if you could put up the shelves too, that would be great."
    mc "OK. Let's do the shelves first."
    "Elise leads you to the area where she wants to set up her garden."
    eli "Here they are."
    scene black with Dissolve(2)
    "You get to work setting up her shelves."
    scene elises house with Dissolve(2)
    show elise neutral with Dissolve(1)
    eli "Perfect!"
    mc "Let me get these pots and let's move the seedlings now."
    eli "Thanks again!"
    scene elises garden with Dissolve(2)
    nvl clear
    n "You go outside and start on the garden."
    n "Some of the plants are already drowned. But you're able to save a surprising number of them."
    n "After repotting the plants and positioning them near the windows, you smile."
    mcn "Ok. That about covers it!"
    nvl clear
    jump EliseBJ

label EliseBJ:
    scene elises house with Dissolve(2)
    show elise neutral with Dissolve(1)
    eli "You're a real lifesaver, [MC]!"
    eli "Let me get this last one."
    scene EF1 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Her ass is just so fucking... I was really hoping she'd want to continue on from yesterday.{/i}{/color}"
    "Elise places the final set of herbs on the shelf."
    scene elises house with Dissolve(2)
    show elise neutral with Dissolve(1)
    eli "Done, and with time to spare. I'm going to have to use you all the time when I need-"
    "Elise turns around and stops in mid sentence. You can tell she's staring at your crotch."
    mc "{color=#b7b7b7}{i}Oh shit. Note to self: get roomier pants.{/i}{/color}"
    eli "Uh... you've got..."
    mc "Sorry, I just was thinking a bit about yesterday..."
    eli "Oh, this is so embarrassing... I'm so sorry."
    mc "Sorry? Why?"
    eli "I feel like I took advantage of you. And you shouldn't have to force yourself with an old woman like myself."
    mc "Forcing? OK, you know this hard on is one hundred percent because of you, right?"
    eli "It's nice that you find me attractive, but this is not going to work."
    mc "But didn't you tell me you needed this every day?"
    eli "Yes, but..."
    mc "I thought you had fun last time."
    eli "[MC], we are not doing this for fun, remember? Anyway, it's wrong."
    mc "Why?"
    eli "You're Sophie's age... I could be your mother!"
    mc "If I don't care why should you?"
    mc "You're gorgeous."
    eli "Oh my... If word got out..."
    mc "I won't tell anyone."
    eli "You promise?"
    mc "Cross my heart!"
    eli "Hum... OK, damn it all, why am I even fighting this? Quickly now, pull out your cock and let's get this over with."
    mc "So romantic..."
    scene EF2-1 with Dissolve(2)
    hide window
    w ""
    "Elise pulls out her tits and kneels in front of you as you release yourself from your trousers."
    eli "Sophie is upstairs so we need to do this quickly. You can do it, right?"
    mc "{color=#b7b7b7}{i}Pulling her tits out of her dress so quickly in front of me... I will never get tired of looking at her tits!{/i}{/color}"
    mc "Uh... Sure, I'll try my best, but..."
    eli "You know what? It'll go faster if I use my hands. Would you like that?"
    "You nod."
    scene EF2-2 with Dissolve(2)
    hide window
    w ""
    "Elise begins jerking you off with expert technique."
    mc "Aaah..."
    eli "Quiet, we don't need Sophie to hear us!"
    mc "Sorry!"
    "Elise grins and keeps up her movements. Her hands are soft, but extremely adept at touching the right places on your dick. She spends some extra time rubbing her palm against your glans after spitting on it."
    "She seems to take a perverse pleasure in watching the expression on your face as she pleasures you."
    mc "Oh! I'm going to..."
    stop music
    sop "HEY!"
    scene EF2-2 with hpunch
    "You freeze in place, as does Elise. She whispers to you."
    eli "Oh shit! Put that away!"
    scene elises house with Dissolve(2)
    play music sophie fadein 1
    sop "Mom? Where are you? I'm heading out."
    show elise neutral with Dissolve(1)
    "Elise quickly fixes her drees and you hastily shove yourself back into your pants."
    eli "Oh... that's nice dear. I'm in the kitchen."
    show sophie neutral at slightleft with easeinright
    show elise neutral at slightright with easeinleft
    sop "[MC]! I didn't know you were here."
    mc "I was helping your mom-"
    eli "Transplanting the garden inside! I'm surprised you didn't hear him."
    sop "Yeah, whatever. I'm heading out to see Toby and... wait. Do you have a hard-on?"
    "You quickly cover your pants with your hands."
    sop "Oh my God! You are such a freak! Mom! Don't let him go near you! And stop inviting this freak to our house!"
    "Sophie seems to stare at you for a few seconds contemplating the situation."
    mc "I, uh..."
    sop "Goddess! You perv on everyone, don't you?"
    eli "Sophie! Don't be rude."
    sop "I'm not the one hiding a blackjack in my pants."
    mc "It's not w-"
    sop "Whatever. Not my problem. Anyway, Lisa left something here last time she was over. I'm dropping it off and I'll be back in a few minutes."
    eli "Sure thing, honey."
    sop "And [MC]?"
    mc "... Yeah?"
    sop "Take care of that shit. Get laid, jerk off, whatever. Getting hard next to my mother... It's fucking gross! "
    hide sophie with easeoutleft
    show elise neutral at center with easeinright
    stop music fadeout 1
    eli "That was too close! You should go."
    mc "Like this? I don't really feel like walking around at full mast."
    eli "Wait, are you even harder than before? Did almost getting caught by Sophie..."
    "Elise smiles."
    eli "Come on. Upstairs."
    "You follow Elise up to her bedroom."

    play music elise fadein 1
    scene EF2-3 with Dissolve(2)
    hide window
    w ""
    "She enters the room and takes off her dress."
    eli "We still need to hurry; Sophie could be back anytime! This should give you some extra motivation."
    eli "Do you like what you see?"
    mc "Very much."
    "Elise sits down on the bed and beckons you to her."
    eli "Now get those clothes off, sweetheart."
    "You get naked and stand in front of her."
    scene EF2-4 with Dissolve(2)
    hide window
    w ""
    eli "You really are huge. Not everyone is as lucky as you are."
    "Elise starts jerking you off again. Faster this time."
    mc "OH, YES!"
    scene EF2-5 with Dissolve(2)
    hide window
    w ""
    "She speeds up, spitting in her hand for extra lubrication."
    eli "Come on, cum for me! I know you want to see me covered in your cum again!"
    mc "I do. I really do!"
    eli "You seem to be taking longer than last time though."
    mc "It's just..."
    eli "What? Sophie could be back at any moment and there's no way we're explaining away you naked in my room."
    mc "Yeah, I know, but the pressure is making it hard to..."
    eli "Oh. Boys and their performance anxiety."
    scene EF2-6 with Dissolve(2)
    hide window
    w ""
    eli "OK. Just this once."
    "Elise slides her lips over your cock and begins to suck."
    mc "AAAAH!"
    "Loud sounds of slobbering fill the room. You groan as you feel the dual pleasure of her tongue swirling around you cockhead as she sucks in the rest of you."
    scene EF2-5 with Dissolve(2)
    eli "You know, it's been so long since I've sucked a dick. Especially one this big and hard!"
    mc "Don't stop..."
    eli "Oh, now you're the impatient one! You're so cute. Don't worry [MC], there's a lot more coming."
    scene EF2-7 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}She's so energetic. It's like she's having more fun now than I've ever seen her have. I wonder how long it really has been since she's done something like this.{/i}{/color}"
    mc "Aaah..."
    mc "{color=#b7b7b7}{i}Where was I... Oh, who cares, she's a dick sucking master!{/i}{/color}"
    scene EF2-8 with Dissolve(2)
    hide window
    w ""
    "You begin to buck your hips against Elise and she takes you in deeper. You grab the back of her head for support."
    eli "MMph... crflll..."
    "Your cock slides further into Elise's wet mouth and you feel it hit the back of her throat."
    scene EF2-9 with Dissolve(2)
    hide window
    w ""
    "You feel the suction of Elise's lips travel up and down your shaft. You guide her with your hands and she grasps onto your legs and ass for support."
    "Drool falls from her lips and runs down to your balls, and the floor below. You can no longer speak but simply grunt in affirmation."
    scene EF2-10 with Dissolve(2)
    hide window
    w ""
    "As you feel your release coming you push Elise's head as far as it will go."
    "When you feel your dick hit the back of her throat you let out a mighty satisfied grunt and explode inside of her."
    scene EF2-11 with Dissolve(2)
    hide window
    w ""
    "A few moments later, your orgasm subsides. You release your grip on her head and Elise slowly removes herself from your cock."
    "You see strands of sperm mixed with saliva coating your cock as she slips it out. She wasn't able to take it all."
    scene EF2-12 with Dissolve(2)
    hide window
    w ""
    "Elise looks up at you with her mouth full of cum. She runs her tongue around, playing with it in front of you."
    "Then she closes her mouth and swallows. Smiling at you all the while."
    scene EF2-13 with Dissolve(2)
    hide window
    w ""
    mc "Wow, Elise."
    eli "Weren't you supposed to cum on my face?"
    mc "Shit! Sorry."
    eli "It's fine, but a little warning would be nice. If you try that again without asking this arrangement is over."
    mc "I really didn't mean to. It just felt so good that I wasn't even thinking."
    "Elise gives you a wicked smile."
    eli "It's all right. Some girls like being treated a little rough from time to time."
    scene EF2-14 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}Wow, I think she's really wet down there.{/color}"
    scene EF2-13 with Dissolve(2)
    eli "Hey, where are you looking at? I just gave you an incredible blowjob, don't press your luck."
    mc "Of course ma'am."
    eli "It's nice to see I've still got it! You'll have to make it up to me, though. I'll need a double next time!"
    mc "A double?"
    eli "You came in my mouth, I need it on my face. Or have you already forgotten why we we're doing this?"
    mc "Oh, right. For science."
    scene elises bedroom with Dissolve(2)
    show elise neutral with Dissolve(1)
    mc "I'm always ready to serve!"
    eli "Aren't you the eager little gnome?"
    mc "When it comes to hot women, what can I say?"
    eli "OK, lover boy. Get dressed and meet me downstairs."
    jump FinishEliseDay7

label FinishEliseDay7:
    scene black with Dissolve(2)
    "You get dressed and head down. Elise follows you a couple of minutes later."
    scene elises house with Dissolve(2)
    show elise neutral with Dissolve(1)
    eli "Well. That was another productive day."
    mc "No lie."
    eli "Here's your payment."
    "Elise holds out a bag of coins and you take them from her."
    mc "Thanks."
    eli "No, thank you."
    $ persistent.elise_facial2 = True
    $ renpy.end_replay()
    eli "But I might need a few days to recover before our next session."
    eli "When I need more work done around the house I'll send for you."
    mc "I'll be waiting."
    "Elise sees you out."
    play sound frontdoor
    scene elises garden with Dissolve(2)
    mc "{color=#b7b7b7}{i}Well, that was great stress relief if nothing else. And it looks like she paid me really well too!{/i}{/color}"
    mc "{color=#b7b7b7}{i}With one or two more jobs today I should have enough to buy the gear we need. That means I should check with the elder, and let's just pray that he didn't notice his missing book.{/i}{/color}"
    stop music fadeout 1
    "Meanwhile..."
    scene nina house exterior with Dissolve(2)
    "[Nova] knocks on the door of Nina's house."
    "An old woman answers the door."
    show grandma neutral with Dissolve(2)
    play music grandma fadein 1
    gra "Oh, if it isn't [Nova]. What brings you to the most boring house in the village?"
    gra "Are you looking to challenge Nina to a fight to the death over the cock of some young stud?"
    nov "No, that'll be Sunday. Today I'm just looking for work."
    gra "Never delay a death battle, dearie. But it's just as well. She's off with Bobby Broadsword."
    nov "Trevor?"
    gra "Is that his name?"
    gra "What a nice boy. He's growing a nice set of horns, but who am I to interfere?"
    nov "Uh, sure... so... work?"
    gra "Oh, right. My good for nothing son is off trying to sell apples. My daughter-in-law is helping one of our neighbors clean up."
    gra "Which is pointless - things just get messy again. On a good day."
    nov "I'll look around somewhere else then. It was nice seeing you!"
    gra "Now hold your horses, I didn't say there was no work. We've actually got some trash that I need help moving."
    gra "And it's a bit too much for my little old lady's back."
    nov "I can help you with that!"
    gra "Well of course you {i}can{/i} help. But WILL you help?"
    nov "Will you pay?"
    gra "Not going to help out of the kindness of your heart?"
    nov "I would, but I need to make some money now."
    gra "HA! Straight and to the point. Fine. Follow me."
    scene grandmabasement with Dissolve(2)
    "Nina's grandmother leads [Nova] down to her basement."
    nov "WOW! Gah... it smells like death down here."
    show grandma neutral with Dissolve(2)
    gra "Yeah. How strange, right?"
    gra "It's just rotting ficuses."
    nov "Ficuses?"
    gra "Yes, they tried to get into the house so I had them pulled."
    gra "Now, can you help me move the box?"
    nov "Uh, sure..."
    hide grandma with Dissolve(1)
    "[Nova] grabs one end of the box and Nina's grandmother picks up the other end."
    nov "What the hell? Is there a dead body in here?"
    gra "{i}A{/i} dead body. That's cute."
    gra "Do you think I'd need help then? Come on, this is just trash."
    scene black with Dissolve(2)
    "Amid several grunts and moans, Nina's grandmother and [Nova] carry the box out towards the well."
    scene well day with Dissolve(2)
    show trevor annoyed at slightright with Dissolve(1)
    show nina neutral at slightleft with Dissolve(1)
    tre "Come on! Just, I don't know, touch it a little?"
    nin "Not now, Trevor! It's the middle of the day and-"
    tre "Tonight then?"
    show nina angry with Dissolve(0.2)
    nin "Trevor! Just drop it."
    show trevor neutral with Dissolve(0.2)
    tre "I don't get it. You've been cold as stygia ever since you came back."
    nin "I... I'm sorry. It was just a tough time."
    tre "Yeah, I know, but we've barely spent any time together since you got back."
    nin "I know what you mean by time. I heard you talking to Toby. Just be honest; by time you really mean sex. I told you I wasn't ready yet."
    tre "No! I'm just concerned about you, OK?"
    show trevor angry with Dissolve(0.1)
    tre "And you know what? I think I've been more than patient on that end."
    nin "..."
    tre "Just forget I said anything."
    gra "Bah! Back in my day a boy would have thrown you down and had his way with you. Consequences be damned."
    show nina surprised with Dissolve(0.2)
    nin "Grandma? What are you doing here?"
    show nina surprised at slightleft with easeinleft
    show trevor neutral at farleft with easeinright
    show grandma neutral at offscreenright
    show nova neutral at offscreenright
    show grandma neutral at slightright with Dissolve(1)
    show nova neutral behind grandma at farright with Dissolve(1)
    gra "Throwing out some spoiled trash from the basement."
    gra "[Nova] here was kind enough to assist an old lady when her only granddaughter ran off to be with her lover."
    show nina neutral with Dissolve(0.2)
    nin "Oh, come on grandma! It's not like that. Anyway, you didn't even say you needed help."
    gra "Oh, didn't I? I wonder why that was?"
    show grandma neutral behind nova with Dissolve(0.2)
    nov "No offense Nina, but can you get out of the way? This is really heavy."
    gra "You need to build more muscle, dear. Especially if you're going to run that farm someday."
    nov "That's a great line of conversation after we've dumped this thing."
    tre "You guys need some help?"
    gra "No, we've got it."
    nov "Do we?"
    gra "Set it over there, by the cliff."
    "[Nova] and Nina's grandmother set the crate down on some rocks by the edge of the cliff."
    show grandma neutral at farright with easeinleft
    show nova neutral at slightright with easeinleft
    nov "HAH!!! Ooof... you're stronger than you look, old woman."
    nin "Yeah, that's grandma for you."
    gra "You kids today are soft is all. Back in my day..."
    nin "Nonono! Not right now! We can hear your stories later."
    gra "See? This is how my family treats me. You love me still, right [Nova]?"
    nov "Sure thing, grannie."
    gra "Nice to see I still get some respect."
    "Nina hugs her grandma."
    show nina smiling with Dissolve(0.2)
    nin "Oh, you know I love you. Even if you are a little weird."
    gra "You'd better after all the times I covered for you with your father when you were out gallivanting."
    show nina neutral with Dissolve(0.2)
    tre "What's in that box? The stench is... special."
    gra "Just some ficuses."
    tre "I'm pretty sure that they don't smell like dead animals..."
    gra "Well, our basement flooded. You know how things rot when water gets to them. And don't even tell me about the bloating."
    nin "You had ficuses in the basement?"
    gra "Only one to be fair."
    show nova surprised with Dissolve(0.2)
    nov "One? Then what else was in that..."
    play sound woodcrash
    show nova surprised with Dissolve(0.2)
    show nina surprised with Dissolve(0.2)
    "Before [Nova] can finish her sentence she hears a crack and the crate falls off the side of the cliff."
    gra "Oh darn. And we aren't supposed to dump off the cliff. No big deal. With the water levels as high as they are I'm sure the contents of that crate will never be seen again."
    show nina neutral with Dissolve(0.2)
    nin "You're being weird again, grandma."
    show nova neutral with Dissolve(0.2)
    gra "I am not!"
    "Nina's grandmother turns to [Nova] and hands her some coin."
    show nova surprised with Dissolve(0.2)
    nov "Forty? That's way too much!"
    gra "You'll need it, dear. Not to mention, always make sure to pay someone well when they help you get rid of some... ficuses."
    show nova neutral with Dissolve(0.2)
    nov "Um, thanks. I really needed this."
    nin "Oh? Is everything OK?"
    show nova annoyed with Dissolve(0.2)
    nov "Well, if you'd been paying attention you'd know Redd is very sick."
    show nina worried with Dissolve(0.2)
    nin "I thought he was doing better!"
    nov "He will be. Soon."
    nov "Maybe you should come by later and visit the deathly ill father of your best friend. You know, the one who's known you since you were a kid?"
    show nina angry with Dissolve(0.2)
    "Nina goes to respond. Then stops herself."
    tre "Hey! She's been in pretty bad shape after the-"
    nov "Yeah, yeah. Whatever."
    show nina worried with Dissolve(0.2)
    nin "And um, is [MC] OK?"
    nov "Ask him yourself."
    "[Nova] turns to Nina's grandmother."
    show nova neutral with Dissolve(0.2)
    nov "Thanks, grannie. I gotta go check on Redd."
    gra "Not at all. It was fun."
    nov "See you."
    jump ElderDay7

label ElderDay7:
    stop music fadeout 1
    scene black with Dissolve(2)
    "Meanwhile.."
    play music afternoon fadein 1
    scene village destroyed with Dissolve(2)
    "You head over to the elder's house ."
    mc "{color=#b7b7b7}{i}OK, I'm here. If he asks about the book, play dumb.{/i}{/color}"
    "You knock on Silas' front door."
    "Silas opens it and greets you."
    scene elders house with Dissolve(1)
    show elder neutral with Dissolve(2)
    eld "Oh! Good day, [MC]. Come in."
    eld "How's your father?"
    mc "He's... in better spirits."
    eld "That's good to hear. Have a seat, Mia should be out in a moment. She's getting ready to head over to your house."
    mc "The thing is..."
    eld "Huh? What is it?"
    mc "He's... this morning he had trouble remembering [Nova] and I."
    "The elder rubs his chin as he mulls over what you said."
    eld "Hmm..."
    mc "Is that normal?"
    eld "It isn't abnormal, exactly. The venomair spores are known to cause hallucinations."
    mc "And memory loss?"
    eld "It's possible. I don't quite recall seeing that on the list of symptoms. Let me check my book and see what it says."
    mc "{color=#b7b7b7}{i}Crap.{/i}{/color}"
    eld "Wait here."
    hide elder with easeoutleft
    "As the elder retires to his library, Mia comes out of a room holding a basket."
    show mia smiling with Dissolve(1)
    mia "Oh! Hello [MC]!"
    "She smiles at you warmly, with a bit of a blush in her cheeks."
    show mia neutral with Dissolve(0.2)
    mia "How's... is your father doing well?"
    mc "That's what we're trying to find out. He was acting a little strange this morning."
    mia "Was it the hallucinations?"
    mc "Yes, actually. It just really worried me."
    mia "Hmm..."
    show elder neutral at slightleft with easeinright
    show mia neutral at slightright with easeinleft
    "The elder returns."
    eld "It's the damnedest thing. I can't seem to find that book from last night!"
    "You look to the side awkwardly."
    mc "Weird."
    eld "Mia. Have you seen volume 4 of \"Monstrous Poisons and their Treatment\"?"
    mia "Which one was that?"
    "Mia looks over at you. You shift a bit."
    eld "Come now! The one which had the information on the effects of the venomair spores."
    mia "Well, if you were reading it, when did you see it last?"
    eld "Last night. I was here talking with [MC] about the Azureola."
    eld "Did you do a reorganization of my books again, Mia? You know how I hate that. My books are set up exactly how I like them!"
    show mia blushing 1 with Dissolve(2)
    mia "I..."
    mc "{color=#b7b7b7}{i}Damn. I think Mia might get in trouble because I stole the book from the elder last night.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Do I let her take the fall for this? Or should I come clean?{/i}{/color}"
    mc "{color=#b7b7b7}{i}Silas will probably be pissed though. And he might even figure out what I'm planning.{/i}{/color}"
    show mc neutral at center with Dissolve(1)

menu:
    "The book is too important. [gr]\[Corruption\]":
        hide mc with Dissolve(0.2)
        mc "{color=#b7b7b7}{i}Sorry Mia, but...{/i}{/color}"
        "Mia looks over at you again. You remain quiet"
        eld "Where did you put it? Come on now!"
        mia "I..."
        "She gives you one last look, and nods."
        $ Corruption += 1
        $ TellTruthMia = 0
    "Confess and help Mia. [gr]\[MiaLove\]\[MiaTruth\]\[Honor\]":

        hide mc with Dissolve(0.2)
        eld "Where did you put it Mia? Come on now!"
        mc "{color=#b7b7b7}{i}I need the book, but I can't let poor Mia get in trouble over this.{/i}{/color}"
        mc "Elder, it's not her-"
        "Mia cuts you off."
        mia "I should have said this earlier, but..."
        $ Honor += 1
        $ TellTruthMia = 1
        $ MiaLove += 1

label ElderDay7Part2:
    show mia neutral with Dissolve(0.2)
    mia "I'm sorry. I should have told you but I hoped to fix it before you noticed."
    mia "I wanted to brush up on the symptoms since I'm taking care of Redd now and I went to the lake to read."
    mia "But... I took too long. So I had to rush back here to get ready. I just noticed a minute ago I left the book up at the lake."
    eld "Mia, you could have just told me! But what have I said about my rare books?"
    mia "They aren't to leave the house."
    eld "That volume is extremely rare and expensive. If it were damaged by the rain or heaven forbid, dropped in the water..."
    mia "I'm sorry..."
    eld "Don't apologize dear, I know how you love to read. But you need to be a little more careful with these things."
    mc "It's OK, she was just trying to help."
    mc "{color=#b7b7b7}{i}I feel like a tool right now.{/i}{/color}"
    show mia ashamed with Dissolve(0.2)
    "Mia looks down, ashamed. The elder sighs."
    eld "Hey, don't look so down. I'm not angry, just promise me you'll be more attentive in the future."
    mia "I will."
    eld "That's all I needed to hear."
    mia "I'm sorry."
    "Silas smiles."
    eld "I know you are. I just don't want a replay of that time you lost \"The Elf, the Orc, and their Lover\"."
    mia "Uh!"
    "Mia blushes profusely."
    mc "The Elf, the Orc, and their what now?"
    eld "It's an amazing book on inter species mating and romance. A true classic. I especially like the sex scene with-"
    show mia blushing 2 with Dissolve(0.2)
    mia "Silas!"
    "Mia turns even redder, something you assumed was impossible."
    eld "Sorry!"
    mc "{color=#b7b7b7}{i}Poor Mia looks like she wants to crawl into a hole and die. She must really like that book too.{/i}{/color}"
    mc "So, the symptoms?"
    show mia neutral with Dissolve(0.2)
    eld "Right. I can't double check, but hallucinations and foggy memory are often linked, so it's quite possible that it's just the venom running its course."
    eld "Redd's body is trying to fight it off but it takes time to eliminate the venom from the blood."
    eld "If it gets worse let me know. Until then, Mia, just keep giving Redd his medicine."
    mia "I will."
    mc "Oh, and before I forget, is there any work that needs to be done around here? Or is there anyone in the area who needs anything?"
    eld "Nothing much yet. But we'll have the bulletin board back up within a couple of days. I'll also be putting together a detail to clear up the town."
    mc "Sounds like something I could help with."
    eld "I think so too. I'll let you know when we're ready."
    mc "Thanks."
    eld "Now Mia, if you want to get that book from the lake you should go now. You don't want to be late to tending to Redd."
    mia "Um, yes! Sure thing."
    "Mia goes to her room and brings back a large rucksack."
    eld "That's a pretty big bag, Mia."
    mia "It's just dinner, and some books. My own this time."
    eld "Ah. Right, you're still reading \"49 Shades of Green\"."
    show mia blushing 2 with Dissolve(0.2)
    mia "Um... I... bye, elder."
    hide mia with easeoutleft
    "Mia rushes past you out the door."
    show elder neutral at center with easeinright
    eld "Such a shy girl. But a sweetheart."
    mc "She is. I'm glad she's helping with dad."
    mc "Speaking of which, I should run. Maybe I can catch up with her."
    eld "As soon as I have more work you'll be the first to know."
    "You say goodbye to the elder and walk out the door."
    scene village destroyed with Dissolve(2)
    play music afternoon2 fadein 1
    show mia neutral with Dissolve(1)
    mia "Um..."
    mc "Hey, Mia."
    mc "Look, I'm sorry about-"
    mia "It's OK. Just be careful. The elder is really touchy when it comes to his books."
    if Honor > Corruption:
        mc "I hope you didn't get in too much trouble."
    else:
        mc "He needs to relax. It's just a book after all."
    mia "It's not like this is the first time this happened, but..."
    mc "Thanks for covering for me."
    show mia assertive with Dissolve(0.2)
    mia "What were you thinking?"
    mc "I just needed some more information on the Azureola. It's the only thing that can save dad for sure."
    mia "I know why. I meant why didn't you ask me for help?"
    show mia blushing 2 with Dissolve(0.2)
    mia "We're... friends. You and [Nova] and even..."
    mia "You could have asked me."
    mc "I didn't even think of it. I just saw the book last night, you weren't around."
    mia "That makes sense..."
    show mia blushing 2 with Dissolve(0.2)
    mia "But remember that from now on, OK?"
    mc "Promise."
    play sound walkgrass
    scene farm fixed with Dissolve(2)
    "You and Mia walk towards your house. She's barely saying a word. From time to time you notice her looking at you and it seems like she's about to speak."
    show mia ashamed with Dissolve(1)
    mia "..."
    "But she stops herself."
    mc "Is something wrong?"
    mia "No."
    mc "It's just... you seem like you want to say something."
    mia "..."
    "You arrive home at the same time [Nova] does."
    show mia blushing 2 at slightright with Dissolve(0.2)
    show nova neutral at slightleft with Dissolve(0.2)
    nov "Hey you two lovebirds!"
    show mia blushing 1 with Dissolve(0.2)
    mia "[Nova]!"
    nov "Relax, Mia, I'm just messing with you."
    nov "You get any gold today, [MC]?"
    mc "A bit. How about you?"
    nov "Had to work my ass off for it, but..."
    nov "Actually, let's go in first. I need to sit down."
    play sound frontdoor
    scene farm house interior with Dissolve(2)
    "You all enter the house. Mia goes off to check on Redd and you and [Nova] sit in the kitchen."
    scene farm kitchen with Dissolve(2)
    show nova neutral with Dissolve(1)
    nov "Here's what I've got. It's not bad, but not great either."
    mc "Yeah, same. The elder says there will be work, but not today. He's still organizing everything."
    nov "Well, it should be enough for a day or two."
    mc "Yeah. We'll be tight on food probably. And might have to skip the tent too."
    show nova annoyed with Dissolve(0.2)
    nov "Bleh."
    mc "It's not that bad sleeping under the stars."
    nov "Until you wake up covered in bug bites."
    mc "Just smear yourself with-"
    show nova neutral with Dissolve(0.2)
    nov "Any sentence that suggests smearing myself with ANYTHING is an automatic no go."
    mc "Hey, you want to itch for a week, be my guest."
    show nova angry with Dissolve(0.2)
    nov "Get a tent."
    mc "I'll try."
    nov "Try hard. Go see Laura, it's going to be dark soon."
    mc "Yeah. Just gonna check on dad first."
    hide nova with Dissolve(1)
    scene farm redd room night with Dissolve(2)
    "Mia is unpacking her bag and preparing Redd's medicine."
    show mia neutral with Dissolve(1)
    mia "He's sleeping."
    mc "Right."
    mia "He'll be fine. I promise."
    mc "Thanks. I'll be back soon."
    show mia smiling with Dissolve(0.2)
    "Mia smiles at you and wipes Redd's head."
    mia "I'll let him know."
    jump Day7Laura

label Day7Laura:
    scene black with Dissolve(2)
    "After a while..."
    play music laura fadein 1
    scene lauras shop interior with Dissolve(2)
    show laura neutral with Dissolve(1)
    lau "You're lucky I like you. Dad would have a heart attack if he knew I was cutting you a deal like this."
    mc "Thanks!"
    lau "What's with all the gear though? Nina mentioned you liked camping or whatever when she was giving me the \"date my buddy\" pitch..."
    mc "Oh, so I was funny and liked camping. Doesn't sound weird at all."
    show laura smiling with Dissolve(0.2)
    lau "I never said it was a GOOD pitch."
    lau "I'm scared to ask how she pitched me for you."

menu:
    "She said you gave good head. [gr]\[Laura Love\]\[LauraCanSuck\]":
        mc "Well, I didn't bring it up at the party, but she said you could suck a man off in half a minute."
        show laura surprised with Dissolve(0.2)
        lau "I told her to keep that to herself!"
        mc "Just kidding! Wait, really?"
        show laura smiling with Dissolve(0.2)
        lau "Wouldn't you like to know?"
        if FuckedLaura == 1:
            lau "And I'd love to show you."
            show laura neutral with Dissolve(0.2)
            lau "But we both know that's a bad idea."
        else:
            "Laura winks at you and smiles."
        "You swallow, and look around a little uncomfortably."
        $ LauraLove += 1
        $ LauraCanSuck = 1
    "Nothing in particular.":

        mc "Nope. Just the personality thing."
        show laura smiling with Dissolve(0.2)
        lau "She really needs to be a better salesman. For me she could have said: Hot, huge tits, gives amazing head."
        if FuckedLaura == 1:
            lau "As for you, she could just say: Cute, a little naive in an endearing way, and has a huge cock. Pretty good in the sack."
        mc "How would she have known that last part?"
        lau "How indeed?"
        "You look around uncomfortably."

label Day7Laura2:
    show laura neutral with Dissolve(0.2)
    mc "So, the tent?"
    lau "Yeah, I checked in the back. Look, I can only stretch things so far, [MC]. Even for a cutie like you."
    mc "No problem. I don't want to put you out."
    "You watch as Laura finishes placing your purchases on the counter."
    lau "You know, this seems like a lot for one person."
    mc "It's not just one person."
    show laura smiling with Dissolve(0.2)
    lau "Uh, OK then! Romantic getaway?"
    mc "Not at all - I'm hunting for some herbs."
    lau "With what you're spending here, you'd be better off just buying them."
    mc "Do you have Azureola in stock?"
    show laura surprised with Dissolve(0.2)
    lau "Azur-what now?"
    mc "Exactly."
    show laura neutral with Dissolve(0.2)
    lau "So why the Azureola thing? Does it get you hella high or something?"
    mc "What? No, I need it for my dad's medicine."
    show laura surprised with Dissolve(0.2)
    lau "Oh. Wait, is your dad OK?"
    mc "He caught some bad spores because of the storm. He's in pretty rough shape."
    lau "I didn't know... I'm sorry."
    mc "Not your fault, but considering how fast news travels in this town I just assumed you knew."
    show laura neutral with Dissolve(0.2)
    lau "Perils of being the new girl, I guess. I don't get timely gossip."
    mc "So nothing to share? I figured you for the girl who'd know it all."
    lau "Please. I'm going through gossip withdrawal. Nina's garbage at it!"
    mc "Yup. [Nova]'s always got her ear to the ground though, talk to her sometime."
    lau "Need anything else for your big trip?"
    mc "I've got flint, rope, climbing gear - which I hope I won't need - and dried foods. So yeah, looking good."
    lau "Where are you going?"
    mc "{color=#b7b7b7}{i}Best not say \"Goblin Mountain\".{/i}{/color}"
    mc "The woods on the mountain to the west. I might have to climb up a bit to get to the Azureola, so the gear is just in case."
    lau "Does it get cold up there?"
    mc "A bit, but we'll have a fire."
    lau "Hold on."
    hide laura with easeoutleft
    "Laura walks down to the basement; you hear some shuffling and she comes back up with some folded canvas in her hands. She places it on the counter."
    show laura smiling with easeinleft
    lau "The tent."
    mc "I thought you said-"
    show laura neutral with Dissolve(0.2)
    lau "I'm not giving it to you. I'm lending it to you."
    mc "Really? You're the best!"
    show laura smiling with Dissolve(0.2)
    lau "Don't I know it?"
    mc "I have to run then."
    lau "Aww, so soon?"
    mc "I have a lot to do before tomorrow."
    show laura neutral with Dissolve(0.2)
    lau "Don't be a stranger."
    mc "I won't."
    "You grab your camping gear and head home."

label Day7Preparation:
    scene farm house interior night with Dissolve(1)
    "You arrive at your house with your supplies."
    mc "[Nova]! I'm back!"
    nov "Took you long enough."
    show nova neutral with Dissolve(1)
    if FuckedLaura == 1:
        nov "Busy with something else?"
        mc "What do you mean?"
        show nova smirk with Dissolve(0.2)
        nov "Something, I dunno... groiny?"
        mc "No! We were busy-"
        nov "That's what I said."
        mc "Anyhow! I've got the gear."
    show nova neutral with Dissolve(0.2)
    nov "Cool! You even got a tent."
    mc "She lent it to me."
    if FuckedLaura == 1:
        show nova smirk 2 with Dissolve(0.2)
        nov "Yep, definitely wants it again."
        mc "Stop it!"
        nov "I'm just sayin!"
    show nova neutral with Dissolve(0.2)
    nov "Laura must really like you. Or pity you."
    nov "You did good."
    mc "Your validation just makes my night."
    show nova smirk with Dissolve (0.2)
    nov "That's why I'm here."
    nov "Dinner's in the kitchen."
    mc "Goddess, I've been so busy I forgot I was hungry."
    nov "Come on."
    scene farm kitchen night with Dissolve(1)
    "[Nova] leads you to the kitchen."
    "You sit down and start to eat."
    mc "So, how's dad?"
    show nova neutral with Dissolve(0.2)
    nov "Still sleeping. Mia's looking over him. She says he's stable, so that's good."
    mc "Yeah, he just needs to hold out for a few more days. If we get the flower..."
    nov "When."
    "You nod."
    mc "When we get the flower. He'll be back on his feet in no time."
    nov "Damn right he will."
    mc "I guess we'd also better ask Mia if she can stay with him all day over the next few days. Just in case."
    nov "Yeah. I feel bad putting it on her though."
    mia "Don't."
    "You and [Nova] look up and see Mia standing at the entrance to the kitchen."
    show nova neutral at slightright
    show mia neutral at slightleft with easeinright
    mia "Don't feel bad for asking. I..."
    mia "I would do it."
    "[Nova] runs over and hugs Mia tightly."
    show nova neutral at center with easeinright
    nov "Thank you!"
    mia "But I can't."
    "[Nova] lets go and looks at Mia confused."
    show nova sad at slightright with easeinright
    nov "Oh... I should have known you'd be busy."
    mia "I am..."
    nov "Sorry."
    "[Nova] looks crestfallen."
    mc "What's going on, Mia? I hate to ask, but can you maybe postpone? I don't think we have anyone else who could do it."
    mia "I... I have two friends who really need my help. So I'm going out to..."
    stop music fadeout 2
    "Mia swallows; she seems to be steeling her courage."
    play music westandtogether
    mia "I'm going to Goblin's Mountain with them."
    mc "What are you saying?"
    show nova surprised with Dissolve(0.2)
    show mia assertive with Dissolve(0.2)
    mia "[MC], I might be a little awkward, but I'm not dumb. Why else would you take the book? I see how Redd is doing, I know what's going on."
    nov "Wait, no way, Mia! It's too dangerous!"
    mc "Yeah! It's not a day trip!"
    show mia ashamed with Dissolve(0.2)
    mia "I..."
    show nova neutral with Dissolve(0.2)
    nov "I appreciate the thought."
    mc "We both do."
    nov "But..."
    mc "But we can't let you do this."
    "Mia takes a deep breath and looks at you with determination in her eyes."
    show mia assertive with Dissolve(0.2)
    mia "And who'll help you two find the Azureola?"
    mia "I've seen it before. And I've been studying herbs and recipes for years. There is no one better then me in finding them!"
    show nova surprised with Dissolve(0.2)
    nov "But sweetie, you could get hurt."
    show mia neutral with Dissolve(0.2)
    mia "So could you. Both of you. What if you get hurt?"
    mc "I can perform some first aid, dad taught us some stuff."
    show mia assertive with Dissolve(0.2)
    mia "Well, I know a lot more than that. So, no. If you guys go, I go too."
    nov "Stop it, this is our responsibility."
    mia "And you're my friends. And Mister Redd is one of the nicest men I've ever met."
    mia "I want you two to come back, and I want you to succeed. So as the village's nurse, there is no way I'm letting you go alone in such a dangerous trip!"
    nov "But..."
    mia "I've made up my mind."
    mc "..."
    stop music fadeout 1
    mc "I don't think we're winning this one."
    show nova neutral with Dissolve(0.2)
    "[Nova] chuckles."
    nov "She beat us both."
    play music nova2
    show mia blushing 2 with Dissolve(0.2)
    mia "Sorry."
    nov "Hey. Don't apologize. You looked so damn cool acting so confident!"
    show mia smiling with Dissolve(0.2)
    "Mia laughs a bit."
    mia "So... I'm not sorry then."
    mc "There you go."
    show nova smirk 2 with Dissolve(0.2)
    nov "And hey, assertive Mia is really sexy. You should do it more often."
    show mia blushing 2 with Dissolve(0.2)
    mia "Stop it."
    show nova neutral with Dissolve(0.2)
    nov "Not going to stop saying true stuff."
    show mia neutral with Dissolve(0.2)
    mia "Fine. Um... if you're getting ready I'll get my things then."
    mc "Oh, right. Do you need to go back home?"
    "Mia shakes her head."
    mia "Why do you think the bag was so big?"
    show nova smirk with Dissolve(0.2)
    nov "You were reading your porn books again?"
    show mia blushing 1 with Dissolve(0.2)
    mia "I'm never drinking around you again."
    nov "It's not my fault you get chatty."
    show mia assertive with Dissolve(0.2)
    mia "And they aren't porn. They're literature."
    nov "Not from where I'm sitting."
    show mia blushing 1 with Dissolve(0.2)
    mia "Just... I mean... [MC] is right here!"
    mc "Don't mind me."
    show nova smirk 2 with Dissolve(0.2)
    nov "You should see HIS collection. High literature indeed."
    mc "OK. We're done here."
    "Mia giggles."
    show mia neutral with Dissolve(0.2)
    mia "Oh, have you read Arising to Depravity, [MC]?"
    mc "Um..."
    "You stammer for a second."
    nov "Awww, you have, haven't you?"
    mc "Actually, yes, but I never got the latest volume!"
    mia "Oh, I'll loan it to you! In this one Judith and Kristen are on the run and have to hide from an evil dragon!"
    mc "No spoilers!"
    show nova smirk with Dissolve(0.2)
    nov "So let me guess, the girls are hiding and start doing all sorts of nasty things to each other."
    show mia blushing 1 with Dissolve(0.2)
    mia "No! Well, yes, but there is really a lot of story behind it!"
    mc "Just because there's sex doesn't make it smut. These books are really captivating."
    show nova smirk with Dissolve(0.2)
    nov "I bet. Oh, you two are adorable."
    nov "So why not act out a scene from-"
    show mia blushing 2 with Dissolve(0.2)
    mia "ANYWAY! Um... don't you need to pack, [MC]?"
    mc "I do. Be back soon."
    scene farm bedroom night with Dissolve(2)
    play sound bedroomdoor
    "You go to your room and pull out your backpack."
    play sound clothes
    scene black with Dissolve(2)
    "After a while..."
    scene farm bedroom night with Dissolve(2)
    "You hear giggling coming from the living room."
    mc "{color=#b7b7b7}{i}Guess they're still getting ready.{/i}{/color}"
    "You hear a loud banging on the door."
    play sound knock2
    mc "{color=#b7b7b7}{i}What the hell?{/i}{/color}"
    play sound frontdoor
    scene farm house interior night with Dissolve(2)
    "[Nova] seems to be arguing with someone in the other room."
    "You head to the front door to see what's happening. Trevor is standing there, along with Nina. Her face is nearly as red as her hair as she and [Nova] are caught up in an argument."
    play music slowly fadein 1
    show nova angry with Dissolve(1)
    nov "No! You don't come in here and tell me what to do!"
    show mia neutral at offscreenright
    show mia neutral behind nova at farright with Dissolve(1)
    show nova angry at slightright with easeinleft
    show trevor annoyed at offscreenleft
    show trevor annoyed at farleft with Dissolve(1)
    show nina angry at offscreenleft
    show nina angry at slightleft with Dissolve(1)
    nin "You're both insane!"
    nin "This was your idea, wasn't it? Why are you always trying to get him into trouble?"
    nov "Why do you care? He's not your boyfriend and he's not your brother!"
    show nina moreangry with Dissolve(1)
    nin "He's not yours either!"
    "You rush over to the two of them before they come to blows."

menu:
    "Stop Nina [gr]\[NinaLove -1\]\[NovaLove +1\]":
        mc "Nina, chill out! Back off!"
        nin "So you finally show up."
        nov "She came in here acting all crazy."
        nin "I did not."
        $ NinaLove -= 1
        $ NovaLove += 1
    "Stop Nova [gr]\[NovaLove -1\]\[NinaLove +1\]":
        mc "[Nova]! Relax!"
        nov "She comes in here acting like a crazy person and you tell ME to relax?"
        nov "Typical."
        $ NovaLove -= 1
        $ NinaLove += 1
    "Stop both":
        mc "Quiet you two! You're gonna wake up dad! And probably everyone else in town."
        nov "What? She comes in here and starts screaming and you-"
        nin "I said one little thing and you blew up."
        nov "Like hell I did!"
        mc "Enough!"

label Day7NinaArgument:
    mc "What the hell's going on?"
    show nina neutral with Dissolve(0.2)
    nin "Well, let me think. I went over to Laura's to buy some flowers for your dad and she mentions that you were going camping in the mountains to the west."
    nin "\"That's crazy.\" I told her. There's no way that [MC] would go out to a mountain filled with goblins, magic traps, man-eating plants, and whatever else decides to show up!"
    nin "But Laura was adamant. So... I came over to check on you. Again, no way my best friend is stupid enough to go out and get himself killed fighting an army of goblins."
    show nova annoyed with Dissolve(0.2)
    nov "We're not going out there to fight anything!"
    nov "We're going to get a flower."
    mc "Nina, we have to do this."
    show nina worried with Dissolve(0.2)
    nin "No, you don't... OK?"
    nin "You're going to get killed out there. Both of you."
    show trevor neutral with Dissolve(0.2)
    "Trevor puts his hand on Nina's shoulder."
    tre "Nina..."
    show nina angry with Dissolve(0.2):
        xzoom -1.0
    nin "You're taking his side?"
    show trevor annoyed with Dissolve(0.2)
    tre "What side? I'm here backing you up!"
    mc "Nina... Without this, dad could die."
    show nina neutral with Dissolve(0.2):
        xzoom 1.0
    nin "You think I don't know that? But this isn't like that time you dragged me along to see the lightning lizards. You're not getting away with electrical burns on your butt. These things will KILL you."
    nin "What am I going to say to Redd if he pulls through and neither of you come back?"
    mc "We're not going to die out there."
    show nina worried with Dissolve(0.2)
    nin "You don't know that."
    mc "Yeah, I guess I don't. But I can feel it."
    nin "You what?"
    nov "Yeah, not your best argument."
    mc "It'll work out. It did last time."
    show nina moreangry with Dissolve(0.2)
    nin "You almost DIED! The only reason that goblin didn't kill us was by dumb luck."
    nov "Goblin?"
    if CoolStoryBro == 1:
        "Trevor turns to you."
        tre "Wait... you were serious? Lisa thought you were joking!"
    mc "It was nothing."
    show nina angry with Dissolve(0.2)
    nin "No, it wasn't. I nearly lost you last time... I'm not letting you do this!"
    "Trevor fidgets a bit at Nina's last comment."
    nin "That was ONE goblin in the cave. There are hundreds up in the mountain."
    mc "And they never really leave their caves without a good reason."
    mc "We're not making a social visit, Nina. We're-"
    nin "Thrill seeking? Is that it?."
    "Nina looks over to Mia."
    show nina neutral with Dissolve(0.2)
    nin "Mia, talk some sense into them."
    show nova neutral behind mia with Dissolve(0.2)
    mia "I..."
    mia "I'm going with them."
    show nina worried with Dissolve(0.2)
    nin "Has everyone gone insane?"
    mc "Sorry, Nina."
    show nina moreangry with Dissolve(0.2)
    nin "Fine! If you want to die just go ahead! See if I care! You..."
    "Nina stares at you for a minute, then shakes her head and runs out the door."
    hide nina with easeoutleft
    play sound frontdoor
    tre "Nina!"
    "Trevor starts to go after her."
    show trevor neutral at slightleft with easeinleft
    show mc neutral at center with Dissolve(1)

menu:
    "Stop him and go after her yourself [gr]\[NinaLove\]":
        hide mc with Dissolve(0.3)
        mc "Trevor, she's pissed at me..."
        nov "And me."
        mc "Yeah. But mainly me."
        tre "[MC], she's my girl."
        if TrevorFriend > 0:
            tre "But this is between you two."
            tre "Just go."
        else:
            show trevor annoyed with Dissolve(0.2)
            tre "There's still something you're not telling me. Talk to her, but if you did anything back then..."
            mc "I..."
            nov "Of course he didn't, you ass."
            tre "Whatever. Go."
        jump MCNinaOutsideDay7
    "Let him go after her. [gr]\[MiaLove\]\[NovaLove\]\[TrevorFriend\]":

        $ NinaLeavingTalk = 0
        "You let him go."
        hide mc with Dissolve(0.3)
        hide trevor with easeoutleft
        show nova neutral at slightleft with easeinright
        show mia neutral at slightright with easeinright
        play music nova2 fadein 1
        nov "What the hell really happened in that cave?"
        mc "We weren't the only ones there."
        mc "There was a goblin, he attacked Nina. Long story short, we survived. Barely."
        show mia blushing 1 with Dissolve(0.2)
        mia "You fought a goblin?"
        mc "I guess I did."
        show nova angry with Dissolve(0.2)
        nov "So why didn't you say anything? Not even to me?"
        if CoolStoryBro == 1:
            mc "I kind of told Lisa, but she thought I was kidding. After that I realized Nina didn't want to talk about it much."
        else:
            mc "I don't think either of us wanted to talk about it much."
        show mia neutral with Dissolve(0.2)
        mia "That's amazing! You're... wow!"
        "Mia beams at you."
        mia "You weren't even trained."
        show nova smirk with Dissolve(0.2)
        nov "See, I told you you were cooler than you look."
        mc "You've never said those words to me, ever."
        show nova neutral with Dissolve(0.2)
        nov "I did. Just now."
        mc "You know what I mean."
        mia "Um... do you think Nina's still angry?"
        nov "If I was her, well, I'd be a little bitchier, but yeah, probably."
        nov "She'll get over it. Maybe in the strong arms of Broadsword McChestMuscles."
        show mia neutral with Dissolve(0.2)
        mia "I'm sure Trevor will escort her home..."
        nov "I'm thinking a walk to the grove. A good night of banging and she'll feel better."
        mia "Is it really that psychologically relaxing?"
        show nova smirk 2 with Dissolve(0.2)
        nov "If he's big enough I'm sure it will be! His tanned body ravaging her tiny frame... It'd be a scene out of one of your books!"
        mc "OK! Can we stop with the mental images? We've still got packing to do."
        nov "Yeah."
        "The three of you finish packing and go to sleep early."
        scene black with Dissolve(2)
        stop music fadeout 1
        $ TrevorFriend += 1
        $ NovaLove += 1
        $ MiaLove += 1
        jump Day8Start

label MCNinaOutsideDay7:
    play music nina2 fadein 1
    $ NinaLeavingTalk = 1
    scene ninafarmfight 1 with Dissolve(2)
    hide window
    w ""
    "You head out and see Nina sitting up against a tree."
    nin "I'm not talking to you."
    mc "Hey, I just wanted some fresh air is all. But it looks comfy where you're sitting. You mind?"
    nin "..."
    scene ninafarmfight 2 with Dissolve(2)
    hide window
    w ""
    "You sit down next to Nina. It's deadly quiet for quite some time until she raises her head and begins."
    nin "What's your deal?"
    mc "My deal? I'm not the one who ran into her friends' house screaming."
    nin "I did not come in screaming, thank you very much. I asked [Nova] a question, and she was a bitch about her response."
    mc "She shouldn't have been. But she's stressed out over dad."
    nin "I know. I would be too. Can we just not talk about her?"
    mc "Fine, so what about then?"
    nin "You still haven't answered my question. What's your deal?"
    mc "No deal. I just have to save dad, or at least try."
    nin "Did you think of asking the militia for help? You know I could swing a favor or two."
    mc "I gathered. But I won't ask someone uninvolved to go with me. And let's be honest, they're a bunch of kids just like us."
    nin "At least they know how to fight."
    mc "Even so."
    nin "But you're fine with [Nova] and Mia going along?"
    mc "They both more or less forced me."
    nin "With [Nova], I buy it. But Mia?"
    mc "When she gets assertive it's a little scary to be honest."
    nin "I'm kind of sad I missed that."
    mc "You should be. It was amazing."
    scene ninafarmfight 3 with Dissolve(2)
    hide window
    w ""
    nin "Just promise me you won't die."
    mc "I promise."
    nin "Don't make a girl a promise... if you..."
    "Nina sighs."
    nin "Thanks. I'll hold you to it."
    nin "I better go. Trevor's over at your door trying NOT to spy. He's not doing very well."
    mc "Should we give him a show?"
    scene ninafarmfight 4 with Dissolve(2)
    hide window
    w ""
    nin "NO! Stop that."
    "She smacks you on the shoulder."
    nin "Get back soon, OK?"
    mc "I'm not making a vacation out of it."
    nin "Good."
    scene farm fixed night with Dissolve(2)
    "Nina gets up and brushes herself off. She approaches Trevor and smiles."
    show trevor neutral at slightleft with Dissolve(1)
    show nina neutral at slightright with Dissolve(1)
    tre "Hey. Everything OK?"
    nin "Not really. But good enough."
    nin "Walk me home?"
    tre "Sure."
    hide nina with easeoutleft
    hide trevor with easeoutleft
    "You wave goodbye to them as they leave. You open the front door to see [Nova] waiting for you."
    scene farm house interior night with Dissolve(2)
    show nova neutral with Dissolve(1)
    nov "Come on! You still have a lot of packing to do. And we need to sleep."
    mc "Yeah. Let's do it."
    $ NinaLove += 1
    jump Day8Start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
