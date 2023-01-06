from docxtpl import DocxTemplate
from tkinter.filedialog import asksaveasfile

doc_1 = DocxTemplate('documents/dodatki_1.docx')
dictionary = dict()
dictionary['т1'] = ''
dictionary['л1'] = ''

def replace_data():
    doc_1.render(dictionary)
    asksaveasfile(mode='w', defaultextension='.docx')
    #doc_1.save('documents/new_doc.docx')
# def replace_data():
#     for d in dictionary:
#         for p in doc.tables:
#             for col in p.columns:
#                 for cell in col.cells:
#                     for par in cell.paragraphs:
#                         if par.text.find(d) >= 0:
#                             par.text = par.text.replace(d, dictionary[d])
#     doc.save('documents/new_doc.docx')
# def replace_data():
#     for d in dictionary:
#         for par in iter_block_items(doc):
#             print(par.text)
#             if par.text.find(d) >= 0:
#                 par.text = par.text.replace(d, dictionary[d])
#     doc.save('documents/new_doc.docx')
