# search for the line containing Solesmes in the musicxml file for hundreds in the just_musicxml.txt file.
import os
import lxml 
from bs4 import BeautifulSoup
import pandas 
from pathlib import Path
  
text = "/home/art/NABCprep/just_musicxml.txt"
directory01 = Path("/home/art/Alleluia")
os.chdir(directory01)
print(f"The current working directory is: {Path.cwd()}")

with open( text, 'r', encoding='utf-8') as t:
    list_of_filenames_to_read = [line.strip() for line in t]
    print(f"list of filenames to read is: {list_of_filenames_to_read}")
for current_file in list_of_filenames_to_read:
    with open(current_file, 'r') as m:
        xml_content = m.read()
        soup = BeautifulSoup(xml_content, features='xml')

        i = 0
        first_three_credit_words = soup.find_all("credit-words", limit=3)
        for w3 in first_three_credit_words:
            i += 1
            text = w3.get_text(strip=True)
            stripped_text = text.strip()
# Triply initialize
            Solesmes2tuple = (i, stripped_text )
            num = len(stripped_text)  

            if i == 1:
                first_credit_words = stripped_text
                print(f"First occurrence of credit words is: {first_credit_words}")
             
            if i == 2:
# if the credit-words text is the empty string...
                if num == 0:
# Anticipate that a third credit-words exists.
                    pick1of3 = 3
                else:
                    pick1of3 = 2  
                    saved_text = stripped_text
        if pick1of3 == 3:  
            saved_text = stripped_text  
        Solesmes2tuple = (pick1of3, saved_text)
        print(f"Final credit-words index and text: {Solesmes2tuple}")
        list_of_chars = list(saved_text)
# Restrict the range of Solesmes Missal page numbers from 100 to 999.
        if list_of_chars[3] == ' ':
# Replace the first blank with a lower case a to assure uniqueness of database key field.
            list_of_chars[3] = 'a'
# Select characters up to but not including 4
        selected_items = list_of_chars[0:4]
        database_unique_item = "".join(selected_items)

        pandas.set_option('display.colheader_justify', 'left')
        dataframe01 = pandas.DataFrame(columns=['pg','col3','col4', 'col5'])
        dataframe02 = dataframe01.copy()
        new_row_label = 2
        dataframe02.loc[new_row_label] = {'pg': database_unique_item}
# The column label, pg, refers to a page number in the Gregorian Missal.
        score_title_minus_dot_musicxml = current_file[:-9] 
        title_of_score = str(score_title_minus_dot_musicxml)
# Swap the .musicxml suffix for the .ods spreadsheet suffix.  
        dataframe02.to_excel(title_of_score + ".z2" + ".ods", sheet_name="Sheet1", engine="odf")
# The middle 2 characters, such as z1, are a Jackson methodology ordering of CodeZ, the back-end code. 
