import readFilms, addFilm, updateFilms, deleteFilms, reports

# functions to  read the respective menu files with their options
def menuFiles():
    with open("filmsMenu.txt") as mainMenu:
        userMenu = mainMenu.read()

    with open("reportOptions.txt") as reportsMenu:
        userReports = reportsMenu.read()

    return userMenu, userReports



# films main menu function
def filmsMenu():
    options = 0 
    optionsList = ["1", "2", "3", "4", "5", "6"]
    userChoices = menuFiles()

    while options not in optionsList: 
        print(userChoices[0])

        options = input("Enter an options from the films main menu choices above: ") # "1"/ "2"

        if options not in optionsList:
            print(f"{options} is not a valid choice in the films menu! ")
    return options

def reportsMenu():
    options = 0
    optionsList = ["1", "2", "3", "4", "5"]
    userChoices = menuFiles()
    
    while options not in optionsList:
        print(userChoices[1])
        options = input("Enter an option from the reports menu choices above: ")
        
        if options not in optionsList:
            print(f"{options} is not a valid choice in the reports menu! ")
    return options

# create a boolean variable and assign with a True value 
mainProgram = True
while mainProgram: # same as While True
    
    mainMenu = filmsMenu() # assign songsMenu function to the mainMenu variable

    if mainMenu == "1":
        addFilm.insert_data()
    elif mainMenu == "2":
        deleteFilms.delete_data()
    elif mainMenu == "3":
        updateFilms.update_data()
    elif mainMenu == "4":
        readFilms.read_data()
    elif mainMenu == "5":
        reportsProgram = True
        while reportsProgram:
            reportMenu = reportsMenu()

            if reportMenu == "1":
                reports.reportAll()
            elif reportMenu == "2":
                reports.reportGenre()
            elif reportMenu == "3":
                reports.reportYear()
            elif reportMenu == "4":
                reports.reportRating()
            else:
                reportsProgram = False
            
    else:
        mainProgram = False
input("Press Enter to quit the songs app")