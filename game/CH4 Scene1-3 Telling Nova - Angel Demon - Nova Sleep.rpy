
label Day6EndCH4:
    play music drama2 fadein 1
    scene farm bedroom night with Dissolve(2)
    show nova worried with Dissolve(1)
    mc "I'm going to the mountain. I won't let dad die."
    "Nova stops for a second to process what you just said."
    show nova neutral with Dissolve(0.2)
    nov "OK."
    mc "Don't try to stop me [Nova], I..."
    mc "What?"
    nov "I said, OK. I understand. If no one else can go it falls to us."
    mc "I wasn't expecting that response..."
    nov "Why not? Redd's in danger. It's pretty clear."
    nov "This is going to be dangerous though. First off, the mountain is surrounded by a dense forest. Second, the mountain's ALSO named after the goblin horde that lives in it."
    mc "I'm pretty good at hiding."
    show nova smirk with Dissolve(0.2)
    nov "You know how crazy this sounds, right?"
    mc "I know, but I can't let dad die... I can't."
    nov "You don't have to explain it to me."
    mc "Thanks Nova, I knew you'd understand."
    show nova neutral with Dissolve(0.2)
    nov "So, when do we leave?"
    mc "Huh? We?"
    mc "No way, [Nova]! It's too dangerous."
    nov "Maybe you didn't hear me before. \"We're\" going."
    mc "Those things are killers, [Nova]! Have you ever seen a goblin before?"
    nov "No. Have you?"
    mc "Yes! And I was scared shitless! I don't want to see you get killed. No way you're going!"
    show nova annoyed with Dissolve(0.2)
    nov "Well, it's a good thing I don't plan to get killed. Don't want to get hurt even."
    mc "I appreciate it, but he's my dad. I can't have you risk yourself for..."
    nov "[MC]!"
    mc "What?"
    show nova angry with Dissolve(0.2)
    nov "You're a son of a bitch."
    nov "I might not be his real kid like you are. He might not trust me with his bedside confessions, but I don't care. He's... family. He's always been there for me."
    "Nova's voice gets louder."
    nov "Without Redd, I don't even know where I'd be right now. So if you think you can just run off to try and save him and leave me here twiddling my fucking thumbs, then fuck you!"
    mc "I didn't mean to..."
    "She screams at you."
    nov "No! You're not the only one who gets to care about him! You're not the-"
    mc "I'm sorry, [Nova]! You know I didn't mean it like that! I know you love dad too."
    "[Nova] breathes and gains her composure. She's still visibly shaken."
    show nova annoyed with Dissolve(0.2)
    nov "Damn right I do. You guys are all I have."
    mc "But [Nova], someone has to look after the farm while I'm gone."
    nov "There is no farm without Redd."
    mc "..."
    mc "Yeah."
    nov "I'm going with you. That's not a request."
    show nova annoyed at farright with easeinleft
    show mc neutral at farleft with Dissolve(0.2)
menu:
    "Fine [gr]\[Nova Love\]":
        hide mc with easeoutleft
        show nova annoyed at center with easeinright
        mc "Fine."
        nov "Good. You're finally seeing reason."
        mc "One of us has to. And I know if I say no, you're going to go by yourself anyway."
        $ NovaLove += 1
    "I can't let you":

        hide mc with easeoutleft
        show nova annoyed at center with easeinright
        mc "Sorry, but I can't let you risk yourself like this."
        show nova angry with Dissolve(0.2)
        nov "That's not your call to make."
        mc "I said no."
        nov "Make peace with it. I'm going."
        mc "I... Fuck. All right then, but I won't save you if a goblin decides to make some [Nova] barbecue! Damn, I might thank it even."
        show nova smirk 2 with Dissolve(0.2)
        nov "Ha! You're the one who needs a bodyguard with those twig arms! You can't cheat and tickle goblins to victory, you know that, right?"

label Day6End2:
    play music nova2 fadein 1
    show nova neutral with Dissolve(0.2)
    nov "Now that that's taken care of we need to come up with a plan."
    mc "How many of our supplies survived the storm?"
    nov "How about none? We stored all of them in the barn, remember? And the barn isn't there anymore."
    mc "We need a tent, or at least some sleeping rolls. And some food. A compass... and flint too."
    mc "I still have my knife at least."
    nov "No food for the trip, though."
    mc "So we have to buy all that tomorrow. Assuming the shop even has rations right now. Or camping gear."
    nov "How much money do you have from odd jobs?"
    mc "Maybe 30G?"
    nov "I'm about the same. It's not much."
    mc "I'll check with Laura tomorrow, maybe she can cut us a deal."
    show nova worried with Dissolve(0.2)
    nov "I wouldn't count on it - they're probably hurting too."
    nov "This is going to be rough."
    mc "I know... So how about this? We leave in the morning, day after tomorrow. That gives us a day to get money and buy supplies."
    mc "I already have some work lined up, I think Elise wants to see me again."
    if NovaDarius == 1:
        nov "And I think Darius has some work for us too."
    else:
        nov "I'm sure I can find something too."
    mc "Then we meet in the afternoon, pool our money and I'll go and see Laura about our gear."
    nov "OK then. Sounds like a plan."
    mc "Let's get to sleep. We have a lot to do tomorrow."
    nov "Yeah, yeah. Get in bed. I'll go put these damned fish away."
    hide nova with easeoutleft
    "Nova grabs the fish and heads out to the kitchen. You get undressed and lie down in the bed."
    mc "{color=#b7b7b7}{i}I don't know, I'm worried about taking her with me. I just can't...{/i}{/color}"
    mc "{color=#b7b7b7}{i}She's right, though. If I did this on my own, it'd be rough.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Hang on, dad. We'll save you.{/i}{/color}"
    "You fall asleep while going over what you need to do tomorrow in your head."

    stop music
    scene black with dissolve
    hide window
    scene titlecardCH4 with Dissolve (3)
    pause 2
    scene whitescreen with Dissolve(4)
    play music dreaming
    '???' "Can you feel it? The power waking inside of you? Coursing through your veins?"
    mc "{i}What?{/i}"
    '???' "Come now..."
    scene HD1 with Dissolve(2)
    hide window
    w ""
    "You wake up in a place that doesn't quite seem connected to the world. Mist roils around the outside of an island floating in what appears to be nothing."
    mc "Where the hell am I?"
    mc "The last thing I remember is being asleep at home..."
    scene HD2 with Dissolve(2)
    hide window
    w ""
    mc "There's nowhere to go! Just fog on all sides."
    scene HD3 with Dissolve(2)
    hide window
    w ""
    ang "Welcome, [MC]. It is good to finally meet you."
    mc "{color=#b7b7b7}{i}An angel? And a demon? What in the world?{/i}{/color}"
    mc "Oh, I'm dreaming again."
    ang "What you consider a dream is just another lens into reality."
    dem "What my pretentious sister here means is: Yes, you are dreaming, but it's also real."
    mc "How does that even work?"
    dem "Two things can be true at once. I didn't think humans like you would have such a hard time figuring it out."
    mc "Just who are you two?"
    scene HD4 with Dissolve(2)
    hide window
    w ""
    lin "My name is Linda. This is my sister, Jasmine."
    jas "I'm the interesting one."
    mc "Yeah... definitely a dream."
    scene HD5 with Dissolve(2)
    hide window
    w ""
    jas "How thick can you be? OK. Yes, it IS a dream."
    scene HD4 with Dissolve(1)
    lin "Actually, This is more like a shared dream. We all exist in here, but we also exist in other planes. It's like an alternative dimension that occurs in your dream!"
    mc "So I'm here... and asleep back home?"
    scene HD3 with Dissolve(1)
    jas "Exactly. And we are too. The dream world links all realities."
    lin "This isn't the first time we've had this conversation. But it also is."
    mc "So why me?"
    jas "Your amulet. We found you because of your amulet. Or more specifically, you found us. Humans normally can't see us on their own and we can never really interact with them, so this is a treat. I've finally met someone who can talk back!"
    mc "So you just want to talk?"
    lin "More than that. We are here to both guide and observe."
    jas "We want to see what you do in the weeks and months ahead. It's going to be interesting!"
    mc "Why me? I'm not..."
    scene HD5 with Dissolve(1)
    jas "Sure you are. I can see the corruption in you, boy. You want to be one of the bad boys. Take what you want and damned be the consequences. You see what others have and want it for yourself. You and I have a lot in common!"
    scene HD4 with Dissolve(1)
    lin "Stop that! He has a purer heart than any I have ever seen. He cares for others and puts their needs above his own, often at the risk of his own life. He is destined for a higher path."
    mc "How can I be both of those things?"
    scene HD6 with Dissolve(2)
    hide window
    w ""
    jas "I told you. Two things can be true at once."
    lin "So go forth and live with honor. It's the only path of true happiness."
    scene HD5 with Dissolve(1)
    jas "And utter boredom. Don't listen to her. Trust me. My way is the way of rulers, hers is the way of peasants."
    scene HD4 with Dissolve(1)
    lin "Oh, quiet you! I know where your path leads. Corruption always reaps what it sows."
    scene HD5 with Dissolve(1)
    jas "And it sows hedonism and excitement. You need to get with the times sister."
    mc "Uh..."
    scene HD3 with Dissolve(1)
    lin "Sorry. Ignore her. Now all we ask is that you live your life as you choose. We will be watching."
    jas "Yeah. We won't intervene... Much."
    lin "At all, Jasmine!"
    jas "Such a buzzkill."
    lin "Your choices will affect the world, so be careful with them."
    scene HD5 with Dissolve(1)
    jas "And this is breaking the rules, but I'm going to give you a bit of a boost. We know where you're going and you're going to need it."
    lin "You can't!"
    jas "Come on! He has less backup this time. Even you have to want him to protect the girls."
    scene HD4 with Dissolve(1)
    lin "That is true. The situation is different this time. I shall assist as well."
    scene HD6 with Dissolve(1)
    jas "This might sting a bit, kid. See you soon."
    lin "Be mindful of your actions, they will have great influence."
    scene whitescreen with Dissolve(2)
    "The angel and demon both put their hand on your forehead. You feel energy coursing through your body. Suddenly you feel like your insides are burning. You scream in pain as you feel your muscles burning."
    mc "AAAAAAH!!!"
    stop music fadeout 1
    scene mc wake up with Dissolve(2)
    "You sit up in your bed covered in sweat."
    mc "These dreams are driving me crazy."
    mc "Sorry if I woke you up..."
    "You look and realize that [Nova] isn't in your bed."

menu:
    "Go back to sleep":
        mc "{color=#b7b7b7}{i}She probably went out to the bathroom or something.{/i}{/color}"
        mc "She'll be fine."
        "You turn over and go to sleep."
        $ NovaBlanket = 0
        jump Day7Start
    "Look for her [gr]\[Nova Love\]":

        play sound walkgrass
        scene farm kitchen night with Dissolve(2)
        mc "{color=#b7b7b7}{i}Where the hell did she go?{/i}{/color}"
        "You walk out of your room and you don't see [Nova] anywhere. You see a checklist on the kitchen table listing supplies for your trip."
        mc "{color=#b7b7b7}{i}Looks like she was doing an inventory of what little we have.{/i}{/color}"
        mc "{color=#b7b7b7}{i}But where is she now?{/i}{/color}"
        "You notice the door to Redd's room has been left slightly open."
        mc "{color=#b7b7b7}{i}I guess she was checking on dad.{/i}{/color}"
        "You enter Redd's room."
        play music night fadein 1
        scene nova redd sleeping with Dissolve(2)
        hide window
        w ""
        "[Nova] shivers."
        mc "{color=#b7b7b7}{i}She's got to be freezing.{/i}{/color}"
        mc "Hey, dummy..."
        "[Nova] shifts in her chair. You shake her a little bit."
        scene nova redd sleeping 2 with Dissolve(2)
        hide window
        w ""
        mc "Ice elemental! Wake up!"
        "[Nova] groans."
        nov "You're an ice elemental... asshole."
        mc "Awake?"
        nov "Izzit morning already?"
        "She seems to be barely conscious."
        mc "No, you fell asleep next to dad."
        nov "Wanna go back to sleep."
        mc "Come on, let's get you to bed."
        "[Nova] continues to mumble. She's half awake at best."
        nov "Gotta make sure, Redd..."
        mc "Yeah. I know. Come on. You got it all."
        "You put your arm on her shoulder again and [Nova] shrugs it off."
        nov "Nuh uh. I want to sleep here."
        "She puts her head back in her arms and tries to go back to sleep."
        jump NovaBlanketChoice

label NovaBlanketChoice:
menu:
    "Bring her a blanket [gr]\[Nova Love +1\]":
        mc "Fine, but don't blame me if your neck is killing you in the morning."
        nov "Mmmhmm..."
        scene farm bedroom night with Dissolve(1)
        "You go to your room and take the blanket off of your bed."
        mc "{color=#b7b7b7}{i}I might be a little cold, but she needs it.{/i}{/color}"
        "When you return to your father's room [Nova] is asleep again. You drape the blanket over her."
        scene nova redd sleeping 3 with Dissolve(2)
        hide window
        w ""
        mc "There you go. Sorry I said that before."
        "[Nova] seems to smile in her sleep. You rustle her hair with your hands and return to your bedroom."
        $ NovaLove += 1
        $ NovaBlanket = 1
        jump Day7Start
    "Carry her to bed [gr]\[Nova Love +2\]":

        mc "Nuh uh, when you don't sleep well you get cranky."
        "You reach over again to try and pull her up."
        nov "I'm cranky now. I wanna stay here!"
        mc "Nope. Come on."
        "You grab [Nova] by the hand and she pulls it away."
        nov "Dummy... can't sleep in there with you. I get too horn...t. Hot..."
        mc "What are you on about?"
        nov "Just let me sleep."
        mc "No way. It's your bed, right? Isn't that what you said?"
        "[Nova] pouts."
        nov "No fair using my words against me when I'm too tired to think."
        mc "You don't want to walk? Fine."
        "You reach under [Nova] and lift her up in your arms."
        scene nova redd sleeping 4 with Dissolve(2)
        hide window
        w ""
        nov "What are you doing?"
        mc "Taking you to bed."
        nov "Stop it!"
        mc "You're acting like you have a choice here."
        nov "Pssh... fine... bed does look comfy."
        scene nova bedroom 16 with Dissolve(2)
        "You lay her down and she immediately falls asleep."
        mc "{color=#b7b7b7}{i}Man, she was beat.{/i}{/color}"
        "You crawl into bed next to her, pull the covers over the both of you and go to sleep."
        mc "{color=#b7b7b7}{i}Still, she's kinda cute when she's like that. Acting like a kid.{/i}{/color}"
        $ NovaLove += 2
        $ NovaBlanket = 2
        jump Day7Start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
