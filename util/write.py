import os; os.chdir("..")

def write(str):
    with open("invites.txt", "a") as f:
        f.write(str)