from modules.database import Database
from modules.utils import *


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

            client_info = self.primary_database.get_client_info()

            self.primary_database.write(str(client_info))

            print('Successfully saved the info! [200]')

        elif (user_input == '2'):

            print('Yayyy 2')

        elif (user_input == '9'):

            return False


if __name__ == '__main__':

    System()
