import pytesseract
from pdf2docx import Converter

def extract_text_from_pdf(pdf_path):
    text = pytesseract.image_to_string(pdf_path, lang='ara')
    return text

def convert_pdf_to_word(pdf_path, output_path):
    with open(output_path, 'wb') as output_file:
        cv = Converter(pdf_path)
        cv.convert(output_path)
        cv.close()

def main():
    pdf_path = '123.pdf'
    word_output_path = 'output.docx'

    # Extract text from PDF using OCR
    text = extract_text_from_pdf(pdf_path)

    # Write text to a temporary text file
    with open('temp.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    # Convert temporary text file to Word document
    convert_pdf_to_word('temp.txt', word_output_path)

    print("Conversion completed.")

if __name__ == "__main__":
    main()