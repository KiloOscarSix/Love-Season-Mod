label Day11WakeUp:
    scene blackout with Dissolve(2)
    play music morninghappy
    "You wake up alone in bed the next morning."
    scene farm bedroom with Dissolve(2)
    mc "[Nova]?"
    mc "{color=#b7b7b7}{i}Where's she? Did I sleep in again?{/i}{/color}"
    "You dress yourself and head out to the kitchen. [Nova] is there preparing breakfast."
    scene farm kitchen with Dissolve(2)
    show nova neutral with Dissolve(1)
    nov "Morning, sleepyhead."
    mc "Morning. You could have woken me up."
    nov "I know, but you were sleeping so soundly."
    mc "So, uh..."
    nov "What?"
    mc "About last night..."
    nov "We discussed it already. Stress relief."

menu StressRelief:
    "Yeah, stress relief.":
        mc "Right, just stress relief."
        nov "We had some fun and yeah, it's a little weird, but we don't have to make a big deal out of it."
        mc "Yeah, it doesn't have to get weird... er, between us."
        nov "Exactly."
        mc "{color=#b7b7b7}{i}Will this become a regular thing now, though? I want to know but I don't want to ask her.{/i}{/color}"
    "I think it was more than that. [gr]\[Nova Love +2\]":

        $ NovaLove += 2
        $ NovaMore = 1
        mc "I think it's more than that. I mean..."
        nov "Breakfast is almost ready."
        mc "..."
        nov "I need to finish cooking, you can sit and wait."
        mc "[Nova]. We need to talk about this."
        show nova annoyed with Dissolve(0.2)
        nov "We don't, OK? It was fun, that's it. Don't make it more than that, we don't have to make a big deal out of it."
        mc "... OK."
        mc "{color=#b7b7b7}{i}Will this become a regular thing now, though? I want to know but I don't want to ask her.{/i}{/color}"

label Day11MiaArrive:
    play sound doorknock
    "You hear a knock at the door."
    scene farm house interior with Dissolve(2)
    "As you walk towards the door, Mia walks in."
    show mia neutral with Dissolve(1)
    mc "Oh, hey Mia!"
    mia "Hi!"
    "[Nova] calls out from the kitchen."
    nov "Hey Mia!"
    mia "Hiii!"
    "Mia gives you a hug."


label Day11MiaCheckUp:
    mia "So, how's Mr. Redd today?"
    mc "I think dad's still sleeping."
    "You follow Mia into your father's room."
    scene farm redd room with Dissolve(2)
    show mia neutral with Dissolve(1)
    mia "I doubt it - he likes to pretend he's asleep so he can eavesdrop."
    dad "Nonsense. I am sleeping perfectly soundly right now."
    mc "You called it, Mia."
    mia "Good morning, Mr. Redd!"
    show mia neutral at slightleft with easeinright
    show father neutral at slightright with Dissolve(1)
    dad "Looking lovely as usual, Mia. This big lug hasn't been a problem, has he?"
    mia "No, not at all."
    dad "Don't be afraid to kick his butt."
    mc "Stop teasing her, dad."
    dad "You won't let me out of bed, I need to have fun somehow."
    mia "It's OK."
    dad "So, what's the verdict, did Silas say anything?"
    mia "Another few weeks until full recovery."
    mia "Is your muscle weakness going away?"
    dad "What weakness? I can walk perfectly well and lift more than this one can."
    mc "No, he can't."
    dad "Quiet, son."
    mia "Just keep resting, I know it seems hard but you'll be good as new soon enough."
    dad "Bah! Fine."
    "Nova calls out from the kitchen."
    nov "Soup's on!"
    mia "Well, I should get going."
    nov "I heard that, Mia! You're staying for breakfast!"
    nov "And before you say no, I can outrun you!"
    "Mia smiles and goes to the kitchen."
    hide mia with Dissolve(1)
    mia "OK. I know better than to run away from you."
    show father neutral at center with easeinright
    dad "She's feeling really comfortable around the house, heh? Like she belongs here already."
    mc "Yeah..."
    mc "Well, I'll bring you some soup before I eat. Be right back."
    scene blackout with Dissolve(2)
    "You get your father some soup and go back to the table with the girls."


label MiaPartyAsk:


    scene farm kitchen with Dissolve(2)
    show mia neutral at slightright with Dissolve(1)
    show nova neutral at slightleft with Dissolve(1)
    mc "So, you really think dad will be out of it for a few weeks?"
    mia "According to the elder, the Venomair causes nerve damage and the energy of the Azureola reverses it over time."
    mc "In the stories the antidote just WORKS."
    mia "I wish it were like that."
    nov "Yeah, I can't wait to get some help around the farm cuz this guy's good for nothing."
    mia "Hey, don't be so cruel, he's helping around the town!"
    show nova smirk with Dissolve(0.2)
    nov "Sorry, won't smack talk your boyfriend again."
    show mia blushing 2 with Dissolve(0.2)
    mia "..."
    mc "Damn it, [Nova]."
    nov "Relax! I'm just screwing around."
    mia "Mmhmmm..."
    show nova neutral with Dissolve(0.2)
    nov "You're coming to the party tonight, Mia?"
    show mia neutral with Dissolve(0.2)
    mia "Um... I don't know. The last one was fun, but there will be a lot of attention on us this time."
    mc "Yeah, but we are all the guests of honor."
    nov "Which is weird."
    mia "I know."
    show nova smirk 2 with Dissolve(0.2)
    nov "You guys should go together."
    mc "[Nova]..."
    show mia blushing 2 with Dissolve(0.2)
    nov "Hey, save it for someone who didn't watch you two go at it like wererabbits."
    nov "Anyway, my work here is done, see you guys later!"
    "[Nova] finishes eating and rushes outside."
    hide nova with easeoutleft
    show mia blushing 2 at center with easeinright
    mia "[Nova] is..."
    mc "Hard to deal with sometimes."
    mia "He-he! Yeah. I love her, but she can be a bit nosy."
    mc "{color=#b7b7b7}{i}I think she's doing this because of what happened last night...{/i}{/color}"
    mc "But hey, she has a point... Do you want to go with me? It doesn't have to mean anything, but... I don't know, I'd like to spend more time with you."
    mia "Sure! It's been all work lately, it'll be nice to hang out as we used to."
    mc "Deal. I'll pick you up at your house, then."
    show mia neutral with Dissolve(0.2)
    mia "Hey, I have an ideia! Why don't you come a bit early and I'll make you another pie? I kinda own you a better pie after the last one and I'm dying to try this Spiked Fruit I found in the forest that day! They are super rare and people say they're, delicious."

    mc "Hell yeah! A Spiked Fruit pie made by Mia? Count me in! I'd love that."
    mia "It's a date then, can't wait for it! See you later, [MC]!"
    "Mia finishes her plate and you walk her to the door."
    scene farm fixed with Dissolve(2)
    show nova neutral with Dissolve(1)
    nov "Hey, did she leave already? Damn, you sure are slow..."
    mc "Shut up, we're going together to the party as you suggested, but it's not like we're dating."
    nov "She's such a cutie, but you'd think she'd be less shy considering how crazy she gets during sex..."
    mc "We're even more out in the open than usual now?"
    nov "What's the point in being circumspect? You already blew a load on me."
    mc "Which we said we weren't gonna discuss!"
    nov "We weren't gonna make a big deal about it. There's a difference."
    mc "You're crazy, you know that?"
    nov "Anyway, going out already?"
    mc "Yeah, I'm going to Elise's house to help her out."
    show nova smirk with Dissolve(0.2)
    nov "Oh, you'll help her... What's your deal with the old lady anyway? Are you fucking her too?"
    mc "What?! She's not old!"
    nov "Old enough to be your mother."
    mc "A YOUNG mother."
    nov "So you ARE fucking her. Oh my God, [MC]!"
    mc "Oh, shut your mouth! See you at the party."
    stop music fadeout 2

label EliseDouble:
    play sound walkgrass
    scene elises garden with Dissolve(2)
    play sound doorknock
    "You walk to Elise's house and knock on her door."
    play sound frontdoor
    mc "Good morning, Elise! I was wondering if you..."
    show elise neutral new with Dissolve(1)
    play music elise
    mc "Wow, you changed your hair! Looking good!"
    eli "Did you like it? Thank you! I think I'm already looking so much younger now and we barely started the... treatment. It's so amazing! Thanks for helping me out, [MC]."
    mc "My pleasure!"
    eli "We should continue it as soon as possible! You promised me a double dose, remember?"
    eli "It's hard doing it here with my daughter in the house, though. Maybe if you could sneak into my bedroom without being noticed... I'll follow you there if you manage to do it!"
    mc "No problem, I can do it! See you there."
    stop music fadeout 2
    play sound walkinside
    scene elises house with Dissolve(2)
    "You enter Elise's house before her and start going upstairs."
    mc "{color=#b7b7b7}{i}Darn... If Sophie catches me here I don't even know what I'll say to her to justify me being here alone...{/color}{/i}"
    "You see Sophie's door closed and relax a bit."
    mc "{color=#b7b7b7}{i}She's probably still sleeping... It's not that early, but she does like to party, after all.{/color}{/i}"
    scene elises bedroom with Dissolve(2)
    mc "{color=#b7b7b7}{i}Got it!{/color}{/i}"
    "You wait for about 5 minutes alone until you hear footsteps approaching. The door opens and you see Elise sneaking in."
    play music sexytime
    scene EliseDouble01 with Dissolve(2)
    hide window
    w ""
    eli "You made it! Good job, [MC]. So, should we begin? I got a surprise for you this time. Wanna see what I'm wearing under my dress?"
    mc "Hell yeah!"
    scene EliseDouble02 with Dissolve(2)
    hide window
    w ""
    mc "Wow, Elise! You're looking so sexy in those!"
    eli "Right? I'm feeling so good and young again, I wanted to try some lingerie for a change. I'm wearing this one specially for you!"
    mc "Oh, my! I'm happy to know you're thinking of me like this!"
    eli "Hm... maybe more than I should. Thinking about a young man all the time... I can't wait to do this with you, I've been wearing this for a long time now, waiting for you."
    mc "Thinking about me all the time, heh?"
    eli "Ah! But only because of... well, I am enjoying having this kind of attention from a boy, but... I don't know, it's good to feel desired, and the results are even better!"
    scene EliseDouble03 with Dissolve(2)
    hide window
    w ""
    eli "But hey! I'm only doing this because I know I must get you as excited as possible! Here... are you ready to give me some of your cream?"
    mc "It's all yours! Take as much as you want."
    eli "Good. Take off your clothes then and sit on my bed."
    scene EliseDouble04 with Dissolve(2)
    hide window
    w ""
    eli "Look at that... your dick is so big! I can hold it with both hands... You're definitely something else!"
    scene EliseDouble05 with Dissolve(2)
    hide window
    w ""
    eli "OK, let's start this. I'll make you feel really good! Hm... this is such an erotic smell..."
    mc "{color=#b7b7b7}{i}Uh... she's getting right to it this time. This is awesome! Elise on her knees with her mouth on my dick... and I can do this every day!{/i}{/color}"
    scene EliseDouble06 with Dissolve(2)
    hide window
    w ""
    eli "You taste so good... Hey! Don't you dare cumming in my mouth again, OK? I need in on my face."
    mc "Don't worry, Elise, I'll be careful this time, I swear!"
    scene EliseDouble07 with Dissolve(2)
    hide window
    w ""
    eli "Hm... good."
    "Elise plays with your cock in her mouth for a bit, without diving too deep on it. She licks the head and keeps shoving it against her cheeks, making some sucking sounds when she occasionally suckles on it."
    scene EliseDouble08 with Dissolve(2)
    hide window
    w ""
    "She starts to suck hard on your cock with great technique, trying to get all the cum from your balls."
    mc "Ah... This feels amazing..."
    scene EliseDouble09 with Dissolve(2)
    hide window
    w ""
    eli "Hm... you're delicious! Time to bring in the big guns, he-he! My big tits are the start of the show for you, aren't they?"
    mc "They are beautiful! I can't take my eyes off of them."
    eli "I know! I see you looking at them all the time, even before we started this!"
    scene EliseDouble10 with Dissolve(2)
    hide window
    w ""
    mc "Your entire body is amazing though, top quality! I can't believe you're not married... I'd do everything to fuck you!"
    eli "Well, now you can! You're so sweet, saying things like that to an older woman like me."
    mc "Because it's true. Seriously, you are hotter than a lot of younger girls!"
    scene EliseDouble11 with Dissolve(2)
    hide window
    w ""
    "Elise presses her breasts against your cock, moving them up and down slowly."
    eli "Thank you, honey! Does this feels good? I think it's safer to finish with my tits."
    mc "Yes, keep going, please!"
    scene EliseDouble12 with Dissolve(2)
    hide window
    w ""
    eli "Let me know when you're almost there. I need you to cum on my face... I want it..."
    "She increases the pace of her titfuck, moving her breasts faster and faster along your cock."
    mc "Huh... I'm close..."
    "Elise presses her breasts against your cock even harder, squeezing its head with her tits. You feel her hard nipples massaging you as she moves them up and down, pressing against your groin."
    scene EliseDouble13 with Dissolve(2)
    hide window
    w ""
    "She presses her tits even harder against you as she puts a hand on your face."
    eli "Come on, babe, cum for me... don't hold it back, it's OK to shoot all your load on me..."
    mc "{color=#b7b7b7}{i}Aaah... Having my dick in between Elise's tits like this... feeling her nipples on my body... I never thought this could happen! And she can handle her breasts with so much force! Maybe women with big breasts like them being handled with a bit more violence than usual...{/i}{/color}"
    eli "It feels so good, your cock fits perfectly on my big boobs... I love it! I've never seen such a huge dick!"
    mc "Uuh... you talking dirty to me like this... Elise, I'm... This is great..."
    scene EliseDouble14 with Dissolve(2)
    hide window
    w ""
    mc "AAAHHHH!"
    eli "Ah! Yes, go for it! Pour it all over my face, [MC]!"
    "Elise receives your cum with a big smile as you shoot it up. It falls all over her face as she positions herself perfectly below it."
    scene EliseDouble15 with Dissolve(2)
    hide window
    w ""
    eli "This is perfect, [MC]! We did it!"
    scene EliseDouble16 with Dissolve(2)
    hide window
    w ""
    mc "Wait, there is still more."
    "You squeeze your cock to get all the cum you can from it. The remaining cum drips on Elise's tits as there isn't enough to generate a new stream to shoot on her face."
    eli "Hm, I got some of it on my mouth again! It's so much though that this isn't a problem. It feels so hot on my face!"
    "She spits the cum, forcing it out of her mouth slowly, as it flows to her chin and neck."
    scene EliseDouble17 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}man, I can't get enough of Elise's face covered with my semen. And the expression she makes! It seems like she's enjoying it so much...{/i}{/color}"
    "You start cleaning you dick on Elise's breasts, pressing it against her nipples."
    scene EliseDouble18 with Dissolve(2)
    hide window
    w ""
    "It feels so good that you decide to put it back in between her breasts, pressing them hard to squeeze the last bit of cum from your cock. You play with her nipple and pull it hard while pressing it with your fingers. Elise moans and gasps in surprise when you shoot a bit more of jizz on her cleavage."
    eli "Again??"
    scene EliseDouble19 with Dissolve(2)
    hide window
    w ""
    mc "Ahh... Not really, seems like I had a bit more in there! Watching you enjoying my cum while I play with your beasts was enough to generate enough power to..."
    eli "I see! Well, even more for me to spread on my body! I just hope this wasn't all the semen you have stored for me today..."
    "Elise starts to spreads your semen on her face, giving it a nice shine."
    eli "My face is all moisty now! And a bit sticky, but I want more today, don't forget you promised me double this time! I want my skin really soaked with your cum! I'm gonna look so good after!"
    mc "I remember! But maybe I need a few minutes to recover..."
    scene EliseDouble20 with Dissolve(2)
    hide window
    w ""
    eli "No way, it won't be as effective if we wait too long! I'll make this work."
    "She gets up and starts stripping for you sensually."
    mc "{color=#b7b7b7}{i}Oh my, Elise is going to get fully naked for me this time! I can't wait to see her body...{/i}{/color}"
    scene EliseDouble21 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Amazing! Elise is naked for me! Oh my God, I can finally see her pussy, her bush... This is gonna be way more fun than I expected!{/i}{/color}"
    "Elise continues to spread your cum all over her body."
    eli "OK, lucky boy, time for the second round!"
    scene EliseDouble21-5 with Dissolve(2)
    hide window
    w ""
    "Elise knees in front of you again, this time completely naked, resting your balls on her breasts."
    eli "You really cleaned it up on me, didn't you? It's amazing that you're still this hard."
    scene EliseDouble22 with Dissolve(2)
    hide window
    w ""
    "She climbs on the bed and pushes you down, rubbing her lips on you and licking your shaft from top to bottom while massaging your balls."
    eli "Hm.. Nothing like being young! What an amazing tool you have, it must feel really good to have it inside me... Your smell is even stronger now. Is it still too sensitive?"
    mc "A bit, yeah, but I don't mind!"
    scene EliseDouble23 with Dissolve(2)
    hide window
    w ""
    eli "I know it stays like that for a while, so I'll start slow, don't worry. I'm also aware I'll have to work harder to get more of your cum since you already came once, but I have a plan!"
    scene EliseDouble24 with Dissolve(2)
    hide window
    w ""
    "Elise sits on your cock and starts humping it slowly."
    eli "Do you want to get inside me? You do, don't you? You've been a good boy lately, so maybe you deserve a nice reward like that."
    mc "Yes, please! I want to fuck you so bad!"
    eli "It's gonna feel way better than a handjob, right? That's the only way I can get you excited enough to cum a lot for me once again, right?"
    mc "Huh.... right! Right... it would take forever to make me climax again after cumming, but if I use your pussy..."
    scene EliseDouble25 with Dissolve(2)
    hide window
    w ""
    eli "Hmm... yeah, that's right. I'll let you fuck me. You're gonna feel so good inside me, I'll make you cum a big load again! But not inside me... OK?"
    mc "Y-yeah..."
    "Elise continues to rub her pussy on your cock. It spreads her lips and you can feel her wetness soaking your cock, letting you smell her pussy odor as it mixes with your own."
    scene EliseDouble26 with Dissolve(2)
    hide window
    w ""
    mc "Ah, Elise...I want you! I'm ready."
    "You sit down and start licking her nipples, pushing them around with your tongue, biting and pulling them gently."
    eli "Hm... yeah, go for it, [MC]... suck them harder."
    scene EliseDouble27 with Dissolve(2)
    hide window
    w ""
    eli "Yes, like that. This feels great! Aahh..."
    scene EliseDouble28 with Dissolve(2)
    hide window
    w ""
    "She pulls your hair and lays you down once again, following with a kiss on your lips. You feel her body pressing against yours, her big breasts spreading all over your chest."
    "Your cock is almost slipping inside her as you move and you never wanted to penetrate her so badly like right now. She opens her mouth and puts her tongue inside yours. You hold her amazing body against yours and move your hips, pressing your cock against her pussy, almost trying to slip it inside her already."
    "You continue to kiss for a few more seconds in silence."
    scene EliseDouble29 with Dissolve(2)
    hide window
    w ""
    "Elise reaches to your cock as she sits back with a smile on her face, looking right into your eyes."
    eli "Are you ready, honey? You're so hard... I want you inside me now."
    mc "Yes, I'm going crazy here! I'll give you so much cum this time if we do this!"
    scene EliseDouble29-5 with Dissolve(2)
    hide window
    w ""
    eli "Good, good... Here."
    "Elise places your cock right below her pussy and starts to lower her hips slowly, allowing you to enjoy every inch of her insides as you go in."
    mc "{color=#b7b7b7}{i}The feeling of Elise's raw pussy on my cock is a whole new experience, holy shit! My cock is so hard right now... even harder than before!{/i}{/color}"
    scene EliseDouble30 with Dissolve(2)
    hide window
    w ""
    eli "Aaah... Oh my Goddess, you're inside me! [MC] is fucking my pussy raw..."
    mc "Your pussy feels so good, Elise!"
    eli "Uuh... Keep going!"
    scene EliseDouble31 with Dissolve(2)
    hide window
    w ""
    "Your cock easily slips all the way inside her as she sits on you."
    mc "{color=#b7b7b7}{i}Oh! She's so lubricated, I can't believe how well she received my whole cock inside her! I can feel how much she wants this, even if she pretends that she doesn't! Her pussy is just so wet... and she's still very tight! I'm glad I already came once otherwise I'd be cumming inside her right now!{/i}{/color}"
    eli "This feels so GOOD! It's been so long, I'm burning!"
    scene EliseDouble32 with Dissolve(2)
    hide window
    w ""
    "You grab and spread her butt cheeks, elevating her hips a bit to create enough space for you to start slamming her pussy hard. You start fucking her really fast, moving your hips up and down while holding her in place. You just want to keep doing this for a few more seconds until you fill her pussy with your seed, but you know you can't do it."
    eli "Aaah... ahhh! Keep going! Oh my God, you're hammering my pussy so deep! If you keep going like this I'll... hmmm! We can't, [MC]... we can't keep doing it in this position... It's too risky!"
    scene EliseDouble32-5 with Dissolve(2)
    hide window
    w ""
    mc "I know! Here, I'll take care of it!"
    eli "Oh, wow! I keep forgetting how strong you are!"
    mc "It helps that you are so slim. I feel like I can handle you anyway I want!"
    eli "I'm already soaking wet! Don't talk like this or I won't be able to control myself!"
    "You get on your knees as you hold Elise, with your cock still inside her pussy. She holds onto your neck as you put her down on the mattress. You feel really strong and confident, being inside Elise and carrying this woman with a big smile on her face."
    scene EliseDouble33 with Dissolve(2)
    hide window
    w ""
    "Your cock slips outside her pussy as you put her down. Elise quickly puts her hand on it and starts putting it back inside her, eager for you to continue fucking her. You keep her hips high to get even deeper inside her."
    scene EliseDouble34 with Dissolve(2)
    hide window
    w ""
    "Elise's pussy easily swallows your cock once again like it's already shaped for it. She stares at you with hungry eyes and a smile."
    eli "Go on. Fuck me hard, [MC]!"
    scene EliseDouble35 with Dissolve(2)
    hide window
    w ""
    mc "Are you sure?"
    eli "Yes, look at this giant thing! Your cock feels so good... I can't hold up any longer!"
    mc "Yes, ma'am!"
    scene EliseDouble36 with Dissolve(2)
    hide window
    w ""
    eli "Hey, don't start calling me \"ma'am\" now! Now keep using my body as you wish, I want more of that cum you promised! Make sure you cum a lot on my face and body, I want to cover every inch of my body on your semen now."
    mc "Holy fuck! I love hearing you say things like this, Elise!"
    scene EliseDouble37 with Dissolve(2)
    hide window
    w ""
    mc "I'm all the way inside your pussy! I'm fucking my friend's mom!"
    eli "Yeah! Hmm... give mamma your dick! Empty your balls on me! I want to smell your semen for a week after this!"
    "You push Elise's legs up and start fucking her as hard as you can, shoving all of your cock inside her pussy and hitting all the way to her cervix over and over. You're surprised by how flexible Elise is as you bend her and keep pounding on her from the top."
    scene EliseDouble38 with Dissolve(2)
    hide window
    w ""
    mc "Aaah, this feels too good! I'm almost cumming again!"
    eli "Aaah, keep going! I'm almost there! Fuck me harder!"
    scene EliseDouble39 with Dissolve(2)
    hide window
    w ""
    mc "I need to... pull it out! Or I'll cum inside!"
    eli "Uuh, just a bit longer... keep going, darling! Fuck me!"
    "You already start shooting a lot of precum inside Elise's pussy. She holds you and moans really loud as she climax, forgetting about the possibility of Sophie hearing her. At this point, you know it's impossible to take it off in time."
    scene EliseDouble40 with Dissolve(2)
    hide window
    w ""
    "You start cumming inside Elise, shooting a big amount of cum inside her already."
    mc "Huh... Elise... I'm cumming..."
    eli "What? Oh my Goddess, I can feel it! You're cumming inside me! Take it out! Come outside!"
    scene EliseDouble41 with Dissolve(2)
    hide window
    w ""
    "You try to hold as you take your cock out of her pussy but its hard to do it after shooting the first jet. You feel like your cock is about to explode."
    eli "Come on, fast! Cover me with your cum, [MC]! I need this!"
    scene EliseDouble42 with Dissolve(2)
    hide window
    w ""
    mc "Aaah! Here it is!"
    "Another jet of cum is released as soon as you take your cock out. It goes straight to her face with a lot of pressure, but some of it goes out even before your cock pops up, shooting jizz all over her pussy, bush and belly along the way. You still try to hold it once more as you approach her face with your cock."
    eli "Wow! You got it!"
    mc "Uh... wait! Here, there is more..."
    scene EliseDouble43 with Dissolve(2)
    hide window
    w ""
    "You finally release it all and start shooting a massive load of cum of Elise's face. You feel all your energy being drained from you, your cock hurting from all the jizz coming out of it."
    eli "Oh my God, [MC]... it's so much... and you also came inside!"
    "As you continue to pour semen over Elise's body, you notice her spasming from cumming with you. She breathes heavily, trying to calm down and relax, still ecstatic from having that huge amount of your jizz on her body."
    stop music fadeout 1
    scene EliseDouble44 with Dissolve(2)
    hide window
    w ""
    mc "A little bit. I'm so sorry, Elise! I couldn't hold all the way."
    play music elise
    eli "Ah, It's OK, don't worry about it. It's my fault too... It felt so good, it's been years since I came like this. Get up, come on, let me see it."
    scene EliseDouble45 with Dissolve(2)
    hide window
    w ""
    eli "Oh wow, it's more than I thought! It's outside and it's also dripping from inside my pussy... you creampied me! Oh my God, [MC]! How can you cum so much?! it's amazing!"
    mc "I don't know. I was too excited! You did a great job!"
    eli "Well, thanks! I'm glad to know I was part of it, that I can make you cum so much..."
    scene EliseDouble46 with Dissolve(2)
    hide window
    w ""
    eli "Anyway, enjoy it while it lasts! And be careful not to be seen leaving my bedroom! I'll stay here to finish spreading it all over my body and to let my body soak it in for a bit."
    mc "I'm not sure how they wouldn't hear all our moaning and screams..."
    eli "I think I heard Sophie leaving the house a while ago, so we got lucky! Anyway, bye [MC]."
    mc "OK, OK, I'll leave you to it. Bye Elise! Talk to you soon?"
    eli "Yes, see you soon!"
    stop music fadeout 2
    $ persistent.elisedouble = True
    $ renpy.end_replay()

label NinaBath:
    play sound walkgrass
    scene elises garden with Dissolve(2)
    mc "{color=#b7b7b7}{i}Damn... This was amazing! I still can't believe what just happened. Yesterday it was [Nova], today it was Elise... What's happening to my life?{/color}{/i}"
    mc "{color=#b7b7b7}{i}Well, I can't complain. Dad's recovering fine, I have a date with Mia and there's a party tonight!{/color}{/i}"
    mc "{color=#b7b7b7}{i}Hm, it's still early and I can't go to Mia smelling like sex! And I don't think going home is a good idea, [Nova] will pick on me forever if I go back for a bath after visiting Elise!{/color}{/i}"
    mc "{color=#b7b7b7}{i}I think I'll just go to the lake and bathe there.{/color}{/i}"
    play sound walkgrass
    scene lake sunny with Dissolve(2)
    "You walk to the lake and notice some movement in the water."
    play music nina2
    mc "Huh? Is someone here already?"
    scene NinaLake1 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Fuck! Is that Nina?{/color}{/i}"
    "You hide yourself behind a bush nearby"
    scene NinaLake2 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Should I be hiding? I think it'll be worse if she sees me here - no way she's gonna believe that I wasn't peeping on her!{/color}{/i}"
    mc "{color=#b7b7b7}{i}It feels weird seeing her like this after what we did... I wish I had the balls to go after her before she started dating Trevor.{/color}{/i}"
    mc "{color=#b7b7b7}{i}Anyway, I better stop looking now. I'll just stay hidden until she finishes and goes away.{/color}{/i}"
    scene blackout with Dissolve(2)
    "You stay hidden for almost 1 hour until Nina finally goes away."
    scene lake sunny with Dissolve(2)
    mc "{color=#b7b7b7}{i}Well, time to take my bath now!{/color}{/i}"
    mc "{color=#b7b7b7}{i}It's so weird how just a little while ago I wasn't anywhere near fucking anyone and suddenly I have all these girls to choose from! [Nova], Nina, Mia, Elise... Life is good!{/color}{/i}"
    scene blackout with Dissolve(2)
    stop music fadeout 2
    "You finish bathing and stays at the lake for a while enjoying the view and thinking about life. After awhile, you go to the elder's house to see Mia."

label PickMiaUp:
    scene elders house with Dissolve(2)
    mc "Hello? Anybody here?"
    play music afternoon2
    show mia neutral cook with Dissolve(1)
    mia "Oh, hi [MC]!"
    mc "Hey, did I get here too early?"
    mia "No, not at all!"
    mia "I mean... I was just starting to make the pie, so it's not early if you don't mind keeping me company while I bake it, he-he!"
    mc "Not at all!"
    scene blackout with Dissolve(2)
    "Mia start baking the pie while you have a casual conversation."
    scene elders house with Dissolve(2)
    show mia neutral cook with Dissolve(1)
    mia "So... anything else exciting today?"
    mc "Nope. First slow day since the storm, I think."
    mia "Lucky you."
    mc "Well, now it's time to relax."
    mia "I hope so. I.. I don't know if I'm quite at the point where these big parties relax me, though."
    mia "But I'm doing a lot better with new people now, thanks to you and [Nova]."
    mc "We're not exactly new, though."
    mia "No, but... I mean, we hang out now when we have time, so that's new."
    mc "Yeah. I guess so. By the way, that smells pretty amazing!"
    mia "Thanks! I really think it's going to come out perfectly this time!"
    mc "I love your pies even when they don't come out perfectly!"
    mia "We'll see! It's done, here you go!"
    mc "Awesome, I'm gonna dig right in!"
    scene cgMiaSpiked1 with Dissolve(2)
    hide window
    w ""
    mia "So...?"
    mc "Wow! It tastes SO GOOD!!"
    mia "Yay!"
    mc "Damn Mia, I can't stop eating it... You're awesome!"
    mia "He-he, thanks! But using Spiked Fruits is a bit like cheating though - they say it tastes so good that it even makes those who eat them taste good! You must taste delicious right now after eating so much!"
    scene cgMiaSpiked2 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Damn, that dress she's wearing is so revealing, I can almost see her nipples! Seems like she still doesn't really know how to deal with her giant tits. She used to be very shy about them though, I guess she's getting more comfortable around me. And by the way she's talking... maybe I should try to get something out of this?{/color}{/i}"
    mia "Is there something wrong [MC]? You went silent all the sudden..."
    scene cgMiaSpiked3 with Dissolve(2)
    hide window
    w ""
    mc "Sorry! I was just remembering the things I read about this fruit. Apparently very few people have had the chance to taste this supposed amazing thing that is someone's... fluids after eating a Spiked Fruit."
    mia "Fluids?"
    mc "Yeah, like saliva or..."
    mia "Ew! Who would drink someone else's saliva?"
    mc "Well, not drink it, more like kissing the person."
    mia "Ah..."
    mc "But what they say it really changes is the taste of semen."
    mia "[MC]!!"
    mc "What? Is it too weird to talk about it?"
    mia "Hm... no... it's OK, I guess. Cooking can get really weird sometimes, I forgot we are talking about 'food' here."
    mc "That's right! They say semen can change its taste based on the person's diet, but what the Spiked Fruit does is just in a whole other level. Like, back in the day people would get really addicted to it, and they even used to sell it in stores!"
    mia "Wow! If people did that than it must really taste amazing! Because... I would never drink something like that from a stranger!"
    mc "Well, I'm not a stranger and this is the chance of a lifetime, I heard that these days some people pay a lot of gold to get it. Can you imagine it? Being one of the few people in the whole world to taste something so good and rare? Specially if you're a cooking enthusiast..."
    scene cgMiaSpiked3-2 with Dissolve(2)
    hide window
    w ""
    "With a fast but smooth movement Mia gets on the tip of her toes and kisses your bottom lip, sucking it a bit, then biting it, pulling it down as she gets back on her feet."
    scene cgMiaSpiked3-3 with Dissolve(2)
    hide window
    w ""
    mia "Hm... It really tastes good! I see what you're doing here, [MC]! You know, I'm not just a country girl afraid of the world like most people here... I also want to experience new things! Just like you talking about seeing the world! I don't think I'll ever leave the village but... I also don't want to miss opportunities in my life. I'm OK with it if you want..."
    mia "I'll eat some of the pie too, so you can kiss me if you want..."
    mc "You're truly an amazing woman, Mia... You never stop surprising me!"
    scene cgMiaSpiked4 with Dissolve(2)
    hide window
    w ""
    "After Mia bites a small piece of the pie you hold her waist and move closer to her. She moves closer to you almost in a jump, holding your neck and touching your lips with hers. You open you mouth and as she follows the movement, you stick you tongue out into her mouth."
    scene cgMiaSpiked5 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Mia is so cute! For a while I thought it would be almost impossible to get something from her, or that she would be very boring, but... I think she may be way more into this kind of stuff than I thought!{/color}{/i}"
    scene cgMiaSpiked6 with Dissolve(2)
    hide window
    w ""
    "You press your hard cock against Mia's pussy as you kiss her. Her dress is thin enough to let you feel her shape very well with your cock."
    mc "{color=#b7b7b7}{i}She's so wet, I can already smell her scent from here!{/color}{/i}"
    mia "W-Wait, [MC]..."
    mc "Huh? What is it, Mia, did I do something wrong?"
    scene cgMiaSpiked3 with Dissolve(2)
    hide window
    w ""
    mia "No! It's just... maybe we should go somewhere else? The elder will be back any time now."
    mc "Oh yeah, I guess it would be awkward if someone catched us doing this! Do you have somewhere in mind? Maybe my house?"
    mia "No... I know this really nice spot near the lake..."
    mc "A secret spot? Cool! I'd love to go there with you."
    scene blackout with Dissolve (2)
    stop music fadeout 2
    "You walk outside the elder's house holding hands with Mia as she pulls you in a hurry to the lake. When you get there, she takes a small, almost hidden path and moves some bushes away to reveal a place never knew existed."
    play music romance3
    scene cgMiaSpiked7 with Dissolve(2)
    hide window
    w ""
    mia "What do you think?"
    mc "I don't think I've even been here before. This place is incredible!"
    mia "Isn't it? It used to be a really popular place for couples and dates a few years ago. Nowadays people seem to have forgotten about this place for some reason. Besides me, only elder Silas seems to come here from time to time to keep the place in a good condition."
    mc "Do you think love is out of fashion or something like that?"
    mia "Maybe... I love coming here though, it's so relaxing. It feels good to have some company for a change."
    scene cgMiaSpiked8 with Dissolve(2)
    hide window
    w ""
    "You wrap your arms around Mia, who promptly hugs you back, putting her head on your shoulder."
    mc "You can call me whenever you want. I really like spending time with you."
    scene cgMiaSpiked9 with Dissolve(2)
    hide window
    w ""
    mia "He-he! I don't know why, but it makes me really happy to hear you saying things like this."
    mc "Well, making you happy definitely makes me happy!"
    mia "I'm so glad we reconnected... even if the reason was something so bad, with the storm and your dad getting sick."
    mc "Me too. It's so funny how life is sometimes... We were always near each other but we didn't talk much."
    mia "Yeah! When we were kids I was way too shy to play with you, Nina and [Nova]."
    mc "But we did, sometimes."
    mia "Mostly when we were alone though. You could be really nice sometimes, but also too rowdy when you were with your friends. It was like knowing two of you."
    mc "I guess everyone has two sides... or more."
    mia "Oh, for sure! Anyway, then I guess everyone just started doing their own things and... well, that's life, I guess."
    mc "Sometimes I have a hard time even remembering what I had been doing before the storm. Like I had a foggy mind back then, just living day by day..."
    mia "I know what you mean. Life is really different now! We are even... I mean, we just ate a pie made with a super rare fruit and... I-I..."
    mc "Hey, Mia... Do you want to do it now?"
    mia "Yes!"
    mc "{color=#b7b7b7}{i}That was a fast answer!{/color}{/i}"
    scene cgMiaSpiked10 with Dissolve(2)
    hide window
    w ""
    "You get up and start removing your pants in front of Mia. She close her eyes right before you start taking your cock out."
    mc "Are you sure this isn't weird? Drinking my semen as a culinary experience..."
    mia "It's a bit weird, but people who sleep together do this for fun all the time anyway, right? Since we already... had sex... I think it's OK for us to do this kind of stuff!"
    mc "Yeah, I agree! It's OK for you to look, you know... You don't have to keep your eyes closed."
    scene cgMiaSpiked11 with Dissolve(2)
    hide window
    w ""
    mia "Oh my God, [MC]... I'm not used to this yet! You have your bare cock right in front of me... It's so big!"
    mc "Do you mind getting on your knees in front of me? It will make it easier to aim into your mouth..."
    scene cgMiaSpiked12 with Dissolve(2)
    hide window
    w ""
    mia "OK... Like this?"
    mc "Yes, that's fine, but it might take a while - I don't think I'll be able to cum very fast."
    mia "Huh? Why not?! We can't stay here doing this too long or someone could see us and..."
    mc "I know, but that's exactly because of this pressure! Maybe you could show me your tits? I think it would help..."
    scene cgMiaSpiked13 with Dissolve(2)
    hide window
    w ""
    mia "Mm... fine... This is so embarrassing..."
    mc "Why? Your body is so beautiful..."
    scene cgMiaSpiked14 with Dissolve(2)
    hide window
    w ""
    mia "You really think so? I feel so embarrassed by how big they are... and most men can't stop staring at them! You don't, though. I mean, only sometimes, but you really try not to... I really appreciate that, but today it's fine, I'll let you look at them as much as you want."
    mia "I can't believe we're like this now... being so casual about you cumming on my mouth. I know it must feel good to have a girl drinking your cum, but... Do you feel the same embarrassment I feel about my tits? Because of your big cock, I mean..."
    mc "Sometimes, specially when it gets hard at inappropriate times."
    mia "I see..."
    "You continue to masturbate right in front of Mia's face"
    mc "This is really helping. You can also look if you want to. And I get it, at the end of the day our big attributes call too much attention when we don't want it and from the wrong people... What a weird match we are at this, right? The boy with a big cock and the girl with big tits... and butt!"
    scene cgMiaSpiked15 with Dissolve(2)
    hide window
    w ""
    mia "Hm, yeah, I hate getting all those looks from every man around me... But you can at least hide yours. I had no idea you were so big! But I guess if someone sees it or hears about it then they might want to approach you just because they are curious, right?"
    mc "Maybe... Are we really talking about our bodies so openly while we do this? I think this shows how comfortable we are getting with each other!"
    mia "Oh my, for sure! I'm burning though, I can't believe I'm actually talking to you like this!"
    mc "Well, I like this Mia. \"Many different sides\", right?"
    mia "R-Right! Are you close?"
    mc "Almost there... you can open your mouth already."
    scene cgMiaSpiked16 with Dissolve(2)
    hide window
    w ""
    "Mia opens her mouth and close her eyes, staying silent, anxiously waiting for you to shoot your cum inside her mouth. You keep stroking your cock and getting it closer to her mouth as you approach climax."
    scene cgMiaSpiked17 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}My cock is so close to her lips... I can feel her warm breath already. Would she mind if I touched her lips with my cock?{/color}{/i}"
    scene cgMiaSpiked18 with Dissolve(2)
    hide window
    w ""
    "You put your cock against Mia's lips and see her gasping. She slowly moves her tongue out, touching you cock with its tip."
    mc "{color=#b7b7b7}{i}Oh, wow, I think she's into this!{/color}{/i}"
    scene cgMiaSpiked19 with Dissolve(2)
    hide window
    w ""
    "Mia opens her mouth even more, sticking her entire tongue out. You start to gently slap your cock on her tongue as you keep masturbating."
    scene cgMiaSpiked19-2 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}She's letting me use her tongue... It feels so good! Getting my cock wet with her saliva... Ah, I really want to cum all over her!{/color}{/i}"
    scene cgMiaSpiked20 with Dissolve(2)
    hide window
    w ""
    "You keep stroking your cock on top of Mia's tongue, ready to fill her mouth with your semen."
    mia "Aahh..."
    scene cgMiaSpiked21 with Dissolve(2)
    hide window
    w ""
    "Mia smiles in silence and looks up at you, placing her tongue between her teeth. With such a playful look on her face, you are now sure she's aware of what's happening and really enjoying it."
    mc "{color=#b7b7b7}{i}Look at that angelical face... Mia... I'm...{/color}{/i}"
    scene cgMiaSpiked22 with Dissolve(2)
    hide window
    w ""
    mc "Cumming!"
    "You start bursting your cum all over Mia's face, forgetting she was supposed to drink it."
    scene cgMiaSpiked23 with Dissolve(2)
    hide window
    w ""
    "Mia quickly realizes it and holds your cock, putting it inside her mouth to send your load into her throat."
    scene cgMiaSpiked24 with Dissolve(2)
    hide window
    w ""
    "She keeps holding you in place, sucking your cock as she tries to get every last drop of cum from it."
    scene cgMiaSpiked25 with Dissolve(2)
    hide window
    w ""
    "You instinctively pull her head for a deeper penetration, but Mia holds her head in place, more interested and focused on drinking all of your load."
    mc "AaaAah, Mia... This feels so good! Here, I'm almost done."
    scene cgMiaSpiked26 with Dissolve(2)
    hide window
    w ""
    "You tilt her head back, needing to use some force to get her mouth out of your cock. You squeeze it to get the last drops inside Mia's mouth."
    scene cgMiaSpiked27 with Dissolve(2)
    hide window
    w ""
    mia "Oh my GOD, [MC]!! It tastes SO GOOD! It's like... 10 times better than chocolate! I've never had something so delicious in my life!"
    mc "That good, huh? I'm glad you enjoyed it so much!"
    mia "It happened so fast... I'm mad you shot so much outside first!"
    scene cgMiaSpiked28 with Dissolve(2)
    hide window
    w ""
    mc "Here, there is a lot on your face still, let me get it for you..."
    "Thinking about enjoying Mia's mouth a bit more you use your own cock to rub on Mia's face and feed her again."
    scene cgMiaSpiked29 with Dissolve(2)
    hide window
    w ""
    mia "Hmm.. Thanks. So good..."
    "Mia doesn't even seem to realize she's actually giving you a blowjob. She finishes licking your cock and drinking your cum, then she puts her dress back on."
    scene cgMiaSpiked30 with Dissolve(2)
    hide window
    w ""
    mia "Wow... I can totally understand why people get so addicted to this... I'm glad we did it, [MC]. Thank you so much! I'm sorry I didn't leave anything for you."
    mc "Uh... No problem. You fed me already, so thanks for the pie!"
    mia "It was my pleasure! Thanks for the dessert, he-he!"
    mc "So, ready to go to the party?"
    mia "We still have some time to kill. I need to go home and change my clothes, though - no way I'm going out dressed like this!"
    mc "You look amazing, but I guess that's the problem, right? People would stare too much."
    mia "Yeah... Walk with me? We can go to the pub after I change."
    mc "Sure!"
    scene blackout with Dissolve(2)
    stop music fadeout 2
    $ persistent.miaspiked = True
    $ renpy.end_replay()
    play sound walkgrass
    "The two of you begin walking down the path to Mia's house. You wait for her to change, then the two of you continue to the party. When you reach the pub you can see that the festivities are underway."


label PubParty:
    play music militia2
    scene pub exterior night with Dissolve(2)
    show laura neutral with Dissolve(1)
    lau "Hey [MC], Mia, you made it! Took you long enough."
    mc "Didn't think we were late... it sounds crazy in there."
    lau "Not yet, but soon enough. Everyone's been asking about you."
    mc "Really?"
    lau "Yes! Really. You and your little party are the hot shit in town right now."
    lau "I still can't believe you guys went into a forest full of goblins with like a hatchet and one sword and came back alive. That's legit badass!"
    mc "I guess it is."
    if FuckedLaura == 1:
        lau "And, you're not half bad in the sack either! If you keep like this, soon you'll be really popular with the girls here!"
        lau "But Mia knows that already, I'm sure."
        "Mia turns beet red."
        lau "Sorry, I'm just fucking around! I drank too much already, I think!"
        mc "That's OK. We're going in now, are you coming?"
    lau "Well, I've been out here long enough to dodge Nickolas' drunk ass, so let's go!"
    play ambient pubparty fadein 1
    $ renpy.music.set_volume(0.4, 0, channel="ambient")
    scene pub interior with Dissolve(2)
    "As you walk in you see [Nova] standing by herself."
    show nova neutral with Dissolve(1)
    mc "Hey [Nova]!"
    nov "Finally! I was scared you two were gonna leave me here alone."
    show mia neutral at slightleft with Dissolve(1)
    show nova neutral at slightright with easeinleft
    mia "Oh, sorry [Nova]! We got a little held up."
    show nova smirk with Dissolve(0.2)
    nov "I bet."
    nov "Hey Mia, come on, join me for a bit!"
    "Nova grabs Mia's hand and walks off before she can object."
    hide nova with easeoutright
    hide mia with easeoutright
    "As you watch them leave, Evelyn greets you with a smile."
    show evelyn neutral with Dissolve(1)
    eve "Welcome to the party!"
    mc "Nice spread."
    eve "Hey, only the best for the town's heroes. The gang's over there at the big table. Trevor's been asking about you."
    "You see Trevor sitting at a table with Sophie and some of the militia."
    tre "Hey man! Good to see you. Grab a drink!"
    mc "{color=#b7b7b7}{i}I'm still not really used to seeing Trevor being nice... it's disquieting.{/color}{/i}"
    hide evelyn with Dissolve(1)
    "You walk to them and Sophie looks up at you with a smirk."
    show sophie neutral at offscreenleft
    show sophie neutral at farleft with Dissolve(1)
    sop "I still barely believe that you pulled this off. Who would have thought?"
    show toby neutral at offscreenleft
    show toby neutral at slightleft with Dissolve(1)
    tob "Did you find any treasure out there?"
    mc "Not really, I wasn't there for-"
    tob "Boring! Well, except for the goblin part. Next time you should fight some richer monsters!"
    show lisa neutral at offscreenright
    show lisa neutral at farright with Dissolve(1)
    lis "It doesn't really work that way, Toby."
    show nina neutral at center with Dissolve(1)
    nin "Hey! How are you? Is everything OK with your dad?"
    mc "Yeah, he's finally getting better!"
    nin "That's good to hear!"
    show nina neutral at slightright with easeinleft
    show evelyn neutral at center with Dissolve(1)
    eve "So, what are you having to drink tonight, [MC]?"
    mc "I think I'll just have some water for now."
    tob "What? Fuckin man up, dude! Drink something hard! Aren't you the new badass or whatever? Prove it."
    eve "Don't let him pressure you, [MC]. but don't hold back on my account. We're celebrating, I won't think worse of you for some drinking, tonight of all nights."
    mc "Alright, then. Give me what you got. House's choice."
    eve "OK, let's go easy to start the night. One beer. Coming up."
    "Evelyn goes off to get you your drink."
    hide evelyn with easeoutright

label PubParty2:
    scene pub interior with Dissolve(2)
    "A few minutes later Evelyn returns with your drink."
    show evelyn neutral at center with Dissolve(1)
    eve "Here you go."
    mc "Thanks, Evelyn!"
    hide evelyn with Dissolve(1)
    show lisa neutral at center with Dissolve(1)
    lis "OK, everyone's here, beverages are served... so, I think it's finally time."
    lis "Mia, [Nova]! Get over here!"
    nov "What?"
    lis "You're needed."
    "Mia and [Nova] arrive at the table."
    show nova neutral at offscreenright
    show mia neutral at offscreenright
    show nova neutral at slightright with Dissolve(1)
    show mia neutral at farright with Dissolve(1)
    nov "Needed for what?"
    lis "Story time, we want details! What happened out there? Why don't you tell us, [MC]? Because we know Trevor will just lie abour how heroic he was."
    lis "And I'm counting on the ladies to call bullshit."
    "Lisa calls out to the party."
    lis "EVERYONE, COME ON! STORY TIME!"
    "The rest of the gang rapidly arrives."
    mc "Hm... What part?"
    sop "All of it!"
    mc "Well, I decided to head out on my own to find the Azureola..."
    stop music fadeout 1
    scene blackout with Dissolve(2)
    "You start telling them about your journey, obviously leaving some stories to yourself and the girls."
    play music brooke
    if NegotiatedBandits == 1:
        scene pub interior with Dissolve(2)
        show lisa neutral at offscreenleft
        show lisa neutral at slightleft with Dissolve(1)
        lis "So, back to the bandits... [MC] decided to risk his life to help some random girl just like that?"
        show laura neutral at offscreenleft
        show laura neutral at farleft with Dissolve(1)
        lau "That was actually pretty badass."
        show trevor neutral at center with Dissolve(1)
        tre "That was too crazy, he definitely shouldn't have done that - he risked everyone's lives."
        show nina angry at offscreenright
        show nina angry at farright with Dissolve(1)
        nin "Yeah, [MC], what were you thinking?"
        $ SophieLove += 1
        $ EveLove += 1
    else:
        scene pub interior with Dissolve(2)
        show lisa neutral at offscreenleft
        show lisa neutral at slightleft with Dissolve(1)
        lis "Back to the bandits... so you guys watched them fuck the small girl first?"
        show laura neutral at offscreenleft
        show laura neutral at farleft with Dissolve(1)
        lau "Yeah, that's a little odd."
        show nova neutral at offscreenright
        show nova neutral at slightright with Dissolve(1)
        nov "In our defense, we really didn't want to be seen."
        mc "And we didn't know that she was in danger until they started threatening her."
        show trevor neutral at center with Dissolve(1)
        tre "I still say you just wanted to watch the action."
        show mia blushing 2 at offscreenright
        show mia blushing 2 at farright with Dissolve(1)
        mia "I did not!"
        tre "I meant [MC], Mia."
        mc "What? You were the one trying to convince us not to intervene!"
        $ NinaLove += 1

    lau "Well, it doesn't matter since Mia had to save your asses anyway!"
    lis "Now THAT is amazing! Who would have guessed it?"
    scene blackout with Dissolve(2)
    "After a while you finish your story and everyone is a bit drunker. Mia, specially, has been knocking back drinks with [Nova]."
    scene pub interior with Dissolve(2)
    show evelyn neutral at center with Dissolve(1)
    eve "I can't believe you actually met a fairy!"
    show lisa neutral at slightleft with Dissolve(1)
    lis "I can't believe you risked your life to save one!"
    show nova neutral at offscreenright
    show nova neutral at slightright with Dissolve(1)
    nov "Oh, I agree!"
    show mia neutral at offscreenright
    show mia neutral at farright with Dissolve(1)
    mia "[MC] and Trevor were so amazing protecting us from all those goblins!"
    if HelpTrevor == 0:
        mia "Oh, and [Nova] too!"
        lis "Yeah, nice one, [Nova]!"
    lis "But damn, [MC], are you a secret badass or something? After that slime incident I'd never think you'd do something like that!"
    show laura neutral at offscreenleft
    show laura neutral at farleft with Dissolve(1)
    lau "That's crazy. You could all have been killed out there."
    show sophie neutral at midleft with Dissolve(1)
    sop "Still, I never would have thought [MC] would be a hero like that."
    eve "There is more to you than meets the eye, [MC]."
    tre "Well, it's not like he did all by himself, you know!"
    eve "Yeah, but he isn't even part of the militia, he has no training at all, it was a really brave thing to do."
    scene blackout with Dissolve(2)
    "After some time the party breaks up into smaller groups. You mingle around for a while until you run into Evelyn."
    scene pub interior with Dissolve(2)
    show evelyn neutral at center with Dissolve(1)
    mc "Hey."
    eve "Hello! So, why is one of the guests of honor sitting by himself at the bar?"
    mc "No reason in particular, just taking a break from all the questions about the goblin horde."
    eve "It was a horde?"
    mc "Tales grow with the telling, I guess."
    eve "Well, you should go and talk to people... enjoy the fame while it lasts!"
    mc "I'm talking to you, aren't I?"
    eve "I suppose you are."
    eve "So, since you're sitting at the bar... let me top you off."
    "Evelyn pours you another beer."
    eve "Here you go. Don't blame me if you wake up under a table tomorrow."
    mc "I'll try not to!"
    eve "Hey, do you believe someone carved out a gloryhole in one of the toilets? I heard Sophie asking Toby to go in there with her, but I can't have that sort of thing in there."
    mc "Really? Those two seem to always be trying to fuck during parties... do you think they're the ones responsible for carving the hole?"
    eve "Hm, I don't think so. Between us, Toby never seems much interested in having sex, you know? At least not with Sophie, and I have no idea why - she's gorgeous."
    mc "True. Well, I can fix it for you."
    eve "Really? That would be great, thank you! But not today, today you party!"
    "You and Evelyn chat for a while before she goes to check on the other guests."
    hide evelyn with Dissolve(1)
    mc "{color=#b7b7b7}{i}Hm, I don't see Sophie in here, and Toby is there drunk as hell talking to his friends... Is she waiting for him? Maybe...{/color}{/i}"

menu GloryChoice:
    "Check the Gloryhole [gr]\[Sophia Scene and {i}Why not?{/i}\]":
        "You walk to the outdoor toilet and try to locate the glory hole."
        $ SophieGlory = 1
        jump SophieGloryHole
    "Head outside to get some fresh air.":

        "You hang out at the bar a bit longer and decide to head outside to get some fresh air."
        stop ambient fadeout 2
        stop music fadeout 2
        scene pub exterior night with Dissolve(2)
        "You sit down on the steps of the pub, and hear a door open behind you."
        $ SophieGloryHole = 0
        jump OutsideBreak

label SophieGloryHole:
    stop ambient fadeout 2
    stop music fadeout 2
    scene GlorySophie0 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Oh, here it is. I can't believe Toby just left her here. She's expecting him to show up, too. She looks kinda hot in there, all pouty... I'd hate to leave her hanging. You know, I guess this couldn't hurt..."
    play music sophie
    scene GlorySophie1 with Dissolve(2)
    hide window
    w ""
    sop "Yawn...Seriously? Where the fuck is he? A couple minutes my ass!"
    sop "If he isn't in here in five minutes I'm going to go out there and drag his ass here."
    sop "What a dick. He's completely wasting my time."
    sop "I still have a whole pint of beer sitting out there."
    sop "Hm?"
    scene GlorySophie2 with Dissolve(2)
    hide window
    w ""
    sop "Oh!"
    sop "{color=#b7b7b7}{i}Shit, that almost scared me. I guess I gave up on him meeting me, but...{/color}{/i}"
    sop "So, you finally decided to show up."
    sop "You know, it took you long enough, asshole. I was about to leave."
    sop "What, you're giving me the silent treatment?"
    sop "Fine. I didn't want to hear your excuses anyway."
    scene GlorySophie3 with Dissolve(2)
    hide window
    w ""
    "You hear Sophie shift onto her knees in front of you."
    mc "{color=#b7b7b7}{i}Oh, shit! I can't believe this is happening! Sophie is going to suck my cock!{/color}{/i}"
    sop "You know, I was going to kick your ass if you didn't show up."
    sop "Honestly, I should just leave you in here. Make you deal with it yourself. How would that feel, huh?"
    sop "Right. Not talking. Fine, asshole."
    sop "You're lucky I'm still in the mood."
    scene GlorySophie4 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Ah, shit...{/color}{/i}"
    "You feel the light touch of Sophie's fingers as she wraps her hand around your cock. It gives a hard throb as her lips brush against your tip."
    sop "You like that, huh?"
    "You have to restrain a low moan as her tongue slips underneath your tip, taking a long, agonizing stroke over the slit."
    "You just barely feel her lips brushing against the sensitive skin. Your cock hardens in response."
    sop "{color=#b7b7b7}{i}Wow... He feels bigger than usual.{/color}{/i}"
    "She continues to tease your tip, her tongue making small patterns against the smooth skin. You bite down hard on your lip to keep quiet, allowing your cock to harden against her lips."
    sop "Is this what you wanted?"
    mc "{color=#b7b7b7}{i}Goddess... I wish I could see her. I bet she looks so hot right now, on her knees, my cock in my mouth...{/color}{/i}"
    sop "Is this good enough? Huh, Toby? Just a little taste..."
    scene GlorySophie5 with Dissolve(2)
    hide window
    w ""
    sop "Mmm..."
    "You feel her other hand press down on your cock firmly as she slowly takes your tip into her mouth. You're barely past her lips, enough for her tongue to flick and tease with more ease."
    sop "{color=#b7b7b7}{i}He's getting so big! Maybe we should do this more often...{/color}{/i}"
    sop "Someone's getting excited. Where am I supposed to put all of this?"
    sop "{color=#b7b7b7}{i}I've never seen him get this big before!{/color}{/i}"
    sop "{color=#b7b7b7}{i}Thank the Goddess. I was worried we'd never find something he'd get this turned on for.{/color}{/i}"
    scene GlorySophie6 with Dissolve(2)
    hide window
    w ""
    "Sophie leans forward, taking you further into her mouth. You're unable to contain a small grunt of pleasure as her saliva coats your cock."
    "Her tongue dances around the sensitive skin, bringing you to your full girth."
    sop "Holy shit!"
    sop "{color=#b7b7b7}{i}Look at the size of that thing! There's no way that's Toby, right?!{/color}{/i}"
    sop "{color=#b7b7b7}{i}Maybe this is why he was taking a while...?{/color}{/i}"
    sop "{color=#b7b7b7}{i}He's huge! Damn! I could get used to this...{/color}{/i}"
    "Sophie lets out a moan, the noise reverberating around your cock. You press it tighter against the wall, desperate to feel it deeper in her mouth."
    scene GlorySophie7 with Dissolve(2)
    hide window
    w ""
    mc "{color=#b7b7b7}{i}Fuck! She feels so, so good on me. I don't know if I'm going to be able to keep quiet if she keeps it up like this...{/color}{/i}"
    "You feel her struggle to take more of your cock into her mouth, unable to fit the entire thing inside of her."
    "She moans again, the vibrations rocking against your erection."
    "It's too much. You can't hold it in anymore. You let out a loud moan and throw your head back in pleasure."
    "You hope it doesn't deter her from blowing you. Your cock just feels so good in her mouth."
    sop "Huh?"
    sop "{color=#b7b7b7}{i}No, that's definitely not Toby. He does not sound like that.{/color}{/i}"
    sop "{color=#b7b7b7}{i}Wait, who the fuck am I blowing?!{/color}{/i}"
    "Sophie stops for a second and, in that moment, you're afraid you've driven her off."
    sop "Who is this? Answer me! Now!"
    "You briefly consider answering but quickly squash down that idea. She has your cock in her hand. That's a dangerous thing to leave in the hands of an angry woman."
    sop "{color=#b7b7b7}{i}I can't believe some creep just came in here and let me start blowing him!{/color}{/i}"
    sop "{color=#b7b7b7}{i}What an asshole! I... I... I kind of like this. What the hell is wrong with me?{/color}{/i}"
    sop "{color=#b7b7b7}{i}I should go out there and have Toby maul this guy... But... Mmm... He just seems so excited...{/color}{/i}"
    "Sophie bobs her head up and down, moving your manhood in and out of her open mouth."
    mc "{color=#b7b7b7}{i}Oh. Ohhh... Thank the Goddess... Mmm...{/color}{/i}"
    "You relax, pressing your hips as tightly against the barrier separating the bathroom stalls."
    "Sophie continues to moan around your cock. It twitches with her movements, hitting the top of her mouth."
    sop "{color=#b7b7b7}{i}Okay... Okay... So it isn't Toby...{/color}{/i}"
    sop "{color=#b7b7b7}{i}I wouldn't put it past Nick to try some bullshit like this... No, it can't be. I've seen his dick. It's nowhere near as thick as this.{/color}{/i}"
    sop "{color=#b7b7b7}{i}...Trevor? That would be a surprise, but the skin tone doesn't match.{/color}{/i}"
    scene GlorySophie8 with Dissolve(2)
    hide window
    w ""
    sop "{color=#b7b7b7}{i}Damn it, whose cock is it in my mouth?!{/color}{/i}"
    sop "{color=#b7b7b7}{i}...[MC]?{/color}{/i}"
    sop "{color=#b7b7b7}{i}No way. It couldn't be. Unless...{/color}{/i}"
    sop "{color=#b7b7b7}{i}Mmm...Fuck it. Who cares? This feels amazing...{/color}{/i}"
    "You feel Sophie's mouth widen around your cock. She inches your erection down her throat."
    mc "{color=#b7b7b7}{i}Mm! Fuck... Sophie hates me, and now she's sucking my cock without even knowing it's me... This has been my dream for so long... I'm gonna cum inside Sophie's mouth!{/color}{/i}"
    "Sophie slips her tongue out, stroking the underside of your cock. You jerk your hips against the stall barrier, desperate for more."
    sop "{color=#b7b7b7}{i}Mmm... He really likes that. If this wall weren't in the way, he would probably shove the whole thing down my throat...{/color}{/i}"
    sop "{color=#b7b7b7}{i}Ah. That's actually kind of exciting to think about.{/color}{/i}"
    sop "{color=#b7b7b7}{i}Fuck Toby. If he had met me like he said he would, maybe he would be getting off right now instead of getting drunk with his idiot friends while his girlfriend sucks some stranger's cock.{/color}{/i}"
    sop "{color=#b7b7b7}{i}At least someone else appreciates this. But if Toby found out...{/color}{/i}"
    sop "{color=#b7b7b7}{i}Shit. That just makes this even hotter!{/color}{/i}"
    scene GlorySophie9 with Dissolve(2)
    hide window
    w ""
    "Sophie leans forward, shoving more cock down her throat until you can practically feel her hot breath against your balls from the narrow passageway of the gloryhole."
    "It's not your whole erection, but it's pretty damn close. You don't bother disguising the grunts and moans of pleasure that escape your throat as she sucks on your manhood."
    "Your cock twitches, and you bang your hips against the wooden barrier, struggling to get as deep down her throat as possible."
    mc "{color=#b7b7b7}{i}Ah... Ah... Fuck, I'm close! If she keeps it up like this...{/color}{/i}"
    "But it seems she's already noticed. Sophie bobs her head up and down, coating your cock in her saliva as she works to pleasure you into your climax."
    sop "{color=#b7b7b7}{i}Oh... Oh, fuck! There's so much cum...{/color}{/i}"
    "You let out a loud, guttural sound as you orgasm, shooting your hot cum into her mouth. Sophie pulls back a little in surprise, then pushes you further into her mouth, struggling to keep all your cum inside, not wasting a single drop."
    "You feel her throat constrict and release as she struggles to swallow your cum from the other side."
    sop "{color=#b7b7b7}{i}There's... there's too much! I can't...{/color}{/i}"
    scene GlorySophie10 with Dissolve(2)
    hide window
    w ""
    "Sophie pulls away from your cock, unable to keep up with the thick spurts of cum being released from your tip."
    "You feel her hand eagerly pump your sensitive skin, coaxing the rest of your cum out."
    mc "{color=#b7b7b7}{i}It must be falling on some part of her. Is it across her face? Her tits? Was she even dressed in there, or did she strip down to nothing?{/color}{/i}"
    "The idea of cumming onto a naked Sophie excites you all over again, sending another spurt from your cock."
    scene GlorySophie11 with Dissolve(2)
    hide window
    w ""
    sop "Shit... Shit! What the hell was that?!"
    sop "You asshole! You came over my entire face!"
    sop "There's so much! It's literally everywhere!"
    "Even though she sounds pissed, you can't help but feel turned on at the mental image of your cum coating Sophie's face."
    sop "It's even in my hair... Gross! I have to really scrub this stuff off before I go back outside."
    sop "I don't even let Toby do this, you know! I've never let anyone cum on my face!"
    scene GlorySophie12 with Dissolve(2)
    hide window
    w ""
    sop "But I just let a stranger do it. And now there's so much of it..."
    sop "{color=#b7b7b7}{i}He must have really liked this. Toby doesn't even cum this much when I give him a normal blowjob...{/color}{/i}"
    sop "{color=#b7b7b7}{i}And he still looks hard! How much more can this guy take?!{/color}{/i}"
    sop "{color=#b7b7b7}{i}I have to know who this guy is. He was definitely in the pub, and there weren't that many of us...{/color}{/i}"
    scene GlorySophie13 with Dissolve(2)
    hide window
    w ""
    "You feel Sophie take the tip of your cock in her hand."
    mc "{color=#b7b7b7}{i}Is she going to keep going...?{/color}{/i}"
    sop "{color=#b7b7b7}{i}I need to find out whose cock this is. It's going to drive me crazy until I do...{/color}{/i}"
    "She leans forward, giving your cock one last, longing lick from her tongue. Your cock bobs in response."
    sop "Now get out. I have to clean up your mess."
    scene blackout with Dissolve(2)
    stop music fadeout 2
    mc "{color=#b7b7b7}{i}Goddess, that felt amazing! I had no idea if she'd really go through with it, but... damn. I should clean myself up as well.{/color}{/i}"
    scene pub exterior night with Dissolve(2)
    "You clean yourself and wait for your erection to go away before going back to the party."
    play sound walkgrass
    show sophie neutral at center with Dissolve(1)
    sop "...No. Fucking. Way."
    mc "Shit."
    play music sophie
    scene GlorySophie14 with Dissolve(2)
    hide window
    w ""
    sop "You fucking creep! What the fuck did you think you were doing?!"
    sop "Just you wait until I tell Toby. He's going to kick your pathetic, scrawny ass."
    "You can't help but smile."
    sop "And what the fuck do you think is so funny?"
    mc "You aren't going to tell Toby."
    sop "Really? And why the hell would you think that?"
    mc "Because you loved every minute of it. You aren't going to tell Toby how much you loved sucking some other guy's cock, right?"
    sop "I didn't-"
    mc "I felt you moaning around my cock the entire time. Shoving it down your throat, swallowing my cum... You loved it. You were having a great time."
    mc "And, worst of all, you knew I wasn't Toby."
    sop "...I don't know what the hell you're talking about. I never-"
    mc "You asked me to tell you who I was halfway through. That kind of gives it away that you knew I wasn't your boyfriend."
    sop "Well, I was... I was drunk! I was confused and... and I wasn't paying attention and..."
    mc "And you still let me cum all over your face. Or were you saying that for dramatic effect?"
    sop "You prick! You shouldn't have been there in the first place! That was supposed to be my boyfriend!"
    mc "And when he didn't show up you didn't seem to have a problem with changing partners. Are you really going to be mad at me for this?"
    sop "Yes!"
    mc "Why? You liked it, I liked it, there's nothing to be upset about."
    sop "There's plenty to be upset about! I didn't want to suck YOUR cock, ew!"
    mc "Sophie, why the hell do you hate me so much? What did I do to you? You're pissed off like, ninety percent of the time!"
    sop "Tch!"
    sop "Well, I'm so sorry we can't always be as happy-go-lucky as you!"
    mc "What's that supposed to mean?"
    sop "Not everyone can have a perfect life like you, [MC]! Some of us actually have to deal with this bullshit reality!"
    mc "{color=#b7b7b7}{i}Oh, it sounds like she's dealing with something serious...{/color}{/i}"
    mc "{color=#b7b7b7}{i}I never even thought to ask.{/color}{/i}"
    mc "Hey, Sophie... what's going on? Is everything okay at home? Did the storm mess things up? It's okay. You can talk to me, you know."
    sop "I don't want to talk to you! About any of it! It's none of your business!"
    "Sophie looks away, but you swear you catch a glimpse of hurt on her face."
    mc "{color=#b7b7b7}{i}What's so bad that she can't talk to me about?{/color}{/i}"
    mc "Sophie..."
    mc "Seems like things are really hard on you right now, but I want you to know that you're very strong and brave to be going through whatever it is you're going through. Especially on your own."
    mc "Just know that you can confide in others, too, okay?"
    sop "...[MC]..."
    scene GlorySophie15 with Dissolve(2)
    hide window
    w ""
    "Her expression softens. Sophie closes her eyes and presses a kiss against your lips."
    "You blink, taken aback. This definitely isn't the response you were expecting."
    "You take in the soft touch of her lips against yours, her warm lips cupping around your upper lip. She traces her tongue over your lip, almost sucking on the skin."
    "Carefully, you place your hands on her hips, guiding her closer. She feels soft and gentle in your arms, words you never thought you'd use to describe Sophie."
    "Slowly, she pulls back, her eyes glazed over and warm."
    "Then she seems to realize what she's done."
    scene GlorySophie16 with Dissolve(2)
    hide window
    w ""
    sop "You creep!"
    "Sophie violently shoves you onto the ground, putting as much distance between you two as she can."
    "You fall back onto hard dirt with a grunt. The rocks and pebbles dig painfully into your back."
    "Before you can get up, Sophie slams her foot down against your crotch. You let out a yelp of pain."
    "She presses the heel of her boot lightly against your balls, pushing down on them. You stare in horror, afraid of what she might do to them."
    sop "Don't think you can say nice things and then plant one on me!"
    mc "But you kissed me..."
    sop "If you ever try to kiss me again, I'll get Toby to kick your ass, and come back personally to finish the job. Understand, creep?!"
    "She puts more pressure on your balls with her boot."
    mc "Yes! Yes! I understand!"
    sop "Do you?!"
    mc "Yes! Yes, Sophie, I get it!"
    "She glowers down at you, keeping a firm pressure on your balls."
    sop "Hmph! What a fucking loser."
    "You let out a gasp of relief when she lifts her foot and makes her way back into the pub."
    "You climb back to your feet, trying to grasp what just happened."
    stop music fadeout 2
    scene pub exterior night with Dissolve(2)
    mc "{color=#b7b7b7}{i}Why did she kiss me if she was just going to be upset about it? I don't get it.{/color}{/i}"
    mc "{color=#b7b7b7}{i}There's a lot you struggle to understand about her right now, though. The blowjob, the kiss, her home life...{/color}{/i}"
    mc "{color=#b7b7b7}{i}It sounds like things are really hard for her at home right now. I wonder if it has anything to do with the storm. That's probably why she's been lashing out so much...{/color}{/i}"
    mc "{color=#b7b7b7}{i}Could she be in some real trouble? What if things are actually really bad? Even dangerous? I need to find out what's going on. Maybe if I can find a way to help, she won't threaten to squash my balls next time. I do like having those attached...{/color}{/i}"
    mc "{color=#b7b7b7}{i}Sigh. There's nothing I can do about it right now.{/color}{/i}"
    $ persistent.sophieglory = True
    $ renpy.end_replay()
    play sound frontdoor
    play music nina2
    show nina neutral with Dissolve(1)
    nin "Hey, is everything OK? I heard Sophie screaming."
    mc "Oh, hey Nina, it was nothing, don't worry about it."
    nin "Hm... Sophie always gives you such a hard time... I don't know why she hates you so much. Anyway..."
    $ SophieGloryHole = 1


label OutsideBreak:
    if SophieGloryHole == 0:
        play sound frontdoor
        show nina neutral with Dissolve(1)
        play music nina2
    nin "What are you doing here alone, [MC]?"
    mc "I just wanted some air. I can barely hear myself think in there."
    nin "Wait, does this mean that the old antisocial [MC] is back?"
    mc "I'll let you know in a couple of hours."
    mc "There's only so much a man can take. Most of the militia guys are OK, but I feel out of place around them."
    nin "I totally understand that, I felt the same way when I started going out with Trevor."
    mc "Yeah... is that why you're out here?"
    nin "I said \"felt\". I was actually looking for you. We haven't really had much of a chance to talk since you got back..."
    mc "Yeah, I know... sorry, it's just been crazy."
    nin "Don't sound so mopey. Your dad's going to make a full recovery, right?"
    mc "Yeah. So they say."
    nin "And I'm glad you're alive too, it would suck to be here without your lazy ass around."
    mc "I am happy too... probably more than you are."
    nin "I could go on and on about how you could have died. But that won't make a difference. I've said it too many times already."
    mc "Only like a thousand times."
    nin "Thousand and one. You could have died."
    mc "You know why I had to go."
    nin "Yeah. I do. I just worry. And that's never stopping."
    mc "I..."
    nin "It's OK... I think. Well, I'll try to keep it OK."
    nin "Life is all about change, that's what grandma always says."
    mc "She's a special lady."
    "Nina laughs."
    nin "You should hear what she says I should do to you!"
    mc "I'm both scared and intruiged."
    nin "I miss this."
    mc "I do too."
    nin "It's like that cave changed everything, you know? I want us to be as close as we were, but..."
    nin "You're not the same. I'm probably not either."
    nin "You're not going to stop this whole danger and adventure thing, are you?"
    mc "I can't promise you that, Nina. This world is... plentifull. And amazing, and mysterious... and dangerous. I just... I feel this new urge. I want to see more."
    nin "So, is this crazy [MC] the new normal now?"
    mc "Sometimes I want to stay here, I really do... to be with the people I love."
    mc "But I... don't know if I can... or even should."
    nin "Just... "
    nin "... I don't want to lose you!"
    mc "I'll be careful, I'm not going to die."
    nin "That's not what I meant."
    "You hold Nina's hands and she stares into your eyes. You move for a kiss but she gently pushes you away."
    nin "I... I can't do this..."
    nin "I already betrayed Trevor once... I'm not this kind of girl. It's not fair to him."
    mc "What about-"
    nin "Aren't you becoming friends with him?"

menu TrevorFriendship:
    "He's okay. [gr]\[Nina Love +1\]" if TrevorFriend > 2:
        mc "Look. He's not what I thought he was. He's kind of an ass, yeah, but I think he really does care about you, so he can't be all bad."
        nin "You really think so?"
        mc "As much as it pains me to say it."
        nin "I feel like such a bitch to him sometimes. I get why he's frustrated, and worst of all I feel like a hypocrite. I won't do anything with him while you and I already..."
        mc "You don't have to if you don't want to."
        nin "Hey, don't give me that look. It's not like you aren't chasing after other girls right now."
        if NinaProposition == 1:
            mc "I told you what I want. I have a reason not to."
        else:
            mc "And why shouldn't I?"
        nin "I... you're right... I mean, I'm right too. This whole thing is complicated."
        mc "It is."
        nin "Look, I'm going inside, the big lug is waiting for me... or really drunk."
        mc "Probably both."
        "Nina smiles and heads inside."
        $ NinaLove += 1
        jump PubParty3
    "Not really \[Nina Love -1\]":

        mc "Not really. I don't think you should trust him."
        nin "Huh? What makes you say that?"
        mc "It's just... I don't think he really loves you the way you deserve. Seems like he cares more about getting in your pants than getting to know you, you know? Anyway, just be careful with those militia guys. He can be a nice guy, just not relationship material."
        nin "Hm, are you sure you're not just feeling a bit jealous and territorial?"
        if NinaProposition == 1:
            mc "Maybe."
        else:
            mc "..."
        nin "He risked his life to help you... because I asked. He didn't ask for anything in return. Well, I mean, he insinuated something, but..."
        mc "See? I told you."
        nin "See what? I feel like such a bitch to him sometimes. I get why he's frustrated, and worst of all I feel like a hypocrite. I won't do anything with him while you and I already..."
        mc "You don't have to if you don't want to."
        nin "Hey, don't give me that look. It's not like you aren't chasing after other girls right now."
        if NinaProposition == 1:
            mc "I told you what I want. I have a reason not to."
        else:
            mc "And why shouldn't I?"
        nin "I... you're right... I mean I'm, right too. This whole thing is complicated."
        mc "It is."
        nin "Look, I'm going inside, the big lug is waiting for me... or really drunk."
        mc "Probably both."
        "Nina smiles and heads inside."
        $ NinaLove -= 1
        jump PubParty3

label PubParty3:
    stop music fadeout 1
    play sound walkinside
    scene pub interior with Dissolve(2)
    play music brooke
    "You follow Nina back into the pub and see Trevor and his friends at the table. Trevor has his head down on the table and he waves at you."
    show luke neutral with Dissolve(1)
    luk "There he is!"
    show trevor neutral at slightleft with Dissolve(1)
    tre "It's you... he's here... I shoulda fought him... you know. Challenge... or whatever."
    luk "We're doing our traditional end-of-night drinking contest."
    mc "And he lost?"
    show lisa neutral at offscreenleft
    show lisa neutral at farleft with Dissolve(1)
    lis "Naaaah.... he won."
    tre "Psh... no! I'm just drunkie!"
    "Lisa points to the back corner of the pub where Toby has passed out."
    show nova neutral at offscreenright
    show nova neutral at slightright with Dissolve(1)
    nov "Mia put up a good fight too, but Lisa was too much for her."
    show mia neutral at offscreenright
    show mia neutral at farright with Dissolve(1)
    mia "Hhhiiii, you're cute, [MC]..."
    nin "Um... he's over there, Mia."
    mia "Hhiii! You're cute, [MC]!"
    mia "And [Nova], you're so sexy! But you never act like it..."
    nov "That's Trevor."
    "Trevor leans forward and slumps out of his chair."
    show nia neutral at offscreenleft
    show nina angry at midleft with Dissolve(1)
    nin "Wow, Trevor... "
    tre "Hi honey... you're so pretty..."
    nin "Thanks. Now let's get you home. Why do you let yourself get this toasted?"
    tre "Sorry... runs in the family..."
    "Nina helps Trevor up and walks him out the door."
    hide nina with easeoutright
    hide trevor with easeoutright
    mia "So sweet."
    nov "If you want to call it that."
    luk "So, looks like there's an open chair if you're up for the challenge, [MC]."
    lis "You're gonna take him on, Luke? That's not even close to fair... he's a rookie."
    mc "I feel like I need to be part of this conversation, but somehow I'm not."
    luk "I'm challenging you, man. Simple, we pound back the drinks until one of us can't anymore."
    luk "So, what do you say? You're the only one left."
    mc "Wait... so why is everyone else here?"
    show laura neutral at slightleft with Dissolve(1)
    lau "Witnesses. And none of us are going to take on Luke."
    nov "I'd try, but someone has to make sure you get home safe... ish... and I'm taking on Mia duty!"
    lis "And Sober McBuzzkill Evelyn is the referee. Hey! Eve! Come here!"
    show evelyn neutral at center with Dissolve(1)
    eve "I heard that, Lisa."
    lis "Still love ya..."
    eve "Uh-huh. But yeah, I brought some more rum."
    lis "Now that's what I'm talking about!"
    lau "Come on! What do you say, [MC]?"
    mc "Uh..."
    mc "Alright... I'm in."
    lau "Woo! Ten gold on [MC]."
    luk "I'll take that bet."
    nov "Ten on Luke."
    eve "I'll take that bet, then."
    "You raise your eyebrow and give [Nova] a dirty look."
    nov "Hey... I know you better than anyone here. Sorry, no way you win."
    mia "Gooooo! [MC]! Gooo!"
    nov "You've got a cheering squad."
    luk "OK, I respect the attempt, but you're still going to lose."
    lau "This should be a good show!"
    eve "I'll get the drinks ready."
    hide evelyn with Dissolve(1)
    luk "So, are you ready?"
    mc "Let's do this!"
    scene blackout with Dissolve(2)
    "You and Luke begin to pound back shots of rum. It's not too bad at first, but as the contest continues, your vision begins to blur."
    scene pub interior with Dissolve(2)
    show luke neutral with Dissolve(1)
    luk "Giving up?"
    mc "Did I say I was?"
    luk "Then keep up."
    "Luke speeds up the pace of his drinking, and you keep up with him somehow."
    luk "I... think I'm going to..."
    hide luke with Dissolve(1)
    "Luke passes out on the table."
    show lisa neutral at offscreenleft
    show lisa neutral at farleft with Dissolve(1)
    lis "Shit! Luke actually lost. Never saw that coming."
    show laura neutral at slightleft with Dissolve(1)
    lau "HA! That's 10 gold you owe me, Lisa."
    lis "Well, technically Luke owes you, but fine..."
    lau "Victory!"
    show evelyn neutral with Dissolve(1)
    eve "Are you still with us, [MC]?"
    mc "My vision's swimming a little. But I'm still good..."
    lau "Good job, [MC]!"
    show nova neutral at offscreenright
    show nova neutral at slightright with Dissolve(1)
    nov "I can't believe this..."
    mc "Should have bet on me..."
    nov "Bah, whatever."
    show mia neutral at offscreenright
    show mia neutral at farright with Dissolve(1)
    mia "Who won? Did [MC] win?"
    nov "Yeah."
    mia "Yea!!!! I knew it! [MC] can do anything! He's full of surprises!"
    "Mia slumps over."
    jump AfterContest


label AfterContest:
    scene blackout with Dissolve(2)
    stop music fadeout 1
    "You blackout. You remember bits of motion and coversation all around you, but little else."
    nov "OK, let me get her home..."
    eve "Yeah..."
    mia "BYEE!!!"
    "You try moving, but your body decides for you that the spot you're in is far too comfortable."
    "Eventually your comfort is broken by a soft push on your shoulders."
    scene pub interior with Dissolve(2)
    show evelyn neutral with Dissolve(1)
    play music evelyn
    eve "Hey... you with us?"
    "Your head feels like it's filled with cotton."
    mc "Ugh... sort of..."
    eve "And this is why I don't drink."
    mc "You said to drink... so..."
    eve "I know, I know... You're gonna regreat this so much in the morning though!"
    "Evelyn tries to help you up, but you push her aside. She laughs, softly."
    eve "Don't worry, I got you for now."
    mc "'s party over?"
    eve "Yes, it's quite late. Everyone went home."
    mc "I should... get home too..."
    eve "That's probably a bad idea. We have a free room upstairs you can use, I'm putting you up there."
    mc "Awesome! You're the beeeest..."
    eve "Let me help you..."
    jump EvelynAfterParty


label EvelynAfterParty:
scene pub bedroom with Dissolve(2)
mc "Is this my room?"
show evelyn neutral with Dissolve(1)
eve "No, [MC], we're at the inn. It's a guest room."
mc "Oh... do I have to pay?"
eve "No, you're all good."
mc "You're so nice... always so polite and kind!"
mc "And sooo... pretty."
eve "OK, OK, and you're sooo... drunk!"
"Evelyn laughs warmly."
eve "But thank you. Let's just see if you remember that in the morning."
mc "I'll remember... I have a great memory. I remember all sorts of stuff."
eve "Come on, let's get you into bed."
mc "Beds are comfortable."
eve "Well, now I know what kind of drunk you are."
mc "What do you mean?"
eve "For example, Lisa gets wild when she's drunk. Toby gets angry and also really touchy feely with the guys. Sophie becomes... more Sophie."
mc "More Sophie Sophie... that sounds scary."
eve "Trevor gets into oversharing mode, Luke falls asleep. And don't even talk to me about how handsy some of the older guys can get."
mc "You didn't list me there."
eve "I hadn't seen you drunk before. You, sir... Well, you're a happy drunk."
mc "Woo!"
eve "Exactly."
eve "Now come on."
scene EveBed1 with Dissolve(2)
hide window
w ""
eve "You spilled some rum on your clothes - if you sleep like this the sheets will stink. Here, let me help you take these off."
mc "Whoa, that seems inappropriate. If I had a girlfriend she'd be angry. Do you have a girlfriend?"
eve "Come on, help me out here!"
mc "OK, OK."
scene EveBed2 with Dissolve(2)
hide window
w ""
"Evelyn lays you in bed and takes off your shirt and shoes."
eve "Uh, it's like trying to move a sack of potatoes. Can't you help me even a little? I suppose we'd better get these off of you too, get you all comfy"
"Evelyn crawls up your legs and reaches for your waistband."
mc "I... Evelyn, you're..."
eve "What?"
mc "I just... I think I'm sobering up, I can do this myself."
eve "Sure, sure, now you wanna help. Lift your hips already!"
mc "{color=#b7b7b7}{i}Goddess... the way she's looking at me...{/i}{/color}"
"Evelyn removes your pants."
scene EveBed3 with Dissolve(2)
hide window
w ""
eve "Wow! [MC]! I wasn't expecting that..."
mc "I'm so sorry! It's this whole situation..."
eve "Really? Wow, sorry! I didn't think about it, honestly."
scene EveBed4 with Dissolve(2)
hide window
w ""
eve "Most guys can't get it up when they drink as much as you did."
mc "Oh, well, I guess I'm not most guys. I can barely keep this thing under control most of the time."
mc "And I don't think anyone could stay soft in this situation."
eve "..."
mc "I mean, you realize how hot you are, right? And you're so nice and thoughtful. Being with you here... I guess it's impossible not to get a reaction."
eve "You're being too sincere, aren't you? It's a good look on you. You really think that of me?"
scene EveBed5 with Dissolve(2)
hide window
w ""
"Evelyn sits down next to you. She looks a bit lost in her own thoughts but she smiles warmly."
mc "Is that OK to say? I'm sorry if-"
eve "Well, it's sweet."
"You look down on your erection and blush."
"Evelyn grins slightly as she sees you shifting uncomfortably."
eve "Hey, [MC]..."
mc "Yeah?"
eve "Why did you get into that drinking contest?"
mc "I'm not sure. It just seemed like the thing to do?"
eve "Why, though?"
mc "..."
eve "Why bother? You're not like them, and I think it's a good thing."
mc "I thought you liked them."
eve "I do. They've been my friends for a long time now."
mc "See? They are popular. I, on the other hand... not so much - most people just see me as this weird guy."
eve "Hey, I'm your friend too!"
mc "Thanks. And I'm sorry, I guess I really don't have any guy friends either. Sam left around the time [Nova] moved over, and Marcus... he's odd."
mc "So between that, and always feeling underappreciated compared to those guys... I know it's dumb."
eve "It's not dumb. But here, how about this for some appreciation?"
scene EveBed6 with Dissolve(2)
hide window
w ""
"Evelyn kisses you on the lips, sensually, but still kind of innocently."
eve "You're one of the good guys, [MC]. So whenever you're feeling a bit unappreciated, just remember you are the guy who kissed the 'hot' bartender after the party!"
mc "I... Wow."
eve "Hey, no more sad [MC], OK? I want to see more of that happy guy from a few minutes ago, without all the booze preferably! Feel better now?"
scene EveBed7 with Dissolve(2)
hide window
w ""
eve "You don't have to answer... because you're poking me pretty hard."
mc "{color=#b7b7b7}{i}She's grabbing my cock... wow! I never thought this could ever happen! Even if it's just over my underwear, feeling her hand touching my cock is...{/i}{/color}"
"Evelyn teases you with a smile."
eve "I should let you get to bed now."
mc "Are you going home this late?"
eve "It is pretty late..."
mc "And isn't it a bit dangerous? Nocturnal monsters can be a problem. I don't think there are people on guard in the streets tonight."
eve "You're right, I'll stay here. The bed's big enough, and I'm really tired from all the work."
scene EveBed8 with Dissolve(2)
hide window
w ""
eve "I just need to get rid of these uncomfortable clothes. It's impossible to sleep on them."
"Evelyn starts undressing in front of you."
scene EveBed9 with Dissolve(2)
hide window
w ""
mc "{color=#b7b7b7}{i}Whaaat? Is this a dream?{/i}{/color}"
mc "{color=#b7b7b7}{i}She's... where does she even find underwear like that? I can see her whole ass.{/i}{/color}"
"Evelyn looks down at her underwear and blushes a bit."
eve "Hey, stop staring over there."
mc "Uh... too late."
scene EveBed10 with Dissolve(2)
hide window
w ""
"Evelyn sighs."
eve "At least you're honest."
eve "Come on, if you could so kindly make some room."
"Evelyn climbs over you and as she does so her knee brushes against your erection."
mc "Ow, careful there."
eve "I won't hurt you."
mc "That's not what I..."
scene EveBed11 with Dissolve(2)
hide window
w ""
eve "Hey, let's just go to sleep..."
mc "Yeah."
eve "And just try not to..."
mc "{color=#b7b7b7}{i}Those tits are magical.{/i}{/color}"
mc "What?"
eve "Eyes up here, tiger."
mc "I didn't mean to stare, sorry!"
eve "Just... turn over."
scene blackout with Dissolve(2)
"A few minutes later."
scene EveBed12 with Dissolve(2)
hide window
w ""
mc "{color=#b7b7b7}{i}She's sleeping already. Damn, I can't sleep! I'm in bed with Evelyn, and she's in her underwear!{/i}{/color}"
mc "{color=#b7b7b7}{i}It's hard to ignore this erection and sleep. Play it cool... I'll stay up all night if I need to, go home in the morning, then jerk off all day to relieve the tension.{/i}{/color}"
mc "{color=#b7b7b7}{i}Sounds like a plan.{/i}{/color}"
scene blackout with Dissolve(2)
"Eventually you fall asleep to thoughts of Evelyn."
stop music fadeout 2
scene blackout with Dissolve(5)
scene EndOfChapter5 with dissolve
"To be continued. Now would be a good time to save."
"Thank you for playing Love Season. Please look forward to our next chapter and consider helping us on Patreon, join our Discord and check our other game - Farmer's Dreams!"
$ persistent.ch5 = True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
