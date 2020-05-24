class Database():

    def __init__(self, database_name):

        # name needs to have '.txt' at the end
        self.database_name = database_name

    # appends a new data to the database
    def write(self, data):

        file = open(self.database_name, 'a')
        file.write(data + '\n')

    # return the query with all the data inside the database
    def read(self):

        file = open(self.database_name, 'r')
        lines = file.readlines()

        for i in range(len(lines)):
            print(f'Index {i}: {lines[i]}', end='')

    # removes the value inside the index
    def delete(self, index):

        file = open(self.database_name, 'r')
        lines = file.readlines()

        # if it's a valid index
        if (len(lines) > index):
            del lines[index]
        else:
            print('Invalid index')

        # clean the database
        file = open(self.database_name, 'w')

        for line in lines:
            file.write(line)

    # changes the value inside the index
    def update(self, index, new_value):

        file = open(self.database_name, 'r')
        lines = file.readlines()

        # if it's a valid index
        if (len(lines) > index):
            lines[index] = new_value + '\n'
        else:
            print('Invalid index')

        # clean the database
        file = open(self.database_name, 'w')

        for line in lines:
            file.write(line)


if __name__ == '__main__':

    database = Database('test.txt')

    # database.write('This is index 0')
    # database.write('This is index 1')
    # database.write('This is index 2')
    # database.write('This is index 3')

    # database.read()

    # database.delete(0)

    database.update(0, 'This is the new index 0')
