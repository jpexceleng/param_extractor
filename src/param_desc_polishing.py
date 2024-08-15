"""
220517 JWP
There are additional fields that were not initially handled in the first attempt
of parameter extraction. This resulted in values being included in the description
that shouldn't be. For example:
    the data table for PAI instructions in the original documentation is simple
    and works well with the current implementation; it has the form:
    <param_name>;<data_type>;<param_description>
    
    with the following result:
    Cfg_AllowDisable;BOOL;1 = Allow maintenance to disable alarms. Default is true. ;

    For PVLV instructions, however, the original data table is of the form:
    <param_name>;<data_type>;<FBD_default_visibility>;<FBD_wiriing_required>;<usage>;<param_description>

    with the following result:
    Cfg_HasExt;BOOL;Not Visible Not Required Input 1 = External exists, can be selected. Default is false. ;

    Notice the additional 'Not Visible Not Required Input' portion that doesn't seem to belong.

This script will handle these cases. Instruction types affected are PDOSE, PMTR, PPID, PVLV, PVSD.
"""

# strategies for handling additional fields:
# - fbd_default_visibility = {'Visible', 'Not Visible'}; extract everything up to and including 'Visible'.
# - fbd_wiring_required = {'Required', 'Not Required'}; extract everything up to and including 'Required'.
# - usage = {'Input', 'Output'}; only two values possible here.
# - default_value; only present for PPID instructions.

# import regular expression methods
import re

def delimit_fbd_default_visibility(line):
    # 'Visible' or 'Not Visible'; 1 after Data_Type.
    # search until after first occurrence of 'Visible'
    # add ';'
    arr = line.split(';')
    

def delimit_fbd_wiring_required(line):
    # 'Required' or 'Not Required'; 2 after Data_Type.
    # search until after first occurence of 'Required'
    # add ';'
    line

def delimit_usage(line):
    # 'Input' or 'Output'; 3 after Data_Type.
    # read in next token (either 'Input' or 'Output')
    # add ';'
    line

def polish_ppid_params(file):
# 'True', 'False', '0.0', '0', '1.0', '1', '4', '2', 100.0' '1.5e+38' '-1.5e+38'
# 1 after Data_Type.
# don't need to be precise, just read up until the next occurrence of whitespace.
    fh = open('test\\test.txt', 'w')

    fh_ref = open(file, "r")
    for line in fh_ref:
        ls = line.split(';')
        
        s = str(ls[2])
        # search for match on page header
        match = re.search(r'\d?\.?\d?', s)
        if match:
            # if match found, add delimiter.
            s = re.sub(r'\bTrue\b | \bFalse\b', match.string+';', s)

            # update list value.
            ls[3] = s

        # rejoin list items on ';' delimiter and write to file.
        line = ';'.join(ls)
        fh.write(line + '\n')

    # close files.
    fh.close()
    fh_ref.close()
        

def polish_other_params(file):
# PDOSE, PMTR, PVLV, PVSD can all be handled by one function.
    fh = open(file, "r")
    for line in fh:
        delimit_fbd_default_visibility(line)
        delimit_fbd_wiring_required(line)
        delimit_usage(line)
        # reconstruct and write line to file

polish_ppid_params('results\\PPID_param_desc.txt')