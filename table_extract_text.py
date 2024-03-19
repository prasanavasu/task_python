import pdfplumber
import pandas as pd
import argparse
import os

def extract_tables_from_pdf(file_path):
    tables_ = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            tables_ += tables     
    return tables_


# Example data
def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Excel")
    parser.add_argument("path_doc", type=str, help="Path to input PDF file")
    parser.add_argument("output_path", type=str, help="Path to output Excel file")
    args = parser.parse_args()

    # Check if the input file is a PDF and output file has the .xlsx extension
    if not args.path_doc.lower().endswith('.pdf'):
        print("Error: Input file must be a PDF.")
        return
    if not args.output_path.lower().endswith('.xlsx'):
        print("Error: Output file must have a .xlsx extension.")
        return

    # Check if input PDF file exists
    if not os.path.exists(args.path_doc):
        print("Error: Input PDF file not found.")
        return
    
    path_doc = args.path_doc
    output_path = args.output_path
    excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    count = 0
    list_data = extract_tables_from_pdf(path_doc)
    for tab in list_data:
        count += 1
        columns = tab[0]
        rows = tab[1:]
        df = pd.DataFrame(rows, columns=columns)
        df.to_excel(excel_writer, sheet_name=f"sheet_{count}", index=False)


    excel_writer.close()

if __name__ == "__main__":
    main()

#python pdf_to_excel_converter.py "C:/Users/PrasanaKumar/Documents/cmp_src/EmployeeDetails2.pdf" "C:/Users/PrasanaKumar/Documents/cmp_src/Output.xlsx"



# convert the output in sheet xlsx
# sheet name is table name
# terminal args path - output and input
