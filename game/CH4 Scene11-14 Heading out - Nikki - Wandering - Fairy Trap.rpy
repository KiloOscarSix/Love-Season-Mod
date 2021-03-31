label Day8Start:
    scene black with Dissolve(2)
    "You barely slept the night before. You let [Nova] and Mia share your bed and slept in one of the bedrolls inside your father's room."
    dad "I... Katherine... are you sure?"
    play music dreaming fadein 1
    "You stir in your bedroll and look up at your father. He's sweating again, and tossing in his sleep."
    dad "Katherine... please..."
    scene redd sick 4 with Dissolve(2)
    mc "{color=#b7b7b7}{i}He's dreaming of mom.{/i}{/color}"
    "You go to the kitchen and get your father's medicine."
    mc "{color=#b7b7b7}{i}The girls are still asleep. I'll handle giving dad his medicine.{/i}{/color}"
    "As you come back from the kitchen your father groans and tosses in his bed a bit."
    "You sit down next to him and help him up."
    mc "Dad?"
    scene redd sick neutral with Dissolve(2)
    "Redd slowly comes to consciousness and looks at you."
    dad "Oh, [MC]. Good morning."
    mc "Morning."
    "You hand your father the medicine."
    mc "Can you hold this?"
    dad "Yes, I'm not that far gone yet."
    mc "Of course you aren't."
    "Redd takes the medicine from you and drinks it quickly."
    scene redd sick dubious with Dissolve(1)
    dad "Bah! You might want to sweeten that up next time. It tastes awful."
    mc "I'll consider it."
    dad "Sorry to keep you and [Nova] worried. The elder wasn't kidding, those damn spores pack a kick it seems."
    mc "You'll beat it, dad."
    "Redd smiles."
    scene redd sick neutral with Dissolve(1)
    dad "I'm still pretty tired son, I think I'm going to rest some more."
    mc "Yeah, of course."
    scene redd sick 4 with Dissolve(2)
    "Redd lies down and is soon asleep again."
    mc "Just hang in there, dad. I'm going to save you."
    mc "I'm going to the Goblin's Mountain. I'm leaving you with [Nova] and Mia."
    mc "Yeah, they're gonna hate me for it when I get back, but if something happened to them..."
    mc "If I die, well, at least I know I died doing the right thing. But if they were hurt..."
    nov "It's our choice."
    scene farm redd room night with Dissolve(2)
    "You look over your shoulder to see [Nova] standing in your dad's bedroom door."
    mc "Huh..."
    show nova neutral with Dissolve(1)
    nov "Sorry to interrupt your confession. And I'm not even pissed that it's what you feel you have to do."
    nov "But I'm not letting you sneak off."
    "You sigh."
    mc "Well, I guess I tried."
    show nova smirk with Dissolve(0.2)
    nov "Not really much of an attempt. I mean, you didn't even make it out the door before I found you out."
    mc "Yeah, yeah."
    nov "So, no more trying to run off on your own?"
    mc "Fine."
    show nova smirk 2 with Dissolve(0.2)
    nov "Good. Because I don't think you want to deal with a pissed off Mia."
    nov "Come on. We're getting ready."
    mc "Actually, I just realized, I need to check with Nina."
    nov "Looking for another fight?"
    if NinaLeavingTalk == 1:
        mc "No. I just need a favor."
    else:
        mc "Not if she isn't. But I don't want to leave it like it was last night. Just in case."
        mc "Plus, I need a favor."
    show nova neutral with Dissolve(0.2)
    nov "OK. Meet us at the road to the mountain then."
    mc "I will."
    nov "And if you try to go alone and we don't see you there... we're going anyway. Without you."
    mc "Don't worry, I said I'll wait for you. See you there."
    scene black with Dissolve(2)
    play sound walkgrass
    stop music fadeout 1
    "You grab your gear and walk over to Nina's house. You see her grandmother sitting in a rocking chair out front."
    play music lessrainforest fadein 1
    scene ninahouse exterior with Dissolve(2)
    show grandma neutral with Dissolve(1)
    gra "Oh, aren't you up early, [MC]?"
    mc "Morning, Granny! You're up early."
    gra "When you get to be my age, sonny, you'll be lucky to wake up later than dawn."
    mc "Is Nina around?"
    play sound frontdoor
    play music nina1 fadein 1
    show grandma neutral at slightright with easeinleft
    show nina neutral at slightleft with Dissolve(1)
    "Nina's front door opens and she walks outside."
    nin "Grandma, tell daddy I'm staying at Laura's for a couple of-"
    show nina worried with Dissolve(0.2)
    "She looks over and realizes you're standing there."
    mc "Hey."
    nin "Um, hey."
    "You and Nina both look like you want to say something. Nina's grandmother laughs."
    gra "Jeez, you kids. Just talk it out, fuck it out, whatever. I'm going inside."
    gra "For the record, there's a spot in the middle of the orchard where you can't be seen from inside the house. Or the road."
    gra "If you're gonna get down to no good, that's where I'd do it."
    show nina surprised with Dissolve(0.2)
    nin "Grannie!"
    hide grandma with easeoutleft
    "Nina's grandmother ignores her and goes back inside."
    show nina neutral with Dissolve(0.2)
    nin "She always... Ah! Whatever."
    "You and Nina start walking through her family's orchard."
    scene orchard with Dissolve(2)
    show nina angry with Dissolve(1)
    nin "I'm still pretty pissed at you."
    mc "Yeah, I figured."
    if NinaLeavingTalk == 0:
        show nina neutral with Dissolve(0.2)
        nin "What's your deal?"
        mc "My deal? I'm not the one who ran into her friend's house screaming."
        show nina moreangry with Dissolve(0.2)
        nin "I did not come in screaming, thank you very much. I asked [Nova] a question and she was a bitch about her response."
        mc "She shouldn't have been. But she's stressed out over dad."
        show nina neutral with Dissolve(0.2)
        nin "I know. I would be too. Can we just not talk about her?"
        mc "Fine, so about what then?"
        nin "You still haven't answered my question. What's going on with you?"
        mc "Nothing. I just have to save dad, or at least try."
        show nina worried with Dissolve(0.2)
        nin "Did you think of asking the militia for help? You know I could swing a favor or two."
        mc "I gathered. But I won't ask someone uninvolved to go with me. And let's be honest, they're a bunch of kids just like us."
        show nina neutral with Dissolve(0.2)
        nin "At least they know how to fight."
        mc "Even so."
        nin "But you're fine with [Nova] and Mia going along?"
        mc "They both more or less forced me."
        nin "With [Nova], I buy it. But Mia?"
        mc "When she gets assertive it's a little scary, to be honest."
        show nina smiling with Dissolve(0.2)
        nin "I'm kind of sad I missed that."
        mc "You should be. It was amazing."
    show nina neutral with Dissolve(0.2)
    nin "I'm trying to be OK with this. I really am..."
    show nina worried with Dissolve(0.2)
    nin "But then I'm back in that cave and I see you on the ground, when I thought..."
    nin "You know what, it's pointless."
    mc "Nina, I'll be OK."
    show nina angry with Dissolve(0.2)
    nin "You tell me that again and I'm gonna kick your butt so hard you won't even THINK of going out there to die."
    nin "Actually, that's perfect. You want to go? Without the militia?"
    nin "Prove you can beat me."
    mc "Nina, come on..."
    show nina smiling with Dissolve(0.2)
    nin "Lisa won't save you this time."
    mc "Save me? I think you don't really remember how it went down."
    nin "I totally had you!"
    mc "Nina, you know I haven't really tried since we were kids, right?"
    show nina angry with Dissolve(0.2)
    nin "A likely story. I'm not letting you go otherwise, so you'd better make peace with it."
    "Nina starts pushing you back."
    nin "How are you going to do this if you can't even beat me?"
    show nina moreangry with hpunch
    play sound hit
    mc "Nina! Stop playing around!"
    show nina neutral with Dissolve(0.2)
    nin "Who's playing? I'm just pointing out your weak skinny arms have no chance against me!"
    show nina moreangry with hpunch
    play sound hit
    mc "I'm going to get you for that one."
    show nina neutral with Dissolve(0.2)
    nin " Ha! There we go! Come on!"
    nin "You beat me, I won't complain anymore. You can do whatever you want, I won't try to stop you."
    mc "You sound insane right now, you get that, right?"
    show nina moreangry with Dissolve(0.2)
    nin "Now you know what it's like talking to a crazy person!!"
    show nina moreangry with hpunch
    play sound hit
    "You step back onto an apple and fall backwards onto the ground."
    scene nina kiss 1 with Dissolve(2)
    hide window
    w ""
    mc "OW!"
    nin "See? You can't even take a little bump."
    mc "I tripped!"
    nin "So? The monsters won't care!"
    scene nina kiss 2 with Dissolve(2)
    hide window
    w ""
    nin "Now, admit I beat you. And stop doing all this crazy stuff!"
    mc "No way! This isn't even fair. You know I can't really fight back!"
    nin "You're not a fighter, you can't fight back against the monsters either"
    nin "You lose, [MC]!"
    mc "I do not! I'm just not going to fight you!"
    scene nina kiss 3 with Dissolve(2)
    hide window
    w ""
    nin "What about now?"
    "Nina climbs on top of your chest and pins you to the ground."
    mc "For crying out... loud..."
    scene nina kiss 4 with Dissolve(2)
    hide window
    w ""
    nin "Can't even move your arms. You're done."
    mc "{color=#b7b7b7}{i}How serious is she? She's... kinda cute when she's mad.{/i}{/color}"
    mc "{color=#b7b7b7}{i}And sexy as hell when she... OK, this is not the time to think about the cave!{/i}{/color}"
    nin "Ha! Now you can't even respond! No more witty comebacks?"
    "Nina slides down your body to strengthen her pin on you."
    scene nina kiss 5 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Shit! Her ass sliding on me... Oh, for fucks sake, erection! Not now!{/i}{/color}"
    scene nina kiss 6 with Dissolve(2)
    hide window
    w ""
    nin "Admit it! I have you! You lost!"
    mc "Nina! Just stop, joke's over... OK!"
    nin "Then cry for mercy!"
    mc "{color=#b7b7b7}{i}If she rubs up on my hard on I don't think I'm going to be able to pretend it's nothing.{/i}{/color}"
    scene nina kiss 7 with Dissolve(2)
    hide window
    w ""
    "You push upwards with all of your strength catching Nina off guard. Soon you have flipped her over."
    nin "What the-?"
    mc "Looks like I win!"
    nin "What? How did you...?"
    mc "I..."
    nin "..."
    scene nina kiss 8 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}This is just like the cave. I know I shouldn't push it...{/i}{/color}"
    nin "I just... I don't want you to die."
    mc "Nina..."
    nin "You win. Just do whatever you want."
    menu:
        "Kiss her now":
            jump MCKissNina
        "Hold on a second [gr]\[NinaLove\]":
            jump DoNotKissNina

label MCKissNina:
    "You move in for the kiss."
    nin "[MC], what are you doing?"
    mc "Whatever I want."
    scene nina kiss 9 with Dissolve(2)
    hide window
    w ""
    "You capture Nina's lips with your own. You know that you shouldn't - she said the cave was a mistake."
    "Nina's mouth opens halfway, giving you the signal you've been waiting for."
    scene nina kiss 10 with Dissolve(2)
    hide window
    w ""
    "Your tongue enters her mouth, and the kiss deepens."
    mc "{color=#b7b7b7}{i}I wanted to ignore these feelings, to not think about the cave, but I can't.{/i}{/color}"
    scene nina kiss 11 with Dissolve(2)
    hide window
    w ""
    nin "[MC]..."
    "Nina shudders as you kiss her neck, her face becomes flushed at the contact."
    nin "[MC]... Please..."
    scene nina kiss 12 with Dissolve(2)
    hide window
    w ""
    "Nina pushes you away."
    nin "I can't do this."

    scene orchard with Dissolve(2)
    show nina worried with Dissolve(1)
    nin "What were you thinking?"
    if NinaProposition == 1:
        mc "You know what I was thinking."
        nin "We talked about that..."
    else:
        mc "I think that's pretty obvious, isn't it?"
        nin "No, it's not! It's never obvious with you."
    mc "Then I'll just say it. I-"
    show nina angry with Dissolve(0.2)
    nin "I have a boyfriend. Did you think about that?"
    mc "Not at that moment, no. All I could think about was how much I wanted to kiss you."
    show nina worried with Dissolve(0.2)
    nin "..."
    mc "Not that it would have made a difference. I don't care."
    show nina neutral with Dissolve(0.2)
    nin "Well, I do. I already feel horrible about lying to him."
    nin "If we do this..."
    nin "Damn it."
    mc "I'm sorry Nina, but I feel what I feel."
    nin "Why couldn't we have figured this out sooner?"
    tre "Nina? Where are you?"
    show nina surprised with Dissolve(0.2)
    nin "Shit! Trevor's here."
    jump HiTrevor

label DoNotKissNina:
    mc "{color=#b7b7b7}{i}No - she's dating Trevor and she will regret this.{/i}{/color}"
    nin "[MC]..."
    scene nina kiss 13 with Dissolve(2)
    hide window
    w ""
    mc "Yeah?"
    nin "What are you thinking about?"
    mc "You don't want to know."
    nin "I think I already do."
    mc "In that case..."
    scene nina kiss 9 with Dissolve(2)
    hide window
    w ""
    "You capture Nina's lips with your own. You know that you shouldn't - she said the cave was a mistake."
    "Nina's mouth opens halfway, giving you the signal you've been waiting for."
    scene nina kiss 10 with Dissolve(2)
    hide window
    w ""
    "Your tongue enters her mouth, and the kiss deepens."
    mc "{color=#b7b7b7}{i}I wanted to ignore these feelings, to not think about the cave, but I can't.{/i}{/color}"
    scene nina kiss 11 with Dissolve(2)
    hide window
    w ""
    nin "[MC]..."
    "Nina shudders as you kiss her neck, her face becomes flushed at the contact."
    scene nina kiss 12 with Dissolve(2)
    hide window
    w ""
    nin "You... you bastard."
    "Nina pushes you away and looks to the side. You can't tell if she's feeling lust or shame. If she's anything like you it is likely both."
    mc "Nina, I-"
    "Nina kisses you and pushes you onto the ground."
    scene nina kiss 14 with Dissolve(2)
    hide window
    w ""
    nin "You stupid... I should kick your butt."
    mc "We both-"
    scene nina kiss 15 with Dissolve(2)
    hide window
    w ""
    nin "Shut up."
    "You stop talking and Nina stares down at you. You both gaze into each other's eyes. Nina's frustration shows on her face. Any fantasy that things would be the same after the cave is now clearly just that."
    "Nina runs her hands over your face."
    scene nina kiss 16 with Dissolve(2)
    hide window
    w ""
    "She kisses you fiercly, almost as if she was in a frenzy."
    mc "{color=#b7b7b7}{i}This is even more intense than before.{/i}{/color}"
    "The kisses slow down to quicken soon after, yet, neither of you stop making out for long enough to take more than a simple breath."
    scene nina kiss 17 with Dissolve(2)
    hide window
    w ""
    "Nina grabs your head with a hunger she never knew she even had in her. She grinds herself on your erection, moaning as she does so."
    scene nina kiss 18 with Dissolve(2)
    hide window
    w ""
    "You run your hands down her back, resting them on her hips."
    "In response, Nina grinds her hips on you and you grab her ass, matching her rhythm with your own thrusts. You could fuck her right there, you can't think of anything else."
    tre "Nina? Where are you?"

    show orchard with Dissolve(2)
    "Nina backs off"
    mc "Damn it."
    show nina neutral with Dissolve(1)
    nin "Uh... over here!"
    "Nina stands up and quickly fixes her clothing."
    $ NinaLove += 2
    jump HiTrevor

label HiTrevor:
    scene orchard with Dissolve(2)
    "Trevor comes out from behind one of the apple trees. He waves as he comes up to the two of you."
    show trevor neutral with Dissolve(1)
    tre "There you are!"
    tre "Is this asshole bothering you, Nina?"
    "You don't think he's being serious, or so you hope."
    "Nina waves at him."
    show nina smiling at slightright with Dissolve(1)
    show trevor neutral at slightleft with easeinleft
    nin "No more than usual."
    tre "Did you give him the good news?"
    mc "Good news?"
    nin "Not yet. Trevor, can you get my bag? It's up in my room. Don't worry, dad shouldn't mind you going up there if I'm outside."
    "Trevor stops for a second and looks at you and Nina."
    tre "Alright. Be back in a second."
    hide trevor with easeoutleft
    show nina neutral at center with easeinright
    mc "So, what's the good news?"
    nin "Trevor and I decided to head out to the death swamps. I need to show you up after all. I thought that would make you happy."
    mc "We don't have death swamps. I mean, we've got a lake... there are cat tails."
    nin "Damn. Well, there goes my plans."
    show nina smiling with Dissolve(0.2)
    "Nina forces a smile."
    nin "The actual plan is to go over to your house. If you're going on a suicidal adventure then someone has to watch over your father."
    mc "Huh? If you were planning on that, why the whole fighting thing?"
    show nina neutral with Dissolve(0.2)
    nin "Because, damn it! I just needed to get some aggression out."
    mc "Thanks, Nina. that's kinda what I came to ask you about before I left. You're doing me a huge favor."
    mc "And I know you don't approve of what I'm doing."
    nin "I don't, but I have to live with it. Just promise me you won't die."
    mc "I promise."
    if NinaLeavingTalk == 0:
        show nina worried with Dissolve(0.2)
        nin "Don't make a girl a promise... if you..."
    "Nina sighs."
    nin "Thanks. I'll hold you to it."
    mc "Should we head back?"
    show nina neutral with Dissolve(0.2)
    nin "Yeah, but one last thing. I want you to know I'm sorry I've been avoiding you after the cave. I don't think I meant to, not really."
    mc "It's not like I was dropping by either."
    nin "You know, I care about Redd too."
    mc "Nina. We're good."
    nin "Are we?"
    mc "It's nice to know you'll be there. And dad gets a cute new nurse."
    nin "{b}Temporary{/b} cute new nurse. So you'd better come back."
    mc "If you look in my trunk you'll find a nurse outfit in just your size. Now, dad likes to-"
    "Nina playfully smacks you."
    nin "Dork."
    scene ninahouse exterior with Dissolve(2)
    "The pair of you walk back to her front door. Trevor is waiting with a pair of packed bags."
    show trevor neutral at slightleft with Dissolve(1)
    tre "That took longer than I thought. Did he complain much?"
    show nina neutral at slightright with Dissolve(1)
    nin "Nope. Not too much."
    mc "Anyway, thanks, you two. I have to run now, I'm meeting with Mia and [Nova] at the road out of town."
    tre "Well, good thing I'm packed."
    mc "Here's the key to the house, Nina."
    nin "Um, yeah, thanks."
    tre "I'll see you in a day or two."
    mc "Yeah, take care of her, Trevor."
    nin "He was talking to me."
    mc "What?"
    tre "What? I'm going with you. I thought you knew."
    nin "We hadn't gotten to that part yet."
    mc "Because you knew I'd say-"
    tre "She asked me to back you up. I agreed. You can throw that kindness in her face or you can deal with it and get going. We don't want to burn daylight here."
    mc "But..."
    "You sigh."
    mc "Alright."
    nin "Thanks, honey."
    "Nina hugs Trevor"
    if NinaTrevor > 1:
        "He gives her a kiss and she wraps her arms around him tightly."
        nin "Be safe, OK?"
    else:
        "She wraps her arms around him tightly."
        nin "Be safe, OK?"
    nin "And that goes for you too."
    stop music fadeout 1
    "You and Trevor finish your goodbyes and walk to the entrance of the village in silence."
    scene black with Dissolve(2)
    play sound walkgrass
    scene village destroyed with Dissolve(2)
    mc "You know I don't need the help, right?"
    tre "You know you're fucking crazy, right?"
    mc "Whatever. There are the girls."
    "You can see Mia and [Nova] waiting for you."
    play music afternoon fadein 1
    show mia neutral adv at slightleft with Dissolve(1)
    show nova neutral at slightright with Dissolve(1)
    nov "Trevor?"
    mc "Long story."
    show trevor neutral at center with Dissolve(1)
    tre "Not that long. Nina asked."
    mc "So short story."
    show mia smiling adv with Dissolve(0.2)
    mia "Great! The more the... well, merrier seems like a bad word to use right now."
    tre "Hey, I'm just here to make sure you don't get killed so my girlfriend doesn't kill me."
    mia "Aww! That's sweet."
    show nova smirk with Dissolve(0.2)
    nov "Your idea of sweet is different than most humans, Mia."
    show mia neutral adv with Dissolve(0.2)
    mia "What?"
    mc "Hey, what's up with the new clothes, Mia?"
    mia "They're just more confortable for a trip like this. Do you think I look weird?"
    mc "Not at all, you look badass!"
    mia "He-he! Thanks!"
    mc "Well, this is going to be an interesting trip if nothing else."
    nov "So, you ready to go?"
    "You look over at your friends."
    if TrevorFriend < 2:
        "And Trevor."
    stop music fadeout 2
    mc "{color=#b7b7b7}{i}Can I really do this? Having Trevor around is going to help, but Mia and [Nova]? They can't fight. Hell, I can't fight.{/i}{/color}"
    "Suddenly the reality of where you are going hits you. You're filled with fear, not just for yourself, but for everyone else."
    "You can't speak. You can't move. You feel panic setting in."

menu:
    "Just man the fuck up and do it, you little bitch!":
        $ HeroAlignment = 0
        $ HeroAlignment -= 1
        jump ForestDay8
    "You've got this! You can do it! [gr]\[Hero\]":

        $ HeroAlignment = 0
        $ HeroAlignment += 1
        jump ForestDay8
    "If you go, you might die. If you stay, it won't matter if you do.":

        $ HeroAlignment = 0
        jump ForestDay8

label ForestDay8:
    "Words in a voice not your own echo in your head and snap you out of your fear."
    mc "{color=#b7b7b7}{i}That's right. I made the choice. We're doing this!{/i}{/color}"
    mc "Yeah, good to go. If anyone wants out... now's the time."
    "Your three companions remain silent."
    mc "OK, then."
    play music strangeplace fadein 2
    scene forest path with Dissolve(2)
    nvl clear
    n "Your party heads down the road to the mountain. [Nova] and Mia whisper and giggle a bit behind you and Trevor."
    n "The road out to the mountain is quiet, no monsters, no real animals other than the occasional squirrel. Trevor takes the lead."
    "After a while."
    nvl clear
    mc "I think you can relax a little bit, Trevor, you're looking kind of paranoid."
    show trevor annoyed with Dissolve(1)
    tre "How about you trust the guy who knows what he's doing?"
    mc "You didn't have to come along, you know? And just because you did, it doesn't mean you're in charge."
    tre "Yeah... bullshit on that one."
    mc "You're the one who-"
    tre "No. Nina's the one who."
    show trevor angry with Dissolve(0.2)
    tre "You want to come out here and get your ass eaten by a monster? None of my fucking business."
    tre "But for some reason my girlfriend actually cares if you live or die."
    tre "And she'd be pretty sad if you got digested by a man-eating plant, or sucked into an antlion pit."
    tre "I'm trying to keep you safe, which would be hard e-fucking-nough, but I also have to watch out for your whatever she is, and Mia."
    tre "So be a good boy and fall in line."
    mc "Hey, this isn't the militia! You can't just order me around."
    show trevor neutral with Dissolve(0.2)
    tre "You're not up for this. Just follow my lead."
    mc "Like you know everything about these woods."
    tre "Not everything. But I know more than you."
    mc "Fine. Which way to the mountain then?"
    tre "..."
    mc "I knew it. You were going the wrong way. I used to camp out here, before the monsters got really bad. I know these woods."
    tre "And I know how to actually fight."
    mc "So if I need something's head cut off, I'll call you."
    tre "I don't even know why I agreed to this."
    show trevor neutral at slightleft with easeinright
    show nova neutral at slightright with easeinright
    nov "Are you two done swinging your dicks around? I thought I heard something."
    "Trevor raises his hand to quiet everyone."
    "You hear some voices coming down the path in the forest."
    tre "Hide!"
    hide trevor with easeoutleft
    hide nova with easeoutright
    mia "Maybe they're-"
    tre "Mia! Please... hide."
    hide all with easeoutright
    "Your party hides behind the trees near the path."
    play music nikki1 fadein 1
    show nikki smirk at center with Dissolve(1)
    show zack neutral at offscreenright
    show zumma neutral at offscreenleft
    show zack neutral at farright with easeinright
    show zumma neutral at farleft with easeinleft
    zum "You led us on quite a chase, Nikki."
    nik "Fucking hell, Zumma? How the hell did you find me?"
    zac "That's what we do, Nikki."
    nik "Well, shit Zack, how was I supposed to know you'd be competent for once?"
    "Nikki tries to run but Zack cuts her off."
    zac "Relax, Nikki, no need to run. We're just here at your father's request."
    nik "Fuck. What does that asshole want now?"
    zac "He just wants you to go back to the camp."
    nik "Fuck that. The answer is no. See you later."
    "Nikki turns to leave and Zack grabs her arm."
    zac "Now, that's probably not smart. Hesaid he'd even forgive you for everything if you came back willingly. And with what you stole? That's a crazy good deal."
    nik "And if I don't go \"willingly\"?"
    zum "Then we'll have to use force. Which is a lot more fun for me. So pick that one."
    zac "But I just want to get this over with. So how about you just let us tie your hands up and get going?"
    nik "Why don't I pay you 3000 Gold each, instead?"
    zac "Damn, that' a lot of money!"
    zum "Yeah, but no way. If we don't bring you back it's our hides that get tanned."
    zac "You remember what happened to the last assholes who failed to bring you back? No bit of shiny is worth that. At all."
    scene FT2 with Dissolve(2)
    hide window
    w ""
    nik "Hum, OK, better idea: How about I suck you both off?"
    zac "WHAT?!"
    nik "That's worth way more than the gold. How many times do you get a chance to get sucked off by the boss' hot... nubile... daughter."
    zac "Very tempting. What do you think, Zumma?"
    zum "Fuck, man! Fucking Nikki... It's almost like fucking a princess, right? It's times like this that make me love this job!"
    zac "Yeah, I think it's worth it."
    nik "Good, it's a deal then, after we finish you let me go. Tell father you never even saw me. And you never will, either."
    zac "Just get down on your knees."
    "You and your friends watch the scene with wide eyes."
    scene nikkibattle1 with Dissolve(2)
    hide window
    w ""
    mc "We have to help her!"
    nov "And how do we do that, exactly?"
    tre "She seems fine to me... and how do we help, exactly? You going to help her with the head, [MC]?"
    mc "It just doesn't seem right."
    tre "It was her idea! "
    nov "He's got a point. I'm pretty sure she knows what she's doing."
    mc "I can't believe you two. Mia? What do you think?"
    mia "Um... how about we stay and watch?"
    nov "Kinky."
    mia "I didn't mean like that! Oh, you're bad, [Nova]."
    mia "I mean, if it gets out of hand, then maybe we should intervene."
    tre "And don't you care about saving your dad? We can't risk the mission for a thief."
menu:
    "Intervene \[Negotiated Bandits\]":

        $ renpy.end_replay()
        scene forest path with Dissolve(1)
        mc "Be right back!"
        show zack neutral at offscreenright
        show zumma neutral at offscreenleft
        show zack neutral at farright with Dissolve(0.2)
        show zumma neutral at left with Dissolve(0.2)
        show nikki smirk behind zack with Dissolve(0.2)
        "You walk up to the pair of bandits with a friendly smile."
        mc "I'm sorry to interrupt, but I couldn't avoid hearing what's happening here and..."
        "Trevor and [Nova] look at each other and back at you."
        tre "What the hell is that idiot doing?"
        nov "I have no idea!"
        zum "The fuck? Go away kid! We're in the middle of something here."
        mc "Sorry, sorry! I'm here to help you though, I think you're making a mistake."
        mc "{color=#b7b7b7}{i}How the hell am I talking so smoothly? It's like it's coming out of nowhere.{/i}{/color}"
        zac "Fuck off! Get going and be lucky I'm in a good mood. But leave that gold pendant. It looks like it's worth a lot."
        zum "Actually, hold on. I'm curious about what he's going to say. This kid must have some balls coming here."
        mc "Well, it'll surely feel good to fuck her, right? But man, fucking the boss's daughter... phew, that's bold, but far too risky!"
        zac "Huh? Do you know our boss? Who are you?"
        mc "All I know is that he will kill you if he finds out about this betrayal. Are you sure this is worth dying for?"
        zum "He will never know about this deal, so..."
        mc "Are you sure, though? Once you do this she'll be holding this against you for the rest of your lives. You'll have to help her forever, otherwise she can just tell her father about what you did."
        mc "And now that you even thought about betraying him, you can't even have her going back there. You're in a tough situation here."
        zac "We'll just say she's lying!"
        nik "Good luck with that! Dad is the only one who knows whenever I lie; this means that he also knows when I'm telling the truth."
        zum "OK, then we'll just kill you both after we're done and tell him we didn't found her."
        mc "That's even worse. Keeping a secret like this is hard, so then what? You'll kill your friend too? Too many loose ends..."
        zum "What do you suggest then, genius?"
        mc "Let her buy only a few days to run ahead of you. Go to the capital for a few days and spend the money with some nice ladies there, then you can start looking for her again."
        mc "Even if your boss finds out about this it's probably not that bad, specially if you manage to catch her anyway, and you do trust yourselves to catch her again, right?"
        zac "That's actually a good idea, I could use a few days off."
        zac "We'll definitly go to the capital after fucking her, stealing her gold and killing you."
        zum "Did you think her father didn't know what she gets up to every time a guard can't find her? After the third or so set of hunters he executed for getting seduced by her, he finally understood."
        show nikki worried behind zack with Dissolve(0.2)
        nik "What? I don't get it."
        zac "We were allowed to use force to bring you home, darling. And I quote \"So long as you two idiots don't get her pregnant, I don't care anymore\"."
        nik "You... you can't be serious!"
        zum "This is what happens when you piss a man off."
        nik "Gods DAMN IT!"
        mc "Well... No other way then."
        $ NegotiatedBandits = 1
        jump FightForNikki
    "Stay Hidden":

        mc "Goddamn it."
        mia "Shh! They'll hear us."
        nik "Come on. Pants off."
        scene FT3 with Dissolve(2)
        hide window
        w ""
        nik "Ugh. Do you guys even understand what a bath is?"
        zac "Yeah, but we've been tracking a little runaway for days. There's not a lot of time to bathe, is there?"
        zum "Come on! Less yapping, more sucking!"
        zac "You get undressed too, Nikki. I've wanted to see those tits for years now."
        scene FT4 with Dissolve(2)
        hide window
        w ""
        nik "Why not? If it helps you get off."
        "Nikki lowers the straps of her shirt and pulls out her tits."
        zac "Oh yeah! The boss' little girl on her knees with her tits out for me... I'm going to love this!"
        scene FT5 with Dissolve(2)
        hide window
        w ""
        zac "Come on, put your mouth on it already!"
        "Zack grabs Nikki by the back and guides her to his cock. She opens her mouth and starts to loudly suck on him."
        zac "Aaah, oh my God! This feels so great! Having Nikki's mouth on my cock, so eagerly sucking it, it feels like heaven!"
        scene nikkibattle2 with Dissolve(2)
        hide window
        w ""
        mia "Oh, she's really..."
        mc "Shh."
        zum "Hey, Nikki, raise your ass for me, baby."
        scene FT6 with Dissolve(2)
        hide window
        w ""
        "Zumma stands Nikki up and bends her over. He runs his hand over her panties and smiles."
        zum "Man. Your perfect little ass cheeks... and a tight little pussy. You look good enough to fuck."
        "Zumma undresses and rubs his cock over Nikki's panties."
        nik "Whoa, whoa, whoa! That was not part of the agreement. No pussy. Just get over here and I'll suck you."
        zum "How about you just let me fuck you in the ass?"
        nik "No way!That thing's way too big!"
        zum "Don't worry, I always carry some lube with me."
        nik "Makes sense. I always figured that you were the top in this relationship."
        scene FT7 with Dissolve(2)
        hide window
        w ""
        zac "Alright, back to sucking!"
        "Zach pulls Nikki's head to his cock and gags her as his cock hits the back of her throat. Zumma slides his hand and cock under Nikki's underwear and starts to slide his cock up and down her ass cheeks."
        nik "Hhhmf"
        zum "Oh, man, I wanna fuck this ass so hard you won't sit for a week!"
        zac "Ah, yeah. You are too good at this, you little bitch. Suck it!"
        scene FT8 with Dissolve(2)
        hide window
        w ""
        "Zack tenses and keeps his grip on the back of Nikki's head. You can tell he's cumming."
        zac "CUMMING! Fuck, I can't stop shooting my load inside her mouth!"
        mia "Oh, right in her mouth. That's so..."
        nov "Well, she's taking it like a champ."
        scene FT9 with Dissolve(2)
        hide window
        w ""
        zac "Drink it all, Nikki, I know you like it!"
        nov "Guy seriously needs some help with his dirty talk skills."
        mia "You think?"
        scene FT10 with Dissolve(2)
        hide window
        w ""
        tre "Shit, I think he's really going for her ass."
        nov "Ouch is what I have to say to that."
        mia "It's so big... do you think it will fit?"
        mc "Not that big, right?"
        nov "Well, I've seen bigger."
        "[Nova] blinks at you."
        mia "Oooh, really?"
        scene FT11 with Dissolve(2)
        hide window
        w ""
        zac "Come on! The least you could do is swallow."
        nik "You're lucky I didn't bite you. I'll spit and you'll deal with it. This is a business transaction, nothing more."
        zum "Get ready, Nikki. This is gonna be a tight fit."
        scene FT12 with Dissolve(2)
        hide window
        w ""
        zum "Come on, bend over for me, Nikki, it'll be easier this way."
        nik "Hey, I haven't said yes yet!"
        zum "You didn't say no either. Anyway, I need more than a sloppy blowjob to cum."
        "Zumma slips the head of his cock into Nikki's ass."
        scene FT13 with Dissolve(2)
        hide window
        w ""
        zum "Better than I even thought it would be."
        nov "It's really going in!"
        tre "Shh... quiet!"
        mia "This feels so wrong to watch..."
        "Even though Mia says this she makes no move to avert her gaze."
        scene FT14 with Dissolve(2)
        hide window
        w ""
        "Zumma grabs a handful of Nikki's hair as he roughly fucks her on the ground. He's not making it all the way in just yet, but each of his thrusts moves a little closer to the goal."
        nik "OW! Not that rough, you son of a bitch!"
        zum "What, this underclass dick not up to your standards? Too bad!"
        scene FT15 with Dissolve(2)
        hide window
        w ""
        zum "You like being dominated. Treated like an animal. Fucked in the ass like a dog."
        "Nikki groans in response."
        scene nikkibattle2 with Dissolve(2)
        "You hear heavy breathing next to you. You look to the side to see Mia, unable to take her eyes away from the show in front of her."
        mia "Oh, my..."
        "Her face is flushed and you see her rub her thighs together."
        mc "{color=#b7b7b7}{i}Is she getting turned on?{/i}{/color}"
        scene FT16 with Dissolve(2)
        hide window
        w ""
        "Zumma is close to his climax and you can see it in his face. His thrusts are harder now and Nikki calls out with each one."
        nov "Is he going to cum inside her?"
        scene FT17 with Dissolve(2)
        hide window
        w ""
        zum "Stay right there. I'm going to cum inside of you. You're getting your ass filled."
        scene FT18 with Dissolve(2)
        hide window
        w ""
        "Zumma speeds up. Each stroke of his now bottoming out inside of Nikki's streched ass."
        zum "Aaah, all the way in! I'm cumming, Nikki! Get ready for my cum! AAAH!"
        scene FT19 with Dissolve(2)
        hide window
        w ""
        zum "Cumming in the boss' stuck up daughter. In her ass even! This is the fucking life."
        scene FT20 with Dissolve(2)
        hide window
        w ""
        "You can see drips of white liquid coming out her ass and dripping over her pussy."
        zac "Damn, man. If I knew this was an option, I would have picked it. But now I need some time to recover."
        zum "I'm still cumming... you want it all over? I want to paint you with it!"
        nik "Fucking gross. No way. You got what you wanted."
        zum "Haha! You'll never forget Zumma and his mighty tool of destruction."
        scene forest path with Dissolve(2)
        "Nikki wipes herself off and doesn't respond. She puts her clothes back on. If she seemed disgusted before, she seems perfectly ok with the situation now."
        show nikki smirk with Dissolve(1)
        nik "Well, that was more of a mess than I thought it would be."
        $ persistent.nikki_bandits = True
        $ renpy.end_replay()
        show zack neutral at farleft with easeinleft
        show zumma neutral at farright with easeinright
        zac "That was a lot of fun. The trip back home is going to be amazing."
        nik "Fuck that! A deal is a deal, you got your part, now shoo!"
        zac "Nah, We're going to keep you and fuck you for a few days before bringing you back to the camp. What do you say, Zumma?"
        nik "This is what I love about guys like you, so fucking predictable. No, that's not how it's going down. You're both my bitches now."
        zum "Huh? What do you mean?"
        nik "You take me back home I'll tell my father what you two did."
        zac "So you'll say we raped you?"
        nik "I don't even need to go that far. I'll just be straight with him. Dad is the only one who knows whenever I lie, but this means that he also knows when I'm telling the truth."
        zum "Fuck! She's right! We're fucked, man!"
        zac "Oh God! Her father will KILL US!"
        zac "I don't wanna die!"
        "Zack and Zumma look at each other. Then they start to laugh."
        zac "HAHA! Oh man! That's rich."
        show nikki worried with Dissolve(0.2)
        nik "I'm serious!"
        zac "I know! That's what makes it so funny."
        zum "She really has no idea."
        nik "Idea of what?"
        zac "Did you think your father didn't know what you get up to every time a guard can't find you?"
        zum "After the third or so set of hunters he executed for getting seduced by you, he finally understood."
        nik "I don't get it."
        zac "We were allowed to use force to bring you home. And I quote \"So long as you two idiots don't get her pregnant, I don't care anymore\"."
        nik "You... you can't be serious."
        zum "This is what happens when you piss a man off."
        nik "Look... I still have money."
        zac "I know you do, but we're still going to have to bring you home."
        nik "Gods DAMN IT!"
        "You and the crew are still watching the scene unfold."
        scene forest path with Dissolve(1)
        show nova worried at slightleft with Dissolve(1)
        show mia ashamed adv at slightright with Dissolve(1)
        nov "Well, that sucks for her."
        mia "After she let him fuck her ass and everything. That's just not right."
        show trevor annoyed with Dissolve(1)
        tre "Yeah, {i}that's{/i} the fucked up part. Not her dad basically saying she can be a fuck toy."
        mc "Agree with Trevor. We should help her."
        show trevor angry with Dissolve(1)
        tre "I didn't say that. I'm just saying her dad's kind of shit. Whoever he is."
        mc "We have to do something."
        show nova neutral with Dissolve(0.2)
        nov "Yeah, we really do."
        show trevor annoyed with Dissolve(0.2)
        tre "Are you forgetting about your father here?"
        mc "No, but dad would help her. And I won't do different."
        tre "This isn't a baby slime. These guys are true killers."
        mc "Why do people keep reminding me that clearly lethal things are lethal?"
        mc "But we've got this."
        tre "And what's the plan, great leader?"
        mc "Watch the girls, Trevor!"
        tre "What? No. Wait! No!"
        show nova worried with Dissolve(0.2)
        nov "[MC]!"
        scene forest path with Dissolve(1)
        show zack neutral at offscreenright
        show zack neutral at farright with Dissolve(0.2)
        show zumma neutral at left with Dissolve(0.2)
        show nikki worried behind zack with Dissolve(0.2)
        $ NegotiatedBandits = 0
        jump FightForNikki

label FightForNikki:
    play sound knife
    "You draw your knife and walk out in front of Zumma and Zack. Nikki looks up at you in confusion."
    show zack neutral at right with easeinright
    show zumma neutral at farleft with easeinleft
    hide nikki with Dissolve(0.2)
    play music action fadein 1
    zac "What the fuck? I don't know who the hell you think you are, kid, but I think you walked into a giant pile of shit you're not ready for."
    scene forest path with Dissolve(1)
    show trevor annoyed with Dissolve(1)
    tre "Fucking hell! Stay here."
    hide trevor with easeoutleft
    "Trevor gets up and runs towards you."
    show nova worried with Dissolve(1)
    nov "Mia, stay here."
    hide nova with easeoutleft
    "Nova gets up and runs after Trevor."
    show mia ashamed adv with Dissolve(1)
    mia "Oh my..."
    scene forest path with Dissolve(1)
    show trevor neutral with easeinright
    tre "[MC]! There you are. What have I told you about running away from the asylum?"
    show trevor at slightright with easeinleft
    show zumma neutral at slightleft with easeinleft
    show zack neutral at offscreenleft
    show zack neutral at farleft with easeinleft
    zum "Asylum?"
    show trevor neutral behind nova at slightright with Dissolve(0.2)
    show nova neutral at offscreenright
    show nova neutral at farright with easeinright
    nov "Oh there you two are! Trevor! What did I tell you about watching him?"
    show nova neutral behind trevor at farright with Dissolve(0.2)
    tre "What can I say? He's an idiot savant when it comes to getting into places where he isn't needed."
    show zumma neutral behind zack with Dissolve(0.2)
    zac "What are you two talking about?"
    mc "They're talking crap is what. I'm here to save the girl."
    nov "Hero complex. He's delusional as you can see."
    "Nova grabs you by the arm."
    zac "Actually... that's a nice sword over there. Way too nice for an asylum guard."
    zum "And you're pretty young to be a nurse."
    zac "Are you buying this, Nikki?"
    "Nikki is nowhere to be found."
    zac "FUCK!"
    zac "You kids lost us our bounty."
    show nova worried with Dissolve(0.2)
    nov "So sorry about that. Guess we'll have to go."
    show nova worried behind trevor with Dissolve(0.2)
    tre "We're not looking for a fight. If you want the redhead, I think she went that way."
    zac "It'll take us days, if ever, to find her again! But..."
    zac "Hey, Zumma, doesn't this one look like the boss' type?"
    show zack neutral behind zumma with Dissolve(0.2)
    zum "You know what? You're right. Good call."
    show zumma neutral behind zack with Dissolve(0.2)
    zac "How about this: you lost us a girl, so you hand the brunette over and we'll call it even. We won't even kick the shit out of you because of it."
    nov "Fuck off!"
    mc "Honestly, I always expected I'd have to pay someone to take her... but nah, I guess she grew on me, so I'll have to say no."
    zac "We'll take her anyway. We'll have some fun with you on the way back, girl. And your pussy isn't off limits."
    nov "Like hell you will!"
    jump Day8BanditFight

label Day8BanditFight:
    "Zack and Zumma draw their swords and start coming after you. You freeze and watch in terror as Zack lowers his weapon towards you."
    stop music fadeout 1
    scene whitescreen with Dissolve(3)
    "There's nothing you can do now."
    mc "{color=#b7b7b7}{i}This was a... mistake.{/i}{/color}"
    play sound hit
    scene nikkibattle3 with Dissolve(2)
    play music afternoon fadein 2
    "Mia sneaks in and hits their head with a big piece of wood. Somehow you are still alive."
    mia "Oh my God... is everyone OK? Are they dead?"
    nov "Holy shit, Mia! You totally saved us!"
    tre "They'll be fine, let's get out of here before they wake up."
    scene forest path with Dissolve(2)
    mc "Sorry guys. I just... I had to help her."
    show nova neutral with Dissolve(1)
    nov "I'm just shocked we came out OK. And that it was Mia after all who totally destroyed those guys."
    show mia neutral adv at right with Dissolve(1)
    mia "They weren't being too nice, so... No way I'd let them hurt you. I just hope I didn't give them a concussion."
    show trevor annoyed at left with Dissolve(1)
    tre "You're all insane. I still can't believe [MC] went for it. Well, you totally froze after acting all tough on them, but still. You always seemed like a weenie."
    mc "I guess I used to be that way. But I can't afford to be anymore. Anyway, thanks for your help, Trevor."
    show trevor neutral with Dissolve(1)
    tre "It would have been my first sword fight. Real sword fight, I mean. I was scared shitless, but there's no way I'd let them kill you without doing something. That's my job, after all."
    tre "But, [MC], you pull something like that again, and I'll kill you myself."
    nov "Okay! We should move."
    mc "Yeah, let's go."
    stop music fadeout 1
    jump Day8Maze

label Day8Maze:
    scene black with Dissolve(2)
    play music strangeplace fadein 2
    "After a while..."
    scene deep forest sunset with Dissolve(2)
    "You and Trevor take point again, as you follow the path."
    show trevor neutral with Dissolve(1)
    tre "We've been here before."
    mc "We can't have been here before. We haven't made a turn. Plus, my compass is showing we're still moving west."
    tre "I'm telling you, this rock is the same rock we passed a while back."
    mc "And I'm telling you it can't be."
    show trevor annoyed with Dissolve(0.2)
    tre "Well, you're the expert."
    mc "I pretty much am."
    tre "So let's just keep walking in circles, then."
    tre "I've always dreamed of dying of starvation in the middle of the forest."
    mc "What's your problem?"
    show trevor angry with Dissolve(0.2)
    tre "My problem is I shouldn't even be out here."
    if NegotiatedBandits == 1:
        tre "And you're fucking acting like you're immortal."
    else:
        tre "Or getting into fights with bandits."
    show trevor annoyed with Dissolve(0.2)
    tre "I promised Nina I'd look after you, but I can't do that if you're actively trying to get yourself killed."
    mc "So go home then. Just tell Nina I was an asshole and you left. She'll buy that."
    show trevor neutral with Dissolve(0.2)
    tre "Yeah, that might work"
    if TrevorFriend > 1:
        tre "But despite all your effort, I don't want to see you dead either, OK?"
    else:
        show trevor annoyed with Dissolve(0.2)
        tre "No way am I leaving a jackass like you out here with [Nova] and Mia."
        tre "You'll get them killed too."
    tre "And I don't like owing you, anyway."
    mc "You don't owe me a thing, Trevor."
    show trevor neutral with Dissolve(0.2)
    tre "You protected Nina during the storm. Fought off a goblin for her, for fuck's sake. Still can't believe that."
    tre "But she swears it happened. I guess that's why she's been a little jumpy around me since she got back."
    mc "You don't have to pay me back for that, I would have done it anyway."
    show trevor annoyed with Dissolve(0.2)
    tre "Yes, I do. Don't argue. My father's an asshole, but he always said not to owe anybody, ever."
    mc "No offense, Trevor, but I didn't do it for you."
    show trevor neutral with Dissolve(0.2)
    tre "But you still did it, so I owe you. I don't much like it, but that's how it is."
    mc "OK, then."
    scene deep forest sunset with Dissolve(2)
    "You keep walking and see the same rock from a few minutes ago in front of you."
    mc "No way!"
    tre "See?! I told you."
    mc "This makes no sense! It's just got to be a similar rock."
    tre "It's not similar, it's the same fucking one."
    mc "It can't be."
    show mia smiling adv at right with Dissolve(1)
    show nova neutral at left with Dissolve(1)
    "You walk over to [Nova] and Mia."
    mia "OH! Hi [MC]! Are we almost there?"
    mc "I'm not sure."
    mc "Let me ask you something. Does that rock look familiar?"
    "You point to the rock and [Nova] and Mia both look at it."
    nov "It does, yeah."
    show mia neutral adv with Dissolve(0.2)
    mia "Um... it looks identical. Even the tree is the same."
    mc "Are you sure?"
    "Mia nods."
    mia "I remember because of the Hyber Flower growing to the side of it. I don't see them at the lake, and they're really pretty."
    mc "Shit."
    nov "Don't tell me you've been walking us in circles for the last couple of hours."
    "Trevor walks up."
    show trevor neutral at center with Dissolve(0.2)
    tre "Are you telling them you got us lost?"
    mc "We're not lost! I've been following the compass and it says that that direction is west."
    "You show the compass to [Nova] and Mia."
    nov "It says that THIS way is west."
    "Nova points in the direction you're currently facing."
    mc "That's impossible."
    "She's right. According to your compass, the direction you are currently facing is the way you should be going."
    mc "Hold on..."
    "You turn and everywhere you turn the compass moves for a moment, but indicates that west is your current heading."
    mc "FUCK! The damn thing is broken!"
    show trevor annoyed with Dissolve(0.2)
    tre "Now you notice."
    mc "It was working before. I know it was."
    mia "Maybe there's some lodestones nearby that are messing with it?"
    mc "Maybe."
    tre "Well, if that path keeps us going in circles what about this one?"
    mc "That is the only... wait a minute. What the hell?!"
    tre "You didn't notice it before?"
    nov "Yeah, I think it's always been there."
    mc "No, I'm sure it..."
    "You feel something digging at your brain, your head begins to throb. Then, the pain subsides."
    "How could you forget the other path? It's been there the whole time."
    mia "Are you feeling OK?"
    mc "Yeah, sorry. So, should we try that one?"
    "Everyone else nods."
    mc "OK, let's get back on track."
    scene blackout with Dissolve(2)
    "You lead the party into the opening in the forest."
    mc "Looks like the compass reset itself. Now we're good."
    tre "Great. Hopefully we get out of here before nightfall."
    scene deep forest night with Dissolve(2)
    "After a while."
    show nova annoyed with Dissolve(1)
    nov "How big is this damn forest?"
    "Nova sits on a rock to catch her breath."
    show nova annoyed at right with easeinleft
    show mia neutral adv at slightleft with Dissolve(1)
    mia "Are you tired?"
    nov "You're not?"
    mia "I've been snacking on a pie I made recently. It keeps my spirits up pretty well."
    show nova neutral with Dissolve(0.2)
    nov "Oooh, sounds good!"
    tre "It's too early to take a break, come on."
    show nova annoyed with Dissolve(0.2)
    nov "Fine, asshole."
    "You all continue through the forest."
    scene deep forest night with Dissolve(2)
    $ TrevorTalk = 0
    $ NovaTalk = 0
    $ MiaTalk = 0
    $ ForestTalk = 0

menu ForestTalkMenu:
    "Talk to Trevor" if TrevorTalk == 0:
        jump ForestTrevorTalk

    "Talk to [Nova]" if NovaTalk == 0:
        jump ForestNovaTalk

    "Talk to Mia" if MiaTalk == 0:
        jump ForestMiaTalk

    "Keep going" if ForestTalk == 3:
        jump Clearing

label ForestTrevorTalk:
    "You walk up to check on Trevor."
    show trevor annoyed with Dissolve(1)
    tre "This forest is bothering the hell out of me."
    mc "Yeah... the creep factor is definitely higher now."
    tre "Aaron doens't even come this far in, and that kid's a damn hunting prodigy."
    mc "And he lets everyone know it! But who's going to come out here without a good reason?"
    mc "If it wasn't for my father's situation, I don't think I'd consider it."
    show trevor neutral with Dissolve(0.2)
    tre "Yeah. My father says that we didn't always have this many monsters. Brooke said she used to come out here to play as a little girl."
    mc "I think my dad said something like that too. But that changed what? Before the bandits' attack?"
    tre "Yeah, something like that."
    mc "Well, no monsters so far."
    tre "Don't jinx it."
    mc "Fair point."
    tre "It's getting too dark, I hope we find a clearing soon."
    mc "It'd be nice."
    "You leave Trevor alone for a bit."
    hide trevor with Dissolve(1)
    $ TrevorTalk = 1
    $ ForestTalk += 1
    jump ForestTalkMenu

label ForestNovaTalk:
    "As you walk through the forest, [Nova] calls you over."
    show nova neutral with Dissolve(1)
    nov "Hey!"
    mc "Hey."
    nov "How much longer do you think?"
    mc "I wish I knew. I can't even see the mountain, the forest is too thick."
    show nova worried with Dissolve(0.2)
    nov "I know, you'd think it'd be easy to get to a mountain. It didn't even look that far away."
    mc "First rule of camping: plan for it to take longer than you think to get where you're going."
    show nova smirk with Dissolve(0.2)
    nov "You just made that rule up right now, didn't you?"
    mc "..."
    nov "I knew it!"
    show nova neutral with Dissolve(0.2)
    nov "This forest is really creepy though. I've got goosebumps... I feel like someone's watching us."
    if TrevorTalk == 1 and MiaTalk == 1:
        mc "You're not alone in that, seems like everyone agrees."
    elif TrevorTalk == 1:
        mc "Yeah, Trevor said the same thing. I kind of agree."
    elif MiaTalk == 1:
        mc "Mia was kinda weirded out too."
    mc "We're just not used to it, I guess."
    nov "I just want out of here, fast."
    mc "Ditto. We'll be through soon enough."
    nov "By the way."
    show nova smirk 2 with Dissolve(0.2)
    if MiaTalk == 1:
        nov "I saw you talking to Mia."
        mc "And?"
        nov "Did you make your move?"
        mc "What? We're in the middle of the forest, and pretty much lost."
        nov "And?"
        if MCMiaLike == 1:
            mc "And what?"
            nov "Come on! You like her!"
            mc "Again, we're in the middle of the forest."
            nov "Don't look at it like an obstacle. It's an opportunity."
            nov "And come on, I don't think she would have come on this trip if Toby needed help."
            mc "Yeah..."
        else:
            nov "You know she... Damn, forget I said anything."
            mc "Forget what?"
            nov "Exactly."
    else:
        nov "You might want to talk to Mia. You've barely spent any time with her."
        mc "I've been navigating."
        nov "I... Goddess, you are so dense."
        mc "What?"
        nov "You think she would have come out here, if say, Toby needed help?"
        mc "Probably?"
        nov "Yup. Dense. Just go talk to her."
    show nova neutral with Dissolve(0.2)
    nov "It's getting dark. I hope we find a place to camp soon. Heck, a little lake would be great... I could take a bath and stuff."
    mc "I doubt we'll find one around here, but who knows."
    mc "I'm going on ahead for a minute."
    nov "OK."
    hide nova with Dissolve(1)
    $ NovaTalk = 1
    $ ForestTalk += 1
    jump ForestTalkMenu

label ForestMiaTalk:
    "You go over to Mia. She smiles when she sees you."
    show mia smiling adv with Dissolve(1)
    mia "Hi! Wow, this forest is pretty crazy, isn't it?"
    mc "Just a bit! I'm hoping we're out of it soon."
    show mia neutral adv with Dissolve(0.2)
    mia "It's definitely a little creepy right now, but... I've seen so many new plants!"
    mia "It's a shame that so many monsters live out here. Elder Silas could make SO many great medicines if we could harvest these things."
    mia "And it wouldn't even cost much."
    mc "So why not grab some?"
    mia "I have been. Look!"
    "Mia opens her pouch and you see a variety of different herbs."
    mia "I even found some black berries! The elder will be so thrilled!"
    show mia smiling adv with Dissolve(0.2)
    mc "You just take everything in stride, huh?"
    mia "I guess. Is that weird?"
    mc "No. Well, maybe a little, but I kind of like it."
    mia "I'll tell you a secret."
    "Mia blushes and whispers to you."
    show mia neutral adv with Dissolve(1)
    mia "I'm really kind of scared..."
    mc "We all are a little bit, I think."
    "Mia nods."
    mia "Don't tell [Nova]. She's worried too, but she doesn't want me to worry so she puts on a front."
    mc "So you're doing the same?"
    show mia smiling adv with Dissolve(0.2)
    mia "I never thought of it that way."
    mc "Looks like you each make each other braver."
    mia "She's a great friend!"
    mc "You guys really hit it off after the party, huh?"
    show mia neutral adv with Dissolve(0.2)
    mia "She's a lot of fun, and she taught me how to drink and stuff. She's kind of like my evil little sister."
    mc "I didn't know you had a little sister."
    mia "I don't. But if I did I'd hope she was like [Nova]."
    mc "Well, I'm glad you guys found each other. And I guess that means I'll see you around the house more!"
    mia "I'm still looking after Mr. Redd, so..."
    mc "After that, even."
    "Mia nods happily."
    mia "Of course! I want to keep seeing more of you."
    show mia smiling adv with Dissolve(0.2)
    mia "I mean, [Nova] and you... both."
    mc "I get you. I'd like that too."
    mia "Do you think we're going to stop soon? It's starting to get dark."
    mc "I hope so. But we need to find a camp site, and this forest is really thick."
    mia "Hmm. When we do stop I hope we can see the moon. I love looking at the stars; they're so romantic."
    mc "I'll be happy with enough space for a fire pit and our tent."
    "Mia nods."
    mia "Um... I'll be fine back here, I'm sure you have stuff to do, or other people to talk to."
    hide mia with Dissolve(1)
    $ MiaTalk = 1
    $ ForestTalk += 1
    jump ForestTalkMenu

label Clearing:
    scene deep forest night with Dissolve(2)
    "You keep walking ahead for what seems like hours. The forest is getting extremely dark. Fireflies zoom around you lighting the way ahead."
    mc "This path never ends."
    tre "I'd say we were going in circles, but I've paid attention. We haven't turned."
    nov "We have to have walked a few miles by now."
    mc "Maybe I should check the map."
    tre "Too dark. Unless you want to use one of the lamps."
    mc "We'll have to soon."
    mia "Is that some light over there?"
    "Mia points off to the side. A path appears that you don't remember seeing before."
    "You feel dizzy."
    "You see a path off to the right. There is an inviting light coming from it."
    mc "Yeah. I think we should go that way."
    "The four of you follow the path for a few hundred feet until you make it to a clearing."
    scene magic campsite with Dissolve(2)
    play music magiccamp fadein 1
    mc "Whoa!"
    tre "Perfect! We've got more then enough space to set up camp!"
    show nova excited at right with Dissolve(1)
    nov "And a lake! I can wash off a bit!"
    mc "There is no lak-"
    "You feel dizzy for a moment."
    "You look over to [Nova] and see a beautiful and peaceful small lake in front of you."
    show mia smiling adv at slightleft with Dissolve(1)
    mia "The stars are beautiful from here! And even the moon is full! It's perfect!"
    mc "Wait, the full moon was like a week ago..."
    "You feel dizzy again. You look up and see the most beautiful full moon you've ever seen."
    "Mia is beaming."
    mia "Isn't this the best?"
    mc "It's beautiful!"
    show trevor neutral behind mia with Dissolve(1)
    tre "You know, when you said we should go on vacation I didn't think it was a good idea, but I take it back."
    mc "Vacation? Nina asked you to come along."
    tre "Nina?"
    tre "Oh, yeah, she said I should have fun... I think."
    mc "Right. And in case monsters showed up."
    tre "Yes. I fight monsters and help the town. It helps me feel special and that way I can hide from my insecurities."
    mc "{color=#b7b7b7}{i}What did he say?{/i}{/color}"
    mc "{color=#b7b7b7}{i}I must be hearing things.{/i}{/color}"
    tre "Let's set up the tent, buddy!"
    "You feel dizzy once more. You clutch your head and your vision swims."
    "{color=#b7b7b7}{i}Buddy? Am I his...{/i}{/color}"
    "Your vision clears."
    mc "Sure thing, buddy!"
    scene MagicCamp1 with Dissolve(2)
    "You and your best friend Trevor set up the tent, smiles on your faces the whole time."
    scene MagicCamp2 with Dissolve(2)
    hide window
    w ""
    "As you two work on the tent, [Nova] and Mia start stripping before taking a bath in the lake."
    nov "Ah, I can't wait to finally take a bath! I'm all stinky from all the walking we just did!"
    mia "I know, right? And this lake looks so beautiful, I bet the water is warm too!"
    nov "By the way, holy shit, Mia! People are always talking about your giant tits, but you also have an amazing ass! What have you been eating, girl?"
    scene MagicCamp3 with Dissolve(2)
    hide window
    w ""
    mia "Huh? People talk about my breasts?"
    nov "You must know that every guy in the village is crazy about them, right? At this point your tits are basically a landmark of our village! I wish I had a body like yours."
    mia " Oh, come on, you look beautiful! I actually hate how much attention my body gets..."
    scene MagicCamp4 with Dissolve(2)
    hide window
    w ""
    nov "Well, you don't mind getting [MC]'s attention, right?"
    mia "No... I wouldn't mind if he... What about you? You don't mind him seeing you naked?"
    nov "Nope. There is nothing he hasn't already seen here. It's kind of weird, but I think I secretly like the way he looks at my body."
    scene MagicCamp5 with Dissolve(2)
    hide window
    w ""
    "The girls play and swim for a bit, then they start washing each other, whispering and giggling as they do so."
    nov "Hey, Mia?"
    mia "Yeah?"
    nov "We don't have any towels. Should we just run for our tent?"
    mia "But... They'll see us..."
    nov "So? Trevor has a girlfriend anyway, and [MC]... It's a good excuse, don't you think?"
    mia "..."
    mia "Okay."
    scene MagicCamp6 with Dissolve(2)
    hide window
    w ""
    "Mia and [Nova] run completely naked to their tent, giggling all the way as they go inside, not looking at you not even once."
    tre "Wow! I can't believe I'm seeing this."
    mc "I know, right? Maybe we should just stay here forever."
    scene MagicCamp7 with Dissolve(2)
    hide window
    w ""
    nov "You could stay there forever, or maybe you want to join us, [MC]?"
    mia "[Nova]! What are you...?"
    mc "Are you serious?"
    nov " Sure. Mia wants it too! Come sleep with us, we could use a man inside to protect us. Trevor can stay on guard, right, Trevor?"
    tre "Sure thing! That's actually a good idea, you guys take this tent and I'll use the other one if I need."
    mc "And you want me inside... now?"
    nov "If you want to."
    stop music fadeout 1
    "You know that Mia and [Nova] are still naked inside. If they don't mind it, you definitely won't. You go inside their tent."
    jump MiaNovaThreesome
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
