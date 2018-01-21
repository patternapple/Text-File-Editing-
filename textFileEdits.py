import codecs
import os.path
import json
import re
import string
import sys

number = 0 
while number == 0: # The program will keep running until the user inputs "Q"
    inputname = input("Please, enter a filename: ")
    f = codecs.open(inputname, 'r+', 'utf-8')
    listing = list(f.read())
    print ("*** MENU ***")
    user_choice = input("Please select one option (either 1, 2, 3, 4, 5, 6, 7, 8, or Q): "
                        + "\n1: Display"
                        + "\n2: Count"
                        + "\n3: Encrypt"
                        + "\n4: Decrypt"
                        + "\n5: Remove"
                        + "\n6: Replace"
                        + "\n7: Statistics"
                        + "\n8: Upper Case"
                        + "\nQ: Quit"
                        + "\n")

    # Displays the contents of the text file 
    def display(inputname, f, user_choice):
        if user_choice == "1":
            listing23 = ''.join(listing)
            print (listing23)
    display(inputname, f, user_choice)

    # Prints the number of characters and lines in the file 
    filelength = len(listing)
    def count(inputname, f, user_choice, filelength):
        if user_choice == "2":
            fileline = len(open(inputname).readlines(  ))
            print (str(filelength) + " characters " + "and " + str(fileline) + " lines")
    count(inputname, f, user_choice, filelength)

    # Saves an encrypted version of the file 
    def encrypt(inputname, f, user_choice, count, filelength, listing):
        if user_choice == "3":
            inputefile = input("What would you like the name for the encrypted file to be? ")
            save_path = "/path" #insert path here
            completeName = os.path.join(save_path, (inputefile +".txt"))
            newfile = open(completeName, 'w')
            n = 0
            whatever = ""
            array = []
            while n < filelength:
                whatever = whatever + (str(listing[n]) + "5")
                n +=1
            newfile.write(whatever)
            newfile.close()
            print ("Done")
    encrypt(inputname, f, user_choice, count, filelength, listing)

    # Saves a decrypted version of the file 
    def decrypt(inputname, f, user_choice, count, filelength, listing):
        if user_choice == "4":
            decryptfile = input("What would you like the name for the decrypted file to be? ")
            save_path2 = "/path" #insert path here 
            completeName2 = os.path.join(save_path2, (decryptfile +".txt"))
            newfile2 = open(completeName2, 'w')
            encryptedfile = input("What is the name of the file you want decrypted? ")
            encrypt_open = codecs.open(encryptedfile, 'r+', 'utf-8')
            encrypt_list = list(encrypt_open.read())
            encrypt_list = [w.replace('5', '') for w in encrypt_list]
            encrypt_list = ''.join(encrypt_list)
            newfile2.write(encrypt_list)
            newfile2.close()
            print ("Done")
    decrypt(inputname, f, user_choice, count, filelength, listing)

    # Removes a certain string in the file 
    def remove(inputname, f, user_choice, count, filelength, listing):
        if user_choice == "5":
            removequestion = input("Enter the string to be removed: ")
            listing_remove = [w.replace(removequestion, '') for w in listing]
            listing_remove = ''.join(listing_remove)
            f.write(listing_remove)
            print ("Done")
    remove(inputname, f, user_choice, count, filelength, listing)

    # Replaces a string in the file with a new string 
    def replace(inputname, f, user_choice, count, filelength, listing):
         if user_choice == "6":
            replacequestion = input("Enter the string to be replaced: ")
            replaceanswer = input("Enter the new string to replace the old string: ")
            listing_replace = [w.replace(replacequestion, replaceanswer) for w in listing]
            listing_replace = ''.join(listing_replace)
            f.write(listing_replace)
            print ("Done")
    replace(inputname, f, user_choice, count, filelength, listing)

    # Displays the most frequent character and the number of occurences of it
    def statistics(inputname, f, user_choice, count, filelength, listing):
        if user_choice == "7":
            array4 = []
            numb = 0
            upperstats = [ w.strip().upper() for w in listing]
            from collections import Counter
            while numb < filelength:
                array4.append(upperstats[numb])
                counter2 = (Counter(array4).most_common(1))
                maximum = max(counter2)
                numb +=1
            print ("Most Frequent, Times Shown: " + str(maximum))
    statistics(inputname, f, user_choice, count, filelength, listing)

    # Creates an all-upper case version of the input file 
    def upper(inputname, f, user_choice, count, filelength, listing):
         if user_choice == "8":
            num = 0
            array3 = []
            while num < filelength:
                results = [ w.strip().lower() for w in listing]
                array3.append(results[num])
                listing2 = ''.join(array3)
                num +=1 
            f.write(listing2)
            print ("Done")
    upper(inputname, f, user_choice, count, filelength, listing)

    # Quits the program, stops the cycle 
    def quit_program(inputname, f):
        if user_choice == "Q":
            sys.exit()
    quit_program(inputname, f)



