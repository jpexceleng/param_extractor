import PyPDF2 

# link to rockwell automation document:
# https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/1756-rm006_-en-p.pdf

# targets to extract; entries have form:
#   <instruction_name>, <start_page>, <end_page> 
targets = [
    ['PAI', 275, 290],
    ['PAO', 346, 359],
    ['PDI', 435, 440],
    ['PDO', 451, 462],
    ['PDOSE', 478, 493],
    ['PMTR', 578, 593],
    ['PPID', 625, 647],
    ['PVLV', 741, 756],
    ['PVSD', 785, 802],
    ['PINTLK', 534, 537],
    ['PPERM', 613, 615]
]

# open pdf file for reading.
pdfFileObj = open ('res/1756-rm006_-en-p.pdf', 'rb')

# create pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# extract text from pdf for all specified targets
for i in range(0, len(targets)):
    file_name = 'output/pdftotext/' + targets[i][0] + '_pdftotext.txt'
    fh = open(file_name, 'w')

    # set page numbers for extraction
    for page_num in range(targets[i][1], targets[i][2] + 1):

        # create page object
        pageObj = pdfReader.getPage(page_num)
        fh.write(pageObj.extractText())

    fh.close()

# clean up.
pdfFileObj.close()