current_command = "start"

def shell():
    global current_command
    while current_command != "exit":
        current_command = input()