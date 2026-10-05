tasks = []

while True:
    print("n1. add task  2. view task  3. remove task  4. quit")
    choice = input("choose an option: ")

    if choice == "1":
        task = input("enter a new task: ")
        tasks.append(task)

    elif choice == "2":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == "3":
        index = int(input("enter task number to remove: ")) -1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print(f"Task number {index + 1} has been removed")

    elif choice == "4":
        print("End of task listing")
        break 

    else:
        print("invalid option")