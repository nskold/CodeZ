# search for z2.ods files in Alleluia2025 folder
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
justz2ods = "/home/art/NABCprep/just_z2ods.txt"
# file_to_remove = "justz2ods"
remove_txt_file(justz2ods)
###
directory_path = "/home/art/Alleluia" # define the directory to search
# Avoid appending duplicates. 
lis2 =  [  ] 
pattern = r"\.z2.ods" # define the (r = raw) static pattern to search
# Dynamically iterate through the files in the directory.
for filename in os.listdir(directory_path):
# Use regular expression search to find static pattern in the current filename.    
    match_object = re.search(pattern, filename) 
    if match_object:
        print(f"Found filename: {filename}")
        lis2.append(filename)
        print(f"Matched string: {match_object.group()}")
        with open(justz2ods, "a") as JMJ: # a = append
            JMJ.write(str(filename) + '\n')

 
  

        
