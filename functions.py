# Ryan Cheevers-Brown
# NSSA 244 Script 01, Prof. Garrett Arcoraci
# 2023mar20
# Helper functions file to clean up main script


DEBUG = False
import subprocess


def dprint(*args, **kwargs):
    # Debug print function, prints everything passed in if DEBUG (global var) is True
    # Used so I don't need to go back and remove prints after debugging.
    if DEBUG:
        print(*args, **kwargs)


def num_input():
    machines = (
        subprocess.check_output("vboxmanage list vms".split(" "))
        .decode()
        .replace('"', "")
        .splitlines()
    )
    machs = []
    for i in range(len(machines)):
        machs.append(machines[i].split(" ")[0])
    print("Available VMs:")
    print(_list(machs))
    vm = input("VM: ")
    try:
        vm = int(vm)
    except:
        vm = str(vm)
    return vm, machs, machines


def _list(machines):
    # private helper function to list the available VMs, only for use as part of other functions
    dprint("Entered _list function.")
    ret = ""
    for i in range(0, len(machines)):
        ret += f"{i+1}: {machines[i]}\n"
    return ret


def create():
    # Function to create a VM
    dprint("Entered _create function.")
    name = input("Please enter a name for the VM: ")
    os = input("Please enter the OS for the VM: ")

    cmd = [
        "VBoxManage",
        "createvm",
        "--name",
        f"{name}",
        "--ostype",
        f"{os}",
        "--register",
    ]
    # TODO: Figure out command handling i guess?
    subprocess.run(cmd)
    return 0


def list():
    # Function to list the available VMs
    dprint("Entered list function.")
    # machines = [m.name for m in vbox.machines]
    machs = (
        subprocess.check_output("vboxmanage list vms".split(" ")).decode().splitlines()
    )
    dprint(machs)
    for i in range(len(machs)):
        machs[i] = machs[i].split(" ")[0].replace('"', "")
    print("Available VMs:")
    print(_list(machs))
    # TODO: test command handling
    return 0


def start():
    # Function to start a VM
    dprint("Entered start function.")
    vm, machs, machines = num_input()
    if type(vm) == int:
        vm = vm - 1
        if vm < 0 or vm >= len(machines):
            print(f"Invalid VM number, please try again.\n")
            return start()
        else:
            cmd = f"VBoxManage startvm {machines[vm]}"
    else:
        if vm in machs:
            cmd = f"VBoxManage startvm {vm}"
        else:
            print(f"Invalid VM, please try again.\n")
            return start()
    print(subprocess.check_output(cmd.split(" ")))
    return 0


def stop():
    dprint("Entered stop function.")
    # Function to stop a VM
    print(f"Please select a VM to shutdown:")
    vm, machs, machines = num_input()
    if type(vm) == int:
        vm = vm - 1
        if vm < 0 or vm > len(machines):
            print(f"Invalid VM number, please try again.\n")
            return stop()
        else:
            cmd = f"VBoxManage controlvm {machines[vm]} poweroff"
    else:
        if vm in machs:
            cmd = f"VBoxManage controlvm {vm} poweroff"
        else:
            print(f"Invalid VM, please try again.\n")
            return stop()
    print(subprocess.check_output(cmd.split(" ")))
    return 0


def settings():
    dprint("Entered settings function.")
    # Function to list the settings/status of a particular VM
    vm, machs, machines = num_input()
    if type(vm) == int:
        vm = vm - 1
        if vm < 0 or vm > len(machines):
            print(f"Invalid VM number, please try again.\n")
            return settings()
        else:
            cmd = (
                f"VBoxManage showvminfo {machines[vm].split(' ')[0].strip()} --details"
            )
    else:
        if vm in machs:
            cmd = f"VBoxManage showvminfo {vm} --details"
        else:
            print(f"Invalid VM, please try again.\n")
            return settings()
    print(subprocess.check_output(cmd.split(" ")).decode())
    return 0


def delete():
    dprint("Entered delete function.")
    # Function to delete a VM
    vm, machs, machines = num_input()
    if type(vm) == int:
        vm = vm - 1
        if vm < 0 or vm > len(machines):
            print(f"Invalid VM number, please try again.\n")
            return delete()
        else:
            cmd = f"VBoxManage unregistervm --delete {machines[vm].split(' ')[0]}"
    else:
        if vm in machs:
            cmd = f"VBoxManage unregistervm --delete {vm}"
        else:
            print(f"Invalid VM, please try again.\n")
            return delete()
    subprocess.check_output(cmd.split(" "))
    print()
    return 0


def close():
    dprint("Entered end function, exiting program.")
    # Function to end the program
    exit(0)
