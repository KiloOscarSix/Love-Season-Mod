label NinaNight:
    if FuckedLaura == 1:
        "You leave Laura's house with a spring in your step."
        mc "{color=#b7b7b7}{color=#b7b7b7}{i}I just... Holy shit. That was AWESOME!{/i}{/color}"
        mc "{color=#b7b7b7}{color=#b7b7b7}{i}I never expected something like that to happen tonight.{/i}{/color}"
        mc "{color=#b7b7b7}{color=#b7b7b7}{i}I mean, I hoped.{/i}{/color}"
        mc "{color=#b7b7b7}{i}And fantasized... a lot.{/i}{/color}"
        mc "{color=#b7b7b7}{i}But it was better than I ever imagined.{/i}{/color}"
        mc "{color=#b7b7b7}{i}It's weird, I just felt more confident tonight... for some reason.{/i}{/color}"
    else:
        "On your way home you start talking to yourself."
        mc "That was..."
        mc "I think I should have done something back there."
        mc "But... I mean, what would people say if they found out."
        mc "I don't know... Maybe I should have."
        mc "Gah! Oh, well."
    mc "{color=#b7b7b7}{i}I'm too fired up to sleep. I think I'll chill out by the well for a while.{/i}{/color}"
    scene well night with Dissolve (2)
    play music drama
    nvl clear
    n "The breeze picks up a bit as you walk to the cliffside. It rocks the bridge as you cross over to the other side."
    n "Unexpectedly, there is someone already there when you arrive."
    show nina neutral with Dissolve (1)
    nin "Huh? Oh, hi, [MC]!"
    mc "Hey!"
    nin "It's a beautiful night. Isn't it? Clear skies, and a Giant Moon... It's relaxing.'"
    mc "Yeah... Dad calls it a Witch's Moon. Supposedly, magic is more powerful on nights like tonight."
    nin "Are you going to cast a spell on me?"
    mc "Do I look like a witch?"
    nin smiling "Nah, I guess not."
    mc "Dad also said that..."
    nin "What?"
    mc "Never mind."
    nin "Come on!"
    mc "Fine, he said that women get a lot more receptive during a Witch's Moon."
    nin neutral "Ha! Maybe... We ladies do have a connection with her, it seems."
    nin "So, what brings you here?"
    mc "I wasn't tired and wanted to decompress... you?"
    nin "More or less the same. I got bored of the party. Laura left, and you went off with Mia."
    nin "So it was just Trevor and his friends around. I wanted to go, Trevor stayed behind."
    mc "Well then, mind if I keep you company?"
    nin "I think you already are."
    "You sit down next to her on the bench."
    mc "So, how are things going with Trevor? Are you guys good?"
    nin "We're fine..."
    mc "But...?"
    nin moreangry "But nothing! Relationships are just hard sometimes, that's all..."
    mc "How'd you even end up with a guy like him?"
    nin worried "He’s not a bad guy, [MC]! He's really not. He doesn’t show it very often, but he can actually be very sweet. He kind of reminds me of you sometimes; I think you guys would be good friends if you gave it a chance..."
    menu TrevorFriend:
        "I don't know... Maybe... [gr]\[TrevorFriend +1\]":
            mc "Maybe in another life, Nina."
            nin angry "God, you are both so stubborn."
            mc "Maybe that's why we don't get along."
            nin "Uh huh."
            mc "I just don't like that he's with..."
            nin neutral "The militia, I know. Some of them are assholes, but he's not like that."
            mc "Right, the militia."
            nin "Just think about it... OK?"
            mc "Yeah, yeah."
            $ TrevorFriend += 1
            jump NinaNight2
        "He's a douche":

            mc "He's just a preening asshole."
            nin neutral "His friends are all douches, I give you that, but it's like he just plays a part around them... "
            nin "I made the same mistake when he was talking to me that first time."
            mc "What do you mean?"
            nin worried "Look I'm not stupid, he was one of the most handsome and popular boys in the village, and he was making moves on me. I mean, no one had ever looked at me like that."
            nin "I thought it was a joke; a joke or a stupid bet. Then I thought that he was just trying to “score”, but he convinced me..."
            nin "He's a lot more caring and patient than you'd think."
            jump NinaNight2

label NinaNight2:
    "You think back to the scene between them earlier in the night."
    mc "So..."
    nin neutral "What?"
    mc "Have you two already..."
    nin worried "Already what?"
    mc "Oh come on, you know what I mean."
    "Nina blushes and smacks you on the shoulder."
    nin "What?! That's none of your business, asshole!"
    mc "I mean, you were going to head to the grove with him."
    nin neutral "Oh god! You heard us back at the party..."
    mc "Yeah... I did. And I just want you to know you shouldn't let him pressure you."
    nin "I know, OK. I wasn't going to do anything just because HE wanted to. Frankly, he's had the patience of a saint so far."
    mc "So that's a no."
    "Nina sighs."
    nin moreangry "Geez, what’s up with all the sudden interest in my sex life? I could ask you that too, you know."
    mc "When did this become about me?"
    nin "Come on, something changed! You were running around the party chatting up all the girls."
    nin "You even had a date while you did it. You're not supposed to be the social guy at the party. That's not like you!"
    mc "So you expect me to be lonely sitting in a corner? Nice to know."
    nin worried "I didn't mean that. You know that."
    mc "Whatever. It's nice to know my best friend thinks I'm meant to fail."
    mc "Why is that? Because I'm just a regular guy. I'm sorry I'm not popular like the militia."
    nin angry "That's bullshit, you don't have to be in the militia to be important! You know that. I know that!"
    mc "Do you, really?"
    nin "What are you talking about? I never cared that you weren't in the militia. Did you hit your head or something?"
    mc "If you didn't care, why are you dating one of them?"
    nin moreangry "I'm not dating Trevor because he's in the militia! I almost didn't exactly because of that!"
    nin "Why are we even talking about him again? It's not like you're jealous!"
    mc "I don't want to fight about this."
    nin neutral "Well, you keep bringing it up."
    mc "Well, sorry! Everywhere I look it's all about them. And when I finally have a good night, for once, you think it's weird."
    nin "You're not like them, [MC]! I've known you my whole life. You're a..."
    mc "Loser?"
    mc "Because that's what it feels like you said."
    nin worried "I didn't mean that... I... You know..."
    nin "Yeah... I'm sorry, [MC]... I wasn't thinking when I said that."
    nin "I meant it like... I was just surprised. I mean... I even heard Brooke talking to her brother about you."
    nin neutral "It's weird. But it shouldn't come as a shock. We're all growing up. We change."
    nin "Maybe it just took you longer."
    "She smiles at you."
    nin "I am sorry, you know."
    mc "I know... I just haven't had a good night like this before. Socially, I mean."
    nin "Well, whatever you're doing..."
    mc "I guess. I just started following [Nova]'s advice."
    nin smiling "I'm not sure if that's a good thing... But if it works..."
    mc "Plus, I don't know. I've felt different these last couple of days."
    mc "Like I have someone looking out for me, or something."
    mc "That probably sounds stupid."
    nin neutral "Just don't change too much. I like the [MC] I'm with right now."
    mc "I like the Nina I'm with too."
    "Nina doesn't say anything but gives you a big hug. You feel her breath match with yours as she puts her head on your chest."
    scene moon 2 with dissolve
    mc "It's nice being with you like this. We don't hang out as much anymore."
    nin "We're just getting older. It happens... But I know what you mean."
    nin "It must be the moon. Tonight feels special."
    scene moon 1 with dissolve
    mc "I just realized, this would be the perfect romantic way to end a date."
    nin "Yeah, don’t get any funny ideas though!"
    mc "Never. Can you imagine that, us as a couple?"
    nin "Well, people used to think that all the time, remember?"
    mc "That was mainly our families. They all acted like we were going to get married one day."
    nin "Well, Trevor thought we were going out before we got together."
    mc "So he was hitting on my girl? Now I'm really pissed."
    nin smiling "Stop that! But I told him we were just friends. Nothing more than that."
    mc "Well, we did kiss once."
    nin "That TOTALLY doesn't count. We were kids!"
    mc "It counts."
    nin "As if you want me as your first kiss!"
    scene moon 4 with dissolve
    nin "You prefer girls with big boobs, right? Like Mia! Mine are too small!"
    "Nina pushes her breasts together for emphasis."
    mc "I, uh..."
    nin "Come on. You can tell the truth."
    scene well night with dissolve
    show mc neutral at left
    show nina neutral at right

menu NinaBodyResponse:
    "You're actually surprisingly hot [gr]\[NinaLove +1\]":
        hide mc
        show nina neutral at center
        mc "I don't know, you're pretty hot yourself. Not as big, but you've definitely got curves."
        nin smiling "Oh, shut up! I know you're just saying that to be nice."
        nin moreangry "And you know I'll hit you if you say otherwise."
        nin smiling "But thanks anyway."
        $ NinaLove + 1
        jump NinaNight3
    "That's right!":

        hide mc
        show nina neutral at center
        mc "Damn straight! Laura's ass is pretty tight too. It's hard to choose."
        nin angry "Wow. You're such a pig, [MC]"
        "Nina laughs."
        jump NinaNight3

label NinaNight3:
    scene moon 1 with dissolve
    "Nina cuddles up to you again."
    mc "Real huggy tonight, aren't you?"
    nin "Oh, shut up."
    "She says the words playfully, then continues."
    nin "I suppose we should be getting home."
    mc "Why? This is better than the party, for sure."
    nin "You're not wrong. In fact..."
    scene moon 3 with dissolve
    "Nina looks up at you and your eyes meet. Neither of you notice the clouds quickly gathering above you."
    "You lean in and she leans forward."
    if FuckedLaura == 1:
        nin "You smell nice... But a little..."
        nin "Wait, that's Laura's perfume..."
        mc "Um..."
        jump Storm
    else:
        "The air is filled with tension; you grab Nina by the sides of her head..."
        nin "What are we doing?"
        mc "I... don't know..."
        "You and Nina don't break eye contact. It's as if you're both frozen. Then, Nina closes her eyes and you move in for the kiss..."
        jump Storm

label Storm:
    stop music
    scene moon 3 with flashbulb
    play sound thunderloud
    "Then, a flash of light and the sound of thunder break up the moment."
    scene well night with Dissolve(1)
    mc "What the hell? Where did that come from?"
    play music action fadein 1
    nvl clear
    n "A gust of wind rips across the cliffside; it's uncharacteristically cold for this time of year. The wind is so strong it almost knocks Nina over."
    scene well night rain with Dissolve(1)
    play ambient storm fadein 2
    n "The sky which was clear just moments ago is now darkened with clouds. Rain begins to fall. And it's quickly becoming more intense. "
    show nina neutral
    nin "I think we should go... now!"
    play ambient2 storm2 fadein 1
    "As soon as she says that the sky opens up in earnest. Sheets of water carried by the wind fall down on you. The rain obscures your vision, and you can barely even see Nina in front of you."
    hide window
    play sound thunderloud
    scene well night rain
    show nina worried
    nin "[MC]!"
    nin "[MC]! We have to go!"
    mc "Uh... Right!"
    nin "Follow me!"
    hide window
    scene storm 1 with dissolve
    w ""
    "Nina begins to run to the bridge, which is already swaying in the wind. You're still confused about what's happening, when a feeling of dread comes over you!"
    mc "Nina! Wait!"
    mc "{color=#b7b7b7}{i}She's going to die!{/i}{/color}"
    nvl clear
    n "You run after her as fast as you can; she makes it to the bridge just before you when it's struck by lightning!"
    hide window
    play sound thunderloud
    play sound woodcrash
    scene storm 2 with flashbulb
    w ""
    nin "AAAAAH!!!!"
    n "Everything after that happens in an instant but seems to drag out for minutes."
    n "The bridge breaks right as Nina steps on it; she screams, but the sound of distant thunder drowns it out."
    n "All you can think of is how your best friend is going to die, randomly, brutally, right in front of you."
    hide window
    nvl clear
    scene storm 3 with dissolve
    w ""
    n "A hand catches her just before she goes over the edge... After a moment, your realize the hand is yours."
    mc "I... I've got you!"
    "Pain shoots up your right arm radiating from the wound the slime inflicted yesterday. You think you might drop her. You know you are going to drop her. Yet, somehow, you pull her up to safety."
    play sound thunderloud
    "You help Nina up, but in her nervous state, her legs give way. You try to catch her, but she falls on top of you."
    scene storm 4 with dissolve

    nin "I thought I was going to..."
    mc "I know... I did too..."
    "Neither of you say another word as the storm continues to intensify."
    mc "{color=#b7b7b7}{i}We're trapped out here, with no shelter...{/i}{/color}"
    mc "{color=#b7b7b7}{i}Now what?{/i}{/color}"
    play sound thunderloud
    stop music fadeout 5
    stop ambient fadeout 5
    stop ambient2 fadeout 5
    scene black with Dissolve(5)
    scene EndOfChapter1 with dissolve
    "Now would be a good time to save."
    "Thank you for playing Love Season. Please look forward to our next chapter and consider helping us on Patreon, join our Discord and check our other game - Farmer's Dreams!"
    $ persistent.intro = True
    jump Chapter2Start
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
