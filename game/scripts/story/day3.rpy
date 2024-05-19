label day3_morning:
    'DAY 3 - MORNING - IF TIME'
    call hero_paths_choice from _call_hero_paths_choice_1
    return

label day3_combat:
    ## NEW SCENE: Day 3 combat
    ## FADE IN to WASTELAND. Hollow wind or desert sound.
    pause 1.0
    scene wasteland with fade
    play music foley_desert_wind fadein 1.0

    ## The group is traveling in search of examples of more obvious malevolent forces. What once might have been a sprawling city can barely be discerned from the rest of the landscape, with only a few walls or building frames sticking up here or there.
    
    ## SLIDE IN Lance
    show lance at grouped_left_lance
    with easeinleft
    lance "“It’s so obvious no one has been here in a long time.”"
    lance "“I thought we were past you wasting our time, Guide.”"
    guide "“Gods, you’re an impatient little brat.”"
    guide "“Hold your tongue for longer than five seconds and you might actually learn something.”"
    
    ## SLIDE IN Gavin
    show gavin at grouped_right_gavin
    with easeinleft
    gavin "“Yeah, Lance... sheesh.”"

    ## SLIDE IN Morgan
    show morgan at grouped_right_morgan
    with easeinleft
    lance "“Oh, I’m sorry, I didn’t realize we were monks now.”"

    ## SPRITE Morgan A
    show morgan annoyed with dissolve
    morgan "“What’s a monk..?”"
    gavin "“I think it’s like half a monkey.”"

    ## SPRITE Morgan SD
    show morgan sad
    morgan "“... What’s a monkey..?”"

    ## LANCE tries not to laugh.
    show lance happy with dissolve
    lance "“Ppfft.”"

    ## SPRITE Morgan ANG
    show morgan angry
    morgan "“It’s not funny, Lance! Not everyone came from the ruins of a college town like you!”"

    ## SPRITE Lance A
    show lance annoyed
    lance "“Didn’t you and Gavin live in the ruins of a zoo for a few months?”"
    gavin "“That’s what the adults told us. But it was all indoors, and all the animal cages were small and had beds and toilets.”"

    ## SPRITES all N
    show morgan neutral
    show lance neutral
    show gavin neutral
    with dissolve
    guide "“For the love of -- be quiet, all of you.”"
    guide "Gods of patience and mercy, grant me strength while I remember why I decided to never have kids..."
    guide "“Listen up. I told you all why we came out here, now I will tell you again.”"
    guide "“If you want to have any chance of finding and defeating the Hidden Darkness, you must learn to find its vestiges in unlikely places.”"
    guide "“The corruption born from the Darkness first took root in places like this.”"

    ## SPRITE Gavin SD
    show gavin sad
    gavin "“It... doesn’t look like there’s anything here?”"
    guide "“Precisely.”"
    guide "“All the darkness can do is warp, corrupt, and consume, until there’s nothing left to change. Then, it moves on to where it can find something new to destroy.”"
    guide "“That does not mean it doesn’t haunt what it leaves behind.”"
    guide "“Listen closely. Attune yourself to the environment. Concentrate hard enough, and you will hear the ghosts of the past that could not move on.”"
    guide "“Listen closely, and you’ll find the agony that remains.”"

    ## SPRITES all N
    show gavin neutral
    pause 1.0
    morgan "“... Maybe we can try that bigger building over there? It looks like it was important once.”"
    lance "“Crumbled pillars, barred window frames, stone steps... either a place of government or finance.”"
    lance "“Not a bad idea.”"
    guide "“Lead on, then.”"

    ## FADE OUT character sprites
    hide gavin
    hide morgan
    hide lance
    with dissolve

    ## FADE IN to DESTROYED BUILDING INTERIOR. Some sort of echoey ambiance.
    scene ruined_building_interior with fade
    play music foley_abandoned_building fadein 1.0
    
    ## FADE IN character sprites.
    show gavin at grouped_left_gavin
    show morgan at grouped_left_lance
    show lance at grouped_left_morgan
    with dissolve

    guide "I can already feel the chill of tragedy and pain deep in the walls."
    guide "This place may be more than they’re ready to handle..."
    ## SLIDE OUT Morgan, CENTER ON Gavin and Lance
    hide morgan with easeoutleft

    show gavin at grouped_center_gavin
    show lance at grouped_center_lance
    with move

    ## SPRITE Gavin H
    show gavin happy
    play sound rubber_duck
    gavin "“Whoa, check this out! There’s half a rubber duck sitting on the desk here!”"
    lance "“You know what a rubber duck is, but not a monkey?”"
    lance "“Let me see that.”"

    ## SPRITE Gavin A
    show gavin annoyed
    play sound rubber_duck
    gavin "“No way! I found it first.”"

    ## SPRITE Lance A
    show lance annoyed
    lance "“I wasn’t gonna {i}take{/i} it from you, idiot, I just wanted to look.”"
    guide "“Lance, we don’t use that language here.”"
    guide_dark "Hah! You sound like mother!"
    gavin "“Yeah, Lance, be nice to me.”"
    gavin "“I’m the leader after all.”"

    ## SPRITE Lance ANG
    show lance angry
    lance "“We agreed no one was a leader!”"

    ## SPRITE Gavin ANG
    show gavin angry
    gavin "“Well it doesn’t make sense {i}not{/i} to have one! There has to be someone who tells the others what to do!”"
    lance "“I don’t need you telling me {i}anything!{/i}”"
    guide "“Enough of that --”"
    gavin "“Well when I don’t say anything, you just end up being a huge {i}jerk{/i} all the time!”"
    gavin "“Being smarter than us doesn’t make you better!”"
    lance "“You know what it {i}does{/i} make me? Better fit to be a leader.”"
    lance "“Just because the Roots of the World spoke to {i}you{/i} first doesn’t mean you’re in charge by default!”"
    guide "“Boys --!”"
    guide_dark "Conflict? Already? No. This is unacceptable --"
    gavin "“We probably wouldn’t have made it here if you’d been leading us! You probably would have made someone mad enough to leave us to starve when we were jumping from camp to camp!”"
    lance "“We wouldn’t have wasted time being their {i}errand dogs{/i}, because you always have to please everyone so they won’t leave you like --”"
    guide_dark "“Ignorant fools, I said {i}silence!{/i}”"

    ## The boys do stop arguing, looking surprised. Meanwhile, the sound of something dropping heavily around the corner, followed by a strange groaning.
    ## SPRITES Lance UNC, Gavin SP
    show lance uncomfortable
    show lance surprised
    play sound object_falling
    stop music fadeout 0.25
    pause 0.25
    play sound monster_groan
    
    ## SLIDE IN Morgan
    ## SPRITE Morgan UNC
    show morgan uncomfortable at grouped_center_morgan
    with easeinright
    morgan "“... It’s here..!”"
    gavin "“Was it attracted by our noise? Or by..?”"
    lance "“Less questioning, more killing.”"
    guide "“Just -- focus on the sensation of its aura. Pay attention to the way you’re feeling. How the air has shifted.”"
    guide "“Consider what must have transpired here for such corruption to take root...”"
    guide "“And know that you can find it {i}anywhere{/i} if you look hard enough.”"
    guide "“Nothing is sacred.”"
    guide "“And nothing -- no one -- is guaranteed to protect you.”"

    ## There’s a ROAR, BEGIN COMBAT
    play sound monster_roar
    call combat_encounter_corrupted_weak from _call_combat_encounter_corrupted_weak
    ## AFTER COMBAT
    scene ruined_building_interior with fade
    play music bgm_the_two_siblings
    play music_extra foley_abandoned_building fadein 1.0

    ## SPRITES Gavin UNC, Morgan UNC, Lance N
    show gavin uncomfortable at grouped_center_gavin
    show morgan uncomfortable at grouped_center_morgan
    show lance at grouped_center_lance
    with dissolve
    call restore_from_combat from _call_restore_from_combat_3
    gavin "“I -- I’ve never seen one so close, until now... it was always the adults who fought them, or... disappeared with them.”"
    gavin "“I... I didn’t know they were...”"
    morgan "“They’re -- they {i}were{/i} -- human...”"

    ## SPRITE Lance A
    show lance annoyed with dissolve
    lance "“Really? You guys didn’t know {i}this?{/i}”"
    lance "“Not knowing what a monkey is, fair enough. But how could you not know the Corrupted were once living things?”"
    lance "“It’s like Guide said; they weren’t born from nothing.”"

    ## SPRITE Morgan ANG
    show morgan angry
    morgan "“He said they were born from the Darkness! Not... {i}this{/i}.”"
    guide "“They do originate from the Darkness, yes.”"
    guide "“But just like the Hidden Darkness begins within the heart and soul of a single person, the corruption within the Darkness also requires a host to grow and spread.”"

    ## SPRITES Gavin SD, Morgan A, Lance N
    show gavin sad
    show morgan annoyed
    show lance neutral
    with dissolve
    gavin "“... We didn’t know...”"
    gavin "“Why wouldn’t they have told us? The adults we traveled with -- they had to have known, didn’t they?”"
    gavin "“Why didn’t they tell us..?”"
    guide_dark "Hmm... to leave them ignorant for so long..."
    guide_dark "Good. That leaves them more malleable to their destiny."
    guide "I don’t want to hear it."
    lance "“If you’d been paying attention, you probably could have figured it out on your own, you know.”"
    lance "“I guarantee someone you once knew is one of these things now. It’s statistically improbable for them {i}not{/i} to be.”"
    lance "“Everyone falls to these things eventually.”"
    lance "“Everyone becomes Corrupted, eventually.”"

    ## SPRITES Morgan SP, Gavin SP
    show morgan surprised
    show gavin surprised
    gavin "“... We’re all vulnerable..?”"
    gavin "“Even us? Even though we know better?”"
    guide "“No one is immune to the Darkness.”"
    guide "“That’s why you must learn to be aware of it in {i}every{/i} corner it may lurk, building {i}or{/i} soul. Like I said before.”"
    
    ## SPRITES Gavin SD, Morgan SD
    ## Everyone pauses for a moment in contemplation.
    pause 0.5
    show gavin sad
    show morgan sad
    pause 0.5
    gavin "“... Can we go home now?”"
    guide_dark "He can’t be tired already. That was only one --"
    guide "We can go home."

    ## FADE OUT
    ## FADE OUT Music/sfx
    $ transition_hold_seconds = 2.0
    call end_scene_fade_to_black_pause from _call_end_scene_fade_to_black_pause

    ## END SCENE
    return

label day3_dinner:
    ## NEW SCENE: Day 3 dinner
    ## BLACK SCREEN
    scene backdrop_black
    guide "The journey home was unusually quiet. The heroes had been rambunctious when they first came to me. Morgan was even more subdued than she had been when she first arrived at my doorstep."
    guide "Naturally, they had much to consider. It seems it hadn’t occurred to them before that the Darkness they’d been taught to fear could lurk in the hearts of those they trusted most."
    guide "But questioning everything is the first crucial step in directing them towards what they were Chosen to do."
    guide "If they remain ignorant and complacent in who they believe is friend or foe..."
    guide_dark "They’ll never reach the potential they need to continue the cycle."
    
    ## FADE IN to CABIN INTERIOR
    ## FADE IN Fireplace sfx, FADE IN Music
    scene cabin_interior with fade
    play music_extra foley_fireplace volume 0.5
    play music bgm_transient fadein 1.0
    
    ## SPRITES Gavin SD, Morgan SD, Lance N
    show gavin sad at linedup_center_gavin
    show lance at linedup_center_lance
    show morgan sad at linedup_center_morgan
    with dissolve
    gavin "“... Guide? How do we know we’re not corrupted?”"
    guide "“You would know.”"
    gavin "“But how?”"
    guide "“{cps=30}...{/cps}”"
    guide "“You would hate everyone, and everything. Even those you once loved most.”"
    guide "“Everything would feel pointless, a waste of time and energy to care for. At the same time, those same things would be valuable to you only in what they could offer in service to your own joy or survival.”"
    guide "“You would want everything they could offer, without providing anything in return.”"
    guide "“Put simply, hatred and hopelessness would become an addiction, because no other emotion could compare.”"
    morgan "“But that makes it sound like... the Corrupted could be saved?”"
    lance "“What?”"

    ## SPRITE Morgan SP
    show morgan surprised
    morgan "“If what makes someone corrupted is hate and hopelessness, they just... need to have hope again, right?”"
    morgan "“Couldn’t that bring them back?”"
    guide "“I assure you, if it were so simple --”"

    ## SPRITE Lance A
    show lance angry
    lance "“That’s {i}stupid{/i}. All Corrupted are beyond saving.”"
    lance "“Didn’t you feel it in the air when we were in that building earlier? It sucked life right out of the room -- right out of us.”"
    lance "“It wasn’t a thing that could be reasoned with.”"

    ## SPRITE Morgan A
    show morgan angry
    morgan "“How do you know that, Mr. Know-It-All? Have {i}you{/i} tried before?”"
    morgan "“If they were once people, wouldn’t there still be something left there that was once part of them? Who they used to be?”"
    lance "“You mean their organs? Their body? Sure, that’s all probably still there.”"
    lance "“Even if it’s nothing more than disintegrated {i}goop{/i}.”"
    lance "“The body is still there, though changed. But the actual {i}person{/i}? I assure you, that part died ages ago.”"

    show morgan angry at sprite_shake_light
    morgan "“That can’t be true!”"
    guide "“Morgan, calm yourself.”"
    guide "“Lance is correct. All that remains of the person the Corrupted once was is their deepest hatred and sorrow.”"
    guide "“Of any emotion left, all they have is that, and a profound sense of betrayal.”"
    
    ## SPRITE Morgan ANG
    show morgan angry
    morgan "“Betrayal?”"
    morgan "“Of course they would feel betrayed! Those were once people’s friends! Family members!”"
    morgan "“And they were just left behind to die!”"

    ## SPRITE Lance ANG
    show lance angry
    lance "“How was anyone going to save them, Morgan?”"
    lance "“It would have been a waste of resources and time even if they {i}could{/i} be brought back.”"
    
    ## SPRITE Gavin A
    show gavin annoyed
    morgan "“How could you {i}say{/i} that?!”"
    lance "“They’re {i}monsters{/i}, Morgan! There’s nothing human left in them!”"
    gavin "“Guys -- guys, please, let Guide tell us. I know he has something more to say about all of this.”"
    
    ## SPRITE Gavin SD
    show gavin sad with dissolve
    gavin "“Right?”"

    ## CHOICE
    ## >Let them discuss their thoughts and theories
    ## >Tell them the history of the Corrupted
    ## (The first choice of the game that leads to two different potential scene outcomes. There are still no long term consequences due to time constraints with the jam however.)

    menu:
        "Let them discuss their thoughts and theories":
            jump day3_dinner_choice_theories
        "Tell them the history of the Corrupted":
            jump day3_dinner_choice_history

    ## >Let them discuss their thoughts and theories
    label day3_dinner_choice_theories:
        guide_dark "Deciding not to intervene? Oh, this could get interesting."
        guide "“This could be a valuable learning moment for you all. Keep going.”"

        ## SPRITE Gavin SP
        show gavin surprised
        gavin "“Huh --?”"

        ## SPRITE Lance A
        show lance annoyed
        lance "“I’ll take your decision to be quiet as a point for my case.”"
        show gavin neutral
        lance "“Think about it, Morgan; where do we decide what’s human and what {i}isn’t?{/i}”"
        lance "“Is a {i}thing{/i} that doesn’t think, speak, or {i}feel{/i} like we do human?”"
        morgan "“That doesn’t matter!”"
        lance "“Why?!”"
        lance "“Is a deer with a parasite controlling its body still the deer? Or is it the parasite?”"
        lance "“Actually, think about those hollow sea shells crabs make into their home sometimes. Do you see the shell as part of the crab?"
        morgan "“I mean, I guess I do. But–”"
        lance "“The shell was {i}once{/i} its own living thing. Now it’s not. Now it’s just part of the crab.”"
        lance "“So a corrupted creature, no matter whether you can still tell it was human once, is still a corrupted creature.”"
        morgan "“That’s not a good comparison! They’re not crabs!”"
        morgan "“They could still be alive in there, those people. Suffering, in a lot of pain.”"
        morgan "“They have to be. The Corrupted feed off of energy and life, right?”"
        morgan "“It has to be...”"
        morgan "“Because they’re alive! Right?”"
        gavin "“I -- I don’t think they are. When we destroyed the Corrupted earlier today, it just sort of... melted.”"
        gavin "“People -- humans -- don’t do that.”"
        morgan "“And people didn’t do {i}magic{/i} a thousand years ago either!”"
        morgan "“Things changed! The world changed!”"
        morgan "“What’s normal is different now!”"

        ## SPRITES Morgan UNC, Lance UNC, Gavin ANG
        show gavin angry
        gavin "“My mom didn’t {i}melt{/i} when {i}she{/i} died!"
        show morgan uncomfortable
        show lance uncomfortable
        with dissolve
        gavin "“... Maybe Lance is right. Me, I don’t think it matters what they are.”"

        ## SPRITE Gavin A
        show gavin angry
        gavin "“They’re dangerous, they want us to die, so they have to die first.”"

        ## SPRITE Morgan SD
        show morgan sad
        morgan "“But...”"

        ## SPRITE Lance N
        show lance neutral
        lance "“Oh, for the love of -- get it through your skull, Morgan!”"
        lance "“Whatever is there isn’t worth {i}saving{/i}.”"
        lance "“All it does is hurt us.”"
        morgan "“{cps=30}...{/cps}”"

        ## SPRITE Morgan A
        show morgan annoyed
        morgan "“... But wasn’t it this kind of thinking that destroyed the world?”"
        morgan "“That some people aren’t worth saving?”"

        ## SPRITES Gavin SD, Lance UNC
        show gavin sad
        show lance uncomfortable
        morgan "“‘Not all those who wander are lost.’”"
        morgan "“I read that in a book once.”"
        morgan "“A really boring book.”"
        morgan "“But when we leave others behind in favor of ourselves... aren’t we leaving pieces of ourselves behind, too?”"
        morgan "“And aren’t we {i}heroes?{/i}”"

        ## SPRITE Morgan ANG
        show morgan angry
        morgan "“What’s the point of saving the world if we don’t think about what it takes to get there, and if there’s a better way?”"

        ## SPRITES Gavin SD, Lance SD
        show gavin sad
        show lance sad

        ## PAUSE
        pause 1.0
        guide "... There is {i}no{/i} reason these kids should be so introspective."
        guide_dark "I blame the tall one."

        ## SPRITE Morgan N
        show morgan neutral
        gavin "“Well, Guide?”"
        gavin "“Anything to say to... all of that?”"
        guide "“{cps=30}...{/cps}”"
        guide "“You all have very valid points.”"
        guide "“To fight and kill what seeks to kill you and think no deeper of it is natural.”"
        guide "“And to mourn the loss of agency and life is profoundly empathetic.”"
        guide "“I will tell you directly, though: the people the Corrupted may have once been no longer exist.”"

        ## SPRITE Morgan A
        show morgan annoyed
        guide "“But asking questions, asking about the nature of things and why they are, is just as important as the rest of your training.”"
        guide "“Hone your physical skills, and hone your minds to understand not just how, but {i}why{/i}.”"
        
        ## PAUSE
        pause 1.0
        guide "“... Go to bed, now.”"

        ## HEROES SLIDE OUT one by one, Morgan is last.
        hide gavin with easeoutleft
        hide lance with easeoutleft
        pause 0.5
        hide morgan with easeoutright

        guide_dark "So close, and yet so far."
        guide_dark "I have to say though, that was {i}extremely{/i} entertaining."
        guide "I should have told them..."
        guide_dark "Told them? Told them what?"
        guide_dark "That their predecessors failed them? They know that. That’s all they’ve known."
        guide_dark "What they don’t understand is how and why."
        guide_dark "And why {i}you{/i} will do the same."
        guide "{cps=30}...{/cps}"
        guide "I know. You don’t have to rub it in."

        ## The screen throbs red
        show overlay_red onlayer foremost at flash_overlay
        guide_dark "{i}Thus, always{/i}."

        ## FADE OUT
        ## END SCENE
        jump day3_dinner_end
    
    ## >Tell them the history of the Corrupted
    label day3_dinner_choice_history:
        guide "“I do have information for you all, yes.”"
        guide "“Settle down, all three of you. There is more yet to be told about the Hidden Darkness and the Corruption it wrought upon our world.”"

        ## SPRITES Gavin A, Lance N, Morgan A
        ## The HEROES settle back down. LANCE and MORGAN are still angry with each other, but they’re not fighting anymore.
        show gavin annoyed
        show lance neutral
        show morgan annoyed
        guide "“As Morgan said last night, the Corrupted are mutated masses. They {i}are{/i} dangerous, and they {i}are{/i} necrotic in nature.”"
        guide "“And, as Morgan said, it would sooner kill you than run away. The promise of taking a life is too great to turn away from.”"
        guide "“The people they once were truly no longer exist. The fact that they were once human does not change what they desire now. All that matters to the Corrupted is their own survival and growth of power.”"

        ## SPRITE Gavin SD
        show gavin sad
        gavin "“If that’s true, and if the Corrupted started appearing early on in the first days that the Hidden Darkness awoke...”"
        gavin "“Then it would have sought out the most powerful people to feed off of, right?”"
        guide "“Yes, exactly.”"

        ## FADE OUT to black, FADE IN to image of pandemonium/some sort of societal chaos
        scene burning_city with dissolve
        guide "“The Corruption did not spread like a normal disease, like a cold or flu. The disease was neither virus nor bacteria, nor was it a fungus or parasite.”"
        guide "“Because the Corruption sought the most powerful people first, political and financial leaders, research for a cure began immediately, but there was nothing scientists could find to cure, in the traditional sense.”"
        guide "“It is a disease of the very soul itself. It is {i}incurable{/i}.”"
        guide "“Because those who ruled at the time were selfish and cruel regardless, the Corruption was, at first, cause for celebration for the common populace. It seemed the worst of humanity would be the only ones impacted.”"
        guide "“That celebration did not last long when the leaders who {i}did{/i} remain saw an opportunity to take advantage of their enemies’ weaknesses.”"
        guide "“They garnished their wars with all manner of excuses. Some bought into them. Most of us knew better.”"
        guide "“All the same, the more war, famine, and disease spread in a mad grab for power, so too did the Corruption.”"
        guide "“The belief that it would dissipate when the most cruel and powerful people were eradicated quickly died.”"
        guide "“Even when people ceased to volunteer to take up the positions of the deceased, the Corruption no longer seemed to differentiate between the worst of us, and those considered only mildly nefarious.”"
        guide "“By the time the Corruption began to spread to animals, and then to the land itself, it was far too late for any substantial action to be taken.”"
        guide "“All institutions of order and aid crumbled. The few remaining civilizations left dispersed with no central power to maintain them.”"
        guide "“The actions of a select few in the beginning of the end of the world, is what led to it all spiraling so far out of hand to begin with.”"
        
        ## FADE OUT to black, FADE IN to CABIN INTERIOR
        scene cabin_interior with Fade(0.5, 1.0, 0.5)
        stop music fadeout 2.0

        ## SPRITES Gavin SD, Morgan SD, Lance SD
        ## The HEROES sit in silence yet again.
        show gavin sad at linedup_center_gavin
        show lance sad at linedup_center_lance
        show morgan sad at linedup_center_morgan
        with dissolve

        guide_dark "Too much all at once -- you’ve broken their hearts."
        guide "I so wish you would go back to sleep."
        guide_dark "And miss all the build up? Miss all the fun?"
        lance "“... You’re saying... this all could have been stopped?”"
        lance "“That if everyone had seen what was happening for what it was, none of this would have happened?”"
        guide "“... I don’t know.”"
        guide "“I am saying that there were signs.”"
        guide "“Truthfully, if it could have been stopped, I don’t know what could have been done.”"
        guide "“The existing institutions of power had been determined for a very long time to minimize the power of the people beneath them, to the point of irrelevance.”"
        guide "“That included the power to gather.”"
        lance "“So they made themselves vulnerable by shutting out the people they were supposed to protect?”"
        lance "“... How did these institutions find out about the Hidden Darkness then, if all they were really concerned about was the Corruption right in front of them and how to use it against their enemies?”"
        guide_dark "{i}Now{/i} you’ve got them thinking."
        guide_dark "But it’s not time to tell them that yet."
        guide "“That can be discussed later. It’s time for you all to turn in for the night.”"

        ## SPRITE Gavin A
        show gavin annoyed
        gavin "“But -- they were more technologically advanced. They must have had a way to detect the Hidden Darkness that’s better than just... ‘{i}feeling{/i} the air’ for it.”"
        guide "“Haven’t you had enough of me yapping, boy?”"
        guide_dark "“You’ll learn what you need to know when you need to know it.”"

        ## SPRITES Gavin SP, Morgan SP, Lance UNC
        show gavin surprised
        show morgan surprised
        show lance uncomfortable
        pause 1.25
        
        ## The HEROES look at each other nervously. They FADE OUT from the table one by one.
        hide gavin with dissolve
        hide morgan with dissolve
        hide lance with dissolve

        guide_dark "You are not assertive enough with them and their inquiries."
        guide_dark "If they know too much before they’re ready, the cycle --"
        guide "I don’t want to hear about the damn cycle tonight."
        guide "You had better stay out of my dreams."
        guide_dark "{i}Your{/i} dreams?"
        guide_dark "Ah... cute. Keep believing this mind is still yours."
        guide_dark "Whatever helps you to help {i}them{/i}."

        ## The screen throbs red
        show overlay_red onlayer foremost at flash_overlay
        guide_dark "{i}Thus, always{/i}."
        jump day3_dinner_end

    ## FADE OUT
    label day3_dinner_end:
        $ transition_hold_seconds = 1.5
        call end_scene_fade_to_black_pause from _call_end_scene_fade_to_black_pause_1
    ## END SCENE
    return

label day3_dream:
    ## NEW SCENE: Night 3 dream
    ## BLACK SCREEN. The sound of jets, gunfire, screaming, explosions.
    play music foley_war_sounds fadein 2.0 volume 1.0
    play music_extra foley_crowd_panic fadein 4.0 volume 0.75

    ## Sound of RUNNING
    play sound running volume 0.5
    gwen "“Lucas, keep up! We have to go!”"
    lucas "“I -- I can’t. I can’t -- breathe --”"
    guide "“Gwen, grab one arm, I’ll grab the other.”"

    ## FADE IN misty background we’ve been using, tinted red. I can make another image for this if need be.
    ## Sound of a jet flying {i}very{/i} close. A very loud explosion nearby.
    play sound jet_flyby volume 0.75
    scene backdrop_mist_red with Fade(0.5, 0.0, 0.5)
    play sound_extra explosion_nearby volume 0.8
    guide "“Shit --!”"
    guide_dark "The first time you ever swore, if I recall. Rather tame, given the circumstances."
    guide "You weren’t there for that."
    guide_dark "A USB can read pictures from a hard drive even if it wasn’t plugged in when the pictures were created, can’t it?"
    gwen "“Up ahead! I can see the military!”"
    gwen "“Keep going, Lucas!”"

    ## The sound of a car horn, a vehicle almost hitting the GUIDE and his friends.
    play sound car_horn volume 1.0
    play music foley_war_sounds fadein 0.0 volume 0.25
    guide "“What the hell?!{w=1.0} Back off!{w=0.75} Argh!{w=1.0} What is wrong with these people?!”"
    guide "“It’s like they can’t even see us!”"
    gwen "“Lucas, don’t you {i}dare{/i} pass out now.”"
    pause 1.0

    guide_dark "And so you ran, and ran. And all the other people you saw ignored three lonely children without any parents or family, thinking only of saving their own hides."
    guide_dark "And when you got to the barricade and pleaded for your lives with everyone else..."
    guide_dark "What was it they said? That this was a “quarantine zone?” That no one was allowed in or out? Not even their own friends or families?"

    ## The sound of another explosion. Angry and scared yelling crowds.
    play sound_extra explosion_nearby volume 0.75
    play music_extra foley_crowd_panic fadein 2.0 volume 0.5
    guide "“You’re just gonna let us all die?!”"

    ## The screen shakes, a sound as the GUIDE kicks a metal fence
    play sound fence_hit
    guide "“Bastards!”" with screen_shake_mid
    gwen "“Please, our friend -- he won’t make it if you leave us in here!”"
    stop music_extra fadeout 2.0

    ## The military on the other side of the fence is suddenly assaulted by Corrupted creatures. This is symbolized by monstrous sounds, followed by yelling and gunfire.
    play sound monster_roar
    play music_extra foley_crowd_panic fadein 0.0 volume 0.8
    pause 1.0
    play sound_extra gunfire
    pause 0.5
    
    guide_dark "What fools, to think they could just fence off the problem and keep their little status quo going on the outside."
    guide_dark "It worked for so long, or so they thought. Then when it came knocking at their door, they hadn’t the slightest clue how to keep their fragile facade in place."
    pause 0.5

    ## SFX Fence rattle signifying a gate opening
    play sound fence_hit
    $ mordred_name = "???"
    mordred "“Kids! This way!”"
    guide "“Who are you?”"

    # Change Mordred name to "General Mordred"
    $ mordred_name = "General Mordred"
    mordred "“General Mordred, but we can have time for nicer introductions later.”"
    mordred "“To hell with this peace and order crap. My duty is to the people of my country, and by God, I’m going to protect them.”"
    mordred "“Let’s get you out of this town.”"
    lucas "“And go where?”"
    mordred "“Away from {i}here{/i}, for starters.”"

    ## SFX Explosion
    play sound_extra explosion_nearby volume 0.75
    guide "I don’t want to see this again! I -- I have to wake up. I have to --"

    ## The screen transitions immediately to black. All the sound stops.
    stop music
    stop music_extra
    stop sound
    stop sound_extra
    $ quick_menu = False
    scene backdrop_black
    with Fade(0.0, 2.0, 0.0)
    $ quick_menu = True
    guide_dark "You have to...?"
    guide_dark "You have to... what? Pinch yourself? Hold your breath and count to ten?"
    guide_dark "Waking up won’t make the past go away. Nor will it stop reminding you of the future not yet come to pass."
    guide_dark "Remember the pain. Remember the horror."
    guide_dark "Remember how the actions of those who were charged to {i}protect{/i} you only made everything worse."
    guide_dark "Remember how they {i}failed{/i} you."
    guide_dark "Remember how they failed you, so that you might try not to make their same mistakes..."
    guide_dark "And then fail all the same."
    guide "I always knew I’d make the same mistakes."
    guide "You’ve guaranteed that."
    guide "I just want to get this over with so I don’t have to worry about it anymore."
    guide_dark "How responsible of you! Then again, what else could I expect?"
    guide_dark "Running from your problems is all you know."
    guide "That’s not true. We {i}tried{/i} to change things."
    guide "Me, Gwen, Lucas -- our first thought wasn’t to just lay down and die."
    guide "We escaped the town and left everything behind -- friends. Family. Siblings."
    guide "We made the best of what was left, tried to help others like us -- children who had lost everything -- but soon, there wasn’t anything left {i}to{/i} work with."
    guide "When we started hearing the radio reports about the few remaining scientists banding together to try to reverse the Corruption, or find someplace else to go..."
    guide "Then we decided something had to change."
    guide "Then we decided that there had to be something we could do to stop it. Save everyone."
    guide_dark "Until you found the Roots."
    guide "... Until we found the Roots."
    guide_dark "A sacred place of pilgrimage. A sacred place with a sacred message, a message whose deeper intent could be ascertained only by the Chosen."
    guide_dark "And tell me, what did that message say?"
    guide "That message is flawed. It doesn’t -- didn’t -- speak the truth of the world."
    guide_dark "{i}Didn’t{/i}?"
    guide "It was a warning. It warned us what the future might become."
    guide_dark "So it speaks truth now?"
    guide_dark "Tell me what it said."
    guide "{cps=30}...{/cps}"

    ## The screen fades in to the MISTY background, tinted dull green. There’s a “throbbing” ambiance (I can’t think of a better way to describe it -- it’s just an unnerving sound.)
    scene backdrop_mist_green
    with Fade(0.5, 0.5, 0.5)
    play music bgm_drone_throb
    play music_extra foley_lab_ambiance volume 0.5
    guide "{i}{cps=20}This place is a message... and part of a system of messages... pay attention to it!{/cps}{/i}"
    guide "{i}{cps=20}Sending this message was important to us. We considered ourselves to be a powerful culture.{/cps}{/i}"
    guide "{i}{cps=20}This place is not a place of honor... no highly esteemed deed is commemorated here... nothing valued is here.{/cps}{/i}"
    guide "{i}{cps=20}What is here was dangerous and repulsive to us. This message is a warning about danger.{/cps}{/i}"
    guide "{i}{cps=20}The danger is in a particular location... it increases towards a center... the center of danger is here... of a particular size and shape, and below us.{/cps}{/i}"
    guide "{i}{cps=20}The danger is still present, in your time, as it was in ours.{/cps}{/i}"
    guide "{i}{cps=20}The danger is to the body, and it can kill.{/cps}{/i}"
    guide "{i}{cps=20}The form of the danger is an emanation of energy.{/cps}{/i}"
    guide "{i}{cps=20}The danger is unleashed only if you substantially disturb this place physically.{/cps}{/i}"
    guide "{i}{cps=20}This place is best shunned and left uninhabited.{/cps}{/i}"
    guide_dark "This place is not a place of honor. We considered ourselves to be a powerful culture. {i}Nothing is valued here.{/i}"
    guide_dark "What a rich and timeless message!"
    guide_dark "The folly of man and its toxic legacy, forever immortalized in every life."
    guide_dark "A message so universally transferable to all things, it’s a wonder it’s not yet considered scripture."
    guide_dark "With that reminder fresh on your mind, tell me..."
    guide_dark "Now, after all this time, what does it mean to be {i}Chosen?{/i}"

    ## CHOICE
    ## > It’s an inevitability.
    ## > It’s a curse.
    ## > It’s a calling.
    ## (Choices come back together at “> RECONVENE” like in the last dream)
    menu:
        "It's an inevitability":
            jump day3_dream_choice_inevitability
        "It's a curse":
            jump day3_dream_choice_curse
        "It's a calling":
            jump day3_dream_choice_calling

    ## > It’s an inevitability.
    label day3_dream_choice_inevitability:
        guide "To be Chosen represents the inevitability of time and growth and the passing of the torch."
        guide "If it wasn’t me, or Gwen, Or Lucas, it would have been someone else. Someone else would have taken up the role."
        guide "As long as there were people who lived and breathed and were considered human, there always would have been someone Chosen."
        guide "Some things are just inescapable, barring annihilation."
        jump day3_dream_choice_reconvene

    ## > It’s a curse.
    label day3_dream_choice_curse:
        guide "One generation after the other, this life into the next, to be Chosen is a curse we have yet to break. Doing things only one certain way locks in certain outcomes."
        guide "All the imperfections we left behind in our rigidity are passed on to the next. I {i}loathe{/i} what those children will be bearing on their shoulders when the time comes."
        guide "And even if they spend their whole lives trying to patch the holes and blemishes, their own will be left behind for {i}their{/i} Chosen to deal with, ad infinitum."
        guide "Being Chosen means inevitable failure."
        jump day3_dream_choice_reconvene
    
    ## > It’s a calling
    label day3_dream_choice_calling:
        guide "To be Chosen is to receive a summons to rise above the failures that made us. It’s to know that life could be so much more."
        guide "And... it’s to give everything to that cause, while being stymied every step of the way by pre-existing systems and notions."
        guide "So you compromise a little bit to make another step forward, and you compromise a little bit more, and a little bit more..."
        guide "And at the end of it all, you look back and realize you’re hardly ten feet from where you started."
        jump day3_dream_choice_reconvene

    ## > RECONVENE
    label day3_dream_choice_reconvene:
        guide "To be Chosen is to be everything you never thought you would be."
    
    ## There’s a pause. The ambiance slowly fades out. The screen shakes.
    stop music fadeout 3.0
    stop music_extra fadeout 3.0
    stop sound fadeout 3.0
    pause 1.0
    scene backdrop_black with Dissolve(1.0)
    gavin "“... Guide..!”" with screen_shake_mid
    play music bgm_dark_ambient fadein 1.0
    guide "The boy...?"
    gavin "“Guide!”"

    ## END SCENE
    return

label day3_night_combat:
    ## NEW SCENE: Night 3 combat
    ## CABIN INTERIOR, night. GAVIN and LANCE are the two characters on screen
    ## SPRITES Gavin SP, Lance UNC
    scene cabin_interior_night with fade
    show gavin surprised at grouped_center_gavin
    show lance uncomfortable at grouped_center_lance
    with dissolve
    gavin "“Guide! Wake up! Morgan -- she’s gone!”"
    play music bgm_dark_ambient fadein 3.0
    guide "“Gone? What do you mean, ‘gone?’”"
    lance "“It’s my fault. I -- I told her she was being a stupid baby about the whole Corrupted thing --”"
    guide "“The Corrupted?!”"
    lance "“-- so I think she went out to find one and prove it’s not dangerous!”"
    guide_dark "What? No! She can’t do that! Does she have a death wish?"
    guide_dark "We need the girl! {i}They{/i} need the girl!"
    guide_dark "Without her, the cycle can’t continue!"
    guide "“Then we don’t have time to lose. Get your weapons, prepare your spells -- tell me which way she went.”"

    ## GAVIN and LANCE run off to one side of the screen.
    hide gavin with easeoutleft
    hide lance with easeoutleft

    ## FADE TRANSITION back into the Wasteland, night.
    scene wasteland_night with fade
    guide "I remember what it felt like to want to still have hope. I remember what it felt like to want to believe that everything could somehow turn around."
    guide "I remember seeing my first Corrupted, remember brandishing my blade to protect Gwen and Lucas, remember seeing what was left of the poor soul it consumed -- the twisted agony, the fear."
    guide "I don’t blame Morgan. I think anyone who was ever Chosen felt as she does, at least for a time."
    guide "But to go {i}alone{/i} to try and prove her thoughts and theories and hopes..!"
    guide "I can only pray we aren’t too late."

    ## The sound of a scream in the distance and a Roar.
    play sound scream_woman volume 0.25
    gavin "“There! Around the corner!”"
    pause 1.0

    ## Fade in GAVIN and LANCE first, then Morgan second.
    ## SPRITES Gavin SP, Lance UNC, Morgan UNC
    ## (If I have time we’ll replace this with a CG of the characters and Morgan backed into a corner by a Corrupted)
    scene wasteland_night_2 with dissolve
    show gavin surprised at grouped_left_gavin
    show lance uncomfortable at grouped_left_lance
    with dissolve
    show morgan uncomfortable at grouped_right_morgan
    with dissolve
    gavin "“Morgan!”"
    morgan "“Gavin! Lance! Help me!”"
    guide_dark "Protect the girl! We need her power!"

    ## BEGIN BATTLE with strong variant CORRUPTED
    ## (Note: this scene could be massively changed pending time with more dialogue and scene-specific art (I think you called them CGs?))
    call combat_encounter_corrupted_strong_day3_night from _call_combat_encounter_corrupted_strong_day3_night
    
    ## AFTER BATTLE, everyone catches their breath.
    ## SPRITES Gavin SP, Lance UNC, Morgan UNC
    play music bgm_meditative_hang
    scene wasteland_night with fade
    show gavin surprised at grouped_left_gavin
    show lance uncomfortable at grouped_left_lance
    show morgan uncomfortable at grouped_right_morgan
    with dissolve
    call restore_from_combat from _call_restore_from_combat_4
    guide "“Morgan? Are you injured?”"
    guide_dark "That was too close."
    morgan "“I... I’m okay.”"

    ## SPRITE Morgan SD
    show morgan sad
    morgan "“I’m so sorry. I didn’t mean for this to happen. I only thought -- I wanted to...”"
    morgan "“... I didn’t think they could be lost.”"

    ## SPRITE Lance ANG
    show lance angry
    lance "“... Gods! What’s {i}wrong{/i} with you!”"

    ## SPRITE Gavin UNC
    show gavin uncomfortable
    gavin "“Lance, don’t --”"
    lance "“No! {i}Shut up!{/i}”"
    lance "“I’m sick of you guys ignoring me because you think I’m a know-it-all jerk!”"
    lance "“I’m not saying these things just to be mean! I {i}know{/i} what I’m talking about!”"

    ## LANCE becomes teary and emotional.
    ## SPRITE Lance UNC
    show lance uncomfortable with dissolve
    lance "“Nothing left in the Corrupted knows anything about compassion or love!”"

    ## SPRITES Gavin SP, Morgan SP
    show gavin surprised
    show morgan surprised
    lance "“I saw what they did to my family! I {i}know{/i} what I’m talking about! Okay?!”"
    lance "“They {i}hated{/i} me before there wasn’t anything left of them!”"
    pause 0.75

    ## SPRITES Gavin SD, Morgan SD, Lance SD
    show gavin sad
    show lance sad
    show morgan sad
    with dissolve
    morgan "“Lance... why didn’t you tell us the truth? How long have your parents been gone?”"
    morgan "“Gavin and I can hardly even remember our families. Did you think we were going to judge you?”"
    lance "“It had only just happened when I met you guys.”"
    lance "“You two were always talking about how much {i}fun{/i} you always had making new friends in new survivor groups, and...”"

    ## SPRITE Lance A
    show lance annoyed with dissolve
    lance "“... I didn’t want to be the odd one out. I’m {i}tired{/i} of being the odd one out.”"
    lance "“I didn’t know anyone outside of my family until I knew you guys. It was just me, Mom, Dad... my little brother...”"

    ## SPRITE Lance SD
    show lance sad
    lance "“I miss them. Why did it have to be them?”"
    lance "“I’m so sick of watching them {i}change{/i} when I close my eyes at night.”"
    lance "“I just want them back. I don’t want {i}this{/i}.”"
    
    ## GAVIN and MORGAN struggle to think of what to say.
    pause 0.75
    show gavin neutral with dissolve
    gavin "“We can be your family, Lance. If you’ll let us.”"
    gavin "“You know that, right?”"
    gavin "“We can’t be your mom and dad, but that doesn’t mean we can’t be... something else.”"
    morgan "“... We’d feel less weird about you if you were more honest with us.”"
    
    ## LANCE calms down a little.
    show lance neutral
    guide_dark "How {i}touching{/i}."
    guide_dark "What a strong little boy."
    guide "I’m sick of {i}you{/i}."

    ## The screen shakes and throbs red
    show overlay_red onlayer foremost at flash_overlay
    guide_dark "{i}Get used to me. I’m not going anywhere.{/i}"
    guide_dark "{i}It’s almost my turn.{/i}"
    gavin "“Guide? You don’t look good.”"
    morgan "“I’m sure it’s my fault. I must have worried you all so much.”"
    guide "“No, I’m just... we’re glad you’re okay.”"
    guide_dark "“You are needed. You are more important than you know.”"

    ## SPRITES Morgan N, Lance N
    show lance neutral
    show morgan neutral
    morgan "“That’s... kind of you, Guide... but you still seem very unwell.”"
    morgan "“We should go home, shouldn’t we?”"
    lance "“... Home. Something like that.”"
    guide_dark "“We will discuss new rules when we return to the cabin, to ensure your safety.”"
    pause 0.5
    guide "Get out of my throat! This isn’t your place to dictate!" with screen_shake_mid
    guide_dark "If you think you’ve been in control before the Chosen arrived, you have been {i}so{/i} sorely mistaken."
    guide_dark "“All three of you play a role too important to risk by such rash decisions. You have to reach your full potential before you can rush headfirst towards your destiny.”"

    ## SPRITE Gavin A
    show gavin annoyed
    gavin "“Our destiny...?”"
    gavin "“... You haven’t wanted to talk much about it before...”"
    guide_dark "“The time draws near where you will be ready to face the Hidden Darkness. To lose before you have the chance to accomplish what you were meant to would be disastrous for all life.”"

    ## SPRITE Gavin N
    show gavin neutral
    morgan "“I guess he’s right.”"
    morgan "“I’m sorry, again, for the trouble.”"
    guide_dark "“You have learned. You will grow.”"
    guide_dark "“You will become stronger from this.”"
    guide_dark "“Now, go. I will watch our backs.”"

    ## One by one, the HEROES fade from the screen.
    hide morgan with dissolve
    hide lance with dissolve
    hide gavin with dissolve

    ## There’s a GASP sound effect as the GUIDE regains control of himself.
    play sound gasp_man volume 0.33
    guide "Gods! I couldn’t breathe!" with screen_shake_mid
    guide_dark "I suppose it’s been a while since I’ve had to consider such trivial functions."
    guide_dark "Now. {i}Walk{/i}."

    ## FADE OUT
    $ transition_hold_seconds = 2.0
    call end_scene_fade_to_black_pause from _call_end_scene_fade_to_black_pause_2
    
    ## END SCENE
    return