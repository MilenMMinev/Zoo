import sys
from animal import Animal
from zoo import Zoo
from create_animal_db import create_animal_table
from create_animal_db import drop_table
import sqlite3

conn = sqlite3.connect("animals.db")
cursor = conn.cursor()


def see_animals(zoo, cursor):
    zoo.table_to_list(cursor)
    for animal in zoo.animals:
        print(animal.get_name() + ' \t:' +
              animal.get_species() + ' , ' +
              animal.get_gender() + ' , ' +
              str(animal.get_age()) + ' , ' +
              str(animal.get_weight()))

def simulate(zoo, interval, period, cursor):
    see_animals(zoo,cursor)
    print('A total of:' + str(len(zoo.animals)))
    total_taxes = 0
    for animal in zoo.animals:
        animal.grow(interval, cursor)
        conn.commit()
    zoo.budget += zoo.get_income(cursor, interval)
    print('your zoo has ' + str(zoo.budget))
    for animal in zoo.animals:
        if animal.die():
            print(animal.get_name() + ' has died :(')
            zoo.move_to_habitat(animal.get_name(), cursor)
        zoo.budget -= animal.eat(interval)
    zoo.reproduce(cursor)
    conn.commit()
    zoo.carry_child(interval * period, cursor)
    conn.commit()
    if not zoo.count_animals(cursor) >= zoo.get_capacity():
        zoo.give_birth(cursor)
        conn.commit()
    zoo.decrease_cooldown(interval * period, cursor)
    conn.commit()


def main():
    myzoo = Zoo()
    create_animal_table(cursor)
    while True:
        command = input('>>>')
        if command == 'list_animals' or command == 'l':
            see_animals(myzoo, cursor)

        elif command == 'simulate' or command == 's':
            interval = int(input('Enter interval of time:'))
            period = int(input('Enter period:'))
            for x in range (period):
                simulate(myzoo, interval, period, cursor)

        elif command == 'accommodate' or command == 'a':
            if myzoo.count_animals(cursor) >= myzoo.get_capacity():
                print("Your zoo is full")
                print(myzoo.count_animals(cursor))
            species = input('Enter species:')
            name = input('Enter name:')
            age = input('Enter age:')
            weight = input('Enter weight:')
            myzoo.accommodate(species, name, age, weight, cursor)
            conn.commit()

        elif command == 'move_to_habitat' or command == 'move':
            name = input('Name:')
            myzoo.move_to_habitat(name, cursor)
            print(name + ' has gone home!')
            conn.commit()

        elif command == 'exit':
            break

    conn.commit()
    conn.close()



if __name__ == '__main__':
    main()
