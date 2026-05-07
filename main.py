import os
import PyPDF2
import re
#from google_sheets import GoogleSheets # for a db saving later

def extract_invoice_info(pdf_file_path):

    # Open PDF File
    with open(pdf_file_path, 'rb') as file:

        # PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        # Get text from each page
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        #print("Text: ",text)

        # Regular expressions
        invoice_number_pattern = r'Invoice Number:\s*#\s*(\d+)'
        bill_to_pattern = r'Bill To:\s*(.*)'
        items_pattern = r'(.*?)\s*(\d+)\s*(\$\d+\.\d{2})\s*(\$\d+\.\d{2})'
        notes_terms_pattern = r'Notes:\s*(.*?)\s*Terms:\s*(.*)'

        # Extract information using regex
        invoice_number_match = re.search(invoice_number_pattern, text)
        bill_to_match = re.search(bill_to_pattern, text)
        items_matches = re.findall(items_pattern, text)
        notes_terms_match = re.search(notes_terms_pattern, text)
        discount_tax_pattern = r'Discount:\s*(\$\d+\.\d{2})\s*Tax:\s*(\$\d+\.\d{2})'

        # Extracted information
        invoice_number = invoice_number_match.group(1) if invoice_number_match else None
        bill_to = bill_to_match.group(1) if bill_to_match else None
        items = items_matches
        notes, terms = notes_terms_match.groups() if notes_terms_match else (None, None)
        match = re.search(discount_tax_pattern, text)
        discount_percentage = match.group(1) 
        tax_percentage = match.group(2) 

        i=0
        subtotal=0
        total = 0
        for item in items:
            if len(Items)-1 != i:
                subtotal += float(item[3].replace('$',''))
            i = i +1
        
        total_discount = subtotal - (subtotal*int(discount_percentage)/100)
        total = total_discount + (total_discount*int(tax_percentage)/100)

        return invoice_number, bill_to, subtotal, total, discount_percentage, tax_percentage, notes, terms

def get_files_in_folder(folder_path):
    files = []
    #iterate through all files in the folder
    for root, dirs, file_names in os.walk(folder_path):
        for file_name in file_names:
            # append the full file path to the list
            files.append(os.path.join(root, file_name)) 
    return files

if __name__ == "__main__":

    folder_path = 'invoices'
    files = get_files_in_folder(folder_path)

    for file in files:

        print("File: ", file)
        invoice_number, bill_to, subtotal, total, discount_percentage, tax_percentage, notes, terms = extract_invoice_info(file)

        # Extracted information
        print(f"Invoice Number: {invoice_number}")
        print(f"Bill To: {bill_to}")
        print(f"Subtotal: {subtotal}")
        print(f"Total: {total}")
        print(f"Notes: {notes}")
        print(f"Terms: {terms}")    
        print(f"Discount: {discount_percentage}")
        print(f"Tax: {tax_percentage}") 

        # Move the file to a processed folder
        processed_folder = 'processed_invoices'
        os.makedirs(processed_folder, exist_ok=True)
        new_file_path = os.path.join(processed_folder, os.path.basename(file))
        os.rename(file, new_file_path)

invoice_number, bill_to, subtotal, total, discount_percentage, tax_percentage, notes, terms = extract_invoice_info('invoices/invoice.pdf')



#extract_invoice_info('invoices/invoice.pdf')
