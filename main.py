from modules.database import Database
from modules.utils import *
from modules.database_utils import *


class System():

    def __init__(self):

        # Initializing both databases
        self.primary_database = Database('clients.txt')
        self.secondary_database = Database('orders.txt')

        show_options()

        while (True):
            response = self.handle_input()

            if (response == False):
                return

    def handle_input(self):

        user_input = input('> ')

        # [ 1 ] - Add client
        # [ 2 ] - Remove client
        # [ 3 ] - Update client

        # [ 4 ] - Add order
        # [ 5 ] - Remove order
        # [ 6 ] - Update order

        # [ 7 ] - Read Client's database
        # [ 8 ] - Read Order's database
        # [ 9 ] - Leave

        if (user_input == '1'):

            '''
                TODO: Make a config.txt file and on the first line it will have the primary's database 'serial_number' or whatever the fuck you wanna call it.
                On the second line it will have the secondary's database 'serial_number'

                TODO: Make a function that identifies the serial_number and places it as the 'order / client' number ( like the 'numero da ordem de servico' )
                and return's it and increment's it on both database and number that return's it.
            '''

            client_info = get_client_info()

            self.primary_database.write(str(client_info))

            print('Successfully saved the info! [200]')

        elif (user_input == '2'):

            print('Yayyy 2')

        elif (user_input == '9'):

            return False


if __name__ == '__main__':

    System()
