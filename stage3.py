from math import floor

num_cups = 0
more_cups = 0

water_quote = "Write how many ml of water the coffee machine has:\n"
milk_quote = "Write how many ml of milk the coffee machine has:\n"
beans_quote = "Write how many grams of coffee beans the coffee machine has:\n"
cups_quote = "Write how many cups of coffee you will need:\n"
positive_prompt = "Yes, I can make that amount of coffee"


def calc_cups(water, milk, beans):
    return floor(min(water/200, milk/50, beans/15))


if __name__ == '__main__':
    water = int(input(water_quote))
    milk = int(input(milk_quote))
    beans = int(input(beans_quote))
    cups = int(input(cups_quote))

    num_cups = calc_cups(water, milk, beans)
    if num_cups == cups:
        print(positive_prompt)
    elif num_cups < cups:
        negative_prompt = f"No, I can make only {num_cups} cups of coffee"
        print(negative_prompt)
    else:
        more_cups = num_cups - cups
        additional_prompt = f" (and even {more_cups} more than that)"
        print(positive_prompt + additional_prompt)

