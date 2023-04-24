# Ryan Cheevers-Brown
# NSSA 244 Script 01, Prof. Garrett Arcoraci
# 2023mar20
# Main Script File

import importlib
from functions import *


# Import modules
def check_imports():
    # Function to import all modules listed in requirements.txt
    # If a module is missing, it will print the missing module name and exit
    with open("requirements.txt", "r") as f:
        requirements = f.read().splitlines()
        for requirement in requirements:
            try:
                importlib.import_module(requirement)
            except ImportError:
                print(f"Missing module {requirement}. Module can be installed with:")
                print(f"python3 -m pip install {requirement}\n")
                exit(1)


def get_action():
    # Function to get user input for action
    # Returns the action function to be called
    # Create
    # List
    # Start
    # Stop
    # Settings
    # Delete
    # End

    available_actions = [
        ["Create a VM", "create", create],
        ["List available VMs", "list", list],
        ["Start a VM", "start", start],
        ["Stop a VM", "stop", stop],
        ["List settings of a VM", "settings", settings],
        ["Delete a VM", "delete", delete],
        ["close program", "close", close],
    ]

    print(f"Please select an action from the list:")
    for i in range(0, len(available_actions)):
        print(f"{i+1}: {available_actions[i][0]}")
    action = input("Action: ")
    dprint("hit past input")
    try:
        action = int(action)
    except:
        action = str(action)
    if type(action) == int:
        # Allows user to choose action by ID #
        action = action - 1
        if action < 0 or action >= len(available_actions):
            print(f"Invalid action ID, please try again.\n")
            return get_action()
        else:
            var = available_actions[action][2]
            dprint(f"returning {var}\n")
            return var
    else:
        # Allows user to choose action by name
        action = action.lower()
        for i in range(0, len(available_actions)):
            if action == available_actions[i][1]:
                return available_actions[i][2]
        print(f"Invalid action, please try again.\n")
        return get_action()


# Main Function
def main():
    dprint("Attempting to import modules.")
    check_imports()
    dprint("All modules imported successfully, returned to main.")

    while True:
        dprint("Attempting to get user action.")
        uact = get_action()
        dprint("Action acquired, returned to main. ")

        dprint(f"Attempting to execute {uact}.")
        if uact == close:
            close()
        try:
            err = uact()
        except:
            print(f"Error executing {uact}, please try again.\n")
            continue
        if err == 0:
            dprint("Action executed, returned to main.")
            continue
        else:
            dprint("Action failed, returned to main.")
            continue


if __name__ == "__main__":
    main()


"""
Sources:"
https://pypi.org/project/virtualbox/
https://www.oracle.com/technical-resources/articles/it-infrastructure/admin-manage-vbox-cli.html
https://www.virtualbox.org/manual/ch08.html
https://blog.scottlowe.org/2016/11/10/intro-to-vbox-cli/

"""
