import os
import subject
import studyDate


def loop(func):
    running = True
    while running:
        if func() == False:
            running = False
    return False












def showScreen(screen):
    os.system("cls")
    for s in screen.split("."):
        print(s.lstrip())
def invalidInput():
    print("invalid input, click enter to continue...")
    input()
def mainMenu():
    screen ='''
    subjects to study = s.
    add subjects      = a.
    quit              = q.
    '''
    showScreen(screen)
    userInput = input()
    if userInput == "q":
        return False
    if userInput == 'a':
        loop(addsubjects)
    else:
        invalidInput()
def addsubjects():
    screen = "enter subject name..."
    subName = input()
    try:
        


if __name__ == "__main__":
    loop(mainMenu)
