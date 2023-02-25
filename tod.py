#!/usr/bin/python3
"""A function that selects between truth or dare"""
import argparse
from random import choice


dare_list = [
    'Give a lap dance to the person sitting next to you',
    'Remove an item of clothing and wear it for the rest of the game',
    'Do 10 push-ups while someone sits on your back',
    'Kiss the person sitting to your left on the lips',
    'Drink a shot of alcohol from the belly button of the'
    ' person sitting across from you',
    'Send a naughty text to your crush',
    'Let someone draw a temporary tattoo on your lower back',
    'Make out with the person who brought you to the party',
    'Take a shower with someone of the opposite sex',
    'Seduce the person to your right for 1 minute',
    'Do a strip tease for the group',
    'Wear your underwear on your head for the rest of the game',
    'Swap clothes with someone of the opposite sex for 10 minutes',
    'Give a sensual massage to the person sitting next to you',
    'Do a body shot off of someone',
    'Give a hickey to the person you find most attractive in the room',
    'Spend 5 minutes in a closet with the person of your choice'
    ]

truth_list = [
    'Have you ever kissed someone of the same sex?',
    'What is the most daring sexual experience you\'ve had?',
    'What is your favorite position?',
    'Have you ever had a one night stand?',
    'What is the most embarrassing thing that has'
    ' ever happened to you during sex?',
    'What is your biggest turn-on?',
    'Have you ever fantasized about someone in this room?',
    'What is the wildest thing you have ever done in bed?',
    'What is the kinkiest thing you have ever done?',
    'What is the most unusual place you have had sex?',
    'Have you ever cheated on a partner?',
    'What is the craziest sexual thing you have ever done?',
    'What is the sexiest outfit you own?',
    'What is the most sensitive part of your body?',
    'Have you ever had sex in public?',
    'What is your favorite type of porn?',
    'What is your biggest sexual fear?'
    ]
previous_dares = []
previous_truths = []
punishment_given = False


def consequence():
    """
    collects and returns repurcursion for failing
    to play
    """
    global punishment_given
    global punishment
    if not punishment_given:
        punishment = input("Enter the Punishment:")
        punishment_given = True
        return punishment
    else:
        return ''


def YourDare():
    dare = choice(dare_list)
    if dare in previous_dares:
        YourDare()
    else:
        previous_dares.append(dare)
        print(f"{dare}\nOr\n{punishment}")


def YourTruth():
    truth = choice(truth_list)
    if truth in previous_truths:
        YourTruth
    else:
        previous_truths.append(truth)
        print(f"{truth}\nOr\n{punishment}")


def main():
    parser = argparse.ArgumentParser(description='Play truth or dare')
    parser.add_argument('play', help='choose truth or dare')
    args = parser.parse_args()
    while True:
        consequence()
        args.option = input("Choose Truth or Dare:").lower()
        
        if args.option == 'truth':
            YourTruth()
        elif args.option == 'dare':
            YourDare()
        else:
            print("Invalid choice. Choose between 'truth' or 'dare'")

        print("Would you like to play again? (y/n)")
        play_again = input().lower()

        if play_again != 'y':
            break


if __name__ == '__main__':
    main()
