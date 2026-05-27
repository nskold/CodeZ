# Input is the relational database key, pg, from z2.ods.  Output the Syllables and other headings into z3.ods for Alleluia.
# ...eventually intend to put headings into z4.ods for Scrape musicxml.
import os
import pandas 
from pathlib import Path
  
text = "/home/art/NABCprep/just_z2ods.txt"
directory01 = Path("/home/art/Alleluia")
os.chdir(directory01)
print(f"The current working directory is: {Path.cwd()}")

with open( text, 'r', encoding='utf-8') as t:
    list_of_filenames_to_read = [line.strip() for line in t]
    print(f"list of filenames to read is: {list_of_filenames_to_read}")
for current_file in list_of_filenames_to_read: 
    dataframe03 = pandas.read_excel(current_file, engine="odf")     
    print(dataframe03.head())

    dataframe02 = dataframe03.copy()
    dataframe02.columns = ['', 'Page', 'Syllables', 'Bible', 'Subheading']
# The column label, Page, refers to a page number in the Gregorian Missal.
# The column label, Bible, refers to the United States Conference Of Catholic Bishops. 
    score_title_minus_dot_z2_dot_ods = current_file[:-7]
    title_of_score = str(score_title_minus_dot_z2_dot_ods)
# Swap the .z2.ods suffix for the .z3.ods spreadsheet suffix.  
    dataframe02.to_excel(title_of_score + ".z3" + ".ods", sheet_name="Sheet1", engine="odf")
# The middle 2 characters, such as z1, are a Jackson methodology ordering of CodeZ, the back-end code. 
