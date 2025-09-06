# search for the line containing Solesmes in the musicxml file for Ascensio
f = "/home/alens/projects/Art/musescoreStudioNABCprep/AscensionOfTheLordAlleluiaAWithUSCCB.musicxml" 
output_file = "SolesmesMusicXMLsubset.txt"
formattedMusicXML = [ ]   
def find_substring_in_file(filepath, substring):
###  Reads a file line by line and prints 1st occurrence of a line containing a specified substring.
###  Arguments:
###       filepath (str)  the path to the file to be read.
###       substring (str) the substring to search for within each line.
    try:
        with open(filepath, 'r') as file:    # r means read-only access
            line_number = 0
            for line in file: 
                line_number += 1
                for chars in line:
                    if substring in line:
                        print(f"Substring found in line {line_number}: {line.strip()}")
                        formattedMusicXML.append(str(line_number))
                        formattedMusicXML.append(str(line.strip()))
                        break              
    except FileNotFoundError:
        print(f"Error:  the file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

find_substring_in_file(f, "Solesmes")

with open(output_file,"w") as JMJ:    # w means write access
    JMJ.write(str(formattedMusicXML))         
