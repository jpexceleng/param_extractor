import re

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

def extract_param_names_to_file(input_file, output_file):
    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')

    param_names = []
    for line in f_in:
        m = re.search('Name="(.+?)"', line)
        if m:
            f_out.write(m.group(1) + '\n')

    f_in.close()
    f_out.close()

for target in targets:
    try:
        f_input = 'data/' + target + '_params_raw.txt'
        f_output = 'output/param_names/' + target + '_param_names.txt'
        extract_param_names_to_file(f_input, f_output)
    except:
        print('Error writing to target: ' + target)