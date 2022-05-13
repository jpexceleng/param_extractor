import re

def extract_descriptions(param_name_file, pdftotext_file, results_file):
# output of this function is a file where each line is of the form:
#   <param_name>;<data_type>;<param_description> 
# args:
#   param_name_file - file containing newline separated param name identifiers.
#   pdftotext_file - file containing the extracted pdf pages converted to plain text;
#                    contains information about the params of interest including 
#                    name, data type, description, etc.
#   results_file - file name to write results to.

    try:
        # get param names into list
        fh = open(param_name_file, 'r')
        params = fh.read().split()
        fh.close()

        # strip raw pdf text of newlines and tabs.
        fh = open(pdftotext_file, 'r')
        data = str()
        for line in fh:
            line = line.strip('\n')
            line = line.strip('\t')
            data += line
        fh.close()

        # find param names and extract params descriptions; assumes params
        # in the pdf plain text file can be identified by the form
        #   '<param_name> <data_type>'
        # where anything after this pattern and not matching the same pattern
        # is part of the description.
        
        descs = []

        # tuple of data types to search for.
        data_types = ('BOOL', 'DINT', 'SINT', 'INT', 'REAL')
        tokens = data.split()
        for i in range(0, len(tokens)):
            if tokens[i] in params:
                if tokens[i + 1] in data_types:
                    # found start param description.
                    desc = tokens[i] + ';'
                    desc += tokens[i + 1] + ';'
                    i += 2
                    while i < len(tokens):
                        if tokens[i] in params:
                            if tokens[i+1] in data_types:
                                # only break if '<param_name> <data_type>' pattern found
                                break
                        # append token as part of param description.
                        desc += tokens[i] + ' '
                        i += 1

                    # add delimiter, store description and reinitialize vars
                    desc += ';'
                    descs.append(desc)
                    desc = str()

            else:
                # scan next token
                i += 1

        # Remove following pattern from description:
        # 'Chapter 2 PlantPAx Publication 1756-RM006L-EN-P - September 2020 <page_num> _'
        # ' Public Input Members Data Type Description '
        descs.sort()
        param_desc_list = []
        for desc in descs:
            ls = str(desc).split(';')
            param_desc_list.append(ls)

        for i in range(0, len(param_desc_list)):
            s = str(param_desc_list[i][2])
            m = re.search(r" Chapter 2 PlantPAx.+?", s)
            if m:
                s = re.sub(r" Chapter 2 PlantPAx.+$", '', s)
                param_desc_list[i][2] = s

        # rebuild list with members of form: <param_name>;<data_type>;<description>
        descs = []
        for item in param_desc_list:
            desc = ';'.join(item)
            descs.append(desc)

        # write results to file.
        fh = open(results_file, 'w')
        for desc in descs:  
            fh.write(desc)
            fh.write('\n')
        fh.close()

    except:
        print('Error extracting descriptions for target')

# list containing targets to extract descriptions for; associated
# files for param_names and pdf plain text must exist for an output
# file containing descriptions to be generated.
targets = [
    'PAI',
    'PAO',
    'PDI',
    'PDO',
    'PDOSE',
    'PMTR',
    'PPID',
    'PVLV',
    'PVSD',
    'PINTLK',
    'PPERM'
]

# attempt to extract descriptions for each target
for target in targets:
    param_name_file = 'output/param_names/' + target + '_param_names.txt'
    pdftotext_file = 'output/pdftotext/' + target + '_pdftotext.txt'
    results_file = 'results/' + target + '_descriptions.txt'
    extract_descriptions(param_name_file, pdftotext_file, results_file)