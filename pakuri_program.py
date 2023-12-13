# pakuri_program driver file

# import Pakuri and Pakudex class
from pakuri import Pakuri
from pakudex import Pakudex

def main():
    # welcome message
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    valid = False

    # get a valid max capacity (must be int greater than 0
    while valid == False:
        try:
            # checks that max_capacity is an integer
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity < 0:
                # checks that max_capacity is greater than 0
                raise ValueError
            # initializes a pakudex with the entered max_capacity using Pakudex class
            my_pakudex = Pakudex(max_capacity)
            print(f"The Pakudex can hold {max_capacity} species of Pakuri.\n")
            valid = True
        except ValueError:
            print("Please enter a valid size.")
    option = None
    while option != 6:
        # program runs until option 6 is selected
        print_menu()
        try:
            # user enters an option from 1 to 6
            # checks that option is an integer
            option = int(input("What would you like to do? "))
            if option < 1 or option > 6:
                # checks that option is only from 1 to 6; else raises error
                raise ValueError
            if option == 1:
                # list Pakuri
                pakuri_list = my_pakudex.get_species_array()
                if pakuri_list == None:
                    print("No Pakuri in Pakudex yet!\n")
                else:
                    # prints all pakuri in pakuri_list, which comes from self.pakuris in my_pakudex
                    print("Pakuri In Pakudex: ")
                    for i in range(len(pakuri_list)):
                        print(f"{i + 1}. {pakuri_list[i]}")
                    print()
            elif option == 2:
                # show pakuri
                name = input("Enter the name of the species to display: ")
                # gets stats in a list
                stats_list = my_pakudex.get_stats(name)
                if stats_list != None:
                    # checks that the pakuri exists, and get_stats() returns a list
                    print(
                        f"\nSpecies: {name}\nAttack: {stats_list[0]}\nDefense: {stats_list[1]}\nSpeed: {stats_list[2]}\n")
                else:
                    # if get_stats() returns None, this message will print
                    print("Error: No such Pakuri!\n")
            elif option == 3:
                # add pakuri
                if my_pakudex.get_size() >= my_pakudex.get_capacity():
                    # checks that there is room in my_pakudex, aka my_pakudex isn't at capacity
                    print("Error: Pakudex is full!\n")
                else:
                    # adds pakuri to my pakudex
                    name = input("Enter the name of the species to add: ")
                    success = my_pakudex.add_pakuri(name)
                    if success == False:
                        print("Error: Pakudex already contains this species!")
                    else:
                        print(f"Pakuri species {name} successfully added!")
                    print()
            elif option == 4:
                # evolve pakuri
                name = input("Enter the name of the species to evolve: ")
                success = my_pakudex.evolve_species(name)
                if success == True:
                    # checks that evolve_species() worked
                    print(f"{name} has evolved!\n")
                else:
                    # can't evolve pakuri if it doesn't exist, otherwise can
                    print("Error: No such Pakuri!\n")
            elif option == 5:
                # sort pakuri in standard lexicographical order by their names
                my_pakudex.sort_pakuri()
                print("Pakuri have been sorted!\n")
            elif option == 6:
                # exit while loop and program
                print("Thanks for using Pakudex! Bye!")
                break
        except ValueError:
            print("Unrecognized menu selection!\n")

def print_menu():
    # prints the Pakudex Main Menu
    print("Pakudex Main Menu\n-----------------\n1. List Pakuri\n"
          "2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n"
          "6. Exit\n")

if __name__ == '__main__':
    main()