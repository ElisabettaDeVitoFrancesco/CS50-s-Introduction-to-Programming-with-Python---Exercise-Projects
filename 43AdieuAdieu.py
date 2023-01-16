import inflect
p = inflect.engine()

def main():
    names_input_list = name_list() # call the function to prompt and save names
    print("\nAdieu, adieu, to", p.join(names_input_list)) # from teh module, used p.join to print out the list's value with commas and "and"

# Function to prompt for n names, to be saved in a list (which is returned)
def name_list():
    names_input_list = []
    while True:

        try:
            name = input("Name: ")
            names_input_list.append(name)
        except EOFError:
            break

    return names_input_list

main()
