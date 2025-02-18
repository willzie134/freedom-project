label prologue:
    
    $ current_scene = "Prologue, Scene 1"
    $ debug_save("1-1", "Prologue, Scene 1")
    call scene_1_1

    $ current_scene = "Prologue, Scene 2"
    $ debug_save("1-2", "Prologue, Scene 2")
    call scene_1_2

    $ current_scene = "Prologue, Scene 3"
    $ debug_save("1-3", "Prologue, Scene 3")
    call scene_1_3

    $ current_scene = "Prologue, Scene 4"
    $ debug_save("1-4", "Prologue, Scene 4")
    call scene_1_4

    $ current_scene = "Prologue, Scene 5"
    $ debug_save("1-5", "Prologue, Scene 5")
    call scene_1_5

    $ current_scene = "Prologue, Scene 6"
    $ debug_save("1-6", "Prologue, Scene 6")
    call scene_1_6

    $ current_scene = "Prologue, Scene 7"
    $ debug_save("2-1", "Prologue, Scene 7")
    call scene_1_7

    $ current_scene = "Prologue, Scene 8"
    $ debug_save("2-2", "Prologue, Scene 8")
    call scene_1_8

    $ current_scene = "Prologue, Scene 9"
    $ debug_save("2-3", "Prologue, Scene 9")
    call scene_1_9
    return

label scene_1_1:

    scene black
    with meddis

    pause 5.0

    sp_n "It's always the same. The smoke, the screams..."
    
    play ambiance ambient_battlefield fadein 1.0 volume 0.5
    scene battlefield dark:
        sepia
        slidezoom(duration=8.0, start_x=0.0, end_x=1.0, start_y=.5, end_y=.5, zoom_val=1.5)
    with meddis

    pause 8.0

    stop ambiance fadeout 1.0
    scene black
    with meddis
    sp_n "The faces I can't forget..."

    scene forest fire at sepia
    with meddis
    play ambiance ambient_battlefield fadein 1.0 volume 0.5
    
    npc "Help!"

    npc "We're all gonna die, we're all gonna die, we're all gonn—"

    stop ambiance fadeout 1.0
    scene black
    play sound explosion fadeout 1.0 volume 0.75

    pause 1.0
    sp_n "I tried to save them... But I.."

    play sound [ heartbeat, "<silence 2.0>" ] volume 0.25 loop

    scene battlefield dark:
        zoom 1.25
        align(0.5, 0.5)
        sepia
    with slowdis
    play ambiance ambient_battlefield fadein 1.0 volume 0.5

    $ npc_name = "Commander?"
    npc "Come on, Corporal. Move!"

    scene black
    with fastdis
    sp_n "I... can't move"

    scene battlefield dark:
        zoom 1.25
        align(0.5, 0.5)
        sepia
    with fastdis

    play sound [ heartbeat, "<silence 1.25>" ] volume 0.25 loop

    npc "Damnit, get a hold of yourself!"

    scene black
    with fastdis
    sp_n "My body... It won't respond..."

    
    play sound [ heartbeat, "<silence 0.75>" ] volume 0.5 loop

    sp_n "Why can't I..."
    sp_n "Ah..." 

    $ renpy.pause(5.0, hard=True) 

    stop ambiance fadeout 1.0
    play sound incoming_mortar fadein .5

    scene sky birb at sepia
    with Dissolve(1.5)

    scene black
    play sound tinnitus fadein 5.0
    pause 5.0

    return

label scene_1_2:

    
    stop sound
    play ambiance heartbeat_long volume .8
    scene port day:
        xalign .5
        yalign .5
        anchor (0.5, 0.5)
        zoom 1.1

    sp_mn "..."
    sp_mn "Where... am I?"

    sp_adh "The stench of salt and sweat clung to the air."
    sp_adh "Waves slapped against the hulls of docked ships, with their engines idling after hours at sea."

    stop ambiance fadeout 5.0
    queue ambiance crowd fadein 5.0

    sp_mn "This is..." 

    sp_adh "The port was overrun, refugees poured onto the docks."
    sp_adh "Their voice were blending into one another."
    sp_adh "No one could tell what they were saying."

    show port day:
        ease 1.0 zoom 1.0

    sp_mn "..."
    
    show port day:
        ease 1.0 blur 5.0

    sp_mn "... The port... but..."
    sp_mn "... but it's far from {i}there{/i}."
    sp_mn "So why does it still feel like I'm still there...?"
    sp_mn "… No. Something's wrong with me."

    show port day:
        ease 1.0 blur 0.0
    camera at look_left(duration=3.0)

    play sound mic_feedback

    sp_adh "A loudspeaker crackled above the crowd."
    
    sp_mic "All newly arrived personnel, proceed to the east checkpoint for processing"
    sp_mic "Injured civilians, report to the medical tent near Dock 3."
    sp_mic "Remain calm and follow the instructions of military personnel."

    sp_mn "... Checkpoint."
    sp_mn "Injured civilians..."
    sp_mn "Military..."


    camera at look_right()

    sp_adh "The walkways were packed with makeshift tents, scattered without order."
    sp_adh "Not from neglect, but from the sheer numbers of people there."
    
    $ npc_name = "Refugee Woman"
    $ npc_name2 = "Young TNI Soldier"
    npc "Please! My husband was supposed to be on the other boat, have you seen him!?"
    npc2 "Please remain calm, ma'am, we're doing the best we can out here."
    npc "But please! My husband, he—"

    $ npc_name2 = "Senior TNI Soldier"
    npc_name2 "Please move along, ma'am. We will handle it."

    camera at reset_camera()

    sp_adh "It was too much for any sane person to handle."
    sp_adh "Even so, it paled in comparison to the intensity of the battlefield."
    sp_adh "Yet, it was enough to relive the horror of that place again."
    sp_adh "... I was no exception."
    

    sp_mn "..."
    sp_mn "So chaotic..."
    sp_mn "..."
    sp_mn "So loud..."

    play sound tinnitus fadein 6.0
    queue sound tinnitus_loop loop

    show port day:
        ease 5.0 blur 5.0

    stop ambiance fadeout 10.0

    sp_mn "People's scream..."
    sp_mn "Despair..."
    sp_mn "..."


    scene forest fire at sepia
    with slowfade

    pause 0.2

    scene port day: 
        blur 5.0
    with vpunch

    stop sound
    play ambiance crowd fadein 1.0 volume .1

    sp_mn "... Wait, No... Calm down..."
    sp_mn "I'm not there..."
    sp_mn "Just... Relax... Me"
    sp_mn "..."

    scene black
    with slowdis

    sp_mn "Breathe in..."
    sp_mn "... Breathe out..."
    sp_mn "Breathe in..."
    sp_mn "... Breathe out..."
    sp_mn "..."
    sp_mn "There..."

    scene port day
    with meddis

    sp_mn "..."
    sp_mn "I've calmed down..."

    stop ambiance fadeout 2.0

    npc "Hey."

    play sound shoulder_pat volume 2.0

    sp_mn "—!" with vpunch
    
    $ sty.name = "???"
    show setya curious
    with fastfade

    stop ambiance fadeout 5.0
    play music music.neutral fadein 2.5

    pause 1.0

    sp_mn "... A soldier."
    sp_mn "He is..."

    sty "Oh! I knew it was you, Andhra!"

    show setya relieved
    sty "Glad to see you made it!"

    $ sty.name = "Setya"
    sp_mn "Setya..."
    

    sp_mn "Was he a part of the South Kalimantan force..?"
    sp_mn "He made it..."
    sp_mn "Thank God he did..."

    adh "... I'm glad you did too, Setya."

    show setya smile neutral
    sty "Of course. I promised to my Pa I'd go back after all."
    
    show setya curious
    sty "Oh, how about your family, Andhra?"
    sty "They lived in Kalimantan too, weren't they?"

    show setya concerned
    sty "Did they..."

    adh "They made it safe, don't worry."
    adh "I had a relative back in Surabaya, so they're staying there."

    show setya relieved
    sty "I see. That's a relief."

    show setya curious
    sty "How about yourself? Are you alright?"

    show setya determined
    sty "You looked really pale when I called you."
    
    adh "Me? I'm alright."
    sp_mn "..."
    sp_mn "Yes, I'm alright..."
    sp_mn "It was just a nightmare."

    show setya determined
    sty "Are you su—"

    play sound mic_feedback volume .25
    show setya curious

    pause 3.0
    
    stop sound

    sp_adh "The sound of the loudspeaker intrupted us."
    sp_adh "Unlike the other loudspeakers, it was directed to us."

    sp_mic "{b}{i}All military personnel, report to the checkpoint six for debriefing.{/i}{/b}"
    sp_mic "{b}{i}I repeat, all incoming personnel, to the checkpoint six for debriefing.{/i}{/b}"

    show setya smile neutral
    sty "Well, guess they're not letting us rest just yet. Come on."

    show setya at moveoutleft

    sp_mn "..."
    hide setya
    sp_mn "...Oh, I gotta catch up."

    show camp day
    with slowfade

    stop music
    play ambiance crowd fadein 4.0
    play sound footsteps_concrete loop

    sp_mn "..."

    camera at look_right()

    $ npc_name = "TNI Officer"

    npc "Get those civilians under control!"
    npc "The last thing we want is for them wandering around!"

    camera at look_left()

    $ npc_name2 = "Refugee Man"
    npc "I'm sorry, but could you spare me a water bottle..?"
    npc "Just a little for my son."


    npc2 "I.. I'll see what I can do."

    camera at reset_camera()

    sp_mn "..."
    sp_mn "It's no different here too..."
    sp_mn "So chaotic..."
    sp_mn "..."

    sp_adh "We proceeded further into the camp."
    sp_adh "The conditions were similar to those in the port."
    sp_adh "There were crowds everywhere, perhaps even more than in the port."
    sp_adh "And a few more soldiers and volunteers were there as well."


    sty "Damn, look at this mess."

    show setya determined
    with meddis

    adh "What did you expect..."
    adh "It was similar in Surabaya too."
    adh "...A mess is an understatement. Chaotic is what it is."

    show setya curious
    with meddis
    sty "Well, as chaotic as it is, it's safer than the frontline out there."
    
    show setya concerned
    with meddis
    sty "Who knows what happened to those who left behind..."

    hide setya
    with fastdis 

    sp_mn "..."

    sp_mn "Those who were left behind..."
    sp_mn "..."
    sp_mn "Who {i}we{/i} left behind..."

    stop ambiance fadeout 2.0
    stop sound fadeout 2.0
    stop music fadeout 2.0
    queue ambiance crowd_angry fadein 2.0 volume .75
    show camp day at panoramic
    with medfade

    $ npc_name = "Angry Civilian"
    $ npc_name2 = "Young Man"

    npc "You just left us there! We trusted you!"
    npc2 "What the hell were you even fighting for, huh?!"
    npc2 "You all ran like cowards."

    sp_mn "The refugees..."
    sp_mn "... They're... Protesting..?"

    sp_adh "A large group of refugees gathered in front of a guarding post, looking upset."
    sp_adh "The atmosphere was chaotic. Officers seemed hesitant to engage, they couldn't done nothing."
    sp_adh "So they just waited, waited until someone else were able to took control of the situation."
    sp_adh "And it was..."

    sp_mn "So loud..."

    stop ambiance fadeout 10.0
    play sound tinnitus fadein 8.0
    queue sound tinnitus_loop loop

    sp_mn "... Too loud..."

    scene black
    with meddis

    pause .5

    sp_mn "It wasn't our-"
    
    sty "Keep yourself together, Andhra."

    adh "Set-"

    play ambiance crowd_angry volume .25 fadein 5.0
    stop sound
    show camp day
    show setya determined at center, close
    with vpunch

    sty "Keep your head low and keep moving."

    play sound footsteps_concrete loop

    sty "I had a feeling this will happen sooner or later."
    sty "I just didn't expect it to be this soon."
    
    show setya smile neutral
    sty "Don't worry, someone will handle this."

    sp_mn "..."
    sp_mn "Someone..?"
    sp_mn "... That doesn't seem right..."
    sp_mn "..."
    sp_mn "No..."
    sp_mn "... That's right.."
    sp_mn "Just keep moving, and everything will be alright..."
    sp_mn "... This is not that place..."
    sp_mn "..."
    
    stop ambiance fadeout 2.0
    stop sound fadeout 1.0

    scene camp day
    show setya smile neutral
    with medfade

    play music music.grim

    sty "... Good, we lost them."

    show setya determined
    sty "Those people... Do they think we wanted this!"
    sty "That we enjoyed leaving them behind!?" with vpunch

    adh "..."
    adh "It doesn't matter what they think..."
    adh "What matter is what we do."

    show setya concerned at shaking
    sty "No, their opinions do matter."
    sty "Without their support, this country will been doomed."
    sty "..."

    show setya determined
    sty "They should've know that we we're just as messed up as they are."
    sty "They just don't see it."

    
    play sound mic_feedback volume .25

    pause 3.0
    
    stop sound
    
    sp_mic "all military personnel, regroup at the checkpoint six for debriefing."

    adh "..."
    adh "Setya, complaining won't solve anything."

    show setya concerned
    sty "..."

    show setya smile neutral at nodding
    sty "I guess you're right."

    show setya relieved
    sty "There are worse problems at hand."

    show setya happy
    sty "Let's hear how screwed we really are."
    
    adh "..."
    adh "Not funny."

    return
    
label scene_1_3:

    stop music fadeout 2.0
    scene black
    with meddis


    sp_adh "We walked into the makeshift command tent. Only to be met with a suffocating atmosphere."  

    scene camp inside day
    with meddis

    play music music.grim

    sp_adh "The air was thick with exhaustion from the soldiers inside."  
    sp_adh "Some sat on crates, others on the ground, their backs resting against the tent walls."  
    sp_adh "A few remained standing, arms crossed, eyes heavy with fatigue."  

    sp_adh "Despite it all, discipline still held. Even in the dim light, the soldiers carried themselves like professionals."  
    sp_adh "The table in the middle had crumpled maps, radios, and a laptop with a live feed of the situation outside on it, flickering."

    sp_adh "A man stepped forward—our acting commander."  
    sp_adh "His uniform was stained with dirt, his face drawn with exhaustion."  

    $ npc_name = "Commander"
    npc "We'll waste no time, let us begin our briefing."
    npc "If anyone from your unit is missing, make sure they're informed later."  

    show camp inside day at bg_close
    with meddis

    npc "I'm not going to sugar coat this, we've lost most of South Kalimantan."
    npc "If anyone had any friends over there, whether it's the South or the West... Assume the worst."

    sp_mn "..."

    scene camp inside day
    with meddis

    sp_adh "A heavy silence settled over the room. No one spoke. No one moved."  
    sp_adh "Some lowered their heads. Others stared at the ground, fists clenched."  
    sp_adh "The silence lingered—a brief moment for the fallen."  

    show camp inside day at bg_close
    with meddis

    npc "In a few days, they'll take the East, the last standing city, Pontianak."
    npc "And I don't think they will stop from there."
    npc "They could be going to Sumatra, or Sulawesi... Or even straight to here, to Java."
    npc "They've got full dominance on land, air, and sea. But the good news is that they don't have access to the Makassar Strait, thanks to the Philippines and the US for protecting it."
    npc "Should we get the chance, we can reclaim Kalimantan through Sulawesi."
    npc "But, we don't know anything yet. The best we can do is to prepare for the worst."
    npc "Pontianak, being the last city to be attacked, would split the remaining forces into two parts. Sumatra and Java."
    npc "They'll strengthen the defense on Sumatra, while also escorting a small amount of the refugees."
    npc "As for their refugees, most will be coming here, to the Java island."
    npc "So, the command will be reorganizing all forces. Some of you will be reassigned to Surabaya or Jakarta."
    npc "You who came from Surabaya, I welcomed you here, but you're all going to Jakarta."

    play ambiance crowd volume .25 fadein 5.0

    sp_adh "The atmosphere changed. Some soldiers quietly discussed on their reassignment. They reacted in different ways, some seemed upset, some frustrated, and some just accepted it."
    
    camera at camera_look_left
    with None

    show setya determined at center, close
    with meddis

    sty "..."
    
    sp_mn "... Setya."
    sp_mn "He doesn't seem... Surprised..."
    sp_mn "It's as if he knew it already..."
    sp_mn "No... It's pretty easy to guess."
    sp_mn "But it didn't seem the news itself surprise him."
    sp_mn "He's clearly bothered by the assignment."

    adh "Hey... What do you have in mind."

    show setya curious
    sty "Hmm?"

    show setya smile neutral
    sty "Oh..."

    show setya happy
    sty "Nothing."

    show setya determined
    sty "I just think they're taking the decision a bit too hastily."
    sty "We were just back from the frontline. I expected us to get some rest before reassignment."
    sty "I have no problem myself for the decision, but it's clear that the soldiers do have it."
    sty "It just shows how desperate we are."

    adh "Setya..."

    sp_mn "That's so unlike him..."
    sp_mn "He's usually never question any order... Maybe the battlefield changed him..."
    sp_mn "The same way it did to me..."

    npc "..."

    sp_adh "The Commander waited for the crowd to finish, which took a while."

    scene camp inside day:
        zoom 1.2
        xalign 0.5
        yalign 0.5
        blur 2.0
    with medfade
    camera:
        ease 1.0 xoffset -100
    stop ambiance fadeout 3.0

    npc "... For those of you who think we're out of options—we're not alone in this fight."
    npc "Many of you may already know KPR. I've heard they had a branch back in Kalimantan. Some of you may have worked with them, or only heard rumors from them."
    npc "They're taking personnel willing to fight under their command, and theirs are much different than ours."

    play ambiance crowd fadein 1.0
    sp_adh "The murmur spread again, some voicing their uncertainty and skepticism."

    $ npc_name2 = "Skeptical Soldier"
    npc2 "So what, we just ditch the TNI and join them?"

    $ npc_name2 = "Judmental Soldier"
    npc2 "We don't even know who they are, they're mostly just civilians. They'd take in anyone, even people without any formal training."

    $ npc_name2 = "Frustrated Soldier"
    npc2 "We've been fighting and dying as an actual army, and now we're supposed to take orders from a bunch of... what? A paramilitary group?"

    $ npc_name2 = "Practical Soldier"
    npc2 "They wouldn't be mentioned here if they weren't useful. Maybe they have something we don't—equipment, tactics, intelligence?"

    $ npc_name2 = "Realist Soldier"
    npc2 "We just lost an entire island to the enemy, and we're debating whether we should accept extra help? Maybe we don't have the luxury to be picky anymore."

    stop ambiance fadeout 1.0
    npc "I understand your concerns. Some of you have fought for months, lost comrades, and now you're being asked to consider something unfamiliar."
    npc "But let me make one thing clear, they're not just some ragtag militia of willing volunteers, they're the real deal."
    npc "And no, you will not be considered abandoning your duty, you can treat it as a redeployment."
    npc "If you wish to join them, we will not hold you back. Your service will still be recognized by the TNI."
    npc "If you don't, then you'll be following our command as planned."
    npc "No one is forcing you to make this choice now."
    npc "You have until we reach Bekasi, that's where KPR's convoy will pick you up along with some refugees."
    npc "The choice is yours, but remember this—no matter where you serve, it is for our cause, the Nation's. We will need every capable fighters to ensure our victory."
    npc "Regroup at the extraction point 15 minutes after you've got your reassignment detail."
    npc "You are all dismissed."

    show camp inside day:
        ease 2.0 blur 0.0 xoffset 100

    play ambiance crowd fadein 2.0

    sp_adh "The Commander left, leaving the soldier into their own discussions."
    sp_adh "Many were genuinely interested, tired with the military's command chain. While the others remained skeptical."

    $ npc_name2 = "Interested Soldier"
    npc2 "Might as well. There must be a reason why they even mentioned it to us. They might have something we don't."
    npc2 "They're not military, dumbass. There's no way some civilian have something better than us. All they can do is complain anyway."
    npc2 "Not trying to fully agree with you, but TNI still need us here, we're not playing the resistance army if we have them."

    sp_mn "..."
    adh "What do you think.. Setya?"

    stop ambiance fadeout 2.0
        
    camera:
        ease 1.0 xoffset 5
    with None
    
    show setya determined at center, close
    with meddis

    sty "Hmm..."

    play ambiance crowd fadein 2.0 volume .1

    show setya determined
    sty "Tough to say. I never expected the military to be so interested at some militia."
    sty "They're not just any street militia, that's for sure. Otherwise, we wouldn't have received the recommendation in the first place."
    sty "But, there's something about it that just doesn't sit right with me."

    adh "... You don't trust them?"
    adh "I feel like we're the ones who should worry about trust."

    "There wouldn't be any angry mob right outside this tent after all."

    show setya smile neutral
    sty "Well, no, of course not. We're fighting for the same clause, and I doubt they're aiming to overthrow the government in this state."

    show setya determined
    sty "The problem is control."
    sty "As a soldier, we follow a chain of command. We know where we stand and who we follow, no question asked."

    show setya concerned
    sty "But KPR?"
    sty "They're different. Too open. Too loose. They take just about anyone."

    adh "And that's a bad thing?"

    show setya determined
    sty "Loss of control is a bad thing. Their fate would be in the hands of their leader."

    show setya smile neutral
    sty "If they can manage to control a bunch of barely disciplined people, they'll get the best out of them."

    show setya determined
    sty "However, if they can't, then they won't hold very long, it'd be a disaster even, not just for them, but for the people who depend on them."
    sty "We've fought side by side with trained men and still lost. How would we joining them make a difference?"

    adh "..."
    sp_mn "Setya is right..."
    sp_mn  "... We're a bunch of trained men, yet we lost the battle..."
    sp_mn "How would they make a difference..."
    sp_mn "But... "

    show setya happy
    sty "... But, there's nothing wrong in joining them either."

    adh "Eh... Huh?"
   
    stop music fadeout 2.0
    stop ambiance fadeout 2.0
    play music music.neutral fadein 2.0

    show setya smile neutral
    sty "I'm not sure I can go with you if you decide to go with KPR over TNI. I've still got a lot more important things to do here."

    adh "So you... Uh... Don't really mind if I chose either side?"

    show setya happy
    sty "Yeah, whoever you want to fight with, I'm fine with it. Our friendship wouldn't really be affected by something like that, would it?"

    show setya determined
    sty "Just don't forget who you're really fighting for."

    adh "......"
    adh "..."
    adh "Of course, I won't. That's why I'm still here."

    show setya relieved
    sty "That's the Andhra I knew."
   
    show setya determined
    sty "Just promise me one thing—don't get yourself killed out of nowhere."

    show setya concerned
    sty "I've lost enough friends already, I don't want to lose another."

    adh "..."
    adh "Of course. You too. Don't you die on me."

    show setya relieved
    sty "I'll try to manage."

    show setya smile neutral
    sty "Anyway, let's get going then, we still have some journey left to do."

    adh "Yeah."

    camera:
        ease 0.2 xoffset 0

    scene black at center
    with meddis

    stop ambiance fadeout 2.0
    stop music fadeout 2.0

    return

label scene_1_4:
    

    sp_adh "..."
    sp_adh "It took several hours of travel before we reached the checkpoint that might separate our paths. I did some thinking during that time."
    sp_adh "Setya wasn't in the same truck as me, so I didn't have much of a second opinion. All I knew was that the soldiers there weren't so eager to join the KPR."
    sp_adh "I haven't come up with anything yet."

    sp_adh "......"
    sp_adh "..."
    sp_adh "Dropping off at the checkpoint, we did a quick report."
    sp_adh "No information was added except to remind us of our choice between KPR and TNI."
    sp_adh "Of course, I hadn't made up my mind at that point, so I decided to go out for some fresh air."

    scene camp day
    show setya happy
    with meddis

    play music music.neutral fadein 0.5

    sty "Oh! There you are, Andhra!"
    sty "How are you holdin' up?"

    adh "I'm fine."
    adh "I just get enough rest on the way here."
    adh "My back was killing me."

    show setya relieved
    sty "Oh. If you can say that, then I guess you're good."

    show setya curious
    sty "Say do you want to visit KPR's court for a bit?"

    show setya happy
    sty "They're right on the corner there, lots of people are lining up there."

    adh "Huh..? KPR? People lining up? I thought they were only here to pick us up?"
    adh "Why would there be so many people?"

    show setya curious
    sty "I dunno. Some of them are refugees from our convoy, so they could be enlisting there."

    show setya relieved
    sty "I'd rather them enlisting to the TNI though, since we're more equipped."

    show setya determined
    sty "But you know how much they trust us.{nw=0.5}"

    show setya concerned
    with None
    extend " Not so much."

    adh "Enlisting huh..."
    sp_mn "That's pretty odd... There are certainly some elderly and children going there..."
    sp_mn "They couldn't be recruiting them too, could they..?"
    sp_mn "Surely they can't mean it when they say they'll take just about anyone..."

    show setya curious
    sty "Oi, Andhra. you listening?"

    adh "Ah! What? Sorry, I was spacing out." with vpunch

    sty "Oh, okay. That's cool. Just try not do too much, or people might think you're insane or something."

    adh "Ugh, sorry."

    show setya smile neutral
    sty "As I was saying, let's try visiting their tents."
    sty "That'd give us a good sense of how they work.{w=0.5} It seems they're pretty open about it."

    show setya happy
    sty "So, what do you say?"

    adh "Uh... I thought you were against KPR..?"

    show setya curious
    sty "Huh? Me?{w=0.5} Well, I did, but{nw}"

    show setya smile neutral
    with None
    extend " come on, give them a shot to prove themselves."
    
    show setya happy
    sty "They do make you a little curious, right?{w=0.5} There's nothing wrong with checking them out, it's not like they're our enemies"

    adh "Huh..? {w=.5}What gave you that idea?"

    show setya curious
    sty "Are you not?"

    adh "Okay, fair."
    adh "But just so you know, you're being pretty weird."

    show setya happy
    sty "Oh, am I now?{nw=.4}"

    show setya smile neutral
    with None
    extend " You're imagining it."
    
    play ambiance footsteps_concrete fadein .2
    scene black
    with medfade

    pause 1.5

    stop ambiance fadeout 1.0
    sp_adh "We walked into the KPR Area."
    sp_adh "The place wasn't all that different from the place in Semarang or Surabaya."
    sp_adh "Tents all over the place, some were quite messy."
    sp_adh "Yet, the atmosphere was totally different."
    sp_adh "......"
    sp_adh "..."

    scene camp day
    show setya happy at center, close
    with medfade

    sty "Here we are, KPR Wonder in Bekasi."

    show setya smile neutral
    sty "I heard they set this up a while."

    show setya determined
    sty "A month before we pulled out.{w=.5} It was like they knew we were going to lose..."

    adh "Woah, really?{w=.5} That's... uh, quite the prediction..."

    sp_mn  "A month before?"
    sp_mn "They're either a pessimist or a supernatural vision..."
    sp_mn "Well, probably the former, since we were fighting a superpower nation..."

    show setya curious
    sty "Well, they had a branch over at the Kalimantan too.{nw=.2}"

    show setya smile neutral
    with None
    extend " I'm guessing that's how they were able to anticipate this many refugees."

    show setya relieved
    sty "Really makes you think how much they prioritize the civilians, even with near zero chance of winning."

    adh "I'm not sure if you should say that here, Setya."

    sp_mn "We're literally in their base..."
    sp_mn "Well, not exactly base, you know what I meant."

    show setya curious
    sty "Oops, yeah. Shouldn't have said that."

    sp_mn "But that's really the truth."
    sp_mn "Even back in Kalimantan, there were a lot of KPR members."
    sp_mn  "I don't think they cared as much about winning as they did about everyone's safety."
    sp_mn "It could be because they had us to defend them."
    sp_mn "We all know what happened when they trust us."

    show setya smile neutral
    sty "Let's start walking then. We'll find out lots of things about them inside.{w=.2} They should be okay with us barging in."

    show setya happy
    sty "Just make sure we don't bother them."

    adh "Yeah, let's go."

    hide setya
    with meddis

    play ambiance footsteps_concrete fadein 2.0
    stop music fadeout 2.0

    camera at camera_zoom

    sp_adh "As we go deeper into the area, we're starting to see more crowds there."

    play ambiance crowd fadein 2.0 volume .5
    play music music.kpr_base fadein 2.0

    sp_mn "This is..."

    sty "Hmm... Well, this wasn't a sight I was expecting to see."

    adh "That's an understatement..."


    sp_adh "There weren't as many refugees as in Surabaya and Semarang, but the atmosphere was totally different."
    sp_adh "It wasn't as grim, and everyone was treated fairly. Even though it wasn't as orderly, they managed to control the crowd."
    sp_adh "There were people in standard uniforms with KPR insignia on their chest. Some had armbands with their insignia, and the rest were in civilian clothes."
    sp_adh "No one could tell if they were parts of KPR, yet no one was batting an eye."

    camera at camera_look_left

    $ npc_name = "Charismatic KPR Member" 
    npc_name "Hey, everyone! If you need something, please speak up to one of the staff. We're here for you."
    npc_name "We still have plenty of rations, so don't hesitate to ask for a second."
    npc_name "If you feel sick or have any injuries, please go to the medical tent."
    npc_name "Our medics are trained professionals, so don't worry."
    npc_name "We've got until three hours before we leave. Please make sure you're prepared until then." 

    camera at camera_look_right


    $ npc_name = "Motherly Refugee"
    npc "Miss... I lost my daughter. Have you seen her around..?"
    npc "I was taking some rations for us to eat, but I lost sight of her... Please."

    $ npc_name2 = "Junior KPR Member"
    npc2 "Please come with me, Ma'am. We'll look for your daughter."
    npc2 "In the meantime, please take a rest in the shade. You already look tired."
    npc2 "Oh! Do you need some medical assistance? I can call someone for you."

    npc "O-oh, thank you very much... And yes please, if it's not too much trouble..."
    npc "I've been feeling unwell during the trip to here."

    npc2 "Sure, Ma'am. Please follow me this way—"

    sp_adh "They're all about helping people, no matter how old or young, experienced or not. There's no difference. They just want to help."
    sp_adh "The refugees were great, working together and not complaining. They're the perfect group to take care of the refugees."
    
    adh "This is totally different from both Surabaya and Semarang...{w=.2} you can tell, right?{w=.2} Setya?"

    sty "... Yeah. I guess they're doing a great job even more than the government."
    
    camera at reset_camera
    with None
    show setya smile neutral at left, close
    with meddis

    sty "This is what happens when people come together."

    show setya determined
    sty "If we as a government fail to meet their expectations, they'll band together to make sure everyone is treated fairly."

    show setya concerned
    sty "There are a lot on our to-do list to get regain people's trust, and it's not going to be easy."

    adh "Yeah..."

    sp_mn "They put people first..."
    sp_mn "Could they really have gained the public's trust more than the government?"

    adh "What do you think of it, Setya?"
    adh "They've also got an army, just like us, I think,{w=.5} if I'm right, that is."

    show setya curious
    sty "That sounds about right.{w=.5} They're not exactly goint to try to recruit a TNI soldier to help them with the refugees."

    show setya smile neutral
    sty "Especially since how they can managed it on their own."

    show setya determined
    sty "They might be trying to build their team since we lost in Kalimantan.{w=.5} Or maybe they've already built their army before we even know about them."

    show setya relieved
    sty "Whichever it is, they convinced the higher-ups to let the TNI soldiers join, and that's telling something."

    adh "I see."

    sp_mn "So that's how it is, huh..."
    sp_mn "An armed organization backed by the TNI soldiers."
    sp_mn "And with overflowing public support."
    sp_mn "They're really good at keeping up the morale of the people, maybe even better than the military."
    sp_mn "I wonder if their firepower can make up for the amount of manpower they have."


    stop ambiance fadeout .2

    scene black
    with meddis

    sp_adh "We found a spot to rest in the corner of the area. There wasn't much KPR activity around."

    scene alley
    show setya determined
    with meddis

    play music music.neutral fadein .2
    sty "Well, this place seems alright."

    show setya smile neutral
    sty "Let's eat our food here."

    adh "Alright..."

    camera at camera_zoom
    pause 1.0

    show setya determined at sighing
    sty "Sigh..."

    show setya smile neutral
    sty "That was a total surprise. There are lots of things we need to take note of."

    show setya relieved
    sty "If this is the way they are treating the refugees, then I wonder if any of our sites are the same way."

    show setya concerned
    sty "Maybe not, considering how hard it is to trust the government since we failed so badly."

    sp_adh "Setya started jotting down his thoughts in his little notebook."
    sp_adh "He liked to get his ideas down as soon as he had them."

    show setya smile neutral
    sty "You thought so too, right, Andhra? {w=.2}"

    adh "Yeah, they're totally different from us."
    adh "No tension, no competition. Just coordination from both sides."
    adh "Hmm..."
    
    show setya curious
    sty "Having a second thought, Andhra?"

    adh "Well, uhh..."
    adh "The KPR certainly got some perks over TNI..."

    show setya smile neutral
    adh "But... we don't know if it'll last in the long run."
    adh "As much as friendliness is needed to gain public's trust, discipline is also needed."
    adh "You can't really trust someone to do their job properly if they're not properly disciplined."
    adh "I don't want to assume too much though. We don't know much about their internal system..."

    show setya curious
    sty "Woah... I didn't realize you were thinking about it so much, Andhra."

    show setya relieved
    sty "You really take them seriously, huh?"

    adh "W-What are you talking about?"
    adh "It was just my observation. No need to act so surprised."

    show setya happy
    sty "Haha, sorry, sorry. I just didn't expect you to such a chatterbox."

    show setya relieved
    sty "In fact, I'm glad that you're still as sharp as ever."

    sp_mn "Huh..."
    sp_mn "Sharp..."
    sp_mn "I'm starting to be a little more...{w=.1} me...{w=.2} I guess..."
    
    show setya smile neutral
    sty "Anyway, I think I can agree with you."
    sty "KPR is great, but we can't be too sure that they're going to last in the long run."

    show setya determined
    sty "If they can hold on as long as we can, that'll be good enough in this situation."

    show setya smile neutral
    sty "I still think the TNI would be a better choice for us because the government directly supports us."
    sty "The public may not like us already, but we're more likely to be the ones to turn the tables."
    
    adh "Well, isn't that a little too optimistic?"
    adh "I'm not saying we're going to lose, but the chances of winning aren't that great."

    show setya happy
    sty "At least, we would die with honor."

    adh "..."
    adh "That's pretty metal, coming from you."

    show setya relieved
    sty "You know it."

    sp_mn "Still... Die with honor, huh..."
    sp_mn "I don't think we can die with honor after leaving that place..."

    sp_adh "Just after we finished our conversation, we received a radio call in from the base."

    $ sp_mic.name = "Radio"
    sp_mic "Attention all units, report back to the station for preparation."
    sp_mic "All units are required to report their decision to remain in order or join the militia organization."
    sp_mic "I repeat, attention—"

    show setya smile neutral
    sty "I guess that's our call then."

    show setya happy
    sty "I'm going to stick with the TNI this time."
    
    show setya relieved
    sty "I just don't see myself fitting into another organization, especially not a militia."

    adh "..."
    
    stop music fadeout 1.0
    play ambiance footsteps_concrete fadein .2
    scene black
    with medfade

    camera

    pause 1.5
    
    stop ambiance fadeout 1.0

    sp_adh "We walked in silence through the KPR area."
    sp_adh "They've already got part of the refugees ready to move to Bogor, the KPR base."
    sp_adh "While another part is going to Jakarta, with the government."
    sp_adh "Not long after, we got to our temporary location for our report."
    sp_adh "After a little body counting, we're ready for our convoy."


    scene camp day
    with medfade

    adh "..."

    sp_adh "I stopped before reaching the truck, Setya was already halfway into the truck convoy."
    
    show setya curious
    with meddis

    sty "What's wrong, Andhra?"
    sty "Come on up. You're in this truck, right..?"
    sty "..."

    show setya determined

    sty "You're thinking about it, huh?"

    adh "...."
    adh "Yeah."

    show setya curious
    sty "And?"

    adh "..."
    adh "I'm going with them."

    show setya determined
    sty "..."
    sty "......"

    show setya relieved
    sty "Figured..."
    sty "I guess they really fit you more, huh?"

    show setya smile neutral
    sty "I've been thinking that you don't really fit in with TNI, Andhra."

    show setya determined
    sty "Not in a bad way. I just think our strict chain of command limits your potential."

    sty "That's what happened back in Kalimantan, right? Even when I wasn't there with you, I know."
    
    adh "..."

    sp_mn "He knows..."
    sp_mn "Is it that obvious..?"
    sp_mn "Doesn't matter... What he said was true."
    sp_mn "But my reason is not because of it..."

    adh "... That's not the only reason."
    
    show setya curious
    sty "Oh?"

    adh "I want to help the people, I don't want to repeat our mistake back in Kalimantan."
    adh "KPR feels... like they're doing the right thing."
    adh "And I'm sure they have much more potential."
    
    show setya determined
    sty "Hmm..."
    sty "Well, if that's what you believed in, I'm not going to question that."

    show setya smile neutral
    sty "If it works for you, then I don't see why not."
    sty "I'll stay here, just to make sure things don't go haywire."

    show setya happy
    sty "I think you'll get along with them. I know you're not the type to stand up to someone more senior."
    sty "Even though I think your ideas are always better than theirs."

    adh "..."
    adh "You're thinking too much of me."

    show setya smile neutral
    sty "Heh, am I, now?"

    show setya happy
    sty "We'll keep in touch in case there's a major change in either of our sides."

    show setya determined
    sty "And just a heads-up, try not to share too much of your side of things. I'll make sure I won't too."

    show setya smile neutral
    sty "Well, I guess I can trust you with that."

    adh "..."
    adh "...Right."
    adh "I will keep that in mind."

    show setya curious
    sty "Oh, and one more thing. Don't try go showing off too much, and don't brag your position in the TNI."

    show setya determined
    sty "If you're starting to become the face of KPR, I'm dragging you out of there, don't you forget. And I'm not playing."

    adh "Haha, I know, I know."
    adh "I'm not the person who will seek fame, you know?"
    adh "And it's not like I have a high rank in the first place, I'm just a Corporal, you know?"

    show setya curious
    sty "Well... That's true..."

    show setya determined
    sty "..."

    show setya smile neutral
    sty "Guess this is goodbye."

    show setya happy
    sty "Don't get killed out there, be safe. I'll get in touch with you as soon as I can."

    adh "Yeah, you too..."

    hide setya
    with meddis

    sp_adh "The convoy started moving, leaving me in the middle of the KPR activity."
    sp_adh "There were also a few TNI soldiers left, presumably to join the KPR."
    sp_adh "I was completely exhausted, so I looked for an empty ready truck convoy reserved for us and took a rest."

    scene black
    with medfade

    return

label scene_1_5:

    sp_adh "I got to Bogor before I even realized it."
    sp_adh "I must've been so tired during the trip from Semarang. I hadn't rested that much."
    sp_adh "It took less than two hours to reach the KPR base."
    sp_adh "I was still sleeping even then."

    pause 3.0

    sp_n "......"
    sp_n "Hot..."

    play ambiance fire_forest fadein 1.0
    scene forest fire at sepia
    with medfade

    pause 3.0

    scene black
    with medfade

    sp_n "I can't breathe..."
    sp_n "... I have to get out of here..."
    sp_n "My legs... So tired..."
    sp_n "...ah."

    scene forest fire at sepia
    with medfade

    stop ambiance fadeout 2.0
    play sound tree_falling
    pause 3.0

    scene truck inside:
        blur 5.0
        zoom 1.1
    play sound heartbeat_long loop

    sp_mn "gasp..."
    sp_mn "... This is..."

    show truck inside:
        ease 5.0 xalign 1.0

    sp_mn "... Right, I was on my way to KPR..."
    sp_mn "Have we arrived..?"
    
    sp_mn "There's no one here..."
    sp_mn "Where are they..?"

    show truck inside:
        ease 3.0 zoom 1.0 xalign 0.5 blur 0

    stop sound fadeout 3.0

    sp_mn "Hot..."
    sp_mn "Damn, I'm drenched..."
    sp_mn "Guess I'll put away my uniform for now..."
    sp_mn "... I should still have my shirt somewhere..."

    scene parking
    with medfade

    sp_mn "..."
    sp_mn "Where's everyone..?"

    sp_adh "Looking around the parking lot, not a single soul was seen."
    sp_adh "The place looked deserted."

    sp_mn "......"
    sp_mn "... Let's try walking around, I guess."

    scene camp day
    with medfade

    sp_mn "Oh, that's people!"

    play music music.neutral fadein 3.0

    camera at camera_zoom

    sp_adh "I walked deeper into the camp. I entered the refugee camp."
    sp_adh "It was busy with people, whether they were KPR, refugees, or even some locals."
    sp_adh "KPR members were moving supplies and giving them out to the people who needed them."
    sp_adh "Medics were taking care of the refugees, and there were even some children playing."
    sp_adh "It's chaotic, but it's a lot like to their temporary camp in Bekasi."
    sp_adh "There were a lot of new arrivals, it seems like most of the refugees decided to come here"
    
    camera at camera_look_up
    
    $ sp_mic.name = "Intercom"
    sp_mic "Attention! If anyone knows where 13-year-old Remy is, please come to this sound source. She was last seen wearing a pink dress. Her family is looking for her!"

    camera at camera_look_center

    $ npc_name = "Tired Refugee"
    $ npc_name2 = "KPR Volunteer"
    npc "I'm sorry, but I don't know where to go. Do you know where tent A4 is? That's where my family should be."
    npc2 "Ah, tent A4 is just around the corner. Just follow this way and turn right. If you need help, just look for someone with a KPR armband, okay?"
    npc "Thank you, young man. Oh, this war, I wonder if it will be over soon-"

    camera at camera_look_right
    
    $ npc_name = "Elderly Refugee"
    npc2 "Here you can have this, ma'am. One per person, please. Let us know if anyone hasn't had their food."
    npc "Is there... enough for everyone?"
    npc2 "Yes, we'll make sure there's enough. Don't worry, ma'am."

    camera at camera_look_left

    $ npc_name = "Child"
    $ npc_name2 = "Mother"
    npc "Mama, Mama. Are we staying long? I want to go home..."
    npc2 "No, sweetheart, we'll stay a little longer and then we'll go."
    npc2 "Your uncle will pick us up soon. Don't you want to see him?"
    npc "Oh, yes!"

    sp_adh "..."
    sp_adh "They seem to be handling it just as well as they did in Bekasi."
    sp_adh "I can't help to see there's not enough manpower to handle all of them though..."
    sp_adh "Hmm?"

    camera at camera_look_center

    $ npc_name = "Young Man"
    $ npc_name2 = "KPR Volunteer"
    npc "Excuse me, where can I sign up for KPR? I want to help."
    npc2 "Oh, this place is not where you can sign up. This is only the refugee camp, you can sign up at the main base."
    npc2 "But if you want to help right away, we need some extra hands back in logistics. I'll write down your name and forward it to the base."
    npc "Alright! Thank you. I'll help then. How can I help?"

    sp_mn "Bingo!"

    camera at reset_camera

    sp_mn "That's where I need to go."

    camera

    sp_mn "Go to KPR Main base, then find out where the rest of the TNI went."
    sp_mn "...Now, where do we go from here—"

    $ npc_name = "???"
    npc "Hey! You there." with hpunch

    sp_mn "Huh?!"

    scene camp day
    with fastfade

    sp_adh "A KPR volunteer suddenly approached me, carrying a crate of ration packs."
    sp_adh "They seemed like they were in a hurry and weren't paying attention to who they were calling."

    $ npc_name = "KPR Volunteer"
    npc "Here, take this to the supply stash at tent A1. It's at the end of the path."

    adh "W-Wait, I'm not—"

    npc "I'm counting on you!"

    adh "He's gone..."

    sp_mn "... Guess I'm doing this now."
    sp_mn "What place did they say I have to put this..?"
    
    scene warehouse
    with medfade

    sp_mn "Phew, That should do it..."
    sp_mn "Now I should go..."

    show warehouse
    with fastfade

    $ npc_name = "KPR Medic"

    npc "Oh, you're new? Did you just finished storing the supplies?"

    adh "I, uh, yes. I did that."

    npc "Great, can you help me bring some of the supplies to the refugees?"

    adh "Huh? W-wait, but I—"

    sp_adh "Before I could explain myself, she's already on the stash, counting the supplies. Checking something on her clipboard."

    npc "Mhm, this is pretty good. Here, it's a list of ration you need to bring."
    npc "Just bring it to the 2B tent, please."
    npc "Thank you."

    adh "... And there she goes..."
    
    sp_mn "Sigh..."

    scene camp day
    with medfade

    adh "Here you go... That should be all, right?"

    sp_adh "I ended up bringing some of the crates to the tent."
    sp_adh "I tried to talk to someone, but everyone was just so busy with their own assignment. I felt bad for bothering them."

    npc "Thanks for bringing the supplies. You can get back to your work."

    sp_mn "Okay... That's done. Oh I should ask for a directions to the main base—"

    $ npc_name2 = "Elderly Refugee"
    npc2 "Miss... Can I trouble you for another water?"

    npc "Oh, yes, no problem. Please this way."

    sp_mn "Or not..."
    sp_mn "Sigh..."
    sp_mn "We should be able to find our way there..."

    scene road
    with medfade

    sp_mn "... Alright, all we have to do is to follow this path..."

    $ npc_name = "Lost Kid"
    npc "Hey mister..."

    sp_adh "I felt a tug on my sleeve, turning around, I saw a lost child. Around 13 years old of age, wearing a pink dress."
    
    npc "Do you know where my relatives are? I'm lost."

    adh "A-ah, I..."

    sp_mn "..."
    sp_mn "I don't see any KPR officer here."
    sp_mn "Sigh... Let's go back to the camp."

    adh "Sure, let's find your Mama."

    npc "Yay! Thank you, Mister."

    sp_mn "Here we go again..."

    scene camp day at center, bg_close(yval=1.0, zoomval=1.1, blurval=0)
    with fastfade

    $ npc_name = "KPR Volunteer"

    npc "Alright, thank you for reporting the child, sir."
    npc "We'll look for their parents in a minute, so just leave it to us."
    
    sp_mn "Here's my chance."
    adh "Ah, right I have a—"

    camera at camera_look_right

    $ npc_name2 = "Young Mother"
    npc2 "Excuse me... I'm trying to meet with my husband."
    npc2 "He should be around here in this camp. Can you help me find him?"
    npc "Of course, ma'am. May I get his info, please?"

    sp_mn "Argh... I missed my chance again..."

    camera at camera_look_left

    npc "There you are, you've already finished your other work, right? We need some help to sorting out our inventory." with vpunch

    camera at reset_camera

    sp_mn "..."
    sp_mn "I'm never getting out of here, am I?!"

    scene warehouse
    with slowfade


    sp_mn "Phew... That's about it..."
    sp_mn "How long have I been working here..."
    sp_mn "I'm not even registered yet, and I'm working so hard..."

    sp_adh "After doing chores all around the place, I finally found a place to take rest, even for a brief moment."
    sp_adh "The place was rather secluded, so I wasn't expecting anyone to find me."

    sp_mn "How did this even happen? I was trying to find out where I was supposed to go, and suddenly I'm playing the delivery boy for a militia I haven't even joined."
    sp_mn "I mean... It's not like I'm opposed to doing these, but shouldn't I be doing something else the main base now!?"
    sp_mn "Sigh..."
    sp_mn "... I think I'm getting a little bit tired now."
    sp_mn "A quick nap wouldn't hurt, right?"
    sp_mn "......"
    sp_mn "..."

    scene black
    stop music fadeout 1.0
    with medfade

    sp_adh "The noise of the camp is still loud, but I was still able to tune it out."
    
    sp_mn "Finally... A moment for myself—"

    play sound footsteps_concrete fadein 1.0

    pause 3.0

    stop sound
    
    sp_mn "Or maybe not..."
    sp_mn "I swear if one more person hands me another crate, I'm going to—"

    $ eka.name = "???"

    eka "You seem so comfortable there."

    sp_mn "Huh..?"
    
    scene warehouse
    show eka disappointed
    with medfade

    pause 1.0

    scene warehouse at bg_close, inspect
    show eka disappointed at closer, inspect
    with meddis

    sp_adh "As I opened my eyes, there she was, a sharp-eyed woman right in front of me."
    sp_adh "She wasn't in uniform at all, but her posture was like that of a military officer."
    sp_adh "But she did wear a KPR armband just like every other member here."
    sp_adh "I couldn't shake the feeling that she might be someone important."
    sp_adh "Her face certainly didn't look like she was too happy to see me."

    adh "Um..."

    sp_mn "She looks hella mad..."
    sp_mn "Is it that bad to take a break here?"

    scene warehouse
    show eka serious
    with meddis

    eka "You know, I was surprised by how eager a TNI soldier was to get to our stash."
    eka "Mostly, new recruits check in first before running around my place."
    eka "And you're certainly not from arond here."

    adh "W-wait! There has been some misunderstanding—"

    eka "Yeah, I know."

    sp_mn "..."
    sp_mn "..... huh?"
    sp_mn "She... knows?"

    show eka smile
    with meddis

    eka "I'm just messing with you."

    adh "W-What?!"

    play music music.funny

    show eka curious

    eka "You're the missing soldier from the convoy, right?"

    show eka talking left

    eka "Um... Your name was—{nw=1.0}"

    show eka smile
    with None

    extend "Andhra, was it?"

    show eka serious
    eka "There was a little mix-up when we counted the TNIs coming, a little miscount."

    show eka embarassed
    eka "So that's our mistake. I apologize for the oversight."

    adh "A-ah, no, it's okay... It was my mistake too for oversleeping in the truck."

    show eka curious
    eka "Well..."

    show eka serious
    eka "I totally understand. You've come a long way from Kalimantan to here."
    eka "You must've only gotten a short rest along the way."
    eka "If we didn't miscount, we would've checked on you."

    adh "I-it's really okay..."

    eka "..."
    
    show eka curious
    eka "Well, if you're okay with it."

    show eka wink
    eka "Let's just forget about this whole thing."

    show eka talking left
    eka "Anyway, I think this one is a bit overdue, but."

    show eka happy
    eka "Ahem, Welcome to KPR, Corporal Andhra Riyadi."

    show eka smile
    eka "My name is Eka Putri Lestari, the one managing most things here."

    $ eka.name = "Eka"

    show eka talking left
    eka "You could say I'm some sort of a leader here."

    adh "Huh..."

    sp_mn "The leader..."
    sp_mn "Wait!" with hpunch

    adh "Y-you're the leader!?"
    adh "As in the head of command of the entire KPR?!"

    show eka flustered
    eka "Y-yeah... That's a bit true..."

    show eka blush
    eka "Why did you scream so suddenly..."

    adh "I'm sorry for sleeping in your store room, ma'am!"
    adh "I didn't mean it!"
    adh "It was just for a small rest, that's all."

    show eka happy
    eka "Oh, come on. it's no biggie."
    
    show eka talking right
    eka "As I said, you're exhausted already. It's normal for you to take a rest."

    show eka talking left
    eka "Besides, you've been so incredibly helpful, and I really appreciate it."

    adh "... I have?"

    show eka smile

    eka "Oh absolutely, I've seen you running around the camp for a while now."

    show eka smug
    eka "You didn't look like you were complaining so I just sat aside."

    adh "H-huh? Really?"

    sp_mn "She's been watching me all those times..."
    sp_mn "... and she hasn't said a thing!?"

    show eka embarassed
    eka "Hey, what's that look for?{w=.5} I didn't know a TNI soldier got loose, okay?"
    eka "I only got the news after I lost sight of you. So sorry about that!"

    show eka smile
    eka "Ahem. Anyway, I think you deserve some rest after this."
    eka "I'll be happy to escort you to the main base as an apology. We have a bathhouse and cafeteria."

    show eka talking right
    eka "Clean yourself up and get something to eat."

    adh "T-thank you... ma'am... you don't need to..."

    show eka disappointed
    eka "Oh, come on, don't call me that."
    eka "I'm still young. I'm not even that much older than you."
    
    show eka smile
    eka "You can call me by my name. Is that all right? Corporal?"

    adh "Ah... okay... thank you, Eka."

    show eka wink
    eka "Yes, you're welcome."

    show eka smile
    eka "Anyway, I'll lead you the way then. You can follow me now."

    show eka smug
    eka "I'll make sure no one asks you for help on the way, ha ha!"

    adh "Hey!"

    show eka smug at moveoutright

    sp_mn "..."
    sp_mn "So she's the leader..."

    hide eka

    sp_mn "I didn't expect the leader to be a woman, and I especially didn't expect her to be so friendly..."
    sp_mn "This is why they say KPR was more lenient than TNI, huh..."

    scene black
    stop music
    with medfade

    sp_adh "I followed her through the refugee area. The area has calmed down just before the sun started to sets."
    sp_adh "The air was hot, but not as much as it was in the noon."

    return

label scene_1_6:

    scene camp day
    with medfade

    play music music.kpr_base

    sp_mn "So..."
    sp_mn "I ended up walking side-by-side with the one running the whole thing."
    sp_mn "But..."

    show eka smile

    eka "Oh, hey Dian."

    show eka serious at moveleft

    $ npc_name = "KPR Volunteer (Dian)"
    npc "Oh, Boss. What's up?"

    eka "Is the deal with the water supply settled yet?"

    npc "Oh, yeah, more or less. We'll probably need a refill in the morning."
    npc "But, we've got it covered for now."

    show eka smile
    eka "Gotcha. If you run into any problem, you can talk to Yadi. I'm sure you already know."

    npc "Yeah, I've heard it like a million times now."

    show eka disappointed
    eka "Sigh, the last time I didn't remind you enough, you ruined one tent."
    eka "You should've been glad Tiara was around to help."

    npc "Ah, come on, Boss. That was just a one-time thing."
    npc "No need to be salty about it."

    show eka smile
    eka "Yeah, sure. Anyway, I'm heading back to the base. Good work out there."

    npc "Right! Boss! You too."

    show eka smile at movecenter

    sp_mn "..."
    sp_mn "She's very casual."
    sp_mn "Very different."

    show camp day
    with medfade

    sp_adh "We got to a small medical tent. It looked like an outpost of some kind."
    sp_adh "There was a tired-looking woman cleaning up the remains of the medical supplies."

    show eka curious at moveright

    eka "Hana, how's everything holding up? You don't look so hot."

    $ npc_name = "KPR Medic (Hana)"
    npc "Huh? Oh, Eka. Barely, but oh well, it could be worse."
    npc "There are still a lot of leftovers for the next batch of people."
    npc "It seems like our branch in Bekasi did a pretty good job at taking care of the people there."

    show eka smile
    eka "I see. Then, take a rest after you finish cleaning up."

    show eka talking right
    eka "Can't have you feeling unwell when everyone's hands are needed here."

    npc "Sure, Eka. You're going to the base? Have a safe trip."

    show eka smile at movecenter

    sp_mn "Some people called her by her name too."
    sp_mn "They seem to see her as a colleague more than a superior."
    sp_mn "..."
    sp_mn "...... No, it's as if she's just another volunteer."

    scene road
    show eka smile
    with medfade
    play music music.walking

    sp_mn "..."

    sp_adh "After walking through the tents, we finally got out of the camp."
    sp_adh "We kept walking toward the woods"

    show eka disappointed

    eka "What's wrong, you're being very quiet for a while know."

    show eka curious
    eka "Thinking about something?"

    show eka flustered
    eka "There's something on my face, isn't there??"

    adh "Nah, It's just..."

    adh "I dunno, you're not quite what I was expecting."

    show eka curious
    eka "Huh... What exactly were you expecting?"

    show eka smug
    eka "Oh, were you expecting a warlord or something?"
    eka "Barking order, getting saluted every inch I go?"
    
    show eka talking right
    eka "Well, I'm not sure if that's a good depiction of a militia leader though."

    adh "I was... expecting you to be a lot more... strict?"

    show eka curious
    eka "Huh..."

    show eka smile
    eka "I mean, I CAN totally be serious when I need to. There's just no reason to be so strict all the time."

    show eka concerned
    eka "It tends to be exhausting, you know?"

    show eka disappointed
    eka "Besides, it's not like everyone can perform better under pressure."

    show eka smile
    eka "I'd rather know them better, so I know what to do to raise their morale."

    adh "..."

    sp_mn "She's speaking like a true leader."
    sp_mn "Different from TNI. where leadership has been taken over by the system."
    sp_mn "She gets her fellow members to a personal level, to a point where they're comfortable with seeing her often."

    adh "It just feels weird... Seeing the one making sure everything is running in the background is... Just here."
    adh "It feels different..."

    show eka curious
    eka "Different from TNI? Is it good different or bad different?"

    adh "... I dunno, it just feels different."

    show eka smile
    eka "You still haven't decided yet? Well, I guess that's alright."

    show eka serious
    eka "It takes time to adjust, especially since you've been with TNI for a while."

    adh "No, it's not just that."

    show eka curious
    eka "Oh?"

    adh "Back in Surabaya, the government was running everything. People are in uniform, soldiers or officials."
    adh "But here... it's more mixed, more free. Everyone feels accepted."

    eka "..."

    show eka smile
    eka "I see."

    show eka explain
    eka "That's just how we do things here. The government and the TNI have their own way of running operations, but here, it's different."
    eka "Some of our people are former TNI, engineers, students, mechanics, or even just plain civilians."

    show eka smile
    eka "We're open to anyone. What matters is that they're willing to help."

    adh "And... That works?"

    show eka talking right
    eka "I dunno, you tell me."

    show eka smile
    eka "Did you not just leave a functioning refugee camp?"

    adh "..."
    adh "I guess, yeah. You're right."

    show eka talking right
    eka "But, it's not like they're completely useless to us. I'm sure that much is obvious."

    show eka serious
    eka "The government and the TNI have the resources, the structure and the legitimacy to fight this war on a national scale."

    show eka concerned
    eka "Without them, there wouldn't even be a battlefield to fight own."

    show eka determined
    eka "But their strength is also their greatest weakness—bureaucracy, rigid command structures, and politic responsibilities slow them down."
    eka "They can't afford to move fast, to take risk, or even to focus on the individual struggles of the people."
    
    show eka smile
    eka "That's where we come in."

    show eka determined
    eka "KPR isn't a replacement for the government, let alone the military—we're a bridge."
    eka "We can respond faster, adapt quicker, and make direct decisions without waiting for order to go through a dozen desks."

    sp_mn "..."
    adh "So... You're saying that KPR is just here to fill in the gap?"
    adh "That's a nice way of putting it. I'm not sure if people have the same idea though."

    show eka smile
    eka "That's just because we're closer than them. They trust us more simply because of that fact."

    show eka smile
    eka "We're closer to people because we are the people."

    show eka concerned
    eka "But trust doesn't translate to capabilities.."

    show eka disappointed
    eka "We don't have the same level of resources, authority, and power."

    show eka sad
    eka "We can't sustain the war the way a real military force can."

    show eka serious
    eka "We might do what they can't, heck we might even feel like we're doing better than them, but in the end, we still need them."

    show eka smile
    eka "The only reason we can do what we do is because they're keeping the war going."    

    show eka determined
    eka "We're just another way to handle this war—one that listen and connect to the people more."


    adh "Still, it's gotta sting when people look at you like you're their real leader and not the ones in charge."

    show eka smile
    eka "Nah, it doesn't sting, it worries me. The moment people start thinking KPR is the answer, they forget why we exist."

    show eka disappointed
    eka "Many people think KPR is proof that the government is failing. But that couldn't be more wrong."

    show eka determined
    eka "We're only here because war doesn't care about policies, procedures, or fair play. It just happens."

    show eka serious
    eka "And someone has to fill in that gap. That's all we are."

    adh "... I see."
    adh "So if the war drags on, even KPR is going to hit a wall eventually."

    show eka smile
    eka "Exactly. And when that time comes, that's when they'll realize, we need the government as much as they've needed us."

    show eka serious
    eka "That's why I don't fight against the system—I just don't want to get stuck in it."

    adh "I see."

    sp_mn "So, KPR is not a replacement for the government, that much is true."
    sp_mn "They're only here so people can get help faster by directly addressing the problem."
    sp_mn "As a buffer so the government can do what they do best while we're here to make sure people are safe."
    sp_mn "They're doing well now, but even they have limits."
    sp_mn "If the war drags on, they're going to struggle too."
    sp_mn "And if we're not careful, people is going to place their hope on something that isn't built to last."
    sp_mn "......"
    sp_mn "..."

    scene black
    with medfade
    stop music

    sp_adh "We walked a bit more after that."
    sp_adh "Not even long we reached the main base."

    scene base sunset
    with medfade
    play music music.kpr_base
    
    sp_adh "There were a couple of buildings inside the region of the base."
    sp_adh "They're a mix of repurposed buildings, and prefab buildings, and there were also a few tents outside."
    sp_adh "The atmosphere is quite lively. A couple people were chatting with each other."
    sp_adh "Some were just walking by, and some other were moving supplies."
    sp_adh "It was both an expected and unexpected sight."

    show eka happy
    eka "Here we are. Your new home, Corporal."

    adh "..."
    adh "Didn't expect there to be some buildings here."

    show eka smug
    eka "Did you think we lived far in the woods or something?"

    adh "Well... We did walk far through the woods."

    show eka embarassed
    eka "That's true, but never mind that."

    show eka smile
    eka "We had a few volunteers who were kind enough to let us use their place."
    eka "Since it's so deep, some of the buildings were just left behind."

    show eka concerned
    eka "It took forever to renovate them, you know?"
    
    adh "Ah..."
    adh "Is it even safe?"

    show eka curious
    eka "Hmm?"

    show eka smile
    eka "Oh, don't worry about that. We made sure everything is safe."
    eka "We managed to hire some professionals to make sure of it."

    show eka wink
    eka "I can assure you, they're even stronger than some of those buildings in Kota Tua."

    adh "..."
    adh "Is that really a good comparison? You're comparing them with old buildings, you know?"

    show eka talking right
    eka "Well, they did survive for four centuries. I'd say it's a good comparison."

    adh "Sure."

    show eka embarassed

    pause 1.0

    show eka determined
    eka "Anyway, you should clean yourself up."

    show eka smug
    eka "You smell like someone who's been running around like a headless chicken all day."

    adh "Hey!"

    sp_mn "Sigh... I thought so much of her."
    sp_mn "Great leader, charismatic and trusted."
    sp_mn "Then she dropped this unfunny joke."
    sp_mn "..."
    sp_mn "It's not like I opposed to that though..."

    show eka smile
    eka "The bathhouse is at the end of the base. Just follow that path. I need to be somewhere first."
    eka "If you're hungry, the cafeteria is close from the bathhouse."

    show eka smug
    eka "Oh, and don't worry about getting drag to work."
    eka "Everyone here wears a KPR armband. People would think you're just an outsider or unregistered TNI."

    show eka wink
    eka "See you later, Corporal."

    show eka wink at moveoutright

    adh "H-hey!"

    hide eka

    sp_mn "And there she goes..."
    sp_mn "......"
    sp_mn "Let's just go to the bathhouse."

    stop music
    scene black
    with medfade

    sp_adh "With that, I went to the bathhouse to clean off."
    sp_adh "There were barely anyone there, mostly because it's almost dark now."
    sp_adh "I forgot that I left my backpack back on the refugee camp. Only realizing after I finished bathing."
    sp_adh "I didn't have any clothes to change into."
    sp_adh "Fortunately, the bathhouse keeper had some spare clothes for me."
    sp_adh "After thanking them repeatedly. I found my way to the cafeteria."
    sp_adh "Similar to the bathhouse, there were barely anyone there. Fortunately, it was still open."

    scene cafeteria night
    with medfade

    play music music.cafeteria

    sp_mn "Huh..."
    sp_mn "The place is cleaner than I thought."
    
    sp_adh "I went deeper into the cafeteria. It was a self-service style."
    sp_adh "Luckily, there were still some leftovers from the lunch time."

    sp_mn "..."
    sp_mn "How has it been since I've seen these foods..?"
    sp_mn "Fried tempeh, tofu, cucumber... Sambal... And rice..."
    sp_mn "I thought I saw the chicken tray, but it's already gone."
    sp_mn "Guess I came really late."
    sp_mn "Well, this is more than I had for a couple of months, so I won't complain"

    sp_adh "After trying all kinds of food I hadn't had since the start of the war, I went around for a place to sit."
    sp_adh "There weren't any full seat to begin with."
    sp_adh "The empty cafeteria means empty seats, I could practically sit anywhere."
    sp_adh "I picked the back of the seat nonetheless. Not wanting anyone to talk to."
    sp_adh "As I tried to eat my food, I've been thinking about the day."
    sp_adh "I've seen how KPR operated, at least how they handled the refugees."
    sp_adh "And also, how the their members interacted with the leader."

    sp_mn "But is Eka the only leader, the only one managing the whole thing?"
    sp_mn "Probably not, she said rank doesn't matter."    
    sp_mn "So there must be someone else with her."

    sp_adh "I was thinking about the command system of KPR, and I felt like someone else was with me."
    sp_adh "I immediately recognized the voice, though."

    eka "Oh, there you are. Doesn't seem we need a search party this time after all."

    show eka smile at moveinleft, center

    sp_adh "I saw her with her papers and a tray of food in her other hand as I looked over."
    
    sp_mn "Speak of the devil."
    sp_mn "...Why does she bring her paperwork with her?"
    sp_mn "Is this her idea of efficiency?"

    adh "Says the person who watched a headless chicken with popcorn at the ready..."
    adh "Are you eating a late lunch?"

    show eka happy at nodding
    eka "Yeah, I usually end up eating last because of some work stuff."

    show eka smile
    eka "You don't mind if I sit here, right?"

    adh "Well, aren't you the one who owns this table?"

    show eka smug
    eka "Oh, you're one step ahead of acknowledging the one who holds everything huh, Corporal?"

    camera at camera_zoom
    show cafeteria night:
        blur 2.0
    with fastfade


    sp_adh "Eka was working on her paper at the lunch table, but she was so focused that she didn't even notice the food on her plate."
    sp_adh "I wasn't trying to be rude, but she didn't even touch her own food."

    show eka sad at sighing
    eka "Sigh... There's so much to do..."

    show eka concerned
    eka "This has to be delivered right in the morning..."

    show eka concerned at umuumu

    pause 1.0

    show eka curious
    eka "And this..."

    show eka curious at umuumu
    
    pause 1.0

    sp_mn "..."
    sp_mn "Her foods are getting cold..."

    show eka talking right at umuumu

    sp_mn "She's quite the hardworking leader, despite her casual approach..."

    adh "Hey, Eka."

    show eka curious
    eka "Hmm?"

    show eka smile
    eka "Oh, right. Sorry."

    show eka talking right at shaking
    eka "I've got a lot on my hands, but you're right."
    
    show eka smile
    eka "You're here, and I don't want waste your time."

    show eka serious
    eka "Wait a moment."

    show eka concerned at umuumu

    pause 2.0

    show eka smile
    eka "What's up, Corporal?"

    adh "Well... Not much..."
    adh "How's your work?"

    show eka curious
    eka "What? This? It's no biggie. I can finish this tonight."
    
    show eka smile
    eka "I'm not usually this busy. It's just because of those new TNI recruits and refugees coming today."

    show eka concerned
    eka "The recruits aren't really the problem. It's just that there were a lot more refugees than we thought there'd be."

    adh "Oh? Is that so?"

    show eka curious
    eka "There's not much we can do about it at this point."

    show eka smile
    eka "We'll just have to find more supplies and more people to help out."

    show eka wink
    eka "Luckily, there were lots of refugees wanting to join in."

    show eka smile
    eka "So, in the end, it wasn't all for nothing."

    sp_mn "..."
    adh "I see, that's good then."

    show eka curious
    eka "What's got you all worked up, Corporal? You haven't even joined yet."

    adh "It's just..."
    adh "Nothing."

    show eka smile
    eka "I see..."

    sp_mn "..."
    sp_mn "Is she though?"
    sp_mn "... I suppose so. She knows what's going on with the government."
    sp_mn "But, I should talk about something else."
    sp_mn "She'll be buried in her work again if I don't talk about anything."

    adh "By the way, why do you always call me Corporal?"

    show eka surprised
    eka "Huh? Isn't that your rank? You don't like it?"

    adh "Well, it's not like I dislike it."
    adh "It's just, how do you even know I was a Corporal?"
    adh "You even know my name."

    sp_mn "She did call me by my full name."
    sp_mn "And I haven't even introduced myself."

    show eka curious
    eka "Oh, that's your problem?"

    show eka smile
    eka "Well, I've got the list of soldiers coming from TNI already."
    eka "So I know most of your faces and names already."

    show eka smug
    eka "Oh, I also knows of your personal history at the back of my head."

    adh "What, really?"
    adh "We were just coming a couple of hours ago, and you've already memorized our names?"

    sp_mn "Does she have a photographic memory? That seems unbelievable."

    sp_mn "..."
    sp_mn "......"
    sp_mn "She doesn't know, doesn't she?"

    show eka flustered
    eka "Alright—Alright, I only skimmed through some of the your files. Mostly the ones with the higher rankings."

    show eka serious
    eka "I know we don't care as much rank as the TNI."

    show eka talking right
    eka "But you won't blame me for paying more attention to them, right?"

    adh "I mean, yeah. If I was a sergeant or even a lieutenant and I joined a militia out of the blue, people would definitely notice."
    adh "Who's the highest-ranking person in our convoy?"

    show eka determined
    eka "There were a couple of sergeants there. Oh, and a first sergeant too."

    show eka concerned
    eka "If I can remember his name...{nw=.5}" 
    
    show eka talking left
    with None
    extend " {i}Luthfi Gunawan{/i}, I think?"

    show eka curious
    eka "Does that ring a bell?"

    adh "Hmm..."

    sp_mn "Luthfi Gunawan, huh..."
    sp_mn "..."
    sp_mn "......"
    sp_mn "Nope, don't know him."

    adh "I think he might be at a separate unit back in Kalimantan."

    show eka smile
    eka "Oh, I see."
    
    sp_mn "..."

    adh "Wait, that doesn't explain why you knew me though."

    show eka surprised
    eka "Oh..."

    show eka curious
    eka "Well, you were certainly one of the most stood out of every soldiers there."

    adh "Huh... Am I that interesting? At least to you?"

    show eka smug
    eka "Not really, but you were the only one getting lost."

    adh "... Should've knew that was coming."

    eka "It's impressive, really. Seeing a TNI committing a desertion just to help out civilians."

    show eka wink
    eka "You're probably the first. You should be applaud."

    adh "That's not desertion, it's called being left behind."
    adh "And you were the one leaving me behind."

    show eka smug at shaking
    eka "Oh, come on. It's not like that's a bad thing, right? I promise it won't happen again."

    show eka talking right
    eka "Not unless it's funny though."

    adh "Hey! I hear that."

    sp_adh "We kept to chatting while we finished our food."
    sp_adh "It seemed like I was able to keep her out of her paperwork."
    sp_adh "For the better or for worse."

    scene cafeteria night
    show eka smile
    with medfade

    sp_adh "As I scraped the last bits of rice off my plate, I set my plate aside."
    sp_adh "On the other side of the table. Eka stretched her arms behind her."
    sp_adh "She finished her food well before I did, and has returned her tray back to the return table."
    sp_adh "Whether her paperwork has finished or not, nobody knows."

    camera at reset_camera

    sp_adh "We finish the food as soon as the sky is getting darker."
    sp_adh "The people were starting to come to get their dinner. It seems like we've been here for too long."

    show eka smug
    eka "What do you think of the food? You don't look like you hated it."

    adh "It's better than ration packs, at least."

    show eka smile
    eka "Glad to know that."

    show eka serious
    eka "Anyway. What's your plan for now? Do you know anyone who lives around here?"

    adh "Huh..."

    sp_mn "I didn't think much of that..."
    sp_mn "I don't have a relative from around here, now that I think about it."

    adh "No..."
    adh "But I figured I'd get a room. You do provide room for the recruits, right?"


    show eka curious
    eka "Well, that's not wrong."

    show eka disappointed
    eka "But you haven't officially registered yet, you know?"

    adh "I haven't?"
    adh "I thought it had already been taken care of. You know our names and all."

    show eka serious
    eka "Yeah, that's true. We'll still need to do some kind of in-person authentication."
    
    show eka disappointed
    
    eka "Someone could change their mind at the last second and decide not to register at all."

    adh "That... happens?"
    
    show eka talking right
    eka "Nah, not really, it didn't happen this time, at least. All of the TNI soldiers were accounted for."

    show eka smug
    eka "Well, you are an exception."

    adh "Oh, that's just great."
    adh "So what now? Do I find an empty bench in a park somewhere?"

    show eka curious
    eka "Well, that's certainly a solution."

    show eka disappointed
    eka "But most parks here are privately owned, and they don't open at night."

    show eka smug
    eka "So you can either find a way to beg someone to let you in, or you can sleep on the street."

    adh "..."
    adh "Is... that it..?"
    adh "I'm just going to sleep at the street?"
    
    show eka flustered
    with meddis
    eka "Well... the locals here are pretty nice though... so I doubt anyone would let you sleep on the street."

    sp_mn "..."
    sp_mn "What's up with the sudden fluster?!"

    show eka blush
    eka "B-but, lucky for you, I happen to know about a \"vacant\" room that you can use."

    show eka smile
    eka "We need to swing by the office first though, to get you through."

    adh "That seems convenient..."

    eka "Well, the open recruitment is until tomorrow, so a vacant room is to be expected."

    adh "I don't like the way you say it, though."

    show eka smug
    eka "It's a perfect place to stay. Better than a bench, for sure."

    adh "I don't like how you make that face, though!"

    stop music
    scene black
    with medfade

    sp_adh "Having no other choice, we walked our way to the office building."
    sp_adh "The place wasn't that far from the cafeteria."
    sp_adh "We arrived at an old, weathered high school building."

    return

label scene_1_7:
    
    scene base kpr main night
    with medfade
    play ambiance night

    sp_adh "Cracks snake along the concrete walls, faded banners from a time long before the war still hang near the entrance."
    sp_adh "The old school emblem was barely visible beneath a newer KPR flag, awkwardly covering it."
    sp_adh "Some broken windows on the upper floors were patched with wooden boards."
    sp_adh "There weren't a lot of people outside, but the sound of paper rustling and muffled voices could be heard from outside."
    sp_adh "The office was so busy processing all of the new recruits coming."
    sp_adh "We stopped just in front of the entrance when Eka stopped."

    show eka serious
    eka "Okay, you'll have to wait here. The office is restricted to personnel only."

    adh "Figured... What are you going to do inside?"

    show eka concerned
    eka "Well, I'll need to grab the keys and contact the dorm keeper as well as a few other people."

    show eka serious
    eka "Oh, right. they might lose the key. You better get ready to sleep outside."

    show eka smug at moveoutright

    adh "Huh!? Hey wait!"

    hide eka

    sp_mn "There she goes again..."
    sp_mn "Why does she always seem in hurry..?"
    sp_mn "Sigh... Whatever. Time to wait."

    sp_adh "Just as I was thinking about it, something—or rather, someone—bumped into me—"

    play sound explosion

    extend "nearly knocking me off balance." with vpunch
    sp_adh "I instinctively turned around to face the person who bumped into me before the noise of boxes falling reached me."

    $ ina.name = "???"

    ina "Ouch, ouch. That hurts..." with fastfade

    sp_adh "I saw a young woman sitting on the ground with boxes scattered all around her."
    sp_adh "After expressing her pain, She saw the mess she had made."
    sp_adh "She got a little panicky, but I was able to talk to her before that happened."

    adh "Are you okay? You should've watched where you were going."

    sp_adh "I offered her my hand to help her up, which she reluctantly accepts."

    show intan blush:
        center
        yoffset 100
        ease 1.0 yoffset 0

    pause 1.0
    ina "T-thank you, I'm fine. I'm really sorry, I'll make sure it doesn't happen again."

    stop ambiance fadeout 5.0
    play music music.playful_intan

    adh "Ah, no. I was the one standing on your way."

    show intan blush:
        ease 1.0 yoffset 100 alpha 0.0
    ina "Sigh..."

    hide intan

    sp_adh "She went back down to get her stuff."

    sp_mn "I should help her..."

    show base kpr main night
    with medfade

    adh "So, where are you taking these stuff?"

    show intan troubled
    ina "A-ah, you don't have to..."

    adh "I insist, I'm just waiting someone anyway, so I don't mind."

    show intan processing
    ina "Huh...?"

    show intan blush
    ina "I-if you're okay, then umm... It's the storage room, just beside the office..."

    adh "Okay, then."

    show intan concerned
    ina "..."

    scene warehouse office
    with medfade

    adh "Here's good, right?"

    ina "Y-yeah..."

    sp_adh "We finished putting everything inside the storeroom."
    sp_adh "Even though the room itself was separate from the school buildings, it was still in the office area."

    sp_mn "Am I even allowed here?"
    sp_mn "Well, no one complained, so I suppose it's fine."

    show intan smile
    ina "Could you wait outside for a moment? I need to check if everything is still there."

    adh "Ah, sure. Feel free."

    scene black
    with medfade

    sp_adh "After checking everything inside, she went outside and locked the storeroom."
    sp_adh "The security was pretty restrictive. Even though it's inside of the office area with a gate, they still needed an extra lock."
    sp_adh "We walked outside of the office area after everything had been checked."
    
    scene base kpr main night
    show intan pout
    with medfade

    ina "Hmm... All that left is... *mumble* *mumble*"

    sp_mn "She's mumbling to herself, huh... She's pretty busy, despite how she looks."
    sp_mn "Maybe she could rival Eka, even."

    show intan happy at umuumu
    ina "Okay! Most of my work is done."
    
    show intan smile
    ina "Oh, right. I forgot to thank you. You sure are a livesaver."

    show intan pout
    ina "I could take another hour if I did it by myself."

    show intan relieved
    ina "Thanks to you, we did it twice as fast."

    adh "Oh, ha ha. It wasn't that big of a deal. I hardly did anything."

    show intan surprised
    ina "Oh, no. You did a great work actually."

    show intan soune
    ina "I'm not strong enough to do it alone, so your strength was actually helping the most."

    adh "Is that so? Glad to hear it."

    show intan curious
    ina "Oh, yeah. By the way, are you new here?"

    show intan pout
    ina "I've never seen you around here before."

    show intan soune
    ina "Well, I mostly work on maintenance though, so I doubt I know everyone here—"

    show intan blush
    ina "{cps=120}I'm quite introverted too, actually.{/cps}{nw=.01}"

    show intan soune
    with None
    ina "{cps=120}Oh, but I have friends!{/cps}{nw=.01}"

    show intan determined
    with None
    ina "{cps=120}So you don't have to worry about that—{/cps}{nw=.01}"

    show intan smile
    with None
    ina "{cps=120}I also have a good relationship with Captain Eka.{/cps}{nw=.01}"

    show intan soune
    with None
    ina "{cps=120}She can be quite cruel though,{/cps}{nw=.01}"

    show intan cry
    with None
    ina "{cps=120}She cuts my paycheck every now and then every time I mess up.{/cps}{nw=.01}"

    show intan blush
    with None
    ina "{cps=120}I mean, it was an honest mistake, but I guess you could still call it a mistake.{/cps}{nw=.01}"

    adh "Yes, yes! I'm new here.{w} I just got here too, actually." with hpunch

    sp_mn "Had to cut her there, I got the feeling she won't stop..."
    sp_mn "Did she really talk about her paycheck at the end there...?"
    sp_mn "Wait, would I get a paycheck?"
    sp_mn "No, no. We're getting sidetracked here."

    show intan surprised
    ina "Oh, really?"

    show intan smile
    ina "Welcome to KPR then! I'm Intan Haira Nurjaya."

    $ ina.name = "Intan"

    show intan happy
    ina "I'm a mechanic, sometimes I work on logistics, {nw}"

    show intan soune
    with None
    extend "Other times, I'm a janitor... And sometimes a box hauler too, as you just saw before..." 

    show intan pout
    ina "Well, basically anything you need me to do... I can probably do..."

    show intan troubled
    ina "Just don't expect too much of me..."

    show intan smile
    ina "A-anyway, it's nice to meet you, new guy."

    sp_adh "She said, as she reached out her gloved hand to me."
    sp_adh "It took me a minute to process at what she just said."
    sp_adh "But I gave up, and just shook her hand back."

    adh "Yeah, Andhra. Andhra Riyadi."

    show intan smile at nodding
    ina "Okay, nice to meet you, uh, Andhra..."

    show intan processing
    ina "Hmm... Andhra..?"

    stop music fadeout 2.0

    show intan surprised
    ina "As in, Corporal Andhra Riyadi, one of the TNI soldier coming from Bekasi?"

    adh "Uh... Yes. Why are you being so specific—"

    show intan troubled at jumping
    with vpunch

    play music music.funny

    ina "Aaaah!! Why are you here!?{nw} "
    extend "No, how can you be here!?" with hpunch

    adh "Huh? What do you mean?"

    sp_mn "She freaked out really bad there..."
    sp_mn "Could it be?"

    show intan cry
    ina "Oooh, I'm saved."

    show intan relieved
    ina "Thank God, I found you. You don't know how hard I tried looking for you—"

    show intan troubled at jumping
    with vpunch
    ina "{cps=120}It was my mistake!{/cps}{nw=0.01}" with None
    ina "{cps=120}I messed up when we counted the soldiers.{/cps}{nw=0.01}"
    
    show intan determined
    with None
    ina "{cps=120}I thought you were there, so I marked you just like the others.{/cps}{nw=0.01}"

    
    show intan cry
    with None
    ina "{cps=120}I didn't realize until I double-checked at the recruitment post.{/cps}{nw=0.01}"
    ina "{cps=120}One was missing, and that was you!{/cps}{nw=0.01}"

    show intan flustered
    with None
    ina "{cps=120}The person I mindlessly marked as present.{/cps}{nw=0.01}"
    ina "{cps=120}But by then, more than half of them have already been registered.{/cps}{nw=0.01}"
    ina "{cps=120}And before I could report it,{/cps}{nw=0.01}"
    ina "{cps=120}I got sent off on another task!{/cps}{nw=0.01}"
    ina "{cps=120}And then—{/cps}{nw=0.01}"

    show intan surprised at jumping
    with vpunch
    ina "Ah! You lost your way here?!"

    adh "Wait, wait, wait! Slow down."

    show intan troubled at jumping
    ina "Y-yes! I'm sorry!"

    adh "... Okay, so, what you're saying is, you miscounted me back at the parking lot."
    adh "And that's why I was left behind?"

    show intan cry at nodding
    ina "Yes... That's correct..."

    adh "I see..."

    sp_mn "Eka had already pointed out the mistake."
    sp_mn "So, I'm not too surprised."
    sp_mn "But still, to meet the troublemaker this soon is... unexpected."

    show intan blush
    ina "Are you... mad?"

    sp_mn "Well, I can't really say she's the only one at fault..."
    sp_mn "Not with those puppy eyes."

    adh "Well, not really. I don't really care enough to be mad."
    adh "It's not like I knew anyone from that convoy either."
    adh "Besides, it was my mistake for oversleeping."

    show intan processing
    ina "O-oh..."

    show intan curious
    ina "Then how about your registration?"

    adh "Oh, yeah. That's right. I forgot about that..."
    adh "I dunno, maybe I just need to wait until tomorrow."

    show intan troubled
    ina "Then do you have a place to sleep?"

    show intan concerned
    ina "We do provide room for most of out-of-town recruits."
    ina "But, we can't exactly do that if you're unregistered."

    adh "That's—"

    show intan direct
    with None
    ina "{cps=120}Oh, I know! I'll try to talk to the refugee area.{/cps}{nw=0.01}"
    ina "{cps=120}They should have some place left for you to stay.{/cps}{nw=0.01}"

    show intan determined
    with None
    ina "{cps=120}It might not be much, but it's better than sleeping on the street.{/cps}{nw=0.01}"
    
    show intan surprised
    with None
    ina "{cps=120}What am I saying, you need to eat!{/cps}{nw=0.01}"

    show intan flustered
    with None
    ina "{cps=120}The journey must be tough, and to think you haven't eaten anything.{/cps}{nw=0.01}"

    show intan flustered at jumping
    with None
    ina "{cps=120}You must be starving!{/cps}{nw=0.01}"

    show intan curious
    with None
    ina "{cps=120}Have they prepared the batch for tonight, I wonder.{/cps}{nw=0.01}"

    show intan troubled
    with None
    ina "{cps=120}Ah, no. Eka would be there at this hour.{/cps}{nw=0.01}"
    ina "{cps=120}I'm still not ready to talk with her yet...{/cps}{nw=0.01}"

    show intan cry
    with None
    ina "{cps=120}Wait, what am I saying, I should report this to Eka!{/cps}{nw=0.01}"

    show intan curious at jumping
    with None
    ina "{cps=120}Oh! You didn't happen to meet Eka, right?{/cps}{nw=0.01}"

    show intan troubled
    with None
    ina "{cps=120}Did she yell at you? Did she mention anything about me?{/cps}{nw=0.01}"

    show intan flustered
    with None
    ina "{cps=120}She's gonna kill me at this point.{/cps}{nw=0.01}"

    show intan cry
    with None
    ina "{cps=120}I starve an actual TNI soldier!{/cps}{nw=0.01}"

    show intan happy
    ina "{cps=120}Well, that's gotta be an achievement, right? Ha ha, ha ha ha!{/cps}{nw=0.01}"

    adh "Hold on! Calm down." with hpunch

    show intan flustered at jumping
    ina "Eeek!"

    sp_mn "Arrgh... I didn't expect her to scream there."

    adh "Come on, deep breath. Everything is fine."

    show intan blush
    ina "R-right..."

    show intan blush at sighing
    
    pause 3.0

    show intan pout
    ina "... I've calmed down..."

    play music music.playful_intan

    adh "Good... Now, let me tell you something."

    adh "Eka already knows. I already talked to her."

    show intan flustered
    ina "S-she does?"
    ina "Did she say anything about me?"

    adh "No, nothing like that. She just said there were some complications with the headcount."
    adh "And it turned out okay for me and for her, no, for KPR."

    show intan surprised
    ina "H-huh..?"

    adh "Though, it's a a bit too soon to say she doesn't have anything to say to you though."
    adh "And, to make you feel a bit better. Eka has already taken care of my needs, you don't need to be worried."


    show intan surprised
    ina "Oh... That's good."

    show intan flustered
    ina "But I'm still not safe, am I?"

    adh "Yeah... All I can say is good luck."

    show intan cry
    ina "T-thanks, I'm going to need that..."

    show intan blush
    ina "Also, I'm really sorry it turned out like this..."

    adh "Hey, I already said I'm not mad. So it's fine."

    show intan surprised
    ina "Huh..."
    
    show intan determined
    ina "T-then, please don't hesitate to ask me if you need anything, okay? I owe you at least that much."

    adh "Sure..."

    show intan surprised
    ina "Oh, that's my phone ringing."

    hide intan
    with meddis

    sp_mn "..."
    sp_mn "She's a pretty hardworking person here."
    sp_mn "I wonder how much she can actually do."
    sp_mn "From what I can see, she can be quite clumsy."
    sp_mn "And pretty awkward around people too, but she's not exactly struggling either."
    sp_mn "I guess KPR influenced her somehow, even though I'm not too sure if she's always like this."

    show intan determined
    with meddis
    ina "Ugh... I gotta go. Another duty call."

    show intan smile
    ina "Thank you very much, Corporal Andhra."

    show intan soune
    ina "And, uh, sorry again."

    adh "Of course. See you next time, Intan."

    show intan blush at moveoutleft

    stop music fadeout 5.0
    play ambiance night fadein 5.0
    
    sp_mn "... And there she goes."
    hide intan
    sp_mn "At least she didn't go out suddenly, like that other person did."

    play sound explosion
    eka "Who were you talking to, Andhra?" with vpunch

    scene base kpr main night
    show eka curious
    with fastfade

    adh "Oh... It's just you, Eka."

    sp_mn "That scared the hell out of me, EKA!"

    show eka smile
    eka "I've got you your room key here."
    eka "Come, I'll show you the way."

    adh "Huh?"
    adh "Didn't think the leader of KPR would offered me a personal escort."

    show eka embarassed
    eka "Don't get the wrong idea, I'm heading to the dorms anyway."

    show eka smug
    eka "Knowing your history, you'd end up lost at the refugee camp."

    adh "Very funny..."

    show eka serious
    eka "Anyway, the dorm keeper needs a headcount update."

    show eka determined
    eka "As you know, we had a wave of recruits coming in, and we need to see how many rooms we've got left."

    adh "Huh..."
    adh "So, was my room just happened to be marked by you or something?"
    adh "How do you know it's vacant?"

    show eka curious
    eka "Hmm..."
    eka "You'll see."
    
    adh "Please stop keeping things off of me."

    show eka happy
    eka "No. Consider this as your punishment."

    show eka talking right
    eka "Oh, you're the first member to get a punishment before you even registered."

    show eka smug
    eka "That's gotta be a record, right?"

    adh "..."
    adh "Please, let's just go."

    show eka happy
    eka "Ahaha~"

    scene black
    with medfade

    stop ambiance

    return

label scene_1_8:
    
    sp_adh "We walked through the night, leaving the office as the glow faded behind us."
    sp_adh "We got to the dorm as the light was coming into view."
    sp_adh "The area had a more structured look with fewer tents around them compared to the main base."
    sp_adh "It seemed like a private complex more than anything. Even though we were supposed to be at the edge of the forest."
    sp_adh "One of the buildings seemed more like an apartment reaching five floors."
    sp_adh "We entered the building, the inside was well lit. There were a couple of staff at the first floor."
    sp_adh "Eka waved her hand on them, before gesturing to me, They nodded and we walked to the upper floors"

    scene apartment corridor night
    show eka explain
    with medfade

    play music music.night

    eka "Alright, here's your room."
    eka "You're lucky we had space. Some other recruits had to cram four to a room."

    sp_adh "We stopped in front of a room. there was a bunch of stuff in front of the room."
    sp_adh "But junk would be more appropriate to describe."
    sp_adh "Some random parts, empty cans and pair of boots are tidied in front of the room."
    sp_adh "It didn't really make it less messy, though. All of them have seen better days."
    sp_adh "And the window next to the door is so grimy, it barely lets in any light."

    adh "This... Doesn't look vacant."

    sp_mn "It's as if someone has been living here for years..."

    show eka curious
    eka "That's because it's not."

    show eka smile
    eka "You've got a roommate."
    eka "He's hardly ever here, though. So you'll probably have the place to yourself most of the time."

    sp_mn "A roommate, huh..."
    sp_mn "It's not unusual, I rarely have any room to myself either in the military... But..."

    adh "Doesn't seem he's ever here to clean either..."
    
    show eka talking right
    eka "Yeah, he basically just uses his room as a storage space than an actual room."

    show eka smile
    eka "Oh, but your side of the room should've been cleared out."
    eka "At least you won't be sleeping on a pile of spare parts or whatever he's got stashed in here."

    sp_adh "Eka said as she opens the door, viewing it from outside."

    scene room andhra
    with medfade

    sp_adh "Inside, the room was pretty much split down the middle."
    sp_adh "One side was messy, full of toolboxes, loose wires, random spare parts and old blurprints,"
    sp_adh "The other side was noticeably emptier, just a simple cot with folded blankets and a small locker besides it."
    sp_adh "There's also an empty desk just right beside the window. A single key was placed on top of the desk."
    
    show eka smile
    eka "See? It's still meant for two people, and your side have been cleared up."

    show eka talking left
    eka "I won't be able to do anything about the oil stench though, but I'll tell him to take care of it tomorrow."

    show eka disappointed
    eka "Until then, you can't complain."

    adh "Well... I'm not complaining or anything..."
    adh "But, is my roommate know about this?"

    show eka curious
    eka "..."

    show eka happy
    eka "Anyway, take a good rest, Corporal. Try not to get lost again."

    show eka surprised
    eka "Oh, and don't forget to sign up tomorrow!"

    show eka talking right
    eka "See you tomorrow!"

    show eka talking right at moveoutleft
    
    adh "Hey!" with vpunch

    hide eka

    adh "..."
    sp_mn "... Am I really gonna be okay living here...?"
    sp_mn "Oh well, when the time comes, I'll try to explain things to him..."
    sp_mn "I'm pretty sure Eka knows what she's doing, I hope whoever my roommate is, I won't at least be chewed by him."

    sp_mn "*Ring Ring*"

    sp_mn "Oh, that's my phone."
    sp_mn "Who could be calling this late in the night..."

    sp_adh "I looked at my phone to see who was calling."
    sp_adh "It was Setya. I forgot we promised to contact each other if we had got time."
    sp_adh "I immediately picked it up."

    adh "Uh, what's up, Setya?"

    sty "Good, you're still alive."

    adh "... Well, glad you're alive too."

    sty "How's your first day in KPR?"

    adh "Well—"

    stop music

    scene room andhra
    with fastfade

    play music music.strategize

    sty "I see... Not a lucky day for you, isn't it?"

    adh "Honestly, yeah. It's pretty unlucky"

    adh "But I'm glad to meet the leader right away though."

    sty "Yeah... I really didn't expect them to be so young though."
    sty "Do you think she has some kind of experience?"

    adh "Hmm... I think so."
    adh "Despite her demeanor, she seems like she has lead some kind of group before."
    adh "She could be a former TNI and I wouldn't be surprised."

    sty "Woah... really?"
    
    adh "I don't know, I could be mistaken. But it's certainly a possibility."

    sty "I can certainly say that she's a good commander, or rather leader."

    sty "You'll have to fill me in more later. Anyway, I called to update you on what's happening over here."

    adh "Something's up?"

    sty "We've prepared for the next coming of the refugees and TNI soldiers."
    sty "Bad news is: it's not gonna be enough."
    sty "I heard that KPR would help too, any news about that?"

    adh "Nothing like that. It's probably going to be the branch."

    sty "Oh, right. There was one in Bekasi, right?"
    sty "I'm still not sure if that's enough though."
    sty "But we don't have any other choice right now."

    adh "How about the TNI?"

    sty "The TNI bases in Jakarta are stretched thin. Some units have been reassigned to handle it, but we're running out of space."
    sty "And worse, the people are getting angry now."

    adh "Angry?"

    sty "Yeah, we've got protests outside the government buildings."
    sty "They're blaming the government for not doing enough for the refugees."
    sty "And many others were thinking we should focus on defending Java or take back Kalimantan."
    
    adh "So both sides are angry, huh..."

    sty "If things keep going like this, we're going to lose to the public first before China gets another chance to attack us."

    adh "Sigh... Do you think things will be okay?"

    sty "I'm not so sure. All we can do is to hope the higher-ups can handle this."
    sty "That's all I needed to update you."

    adh "Guess things are just going to spiral down as you go forward."

    sty "Well, at least KPR are doing okay at your side."

    adh "Don't jinx it."

    sty "Haha, sure."
    sty "Anyway, I gotta go. You take a rest. I'm sure this will be the first time you sleep on a matress after so a while."

    adh "Sure is, see you around, Setya."

    stop music

    sp_mn "..."
    sp_mn "Sigh, we're not getting any good news..."

    scene room andhra
    with fastfade

    sp_mn "A lot is happening today, and it's not getting any better."
    sp_mn "Sure hope tommorows will be better..."

    sp_mn "......"
    sp_mn "..."

    scene black
    with medfade

    return

label scene_1_9:

    sp_mn "..."
