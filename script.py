# Ryan Cheevers-Brown
# NSSA 244 Script 01, Prof. Garrett Arcoraci
# 2023mar20

DEBUG = True

import importlib

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


def dprint(*args, **kwargs):
    # Debug print function, prints everything passed in if DEBUG (global var) is True
    # Used so I don't need to go back and remove prints when done debugging.
    if DEBUG:
        print(*args, **kwargs)


def _create(vbox: virtualbox.VirtualBox):
    # Function to create a VM
    dprint("Entered _create function.")
    pass


def _list(vbox: virtualbox.VirtualBox):
    # Function to list the available VMs
    dprint("Entered _list function.")
    pass


def _start(vbox: virtualbox.VirtualBox):
    dprint("Entered _start function.")
    # Function to start a VM
    pass


def _stop(vbox: virtualbox.VirtualBox):
    dprint("Entered _stop function.")
    # Function to stop a VM
    pass


def _settings(vbox: virtualbox.VirtualBox):
    dprint("Entered _settings function.")
    # Function to list the settings of a particular VM
    pass


def _delete(vbox: virtualbox.VirtualBox):
    dprint("Entered _delete function.")
    # Function to delete a VM
    pass


def _end():
    dprint("Entered _end function.")
    # Function to end the program
    exit(0)


def action():
    # Function to get user input for action
    # Returns the action function to be called
    available_actions = [
        ["Create a VM", "create", _create],
        ["List available VMs", "list", _list],
        ["Start a VM", "start", _start],
        ["Stop a VM", "stop", _stop],
        ["List settings of a VM", "settings", _settings],
        ["Delete a VM", "delete", _delete],
        ["End program", "end", _end],
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
    dprint("Action acquired, returned to main. ")

    dprint("Attempting to execute action.")
    uaction()
    dprint("Action executed, returned to main.")


if __name__ == "__main__":
    main()
