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

            print('Add client ->\n')

            client_info = self.primary_database.get_client_info()
            self.primary_database.write(str(client_info))

            print('Successfully saved the info! [200]')

        elif (user_input == '2'):

            print('Remove client ->\n')

            index = input('Index: ')
            self.primary_database.delete(int(index))

            print('Successfully removed the client! [200]')

        elif (user_input == '3'):

            print('Update client info ->\n')

            index = input('Index: ')
            new_client_info = self.primary_database.get_client_info()

            self.primary_database.update(int(index), str(new_client_info))

            print('Succesfully updated the client info [200]')

        elif (user_input == '4'):

            print('Add order ->\n')

            order_info = self.secondary_database.get_order_info()
            self.secondary_database.write(str(order_info))

            print('Successfully added the order! [200]')

        elif (user_input == '5'):

            print('Remove order ->\n')

            index = input('Index: ')
            self.secondary_database.delete(int(index))

            print('Successfully removed the order! [200]')

        elif (user_input == '6'):

            print('Update order info ->\n')

            index = input('Index: ')
            new_order_info = self.secondary_database.get_order_info()

            self.secondary_database.update(int(index), str(new_order_info))

            print('Successfully updated the order info! [200]')

        elif (user_input == '7'):

            print('Read client database ->\n')

            option = input('CPF or Name: ')

            self.primary_database.read_(option)

        elif (user_input == '8'):

            print('Read order database ->\n')

            option = input('Client ID or Order ID: ')

            self.secondary_database.read_(option)

        elif (user_input == '9'):

            return False


if __name__ == '__main__':

    System()
