def scenario_1():
    options = ['1a','1b']
    print('You wake up to find yourself in a cold, dark cave.')
    print('The air is damp, and the faint echo of dripping water fills your ears.')
    print('You have no memory of how you got here.')
    print('As you get up and dust yourself off, you notice two paths ahead:')
    print('1a:')
    print('To your left, a narrow tunnel leads deeper into darkness')
    print('The air is colder there, and you can faintly hear the sound of rushing water.')
    print('1b:')
    print('To your right, a wider passage seems to have some light coming from it.')
    print('The source of the light is unclear, but you hear distant whispers echoing from within.')
    user_input = ''
    while user_input not in options:
        print('Choose between 1a or 1b')
        user_input = input().strip()
        if user_input == '1a':
            print('1')
        elif user_input == '1b':
            print('5')
        elif user_input == None:
            print('a')
        else:
            print('Invalid answer')


def main():
    while True:
        print('Welcome to the Adventure game run in python.')
        print('Read the story and choose the right path in order to escape your predicament!')
        scenario_1()
        break

if __name__=="__main__":
    main()
