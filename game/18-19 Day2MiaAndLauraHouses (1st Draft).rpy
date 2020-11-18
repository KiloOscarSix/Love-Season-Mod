label AfterParty:
    stop ambient
    scene village 1 night
    show mia neutral
    play music afternoon2
    "You slowly walk a stumbling Mia back to her front door."
    mia "Thank you for escorting me. You're like a hero from a story. You know that?"
    mc "Hah. Yeah, right. You really are drunk, aren't you?"
    "Mia pouts at you."
    mia blushing 1 "I am so!"
    mia neutral "Wait."
    "You smile at her."
    mc "It's ok. I'm not a hero, though. Just a boring farmer."
    mia "You're not boring!"
    mia "Today was really exciting."
    mia blushing 2 "Thanks to you."
    "Mia blushes."
    mc "I'm glad you had fun."
    mia "I did."
    "Mia stumbles for a second, and you catch her."
    mc "Careful."
    mia smiling "See, you ARE a hero."
    mc "Ok, sure, I'm a hero."
    mia "Good."
    mia "[MC]?"
    mc "Yes."
    mia blushing 1 "Do you think my head will hurt in the morning, like it happens to Silas the morning after a late night in the pub?"
    mc "I'd like to say no... but probably yes."
    mia smiling "Oh well. It's worth it."
    mc "Try to remember that when your head is pounding."
    mia "I will."
    scene mia party kiss with dissolve
    "Mia kisses you on the cheek."
    mia "For my hero. Good night."
    "She blushes."
    scene village 1 night
    show mia blushing 2
    mia "I had fun."
    "You smile as Mia walks inside."
    hide mia with dissolve
    mc "{color=#b7b7b7}{i}Things are going well... Really well...{/i}{/color}"
    mc "{color=#b7b7b7}{i}I mean, I wish it was more than that. But I shouldn't push it, right?{/i}{/color}"
    "You leave the elder's house and look at the nearby store."
    scene black with Dissolve(3)
    mc "{color=#b7b7b7}{i}I guess that's Laura's place now. The lights are off. So she probably got home already.{/i}{/color}"
    scene lauras shop exterior night with dissolve
    lau "You're weird."
    "You turn to see Laura coming up behind you."
    mc "Excuse me?"
    show laura neutral with Dissolve(1)
    play music romance1 fadein 1
    lau "You heard me."
    mc "How am I weird?"
    lau "Well, for one. That scarf."
    mc "Well, maybe I should wear a tube top."
    lau "Hey, that's my thing! Plus, it looks good on me."
    mc "True."
    lau "That scarf though."
    mc "Ok, fine, the scarf. It's not going anywhere, by the way."
    mc "What was the other thing?"
    lau "You had the hottest girl at the party chatting you up, and you just ignored her."
    mc "Did I?"
    lau "You had to take knockers home. I get it."
    mc "Well, her condition was partly your fault from what she says."
    lau "Guilty as charged."
    mc "To be honest, I thought you'd still be at the party drinking it up and teasing Nina."
    lau "Only so much you can do there. The militia guys are all doing their thing, and I don't feel like being arm candy. Nina's off with her beau."
    lau "And your sister left."
    mc "She's not my sister."
    mc "What is it with everyone tonight?"
    lau "Ok, your hot live in maid left."
    mc "I wish she was here just so I could see the look on her face when she heard you say that."
    lau "So it was looking to be a boring end to the night. But then I ran into you."
    mc "If I'm your definition of excitement..."
    lau "Well, in this village you take what you can get."
    "Laura walks to her door."
    lau "I'll call this as you walking me home."
    mc "We walked a few steps at least."
    lau "Good."
    "Laura stands in front of her door, staring at you."
    mc "{color=#b7b7b7}{i}Is she... I mean, I guess I'm supposed to kiss her right now.{/i}{/color}"
    mc "{color=#b7b7b7}{i}But... what if I'm reading things wrong?{/i}{/color}"
menu KissLauraChoice:
    "Go for it! [gr]\[LauraLove +1\]":
        hide window
        scene kiss party 2 with dissolve
        w ""
        "You pull Laura in close to you and kiss her."
        "You pull back, unsure if a slap is coming or not."
        scene kiss party 1 with dissolve
        hide window
        w ""
        "Laura smiles at you."
        lau "Took you long enough. You country boys are too shy."
        lau "If I had to drop another hint..."
        hide window
        scene kiss party 2 with dissolve
        w ""
        "Laura grabs you by the side of the head and kisses you."
        scene kiss party 3 with dissolve
        "Feeling braver, you run your hands down Laura's back and cup her ass."
        "You manage to lift her skirt a bit, and you hands rest on her bare ass."
        mc "{color=#b7b7b7}{i}She's not wearing any...{/i}{/color}"
        hide window
        scene kiss party 1 with dissolve
        w ""
        "Laura backs off from the kiss again."
        lau "I knew I forgot to put something important on."
        mc "I... Uh..."
        "You're at a loss for words."
        lau "Well, stuttering was the effect I was going for."
        $ LauraLove += 1
        jump AfterParty2
    "Better not.":

        "The awkward silence continues for a little while"
        mc "Uh... I'll see you around."
        "Laura looks a little dejected."
        lau "Yeah sure. See you around [MC], nice meeting you."
        "She turns and enters her house."
        jump AfterPartyEnd


label AfterParty2:
    scene lauras shop exterior night with dissolve
    show laura neutral
    lau "That was fun. But it's late. I should get ready for bed."
    lau "Did you have fun?"
    mc "Yeah... definitely"
    lau "You're speaking again."
    "She opens her door."
    mc "Ah. I'll see you later then, I guess."
    scene kiss party 4 with dissolve
    "Laura smiles seductively at you."
    lau "I could actually use a hand with something inside."
    lau "What do you say? Want to come in?"
    mc "{color=#b7b7b7}{i}Wait, is she inviting me in? By the gods! Should I follow her? I mean, I barely know her.{/i}{/color}"


menu LauraSexChoice:
    "[gr]Hell to the yes":
        scene lauras shop exterior night with dissolve
        show laura neutral at center
        jump FuckLaura1
    "This doesn't feel right.":
        hide mc
        scene lauras shop exterior night with dissolve
        show laura neutral at center
        "You have trouble responding, and there is an awkward silence again."
        jump AfterPartyEnd

label FuckLaura1:
    mc "Yeah, of course."
    lau "Good... Come in. I don't want to wake up daddy."
    play sound frontdoor
    scene lauras shop interior
    "You follow Laura in."
    show laura neutral
    lau "Home sweet hovel."
    mc "It's nice."
    lau "Not really, but thanks, I guess."
    "You grab Laura around the waist."
    lau "Relax, I didn't call you in for that."
    lau "I need your help."
    mc "Are you... I mean..."
    lau "I forgot to get the shipping manifest for dad before I left today."
    mc "What? But I..."
    "You sigh."
    mc "So what do I need to do?"
    lau "Downstairs. I need to go downstairs. And I want an escort."
    mc "Why?"
    lau "I mean... The thing is..."
    lau "There are strange noises down there sometimes. I don't like going down by myself."
    mc "The houses around here can get a little creaky. What kind of noises have you been hearing?"
    lau "I don't know... Shuffling and stuff. I never had to deal with this in the city."
    mc "I'm sure it's nothing."
    lau "Look, I know... But I hate going down there by myself."
    "Laura bats her eyes at you."
    lau "Please."
    mc "OK."
    mc "Do we have any lights at least?"
    lau "Yeah. I have a lamp. We'll be ok."
    mc "Lead on, then."
    play sound bedroomdoor

    scene laura fuck 1 with dissolve
    lau "Are you ready? I'll lead the way, it's really dark in there, so be careful."
    lau "Watch your step."
    "You stare at her ass as she walks ahead of you."
    mc "{color=#b7b7b7}{i}Man, she has such a nice ass. And she's totally naked under that skirt.{/i}{/color}"
    mc "{color=#b7b7b7}{i}Even the way she walks is sexy as hell. I just want to grab her and bend her over.{/i}{/color}"
    "You feel yourself getting hard at the thought. The growing tent in your pants is very obvious to you and you try to hide it with your hands best you can."
    scene laura fuck 2 with dissolve
    lau "Is something wrong? You're really quiet right now."
    mc "Nope. Everything's fine. Totally fine. I'm just trying not to fall on those steps..."
    lau "Well, man up. You're my protector here."
    mc "Just keep going. I doubt there's a monster down here, you'll be fine."
    lau "I just want to find that and go."
    "You follow Laura around the basement, grabbing a look at her ass whenever she isn't looking."
    "She suddenly stops."
    lau "Oh, here it is!"
    scene laura fuck 3 with dissolve
    mc "Hey, watch it!"
    "Laura bends over to read the manifest and you bump into her from behind."
    lau "Ah!"
    lau "[MC]! What are you doing?"
    mc "Damn! I'm so sorry! Are you OK, Laura?"
    hide window
    scene laura fuck 4 with dissolve
    w ""
    lau "Watch it! My dad's upstairs!"
    "Your hard on is poking into the soft flesh of her ass. Laura moves up and down on it, moaning slightly."
    mc "{color=#b7b7b7}{i}Wait, is she... rubbing on me?{/i}{/color}"
    lau "He'd freak out if he found out his daughter was being... attacked... by a village boy..."
    hide window
    scene laura fuck 5 with dissolve
    w ""
    mc "{color=#b7b7b7}{i}Is this actually happening? Fuck it! This HAS to be a signal.{/i}{/color}"
    "You push Laura down and she grinds into you. You reciprocate her movements, and you dry hump her. The feeling in your cock is better than you imagined."
    hide window
    scene laura fuck 5C with dissolve
    w ""
    lau "Ah... [MC]... Just."
    hide window
    scene laura fuck 6 with dissolve
    w ""
    "Without saying another word, Laura reaches back and pulls her skirt up, revealing her pink wet pussy."
    hide window
    scene laura fuck 6B with dissolve
    w ""
    mc "{color=#b7b7b7}{i}My heart is racing right now! Fuck! This isn't a dream{/i}{/color}"
    hide window
    scene laura fuck 7 with dissolve
    w ""
    "You stare at her pussy. The drawings in your magazines can't compare to the real thing."
    mc "{color=#b7b7b7}{i}Ah, I feel my cock almost exploding already, that's it, I'm going to fuck Laura! This is almost surreal.{/i}{/color}"
    hide window
    w ""
    lau "Ah..."
    "The moan is the first sound you heard from her since she pulled up her skirt..."
    hide window
    scene laura fuck 8 with dissolve
    w ""
    mc "{color=#b7b7b7}{i}My dick is already touching her pussy! She's so wet! It should slide right in{/i}{/color}"
    "You take stock and hesitate for a moment..."
    mc "{color=#b7b7b7}{i}This can't be that hard, right?{/i}{/color}"
    hide window
    scene laura fuck 9 with dissolve
    w ""
    "You thrust forward, and in an instant your cock is surrounded by her wet pussy."
    lau "OOH! [MC]... That's it... Ah..."
    mc "{color=#b7b7b7}{i}By the gods! This is amazing! Her pussy is on fire! It's like I'm melting.{/i}{/color}"
    mc "Ah! You're so hot, Laura! So tight..."
    hide window
    scene laura fuck 10 with dissolve
    w ""
    "You grab her hair and push yourself even deeper inside her."
    lau "Mmm... You're huge! Fuck me..."
    hide window
    scene laura fuck 11 with dissolve
    w ""
    "Thrusting your hips as fast as you can you're overcome by just how wet and hot her pussy is."
    "Her moans echo in the basement, and that makes you more and more excited."
    mc "{color=#b7b7b7}{i}All I want right now is to make this last but... it feels too good."
    mc "{color=#b7b7b7}{i}Ah, I can't hold any longer!{/i}{/color}"
    hide window
    scene laura fuck 12 with dissolve
    w ""
    mc "I'm cumming!"
    lau "Wait, what? Ah!"
    hide window
    scene laura fuck 13 with dissolve
    w ""
    "Laura shudders as you spray her insides with your cum."
    mc "Ahhh! Holy fuck, I can't stop cumming, this feels way too good!"
    "You feel like you've never cum this much in your life."
    "Once you are done you take a moment to regain your composure."
    hide window
    scene laura fuck 14 with dissolve
    w ""
    lau "Y-you came inside me."
    mc "I... Uh... I'm so sorry. You just felt way too good."
    lau "It's OK, this time... I'll take it as a compliment. But give me a little warning next time, [MC]..."
    scene lauras shop basement with dissolve
    show laura neutral
    mc "Sorry."
    lau "Don't be. It was one of the better first runs. But you need to work on endurance."
    lau "You've got some potential, farm boy."
    "You hear some noise coming from upstairs."
    lau "Shit, that's daddy, I don't think we woke him up... But better safe than sorry."
    lau "There's a cellar door to the outside, take that. I'll see you tomorrow."
    scene lauras shop exterior night with dissolve
    "Laura pushes you out the steps of her cellar door and you find yourself outside before you know it."
    "You realize your cock is still out, and you put it away."
    mc "{color=#b7b7b7}{i}By the gods! I just had sex!{/i}{/color}"
    $ FuckedLaura = 1
    $ NotAVirgin = 1
    $ renpy.end_replay()
    $ persistent.laura_first = True
    jump NinaNight

label AfterPartyEnd:
    lau "So, yeah... Nevermind."
    lau "See you later."
    hide laura with dissolve
    "Laura enters her house. She looks a little dejected."
    mc "{color=#b7b7b7}{i}I think I might have missed out on an opportunity there.{/i}{/color}"
    mc "{color=#b7b7b7}{i}But I barely knew her... What was supposed to happen?{/i}{/color}"
    $ FuckedLaura = 0
    $ renpy.end_replay()
    jump NinaNight
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
