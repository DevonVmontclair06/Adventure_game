def scenario_1():
    options = ['1a','1b']
    print('You wake up to find yourself in a cold, dark cave.')
    print('The air is damp, and the faint echo of dripping water fills your ears.')
    print('You have no memory of how you got here.')
    print('As you get up and dust yourself off, you notice two paths ahead:')
    print()
    print('1a:')
    print('To your left, a narrow tunnel leads deeper into darkness')
    print('The air is colder there, and you can faintly hear the sound of rushing water.')
    print()
    print('1b:')
    print('To your right, a wider passage seems to have some light coming from it.')
    print('The source of the light is unclear, but you hear distant whispers echoing from within.')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 1a or 1b')
        user_input = input().strip()
        if user_input == '1a':
            scenario_2()
        elif user_input == '1b':
            scenario_5()
        else:
            print('Invalid answer')

def scenario_2():
    options = ['2a','2b']
    print('As you tugs on towards the source of the sound, the wall around you begins to feel slimy. ')
    print('Droplets of water steadily bang your head as you traverse through the ankle deep water that surrounds you.')
    print('Near impossible to see, you feel the walls for comfort and are supposed to brush by a door handle.')
    print('There is a faint odor coming from the door.')
    print()
    print('2a:')
    print('You can enter the doorway. Its door is covered in mold and grime. You can feel the metal peeling at the slightest touch.')
    print('A sign is posted onto the door with words you cannot understand.')
    print('In the low visibility, the only thing that stands out is the red plastered on it in the form of an x.')
    print()
    print('2b:')
    print('You can continue tracking down the dark, wet corridor.')
    print('The noises echo through the chamber, beckoning you forward.')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 2a or 2b')
        user_input = input().strip()
        if user_input == '2a':
            scenario_3()
        elif user_input == '2b':
            print(end_a)
        else:
            print('Invalid answer')
end_a = [
    'As you venture further into the cave, the water slowly begins to rise. '
    'Now, you were half submerged in the water, barely trudging forward. '
    'As you wander, the sound grows louder and louder. '
    'The water begins to push more forcefully at your legs. '
    'Before you can realize the danger, you are swept off your feet by a powerful current. '
    'Struggling to get air, you flair your arms in desperation as the sound of a waterfall grows near. '
    'Within moments, you are dragged through the waterfall, plummeting to your death.'
]

def scenario_3():
    options = ['3a','3b']
    print('Deciding not to be drenched in water, you pull the handle down and enter the slimy door.')
    print('The room is pitch-black with a foul odor coming from all directions.')
    print('You remember the smell of diesel.')
    print('Embracing the darkness, you move your hands across the room to find a box of matches, dry compared to the moldy table you found them in.')
    print()
    print('3a:')
    print('Light the boxes of matches to get a better understanding of where you are')
    print()
    print('3b:')
    print('Continue searching blindly in the dark in hopes of finding something to get you out')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 3a or 3b')
        user_input = input().strip()
        if user_input == '3b':
            scenario_4()
        elif user_input == '3a':
            print(end_b)
        else:
            print('Invalid answer')
end_b = [
    'As darkness surrounds you, fear begins to set in. '
   'In desperation you finger your way through the matches, grabbing one and striking it against the box. '
   'Suddenly there is a small light emanating from the match. '
   'Then, the whole room glows brightly. '
   'Before you have time to react, your body is turned into ash as the room combusts into itself.'
]

def scenario_4():
    options = ['4a','4b']
    print('Not wanting to ignite the mysterious gas, you decide to drop the matches and finger your way through the room.')
    print('On all fours, you rummage through the floor, hoping to find something of value.')
    print('At last, you discover a ladder sticking out from the floor.')
    print('The ladder is beyond rusted, with the metal peeling as you brush your hand on it.')
    print()
    print('4a:')
    print('Assed the ladder')
    print()
    print('4b:')
    print('Descend the ladder')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 4a or 4b')
        user_input = input().strip()
        if user_input == '4a':
            print(end_c)
        elif user_input == '4b':
            print(end_d)
        else:
            print('Invalid answer')
end_c = [
    'In desperation, you climb the ladder, hoping for a way out. '
    'As you ascend the wall around you disappears as if you are in an abyss. '
    'As you climb, you begin to see a faint light emanating from the top. '
    'The mere sight of light boosts your mind to reach out and grab it. '
    'With new-found courage you ascend faster, not remembering the state it was in. '
    'With each step, the metal growls until it gives way, plummeting yourself to your death.'
]
end_d = [
    'Believing the light to be a trick, you decide to descend further and farther down the ladder. '
    'For what seems like an eternity, you climb further and further down, embracing the darkness below you. '
    'After a long descent, you reach the bottom, your feet echoing as you reach the cavern below. '
    'Before you have time to take in the surroundings, you hear something behind you, a low growl. '
    'Frightened, you try to grab the ladder and head up. Before you can, something bites your head. '
    'As you scream, the beast snaps your jaw, decapitating you in mere seconds of spotting you.'
]

def scenario_5():
    options = ['5a','5b']
    print('Following the beckoning light, you creep your way through the corridor.')
    print('The once black walls come alive with detail as the light reflects off of their shiny surface.')
    print('You make out that the walls seem not natural, as each layer is stacked on top of one another.')
    print('As the whispers grow louder, you see a split in the walls leading to another source of light.')
    print('This pathway seems more crudely made compared to the sophistication of the forward path.')
    print()
    print('5a:')
    print('Follow the path you are originally on in the direction of the whispers')
    print()
    print('5b:')
    print('Follow the new source of light in hopes it will lead you out')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 5a or 5b')
        user_input = input().strip()
        if user_input == '5a':
            scenario_6()
        elif user_input == '5b':
            scenario_7()
        else:
            print('Invalid answer')

def scenario_6():
    options = ['6a','6b']
    print('Deciding to continue where you were going, you walk closer and closer to the source of the noise, hoping to see a friendly face.')
    print('As you turn the corner, you see two large creatures conversing with each other.')
    print('Their bodies stretch out twice the size of you.')
    print('Their arms contain various equipment you have never seen before.')
    print('Suddenly, the creatures both look at you, confused and awed by your arrival.')
    print('One of them readies their weapon.')
    print()
    print('6a:')
    print('Fight the creatures')
    print()
    print('6b:')
    print('Flee the creatures')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 6a or 6b')
        user_input = input().strip()
        if user_input == '6a':
            print(end_e)
        elif user_input == '6b':
            print(end_f)
        else:
            print('Invalid answer')
end_e = [
    'Hoping to take them on by surprise, you charge the one closest to you, knocking them onto the ground with ease. '
    'You grab the weapon he was holding and swiftly allow a blow to the head of the first creature. '
    'Alarmed, the second moves to strike you down. '
    'You swiftly move out of the way, your mind and body moving in unison. '
    'Before you can react, however, the creature on the ground tackles you to the floor. '
    'Within moments, both creatures are on top of you, tearing you apart as you helplessly fight back.'
]
end_f = [
    'Not wanting to get into a fight you are un-equipt to do so, you slowly walk backwards, eyes focused on the creatures. '
    'Both creatures look at you for a moment before darting towards you with extreme speed. '
    'You quickly turn around and sprint further into the cave with both creatures pursuing you. '
    'The light that one illuminated the walls slowly faded away, returning you to the pitch black that you started off with. '
    'The cave becomes so dark that you run face-first into a ditch, falling to your death.'
]

def scenario_7():
    options = ['7a','7b']
    print('Fearing what those whispers were coming from, you seek out the new set of light from the corridor.')
    print('The once man-made walls are replaced with slimy rock and granite.')
    print('The surface becomes squishy to touch as the ground benefits you and becomes more and more slimy')
    print('Overcoming the disgusting feeling, you venture further into the corridor, before coming to a crossroad.')
    print('The left path is pitch black with the only light coming from an unknown source.')
    print('The right leads to the glowing light that first brought you into the corridor in the first place.')
    print()
    print('7a:')
    print('Take the left path')
    print()
    print('7b:')
    print('Take the right path')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 7a or 7b')
        user_input = input().strip()
        if user_input == '7a':
            print(end_g)
        elif user_input == '7b':
            scenario_8()
        else:
            print('Invalid answer')
end_g = [
    'As you journey through the darkness, the wall slowly comes alive in an array of colors. '
    'Crystals begin to glow as if welcoming your presence. Feelings of joy and happiness wash over you as you begin to pay less and less attention to the walls as you walk. '
    'In your trance, to neglect to see the put that you are walking towards. '
    'Before you can react, you slip into the void below, never to be seen again.'
]

def scenario_8():
    options = ['8a','8b']
    print('Following the glow, you walk closer and closer to the source.')
    print('The once cold and damp room slowly becomes dry and warm.')
    print('Feelings of excitement begin to wash over you as you run closer to the light, grabbing it as you go.')
    print('Suddenly, you see where it is coming from.')
    print('A hole in the ceiling creates an almost blinding light that hurts to look at. However, the hole is just out of reach for you to reach it.')
    print('As you scan the room it is contained in, you see two objects, a rusted ladder and a rope with a grapple attached to it.')
    print()
    print('8a:')
    print('Use the ladder.')
    print('It appears to be very rusted and shakes when stepped on.')
    print()
    print('8b:')
    print('Use the rope.')
    print('It is very old and is wearing down, but sturdy.')
    print()
    user_input = ''
    while user_input not in options:
        print('Choose between 8a or 8b')
        user_input = input().strip()
        if user_input == '8a':
            print(end_h)
        elif user_input == '8b':
            print(end_i)
            print()
            print('Congratulations on successfully completing My Adverturn Game!')
        else:
            print('Invalid answer')
end_h = [
    'As you line up the ladder with the hole, shavings of iron corrode off of its side. '
    'The paint is long gone, replaced with an orange, brown tint. '
    'Stepping on the ladder, it grows in protest. '
    'Each step closer brings the ladder closer to breaking. '
    'All you can see is light as you slowly make your way towards the hole. '
    'Your heart beats harder and harder as you reach out to grab the surface. '
    'Unbenoused to you, the ladder is at its final end. '
    'Quickly, the ladder collapses in on itself, plummeting you towards the ground. '
    'Your last thoughts before hitting the rocks below you are of the light, taunting your decent.'
]
end_i = [
    'Grabbing the rope, you throw the grapple part at the hole. '
    'The grapple flies through the hole and gets stuck on an unknown source. '
    'Pulling the rope, you began to climb. As you do so, the light becomes blinding. '
    'Your muscles ache as you pull your weary body closer to the hole. '
    'Each pull brings you closer to salvation. '
    'Finally, you reach the hole. '
    'With one final push, you land on solid ground. '
    'The warmth of the grass on your pale body envelops you as you breathe a sigh of relief. '
    'You are free. '
]

def main():
    while True:
        print('Welcome to the Adventure game run in python.')
        print('Read the story and choose the right path in order to escape your predicament!')
        print()
        scenario_1()
        break

if __name__=="__main__":
    main()
