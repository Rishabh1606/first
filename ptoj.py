import PyPDF2 as pypdf
import json

pdfobject = open(r'C:\Users\leovo\Downloads\convert/LLP_Form11-28052016_signed (1).pdf', 'rb')
pdf = pypdf.PdfFileReader(pdfobject)
pdf_data = pdf.getFormTextFields()
print(pdf_data)

cleaned_data = {key.replace("[0]", "").strip(): value for key, value in pdf_data.items() if value is not  None}
print(cleaned_data)








# for key, value in cleaned_data.items():
#     print(key, value)

# for key, value in pdf_data.items():
#     if value is not None:
#         clean_key = key.replace("[0]", "").strip()
        # print(clean_key, value)
