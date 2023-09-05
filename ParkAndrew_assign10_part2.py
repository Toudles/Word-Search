"""
Assignment #10, Part 2
Andrew Park
"""

def cleanup_string(s):
    result = ''
    for char in s:
        if char.isalpha() or char.isspace():
            result += char.lower()
    return result

#part b
import os
files = os.listdir("data")
#print (files)



#part c
search = {}

#files.remove('.DS_Store')

for i in files:
    file = open('data/'+ i, 'r')
    fi = file.read()
    clean = cleanup_string(fi)
    clean_read = clean.split('\n')
    for line in clean_read:
        for currWord in line.split():
            file_name = i
            #find what file the word is in and prints it
            if currWord not in search.keys():
                search[currWord]=[file_name]
            else:
                if file_name not in search[currWord]:
                    search[currWord].append(file_name)

while True:
    choice = input("search for a (s)ingle word, (m)ultiple words or (q)uit: ") 
    if choice.lower() not in ['s','q','m']: 
        print("Invalid choice")
    else:
        #goes through the files and searches 
        if choice.lower() == 's':
            word = input("Enter a word to search for: ") 
            filesfound = (search.get(word)) 
            print(f"'{word}' can be found in {len(filesfound)} files")
            print("These files are:") 
            for f in filesfound:
                print("* "+f)
                
            display = (input("Display these files? (y/n): "))
            display = display.lower()
            if display != "y" and display != "n":
                print("Invalid command") 
            elif display == "y":
                #call file 
                for f in filesfound:
                    file = open('data/'+ f, "r") 
                    content = file.read() 
                    print("\n* "+f) 
                    print(content) 
                    file.close() 
                print()
            else:
                continue

        elif choice.lower() == 'm':
            input2 = input("Enter two or more words to search for: ")
            #split to search for both words
            i = input2.split(" ")
            found_files = []

            for file in os.listdir('data'):
                with open('data/' + file, 'r') as f:
                    file_content = f.read()
                    #if everything (word in i = both words) are in, then append and print
                    if all(word in file_content for word in i):
                        found_files.append(file)

            if found_files:
                print(f"'{input2}' can be found in {len(found_files)} files")
                print("These files are:")
                for f in found_files:
                    print("* " + f)

                display = input("Display these files? (y/n): ").lower()
                if display == 'y':
                    for f in found_files:
                        with open('data/' + f, 'r') as file:
                            content = file.read()
                            print("\n* " + f)
                            print(content)
                    print()
            else:
                print(f"'{input2}' can't be found in a file!\n")
        elif choice.lower() == 'q':
            break

# print()
# print ('happy:', search['happy'])
# print ('cat:', search['cat'])
# print ('rainbow:', search['rainbow'])
# print ('apple:', search['apple'])
