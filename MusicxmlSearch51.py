# search for musicxml files in Alleluia2025 folder
import os
import re
def remove_txt_file(file_path):
# Removes a specified .txt file.
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' removed successfully.")
        except OSError as e: 
            print(f"Error removing file '{file_path}': {e}")
    else:
        print(f"Thankfully file '{file_path}' does not exist.")
###
justmusicxml = "/home/art/NABCprep/just_musicxml.txt"
# file_to_remove = "justmusicxml"
remove_txt_file(justmusicxml)
###
directory_path = "/home/art/Alleluia" # define the directory to search
# lis = os.li
# justmusicxml = "/home/alens/projects/Art/just_musicxml.txt"
# Avoid appending duplicates. 
# if os.path.exists(justmusicxml):
#    os.remove(justmusicxml)
lis2 =  [  ] 
pattern = r"\.musicxml" # define the (r = raw) static pattern to search
# Dynamically iterate through the files in the directory.
for filename in os.listdir(directory_path):
#    print(f"A cdhjk filename is: {filename} ")  
#     text = fi
#     pattern = r"'(.*)\.musicxml'"
# Use regular expression search to find static pattern in the current filename.    
    match_object = re.search(pattern, filename) 
    if match_object:
        print(f"Found filename: {filename}")
#         topheading = match_object.group(1)
#        print(f"A filename without extension is: '{topheading}' ")
        lis2.append(filename)
        print(f"Matched string: {match_object.group()}")
        with open(justmusicxml, "a") as JMJ: # a = append
            JMJ.write(str(filename) + '\n')

 
  

        
