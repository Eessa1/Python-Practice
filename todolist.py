def Add():
    task = input("Enter task")
    file = open('file.txt', mode = 'a')
    file.write(task + '\n')
    file.close()
    

def View():
    file = open('file.txt', mode ='r')
    print(file.read())
    file.close()

def Delete():
    file = open('file.txt', mode ='r')
    list = file.readlines()
    for x in range(len(list)):
        print(x,list[x])
    delnum = int(input("Which item would you like to remove").strip())
    list.pop(delnum)
    file = open('file.txt', mode='w')
    file.writelines(list)
    file.close()

def Quit():
    exit()

while True:
    Choice = int(input("To do list\n 1: Add task \n 2: View tasks\n 3: Delete task\n 4: Quit").strip())
    if Choice == 1:
        Add()
    elif Choice == 2:
        View()
    elif Choice == 3:
        Delete()
    elif Choice == 4:
        Quit()

