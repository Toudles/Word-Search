In this program you will be writing a program that allows the user to search through a series of text files for a word or series of words. This is not unlike the search tool that is built into your Mac or PC that you use to find text within files on your hard drive.

Next, you will need a series of files to search. For the purpose of this program we are providing you with a ZIP file that contains over a hundred random paragraphs of text.

Next you are going to write a parser that will extract the individual words from each of the files listed in this folder. Your end goal is to create a dictionary that has a series of KEYS which represent the individual WORDS found in your files. The VALUES in this dictionary will be a LIST of files that contain that word. For example, the word 'happy' can be found in two files.

For this part of the assignment you will want to write a program that does the following:
  - Begin by creating a new empty dictionary called search
  - Visit each item in the list you obtained from the os module
  - Open each file, read in its contents and clean it up (using your function)
  - Identify each word in the file (hint: how can you break apart each word? what separates them?)
  - Add these words to the dictionary as keys. Hint: if the word is a "new" word you will need to set it up for the first time. If the word is not a "new" word you will need to update      the list associated with that word. Also make sure that you don't add the same filename to the same word twice (for example, if the word 'happy' appears 2 times in file                 'ABC123.txt' you should only add 'ABC123.txt' one time to the list associated with the word happy)
  - When you are finished you should print out the total number of KEYS in the dictionary which represent the total # of words you parsed. The program should generate 1679 unique words     across all 117 files.

Now that you have a working dictionary of words you will be moving on to build a program that will allow users to search for a single word across all of the files.

Finally add in a feature to allow a user to search for multiple words that exist in the same file. These words do not need to be in order (i.e. the search query 'happy birthday' would trigger a hit on 'happy birthday sad kitten!' as well as 'he was so happy on his birthday')
