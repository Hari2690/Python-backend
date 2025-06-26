# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tests.test_google_gpt import test_google_gpt_api


def print_hi(name):
    print(f'Hi, {name}')
    user_input = input("Enter your GPT Question message: ")
    print("You entered:", user_input)
    data=test_google_gpt_api(user_input)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
