import reader
from Library import Library

def display_lib(lib):
    print(lib.get_lib())

if __name__ == '__main__':
    user_lib = Library()
    print('Current library:')
    display_lib(user_lib)

    while True:
        prompt = input("Enter [n] to add uid/directory pair to library or [q] to quit: ")

        if prompt == 'q':
            break
        elif prompt == 'n':
            #print('Waiting for tag...')
            new_uid = reader.listen()
            new_directory = input('Please enter music directory: ')
            print('New uid:', new_uid, 'New directory:', new_directory)

            while True:
                confirmation = input('Are you sure you would like to associate this uid with this directory? [y/n]: ')

                if confirmation == 'y':
                    user_lib.update(new_uid, new_directory)
                    print("Library updated")
                    break
                elif confirmation == 'n':
                    print('Update canceled')
                    break
                else:
                    print('Invalid input')
        else:
            print('Invalid input')