### CINEMA APP ###
from classes.customer import Customer
from classes.mytime import MyTime
from classes.reservation import Reservation
from classes.theater import Theater
from classes.transaction import Transaction


movie_list, command, m_command, b_command, r_command = [], '', '', '', ''


def show_movies(list):
    if len(list) > 0:
        i = 1
        for movie in list:
            name, seat, available = movie.get_name_seat_available()
            print(f"{i:<2}. {name:<10} {seat} seats / remaining {available} seats")
            i += 1
        print()
    else:
        print('No movies\n')


### MAIN LOOP ###
while command != 'e':
    #  give choice
    print('(m)ovies\n(b)ookings\n(r)eports\n(e)xit')
    command = input('Choose a menu: ').lower()

    while command == 'm':
        #  print movie list
        print('\nMovies summary')
        show_movies(movie_list)
        #  give choice
        print('(n)ew movie\n(d)elete\n(m)ain menu') if len(movie_list) > 0  else print('(n)ew movie\n(m)ain menu')   
        m_command = input('Choose a menu: ').lower()

        if m_command == 'n':
            movie_name = input('Movie name: ')
            seat_cap = input('Seat capacity: ')
            #  add movie
            movie_list.append(Theater(movie_name, 1, seat_cap))

        elif m_command == 'd':
            index_del = int(input('Movie number: '))
            movie_list.pop(index_del-1)

        elif m_command == 'm':
            command = ''

    while command == 'b':
        #  show movie list
        print('\nBooking summary')
        show_movies(movie_list)
        #  give choice
        print('\n(b)ook\n(m)ain menu')
        b_command = input('Choose a menu: ').lower()
        
        if b_command == 'b':
            name, movie_index, num_seat = input('Name: '), int(input('Movie: ')), int(input('Amount: '))
            #  create customer
            temp_cus = Customer(name, '')
            #  book him/her
            movie_list[movie_index-1].reserve(temp_cus, num_seat)
        elif b_command == 'm':
            command = ''
        
    while command == 'r':
        #  show movie list
        print('\nBooking summary')
        show_movies(movie_list)
        #  give choice
        r_command = input('Enter a movie number or (m)ain menu: ')

        if r_command != 'm':
            r_command = int(r_command)
            #  show customer in r movie
            print(movie_list[r_command-1].get_reserved_seating_info(), '\n')
            #  give choice
            r_sub_command = input('delete item number or (b)ack: ')

            if r_sub_command != 'b':
                r_sub_command = int(r_sub_command)
                #  delete customer from given index
                customer_x = [reservation.get_booker() for reservation in movie_list[r_command-1].get_reserved_list()]
                # movie_list[r_command].cancel(customer_x[0],movie_list[r_command-1].get_tt_id(), 1)
                movie_list[r_command-1].del_customer(r_sub_command-1)
            elif r_command == 'b':
                pass

        elif r_command == 'm':
            command = ''
