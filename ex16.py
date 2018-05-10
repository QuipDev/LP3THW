#imports the argv module from Sys
from sys import argv

#creates variables that stores the two first properties of Argv
script, filename = argv

#Simple print's to give users an option to open or abort.
print(f"We're goingto erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#a simple input to await the users choice
input("?")


print("Opening the file...")
#opens the file in write-mode and saves the fileID in variable target.
target = open(filename, 'w')
print("Truncating the file. Goodbye!")

#empties the file i choosed
target.truncate()


#asks for 3 lines and saves the strings in line1,2 and 3
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")


#writes each string in the variables line1,line2 and line3, it also has a newline formatcode after each line.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#drill 3. writes all the line's in one target.write()
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")



#selfexplained.....
print("And finally, we close it.")
target.close()

# --- study Drills ---
#1. write comments for each line
#2. skipped
#3. marked the line with a comments
#4. It opens the file in read mode and thus making it possible to use readwrite flagged operations on the file.
#5. If you use the w handle when you open a file it automaticlly truncate's the file beforehand so no it's not needed.
