import random

def generate_story():
    who = ['alex','sam','steve','Ram']
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
    residence = ['chen','madurai','usa','uk']
    print(f'{random.choice(who)} lived in {random.choice(residence)} {random.choice((when))}')
    answer = input('you want to continue \'y\' or \'n\' : ')
    while (answer == 'y'):
        generate_story();

generate_story()

def generate_password():
    passwordlength = int(input("Enter your password length"))
    pcharacters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    gnpwd = "".join(random.sample(pcharacters,passwordlength))
    print(f'your new password : {gnpwd}')

generate_password()