import sys
import os

'''
NAME = ('Main')

def config():
    print('Which supported rocket are you using?')
    print("(1)(001225 - Alpha Rocket)")
    print("(2)(001261 - Baby Bertha)")
    print("(3)(001948 - Big Bertha)")
	print("(0)Nevermind please take me back (Returns to Main Menu)")
	rocket_choice = input('>>  ')
	
def launch():
    print('Hallo! Sind wir eine Rakete starten?')
    print(' 1. Ja start die Rakete')
    print(' 0. Nein, Wir sollen zuruek gehen')
    menu_choice = input('>>  ')
    if menu_choice == ('0'):
        main_menu()
    if menu_choice == ('1'):
        print('##### WIP #####')
        main_menu()

def configure_rocket_menu():
    print(' 1. To config')
    print(' 0. GEH ZURUEK!!!')
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
    print('###Disclaimer: Our current equations do not currently support liquid state fuel###')
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
###################


001598 - A8-3 STANDARD ENGINE (001225 - Alpha Rocket)(001261 - Baby Bertha)
001601 - B4-2 STANDARD ENGINE (001948 - Big Bertha)
001602 - B4-4 STANDARD ENGINE (001225 - Alpha®)(001261 - Baby Bertha)


###################
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


delP = Ft
m * delV = delp and Ft


.500 * m * (v**2) - (F * h) = (m * g * h)
'''
F = int(((pC * A) / 2) * v ** 2) 
x = int((.500 * m * (v**2)))
y = int((m * g + F))
launch_height = int(x/y)







