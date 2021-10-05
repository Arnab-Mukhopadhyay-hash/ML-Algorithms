def get_date():
    import datetime
    return datetime.datetime.now()


def retrieve_client(client_name):
    n = int(input("Enter 1 for exercise chart\nEnter 2 for diet chart\n"))
    if client_name == "Harry":
        if n == 1:
            with open('Harry_workout.txt') as hw:
                for line in hw:
                    print(f"[{get_date()}]", line)
        else:
            with open('Harry_Food.txt') as hf:
                for line in hf:
                    print(f"[{get_date()}]", line)
    elif client_name == "Rohan":
        if n == 1:
            with open('Rohan_Workout.txt') as rw:
                for line in rw:
                    print(f"[{get_date()}]", line)
        else:
            with open('Rohan_food.txt') as rf:
                for line in rf:
                    print(f"[{get_date()}]", line)

    elif client_name == "Shyam":
        if n == 1:
            with open('Shyam_Workout.txt') as sw:
                for line in sw:
                    print(f"[{get_date()}]", line)
        else:
            with open('Shyam_Food.txt') as sf:
                for line in sf:
                    print(f"[{get_date()}]", line)


def input_func():
    client = input("Enter the client name: ")
    retrieve_client(client)
    # n = int(input("Enter 1 for exercise chart\n Enter 2 for diet chart\n"))


input_func()