try:
    file=open("About.txt" ,"r")
    print(file.read())
except FileNotFoundError:
    print("OOps this file doesn't exist")
finally:
    print("Great minds are build with Great things ,keep the spirit SIMON LESHIPAYO")