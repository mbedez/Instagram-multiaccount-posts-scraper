import instaloader
import csv
import time

L = instaloader.Instaloader()

# Replace 'your username' and 'your password' by your login infos
username = 'your username'
password = 'your password'

# Login
try:
    L.load_session_from_file(username)
    if not L.context.is_logged_in:
        L.context.log("Invalid session. You must log in again.")
except FileNotFoundError:
    L.context.log("No session found.")

if not L.context.is_logged_in:
    L.context.log("Connecting...")
    L.load_session_from_file(username)
    if not L.context.is_logged_in:
        L.context.log("Impossible to connect. Please verify your credentials.")
        L.save_session_to_file()

L.context.log("Connected as @" + L.context.username)
 
# All your concerned profiles
profiles = [
    'account1', 'account2', '...'
]

# Open a CSV file in write mode
with open('posts_instagram.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Username', 'Creation_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for username in profiles:
        # load profil
        print(f'\n\n{username}\n')
        profile = instaloader.Profile.from_username(L.context, username).get_posts()

        # Browse posts and write to CSV
        for post in profile:
            date = post.date_utc
            print(f'{date}')
            writer.writerow({
                'username': username,
                'date of creation of the post': date
            })
        time.sleep(30)


print("Datas saved in 'posts_instagram.csv'.")
