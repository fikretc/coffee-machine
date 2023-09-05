
mytext = "Starting to make a coffee\n\
Grinding coffee beans\n\
Boiling water\n\
Mixing boiled water with crushed coffee beans\n\
Pouring coffee into the cup\n\
Pouring some milk into the cup\n\
Coffee is ready!\n"

prompt1 = "Write how many cups of coffee you will need:\n"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def calculate_ingredients(num_cups):
    return 200*num_cups, 50*num_cups, 15*num_cups


if __name__ == '__main__':
    num_cups = int(input(prompt1))
    water, milk, coffee_beans = calculate_ingredients(num_cups)
    print(f'For {num_cups} cups of coffee you will need:\n\
{water} ml of water\n\
{milk} ml of milk\n\
{coffee_beans} g of coffee beans')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
