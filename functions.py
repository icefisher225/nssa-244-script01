# Ryan Cheevers-Brown
# NSSA 244 Script 01, Prof. Garrett Arcoraci
# 2023mar20
# Helper functions file to clean up main script


DEBUG = True


def dprint(*args, **kwargs):
    # Debug print function, prints everything passed in if DEBUG (global var) is True
    # Used so I don't need to go back and remove prints when done debugging.
    if DEBUG:
        print(*args, **kwargs)


def _getStatus(vbox: virtualbox.Virtualbox, session: virtualbox.Session, machine: virtualbox.Machine):
    # Function to get the status of a VM
    dprint("Entered __getStatus function.")
    status = machine.state
    if status == 1:
        # TODO: Figure out how this function works and what it returns
        pass

def create(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    # Function to create a VM
    dprint("Entered _create function.")
    pass


def list(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    # Function to list the available VMs
    dprint("Entered _list function.")
    machines = [m.name for m in vbox.machines]
    print("Available VMs:")
    print(_list(machines))


def _list(machines):
    # Function to list the available VMs
    dprint("Entered __list function.")
    ret = ""
    for i in range(0, len(machines)):
        ret += f"{i+1}: {machines[i]}\n"
    return ret


def start(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    # Function to start a VM
    # TODO: testing/finishing, may not actually start and just opens session instead
    dprint("Entered _start function.")
    machines = [m.name for m in vbox.machines]
    print(f"Please select a VM to start:")
    print(_list(machines))
    vm = input("VM: ")
    if type(vm) == int:
        vm = vm - 1
        if vm < 0 or vm > len(machines):
            print(f"Invalid VM number, please try again.\n")
            start(vbox)
        else:
            session = virtualbox.Session()
            mac = virtualbox.find_machine(machines[vm])
            progress = mac.launch_vm_process(session, "headless", [])
            progress.wait_for_completion()
    else:
        if vm in machines:
            session = virtualbox.Session()
            mac = virtualbox.find_machine(vm)
            # TODO: check the 'gui' parameter, may need to be changed to 'headless'
            progress = mac.launch_vm_process(session, "gui", [])
            progress.wait_for_completion()
        else:
            print(f"Invalid VM, please try again.\n")
            start(vbox)


def stop(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    dprint("Entered _stop function.")
    # Function to stop a VM
    machines = [m.name for m in vbox.machines]
    print(f"Please select a VM to shutdown:")
    print(_list(machines))
    vm = input("VM: ")
    if type(vm) == int:
        vm = vm - 1
        if vm < 0 or vm > len(machines):
            print(f"Invalid VM number, please try again.\n")
            stop(vbox)
        else:
            session = virtualbox.Session()
            mac = virtualbox.find_machine(machines[vm])
            # TODO: Probably needs different parameters
            progress = mac.launch_vm_process(session, "gui", [])
            progress.wait_for_completion()
            session.console.power_down()
    else:
        if vm in machines:
            session = virtualbox.Session()
            mac = virtualbox.find_machine(vm)
            progress = mac.launch_vm_process(session, "gui", [])
            progress.wait_for_completion()
        else:
            print(f"Invalid VM, please try again.\n")
            stop(vbox)


def settings(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    dprint("Entered _settings function.")
    # Function to list the settings of a particular VM
    settings = []
    # RAM
    # CPU arch, Sockets, cores, threads
    # Firmware type (BIOS or UEFI)
    # state
    # OS type



def delete(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    dprint("Entered _delete function.")
    # Function to delete a VM
    pass


def end(vbox: virtualbox.Virtualbox, session: virtualbox.Session):
    dprint("Entered _end function.")
    # Function to end the program
    exit(0)
