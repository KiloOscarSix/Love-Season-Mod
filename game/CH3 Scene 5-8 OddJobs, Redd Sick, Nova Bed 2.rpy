label Day5NovaTown:
    $ persistent.selena_first = True
    scene market with Dissolve(2)
    play music nova fadein 1
    "You walk over to the market and see [Nova] standing around."
    show nova angry with Dissolve(1)
    nov "Took you long enough."
    mc "Yeah look, sorry about that, I just-"
    nov "Needed to get shot down?"
    mc "Hey!"
    show nova neutral with Dissolve(0.1)
    nov "Whatever, do what you want, but I'd avoid strange travelers - I heard a story of a dude who fucked a camp follower. She had a magic disease and his dick exploded."
    "You shiver."
    show nova smirk with Dissolve(0.1)
    nov "True story."
    mc "Never mention that again."
    nov "Mention what, dick necrosis?"
    mc "Ugh..."
    show nova neutral with Dissolve(0.1)
    nov "So how much did you spend?"
    mc "What?"
    nov "On that amulet thing. How much did she cheat you out of?"
    mc "Nothing, it was a gift."
    nov "You just don't want to tell me because you know I'll make fun of you."
    mc "No, really! She said it was a free charm that-"
    show nova smirk with Dissolve(0.1)
    nov "Is probably worth less than the fake gold it's made out of."
    mc "You're just jealous that she didn't give you anything."
    show nova smirk 2 with Dissolve(0.1)
    nov "Way too gaudy for me, thanks. Not even Sophie would wear something like that."
    mc "I think it looks pretty cool."
    nov "Sure thing, [MC]. Keep believing that."
    scene village destroyed with Dissolve(2)
    "You and [Nova] head out into the village proper."
    show nova neutral with Dissolve(1)
    nov "So, where to?"
    mc "I don't know... I'm pretty sure the job board got destroyed."
    "[Nova] points to a nearby house."
    nov "Nah, it's over there on the roof of Toby's house."
    mc "I stand corrected."
    nov "So door to door?"
    mc "I don't think we have another option."
    hide nova with Dissolve(1)
    "You and [Nova] walk down the streets of the town, knocking on doors and checking in on the residents."
    show village day 2 behind nova with Dissolve(2)
    show toby neutral at slightleft with Dissolve(1)
    show nova neutral at slightright with easeinleft
    tob "Yeah, like I'd need help from you. [Nova] can give me a hand with something out back if she wants!"
    show nova smirk with Dissolve(0.1)
    nov "I would, but I don't take jobs that small."
    scene elises garden with Dissolve(2)
    show sophie neutral with Dissolve(1)
    sop "Mom mentioned something, but she heard there was a new merchant in town and ran out to see her."
    mc "All good."
    scene elders house with Dissolve(2)
    show elder neutral at slightleft with Dissolve(1)
    show nova neutral at slightright with Dissolve(1)
    eld "Ah, good of you to ask! My home was spared the brunt of things, but I'll ask around. Come by tomorrow and I'll see what I can find."
    "Mia walks in."
    show nova neutral at center with easeinright
    show mia neutral at slightright with Dissolve(1)
    play music afternoon2 fadein 1
    mia "Oh, [MC]! It's great to see you. I heard you made it back!"
    mc "Yes, yesterday."
    mia "I'm sorry I didn't go to see you, but it's been crazy..."
    mc "I understand. We spent all of yesterday fixing up the house. Didn't even get a chance to rest."
    mia "Oh, you poor thing... If you need any help at all. I am here."
    mc "Thanks."
    show nova annoyed with Dissolve(0.1)
    nov "Geez, she's fawning all over you and doesn't even say hi! I thought we bonded."
    show mia blushing 1 with Dissolve(0.1)
    mia "I'm so sorry [Nova]! That was rude. I didn't mean to... I mean-"
    show nova neutral at center with Dissolve(0.5)
    nov "I'm just messing around, relax!"
    show mia neutral at slightright with Dissolve(0.5)
    mia "But I just don't want you to think that I... I mean, I had a lot of fun at the party! thanks to both of you."
    nov "Well, I did too. you're a sweetheart, we need to hang out more!"
    mia "It sounds like fun!"
    "Mia frowns as she thinks over something."
    mia "But, I have so much to do here. I don't know if I will have time."
    eld "Nonsense. Don't dote on me, Mia. I always tell you to get out more."
    nov "See? all taken care of. We're busy as hell too, but don't worry, I always find time for friends. Even new ones."
    "Mia beams at the two of you."
    eld "I'm sure that you all have work to find or do."
    mc "We do."
    mia "Good luck then!"
    nov "See you later! We'll get together soon."
    "The two of you leave the Elder's house."
    scene village destroyed with Dissolve(2)
    show nova neutral with Dissolve(1)
    mc "Damn, it was nice seeing Mia, but still no work."
    nov "Yeah, I think we should split up for a bit. Check out the bar and the new shop, see if there's anything there."
    nov "I'll check on Lisa and the baker's place."
    mc "Sounds good. Meet up at the market afterwards?"
    nov "Yup."
    "You wave goodbye to [Nova] and head in the direction of Evelyn's pub."
    play music evelyn fadein 1

    scene evelyn pub 1 with Dissolve(2)
    hide window
    w ""
    "When you arrive you can see Evelyn playing with Beanie outside the pub."
    mc "{color=#b7b7b7}{i}Dayum!{/i}{/color}"
    mc "{color=#b7b7b7}{i}Evelyn really has an amazing ass. No wonder all the guys here are after her...{/i}{/color}"
    mc "{color=#b7b7b7}{i}But she's also really easy to talk to, like she could hang out with Nina, [Nova] and I just as easily. That could be why she's so popular; she's not a flirt, she's just genuinely friendly.{/i}{/color}"
    mc "{color=#b7b7b7}{i}I wonder what I'd need to do to get her attention?{/i}{/color}"
    mc "Hi, Evelyn!"

    scene pub exterior day with Dissolve(2)
    show evelyn excited with Dissolve(1)
    eve "Oh! [MC], I'd heard you made it back! In fact it's all the militia guys could talk about last night."
    mc "Um... what did they say?"
    eve "Nothing you don't know. Something about being amazed you survived out there."

default dynamicChoice1 = ""
default dynamicChoice2 = ""
if CoolStoryBro == 1:
    dynamicChoice2 = "[red]\[EveLove -1\]"
else:
    dynamicChoice1 = "[gr]\[EveLove +1\]"

menu:
    "It was nothing. [dynamicChoice1]":
        mc "It was nothing, really. We just holed up in a cave and waited for the storm to pass."
        if CoolStoryBro == 1:
            show evelyn neutral with Dissolve(0.1)
            eve "Really? Because after she got some drinks in her Lisa said you told her you fought a goblin!"
            mc "{color=#b7b7b7}{i}Ah, shit.{/i}{/color}"
            mc "Did she say anything else?"
            eve "Not really. Pretty sure no one believed it anyway."
            mc "Did you?"
            show evelyn smiling with Dissolve(0.1)
            eve "Maybe. I mean, you are a hero."
            mc "What?"
            eve "You rescued Beanie after all!"
            jump EvelynPubClean
        else:
            show evelyn smiling with Dissolve(0.1)
            eve "Don't sell yourself short. A lot of people I know would have died out there. Or needed rescue."
            mc "I just don't like talking about it that much."
            eve "I get you, but hey, I think it was pretty impressive!"
            mc "Thanks."
            eve "You did rescue Beanie after all, so I already know you're a hero."
            $ EveLove += 1
            jump EvelynPubClean
    "Badass, right? [dynamicChoice2]":

        mc "It was crazy as fuck out there, but I made it through like a champ."
        if CoolStoryBro == 1:
            show evelyn smiling with Dissolve(0.1)
            eve "I heard! Because after she got some drinks in her Lisa said you told her you fought a goblin!"
            mc "{color=#b7b7b7}{i}Ah shit...{/i}{/color}"
            mc "Did she say anything else?"
            eve "Not really. Pretty sure no one believed it anyway."
            mc "Did you?"
            eve "Maybe. I mean, you are a hero."
            mc "What?"
            eve "You rescued Beanie after all!"
            show evelyn frowning with Dissolve(0.1)
            eve "But bragging like that... not the greatest look. But I'll give you a pass this time!"
            $ EveLove -= 1
            jump EvelynPubClean
        else:
            show evelyn neutral with Dissolve(0.1)
            eve "You don't need to brag, it's not the best look, but you are a hero."
            mc "Huh?"
            show eveyln smiling with Dissolve(0.1)
            eve "You saved Beanie after all!"
            jump EvelynPubClean

label EvelynPubClean:
    show evelyn neutral with Dissolve(0.1)
    eve "So, what brings you here? You know we aren't open, right?"
    mc "[Nova] and I are out making ourselves useful, seeing if anyone has work that needs to get done."
    eve "I see. That's kind of you. Thankfully we weren't really damaged badly."
    mc "That's great to hear."
    eve "But why don't you come in for a bit at least? I can make you some coffee and I need to feed Beanie."
    mc "That'd be great."
    eve "Come on in then."
    "Evelyn turns around and enters the pub."

    scene pub interior with Dissolve(2)
    "You enter the pub with Evelyn, trying very hard not to stare at her ass."
    "Evelyn walks over to the bar where Beanie is waiting for her."
    show evelyn neutral with Dissolve(1)
    eve "You hungry? Just hold on."
    "Evelyn pours some milk into a dish and puts it in front of her cat. It starts lapping away at it with vigor."
    play sound meow
    mc "Well, you just made his day!"
    show evelyn smiling with Dissolve(0.1)
    eve "He's easy to please that way."
    mc "This place looks so different in the daytime."
    eve "Well, it's a lot quieter, that's for sure."
    eve "But I still have a lot of work to do."
    mc "Already? Don't you work all night? When do you get a break?"
    show evelyn frowning with Dissolve(0.1)
    eve "A break? I wish! My dad doesn't have enough help around here, so I'm not only the waitress but the designated cleaner now."
    mc "Ouch. Sounds rough."
    eve "Eh, It's not so bad. I prefer working here when it's quiet, actually. Once people start drinking, that's when it gets to be a headache."
    mc "I've seen how it can get in here at night so I totally understand. Ether way, I have some free time now, I could lend you a hand if you want."
    show evelyn neutral with Dissolve(0.1)
    eve "I was thinking about that actually! But I haven't even given you your coffee yet."
    mc "It's fine, if you want we can drink after I help you clean."
    eve "I can't really pay much though, not without my father's permission."
    mc "How hard can it be?"
    eve "Harder than it looks. But I'll take you up on your offer all the same."
    show evelyn smiling with Dissolve(0.1)
    eve "No take backs, by the way! There's a lot to do, and I do mean a lot. Let's see if you're still acting all tough after we spend the next few hours cleaning the place."
    mc "OK, now I'm worried."
    show evelyn frowning with Dissolve(0.1)
    eve "Thinking of running already? I locked the door, so you're stuck here now!"
    mc "You're not serious are you?"
    eve "Maybe."
    show evelyn smiling with Dissolve(0.1)
    eve "Let's get started."
    "Evelyn leads you to the cleaning supplies, her ass swaying side to side as she walks. You catch yourselve staring once again and snap yourselve out of it as she turns to you."
    eve "Here we are, [MC]. Just grab this and... Oh, wait, I need to change! I'm still in my nice clothes."
    eve "You should change to something more appropriate too. You won't want to get your regular clothes all wet and dirty!"
    eve "Not to mention the cleaning supplies can destroy nice fabrics and dyes."
    mc "I didn't bring any spare clothes. And I don't think you're my size..."
    eve "So just strip down to your underwear then."
    mc "Haha! Wait, are you serious?"
    show evelyn neutral with Dissolve(0.1)
    eve "Are you shy?"
    mc "Not shy exactly, but..."
    eve "You're thinking too much about it. It's not like we're getting naked or anything."
    mc "No, that would be crazy. You have a good point."
    eve "OK then! I'll be right back."
    hide evelyn with easeoutright
    "Evelyn walks upstairs and you begin taking off your clothes."
    mc "{color=#b7b7b7}{i}*I really hope her dad doesn't come down right now, that would be awkward.*{/i}{/color}"
    mc "{color=#b7b7b7}{i}Still, Evelyn naked... that's a nice thought!{/i}{/color}"
    "You're lost in thought, dreaming of Evelyn and you feel yourself get hard."
    mc "{color=#b7b7b7}{i}NO! DOWN! STOP! Think of something not sexy, fast! I can't have a hard on when she gets back.{/i}{/color}"
    "You focus on the least sexy thing you can think of - Trevor in a dress making the moves on you, and your erection vanishes with all speed."
    "As it does, you hear Evelyn walking down the stairs."
    mc "{color=#b7b7b7}{i}Oh, thank the maker. That would have been embarassing.{/i}{/color}"

    scene evelyn pub 3 with Dissolve(2)
    hide window
    w ""
    eve "What do you think? It's the height of fashion right?"

menu:
    "Joke with her [gr]\[EveLove +1\]":

        mc "Oh, without a doubt. In fact, you should go out in that every day, it'll start a new trend!"
        "Evelyn smiles."
        eve "I have enough people staring at me at night, thank you very much."
        mc "I'm just being honest."
        $ EveLove += 1
        jump EvelynPubClean2
    "Straight up compliment":

        mc "Even in those old clothes you look amazing. Seriously, wow."
        "Evelyn seems unsure as how to best respond."
        eve "Uh... thanks."
        mc "{color=#b7b7b7}{i}Her legs are even better than I imagined! And look at her toned stomach! I'm lucky as hell right now. She never dresses like this! Oh man... seeing her naked would be amazing.{/i}{/color}"
        mc "{color=#b7b7b7}{i}But... she's not even looking at my body. I guess she doesn't see me as a guy. Damn it.{/i}{/color}"
        jump EvelynPubClean2

label EvelynPubClean2:

    play sound frontdoor
    scene pub interior with Dissolve(2)
    show evelyn cleaning neutral with Dissolve(1)
    eve "Well, if you're done staring at my fashion choices, let's get to work."
    mc "Fair enough."
    hide evelyn with easeoutleft
    nvl clear
    "You and Evelyn begin cleaning the pub. The work is a lot harder than you would expect."
    "After some time..."
    show evelyn cleaning neutral with Dissolve(1)
    eve "Way too slow! Come on, you have to go a little faster than this or we'll never finish."
    mc "OK OK!"
    hide evelyn with easeoutleft
    "After some more time..."
    "Evelyn cleans the rafters in the pub."
    show evelyn cleaning neutral with Dissolve(1)
    eve "How is it going down there? My back is already starting to hurt a bit! Don't forget to do some stretches."
    mc "It might be a little late for that already."
    mc "{color=#b7b7b7}{i}Damn, this view! I can't afford another hard-on!{/i}{/color}"
    hide evelyn cleaning neutral with Dissolve(1)
    "A little while later..."
    mc "Do your customers know that alcohol goes in the mouth, not on the floor?"
    show evelyn cleaning neutral with Dissolve(1)
    eve "Sometimes, but if you think you've got it bad I think someone pissed in a corner over here."
    mc "Yee..."
    hide evelyn cleaning neutral with Dissolve(1)
    "A little while later. You're checking a tankard hidden on a beam."
    mc "Hm, Evelyn, these aren't your panties in this empty tankard, are they?"
    show evelyn cleaning frowning with Dissolve(1)
    "Evelyn just stares you down."
    mc "Just checking!"
    hide evelyn with Dissolve(1)
    "Even later on..."
    "You and Evelyn finish cleaning. You're both covered in sweat, but the work is done."
    mc "I think that's it!"

    scene evelyn pub 4 with Dissolve(2)
    hide window
    w ""
    "She stretches in front of you and her top almost comes off."
    eve "Yep. Not too bad, all things considered."

    scene pub interior with Dissolve(2)
    show evelyn cleaning neutral with Dissolve(1)
    mc "If this is \"Not too bad\" I'd hate to see an awful night. How can you do this every day?"
    eve "Eh, you get used to it."
    mc "You live a hard life, Evelyn."
    "Evelyn shrugs."
    eve "And people wonder why I don't like alcohol."
    mc "Well, alcohol did indirectly lead to me seeing you in your spiffy new outfit, so I can't hate on it."

    scene evelyn pub 5 with Dissolve(2)
    hide window
    w ""
    "Evelyn turns to you and you notice that all the sweat has made her top nearly transparent."
    mc "{color=#b7b7b7}{i}Oh shit, I can see nearly everything!{/i}{/color}"
    "Evelyn sees you staring and looks down, realizing for the first time how exposed she is."
    eve "I think I should get out of this thing now. Goddess, [MC]! You're... you should probably get dressed too!"
    "Evelyn blushes slightly and continues staring for a second before she shakes herself out of it."
    mc "{color=#b7b7b7}{i}Well, at least she noticed me now. I hope that's a good thing.{/i}{/color}"
    mc "Yeah, right away."
    scene black with Dissolve(4)
    "Evelyn cleans up and gets dressed, and you do as well."

    scene evelyn pub 6 with Dissolve(2)
    hide window
    w ""
    "She returns and gets behind the bar, signalling you over to her."
    eve "So, the best part about hard work, is kicking back to relax afterwards. And if I remember right, I promised you a drink."
    mc "You did."
    eve "So what will it be?"

menu:
    "Coffee [gr]\[EveLove +1\]":
        mc "A coffee'd be great."
        eve "I was hoping you'd say that. It's my favorite."
        eve "I'll make us some of my personal blend."
        mc "Sounds fancy!"
        "Evelyn brews up the coffee and you make small talk for a bit until it's done."
        $ EveLove += 1
        jump EvelynPubClean3
    "Milk [gr]\[EveLove +1\]":

        mc "Some milk would be great!"
        eve "Milk?"
        "Evelyn laughs."
        eve "You really don't care about your image at all, do you?"
        mc "Hey, it does a body good. Especially after hard work like this."
        mc "I also look cool with a nice milk moustache!"
        eve "Jeez, you're starting to remind me of Beanie."
        mc "He's got good taste, in drinks and in people."
        eve "We mainly use the milk for cooking, so don't expect this every time you're here! I'm making an exception here."
        "Evelyn pours you a glass of milk."
        $ EveLove += 1
        jump EvelynPubClean3
    "Beer [red]\[EveLove -1\]":

        mc "Beer me."
        eve "Starting a little early, aren't you?"
        mc "I'm at the bar... it seems appropriate."
        eve "OK, cool, I'll get you a beer."
        "Evelyn goes behind the bar and gets your drink ready."
        $ EveLove -= 1
        jump EvelynPubClean3

label EvelynPubClean3:
    "Evelyn serves you your drink. You drink and make small talk with Evelyn until you are done."

    scene pub interior with Dissolve(2)
    show evelyn smiling with Dissolve(0.2)
    eve "There you go. Thanks for the help today! And for helping with Beanie before."
    mc "Hey! I'm a helper."
    eve "Can't deny that."
    show evelyn neutral with Dissolve(0.1)
    "Evelyn goes behind the bar and pulls out some gold."
    eve "It's not much, but I hope that covers things."
    mc "Thanks! Normally I'd help you out for free..."
    eve "Hey, none of that! You did a great job, so you get your reward."
    eve "Simple as that."
    show evelyn smiling with Dissolve(0.2)
    eve "But if you need more work I'll talk to my dad. You're really good at cleaning up after drunks and I need some help around here from time to time."
    mc "Sure, if I'm free I'll stop by!"
    eve "Perfect! It doesn't have to be a regular thing, but I do want to help you out."
    mc "Thanks."
    eve "I still need to finish getting ready for tonight. I'll see you later [MC]!"
    mc "Bye, Evelyn."
    "You say goodbye to Evelyn and head outside."
    mc "{color=#b7b7b7}{i}It's not much but maybe it's enough to buy some seeds for Dad...{/i}{/color}"
    mc "{color=#b7b7b7}{i}Laura's store should have some, I hope. And she might even have some odd jobs to do there too.{/i}{/color}"
    scene pub exterior day with Dissolve(2)
    "You walk across the way towards the general store."
    if FuckedLaura == 1:
        mc "{color=#b7b7b7}{i}I haven't seen her since the night we had sex. I wonder if she's wants to keep going with that.{/i}{/color}"
    "You enter the general store."
    scene lauras shop interior with Dissolve(2)
    play music laura fadein 1
    play sound frontdoor
    if FuckedLaura == 1:
        show laura neutral with Dissolve(0.2)
        lau "Nina, you should have told me! I never would have done anything."
        show laura neutral at slightleft with easeinleft
        show nina neutral at slightright with Dissolve(0.2)
        nin "There is nothing to apologize for."
        lau "Bullshit! I can tell it's making you uncomfortable. You even tried to hook us-"
        "Laura stops talking as you walk in."
    else:
        show laura neutral with Dissolve(0.2)
        lau "You know I'm not going to blab to anyone right? What happened?"
        show laura neutral at slightleft with easeinleft
        show nina neutral at slightright with Dissolve(0.2)
        nin "Nothing happened!"
        lau "Bullshit! You just don't want to talk about it."
        show nina angry with Dissolve(0.2)
        nin "Can we just drop this?"
        lau "Sure, but I think I know your secret."
        "Laura stops talking as you walk through the door."
    show laura surprised with Dissolve(0.2)
    lau "Speak of the demon!"
    show nina worried with Dissolve(0.2)
    show laura neutral with Dissolve(0.2)
    "Nina turns around. You both stare at each other."
    mc "{color=#b7b7b7}{i}This is the first time I've seen her since I got back... This should be easy, just act normally.{/i}{/color}"
    mc "Uh..."
    nin "I heard about your house. How is everything?"
    mc "Darius helped us rebuild, we're a lot smaller for now... [Nova] and I are sharing a room."
    show nina neutral with Dissolve(0.2)
    nin "That's... a little weird."
    mc "You have no idea."
    "Nina pauses. She starts to say something then stops herself."
    mc "Hm... How's your family?"
    show nina neutral with Dissolve(0.1)
    nin "Great. All good there."
    nin "Dad wants to thank you personally or something."
    mc "Probably just an excuse to get me to ask you out again."
    "Nina laughs."
    show nina smiling with Dissolve(0.1)
    nin "Like he needs an excuse."
    mc "Well, tell him I said hi."
    nin "Sure."
    "She turns to Laura."
    show nina neutral with Dissolve(0.1)
    nin "Anyway, I have to run. I'll see you later, OK?"
    lau "Sure thing."
    "Nina walks past you."
    nin "Bye, [MC]."
    "She rushes out the door."
    hide nina with moveoutright
    mc "{color=#b7b7b7}{i}That was weird. And more uncomfortable than I thought it would be. Or am I just overthinking it?{/i}{/color}"
    if FuckedLaura == 1:
        show laura neutral at center with easeinleft
        lau "So, why didn't YOU tell me?"
        mc "Excuse me?"
        lau "That you two were into each other."
        "You remain silent for a moment before responding."
        mc "I don't know what you're talking about."
        lau "What's going on with you two?"
        mc "Nothing. We're just friends."
        lau "OK, be stubborn. You're both acting like idiots."
    else:
        show laura neutral at center with easeinleft
        lau "I guess that explains why you ran off!"
        mc "Excuse me?"
        lau "You two look really cute together."
        mc "What, me and Nina?"
        mc "You know she has a boyfriend, right?"
        show laura smiling with Dissolve(0.1)
        lau "And that always stops people."
        mc "Look, nothing happened, I don't know what you think you're seeing here, but..."
        show laura neutral with Dissolve(0.1)
        lau "None of my business I guess."
    mc "Sorry."
    lau "Whatever, I'll drop it for now."
    lau "Anyway, do you need something?"
    mc "Two things actually. First, do you have any seeds? Our fields got wrecked and we lost our entire crop."
    lau "Oh man, that's pretty shitty."
    lau "I think we still have some that weren't destroyed by the storm. Our basement flooded so we lost a lot of stock."
    mc "Everyone's having a rough time it looks like."
    lau "How much do you have on you?"
    mc "Not nearly enough. That's the other thing I wanted to talk to you about - can we get some credit to get enough seeds to replant? If we don't do it this week we might not make harvest in time."
    lau "That's not up to me. Daddy handles the credit. I really want to help, but you'll have to check back later."
    mc "He's not here right now?"
    lau "Nope, he went with Mom to check on an incoming shipment that hasn't shown up."
    if FuckedLaura == 1:
        mc "In that case, since we're alone..."
        mc "Maybe we can have some more fun?"
        "You walk up to Laura and move in for a kiss."
        "Laura backs off."
        lau "Easy there tiger, I had a good time the other night, but I'm kind of busy right now."
        lau "And I don't think that would be fair to Nina."
        mc "Nina again? We're not dating! What does she have to do with this?"
        lau "What does she have to do with this? Nina's like my only friend in this town, well, besides you. I don't want to ruin that."
        mc "She has a boyfriend, we're not dating. We're just friends. "
        lau "Come on, that awkwardness... that's not just friends. I don't know what it is but you'd better figure it out."
        lau "Oce you have that resolved we'll talk, but not until then."
    lau "So I'll see you later, OK?"
    if FuckedLaura == 1:
        mc "OK... sure thing."
    else:
        mc "Sure thing."
    lau "I promise I'll ask Daddy about the seeds. Good luck with everything!"
    mc "Thanks."
    scene village day 2 with Dissolve(1)
    "You walk out of Laura's store a little confused."
    if FuckedLaura == 1:
        mc "{color=#b7b7b7}{i}I guess I expected more after the stuff we did at the party.{/i}{/color}"
        mc "{color=#b7b7b7}{i}And she seems to know something's up with Nina, which could be a problem.{/i}{/color}"
        mc "{color=#b7b7b7}{i}I don't think I did anything wrong when I hooked up with Laura though. Did I?{/i}{/color}"
    else:
        mc "{color=#b7b7b7}{i}Damn, she seems to know something's up between Nina and I. I hope it's not obvious to anyone else.{ /i}{/color}"
        if NinaProposition == 1:
            mc "{color=#b7b7b7}{i}Then again, that could break her up with Trevor.{/i}{/color}"
            mc "{color=#b7b7b7}{i}And also get my ass kicked.{/i}{/color}"
    "You notice the sun is starting to set."
    mc "{color=#b7b7b7}{i}I should go check in with [Nova]. I hope she found some work, at least.{/i}{/color}"
    scene market with Dissolve(2)
    play music evening fadein 1
    "You head over to the Market again."
    show nova neutral with Dissolve(0.2)
    nov "Hey! Took you long enough."
    mc "Busy day."
    nov "Looks like you had more to do than I did."
    mc "Helped Evelyn clean up the pub."
    nov "That doesn't sound too bad."

menu:
    "Evelyn was hot at least":

        mc "Oh it was bad! But the company was good."
        "You grin."
        mc "Evelyn had some pretty sheer clothing on."
        show nova annoyed with Dissolve(0.1)
        nov "Typical! Tits are the first thing on your mind."
        mc "Hey! Asses too."
        nov "How could I ever forget."
        nov "Seriouly, [MC] you need to get laid. Big time."
        jump Day5MCNovaSunset
    "It was pretty gross.":

        mc "There was... stuff. Everywhere."
        "You shudder."
        show nova smiling with Dissolve(0.1)
        nov "Well, drunks aren't known for their cleanliness."
        mc "Or bladder control."
        nov "Gross!"
        mc "You have no idea."
        nov "But you powered through like a champ. I bet."
        jump Day5MCNovaSunset

label Day5MCNovaSunset:
    show nova neutral with Dissolve(0.2)
    nov "Oh, I stopped by Darius' house and sadly he was there."
    mc "Did he have anything for us?"
    nov "He needed some help hammering fence posts. He said it was brainless and we could help speed it up."
    mc "If he's paying I guess we should do it. I also need to swing my Elise's house tomorrow."
    nov "Sure, we can do that after we hammer posts. So long as he doesn't keep creeping on me."
    show nova angry with Dissolve(0.2)
    nov "\"Oh, Nova, there's another post you can help me with in my bedroom! I'm sure you'd be great at it\"!"
    nov "Fucking creep."
    mc "You could just not do it."
    show nova neutral with Dissolve(0.2)
    nov "I don't think he'll try anything with you there."
    mc "Yay, More hard labor! gotta love our life right now."
    nov "You'd complain no matter what we had to do."
    mc "I would not."
    nov "Come on, Redd's probably waiting."
    "You and [Nova] head back home."
    scene farm fixed with Dissolve(2)
    "When you reach your house you see Redd outside."
    mc "Hey Pop! You look like hell."
    show father neutral with Dissolve(1)
    dad "I'm fine, just a little bit under the weather. I was able to get most of the farm tilled, so after tomorrow we should be able to plant again."
    show father neutral at slightleft with easeinright
    show nova neutral at slightright with Dissolve(1)
    nov "That's great news!"
    dad "Since both of you were out all day I hope you were able to get some work in?"
    dad "Well, [Nova] at least."
    mc "When are you going to stop busting my balls?"
    dad "Never."
    "Redd laughs. Then breaks into a cough."
    mc "Dad! That doesn't sound good at all."
    dad "I'm fine son, like I said."
    show nova worried with Dissolve(0.2)
    nov "You need to get that looked at, Redd! Should I go get Silas?"
    dad "I said I'm fine. You kids worry too much."
    dad "Anyway, tell me about what you did today."
    "You and [Nova] recount the jobs you completed and you hand over the gold you received."
    dad "Damn, not enough for a full field of seeds yet."
    mc "Laura said she'd ask her father about extending us some credit at least."
    dad "We can only hope."
    show nova smirk 2 with Dissolve(0.1)
    nov "We'll be fine! No one can farm like you can, Redd."
    dad "Thank you Nova! I just wish my son would compliment me like that more often."
    mc "Just keep fishing, dad! It might happen someday."
    dad "Come on you two, it's dinner time. We're low on meat, but we have some leftover potatoes that I-"
    "Redd starts coughing again."
    mc "Dad!"

    scene redd sick 1 with Dissolve(2)
    play music reddsick fadein 1
    "As he turns to you you see blood dripping down his lips."
    dad "I'm..."
    scene redd sick 2 with Dissolve(2)
    "Redd falls to the ground in a heap."
    nov "REDD!"
    mc "DAD!"
    "After the collapse you stayed with your father and [Nova] went to get help."
    mc "Stay with me, dad, come on..."
    "Redd doesn't respond. His breathing is labored."
    "Redd flitters in and out of consciousness as you watch over him. You grip his hand and constantly look at the road to your farm for any sign of [Nova]."
    mc "{color=#b7b7b7}{i}Damn it! What's taking so long?{/i}{/color}"
    dad "Son?"
    mc "Dad! Just relax, help is coming."
    dad "I must have caught something from that damn..."
    mc "You'll be OK. Just relax."
    dad "I'm sorry, I should have taken more care..."
    mc "Come on! Where are they?"
    scene farm fixed with Dissolve(2)
    "You look to the road again and see [Nova] and Mia running at an almost full sprint towards your house."
    show nova worried with Dissolve(0.2)
    nov "How is he?"
    mc "He's in and out..."
    show nova worried at slightright with easeinleft
    show mia neutral at slightleft with Dissolve(1)
    mia "The elder is out by the lake, we sent Trevor to go and fetch him."
    mc "Damn it. Dad's in rough shape."
    mia "I understand. I'll do everything I can, please step aside."
    mc "Will he be OK, Mia?"
    mia "I need to take a look at him."
    scene redd sick 3 with Dissolve(2)
    mia "He has a severe fever."
    "Redd looks up at Mia."
    dad "Honey?"
    mia "Seems like he's delierious from the fever. I think I have something that can help."

    "Mia looks down at Redd and pulls a vial out of one of her pockets."
    mia "Mr. Redd, I need you to drink this."
    dad "Of course, dear!"
    mc "Is he seeing Mom?"
    nov "I think so... wow."
    "Mia feeds Redd the medicine and he drinks it eagerly."
    mia "Good."
    scene farm fixed with Dissolve(2)
    mc "{color=#b7b7b7}{i}I know Mia's been training for this and looking after sick people for a while now.{/i}{/color}"
    mc "{color=#b7b7b7}{i}But its like she's almost a different person! I'm impressed.{/i}{/color}"
    show mia neutral at slightleft with Dissolve(1)
    show nova worried at slightright with Dissolve(1)
    "Mia sighs."
    mia "The medicine will knock him out for a little while. We need to move him inside."
    mc "Right."
    show nova neutral with Dissolve(0.2)
    nov "Come on then."
    play sound frontdoor
    scene redd sick 4 with Dissolve(2)
    "You and [Nova] grab your father and take him inside to his bed. He's sleeping peacefully."
    nov "Is he going to be OK?"
    mia "We just have to wait. If the fever breaks that's a very good sign."
    "The three of your sit at Redd's bedside in silence. Waiting for any change."
    "You hear a knock at your front door. You rush over to find Elder Silas and invite him in."
    scene farm house interior with Dissolve(2)
    show elder neutral with Dissolve(1)
    eld "Where is your father?"
    mc "This way."
    scene farm redd room with Dissolve(2)
    nvl clear
    n "You escort the elder into your room and hear him talking over your father's condition with Mia."
    n "[Nova] walks up to you."
    nvl clear
    show nova neutral with Dissolve(0.2)
    nov "We should let them work."
    "You nod and the two of you walk to the living room."
    scene farm house interior night with Dissolve(2)
    mc "Damn it all."
    show nova neutral with Dissolve(0.2)
    nov "He's a strong old cuss, I'm sure he'll be fine, he just overworked himself."
    "You force a smile."
    mc "You're right."
    show nova smirk with Dissolve(0.1)
    "[Nova] tries to smile back but she can't, tears well up in her eyes."
    show nova worried with Dissolve(0.1)
    nov "No I'm not. He was coughing up blood [MC], that's not normal."
    nov "I'm so worried..."
    mc "[Nova]..."
    show nova sad with Dissolve(0.1)
    nov "I just don't want to lose him, you know."
    mc "I know."
    scene farm kitchen night with Dissolve(2)
    "You and [Nova] sit at your dinner table in silence until Mia and the Elder come out of Redd's room."
    mia "Hey..."
    "Both you and [Nova] look up at them."
    scene redd sick 5 with Dissolve(2)
    play music romance1

    eld "It looks like Mia's medicine did the trick. From what I can see so far he's doing better right now."
    mia "It was probably just a miasma from the storm, but his fever has broken."
    nov "Oh! That's amazing!"
    scene redd sick 6 with Dissolve(2)

    mia "Oh!"
    nov "Thank you!"
    eld "And this old man doesn't get a hug?"
    mc "I can hug you if you want, Silas."
    "Silas laughs."
    eld "No, that's quite alright."
    mc "Well, thank you. Both of you."
    "Mia looks at you while still being hugged my [Nova]."
    mia "I'm having a little trouble breathing, but it was nothing!"
    "[Nova] lets her go."

    scene farm kitchen night with Dissolve(2)
    show nova blushing with Dissolve(0.2)
    nov "Sorry Mia, I don't know what came over me."
    show nova blushing at left with easeinright
    show mia smiling at right with Dissolve(1)
    show elder neutral with Dissolve(1)
    eld "In either case, your father is awake though he's quite tired."
    mc "Can we see him?"
    eld "Of course."
    "Silas and Mia walk to your front door."
    eld "Let me know if anything changes, but in either case I'll be back tomorrow to check in on Redd."
    mc "Right. Thanks again!"
    mia "I'm happy that everything worked out!"
    "Once you've seen them out you and [Nova] go to Redd's room."

    scene redd sick 4 with Dissolve(2)
    nov "He still looks weak. And I think he's sleeping."
    dad "There you two are. I thought you'd abandoned me here."
    mc "Come on Dad, not now."
    dad "Your old man is fine. Like I said, just overwork and the cold nights got to me."
    dad "Silas says I need to rest for a week at least."

    scene redd sick 7 with Dissolve(2)
    nov "Don't worry, we'll cover for you."
    dad "I hope I didn't worry you, [Nova]."
    nov "Not at all! I knew you were too stubborn to let a cold get to you."
    "Redd looks at [Nova] and you can tell he notices the red in her eyes."
    dad "That's good. Nothing to worry about at all - I'm not going anywhere."
    nov "Good. Because this one over here is useless at farming."
    "You sigh."
    mc "It never ends."
    dad "Nova, would you be a dear and give me a few minutes with [MC]? I need to have a man to man talk with him."
    "[Nova] seems to be taken by surprise at the request."
    nov "Of course."
    nvl clear
    "[Nova] kisses Redd on the forehead and leaves the room. As she does she looks at you quizzically, you shrug your shoulders."
    mc "{color=#b7b7b7}{i}It's not like I know what he wants either.{/i}{/color}"
    "[Nova] closes the door behind her as she leaves."
    play sound bedroomdoor
    scene redd sick neutral with Dissolve(2)
    dad "OK, time for a talk, son."
    mc "You're giving me serious face right now, I'm starting to get concerned."
    dad "Well... this scare got me thinking."
    dad "Can you handle things when I'm gone?"
    mc "You're not going anywhere, dad."
    scene redd sick serious with Dissolve(1)
    dad "Not this time, but you never know."
    mc "Sure you do!"
    dad "I'm not planning on kicking the bucket, and I'm proud of what you've done these last few days."
    dad "But I'm still worried about something."
    mc "[Nova] and I can handle stuff. You just rest."
    scene redd sick neutral with Dissolve(1)
    dad "It's not about that. I'm sure she'll run the farm just fine."
    dad "But I see you still single after all these years and it worries me."
    mc "We're going to talk about this NOW?"
    scene redd sick joking with Dissolve(1)
    dad "Now, if your tastes go elsewhere, I want you to know you can tell me. I won't judge."
    mc "What? No dad! What the hell!"
    dad "I just never see you with the ladies. A boy your age should have a girlfriend, thinking about settling down in a few years."
    mc "I'm just looking around."
    scene redd sick neutral with Dissolve(1)
    dad "You don't seem to be looking very hard. You can tell your old man, have you ever been with anyone?"
    mc "DAD!"
    mc "We're NOT having this conversation!"
    dad "I didn't think so."
    mc "Look, I mean, yes... OK... I have."
    scene redd sick dubious with Dissolve(1)
    dad "So you do have a girlfriend?"
    mc "No! it's... It's just a little complicated."
    dad "It always is at your age."
    dad "You need to find someone stable, someone who can keep you in check."
    mc "Geez dad... what's with this?"
    scene redd sick serious with Dissolve(1)
    dad "It's important for a man to have a good woman in his life, a partner, not just a fling. You're a good kid, but don't be afraid to put it all on the line!"
    dad "It would be nice to see you with someone before I-"
    mc "Now you're talking like you're not going to get better. You heard what the Elder said."
    dad "It must be the medicine... I'm a little loopy."
    mc "You're telling me. Look, you'll feel better tomorrow, then we can talk when you're you again."
    scene redd sick joking with Dissolve(1)
    dad "You're right, but I'll feel better faster if you bring a girl over!"
    mc "Gross! Find your own girl!"
    scene redd sick serious with Dissolve(1)
    dad "Not for me!"
    mc "I was kidding. Come on now, get some sleep."
    dad "I'll take you up on that. I am pretty tired. Tomorrow we'll talk about [Nova], there's something I..."
    scene redd sick 4 with Dissolve(2)
    "Redd closes his eyes and immediately falls asleep."
    mc "{color=#b7b7b7}{i}That medicine took a lot out of him. I'm really hoping dad doesn't bring this up EVER again.{/i}{/color}"
    mc "{color=#b7b7b7}{i}What was he mumbling about [Nova] at the end there anyway?{/i}{/color}"
    "You open the door to your father's room."
    scene farm house interior night with Dissolve(2)
    play sound bedroomdoor
    play sound blow
    "There is a slight bump when you open the door and you see [Nova] standing in the hallway."
    show nova neutral with Dissolve(1)
    play music nova2 fadein 1
    nov "So, what was that all about?"
    mc "Don't you already know?"
    nov "What?! How would I know? You were the one in there."
    mc "Uh-huh."
    nov "So...?"

menu:
    "He wants me to get a girlfriend [gr]\[NovaGFTell\] \[NovaLove +1\]":
        mc "He wants me to find a girlfriend because he might die someday or something."
        mc "He's pretty loopy."
        show nova surprised with Dissolve(0.1)
        nov "He is if he thinks anyone would date you!"
        mc "..."
        nov "You know I'm kidding, [MC]! Relax."
        nov "You'll get someone soon... if you follow my advice anyway."
        $ NovaGFTell = 1
        $ NovaLove += 1
        jump Day5Sleep
    "Nothing in particular [red]\[NovaGFTell\]":

        mc "He's pretty high on that Medicine. It was a lot of rambling, nothing important."
        show nova neutral with Dissolve(0.1)
        nov "Oh, so no reason at all."
        mc "Nope. Nothing worth talking about."
        nov "And you expect me to believe that?"
        mc "You can believe what you want."
        show nova angry with Dissolve(0.1)
        nov "Bleh! You suck right now."
        $ NovaGFTell = 0
        jump Day5Sleep

label Day5Sleep:
    show nova neutral with Dissolve(0.1)
    nov "Well, I'm beat so I'm going to bed."
    mc "Maker, yes! That sounds great."
    "You walk to your bedroom."
    mc "No feet shenanigans tonight, deal?"
    nov "So I can still steal the blanket?"
    mc "NO!"
    show nova smirk 2 with Dissolve(0.1)
    nov "Stingy."
    mc "Yep. I'm stingy because I don't want to freeze."
    nov "Fine. I'll let you have half the blanket, but promise no more tickling?"
    mc "Deal."
    scene nova teasing 1 with Dissolve(2)
    hide window
    w ""
    "You strip to you underwear and look over to see that [Nova] has started changing as well."
    mc "Whoa! Hold on, I'll step outside."
    nov "Meh, whatever. We've seen everything at this point."
    mc "This is weird."
    nov "Only if you make it that way. Leave if you want."
    scene nova teasing 2 with Dissolve(2)
    hide window
    w ""
    mc "Kind of pointless now, isn't it?"
    nov "Pretty much my point."
    scene nova teasing 3 with Dissolve(2)
    hide window
    w ""
    "[Nova] puts her bedclothes on and slides into your bed. You put out the lamp and join her. You pull in close and brush against her soft skin as you do."
    nov "You know, this isn't so bad. I say when we fix up the house we just turn my old room into a really nice bath! Our old one was too small."
    mc "There's not enough room in here for two beds and all our stuff."
    nov "I'm good sharing."
    mc "But you don't have the fear of frozen feet keeping you up at night."
    "[Nova] shifts and moves her feet towards you."
    mc "You do that and our deal is off!"
    scene nova closeup smiling with Dissolve(1)
    nov "I'm prepared. I can beat you in a tickle fight.."
    mc "I'm just not in the mood I guess. But I'll do it if I have to."
    scene nova closeup neutral with Dissolve(1)
    nov "I'm not either to be honest. Plus it's not the same if Redd isn't gonna scream at us for being too loud."
    mc "Yeah... But at least he's going to be OK."
    nov "I know, I don't think I was really able to breathe right until I heard the good news."
    nov "I'm going to bitch him out when he's better though! He shouldn't scare us like that."
    mc "Just give him a bit. He's still acting a little off. I guess because of the fever or whatever."
    nov "Like when he asked you to get a girlfriend?"
    if NovaGFTell == 0:
        mc "You heard all of that after all?"
        show nova closeup smiling with Dissolve(1)
        nov "DUH! Still kind of pissed you didn't come clean with me about it."
        mc "It felt a little private."
        nov "I thought we didn't keep stuff from each other."
        nov "Speaking of which..."
    else:
        mc "Yeah, that was weird."
        nov "Just a little. By the way..."
    show nova closeup annoyed with Dissolve(1)
    nov "You've been holding out on me!"
    mc "What?"
    nov "Or were you lying to him?"
    mc "{color=#b7b7b7}{i}What's she talking about? Oh!{/i}{/color}"
    if NovaGFTell == 1:
        mc "You heard the whole conversation, didn't you?"
        nov "DUH! Of course I did. But don't change the subject."
        mc "I'm not changing the subject."
    else:
        mc "You heard that part too?"
        nov "Yes. Now, don't even try stalling."
    show nova closeup neutral with Dissolve(1)
    nov "So who was it?"
    mc "No one. I was lying, OK?"
    nov "Ok. Mia is out, she's not that kind of girl."
    mc "Oh my..."
    nov "So who else could it be?"
    mc "It's nobody and it's none of your business anyway."
    show nova closeup annoyed with Dissolve(1)
    nov "Sure it is! I'd totally tell you if I got laid!"
    mc "I wouldn't ask."
    nov "I'd still tell you."
    if MCSophieLike == 1:
        show nova closeup surprised with Dissolve(1)
        nov "Did you punch above your weight and finally bag Sophie at the party?"
        mc "NO!"
        nov "Damn... I was going to say congrats on converting that crush."
    else:
        show nova closeup neutral with Dissolve(1)
        nov "Sophie? I mean, she was fucking PLASTERED at the party."
        mc "Not as much as Toby was."
        mc "But no."
    mc "Are we done now?"
    show nova closeup neutral with Dissolve(1)
    nov "Well, this is a mystery then."
    if MCEvelynLike == 1:
        nov "OK, I know you've got a thing for Evelyn..."
    else:
        nov "Next in the process of elimination... Evelyn."
    show nova closeup smiling with Dissolve(1)
    nov "Wait! You went to her place and helped her \"clean\"."
    nov "So THAT'S why you wanted to split up today!"
    mc "Nope. I wanted to split up because we could do more."
    show nova closeup annoyed with Dissolve(1)
    nov "Darn, running out of options here."
    mc "You're getting obsessed."
    show nova closeup surprised with Dissolve(1)
    nov "Wait... of course! That new city girl!"
    mc "Laura?"
    nov "Laura!"
    if FuckedLaura == 1:
        mc "What? How would I even... I barely know her."
        show nova closeup smiling with Dissolve(1)
        nov "Shit! I was right!"
        nov "I never thought you had it in you! Good for you, buddy!"
        mc "I'm not confirming anything."
        show nova closeup annoyed with Dissolve(1)
        nov "Fine, be that way."
        "[Nova] looks at you with an expression that says she clearly doesn't buy it."
    else:

        mc "No, I kinda chickened out there."
        show nova closeup neutral with Dissolve(1)
        nov "Seriously?"
        mc "I said too much already. Just forget about it."
        nov "I mean, YOU turned down a hot girl? I guess it's kinda noble."
        show nova closeup surprised with Dissolve(1)
        nov "But that just leaves... Nina?"
        show nova closeup annoyed with Dissolve(1)
        nov "Psh! You were lying after all."
        mc "I told you."
        show nova closeup neutral with Dissolve(1)
        nov "You shouldn't lie to Redd like that, but I guess you wanted to make him feel better."
        nov "Don't worry, I won't tell him anything."
        nov "But how weird would that have been? You know getting together with her is a horrible idea, right?"
        mc "Right."
    show nova closeup neutral with Dissolve(1)
    nov "Well, since we've made clear your lack of experience, do you want me to give you some pointers?"
    mc "What the hell? NO!"
    show nova closeup smiling with Dissolve(1)
    nov "God, you boys are so damn shy when it comes to talking about this stuff!"
    mc "I'm not shy, this is just weird!"
    scene nova teasing 4 with Dissolve(2)
    hide window
    w ""
    nov "Whatever. Anyway, you should definitely get yourself a girlfriend as soon as possible."
    nov "I don't want to deal with this thing every time we're sleeping together or when I beat you in a tickle fight!"
    "[Nova] reaches down, and her hand brushes against your cock."
    mc "[Nova]! Watch your hands!" with vpunch
    mc "{color=#b7b7b7}{i}What is she doing?{/i}{/color}"
    "You twitch against her hand and she quickly pulls away from you."
    mc "{color=#b7b7b7}{i}She's almost my... This feels so wrong!{/i}{/color}"
    scene nova closeup surprised with Dissolve(2)
    nov "What the hell, [MC]? Did I get you hard, AGAIN?!"
    mc "Of course not! It was because you were talking about all the other girls!"
    mc "No way am I going to be turned on by sleeping next to you."
    scene nova teasing 5 with Dissolve(2)
    hide window
    w ""
    "As you say that you turn over, back towards [Nova]. You have enough on your mind without thinking about how what you just said was an absolute bald-faced lie."
    nov "Oh really? Not at all?"
    mc "The idea is gross."
    scene nova teasing 6 with Dissolve(2)
    hide window
    w ""

    nov "Well in that case, since I don't do anything for you. That makes things easier."
    "[Nova] waves her bra in front of your face."
    mc "What the hell?"
    nov "Just go to bed, nothing to see here."
menu LookOrTurn:
    "Turn around to confront her":
        scene nova teasing 7 with Dissolve(2)
        hide window
        w ""
        "You flip over and see [Nova], completely naked."
        nov "Wow, I really thought you'd have pussied out. But tits are tits I guess. Something tells me you'd even want to see Nina's grandma naked."
        mc "How am I the bad guy here?"
        nov "You are such a pervert! I guess it is true, when the blood goes down there you just don't even think."
        mc "Oh, I get it, you just want the bed to yourself! Fine, I'll sleep outside. Fuck it."
        nov "Oh please, you're taking this way too seriously. You've seen me naked before."
        mc "{color=#b7b7b7}{i}Not this close!{/i}{/color}"
        mc "Going now."
        scene nova teasing 8 with Dissolve(2)
        hide window
        w ""
        nov "I get it, you just need some time to relieve your tension. How about this? To show what a good friend I am, I'll let you jerk off to me before you go to sleep."
        mc "Are you fucking serious?"
        nov "I already said I don't want to deal with that thing every night."
        mc "I..."
        "You subconsciously start reaching out for your cock."
        nov "OH MY GOD! I was kidding!"
        mc "What?"
        nov "Good night, [MC]!"
        scene nova teasing 9 with Dissolve(2)
        hide window
        w ""
        "[Nova] lies down in bed and rolls over."
        mc "{color=#b7b7b7}{i}What just happened?{/i}{/color}"
        "You sit there dumbfounded."
        nov "Revenge is a trollfucker. Enjoy your blue balls."
        mc "You little... We had a truce!"
        nov "You still have your blanket. And my 'ice-elemental' feet - still SUPER mean by the way - haven't touched you."
        mc "That was pure evil. The purest."
        nov "You'll recover."
        nov "Good night, you perv."
        mc "I am going to get you for this!"
        nov "Promises, Promises. I know you're not going to do anything."

        scene nova teasing 10 with Dissolve(2)
        hide window
        w ""
        "[Nova] rubs her ass against your erection..."
        mc "{color=#b7b7b7}{i}God damn it! I should not be this turned on by her. It's fucking [Nova], we're almost family...{/i}{/color}"
        nov "Good night."
        mc "{color=#b7b7b7}{i}She's still messing with me... What's the best way to handle this?{/i}{/color}"
        jump NovaAttackMenu


menu NovaAttackMenu:
    "Turn Away and go to bed.":
        mc "Whatever. Goodnight."
        "You turn around and ignore her."
        scene black with Dissolve(2)
        mc "{color=#b7b7b7}{i}Sleep well, [Nova]. This isn't over.{/i}{/color}"
        jump NovaMasturbation
    "Up the ante [gr]\[NovaFlirt\]":

        $ NovaFlirt = 1
        mc "Ok then."

        scene nova teasing 11 with Dissolve(2)
        hide window
        w ""
        "You surreptitiously lower your underwear letting your cock free."
        nov "What are you doing?!"
        mc "You're right, it is nice sleeping naked, isn't it?"
        "Your cock presses up against her naked ass, you feel it twitching against her. You move your hips and slowly press her ass apart."
        "[Nova] moans in surprise and shifts herself away, but it doesn't help as she's rubbing you with her ass as she moves. "
        "She offers no resistance, in fact she seems to be getting into it."
        scene nova teasing 12 with Dissolve(2)
        hide window
        w ""

        "You pull her in closer."
        nov "Stop poking my ass!"
        "[Nova] grinds against you. She spreads her legs and shifts so your cock slips between her thighs."
        mc "{color=#b7b7b7}{i}She's so wet right now... and she was giving {i}me{/i} shit?{/i}{/color}"
        nov "You're gonna make a mess..."
        mc "Not so much fun when the shoe's on the other foot, is it?"
        nov "Shut up, this is just me trying to get comfortable."
        nov "You know I like to move in bed."
        scene nova teasing 13 with Dissolve(2)
        hide window
        w ""

        "She moves her hips and you keep sliding along her wet thighs."
        mc "{color=#b7b7b7}{i}I can feel the lips of her pussy on my cock! I just want to...{/i}{/color}"
        scene nova teasing 14 with Dissolve(2)
        hide window
        w ""
        "You can't think straight anymore. You grab her tits and move your hips even faster. You adjust your angle and press upwards and you feel her lips slightly part as your head reaches her entrance."

        "[Nova]'s eyes open with surprise as she realizes what's about to happen."
        nov "Wait!" with vpunch
        mc "What?"
        scene nova teasing 15 with Dissolve(2)
        hide window
        w ""
        nov "Whoa! You almost... Are you crazy? You almost put it in! And... we can't."
        mc "I thought that..."
        "You take a moment and catch your composure. Hot or not you know this is wrong, or at least you desperately are trying to convince yourself that it is."
        mc "Sorry. I went too far."

        show nova teasing 16 with Dissolve(1)
        nov "Don't take all the blame. I teased you too much, what did I expect, right? Lesson learned!"
        mc "Uh, yeah... totally wrong."
        scene nova teasing 15 with Dissolve(1)
        nov "It's been an emotional day, we're obviously still shaken about everything that happened. How about we promise, no more jokes?"
        mc "Deal. And we-"
        nov "Never talk about this again."
        mc "Talk about what?"
        nov "Exactly."
        nov "I'm going to close my eyes and go to sleep, you do the same, OK?"
        mc "OK."
        scene black with Dissolve(2)

        "You turn over and feel [Nova] scooting away from you."
        nov "Good night, [MC]."
        mc "Good night..."
        $ renpy.end_replay()
        jump Day6WakeUp

label NovaMasturbation:
    scene black with Dissolve(2)
    "[Nova] doesn't look back at you. You turn the other way and try to relax."
    "After some tossing and turning you fall asleep."
    nov "Mmm... hah... hah..."
    mc "{color=#b7b7b7}{i}What is that?{/i}{/color}"
    "You hear [Nova] moaning behind you."
    mc "{color=#b7b7b7}{i}Is she masturbating?{/i}{/color}"

    scene nova teasing 17 with Dissolve(2)
    hide window
    w ""
    "You can't see her from your position, but the vibrations on the bed are happening at a faster and faster pace."
    mc "{color=#b7b7b7}{i}This is so wrong... if I turned over right now, what would happen?{/i}{/color}"
    "[Nova] cuts off her scream of orgasm by biting on her pillow."
    "[Nova] breathes heavily. You feel her shuffle in the bed and stop moving."
    mc "{color=#b7b7b7}{i}Shit, was she masturbating because of what happened earlier?{/i}{/color}"
    mc "{color=#b7b7b7}{i}Damn it, I'm going to be hard all night again!{/i}{/color}"
    mc "{color=#b7b7b7}{i}I need to stop thinking about her like that, but...{/i}{/color}"
    "You lie awake for what feels like hours mulling over this problem until sleep finally comes."
    $ renpy.end_replay()
    jump Day6WakeUp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
