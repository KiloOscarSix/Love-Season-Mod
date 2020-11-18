label Day4WakeUp:
    stop ambient2 fadeout 1
    scene black with Dissolve(5)

    scene selena dream 1 with Dissolve(1)
    scene selena dream 2 with Dissolve(1)
    scene mermaid intro with Dissolve(1)
    show black with Dissolve(1)
    show fairy neutral with Dissolve(1)
    scene black with Dissolve(2)
    w ""
    mc "Wha?"
    scene cave campsite with Dissolve(2)
    "You wake up alone on the tarp."
    mc "That dream again..."
    mc "Nina?"
    "She's nowhere to be found."
    mc "{i}Where is she?{/i}"
    if NinaProposition == 1:
        mc "Did I go too far when we talked last night?"
    mc "{i}*I'd better get up.*{/i}"
    scene cave entrance with Dissolve(2)
    "You get up and check out the entrance. Nothing seems to be out of place and the weather actually seems pleasant outside."
    show nina smiling with Dissolve(0.3)
    nin "Finally up? How is it you can still sleep in, even when you're sleeping on the floor?"
    mc "I like sleeping. Sleeping is one of life's greatest pleasures."
    mc "Right next to eating, and s-"
    "You stop mid sentence."
    show nina neutral with Dissolve(0.3)
    nin "[MC], you don't need to walk on eggshells around me."
    if NinaProposition == 1:
        show nina crossing with Dissolve(0.1)
        nin "But my answer still stands."
    show nina neutral with Dissolve(0.3)
    nin "I'm sure we'll get back to normal soon enough."
    mc "Nothing more normal than sleeping in."
    nin "That's true, and you've even got your morning wood to boot!"
    mc "Shit! Again?"
    "You look down."
    show nina smiling with Dissolve(0.3)
    nin "Gotcha!"
    scene cave campsite with Dissolve(2)
    "As you return to the camp to grab the last of your supplies, Nina tells you that she scouted out ahead before you woke up."
    mc "You could have waited for me."
    nin "Sorry, I really needed the fresh air."
    mc "Yeah. So how's it looking?"
    nin "Well, the route is muddy for sure but it looks like none of the paths nearby are blocked."
    nin "The animals are coming back, so we should probably get moving before the monsters decide that their meals aren't in hiding anymore."
    mc "Good point."
    mc "And it's not like we have to pack."
    scene cave entrance with Dissolve(2)
    mc "Ready whenever you are."
    show nina neutral with Dissolve(0.3)
    nin "Ok, then..."
    mc "After you."
    play sound walkgrass
    scene forest path with Dissolve(2)
    "You and Nina exit the cave and walk through the forest."
    play music afternoon fadein 1
    show nina neutral with Dissolve(0.3)
    mc "Crazy how just a couple of nights ago this forest was both wet and burning."
    nin "This whole thing has been surreal honestly. Like a dream."
    mc "I know, right?"
    nin "Just be careful, we don't know what's out here."
    mc "Since when are you the designated leader?"
    show nina angry with Dissolve(0.3)
    nin "Hey, just because you got all badass killing the goblin doesn't mean I can't take point sometimes!"
    show nina worried with Dissolve(0.3)
    nin "And you're still injured."
    mc "It's feeling a lot better this morning, actually."
    show nina smiling with Dissolve(0.3)
    nin "Well, considering you can't beat me when you're at full strength..."
    mc "What now?"
    nin "I still kick your butt at wrestling."
    mc "You most certainly do not! We haven't wrestled since we were kids."
    nin "Because I whooped you."
    mc "I just didn't want to hurt a girl. I let you win."
    show nina angry with Dissolve(0.3)
    nin "Big words for someone who hasn't won once. Come here, I'll show you my skills."
    mc "W-Wait! I'm not going to fight you Nina!"
    nin "Scaredy-cat!"
    mc "Did you hear the part about hurting a girl?"
    show nina moreangry with Dissolve(0.3)
    nin "I did! Not good enough. Try again."
    mc "I... Not going to..."
    scene nina fight 1 with Dissolve(2)
    nin "Looks like I'll have to force you!"
    "Nina grabs you and puts you in a hold."
    nin "Got you!"
    scene nina fight 2 with Dissolve(2)
    mc "Hey, watch it!"
    nin "Stop complaining and accept your doom!"
    mc "I will not!"
    scene nina fight 3 with Dissolve(2)
    "You shift your weight and grab Nina by the waist. Nina loses her balance and laughs as you fall to the ground with her."
    nin "It's not over yet!"
    mc "Ow! Are you OK?"
    nin "Uh... yeah..."
    "You find yourself between Nina's legs, and your focus disappears for a second. This would have been a normal thing between the two of you just a day ago, but now you can't not think of sex with her."
    scene nina fight 4 with Dissolve (2)
    nin "Hey! Focus on the fight! No mercy, [MC]!"
    "She pushes you away, and you lose a bit of your balance, and that was just the opening she was looking for."
    scene nina fight 5 with Dissolve(2)
    "Nina laughs and pounces on you, puts some weight on your shoulder and you wince."
    mc "Not over yet!"
    "She pushes down against you and you cry out in pain as your shoulder hits a tree root."
    mc "OW! FUCK!!!"
    scene forest path with Dissolve(2)
    show nina worried with Dissolve(0.3)
    nin "Oh shit! Sorry, [MC], I forgot..."
    mc "It's not a problem."
    show nina crossing with Dissolve(0.3)
    nin "I got carried away..."
    mc "Nina, it's fine."
    lis "Awww! Don't tell me the sexually charged wrestling is over?"
    mc "What?"
    nin "Lisa?"
    play music militia2 fadein 1
    show nina at slightleft
    show lisa neutral at slightright
    lis "To the rescue. I'm here to drag your happy butts back to the village."
    mc "The bridge is fixed?"
    lis "Almost. Once the rope was secure I volunteered to shimmy across."
    nvl clear
    n "Lisa delivers the lines in her trademark deadpan tone. You still can't quite read her true emotions, but you're thankful (begrudgingly) that she is here."
    n "The co-founder of the militia reaches out her hand to assist you, and nearly pulls you up all by herself. You're glad you weren't wrestling her instead of Nina."
    n "She's the only person in town who has ever beaten Trevor in a fight besides his father, and no one in town is a better climber or scout."
    n "You always thought she was attractive, but her cold personality is a little off-putting."
    show nina neutral with Dissolve(0.3)
    nin "But you came out here by yourself?"
    lis "Not from lack of Trevor trying. I nearly had to knock your boyfriend out to stop him from killing himself on the ropes."
    "Lisa's only emphasis is in the word 'boyfriend', and that isn't lost on Nina."
    show nina worried with Dissolve(0.3)
    nin "Oh! Well, um, thanks."
    lis "None of my business."
    show nina neutral with Dissolve(0.3)
    nin "How long have you been looking for us?"
    lis "Not long, I was half expecting a couple of bodies actually."
    mc "Sorry to disappoint."
    lis "Surprised. Not disappointed, keep up."
    mc "I'll try."
    lis "Still... Surviving in the wild in a storm like that? No joke."
    lis "You're not nearly the weakling you seem to be, [MC]."
    mc "Thanks?"
    lis "Now if you guys are done with your sexy wrestling time, let's get back to the bridge."
    show nina worried with Dissolve(0.3)
    nin "It's not sexy wrestling!"
    lis "Non sexy platonic wrestling then. Got it."
    scene deep forest sunset
    "The three of you walk back to the bridge. On the way back, you and Nina barely look at each other."
    show lisa neutral at slightright
    show nina neutral at slightleft
    lis "Well, since we're all happy you're not dead, what's the story?"
    nin "We hid out in a cave and rode out the storm."
    lis "That's boring... Details, [MC]?"
    show mc neutral at left
    show nina neutral behind lisa at farright

menu CaveStory:
    "Tell the whole truth [gr]\[LisaInterest +1\] \[CoolStoryBro\] [red]\[NinaLove -1\]":
        hide mc
        show nina neutral at slightleft with Dissolve(0.5)
        mc "The whole truth?"
        lis "Can there ever be?"
        mc "Well, if you're sure. But this stays between us. I don't like to brag."
        show nina worried with Dissolve(0.3)
        "Nina, realizing what you're about to do, tries to frantically wave you off."
        mc "Well we ran through the sheets of rain and lightning, then found a cave."
        mc "Then we huddled together for warmth, naked of course, because of the cold."
        mc "Then the next day while exploring the cave we ran into a goblin. He attacked Nina, then me."
        mc "I led him on a chase into a room with fire crystals and blew him up."
        mc "After which Nina and I made love near an underground lake, illuminated by the glow of natural crystal formations."
        mc "Then we cooked some mushrooms."
        mc "So, you know... the usual."
        "You turn and see Lisa and Nina both stopped in their tracks and staring at you."
        show nina moreangry with Dissolve(0.3)
        nin "Why would you tell her that? What were you thinking?"
        lis "Damn..."
        "Lisa laughs."
        mc "{i}She laughs? That's a little creepy.{/i}"
        lis "You're a funny dude, you know that [MC]?"
        lis "Nice details on the story too!"
        lis "I wouldn't joke like that with Trevor though."
        lis "He's got NO sense of humor."
        mc "It's true..."
        lis "Sure it is! Don't worry you two, your secret's safe with me."
        hide lisa with easeoutleft
        show nina moreangry at center with Dissolve(0.3)
        "Your group keeps walking towards your destination, Lisa laughing the whole time. When Lisa isn't looking, Nina elbows you in the ribs."
        mc "Ow!"
        mc "What was that for?"
        lis "That's what you get for using her in your little hero sex fantasy."
        lis "Man, that made my day!"
        nin "Hmph!"
        "You soon reach the cliffside well."
        $ CoolStoryBro = 1
        $ LisaInterest += 1
        $ NinaLove -= 1
        jump BridgeDone
    "Tell the partial truth":

        mc "Nothing. We holed up in a cave until the storm passed. It was cold, I started a fire."
        nin "We ate some mushrooms. Ran from a goblin... Nearly died. Didn't."
        lis "Man, how is it you can tell a tale of survival and adventure and make it boring?"
        lis "It boggles the mind."
        nin "Sorry."
        lis "Well, that should ease Trevor's mind at least."
        "You soon reach the cliffside well."
        jump BridgeDone

label BridgeDone:
    scene well day with Dissolve(2)
    play music trevor fadein 1
    "Trevor is surrounded by a small group of men including Luke, the Elder and Trevor's father, Darius."
    show trevor angry at center with Dissolve(0.3)
    tre "I'm going..."
    show trevor angry at slightleft with Dissolve(0.3)
    show luke neutral at slightright with Dissolve(0.3)
    luk "Relax... Lisa's got it covered."
    tre "She could be hurt..."
    show darius neutral at center with Dissolve(0.3)
    show luke at right with Dissolve(0.3)
    show trevor annoyed at left with Dissolve(0.3)
    dar "Oh quit whining like a little girl, Trevor."
    tre "Dad! Shut up for once!"
    show darius neutral at slightleft with Dissolve(0.3)
    show elder neutral at slightright with Dissolve(0.3)
    eld "Now calm down you two... We can send out more people as soon as it's safe."
    show darius neutral behind trevor with Dissolve(0.3)
    tre "I don't care, I'm going!"
    play music afternoon fadein 1
    lis "Relax stud. Your girl's right here."
    "Lisa announces you all as she exits the forest."
    tre "Nina!"
    nvl clear
    scene well focus with Dissolve(2)
    n "Trevor rushes over to Nina and hugs her."
    mcn "{i}Awkward...{/i}"
    if NinaProposition == 1:
        mcn "{i}Damn it... I don't like this.{/i}"
        n "Lisa looks at you. If she senses something off with your reaction, you can't tell."
    show trevor neutral at slightright
    show nina worried at slightleft
    nin "Hi..."
    tre "I thought you might be hurt! Or worse!"
    nin "I'm fine!"
    show darius neutral behind trevor at center
    show darius neutral behind nina
    dar "Come on! Kiss her, boy! It's the time for it!"
    tre "Stop it, father..."
    dar "Kids today... All I'm saying is that your girl was off alone with another guy for two days. You need to reassert yourself."
    tre "Whatever."
    tre "Sorry Nina..."
    nin "It's fine."
    hide darius neutral with Dissolve(0.3)
    show trevor neutral at left with Dissolve(0.3)
    show nina neutral behind trevor at slightleft with Dissolve(0.3)
    show elder neutral at slightright with Dissolve(1)
    eld "Well, I am delighted to see that the two of you are safe. With all the monsters in that forest, I had dreaded the worst."
    nin "Most of them were gone, thankfully."
    eld "Tell us what happened!"
    hide nina
    hide trevor
    hide elder
    nvl clear
    n "You're about to start the story when Nina begins. She tells a general outline of what happened."
    n "Trevor stares a little dumbfounded. When Nina mentions her near death experience, he looks at you in shock."
    if CoolStoryBro == 1:
        n "When Nina doesn't bother mentioning the goblin, Lisa smirks."
    else:
        n "She of course leaves out any mention of the goblin, or the sex."
    show luke neutral at slightright with Dissolve(0.3)
    luk "Wow. That was crazy. Also, lucky."
    show elder neutral at slightleft with Dissolve(0.3)
    eld "Indeed."
    mc "I guess so."
    hide luke
    hide elder
    show trevor neutral with Dissolve(0.3)
    "Trevor walks up to you and puts his hand out."
    tre "You kept her safe... again. Thanks."
    show trevor at farright
    show mc neutral at left with Dissolve(0.5)
menu:
    "Shake his hand [gr]\[TrevorFriend +1\]":
        hide mc
        show trevor neutral at center with Dissolve(0.5)
        mc "It was nothing, she watched my ass too."
        "You shake Trevor's hand."
        if TrevorFriend > 0:
            tre "You're cool, the other guys need to give you more credit."
        else:
            tre "You keep surprising me!"
        $ TrevorFriend += 1
        jump BridgeDone2
    "Don't [red]\[TrevorFriend -1\]":

        hide mc
        show trevor neutral at center with Dissolve(0.5)
        mc "Yeah, I did."
        "Trevor looks at his hand, then at you and pulls back."
        show trevor annoyed with Dissolve (0.3)
        tre "Whatever. Just... the thanks still stand."
        $ TrevorFriend -= 1
        jump BridgeDone2

label BridgeDone2:
    scene well day with Dissolve(2)
    show elder neutral at center
    play music morningquiet fadein 1
    eld "You both should come to my place and get looked over."
    mc "I'm fine... Just glad to be home."
    show elder neutral at slightleft
    show nina neutral at slightright
    nin "Same."
    eld "Well, we're glad to have you."
    show darius neutral at center
    dar "Now that this is handled, I should get moving to Redd's house and see if I can salvage anything."
    mc "What happened to the farm?"
    mc "Wait! Is dad ok? What about [Nova]?"
    show elder neutral at slightleft with Dissolve (0.2)
    show trevor neutral behind nina at left with Dissolve (0.2)
    show luke neutral at right with Dissolve (0.2)
    luk "They're good, dude... whole village is copacetic."
    luk "Well, the people anyway."
    show elder neutral behind nina with Dissolve (0.2)
    show nina worried with Dissolve(0.3)
    nin "What do you mean?"
    show nina worried behind elder
    eld "Best you see for yourselves."
    scene black with Dissolve(2)
    stop music fadeout 1
    nvl clear
    play ambient town fadein 1
    n "You follow everyone to the village itself."
    n "As you near the outskirts you already see damaged buildings, ruined crops and torn roofs."
    n "Several villagers are picking up debris, trying to salvage what they can from the destruction."
    scene village destroyed with Dissolve(2)
    mc "What the hell?"
    show nina worried with Dissolve(0.3)
    nin "This is awful!"
    show nina crossing with Dissolve(0.3)
    nin "I-I need to check on dad and mom!"
    nin "I'm sorry. I'll see you later, [MC]!"
    hide nina with easeoutleft
    show trevor neutral with Dissolve(0.3)
    tre "Nina, wait!"
    "Trevor runs after Nina."
    hide trevor with easeoutleft
    show darius neutral with Dissolve(0.3)
    dar "My son. Whooped as ever."
    mc "Silas... How bad is my house?"
    show darius neutral at slightright with Dissolve (0.2)
    show elder neutral at slightleft with Dissolve (0.2)
    eld "I haven't seen it myself..."
    dar "But your father sent for me almost immediately. It's my first priority now that the bridge is done."
    dar "So come on."
    hide all
    "You shake the Elder and Luke's hands goodbye and walk with Darius to your home."
    scene farm destroyed with Dissolve(2)
    stop ambient fadeout 1
    play music reddsick fadein 1
    "When you get there, you are dumbfounded. While part of the roof is intact, much of the rest of the house is shambles."
    scene farm fixing with Dissolve(2)
    "You see Redd and [Nova] picking through the debris and separating usable wood."
    mc "What the fuck?"
    "[Nova] hears your voice and turns her head."
    nov "[MC]!"
    scene farm destroyed with Dissolve(2)
    show nova excited with Dissolve(0.4)
    "She runs over and takes you in a fierce hug."
    mc "OW! Watch the shoulder..."
    "That snaps [Nova] out of it and she backs up."
    show nova blushing with Dissolve(0.4)
    nov "I mean, it took you long enough. We've been working all morning."
    show nova neutral at slightright with Dissolve(0.4)
    show father neutral at slightleft with Dissolve(0.4)
    "Redd comes up to you and places his hand on your shoulder."
    dad "Good to see you, son. I never doubted you for more than a minute."
    mc "Thanks. Hold on... More than a minute?"
    dad "Ha!"
    nov "Really, he wasn't worried at all."
    dad "She was worried sick about you, though."
    nov "I was not! I just didn't want to do extra work."
    "Darius comes up and puts his hand on [Nova]'s shoulder."
    show darius neutral behind nova at right with Dissolve(0.1)
    dar "Always willing to help you with {i}anything{/i} you might need, [Nova]."
    show nova annoyed with Dissolve(0.3)
    "She moves away from him, but doesn't say anything."
    show darius neutral at slightright with Dissolve(0.1)
    show nova neutral behind darius at right with Dissolve(0.4)
    dad "Now, Darius, what do you think?"
    "Darius looks over the house."
    dar "Yep, this house is well and truly fucked."
    show darius neutral behind nova with Dissolve(0.1)
    show nova smirk with Dissolve(0.3)
    nov "That your professional opinion?"
    dad "Forgive her, she's on edge."
    show nova neutral behind darius with Dissolve(0.3)
    dar "I understand. I have to say though, the whole village is in bad shape, but it looks like the storm hated you personally."
    dad "So, what will it take to fix it?"
    dar "Most of the beams are beyond saving. So long as the roof doesn't collapse you might be able to save some of your furniture, I guess."
    dar "Even if I had the lumber available, which I don't, it would cost way too much to fix it."
    dar "Level with me Redd, how much can you afford?"
    dad "I have about 10,000 gold saved up."
    mc "Dad!"
    show nova surprised with Dissolve(0.1)
    show darius behind nova with Dissolve(0.1)
    nov "That's everything we have..."
    dad "I know, but this has to be done."
    show nova neutral behind darius with Dissolve(0.1)
    dar "It's a tidy sum, but honestly, that won't even cover new materials."
    dad "What if we use one of the walls and make something smaller?"
    dar "That could work."
    dar "OK, here's what we'll do, we'll salvage some of the wood here. Then, like you said, we use that to build a new, smaller house."
    mc "How small are we talking?"
    dar "One less bedroom, for certain."
    nov "That sucks..."
    dad "We can work with that."
    dar "6000 should cover my labor, and I'll scrounge together enough to get a solid roof up there too. I'll need about 3000 for that. Those are friend prices."
    show nova angry with Dissolve(0.3)
    "[Nova] mutters under her breath."
    nov "Sure they are."
    "You glance over at [Nova]."
    mc "I know, just... relax."
    dad "Can we start right away?"
    dar "Of course."
    dad "Perfect."
    "Darius leaves."
    hide darius with easeoutright
    show nova at slightright with Dissolve(0.3)
    nov "I don't like him."
    dad "Darius is just a little... raw. But he's helped the village out quite a bit, [Nova]."
    show nova neutral with Dissolve(0.3)
    nov "I guess."
    dad "Let's get to work. While we clean up [MC] can tell us about his romantic adventure with Nina."
    mc "It wasn't like that, Dad!"
    nov "So what {i}was{/i} it like? I want to know too!"
    "You sigh and recount an edited version of the story to your father and [Nova]. Leaving out the goblin and everything after."
    dad "So how did you hurt your shoulder?"
    mc "I fell on a rock."
    show nova smirk with Dissolve(0.3)
    nov "Clumsy as always!"
    dad "Are you able to help?"
    mc "I'll do what I can."
    dad "Good, we need everyone working at least somewhat."
    dad "I'm sorry, I'm sure you'd prefer to rest."
    mc "It's fine, dad, don't worry."
    play ambient fixing fadein 1
    scene black with Dissolve(2)
    "After a while..."
    scene farm destroyed with Dissolve(2)
    play music nova fadein 1
    "You and [Nova] are sorting some wood."
    show nova neutral with Dissolve(0.3)
    nov "I wish dad wasn't working with Darius."
    mc "You really don't like him, do you?"
    nov "He's always hitting on me, asking if I want to be his apprentice."
    nov "It's creepy!"
    mc "Maybe he's just being nice?"
    nov "You don't believe that."
    mc "..."
    mc "No. "
    show nova tease with Dissolve(0.3)
    nov "Still... Maybe if I bat my eyes at him he'll think of us and give us a discount."
    show mc neutral at left with Dissolve(0.5)
    show nova at farright

menu NovaFlirtDarius:
    "Don't do it [gr]\[NovaLove +1\]":
        hide mc
        show nova at center with Dissolve(0.5)
        mc "Bad idea! I wouldn't want to be in a room alone with him if I were you."
        mc "I mean, he's nice enough to me, but you don't like him. Don't force yourself."
        show nova neutral with Dissolve(0.3)
        nov "Yeah... you're right. I wouldn't want him to try to take things too far. And you heard the rumor about Heather."
        mc "Exactly."
        mc "Plus if he did something I'd have to kick his butt."
        show nova smirk with Dissolve(0.3)
        nov "Aww... You'd do that for l'il ol' me?"
        mc "Of course! No one messes with this household."
        $ NovaLove += 1
        $ NovaDarius = 0
        jump FinishFixing
    "Go for it. [gr]\[NovaDarius\] [red]\[NovaLove -1\]":

        hide mc
        show nova at center with Dissolve(0.5)
        mc "It might not be a bad idea."
        mc "I mean, that horn dog is clearly hard up."
        show nova smirk with Dissolve(0.3)
        nov "Takes one to know one?"
        mc "Ignoring that..."
        show nova neutral with Dissolve(0.3)
        nov "But... What if he try to take things too far?"
        mc "Like you'd ever do anything against your will..."
        mc "Just string him along."
        mc "It'll help us all out."
        nov "I... I guess you're right."
        $ NovaLove -= 1
        $ NovaDarius = 1
    "You and [Nova] get back to work."


label FinishFixing:
    scene black with Dissolve(2)
    scene farm destroyed with Dissolve(2)
    nov "Oh... By the way... Your porn mags are all destroyed."
    mc "No! Damn it all to hell."
    scene black with Dissolve(2)
    scene farm destroyed with Dissolve(2)
    nvl clear
    n "Some time later, Darius returns with some other villagers to help you fix up your house."
    scene farm fixed with Dissolve(2)
    play music redd fadein 1
    n "Right around sundown you finally finish."
    n "It goes better than you had hoped. Outside the loss of [Nova]'s room and the bathroom, the rest of the interior is nearly identical."
    n "In fact, at first glance, the exterior is the same as well."
    scene farm fixed with Dissolve(2)
    show darius neutral with Dissolve(0.3)
    dar "Not one of my masterpieces. But it will keep you warm at night."
    show father neutral at slightleft
    show darius neutral at slightright
    dad "Here's your gold, Darius. That should cover it."
    dar "Yep, that's all of it."
    dad "Thanks for the help, my friend. I owe you one. And all the rest of you, too."
    "Redd shakes the hands of the villagers and they all head on their way except for Darius."
    dar "Much obliged, Redd. Take care of yourself."
    dar "You too, kids."
    "Darius nods at you."
    mc "We will."
    nov "Don't worry."
    hide darius with easeoutright
    "Once Darius has left, you all head inside the new house."
    scene farm house interior night with Dissolve(2)
    mc "Man, I am beat!"
    show nova neutral at slightright
    nov "We all are!"
    show father neutral at slightleft
    dad "Well, maybe if you actually worked every day, you wouldn't be so tired."
    mc "Hey! Thrilling cave adventure over here! Plus, don't tell me you aren't tired, old man."
    dad "Oh gods, no! I want to pass out. My bed is calling to me."
    show nova smirk with Dissolve(0.3)
    nov "Don't you ever change, Redd."
    dad "[MC]! You and I will be sharing a bed now that we only have two in the house."
    show nova surprised with Dissolve(0.3)
    nov "What? No way!"
    nov "Don't make me the odd one out. It's your house, Redd, you get your own bed."
    mc "I'm not even considered for this, am I?"
    dad "Nope."
    show nova smirk with Dissolve(0.3)
    nov "Nope."
    dad "I appreciate the offer, [Nova], but..."
    show nova angry with Dissolve(0.3)
    nov "But nothing."
    nov "You'd rather sleep with me anyway, right, [MC]?"
    mc "{i}Phrasing, [Nova].{/i}"
    mc "But annoying as it can be, she's right, dad."
    dad "Fine. If you two are so insistent - I was trying to save [Nova] from your poor hygiene, but since she'll have none of it."
    mc "My family, lords and ladies."
    dad "Well, either way, get some sleep. There is a lot we'll have to discuss tomorrow."
    dad "We need to get this farm back on its feet."
    show nova neutral with Dissolve(0.3)
    nov "Right..."
    mc "We'll need some money too. Fast. That was just about our entire savings."
    dad "Exactly. Good to see you on the ball."
    dad "All this can wait, though. I'll see you all tomorrow morning."
    "Redd looks at you, and you can see pride in his eyes as he says the following."
    dad "It's good to have you back, son."
    mc "Thanks, dad."
    dad "Ok, enough of that. Good night you two."
    hide father with easeoutleft
    "Redd leaves for his room."
    play music nova2 fadein 1
    show nova neutral at center with Dissolve(0.3)
    "[Nova] stares at you."
    mc "What?"
    nov "Just thinking..."
    mc "About?"
    nov "Our sleeping arrangements. How Darius is kind of a pig... But mostly how you're hiding something."
    mc "I don't know what you mean."
    show nova smirk 2 at center with Dissolve(0.3)
    nov "Yeah, you do."
    "You sigh and walk into the house, stretching as you head to your room. After a couple of nights in a cave, sleeping in a bed will be glorious."
    nov "Not so fast! Ladies first."
    scene nova bedroom 1 with Dissolve(2)
    "[Nova] enters your room and leaves the door a little open so you can talk."
    nov "How long has it been since we've slept in the same bed?"
    mc "It has to be... years. I guess when you first moved in..."
    nov "Feels like forever ago."
    scene farm bedroom night with Dissolve(2)
    "[Nova] opens the door."
    show nova bed neutral with Dissolve(0.3)
    nov "Come on in."
    mc "Thanks. It's funny, I was so confused when dad brought you in, and then I had to share my room!"
    nov "It was tough on me too. It's not like I knew you all that well!"
    mc "Yeah, and my bed was tiny."
    show nova bed teasing with Dissolve(0.3)
    nov "It still is. Though when you think about it, Redd offered the bed to me, so I guess it's MY bed now."
    mc "Not how it works!"
    nov "Sorry, them's the rules."
    mc "Can we just get to sleep now? I've had a really long couple of days and I'm not in the mood for your teasing, [Nova]."
    nov "Ok, fine. But only on account of you being a hero and all."
    "[Nova] jumps into bed."
    nov "Come on, hop in!"
    show nova bedroom 2 with Dissolve(2)
    "You look at [Nova] in the bed and immediately think of sex. That's something that you are not at all comfortable contemplating right now."
    mc "{i}What the hell am I thinking? I just...{/i}"
    if FuckedLaura == 1:
        mc "{i}Twice! in a few days...{/i}"
    mc "{i}And this is [Nova]. {i}[Nova]{/i}. Something is clearly wrong with me.{/i}"
    nov "What? Am I on your side?"
    mc "No."
    nov "Then get in already."
    "You nod and slide under the covers."
    scene black with Dissolve(5)
    scene EndOfChapter2 with dissolve
    "To be continued. Now would be a good time to save."
    "Thank you for playing Love Season. Please look forward to our next chapter and consider helping us on Patreon, join our Discord and check our other game - Farmer's Dreams!"
    $ persistent.ch2 = True
    jump Chapter3Start
    return
    jump Chapter3Start
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
