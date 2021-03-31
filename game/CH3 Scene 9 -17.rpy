label Day6WakeUp:
    $ persistent.nova_sleep = True
    scene black with Dissolve(2)
    play sound knock1
    mc "M... what?"
    play sound knock1
    nov "Get up [MC]..."
    nov "Someone's at the door."
    mc "You get it. I always get it..."
    nov "I'm comfy over here."
    mc "Well, that changes everything."
    mc "And by everything I mean nothing. Get the door."
    scene day5 morning 1 with Dissolve(2)
    nov "It's probably Nina, you should get it lover boy."
    mc "Doubt it."
    nov "No one else comes here this early."
    mc "Mia and Silas probably."
    mc "Just get it... I'll be out in a minute."
    nov "You suck."
    mc "No I don't. You're just bitchy in the mornings."
    scene farm bedroom with Dissolve(2)
    show nova neutral with Dissolve(1)
    "[Nova] gets out of bed and throws on her clothes. She walks out the door."
    hide nova with easeoutright
    play sound bedroomdoor
    "You relax in bed for a few minutes and hear muffled conversation through your door."
    mc "{color=#b7b7b7}{i}Sounds like Mia and the Elder.{/i}{/color}"
    "You get dressed and walk into the living room."
    scene farm house interior with Dissolve(2)
    "It's empty, but you hear muffled voices coming from your father's room."
    mc "{color=#b7b7b7}{i}Looks like they're already with Dad.{/i}{/color}"
    "You knock on the door and walk in."
    play sound knock1
    pause(1)
    play sound bedroomdoor
    play music reddsick fadein 1
    mc "Everything OK in here?"
    show redd sick 7 with Dissolve(2)
    dad "There he is! The way [Nova] talked I thought I wouldn't see you until lunch time."
    "Your father's skin looks paler than it did the night before."
    mc "How are you feeling?"
    dad "Not great. If I was I'd be asking you why you're up so late and pulling you out of bed by your ear."
    nov "I can do that if you want!"
    dad "It just wouldn't be the same, honey."
    mc "You're still sarcastic, so that's a good sign."
    "Redd chuckles, but that soon transforms into a cough."
    dad "Looks like I'm still not one hundred percent."
    scene farm redd room with Dissolve(2)
    show elder neutral at right with Dissolve(1)
    show mia ashamed at left with Dissolve(1)
    eld "That cough still sounds serious, let's take a look at you, again."
    eld "I hate to ask, but it will be easier to examine Redd without you two here."
    dad "Just go... get to work already."
    "Redd coughs again."
    "[Nova] looks up at you and you follow her out of the room to give Silas and Mia more space."
    scene farm house interior with Dissolve(2)
    show nova worried with Dissolve(1)
    nov "He's not looking better."
    mc "It happens sometimes I guess. You know you get sick the first day then you really feel it on day two."
    nov "Yeah..."
    hide nova with dissolve
    "You and [Nova] sit down and wait for word from Silas or Mia. After a few minutes the door opens."
    show mia ashamed with Dissolve(1)
    mia "Um..."
    mc "How is he doing?"
    mia "His fever came back last night, but we were able to break it. He's supposed to rest now and he should stay in bed."
    mc "{color=#b7b7b7}{i}Something seems wrong here... she's usually so chipper.{/i}{/color}"
    mc "Mia?"
    mia "The Elder wants to talk to all of you together."
    scene farm redd room with Dissolve(2)
    play sound bedroomdoor
    nvl clear
    n "[Nova]'s expression turns to one of pure worry and she rushes in. You run in after her."
    n "The elder begins to speak and they are words that you know you should understand, but you can't."
    n "[Nova] looks extremely upset. It should bother you more, but it seems like you are looking at her from outside your body."
    n "Your father looks weak. He looks extremely weak. This isn't right. He was doing well last night."
    n "Silas turns to you and asks a question. Then he asks again."
    nvl clear
    show elder neutral with Dissolve(1)
    show mia neutral at left with Dissolve(1)
    eld "Do you understand?"
    mc "He's got the flu... that's what you said."
    eld "No, [MC], your father doesn't have a flu. I think he's suffering from poisoning."
    mc "Poisoning?"
    show father neutral at right with Dissolve(1)
    dad "If you wanted to do me in son you could have just stabbed me."
    mc "Dad! Not now."
    show nova worried at slightright with Dissolve(1)
    "Redd coughs uncontrollably. [Nova] rushes to his side and puts her arm on his back."
    nov "Don't talk so much, Redd..."
    dad "Thank you. This doesn't make sense... I might joke, but I don't see anyone poisoning me. And the kids haven't cooked in days."
    eld "It had crossed my mind last night - you're a very resistant man, Redd, so it's unusual for you to get sick from work like this, even in such an extreme situation. But I missed one of the symptoms."
    dad "Which one?"
    eld "Mia, can you hear the crackling in his breath?"
    show mia neutral zorder 2
    show mia neutral at slightright with easeinleft
    show nova worried at slightleft with easeinright
    mia "Yes - there is a slight crackling in his breath. How I did I miss it?"
    eld "I wasn't sure last night either, but I went through my books. I'd hoped to see him in better condition when I arrived."
    dad "What poisoned me?"
    eld "These symptoms caused by a very dangerous plant-monster called Venomair. It’s been awhile since we have seen them near the village. My guess is that their spores were brought here from the forest by the strong winds."
    dad "Or maybe it was that damn fairy."
    nov "Elder, what is the treatemnt?"
    eld "There are a few ways to treat the poison, but nothing that we have access to right now. I'll look into it more, but for now we can only treat the symptoms."
    nov "Will he recover on his own?"
    eld "It's possible, and has happened in the past, but I can't guarentee anything."
    scene redd sick joking with Dissolve(2)
    dad "Don't worry son, you won't get rid of me that easily."
    mia "That's the spirit, Mr. Redd!"
    nov "Yeah, you'll be fine."
    eld "That attitude is good Redd, but you need to take your medicine. I'll have more for you tonight, we need to keep that fever low."
    eld "You also need to eat. Meats would be best."
    scene redd sick neutral with Dissolve(2)
    dad "Well, all our livestock is gone."
    eld "I understand, there isn't much available in the town right now either."
    mc "I'll go fishing and bring enough for some stew to last a few days."
    eld "Ah, yes. A fish stew would be quite nutritious."
    "Redd begins coughing violently again."
    scene redd sick 7 with Dissolve(2)
    "[Nova] pats him on the back."
    dad "I'll be alright now. You two just go get your work done - we still need to replant."
    nov "I can't leave you alone like this."
    "Mia puts a reassuring hand on [Nova]'s shoulder."
    mia "I can stay here with him while you are both out."
    dad "See? Thank you, dear."
    "Redd coughs again."
    mc "Dad, just... stop talking, OK?"
    "Redd regains his composure and looks down at his hand. You see a fleck of red on his palm."
    dad "Yeah, I need to rest. So get out of here."
    eld "I will check in tomorrow morning. Mia, if there is any change send a runner."
    mia "I will."
    eld "[MC], I'll have more doses of his medicine brewed by this evening."
    mc "OK. I'll come by to pick them up."
    eld "Perfect. I'll be on my way. Redd, I know how you are but don't forget to rest, you undertand me?"
    dad "I heard you the first few times, Silas."
    mc "OK, I'll head out too."
    dad "Go, go. Don't worry, Mia will keep me company if I need it."
    "Mia blushes."
    "You wave goodbye to your father and leave with [Nova]."
    scene farm house interior with Dissolve(2)
    play music afternoon fadein 1
    show nova neutral with Dissolve(1)
    nov "Let's get going then. [MC], we need to go see Darius. I promised him we'd come by, so we're coming by."
    "You blanch."
    mc "I'm sure there's other work."
    show nova annoyed with Dissolve(0.2)
    nov "What's your problem now?"
menu:
    "I just don't like Trevor":
        mc "Trevor rubs me the wrong way is all."
        nov "He's probably not even going to be there."
        show nova smiling with Dissolve(0.2)
        nov "Plus... hot sister, right?"
        mc "I mean, yes, but still."
        show nova neutral with Dissolve(0.2)
        nov "Come on, it's been like a half a decade since Nina kicked his butt for bullying you! You need to get over these things."
        mc "You're right."
        jump Day6Trevor
    "I don't like how Darius creeps on you [gr]\[NovaLove\]":

        if NovaDarius == 1:
            nov "You're the one who said I should take advantage of that."
            mc "Well, here, not over there. I can watch out for you here."
            nov "I doubt he'll do anything, and you'll be there anyway, right?"
            mc "I just don't want to have to stab him."
        show nova smiling with Dissolve(0.2)
        nov "Aw, it's sweet that you say that!"
        nov "But I can take care of myself."
        $ NovaLove += 1
        jump Day6Trevor

label Day6Trevor:
    scene black with Dissolve(2)
    play sound walkgrass
    scene trevors house exterior with Dissolve(2)
    mc "So again I say we don't have to do this."
    show nova neutral with Dissolve(1)
    nov "Too late. We're here."
    hide nova with Dissolve(1)
    show trevor annoyed at left with Dissolve(1)
    show brooke neutral at right with Dissolve(1)
    tre "You're going out drinking?"
    bro "Either that or stay here with dad, little brother. And you know which one I pick."
    bro "And look at it this way: the more I take from Darius' reserve, the less he can drink at home. It's a win win for all of us. Especially you."
    tre "Fine, just go."
    bro "Didn't need your permission."
    hide trevor with Dissolve(1)
    show brooke neutral at center with easeinright
    "Brooke walks off and almost bumps into you."
    bro "Hey."
    mc "Hi, Brooke. Where are you off to?"
    bro "I'll be drinking by the lake, maybe have some real fun later. Who knows?"
    if PeepedLake == 1:
        bro "If you're looking for another show though you might want to hurry."
    bro "Gotta run, see ya."
    mc "Uh, OK, bye. "
    "Brooke leaves barely giving you another look."
    hide brooke with easeoutleft
    show nova neutral with Dissolve(1)
    nov "Got to love how sociable she is."
    show nova neutral at slightleft with easeinright
    show trevor neutral at slightright with Dissolve(1)
    tre "If you get a few drinks into her, maybe. But she seems to like you more than most."
    "Trevor waves at you."
    tre "I wasn't expecting you two. Something up?"
    mc "Yeah, apparently your dad has work that needs getting done or something."
    tre "He didn't say shit about that, but that's nothing new."
    tre "He's around back."
    "You nod at Trevor."
    nov "You hanging around?"
    tre "Not really, I have to meet with the guys. But before you guys head out back, can you give us a couple of minutes, [Nova]?"
    "[Nova] turns to you and raise her eyebrow. You nod."
    nov "Sure."
    hide nova with easeoutleft
    "[Nova] goes to the back of the house."
    show trevor neutral at center with easeinright
    mc "So?"
    tre "Look, there's not good way to say this, but Nina's acting kind of weird since she got back."
    tre "What the hell happened with you there?"
    mc "Can't you just ask her?"
    show trevor annoyed with Dissolve(0.2)
    tre "Come on, man! I need your help here, she isn't really talking about it with me."
    mc "It was a rough couple of nights. She'll talk when she's ready. But if she doesn't want to say anything, would you want me to break her trust?"
    if TrevorFriend >= 1:
        show trevor neutral with Dissolve(0.2)
        tre "She's your friend, I get it. I'll try talking to her again."
    tre "Thanks again for keeping her safe. See you later, Slime Boy!"
    hide trevor with easeoutleft

    scene trevors backyard with Dissolve(2)
    "Darius is sitting in front of a carpenter's table with a saw in his hand. A half empy bottle of what looks like liqor is on the table."
    show darius neutral at right with Dissolve(1)
    show nova neutral at left with Dissolve(1)
    dar "Ah, [Nova]! I'm glad you made it. I didn't expect to see you."
    nov "You said you had some work."
    dar "And I do! I'm making fences today - it's damned tedious work."
    nov "Beggars can't be choosers."
    dar "Perfect. Come over here and I'll show you how to cut the planks."
    show nova neutral at slightleft with easeinleft
    "[Nova] joins Darius at his carpenter's table."
    dar "Now sit right here."
    "He places a plank in front of her."
    dar "I marked out the pattern."
    dar "Now take the saw and cut away."
    "[Nova] grabs the saw in one hand, hold the plank steady and she saws into the wood."
    dar "Stop!"
    nov "What?"
    dar "You'll split the wood with that technique."
    dar "Let me show you."

    scene nova darius saw with Dissolve(2)
    hide window
    w ""
    nov "I think I've got it."
    dar "Nonsense. relax, it's all about the positioning."
    "Darius squeezes [Nova]'s side."
    nov "Hey!"
    dar "Now move your arm like this."
    "Darius leans into [Nova] as he explains how to correctly saw the wood."
    "He grins and presses his crotch into her from behind."
    if NovaDarius == 1:
        "[Nova] sighs and lets him continue."
        nov "You're crossing a line here Darius. Just show me what I need to do."
        dar "You might have to do a lot. Here, use this angle."
        nov "Great! That was super helpful!"
        dar "I try to be."
        nov "Now move your hands."
        dar "What?"
        scene trevors backyard with Dissolve(2)
        show darius neutral at slightright with Dissolve(1)
        show nova angry at left with Dissolve(1)
        nov "I'm not dumb! I know how you want it sawed, so I don't need you hanging on me."
        dar "You're being a little presumptive here. This is all perfectly normal."
        nov "No, it's not, but I need the money or else I'd have slapped you and left."
        nov "But that doesn't mean you can do whatever you want."
        dar "A girl like you can make a lot of money from me without all this hard work, you know? "
        nov "Ew! Just... go away let me get started. I'll show [MC] how to do it when he's done with Trevor."
        show darius neutral at farright with easeinleft
        dar "Oh, you invited [MC] too?"
        nov "I assumed you'd need us both."
        dar "I never said I had that much work."
        show nova annoyed at left with Dissolve(0.2)
        nov "I said we both needed work and you offered."
        "You walk around back after your conversation with Trevor."
        mc "Hey [Nova], how's it going?"
        nov "Took you long enough."
        mc "{color=#b7b7b7}{i}[Nova] looks a little flustered.{/i}{/color}"
        mc "Everything OK?"
        show nova neutral with Dissolve(0.2)
        nov "It's fine, we're going to help Daruis build fences."
        mc "Well, the elder said that his medicine wouldn't be ready until later. So I do have time to kill."
        mc "Will this be an all day thing?"
        dar "For her, yes."
        dar "I'm sorry, [MC]. I didn't realize that she thought I needed help from the two of you."
        dar "I only have enough tools for two, and space is an issue."
        dar "But don't worry, [Nova]. You'll be well compensated."
        nov "I'll stay so long as the working conditions are acceptable. No more funny moves! Is that alright with you, Darius?"
        dar "Perfectly."
        mc "You sure about this, [Nova]?"
        nov "Go on, I'll see you tonight. I can handle him."
        jump Day6EliseFacial
    else:

        scene trevors backyard with Dissolve(2)
        show nova angry at left with Dissolve(1)
        show darius neutral at center with Dissolve(1)
        nov "You know what? I don't need money THAT bad."
        dar "This is simply-"
        nov "A drunk man's try to get in my pants. Well, that's never happening, so find someone else."
        dar "I pay well."
        nov "I'm not that desperate. And I don't want to deal with a drunkard."
        dar "Hey, you don't have to be so rude."
        mc "Is there a problem?"
        "Having just entered the backyard to see [Nova] and Darius arguing. They both stop and turn to you."
        nov "No. We're finished here though."
        dar "It seems there's a misunderstanding here."
        nov "I don't think there is, old man!"
        "[Nova] grabs you by the wrist and walks away from Darius' house."
        scene village destroyed with Dissolve(2)
        mc "What was that about?"
        show nova annoyed with Dissolve(1)
        nov "I just can't work for that creep!"
        mc "What did he do?"
        nov "Nothing... yet. But every part of me was telling me to get out of there. And I am starting to think those rumors about Heather were true."
        mc "Yeesh. Yeah, good call. Only question now is what are you going to do for money instead."
        show nova neutral with Dissolve(0.2)
        nov "Something that doesn't involve getting groped. Don't worry, I'll find something. We'll meet up back home for dinner."
        mc "Ok. See you then."
        "[Nova] and you part ways."
        hide nova with easeoutleft
        jump Day6EliseFacial

label Day6EliseFacial:
    play sound walkgrass
    scene village day 2 with Dissolve(2)
    mc "{color=#b7b7b7}{i}OK, Elise was supposed to need help with something today.{/i}{/color}"
    mc "{color=#b7b7b7}{i}I wonder if Sophie's going to be there? I still can't believe I saw her tits at the party!{/i}{/color}"
    mc "{color=#b7b7b7}{i}By the gods. Am I just horny all the time now?{/i}{/color}"
    mc "{color=#b7b7b7}{i}What am I saying? I was horny all the time before.{/i}{/color}"
    scene elises garden with Dissolve(2)
    "You arrive at Elise's house and knock on the door."
    play music elise fadein 1
    show elise neutral with Dissolve(1)
    eli "[MC]! What brings you here?"
    mc "Good morning, Elise! [Nova] and I are still offering our services around town."
    eli "Oh, are you now? I heard your father was sick. Is he doing better?"
    mc "Not really, but I'm sure he will be..."
    eli "You're worried, aren't you?"
    mc "Nah, Dad's tough. Nothing can take him down."
    eli "You don't need to act tough on my account. But yes, I'm sure he'll be better soon and back on working as hard as ever!"
    mc "Thank you. So, I heard that you need help with something?"
    eli "Yes! Please, come in."
    "Elise opens the door and motions to you."
    scene elises house messy with Dissolve(2)
    "The inside of Elise's house is quite the mess. It's filled with pots and and yard decorations that were taken in during the storm."
    show elise neutral with Dissolve(1)
    eli "So, I need to be able to cook again but there is stuff everywhere. Can you help with that?"
    mc "Sounds good."
    eli "I'd ask Sophie but, surprise, she's out. Sorry for the mess."
    mc "Sorry? This is nothing, you should see what I had to clean yesterday."
    show elise laughing with Dissolve(0.2)
    eli "You can tell me the story as you work."
    scene black with Dissolve(2)
    nvl clear
    n "You tell Elise about cleaning the pub as you fix up the interior of her house. The cleaning would be normal except for two things, first you are amazed that anyone could own so much useless crap."
    n "Secondly, you are amazed at how {i}heavy{/i} said useless crap truly is. Despite it all, with her assistance, you make quick headway on the piles of junk, and within an hour the inside of her house looks spotless."
    nvl clear
    scene elises house with Dissolve(2)
    show elise neutral with Dissolve(1)
    eli "So this really IS nothing."
    mc "Compared to that?"
    mc "{color=#b7b7b7}{i}It was damn close.{/i}{/color}"
    mc "That was cake."
    show elise laughing with Dissolve(0.2)
    eli "My young hero!"
    show elise neutral with Dissolve(0.2)
    eli "The kitchen is usable again! So stay and let me treat you to some food."
    mc "Oh! Thanks, I've barely eaten since the storm."
    eli "You poor dear, just leave everything to me and we can chat while I cook. But first, would you like some tea?"
    mc "Oh sure."
    "Elise pours you a cup of tea. You gratefully accept and take a sip."
    mc "Wow! This is great."
    eli "Thank you! You're such a nice boy. It's good to see someone so young with manners, not like that boy Sophie's dating."
    eli "I keep telling her she's barking up the wrong tree with him, but if it makes her happy."
    eli "Daughters don't listen to their mothers about boys. It's just how it works."
    "Elise took Sophie in around the same time [Nova] came to live with you. Amanda, Sophie's best friend, had been Elise's daughter. Amanda died in the same bandit attack that took the life of Sophie's parents."
    "But they were for all intents and purposes as much family now as if they were related by blood. And Neither Elise nor Sophie would say otherwise."
    eli "I wonder if Redd worries this much about [Nova]?"
    mc "If he does, he hides it well. He's always on me to get a girlfriend though."
    eli "You should be dating a nice girl. I'm probably being old fashioned. Now you all don't even really court eachother anymore. "
    mc "Some of us do I guess, but the way dad talks sometimes, I wonder if your generation was all that different."
    eli "Oh, Redd and his big mouth! I never {w} expected you to figure that out. Maybe we just want our kids to not be as crazy as we were."
    eli "Or maybe we're just jealous that we can't go wild. Enjoy your youth, [MC]."
    mc "I plan to."
    eli "Good."
    "She turns to the kitchen and starts fixing lunch. You take another sip of tea."
    eli "So, speaking of which, how's your sex life?"
    "You spit the tea in your mouth out all over the table below."
    mc "Ex-"
    "You cough."
    mc "Excuse me?"
    show elise laughing with Dissolve(0.2)
    eli "I'm sorry, that's was a little forward, wasn't it? I'm just that way. Too much for you?"
    mc "No, just surprising."
    show elise neutral with Dissolve(0.2)
    eli "How about this: are you with anyone? In love? In lust?"
    mc "Hm..."
    eli "All of the above?"
    mc "I mean, I wouldn't say in love, but..."
    eli "Here's some advice: just talk to whoever it is and let it all out. When you do that, it shows you're willing to take a risk."
    eli "You're a handsome boy, so you'll be ok. Just don't be too creepy, girls can sniff that out! A few months back Sophie was ranting about this creepy guy who asked her out."
    mc "{color=#b7b7b7}{i}So I was creepy!{/i}{/color}"
    eli "He took nearly five whole minutes to ask her out. It was apparently really embarrassing."
    mc "Yeah, what a loser..."
    eli "Oh. And that was you."
    mc "Guilty."
    eli "I'm sorry. I didn't realize."
    eli "And I don't know what she was on about, you're not a creep at all. Don't think too much about it."
    eli "I shouldn't say this about my daughter but it's her loss. I gueess young ladies don't know what to look for in men yet."
    mc "Thanks. I guess I was just nervous."
    eli "Yeah, I think they forget how scary it can be for the boys asking as well."
    "Elise turns to you."
    eli "How about this? You can practice talking with me! That way you won't be nervous when you ask girls out."
    mc "Thanks for the offer, but I don't know..."
    eli "Oh, come on. don't be shy! It's cute, but it feeds into your nervousness. Like I said, you have a lot going for you."
    eli "I wish there were more men like you around. Responsible and without any ulterior motives. A girl knows that everyone's always looking for a little \"something else\"."
    mc "{color=#b7b7b7}{i}Of course they are. Look at her!{/i}{/color}"

menu:
    "I wouldn't mind something else, either!":
        mc "Well, I have a confession. I wouldn't mind a little something else with you either!"
        eli "I didn't mean me!"
        mc "What? I know what you're thinking, but don't worry, you aren't too young for me."
        eli "Oh, I see! You were practicing."
        eli "It's not a bad attempt, but try to be a little less forward. Try to compliment in a roundabout way and it'll sound better."
        jump Day6EliseFacial2
    "I understand why they'd want that. [gr]\[EliseLove\]":

        mc "I mean, you are so beautiful, it’s not a surprise men are all over you!"
        eli "Oh, thank you honey! It’s complicated though; I have to be always careful to not send them any mixed signals, you know?"
        eli "You are a sweetheart. I stand what I said about Sophie. If I was just a few years younger..."
        $ EliseLove += 1
        jump Day6EliseFacial2

label Day6EliseFacial2:
    eli "Now, let me finish up lunch here!"
    hide elise with Dissolve(1)
    "Elise finishes making lunch and serves it to you."
    show elise neutral with Dissolve(1)
    eli "Dig in."
    "You take a bite."
    mc "Wow! This is amazing."
    eli "Thank you!"
    "You wolf down the rest of your lunch."
    eli "You were hungry, weren't you?"
    mc "More than I thought I was."
    "Elise picks up your empty plate."
    show elise laughing with Dissolve(0.2)
    eli "You remind me of my first husband. He'd come home after work and eat everything up in such a rush, like he couldn't wait another second to bend me over the table!"
    mc "{color=#b7b7b7}{i}Now that's a nice thought right there.{/i}{/color}"
    show elise neutral with Dissolve(0.2)
    eli "Oh dear, sorry for the imagery. You don't need a mental picture of that, do you?"
    mc "Don't be sorry."
    eli "Oh please, you look more uncomfortable than..."
    "Elise looks down."
    eli "Are you? Oh. I take it as a compliment."
    mc "That's embarrassing. I'm really sorry."
    "Elise keeps staring at you. She seems to be lost in thought, but she doesn't take her eyes off of your cock."
    mc "Elise?"
    eli "[MC], I have another favor to ask."
    mc "Anything."
    eli "Please don't think I'm crazy! Just yesterday I got a visit from a traveling merchant who was selling some protection artifacts and she was so pretty, her skin was simply divine! And then she told me she was over decade older than me. I didn't want to believe it."
    mc "{color=#b7b7b7}{i}A merchant? Selena? I'm not sure I would believe it either.{/i}{/color}"
    eli "Anyway, I asked her what was her secret and... oh my... and she said \"Semen. It's a powerful element that can be used in all sorts of spells too. If you want to look younger, find a young boy with a great sexual energy to cover your face with jizz every day.\""
    mc "{color=#b7b7b7}{i}If this is going where I think it's going I have to thank Selena next time I se her!{/i}{/color}"
    mc "{color=#b7b7b7}{i}Every guy around my age has had a crush on Elise at some point in their lives. I don't know how old she was when she became a mom, but it was pretty young.{/i}{/color}"
    eli "I'm usually at home all day and young guys like you, well, they chase after girls like Sophie. So I just accepted there was nothing I could do, but... you're the perfect candidate - it's almost like she was talking about you specifically!"
    eli "I know this is a weird request but, could you... do this for me?"
    mc "Really? Of course! I can't say no to something like that!"
    eli "It's not a sexual thing, OK? And promise me you won't tell anyone!"
    mc "I promise!"
    "Elise giggles at your obvious excitement and surprise."
    eli "OK, we have to do this quickly! Sophie will be back soon."
    "You just stand there, dumbfounded."
    eli "Come on. I told you, no need to be shy. Pull it out."
    mc "{color=#b7b7b7}{i}At this point I'm just going to stop questioning these things.{/i}{/color}"

    scene EF3 with Dissolve(2)
    hide window
    w ""
    "You pull out your cock and Elise gasps."
    eli "Wow!"
    mc "{color=#b7b7b7}{i}Dreams are coming true! I love the girls my age, but Elise, she's always been something special.{/i}{/color}"

    scene EF4 with Dissolve(2)
    hide window
    w ""
    "You run your hands over you cock and stare at Elise's cleavage."
    eli "Quickly now! Sophie could come in at any moment."
    mc "I'm trying, but I can't cum that fast! Maybe you could show me your tits? It would help a lot!"

    scene EF5 with Dissolve(2)
    hide window
    w ""
    "Elise smiles and lowers her shirt."
    mc "Your tits look amazing! Better than I ever imagined. I can't believe I'm finally seeing you like this!"
    eli "You imagined them a lot?"
    mc "Um..."
    "Elise laughs."

    scene EF6 with Dissolve(2)
    hide window
    w ""
    eli "[MC], you're jerking off to me, you can be honest."
    mc "I... Yes, I imagined them a lot."
    "Elise doesn't respond, but she looks up at you with lust in her eyes."
    eli "Cum for me..."

    scene EF7 with Dissolve(2)
    hide window
    w ""
    "You shoot your load all over Elise's face. You fire a load so large and strong that it nearly hurts."
    eli "Yes! You came so much! How is this even possible? This is perfect!"
    "As she speaks some of the cum enters her mouth."
    eli "Oh, I shouldn't waste it."

    scene EF8 with Dissolve(2)
    hide window
    w ""
    "Elise rubs the cum into her skin, smiling as she does so."
    eli "Now, just remember this is simply some assistance. It's not-"
    mc "Anything special. I know."
    eli "Well, it's a little special."

    scene elises house with Dissolve(2)
    show elise neutral with Dissolve(1)
    eli "You know, if you need money we could sell this around town as a skin cream."
    mc "I don't know, I think we need to keep testing it first."
    eli "The merchant said I need to do this every day ro really see some results, but..."
    mc "What's wrong?"
    eli "I can't! I feel like I'm using you! And you're Sophie's age! I don't know what came over me."
    mc "Don't worry, this is not that big of a deal. You helped me and I helped you, that's all. It's our secret! You even look younger already!"
    eli "Oh, you're such a flatterer."
    mc "It's not flattery if it's true."
    eli "Come by tomorrow, maybe I'll have some more errands for you to help with."
    mc "I'll do that."
    eli "I'll see you out."
    "Elise walks you to the door. When you arrive she gives you a small bag of coins."
    mc "You don't have to pay me! Especially not after what we did."
    eli "You also helped me clean and I promised to pay you. And you need the money, so take it."
    show elise laughing with Dissolve(0.2)
    eli "Cleaning your pipes was a bonus for us both."
    mc "Well, thank you! I'll see you tomorrow, then."
    show elise neutral with Dissolve(0.2)
    eli "Yes. Tomorrow."
    play sound frontdoor
    stop music fadeout 1
    scene village day 2 with Dissolve(2)
    play ambient town
    "You head outside."
    mc "{color=#b7b7b7}{i}That was intense.{/i}{/color}"
    mc "{color=#b7b7b7}{i}It's too early for the Elder's medicine to be finished. Maybe I should head out to the lake to get some fish for tonight.{/i}{/color}"
    scene black with Dissolve(2)
    $ persistent.elise_facial = True
    $ renpy.end_replay()
    "Later"
    stop music fadeout 1
    stop ambient fadeout 1
    stop ambient2 fadeout 1
    scene lake sunny with Dissolve(2)
    "You arrive at the lake. The smell of overripe fruit fills your nostrils."
    mc "{color=#b7b7b7}{i}I guess the storm knocked all the apples down. Kind of a shame. Not really important though, I need to get fishing.{/i}{/color}"
    "You walk to the edge of the lake looking for the best place to cast your line."
    mc "I wonder where the best place to catch Waryfish is?"
    '???' "Not here."
    play music dreaming fadein 1
    "You look to where the voice is coming and see a black haired woman in the water."
    mc "Oh, Brooke? Is that you?"
    scene mermaid intro with Dissolve(2)
    hide window
    w ""
    "The woman swims closer to you with her scales shinking in the sun. This is clearly not Brooke."
    mer "Brook? This is a lake, human."
    mc "You... you're a mermaid!"
    mer "Indeed. Do all humans have such a gift for regocnizing the obvious?"
    mc "{color=#b7b7b7}{i}First Selena and now the Mermaid! What's going on?{/i}{/color}"
    mer "Is it really that suprising to see a mermaid in the water?"
    mc "Yes, but it's not that. I think I saw you before."
    mer "I don't think so. I don't remember meeting you, and I remember everything."
    mc "{color=#b7b7b7}{i}This isn't a dream, she's definitely here!{/i}{/color}"
    mer "Are you staring at my breasts?"
    mc "Sorry."
    mer "Go right ahead. I find it amusing how you humans are so fixated on them. Look all you want."
    mc "Uh, thank you."
    mer "Oh, and to answer your question, the best place to fish is actually to the south. Follow me if you want."
    "The mermaid swims to the south of the lake and you follow her."
    play sound walkgrass
    scene black with Dissolve(2)
    pause 2
    scene lake sunny with Dissolve(2)
    mc "{color=#b7b7b7}{i}Fuck! This is really happening! A mermaid? I can’t believe I just saw one! people say they are dangerous creatures, but maybe it’s all just legends?{/i}{/color}"
    mc "{color=#b7b7b7}{i}I’m so curious, I can’t miss this chance and run from her! I have to be careful, but I need to know what's going on here.{/i}{/color}"
    n "You follow the road to the southern part of the lake when you arrive, the Mermaid emerges from the water."
    n "She throws a half dozen fish onto the shore."
    nvl clear
    mc "What are those for?"
    show mer neutral with Dissolve(1)
    mer "I thought I'd save you some time."
    mc "How is it I saw you in my dreams? I remember now, back then after I talked to you a storm began. Did you have something to do with that?"
    mer "I give him fish and he asks me boring questions."
    mer "Normally you should thank someone who helps you."
    mc "Thank you. But you didn't answer me."
    mer "Then answer me. Why did you need all these fish?"
    mc "My father is sick. He needs fresh food to keep his strength up."
    mer "Do you normally spend your days assisting others? For no advantage to yourself?"
    mc "Sometimes? It depends."
    mer "Humans are indeed strange."
    mc "{color=#b7b7b7}{i}She thinks I'm strange? She's the one with her tits hanging out!{/i}{/color}"
    "You feel your loins stir. The Mermaid stares at you."
    mer "Oh ho, that took longer than I thought."
    mc "{color=#b7b7b7}{i}Again? What is wrong with me lately?{/i}{/color}"
    mer "You know, since you seem to enjoy helping others perhaps you can help me."
    mc "Help you with what?"
    mer "That thing looks very uncomfortable."
    mer "Why don't you come and swim with me?"
    mc "Sure.{w} I mean no!"
    "You just want to take me to your undersea palace! Then by the time I get back a thousand years will have passed."
    show mer confused with Dissolve(0.2)
    mer "That's absurd! I just want to help you with your problem."
    mc "I..."
    mer "Come on. Join me."
    mc "{color=#b7b7b7}{i}I just got off earlier, but I think I have to do it again already. It's getting harder to control myself.{/i}{/color}"
    mc "{color=#b7b7b7}{i}What am I doing? I’m gonna die! I just... I can’t resist her - the opportunity to be with a beautiful mermaid! A fucking mermaid! Maybe any other day I wouldn’t take this risk, but today...{/i}{/color}"
    mer "Take off your clothes and join me."
    "You remove your clothes and enter the shallows of the lake."
    scene mermaid paizuri 1 with Dissolve(2)
    hide window
    w ""
    mer "Look at this amazing cock you have here!"
    "She wraps her breasts around your cock. They're cool to the touch and soothing. Her skin is impossibly smooth."
    mer "You’re already so hard! Do you like when I do this? Do you like having it between my breasts?"
    mc "Your skin feels like silk!"
    mer "Do you want to cum on me? I want you to."
    mc "Of course I do."

    scene mermaid paizuri 2 with Dissolve(2)
    hide window
    w ""
    mer "Then I need a little favor. Just make me a promise and you can shoot your load wherever you want."
    mc "Anything."
    mer "I need a Blue Flower."
    mc "Sure! Whatever you want."
    mer "You promise you'll bring me one, human?"
    mc "Yes! Of course."
    mer "Very well then."
    "The mermaid speeds up her movements and the smooth cool sensation drives you over the edge."
    mc "Ah..."
    mer "Cover me up!"

    scene mermaid paizuri 3 with Dissolve(2)
    hide window
    w ""
    "She keeps milking you with her tits and you shoot load after load onto her face. Just when you think you can't cum anymore she coaxes even more out of you. It's as if her touch extended your orgasm."
    "The drops of your semen mix with the water dripping down her... she looks up at you with a develish grin."
    mer "You taste good human. I may have to drink human seed more often, it's a nice change."
    mer "Oh, and there was so much! This feels great and seems like you can keep going! Looks like you are a really good human to... Anyway, come back with my flower and I'll make you feel even better!"

    scene lake sunny with Dissolve(2)
    show mer neutral with Dissolve(1)
    mer "And because I like you I'll even answer those annoying questions of yours."
    mer "I'll be back here the next time you dream with me. Don't forget my flower or I'll be very cross with you."
    mc "I- I won't."
    "The mermaid smiles at you with a look in her eyes like that of a cat playing with its food."
    mer "Thank you. We will meet again soon."
    "And with that she swims away."
    hide mer with easeoutleft
    stop music fadeout 1
    mc "Man, she really likes blue flowers."
    "You kneel down and pick up the fish the mermaid left on the shore."
    mc "I don't know why people say mermaids are bad luck. She really helped me out here. In more ways than one."
    mc "I wonder if the elder is done brewing his potion. I'll stop by his house on my way home."
    jump Day6Elder

label Day6Elder:
    play sound walkgrass
    scene village destroyed with Dissolve(2)
    pause 2
    "You knock on Silas' door."
    play sound knock1
    pause 1
    play sound frontdoor
    show mia neutral with Dissolve(1)
    mc "Mia! I didn't expect to see you here."
    show mia ashamed with Dissolve(0.2)
    mia "I wanted to stay with Redd, but [Nova] kicked me out."
    mc "She what?"
    mia "She said \"I got this. And you need some sleep or a drink. Probably both.\" I tried to protest, but she pushed me out!"
    mia "Is [Nova] mad at me? I thought she liked me but she just threw me out."
    mc "Of course she likes you. That's why she kicked you out. It's her weird way of saying thank you I think."
    show mia neutral with Dissolve(0.2)
    mia "I hoped it was something like that."
    mc "So, is Silas home?"
    "Mia nods."
    mia "Uh-huh. Come in."
    scene elders house with Dissolve(2)
    "Mia sees you in and calls Silas over."
    show mia neutral at slightleft with Dissolve(1)
    show elder neutral at slightright with Dissolve(1)
    eld "Ah, [MC]!"
    mc "Hello, Elder. Any news?"
    eld "Nothing good I'm afraid."
    mc "You couldn't find a cure?"
    eld "I did, but..."
    mc "But what?"
    eld "Let me show you."
    scene elder book with Dissolve(1)
    play music reddsick fadein 1
    hide window
    w ""

    "The elder pulls out a large book on medicine."
    eld "I found out about a cure that does exist - The Blue Flower is almost the exact opposite of the Venomair. If prepared correctly it has the ability to counteract the venomous spores."
    mc "That's great news then!"
    eld "It would be, but... I'm sorry, [MC]."
    mc "What? It only grows far from here?"
    eld "No, actually it grows nearby."

    scene elders house with Dissolve(2)
    show elder neutral with Dissolve(1)
    mc "So what's the problem? Tell me where to go and I'll go pick it up."
    eld "It only grows on the Goblin's Mountain."
    mc "Then I just go and get it."
    eld "You aren't trained for this. And as much as I respect Trevor and Lisa's militia, they aren't either."
    eld "If Vincent was still alive, then maybe, but..."
    mc "We don't need anyone else. I'm going myself."
    eld "I forbid it!"
    mc "I don't care, this is my dad!"
    eld "The goblins do not grant mercy to anyone, let alone someone who trespasses on their territory. A single goblin is extremely dangerous, the mountain is filled with them."
    mc "But..."
    eld "The potion I'm brewing will help with your father's recovery. I have high hopes that a strong man like Redd will beat the odds."
    eld "But you have to prepare yourself for the possibility that-"
    mc "But if you had the flower, it would be a sure thing."
    eld "Very nearly. I have all the other ingredients here."
    mc "And the city doesn't have any?"
    eld "The bridge to the Capital is getting fixed, but the river is too strong to ford right now, and it might not make it in time."
    eld "Right now there is no way to even place an order."
    eld "[MC], I know this is hard to hear. There is still hope, but for now, go home and be with your father. No matter what happens you should stay with him."
    "Silas closes the book and leaves it on the table."
    eld "I need to begin brewing the next batch of medicine. What I left should last a few days. If you need anything, I'll be here."
    hide elder with easeoutright
    "The elder enters his alchemy lab."
    mc "{color=#b7b7b7}{i}Damn it all! What can I do here?{/i}{/color}"
    mc "{color=#b7b7b7}{i}I need that flower. I....{/i}{/color}"
    mc "{color=#b7b7b7}{i}I know what I have to do.{/i}{/color}"
    jump Day6End

label Day6End:
    play music drama2 fadein 1
    scene farm bedroom night with Dissolve(2)
    "You enter your room. and set your pack on your bed."
    mc "OK, how am I going to do this?"
    "Your door opens."
    play sound bedroomdoor
    show nova neutral with Dissolve(1)
    nov "Do what?"
    mc "Nothing."
    show nova angry with Dissolve(0.2)
    nov "You come in, you don't even check on Redd. What's going on? Did you forget about the fish?"
    mc "No, they're right here."
    "You point to some fish tails hanging out of your bag"
    nov "On the bed?! Ew! You know we're sleeping there, right?"
    mc "Not now, [Nova]."
    show nova worried with Dissolve(0.2)
    nov "What happened?"
    mc "Nothing."
    nov "Don't lie to me."
    mc "I went to see the elder to get the medicine."
    nov "And?"
    mc "Silas told me that he found a cure."
    show nova excited with Dissolve(0.2)
    nov "A cure? That's great!"
    mc "..."
    show nova worried with Dissolve(0.2)
    nov "Why isn't this a happy thing?"
    mc "..."
    nov "He can't get it, can he?"
    mc "He won't."
    mc "Here, take a look. There's a flower that can save dad."
    nov "Why didn't the elder mention this before?"
    mc "Because it only grows on the Goblin's Mountain, and he says going there is suicide."
    show nova sad with Dissolve(0.2)
    nov "Damn it..."
    mc "But what does he know? I'm going to the mountain, [Nova], I won't let dad die, I don't mind the risk."
    scene black with Dissolve(2)
    scene EndOfChapter3 with Dissolve(3)
    $ persistent.ch3 = True
    pause

    jump Day6EndCH4
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
