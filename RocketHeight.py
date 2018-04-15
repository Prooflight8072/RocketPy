import sys
import os
NAME = ('Main')

def config():
    print('Which supported rocket are you using?')
    print("(1)(001225 - Alpha Rocket)")
    print("(2)(001261 - Baby Bertha)")
    print("(3)(001948 - Big Bertha)")
	print("(0)Nevermind please take me back (Returns to Main Menu)")
	rocket_choice = input('>>  ')
	if rocket_choice == ('1'):
		rocket_type = ('Alpha')
	if rocket_choice == ('2'):
		rocket_type = ('Baby')
	if rocket_choice == ('3'):
		rocket_type = ('Big')
	
def launch():
    print('Make sure your rocket is configured before launching')
    print(' 1. Launch the rocket')
    print(' 0. No Take Me Back')
    menu_choice = input('>>  ')
    if menu_choice == ('0'):
        main_menu()
    if menu_choice == ('1'):
        print('##### WIP #####')
        main_menu()

def configure_rocket_menu():
    print(' 1. To config')
    print(' 0. Go back')
    menu_choice = input('>>  ')
    if menu_choice == ('0'):
        main_menu()
    if menu_choice == ('1'):
        config()

def back_main():
    main_menu()

def exit():
    sys.exit()

def main_menu():
    print('Welcome,')
    print('Select a Menu Bellow')
    print(' 1. Launch')
    print(' 2. Configure Rocket')
    print(' 0. QUIT')
    menu_choice = input(' >> ')
    if menu_choice == ('1'):
        launch()
    if menu_choice == ('2'):
        configure_rocket_menu()
    if menu_choice == ('0'):
        exit()

if NAME == ('Main'):
    main_menu()
'''
###################
001598 - A8-3 STANDARD ENGINE (001225 - Alpha Rocket)(001261 - Baby Bertha)
001601 - B4-2 STANDARD ENGINE (001948 - Big Bertha)
001602 - B4-4 STANDARD ENGINE (001225 - Alpha®)(001261 - Baby Bertha)
###################
'''
def velocitycalc():
	distance = input('How far are you traveling? km')
	time = input('how long do you want to take getting there? min')
	velocity = (distance * time)
	print (velocity, 'km/min')
	
def accelcalc():
	inivel = input('what is your initial velocity? km')
	finvel = input('what is your final velocity? km')
	vel = (finvel - inivel)
	initime = ('what is your initial time (usualy this value is zero) min')
	fintime = ('what is your final time (how long) min')
	finini = (fintime - initime)
	acceltime = (vel / finini)
	print (acceltime , 'km/min')

def height_find():
	A = int(math.py() * (r**2))
	Fx = int((0.45*0.25)* A)
	Fy = int(2)
	Ffin = ((Fx / Fy)*r**2)








