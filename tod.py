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
    'Spend 5 minutes in a closet with the person of your choice',
    'Give someone in the room a sensual lap dance.',
    'Kiss the person on your left passionately.',
    'Remove an article of clothing and wear it in a provocative way.',
    'Send a flirty or provocative text to someone you\'re attracted to.',
    'Give a detailed description of your last sexual encounter.',
    'Use an ice cube to tease and pleasure a volunteer.',
    'Create an erotic story or poem and share it with the group.',
    'Share your best seductive pick-up line.',
    'Role-play a steamy scene with another player.',
    'Blindfold one person and let them guess who\'s kissing them.',
    'Perform a sensual striptease for the group.',
    'Share a naughty photo (with your consent and within legal boundaries) with someone you trust.'
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
    'What is your biggest sexual fear?',
    'Have you ever had a one-night stand? Share the details.',
    'What\'s the most adventurous place you\'ve had sex?',
    'Describe your favorite sexual fantasy.',
    'Have you ever used a sex toy? Which one is your favorite?',
    'What\'s the kinkiest thing you\'ve ever done in the bedroom?',
    'Have you ever watched or read adult content in a public place?',
    'Share your most embarrassing sexual moment.',
    'Who is your celebrity crush, and what would you do if you met them?',
    'Have you ever had a threesome? Share the experience.',
    'What\'s your secret turn-on that most people wouldn\'t expect?',
    'Share your wildest and most unforgettable sexual experience.',
    'Have you ever had a romantic or sexual encounter with someone of the same gender?'
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
