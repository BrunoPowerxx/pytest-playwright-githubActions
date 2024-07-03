import PyPDF2

# Open the PDF file
with open('Northern Cape Government jobs.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from all pages (modify the loop for specific pages)
text = ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extractText()

# Process or print the extracted text
print(text)
