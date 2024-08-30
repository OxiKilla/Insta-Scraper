import instaloader
import time
import getpass
import sys
import random
import signal
import os
from colorama import init, Fore
from instagrapi import Client  # Import instagrapi

init(autoreset=True)

def print_colored_ascii_art():
    ascii_art = f"""
{Fore.YELLOW}

 ,adPPYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYba,  8b,dPPYba,  
a8P_____88 88P'   "Y8 88P'   "Y8 a8"     "8a 88P'   "Y8  
8PP"'''''' 88         88         8b       d8 88          
"8b,   ,aa 88         88         "8a,   ,a8" 88          
 `"Ybbd8"' 88         88          `"YbbdP"'  88          

                Instagram Scraper
                made by @OxiKilla         
    """
    print(ascii_art)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_loading(message):
    colors = [Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.WHITE, Fore.LIGHTBLACK_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]
    sys.stdout.write(message)
    sys.stdout.flush()
    for _ in range(3):  # Adds a dot animation
        for color in colors:
            sys.stdout.write(f"\r{color}{message}{'.' * _}")
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write("\r")
    sys.stdout.flush()

def print_message_with_effect(message, delay=0.3):
    for i in message:
        print(f"{Fore.GREEN}{i}", end='', flush=True)  # Print each letter on the same line
        time.sleep(delay)  # Delay between letters
    print()

def random_delay(min_delay=0.2, max_delay=2):
    time.sleep(random.uniform(min_delay, max_delay))

def print_exit_message(signum, frame):
    """Handle Ctrl+C interruption and print exit message."""
    exit_message = f"""
    
    {Fore.RED}

⠀⠀⠀⢀⡤⢤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⡅⠠⢀⡈⢀⣙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⠈⠙⠿⣝⢇⠀⠀⣀⣠⠤⠤⠤⣤⡤⠚⠁⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡀⠀⠀⠠⣄⠈⢺⣺⡍⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡆⢀⠘⣔⠄⠑⠂⠈⠀⡔⠤⠴⠚⡁⠀⠀⢀⠀⠀⠀⣠⠔⢶⡢⡀⠀⠠⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣇⠀⢃⡀⠁⠀⠀⠀⡸⠃⢀⡴⠊⢀⠀⠀⠈⢂⡤⠚⠁⠀⠀⠙⢿⠀⠉⡇⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠾⣹⢤⢼⡆⠀⠀⠀⠀⠀⠀⠈⢀⠞⠁⠀⢠⣴⠏⠀⠀⠀⠀⠀⠀⠸⡄⠀⢇⠀⠀⠀⠀⠀
⠀⠀⣾⢡⣤⡈⠣⡀⠙⠒⠀⠀⠀⠀⣀⠤⠤⣤⠤⣌⠁⢛⡄⠀⠀⠀⠀⠀⠠⡀⢇⠀⠘⣆⠀⢀⡴⡆
⠀⠀⣿⢻⣿⣿⣄⡸⠀⡆⠀⠒⣈⣩⣉⣉⡈⠉⠉⠢⣉⠉⠀⠀⠀⠀⠀⠀⠀⢣⠈⠢⣀⠈⠉⢁⡴⠃
⠀⢀⢿⣿⣿⡿⠛⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣸⢿⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⡇⠉⠉⠁⠀⠀  
⣠⣞⠘⢛⡛⢻⣷⣤⡀⠈⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠇⢰⡇⠀⠀⠀⠀⠀
⠻⣌⠯⡁⢠⣸⣿⣿⣷⡄⠁⠈⢻⢿⣿⣿⣿⣿⠿⠋⠃⠰⣀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀      BYE !
⠀⠀⠉⢻⠨⠟⠹⢿⣿⢣⠀⠀⢨⡧⣌⠉⠁⣀⠴⠊⠑⠀⡸⠛⠀⠀⠀⠀⠀⣸⢲⡟⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠏⠀⠀⠀⠉⠉⠁⠀⠐⠁⠀⠀⢉⣉⠁⠀⠀⢀⠔⢷⣄⠀⠀⠀⠀⢠⣻⡞⠀⠀⠀⠀⠀⠀⠀          
⠀⢠⠟⡦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢾⠉⠀⣹⣦⠤⣿⣿⡟⠁⠀⠀⠀⢀⣶⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⣦⣁⡎⢈⠏⢱⠚⢲⠔⢲⠲⡖⠖⣦⣿⡟⠀⣿⡿⠁⣠⢔⡤⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣟⠿⡿⠿⠶⢾⠶⠾⠶⠾⠞⢻⠋⠏⣸⠁⠀⡽⠓⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡏⠳⠷⠴⠣⠜⠢⠜⠓⠛⠊⠀⢀⡴⠣⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣏⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⢀⣀⣀⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠖⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠑⠒⠒⠐⠒⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      
    """
    print(exit_message)
    sys.exit(0)

def show_menu():
    clear_screen()  # Clear the screen before showing the menu
    print(f"""
{Fore.YELLOW}

88,dPYba,,adPYba,   ,adPPYba, 8b,dPPYba,  88       88  
88P'   "88"    "8a a8P_____88 88P'   `"8a 88       88  
88      88      88 8PP''''''' 88       88 88       88  
88      88      88 "8b,   ,aa 88       88 "8a,   ,a88  
88      88      88  `"Ybbd8"' 88       88  `"YbbdP'Y8  
                                                        
    """)
    print(f"{Fore.CYAN}1) Show users who don't follow back")
    print(f"{Fore.CYAN}2) Automatic unfollow (risky)")
    print(f"{Fore.CYAN}3) Exit")

def handle_menu_choice(choice, profile, client):
    if choice == '1':
        display_loading("Fetching profile data...")
        try:
            # Retrieve followers and followings
            followers = set(profile.get_followers())
            followings = set(profile.get_followees())

            # Determine who follows you back
            followers_usernames = set(follower.username for follower in followers)
            followings_usernames = set(following.username for following in followings)

            # Find who you follow but don't follow you back
            non_follow_back = followings_usernames - followers_usernames

            # Print results
            print(f"\n{Fore.RED}💀 Users you follow but who don't follow you back:")
            for user in non_follow_back:
                print(f"\t{Fore.RED}{user}")
                random_delay(0.5)  # Random delay between printing users

            print(f"{Fore.GREEN}Data fetching completed!")
        
        except Exception as e:
            print(f"Error during data fetching: {e}")
    elif choice == '2':
        if not client:
            print(f"{Fore.RED}Client not initialized. Cannot perform unfollow.")
            return
        
        display_loading("Fetching profile data for unfollow...")
        try:
            # Retrieve followings
            followings = set(profile.get_followees())
            followers = set(profile.get_followers())
            followers_usernames = set(follower.username for follower in followers)
            followings_usernames = set(following.username for following in followings)

            # Find who you follow but don't follow you back
            non_follow_back = followings_usernames - followers_usernames

            # Unfollow users who don't follow you back
            for user in non_follow_back:
                client.user_unfollow(client.user_id_from_username(user))
                print(f"{Fore.RED}Unfollowed: {user}")
                random_delay(5, 15)  # Random delay between unfollows

            print(f"{Fore.GREEN}Unfollowing process completed!")
        
        except Exception as e:
            print(f"Error during unfollowing: {e}")
    elif choice == '3':
        print_exit_message(None, None)  # Exit gracefully
    else:
        print(f"{Fore.RED}Invalid choice. Please enter 1, 2, or 3.")

def main():
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, print_exit_message)

    # Prompt for credentials
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")

    # Initialize Instaloader and login
    L = instaloader.Instaloader()

    try:
        # Login with username and password
        L.login(username, password)
        random_delay(2, 5)  # Slight delay after login
    except Exception as e:
        print(f"Error during login: {e}")
        return

    # Initialize instagrapi client for unfollowing functionality
    client = Client()
    try:
        client.login(username=username, password=password)
    except Exception as e:
        print(f"Error logging into client: {e}")
        client = None

    # Fetch profile
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except Exception as e:
        print(f"Error fetching profile: {e}")
        return

    while True:
        show_menu()
        choice = input().strip()
        handle_menu_choice(choice, profile, client)

if __name__ == "__main__":
    print_colored_ascii_art()
    main()
