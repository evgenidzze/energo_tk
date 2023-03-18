from docxtpl import DocxTemplate
from tkinter import filedialog as fd

doc_1 = DocxTemplate('documents/d_1.docx')
dictionary = dict()


def replace_data():
    doc_1.render(dictionary)
    file_name = fd.asksaveasfilename(filetypes=[("DOCX", ".docx")], initialfile='.docx')
    if '.docx' in file_name:
        doc_1.save(file_name)
    else:
        doc_1.save(file_name + '.docx')
