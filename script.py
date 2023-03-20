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


def action():
    # Function to get user input for action
    # Returns the action function to be called
    available_actions = [
        ["Create a VM", "create", create],
        ["List available VMs", "list", list],
        ["Start a VM", "start", start],
        ["Stop a VM", "stop", stop],
        ["List settings of a VM", "settings", settings],
        ["Delete a VM", "delete", delete],
        ["End program", "end", end],
    ]
    print(f"Please select an action from the list:")
    for i in range(0, len(available_actions)):
        print(f"{i+1}: {available_actions[i][0]}")
    action = input("Action: ")
    if type(action) == int:
        action = action - 1
        if action < 0 or action > len(available_actions):
            print(f"Invalid action number, please try again.\n")
            action()
        else:
            return available_actions[action][2]
    else:
        action = action.lower()
        for i in range(0, len(available_actions)):
            if action == available_actions[i][1]:
                return available_actions[i][2]
        print(f"Invalid action, please try again.\n")


# Main Function
def main():
    dprint("Attempting to import modules.")
    check_imports()
    dprint("All modules imported successfully, returned to main.")

    dprint("Creating virtualbox object.")
    vbox = virtualbox.VirtualBox()
    dprint("Virtualbox object created, continuing.")

    dprint("Attempting to get user action.")
    uaction = action(vbox)
    session = virtualbox.Session()
    dprint("Action acquired, returned to main. ")

    dprint(f"Attempting to execute {uaction}.")
    uaction(vbox, session)
    dprint("Action executed, returned to main.")


if __name__ == "__main__":
    main()
