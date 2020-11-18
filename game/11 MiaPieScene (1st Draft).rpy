label Day2MiaPieTasting:
    scene village 2 day with dissolve
    play ambient town
    nvl clear
    hide window
    w ""
    n "The early afternoon bustle of the village is in full swing as you walk towards the elder's house."
    n "You spy several militia members helping the new shop owner move boxes into his home."
    n "Several of the younger kids are out making deliveries, and there is a line outside the baker's shop."
    n "As you near the elder's house, you hear a familiar voice."
    nvl clear
    show nina apples
    nin "[MC]!"
    "You turn around and see Nina carrying a basket of apples."
    mc "Hey!"
    nin "What's up?"
    mc "Just heading over to the elder's house."
    nin "What did you do this time?"
    mc "Nothing!"
    nin moreangry "You were probably caught peeping again."
    mc "That has never been proven."
    nin neutral "Yuh-huh."
    "Nina waves her hand at you dismissively."
    mc "Out making deliveries?"
    nin "Yeah. I'm heading to the elder's house too. So it works out."
    nin neutral "By the way, you're going to the party, right?"
    mc "Yeah, that's the plan."
    nin "Good... Don't change your mind..."
    mc "I don't plan on it."
    nin "Great! There's a friend I want you to meet."
    mc "A \"friend\"?"
    nin "Yeah, she's new in town... and I think you'd like her."
    nin "She's really nice!"
    mc "{color=#b7b7b7}{i}Really nice is usually code for troll-faced.{/i}{/color}"
    nin worried "What's that look?"
    mc "Nothing, just remembered some work I have to do. Gotta miss the party."
    nin smiling "I think you'll like her. Trust me."
    mc "Ok, I'll be there anyway."
    scene village 1 day behind nina with dissolve
    "The two of you arrive at the elder's house."
    "You knock on the door."
    play sound knock1
    show elder neutral at slightleft
    show nina neutral at slightright
    eld "Oh, good afternoon, you two!"
    nin apples "Good afternoon, Elder. I brought your apples."
    eld "Why, thank you, dear. Come on in. I just have to get your payment."
    nin "Thank you."
    eld "It's nice of you to keep Nina company on her deliveries, [MC]."
    mc "Actually, I am here to see Mia."
    eld "Of course! Come on in!"
    "The elder enters his home and invites you in."
    "Nina turns to you, in a bit of shock."
    nin worried "I didn't know you were coming to see Mia."
    mc "Didn't I mention it?"
    nin "No..."
    scene elders house with dissolve
    stop ambient fadeout 1
    show nina neutral
    "The two of you enter, and the first thing you notice is the smell of pie."
    nin "Someone's been baking.'"
    "Mia comes in to the room."
    play music afternoon2 fadeout 1
    show nina neutral at slightright
    show mia smiling at slightleft
    mia "[MC]! You made it! I though you might not come."
    mc "Yeah, it just took me a little time to get away from work at home."
    mia "Oh, and Nina's here too."
    nin "We, just ran into each other. I'm delivering apples today."
    mia blushing 1 "That's nice..."
    "Mia looks uncomfortably between you and Nina."
    mc "So how'd the pie making go, Mia? It smells great!"
    mia blushing 2 "Oh! Yes! Um... Thank you."
    mia "Do you still want to try it?"
    "Mia looks uncomfortably at the ground."
    mc "That's why I'm here."
    mia smiling "Great!"
    show elder neutral at center
    show nina neutral at farright
    show mia smiling at farleft
    eld "Well, what are you kids up to?"
    mia "[MC] came to try some of the pie."
    eld "You're going to love it. Mia baked two."
    eld "She was quite excited."
    mia "Elder!"
    eld "Haha! I said too much, didn't I?"
    "He hands a pouch of coins to Nina."
    eld "Here you are, Nina. Thank your father for me."
    nin "Will do, Elder."
    eld "Well, I'm going to my room to do some reading. I'll leave you kids to it."
    hide elder
    show nina neutral at slightright
    show mia neutral at slightleft
    "The elder leaves to his room."
    "The room gets awkwardly quiet for a second."
    nin "Well, that's my cue."
    "Mia turns to Nina."
    mia blushing 1 "Um... I mean... You're welcome to try some too, Nina."
    "Nina is quiet for a moment, then looks at you."
    nin smiling "Nah, I still have some deliveries to make."
    nin "You two have fun."
    mc "You can't stay? That sucks."
    nin angry "No. I should go. You keep her company."
    "Nina's words are sharp and direct."
    mc "{color=#b7b7b7}{i}I wonder what's with her?{/i}{/color}"
    mc "Ok, see you later."
    "Mia smiles at Nina."
    mia "See you later!"
    nin smiling "See you, Mia!"
    "Nina finishes saying her good-byes and leaves."
    hide nina with moveoutright
    show mia neutral at center
    mia neutral "I wonder what was that about?"
    mc "No idea."
    mia smiling "Well, your timing is perfect. The pie should have just finished cooling."
    mc "Well, I for one can't wait to try it."
    mia blushing 1 "Just remember I'm not very good at it, so you might not like it..."
    mc "I'm sure it'll be great!"
    hide mia with dissolve
    "Mia goes in the back to get her pie. She calls out to you from the kitchen."
    mia "I'm kind of nervous to have you eat my pie, but I'm also excited about it!"
    mia "Only the elder has ever eaten it before, and I want another opinion on how it tastes."
    mc "{color=#b7b7b7}{i}Dear goddess. She really has no idea what sexual innuendo is.{/i}{/color}"
    show mia neutral
    mia "Here you go."
    "Mia brings the pie out. It smells different than you expected, and it looks a little weird."
    mia blushing 1 "Is something wrong? Does it smell bad?"
    mc "No! No! Not at all."
    mc "{color=#b7b7b7}{i}Actually the pie smells a little weird now... Maybe it's the insides.{/i}{/color}"
    "It looks edible though."

    "You eat the pie. It doesn't taste bad, but it is a little bit odd. It's savory, but also a little sweet, with a hint of a fishy aftertaste."
    "As you eat it, you feel more energized. It's as if you hadn't been breaking your back working all morning."
    mia "Um..."
    mc "Yeah?"
    mia "How was it? Was it bad? Be honest."
    show mc neutral at left
    show mia blushing 1 at right
menu MiaPieChoice:
    "It's delicious!":
        hide mc neutral with dissolve
        show mia neutral at center with dissolve
        mc "It's delicious."
        mia neutral "R-Really?"
        mc "Yep, it's the best pie I've ever had! It has a unique taste, and the aroma is out of this world too. I want more!"
        mia "Are you just saying that..."
        mc "No... It's really good."
        mia "Come on. You can be honest."
        mc "Ok... Look, I do like it. But it's a little strange at the same time."
        mia "You... You could have just said that."
        mc "I'm sorry. But I really do like it..."
        mc "But..."
        mia "I think only Elder Silas really likes the taste of these berries."
        jump MiaPieTasting2
    "It's not bad... [gr]\[MiaLove +1\]":


        hide mc neutral with dissolve
        show mia neutral at center:
            linear 0.5
        mc "It's not bad. But the flavor of the berries is a little strange."
        mia "Darn it. Elder Silas loves the taste, but I always thought it was a little weird."
        mia "I thought... it might be me."
        mc "I mean, you still did great! And it's the thought that counts."
        mia "Thanks. I'm still learning, but I really wish that I could make a healthy pie that tastes great too."
        mia "But thank you for being honest with me."
        $ MiaLove += 1
        jump MiaPieTasting2

label MiaPieTasting2:
    mia smiling "Oh well, thank you for trying it! It's healthy at the very least. According to the elder's books these berries help restore a man's vitality and performance."
    mc "Wait, what?"
    mia "If the books are right, you can go all night, and still be ready for more. I don't know who does manual labor at night though..."
    mc "No one I know."
    mc "{color=#b7b7b7}{i}I just don't have the heart to tell her she's misunderstanding things.{/i}{/color}"
    mia "Well, maybe I can find some other berries to use."
    mc "Well, if you need help again... let me know."
    mc "It was fun hanging out."
    mia "Yes! I'd love that!"
    "Silas comes out of his room."
    show mia neutral at slightright
    show elder neutral at slightleft
    eld "So, what did you think, [MC]? Is that not the best pie you've ever eaten?"
    mc "Uh... Yes, sir. It was really good."
    eld "I told you he'd like it, Mia."
    "Mia blushes."
    mia blushing 1 "I, uh..."
    eld "So, are you going to the party tonight?"
    mc "You know about that?"
    eld "I know everything around here... I was young too, once."
    eld "I'd tell you stories of the bonfires back in my day... but they're a little blue for young ears."
    mc "{color=#b7b7b7}{i}I can't even imagine him young.{/i}{/color}"
    eld "What about you, Mia?"
    mia blushing 2 "I... think I'll just stay home."
    mc "Wait... Why?"
    mia "I just... I'm not really friends with anyone there."
    mc "You're friends with me right?"
    mia "Well, yes."
    mc "And Nina will be there too. She gets along with everyone."
    mia "I guess so..."
    "You think back to what Nova told you this morning."
    mc "{color=#b7b7b7}{i}She was right... I just need to do it.{/i}{/color}"
    mc "{color=#b7b7b7}{i}It's better than going alone... and maybe she can make some more friends.{/i}{/color}"
    mc "Mia?"
    mia "Yes?"
    mc "Why don't you come with me?"
    mc "We can go together."
    "Mia takes a moment to process what you just said."
    "The elder slips away before you even noticed."
    hide elder with dissolve
    show mia blushing 1 at center
    mia blushing 1 "Um.. Won't it be weird going with me? I'm not popular like you are."
    mc "{color=#b7b7b7}{i}She thinks I'm popular? She really needs more friends.{/i}{/color}"
    mc "Come on! It's just a party, people just want to go an have fun."
    mc "You like fun. I know that much."
    mia smiling "I do."
    mc "So come with me. You can hang out with new people too."
    "Mia smiles."
    mia "Um... Ok. I'd love to go with you."
    mc "Great! So, I still need to finish up some work and get ready. I'll come by before sunset to pick you up."
    mia neutral "Ok, should I wear anything special? I don't really have anything like that."
    mc "You look beautiful as it is, Mia."
    "Mia blushes."
    mia neutral "Th... Thank you."
    mia "I'll see you later, then."
    mc "Later, Mia. Thanks for the pie."
    "Mia walks you to the door, and you walk home."
    jump NovaBath
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
