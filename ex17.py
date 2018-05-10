from sys import argv
from os.path import exists

script, from_file, to_file = argv

#-print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
#-in_file = open(from_file)
#-indata = in_file.read()

in_file = open(from_file); indata = in_file.read()


#-print(f"The input file is {len(indata)} bytes long")

#-print(f"Does the output file exist? {exists(to_file)}")
#-print("Ready, hit RETURN to continue, CTRL-C to abort.")
#-input()

out_file = open(to_file, 'w')
out_file.write(indata)

#-print("Allright, all done.")

out_file.close()
in_file.close()


# --- study Drills ---
#1. Remove "features" and make the code less anoying, going to comment out and add a - after. example: #-
#2. see how short u can make the script
#3. do man cat in the commandline and learn about cat
#4. Find out why you had to write out_file.close() in the code: That file is also opened used the Open() function and thus it has to be closed.
#5. Go read up on Python’s import statement, and start python3.6 to try it out. Try importing some things and see if you can get it right.
