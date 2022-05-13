PURPOSE:
The purpose of this program is to extract parameter descriptions from PAx documentation for
embedded instructions that fail to be included as part of report for Tag Parameter Properties
exported to an Excel Worksheet using PlantPAx Configuration Tools for Tags, Alarms, and Historian.

THIRD PARTY LIBRARIES USED:
PyPDF2 - used to work with pdf files.
re - regular expression library used for find/search.

OVERVIEW:


HOW TO USE:
1. Run 'extract_pdf_convert_to_text.py' to extract/convert relevant PlantPAx documentation
   for parameters specified in the routine; running this routine results in text files 
   containing the param name and description.

2. Run 'extract_param_names.py' to extract param names from 