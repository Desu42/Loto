import random
import datetime

def menu():

    print('\n1. alege jocul: 6/49 sau 5/40')
    print('2. cumpara bilet (alegere numere)')
    print('3. extragere numere (generare numere )')
    print('4. rezultat')
    print('5. exit\n')

def chose_game():
    '''
    Choses the game to play. 
    '''
    try:

        game = int(input('\n6 for 6/49 \n5 for 5/40\n\nChoice = '))

    except ValueError:

        print('Error.')
        return 

    if game not in [5, 6]:

        print('Not a valid option. Try again.')
        chose_game()


    return game

def chose_numbers(game):
    '''
    generates a list of the user input
    6 or 5 numbers depending on game
    '''
    ticket = [int(x) for x in input('Chose numbers: ').split()]

    if len(ticket) != game:

        print('Error. Try again.')
        chose_numbers(game)

    return ticket

def generate_winner_ticket(game, ticket):
    '''
    generates a list of random numbers
    '''
    d = datetime.datetime.today()
    i = random.randint(0,9)
    #better odds
    if d.day == 13 and d.weekday() == 4 and i == 7:

        winner_ticket = ticket

    elif game == 5:

        winner_ticket = random.sample(range(41), 5)

    elif game == 6:

        winner_ticket = random.sample(range(50), 6)

    return winner_ticket

def check_if_winner(ticket, winner_ticket):

    copie_ticket = ticket
    copie_winner = winner_ticket

    copie_ticket.sort()
    copie_winner.sort()

    if copie_ticket != copie_winner:
        return False

    return True

def UI():

    menu()
    while True:

        try:

            option = int(input('\nChose option: '))

        except ValueError:

            print('\nError.')
            continue

        if option == 1:

            games = {5:'5/40', 6:'6/49'}
            game = chose_game()
            print('You chose {}.'.format(games[game]))

        elif option == 2 :

            ticket = chose_numbers(game)
            print('You bought a ticket! ')

        elif option == 3:

            winner_ticket = generate_winner_ticket(game, ticket)
            print('The numbers were drawn! Check to see if you won!')

        elif option == 4:

            winner = check_if_winner(ticket, winner_ticket)

            if winner:

                print('Over an infinite amount of time, anything that can happend will happen.')
                print('What are the odds of a monkey writing Hamlet on a typewriter?')
                print('But what about an infinite number of monkeys over an infinite amount of time?')
                print('I digress.')
                print('...')
                print('Congrats! You won 1 billion dollars.')
                print('Your ticket was: ', end = ' ')
                print(winner_ticket)

            elif not winner:
                
                print("You're more likely to become a billionaire than win the lottery.")
                print('Huh? What? ')
                print("Of course you didn't win.")
                print('Your ticket was: ', end = ' ')
                print(ticket)
                print('Winner ticket is: ', end = ' ')
                print(winner_ticket)

        elif option == 5:

            exit(0)

        else:

            print('Not a valid option.')
            continue

UI()