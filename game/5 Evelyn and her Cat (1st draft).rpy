label EvelynTree:
    hide window
    scene village day 1 with dissolve
    play music morningquiet
    "You leave your home and search the village for any sign of the missing chickens."
    mc "{i}At this point they could be anywhere{/i}"
    "After asking around, one of the villagers mentions seeing one headed in the direction of the local pub."
    mc "{i}Well, that's my only lead. Let's see if I can find it.{/i}"
    play sound chicken
    "You head over toward the pub and hear a loud clucking."
    mc "{i}Jackpot!{/i}"
    scene pub exterior day
    show chicken:
        xalign 0.5 yalign 1.0
    "In front of the pub you see one of your chickens pecking around a tree trunk. Evelyn, the daughter of the pub's owner, is trying to shoo it away."
    hide chicken
    play music evelyn fadeout 1
    show evelyn neutral at center
    "Beautiful and well-known in the town. Every guy you know wants to get on with her, and if she knows it, she never puts on airs about it. In fact, she treats everyone equally."
    "Something rare in this town."
    show chicken:
        xalign 0.5 yalign 1.0
    show evelyn neutral at slightright
    eve "Get away!"
    play sound chicken
    "The chicken backs off for a little while."
    hide chicken with moveoutleft
    "After the chicken retreats, Evelyn cautiously approaches the tree."
    show evelyn neutral at center
    eve "Come on! He won't hurt you! Just jump into my arms."
    play sound meow
    "She is answered by a loud meow."
    mc "{i}Looks like her cat's stuck up there.{/i}"
    mc "Need some help?"
    "Evelyn turns her head and sees you. She smiles for a moment."
    show evelyn smiling at center
    eve "Yeah, this chicken scared the crap out of my cat. She's stuck at the top of the tree and won't jump down."
    eve "Where did that thing even come from?"
    mc "Someone broke into our coop last night. I'm going around trying to find them all right now."
    eve frowning "Well, if you find the guy who did it, hit him for me."
    mc "Will do."
    eve neutral "Well, I shooed him into the corner over there. He's all yours now."
    mc "She... But here, let me close your fence, so she won't go anywhere."
    eve "Well she'd better not. She scared the crap out of Beanie."
    mc "You named your cat after a hat?"
    eve "Not now, please. Can you help me get her down?"
    mc "Uh... sure. What do you need?"
    eve "These aren't really good clothes for climbing trees, but if I get on your shoulders, I think I can reach her."
    mc "I could climb up and get her myself."
    eve "Bad idea. She doesn't really like boys much. She'll just try to scratch your eyes out."
    mc "Animals love me."
    eve "Even if they did, I'm not so sure about Beanie. She's been really jumpy all day."
    mc "What? Why?"
    eve "I don't know... she's just always been a scaredy cat. But today she's been acting worse than usual. Then the run in with your chicken really set her off."
    mc "Well, in that case..."
    "You bend over and point towards your shoulders."
    eve smiling "Perfect, just... don't drop me, ok?"
    mc "Promise."
    "You bend over and Evelyn climbs onto your back. She sits on your shoulders and you lift her up."
    play sound clothes
    mc "{i}Either she's heavier than she looks, or I'm weaker than I look, one of the two.{/i}"
    mc "Ok, going up in one, two, THREE."
    scene evelyn tree 1
    hide window
    w ""
    mc "There we go."
    eve "Ok, let's just move forward a bit. I've almost got her."
    mc "Yup. Moving now."
    "You inch forward, slowly so as not to mess with Evelyn's balance, and soon she's level with Beanie."
    eve "Come on girl. Jump into my arms."
    "Evelyn reaches out, and right as she's about to grab Beanie, the cat hisses and scratches at her."
    eve "Wha...?"
    "Evelyn pushes herself back, but it causes you to lose your balance, and before you know it."
    mc "Whoa!"
    "You back off trying to maintain your balance, and you're actually doing alright until your foot hits one of the roots of the tree."
    mc "Shiiiiiit!"
    eve "Whoaaaa!"
    "You fall back to the ground and Evelyn falls on top of you."
    hide window
    play sound hit
    scene evelyn tree 3 with vpunch
    w ""
    mc "Ow... just not my day."
    eve "Ow is right."
    hide window
    scene evelyn tree 2 with dissolve
    w ""
    mc "{i}Then again, having Evelyn on top of me isn't too bad at all.{/i}"
    eve "Are you ok?"
    mc "Yeah... I'm fine... Just in pain. Again."
    mc "You?"
    eve "Well, you broke my fall pretty well."
    mc "That's... ow... what I'm here for."
    eve "I thought you said you wouldn't drop me."
    mc "Well... considering you're on top of me, and I'm pretty sure my spine is merged with the tree's root, I'm sure I didn't."
    eve "Ok. I'll buy that."
    "She laughs."
    eve "Seriously, I should have known better than to expect anything else."
    mc "What does that mean?"
    eve "Nothing bad. Just... Come on... Did you forget the time you crashed into the tables at the Harvest Festival last year?"
    mc "That was an accident."
    eve "Or the time you nearly set the store on fire..."
    mc "Also an accident."
    eve "Well, you're accident prone."
    mc "Yeah... guess so."
    eve "Ah, look, that came off as mean. I'm not trying to be, I'm just straightforward."
    eve "I do appreciate the help."
    mc "Not at all... It's probably worse for you. Someone might come by and see us like this."
    eve "So?"
    mc "They'd get the wrong idea."
    eve "And that affects me how? Let them think what they want. Rumors are only a problem if you let them be."
    mc "That's... a pretty cool way to look at things."
    eve "Now, come on, we still have to figure out what to do about Beanie."
    "You see a handkerchief sticking out of one of Evelyn's pockets."
    mc "I have an idea."
    eve "What?"
    scene pub exterior day with dissolve
    "You grab the handkerchief and stand up."
    mc "Watch."
    nvl clear
    n "You wave the handkerchief at Beanie. The cat's eyes follow its movements. After some time, you can see Beanie getting more and more excited and she starts pawing at it."
    play sound meow
    n "\"There we go!\""
    n "You finally throw the handkerchief up in the air in front of Evelyn and Beanie pounces, catching it midair. The cat falls into her arms."
    nvl clear
    mc "There you go."
    show evelyn neutral
    eve excited "Wow! It worked."
    mc "Yeah, I just had to make down here more interesting than being scared up there."
    "You pet Beanie, and she purrs."
    eve "She actually likes you."
    mc "I told you so."
    "Evelyn opens the door to her pub and puts Beanie inside."
    play sound meow2
    eve smiling "Thanks again. I don't know what I would have done without you."
    mc "It was easy..."
    eve "Not so easy. I had been at it for an hour before you showed up."
    play sound chicken
    "Your conversation is interrupted by a clucking chicken."
    mc "Oh... Right. I forgot about her."
    eve neutral "Do you need some help? I heard catching chickens is hard."
    mc "Nah! Watch."
    "You walk up to the hen and make eye contact with it; it falls silent and stands still. You pat it on the back, and then pick it up."
    eve excited "Wow! That... How did you do that?"
    mc "A magic spell I learned."
    eve frowning "..."
    mc "Yeah... We have our chickens trained to do that. They will see anyone who does that as a rooster, so they become submissive. It's really easy to move them."
    eve neutral "Huh, you learn something new every day."
    mc "Well, if you want to learn about farming... talk to dad. I just do what he does."
    eve "Hey, don't sell yourself short. You really helped me out today."
    show evelyn neutral at right
    show mc neutral at left

menu EvelynTreeChoice:
    "Anything for a pretty lady":
        hide mc
        show evelyn neutral at center
        mc "Well, how could I say no to someone as hot as you?"
        "Evelyn frowns."
        eve frowning "Not... Not a great line there, [MC]"
        eve "You sound like one of the militia guys..."
        eve "Not a good thing."
        eve neutral "I'll take the compliment though."
        mc "Oh.. Ok."
        $ EveLove += 0
        jump EvelynTreeFinish
    "Always willing to help [gr]\[EveLove +1\]":

        hide mc
        show evelyn smiling at center
        mc "Well, how could I say no to a friend?"
        eve "Ok then, {i}friend{/i}. I'll have to make it up to you sometime."
        mc "You don't have to."
        eve "You're right, I don't. But I want to."
        mc "Thank you."
        eve "No need. I should be thanking you."
        $ EveLove += 1
        jump EvelynTreeFinish

label EvelynTreeFinish:
    eve "Well, I'll see you later, [MC]. This was fun, but I need to get ready to open tonight."
    mc "Yeah. I need to get this chicken back home."
    eve "Hey... Are you going to the party?"
    mc "Pretty sure I am."
    eve "Well, maybe I'll see you there."
    eve "Thanks again."
    "You wave goodbye and walk through the gate."
    mc "{i}OK, let's get you home, chicken.{/i}"
    scene farm_fixed with dissolve
    "You take the chicken back home and drop it off in the coop."
    play sound chicken
    mc "{i}One down, four to go{/i}"
    scene black with dissolve
    jump EliseSophieGarden
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
