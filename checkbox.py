import pdfplumber

def extract_checkboxes_with_text(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            # Extract the page's data
            page_text = page.extract_text()

            # Customize checkbox identification based on your PDF structure
            # Here, we'll look for specific checkbox symbols and associated text
            checkboxes = []

            for line in page_text.split('\n'):
                # Identify the checkbox and associated text
                if '☐' in line or '☑' in line or '☒' in line:
                    # Determine the state (checked or unchecked) and associated text
                    text_association = line.split()
                    if '☑' in line:
                        is_checked = True
                        text_index = text_association.index('☑')
                    elif '☒' in line:
                        is_checked = True
                        text_index = text_association.index('☒')
                    try:
                        state = text_association[text_index+1]
                    except Exception as e:
                        state = text_association[text_index-1]
                    # Capture checkbox information
                    checkbox_info = {
                        'is_checked': is_checked,
                        "state" :state
                    }
                    checkboxes.append(checkbox_info)

            # Now checkboxes list contains information about all checkboxes on this page
            # Print or process each checkbox to determine its state
            print(checkboxes)
# Usage
pdf_file_path = "formvalue.pdf"
extract_checkboxes_with_text(pdf_file_path)
