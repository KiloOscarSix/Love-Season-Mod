label NinaAid:
    scene black with Dissolve(2)
    play ambient ringing
    nin "[MC]!"
    scene nina over neutral with Dissolve(0.5)
    scene black with Dissolve(1)
    nin "No... Damn it... Wake up..."
    scene nina over surprised with Dissolve(0.5)
    scene black with Dissolve(1)
    nin "Come on..."
    scene nina over angry with Dissolve(0.5)
    scene black with Dissolve(2)
    stop ambient fadeout 1

    "Through the blackness you hear Nina's voice, but you can't respond."
    nin "Please..."
    nin "Don't do this to me..."
    "You feel something drip on your cheek, and a muffled cry. It' a little strange, but..."
    mc "Jussa... couple'a mins... ok?"

    scene nina over angry with Dissolve(2)
    play music drama2 fadein 1
    "Your vision clears and Nina is staring down at you, tears in her eyes. It's strange, something is clearly upsetting her, but you don't know what it is."
    "When you see her, you're filled with a sense of relief. She's ok."
    scene nina over surprised with Dissolve(2)
    nin "[MC]..."
    mc "Hey... Nina... What's wrong? Did... something happen?"
    scene nina over angry with Dissolve(1)
    nin "What's WRONG? I thought you died!"
    "Nina hits you on the chest, harder than she intended, it seems."
    mc "Ouch."
    "You try to sit up, but Nina presses you down. She wipes her eyes and tries to gain some composure."
    scene nina over neutral with Dissolve(1)
    nin "Don't you move yet... Just rest there. What did you do?"
    mc "What did I? Oh right..."
    "Your fight with the goblin comes back in vivid detail."
    mc "I think I may have... kinda sorta... accidentally... blown myself up."
    nin "Are you crazy?"
    mc "Probably..."
    scene nina over angry with Dissolve(1)
    nin "What were you thinking!?"
    "Her composure vanishing in an instant, Nina screams and slaps your chest."
    mc "OW... Please don't scream."
    nin "You're such an idiot! That goblin could have killed you!"
    mc "I got lucky... But... I wouldn't let it hurt you..."
    scene nina over relieved with Dissolve(1)
    nin "He's dead?"
    mc "He won't bother you again... I promise."
    nin "But he..."
    mc "He's dead."
    nin "I..."
    "You try to stand up but can't quite find the strength."
    scene nina over resolved with Dissolve(1)
    nin "What are you doing? You need to rest..."
    mc "I'm fine..."
    "You wobble for a second using the cave wall to hold yourself up."
    nin "That doesn't look fine!"
    mc "Just... a little sore..."
    scene nina over neutral with Dissolve(1)
    nin "Are you bleeding?"
    mc "Am I?"
    scene nina over relieved with Dissolve(1)
    nin "Well, you're covered in soot... and dirt... and I think some goblin blood."
    mc "See, it's all ok."
    nin "Come on..."
    mc "Where are you going?"
    scene nina over neutral with Dissolve(1)
    nin "{i}We're{/i} going to the pool..."
    mc "I'm fine... Really.'"
    scene nina over resolved with Dissolve(1)
    nin "Now."
    mc "Ok, ok!"
    scene cave indoor pool with Dissolve(2)
    "You follow Nina to the pool, or try to. You stumble for a moment and she helps prop you up for part of the way. Soon enough though you can walk on your own."
    "When you reach the pool you notice your dagger on the ground by a crystal."
    show nina scarf neutral with Dissolve(0.5)
    nin "Come on. Get in the water."
    "You walk towards the pool..."
    mc "Ok..."
    show nina scarf worried with Dissolve(0.3)
    nin "And..."
    "Nina takes a deep breath."
    nin "And... drop your shorts."
    mc "I don't think I need to..."
    nin "Just do it. Once we get you cleaned up... I need to look for wounds."
    mc "You're just trying to see it again, aren't you?"
    show nina scarf angry with Dissolve(0.5)
    nin "For crying out loud... Not now! And since you're healthy enough to make jokes, just scrub yourself off when you get in there."
    mc "Ok..."
    scene nina sex 1 with Dissolve(2)
    "You take off your underwear and enter the pool. The warm water soothes your muscles and you can feel the tension wash away from you."
    "Nina sits at the edge of the water. She very much makes a show of averting her eyes as you scrub off the dirt and grime."
    mc "What?"
    nin "Nothing. Just hold on..."
    scene nina sex 4 with Dissolve(2)
    "Nina sighs and joins you. She comes up behind you and you feel the soft touch of her hands run up your back."
    nin "Let me help you with your back."
    "She rubs down your back with the water, cleaning you up as best as she can. When she reaches your right shoulder, you feel a sharp pain."
    mc "OW!"
    nin "Sorry..."
    mc "What did you do?"
    nin "Nothing! I'm cleaning it but..."
    nin "You've got a pretty bad looking wound here."
    mc "It must have been from when I got thrown against the cave wall."
    nin "It's filled with dirt and I'm not sure what else... but it's gross."
    nin "I need to clean it."
    mc "No other option, is there?"
    nin "This is going to hurt..."
    "You'd always appreciated Nina's honesty, even if it was often blunt. This once, you wish she was a liar."
    "Every time she touches you you want to cry out. The pain is excruciating."
    "Nina cleans out the wound on your shoulder. The pain is immense, but you grit your teeth."
    nin "Are you ok?"
    mc "Yeah... Just a little sting."
    "You grunt."
    nin "Sorry... I wish it didn't hurt so much. I'm almost done."
    "You nod."
    nin "It's actually not too deep... but it was just filled with all sorts of shit so it looked worse than it was."
    jump Disinfect

label Disinfect:
    scene cave indoor pool with Dissolve(2)
    show nina scarf neutral with Dissolve(0.1)
    nin "Ok... Much better. But..."
    mc "But what?"
    nin "I need to do one last thing."
    nin "I'll be right back."
    "Nina starts to walk away and you get up to follow her."
    show nina scarf angry with Dissolve(0.5)
    nin "No... You stay there."
    mc "I'm fine..."
    show nina scarf neutral with Dissolve(0.5)
    nin "You will be if you rest... Just take a seat and relax. I'll be right back."
    hide nina with easeoutleft
    "You do as she says, trying to ignore the throbbing in your shoulder as you do."
    "As you wait, your thoughts drift to her body, her smile... and other things you'd prefer not confronting at this time."
    nin "Back!"
    "She returns, holding a small flask."
    show nina scarf neutral with Dissolve(0.5)
    nin "Trevor gave this to me last night... Didn't get too much chance to drink."
    mc "You don't have to lie to me, drunkie!"
    show nina scarf laughing with Dissolve(0.5)
    nin "Yeah, that's me. Brooke better watch out!"
    mc "Ha!"
    show nina scarf neutral with Dissolve(0.5)
    mc "I wouldn't mind getting wasted right now, but that look on your face tells me that's not the plan."
    "Nina points at the ground."
    nin "Lie down with your back to me and just stay still..."
    "You follow her directions and Nina gets on top of you."

    scene nina sex 5 with Dissolve(2)
    hide window
    w ""
    play music drama fadein 1
    if Whiner == 1:
        mc "This is going to hurt again, isn't it."
        nin "Worse if you don't stop complaining."
    "You nod and Nina pours some of the alcohol over the wound."
    "You hiss as you feel the alcohol burning."
    nin "You ok?"
    mc "Compared to you poking around this is nothing."
    nin "Good. Now..."

    scene nina sex 5-2 with Dissolve(2)
    hide window
    w ""
    "Nina shifts on top of you and you feel a splash of alcohol on your back."
    mc "What are you doing back there..."
    nin "Just... disinfecting the bandage."
    "Nina binds your wound tightly, and as you look at your shoulder you realize she used your scarf as the bandage."
    nin "That should be good."
    mc "Yeah..."

    scene nina sex 6 with Dissolve(2)
    hide window
    w ""
    "You sit up and take a deep breath. When you turn around you expect Nina to be covering herself, but she's not."
    "She blushes."
    nin "I think you're cleaned up pretty well."
    mc "So that was the only thing that worked as a bandage?"
    nin "Only thing here... That or the panties. But like I said, I liked those."
    mc "{i}She's not even covering herself up. It's like she's trying to... No way. That's crazy.{/i}"
    mc "Uh... Thanks."
    nin "Why are you thanking me? You..."
    mc "Nina..."
    nin "First the bridge... then the goblin..."

    scene nina sex 7 with Dissolve(2)
    hide window
    w ""
    "Nina embraces you tightly. You can feel her shiver as she does so. The hug is not about friendship, or even love... It's about desperation and relief. "
    nin "Maker! I almost died twice... and you..."
    mc "Hey... Relax. You're ok. So am I."
    nin "I know, I know... but... we're still stuck here... The storm's still going."
    nin "There could be other monsters..."

    mc "Hey... I would never let anything happen to you. I'll blow myself up as many times as necessary to keep you safe."
    nin "You asshole..."
    nin "I thought I... I thought you were dead. When I saw you on the ground..."
    nin "I've never been so scared..."
    scene nina sex 8 with Dissolve(2)
    hide window
    w ""
    "Nina looks up to you and you lock eyes."
    "Her eyes are red from the tears, but the look you share moves beyond that. It's filled with regret and all the feelings either fear or lack of understanding stopped you from articulating."

    scene nina sex 9 with Dissolve(2)
    hide window
    w ""
    "Nina kisses you softly on the lips."
    "It lingers a moment and threatens to become something more, when Nina backs away."
    scene nina sex 10 with Dissolve(2)
    hide window
    w ""
    nin "I... I shouldn't have..."
    nin "I..."
    scene nina sex 11 with Dissolve(2)
    hide window
    w ""
    "You grab her by the arms and kiss her more fully. She returns the kiss wrapping her arms around you tightly."
    "When it's over, the two of you share an awkward silence."
    scene nina sex 10 with Dissolve(2)
    hide window
    w ""
    "Nina stares at you, unmoving."
    mc "{i}Should I have done that? She backed away, and she's still with someone...{/i}"
    mc "I'm sorry Nina, I don't know what came over me but..."
    jump NinaSex

label NinaSex:

    scene nina sex 11 with Dissolve(2)
    hide window
    w ""
    "Nina kisses you again, hungrily."
    "You hug her closely and feel her nipples against your chest."
    "Any chance of you two stopping, if it ever existed, has now passed."
    "She sucks on your lip, then each of your tongues dance with the others in the kiss."
    scene nina sex 12 with Dissolve(2)
    hide window
    w ""
    "You reach up her back, then run one of your hands forward to cup her breast."
    "Nina groans."
    nin "[MC]..."
    "Thinking you might have gone too far, you relax your grip on her breast."
    "But Nina holds your hand in place."
    scene nina sex 13 with Dissolve(2)
    hide window
    w ""
    "You place her on the soft ground and kiss down her neck to her chest. She tenses as your lips arrive at her pink peaks and you take one into your mouth."
    "You feel her nipple harden."
    nin "Ahhh."
    "Nina sighs."
    "You flick your tongue as you suck on her, alternating from breast to breast."
    "This is Nina, the girl you have known since diapers. One you never imagined, or rather had never believed would be here, with you, about to make love."

    scene nina sex 14 with Dissolve(2)
    hide window
    w ""
    "You stop licking her tits... Nina is breathing heavily... and she looks up at you."
    "She takes your cock in her hands and holds it gently as if she's trying to get used to the feel of it."
    "You kiss her again and reach down to her panties. You pull them down, but they catch a bit."

    scene nina sex 15 with Dissolve(2)
    hide window
    w ""
    "Nina giggles and lifts her legs in the air and slides off her panties. They catch a bit again but she is far more experienced at their removal than you are."
    "You can't stop yourself from staring."

    scene nina sex 16 with Dissolve(2)
    hide window
    w ""
    "You run your fingers up her legs feeling goosebumps form on her legs in their wake."
    "You're not touching her maidenhood just yet, instead enjoying the smoothness of her skin, the feel of her body heat, the shuddering of her breath."
    nin "Mmm... That..."
    scene nina sex 17 with Dissolve(2)
    hide window
    w ""
    "You spread her legs and truly take in her full beauty for the first time. Your eyes are drawn to her perfectly smooth pussy, open, wet... and inviting."
    "Nina sees the hunger in your eyes and nods, before looking away."
    nin "Go ahead... I'm... I trust you..."
    scene nina sex 18 with Dissolve(2)
    hide window
    w ""
    "Willing yourself to take things slowly, you massage the outside of her pussy, softly. As your fingers brush along her lips she sharply inhales, then when you press on the small bump at the peak of her sex she lets out a loud cry of pleasure."
    "You keep rubbing the nub with your thumb and slip your pointer finger into her pussy."
    nin "AAAH!"
    mc "Oh, crap! Did I do something wrong?"
    scene nina sex 19 with Dissolve(2)
    hide window
    w ""
    "Nina shakes her head."
    nin "Keep going..."
    "Following her instructions you intensify your rubbing while slowly moving your finger in and out."
    nin "[MC]!"
    "The volume of her cry shocks you. You stop your motions."
    scene nina sex 20 with Dissolve(2)
    hide window
    w ""

    "Nina's body is flushed. She catches her breath."
    "You capture her lips with yours again, and again you taste her tongue. Nina reaches down and grips you again, her soft fingers filling you with even greater lust."
    scene nina sex 21 with Dissolve(2)
    hide window
    w ""
    "Nina wraps her arms around your back and pulls you closer in. She breaks off the kiss and says nothing. She slides your cock along her outer lips. You are fairly certain you know what she wants."
    mc "Ah..."
    mc "Nina... Are you sure..."
    scene nina sex 22 with Dissolve(2)
    hide window
    w ""
    "Nina remains silent, staring."
    nin "I... just... You'll be gentle, right? You know I..."
    "You nod."
    scene nina sex 23 with Dissolve(2)
    hide window
    w ""
    "You climb over her and place yourself against her lips. Her wetness spreads over the head of your cock."
    "Nina nods."
    "You lock eyes with each other and you push in."
    scene nina sex 24 with Dissolve(2)
    hide window
    w ""
    nin "Nngh..."
    "You feel your head surrounded by her warm flesh."

    scene nina sex 25 with Dissolve(2)
    hide window
    w ""
    nin "You can... go on..."
    "You press in more."

    scene nina sex 26 with Dissolve(2)
    hide window
    w ""
    nin "Aaah!"
    "Your cock slowly works its way further into her tight pussy."

    mc "I... oh my god..."
    scene nina sex 27 with Dissolve(2)
    hide window
    w ""
    nin "Is it all in?"
    "You shake your head."
    mc "Not yet."
    scene nina sex 28 with Dissolve(2)
    hide window
    w ""
    "Nina looks down and sees that there's a lot of you to go."
    nin "Oh..."
    "You stop to let her adjust."
    nin "Ah... just... do it..."
    "Nina holds her breath and you do as she asks. You pull back slightly then bring your hips forward in one full thrust."
    scene nina sex 29 with Dissolve(2)
    hide window
    w ""
    nin "Ngh...AAAH!"
    mc "Nina..."
    nin "Ow! Ahh... ha..."
    scene nina sex 30 with Dissolve(2)
    hide window
    w ""
    "She looks up at you and gives you a weak smile."
    mc "Are you ok?"
    nin "I'm fine..."
    nin "It stings a bit... but... keep going."
    scene nina sex 31 with Dissolve(2)
    hide window
    w ""
    "You kiss Nina and begin to move your hips slowly."
    "Her taut insides grip you as you move."
    nin "Ah... slow... like that... it's..."
    mc "{i}She's so tight... So intense.{/i}"
    nin "Mmm..."
    scene nina sex anim with Dissolve(2)
    hide window
    w ""
    "You lose yourself in the pleasure of fucking Nina. Each thrust in and out causes you to moan."
    "Your best friend raises her hips to meet yours."
    nin "It's... starting to feel..."
    "Nina bites her lip as continued new sensations rush through her."
    nin "You can go faster..."
    "You didn't need extra motivation. You thrust faster and hear Nina cry out as you do."
    nin "[MC]!"
    scene nina sex anim fast with Dissolve(2)
    hide window
    w ""

    "You see the face of your best friend, eyes shut in pleasure due to your lovemaking."
    mc "{i}I never thought... this could happen...{/i}"
    mc "{i}She's my best friend... I've known her my whole life... and now...{/i}"
    "Nina's gasps are becoming shorter and you realize that yours are as well."
    "You speed up more as you feel your climax approaching."
    scene nina sex 32 with Dissolve(2)
    hide window
    w ""
    mc "{i}I want to keep going... This feels so good...{/i}"
    mc "{i}Oh gods! I'm going to cum soon... I need to... hold off as much as I can...{/i}"
    scene nina sex 33 with Dissolve(2)
    hide window
    w ""
    "Nina locks eyes with you, and all thoughts leave your mind..."
    if NinaLove > 7:
        nin "I love y... AAAAH!"
    "The raw pleasure of the moment finally overtakes you. You're about to cum."

menu PullOut:
    "Pull out!":
        scene nina sex 34 with Dissolve(2)
        hide window
        w ""
        "With every bit of willpower you can muster you pull out of Nina and explode on her chest."
        mc "Nina, I..."
        scene nina sex 35 with Dissolve(2)
        hide window
        w ""
        mc "AAAH!!"
        "Nina looks up at you with shock at the sheer volume of your orgasm. Her chest, now painted white, drips with the evidence of your lovemaking."

        $ CumInNina = 0
        jump NinaSex2
    "Cum inside! [gr]\[CumInNina\]":

        scene nina sex 37 with Dissolve(2)
        hide window
        w ""
        mc "{i}I can't control it anymore... It feels too good.{/i}"
        mc "Nina! I'm going to..."
        scene nina sex 38 with Dissolve(2)
        hide window
        w ""
        "Nina wraps a leg around your ass and pulls you in for one last kiss. Your hips don't stop moving as you reach your full..."
        mc "AAAAH!"
        "Your kiss continues as you make one last thrust and empty yourself into her tight hole."
        "You pull out and your cum starts to leak out of her. She lets out one last moan as you do."
        $ CumInNina = 1


label NinaSex2:
    if CumInNina == 0:
        scene nina sex 36 with Dissolve(2)
        hide window
        w ""
    else:
        scene nina sex 39 with Dissolve(2)
        hide window
        w ""
    nin "Ah... ah... ha..."
    "Nina is still breathing heavily."
    "You collapse next to her."
    nin "Hmmm..."
    scene nina sex 40 with Dissolve(2)
    hide window
    w ""
    nin "That was... nice..."
    mc "Yeah it... really was."
    "Nina hugs you closely."
    nin "I... didn't expect that..."
    mc "I guess I didn't either..."
    nin "You were... "
    "Both of you remain silent for a few minutes. Nina turns to you after her extended silence."
    scene cave indoor pool with Dissolve(2)
    show nina naked neutral with Dissolve(0.1)
    nin "Um..."
    mc "Yeah?"
    nin "We should... probably move stuff back to the camp..."
    mc "Yeah... I guess."
    nin "Let me clean up first... ok?"
    mc "Are you..."
    nin "I'm perfect. Alittle sore, but... I just want to clean up."
    scene nina sex 41 with Dissolve(2)
    hide window
    w ""
    "She walks into the pool."
    "You look down and see a fresh bloodstain in the sand and some dried blood on your cock."
    mc "{i}Wow... I'd heard about it... but...{/i}"
    "You look up and follow her."
    scene nina sex 42 with Dissolve(2)
    hide window
    w ""
    "Nina glances over her shoulder"
    nin "Didn't get enough?"
    mc "I wanted to clean up too and well... it'll save time."
    nin "Heh. Ok."
    "You get into the water and scrub yourself. Nina stays a bit away from you as she gets the cum and dirt off of her body."
    "After a minute she comes back, nervous again."
    scene nina sex 43 with Dissolve(2)
    hide window
    w ""
    nin "Um, [MC]?"
    mc "Yeah?"
    nin "Nevermind..."
    mc "You can ask."
    nin "Was I...?"
    nin "Forget it, it was a dumb thought! Just... take your time."
    mc "{i}It got awkward all of the sudden.{/i}"
    scene cave indoor pool with Dissolve(2)
    hide window
    w ""
    "Nina gets out of the water, takes the flask and heads back to camp."
    mc "{i}Is something bothering her?{/i}"
    "You finish washing and follow her soon afterwards."
    $ renpy.end_replay()
    $ persistent.nina_first = True
    scene cave campsite with Dissolve(2)
    hide window
    w ""
    play ambient caverain
    play ambient2 fire
    "When you return to the camp you don't see Nina anywhere."
    mc "{i}It's still raining... I don't think she's outside.{/i}"
    mc "{i}I don't see her clothes...{/i}"
    mc "{i}Maybe she went to get something else.{/i}"
    mc "{i}Or maybe she doesn't want to see me.{/i}"
    nin "Hey! You're back!"
    "Nina comes into the cave. She's fully dressed."
    show nina neutral with Dissolve(0.5)
    mc "Oh! Hi."
    "You try to not be awkward."
    nin "Our clothes are dry! So no more naked stuff."
    mc "That's good..."
    nin "I think I did an OK job fixing up the fire."
    mc "Well... You could have stacked it a bit better. But not bad for a beginner!"
    nin "The campfire king has to show off again..."
    mc "Ha ha!"
    show nina smiling with Dissolve(0.5)
    nin "Come on, I'm starving. We worked up quite an appetite today."
    mc "Patience, young Nina."
    "The new fire springs to life."
    mc "Perfect."
    nin "Great. Now out of the way. Let's see if I can cook these up so they don't taste like butt."
    mc "Here's hoping."
    show nina angry with Dissolve(0.5)
    nin "And get dressed already."
    "You put on your clothes as Nina fixes the mushrooms."
    "After some time..."
    show nina smiling with Dissolve(0.5)
    nin "We're done."
    mc "Awesome!"
    "You grab one of the roasted mushrooms."
    nin "Well... Try it..."
    mc "Have you tasted them yet?"
    nin "No... Because you're the taster. I want to know what I'm in for."
    mc "Well, If I get sick..."
    nin "Then I'll take it as an insult to my cooking."
    "You take a bite of the mushroom. It's slightly burnt, but other than that it's bland and inoffensive."
    show nina worried with Dissolve(0.5)
    show nina worried at farright
    show mc neutral at left with Dissolve(0.5)
    nin "So?"

menu MushroomGood:
    "Bland... but filling.":
        hide mc
        show nina at center with Dissolve(0.5)
        mc "Bland, but it's edible... and as hungry as I am, it's like the best mushroom in the world."
        show nina smiling with Dissolve(0.1)
        nin "I'll take bland over butt any day."
        mc "Good job."
        nin "I held them over the fire, not like I baked a pie or anything."
        mc "Still, my compliments."
        jump DinnerTalkCave
    "Best mushrooms ever!":

        hide mc
        show nina at center with Dissolve(0.5)
        mc "Amazing! They're going to be a new taste sensation."
        show nina crossing with Dissolve(0.5)
        nin "That bad? Sorry. But you didn't have to make fun of me."
        mc "Just having some fun. They're fine... just bland."
        show nina smiling with Dissolve(0.5)
        nin "I'll take bland... "
        nin "Dick."
        jump DinnerTalkCave

label DinnerTalkCave:
    "The two of your dig into the pile of mushrooms Nina cooked up. The rain continues to pour outside of the cave."
    show nina neutral with Dissolve(0.5)
    nin "Well, at least it's a bland you can get used to."
    mc "Yeah, that's true."
    "You take another mushroom from the pile."
    mc "And they're filling at least."
    nin "No doubt."
    mc "{i}She still hasn't said anything about what we did...{/i}"
    show nina worried with Dissolve(0.3)
    nin "What is it?"
    mc "Nothing."
    "Nina sighs, and you're not sure she believes you."
    "She pulls the flask out of her overalls."
    show nina smiling with Dissolve(0.3)
    nin "You look like you need a drink."
    mc "There's a look for that?"
    nin "You'll join me?"
    mc "Uh... Sure."
    scene nina after sex 1 with Dissolve(2)
    "Nina takes a swig of the flask, coughs, and passes it on to you."
    nin "It's pretty strong."
    "You drink from the flask and cough."
    if DrinkOn == 0:
        mc "What the hell is that?"
    else:
        mc "God... That's..."
    nin "Darius' special reserve, or so I'm told."
    if DrinkOn == 1:
        mc "Yeah... The same shit Brooke had."
    mc "That shit is going to blind us!"

    "Nina sits next to you and put her head on your shoulder."
    nin "I..."
    nin "It's kinda nice seeing you react like that."
    mc "Coughing up wood alcohol?"
    nin "Just... That way I know it's still you."
    mc "What does that even mean?"
    nin "I don't know, I just... know it's still you."
    mc "You said that twice now."
    nin "What do you want me to say? You've done stuff... protected me. I always thought I was the strong one."
    mc "You still are. You patched me up."
    mc "And without you that goblin would have killed me!"
    nin "Yeah, I know, but..."
    nin "There's times you seem different and it worries me, but I talk to you... and it's still you. Does that make sense?"
    mc "Not really?"
    nin "That's OK. But tonight? You were great... crazy... naive... And did I mention crazy?"
    mc "Thanks?"
    "The rain outside stops."
    stop ambient fadeout 1
    nin "Finally."
    mc "Heh, I guess that means we can go home tomorrow!"
    nin "No more cave! I'll be happy with that. I miss my bed!"
    mc "Hah. I miss mine too. Heck... I even miss dad complaining all day."
    mc "Or [Nova] playing her stupid tricks."
    nin "Hard to beleive it's only been a day here. It feels like a week."
    mc "Tell me about it."
    nin "So... besides sleeping, what's the first thing you're going to do when you get home?"
    mc "I don't know."
    mc "After this I think farming's going to be even more boring, though."
    nin "You'd rather run for your life than plant seeds? Are you serious?"
    mc "I didn't say that, but..."
    mc "You know I've never really liked the farm life."
    nin "But... it's your thing!"
    mc "... I had this dream a couple of nights ago..."
    nin "And?"
    mc "It was about a mermaid."
    nin "I don't need to know your wet dreams."
    mc "It wasn't!"
    mc "I also dreamed of a sorceress, and a sword. And she told me to seek my destiny."
    nin "It sounds like you snuck something out of the larder before bed."
    mc "Well, yes I did, but the dream was still different."
    mc "Ever since then..."
    mc "I felt different. Like I can do things I never did before."
    nin "Look... A lot has happened, it's been a rough day and..."
    nin "You're just overthinking it. If it had been a normal day you'd barely remember the dream."
    mc "I guess."
    nin "Come on, we'll go home tomorrow and everything will be back to normal!"
    nin "This whole cave thing... it'll be just a memory."
    mc "What about..."
    "Nina takes another swig of alcohol."
    nin "What about what?"
    mc "What happened between us."
    nin "Yeah... don't you think it has to be?"
    mc "I don't know..."
    nin "I'm glad you were my first, [MC]... I'd been so insecure about sex for so long, but you... you made me feel so comfortable."
    nin "I didn't expect it, but it makes sense that it happened, right? I think we've both been denying some feelings for a long time now."
    mc "You're probably right..."
    "Nina smiles at you softly."
    nin "Duh, of course I am!"
    mc "I guess our families were right then... about us?"
    nin "Maybe. but I'm not going to give grandma the satisfaction!"
    nin "And I don't think dad would like you too much anymore if he found out you despoiled his little girl."
    mc "Your dad's a teddy bear."
    nin "HA! You should have seen the murder in his eyes when I brought Trevor over for the first..."
    "Nina falls silent."
    mc "{i}Oh, yeah, I almost forgot about him...{/i}"
    mc "Nina?"
    nin "I..."
    "Nina pauses and looks at you. She tries to stay stoic, but her eyes are watering."
    nin "I... I can't tell him. It would hurt him a lot."
    mc "Oh."
    nin "This was a one time thing, right?"
    mc "..."
    "You try to respond, but the words catch in your throat."
    nin "Trevor and I just started seeing each other... I still like him... That hasn't changed."
    mc "I get it, Nina."
    if TrevorFriend == 0:
        mc "I don't have to like it."
        nin "Come on, [MC]..."
    else:
        mc "He's an okay guy... Even if he rubs me the wrong way."
        mc "But I still don't know."
    nin "Hey, don't get all judge-y on me. It's not like you don't have prospects."
    if FuckedLaura == 1:
        nin "Mia is totally into you."
        nin "And let's not forget Laura either... You dog!"
    else:
        nin "Mia's totally into you, you know."
    nin "[MC], you're my best friend, but we're not dating. Not that you'd even want that... Right?"
    mc "How am I supposed to know? Usually the sex thing is supposed to be a decent indicator."
    nin "It can just be sex too..."
    nin "Maybe the best way to look at it is as a really nice dream. One I'm not going to forget."
    mc "Well, I am a dreamboat."
    nin "I'll pretend you didn't say that."
    nin "You're my best friend, [MC], what happened happened for a bunch of reasons that... heck, I can't even begin to explain!"
    nin "But..."
    nin "More than anything, I want to make sure I don't lose our friendship."
    nin "And that's what we are, right? Friends?"

menu AgreeWithNina:
    "No [gr]\[NinaProposition\]":
        mc "..."
        mc "What if we wanted to try something else?"
        nin "[MC], that's the booze talking, and you know it! And if it's not, I... I can't."
        nin "I'm sorry. Maybe if I wasn't with Trevor."
        if NinaLove > 8:
            nin "It would be nice though... if things were different."
        mc "{i}I can't argue. She's right, I guess. But why is that bothering me?{/i}"
        $ NinaProposition = 1
    "Yes":
        mc "You're right. I woudn't want things to be weird."

label Day3Bedtime:
    nin "That means..."
    nin "After tonight, it's done. OK?"
    mc "It's for the best."
    nin "We should get some sleep then."
    "Nina sets the empty flask on the ground, and you both lie down next to each other."
    scene nina after sex 2 with Dissolve(2)
    hide window
    w ""
    "Nina hugs you and places her head on your chest."
    if NinaLove > 8:
        nin "[MC]..."
        "You turn to her."
        "She kisses you softly."
        nin "Good night..."
        mc "Good night."
    "You embrace Nina and the two of you drift off to sleep."
    jump Day4WakeUp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
