# My Personal Diary Application
# List of requirements for diary application : title, text features, menu, user login.
# Please create a file named 'personaldiaryapp.txt'.(in the development stage)


import sys

class Diary:
    def __init__(self, title, text, add_diary, view_diary, log_out):

        self.title = title
        self.text = text
        self.add_diary = add_diary
        self.view_diary = view_diary
        self.log_out = log_out



def menu():

    while True:
        selection = input("Press '1' to add a diary entry.\nPress '2' to view the diary.\nPress '3' to log out.\n")
        if selection == "1":
                print("Diary entry selected.")

                file_name = "diaryapp.txt"

                with open(file_name, "w") as file:
                    file.write(userinput())

                    looptext = input("Would you like to write a new text?\nIf your answer is yes, press '1'; if no, press '2'.\n")

                if looptext == "1":

                    with open(file_name, "w") as file:
                        file.write(userinput())

                elif looptext == "2":

                    print("Log out selected, See you next time.")
                    print("Exited.")
                    sys.exit()
                    
                else:

                    print("Please press '1' or '2'.\n")

        elif selection == "2":

            print("Diary viewing selected.")

            file_name = "diaryapp.txt"
            with open(file_name, "r") as file2:
                contents1 = file2.read()

            print("Content of the file:")
            print(contents1)

        elif selection == "3":

            print("Log out selected.")
            print("Exited.")
            sys.exit()
            

        else:

            print("Please press '1','2' or '3'.")



def userinput():

    new_title = str(input("Enter the diary title: "))
    new_text = str(input("Enter the diary text: "))
    add_diary =""
    view_diary =""
    log_out =""

    diaryapp = Diary(new_title, new_text, add_diary, view_diary, log_out)
    
    return f"Title: {diaryapp.title}\nText: {diaryapp.text}"


def writer():

    with open(file_name, "w") as file3:
        file3.write(userinput())

file_name = "diaryapp.txt"


with open(file_name, "r") as file4:
    contents2 = file4.read()
    
    print(f"{file_name} content of the file: \n\n {contents2} \n")


print(menu())
print(writer())