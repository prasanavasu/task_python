import pdfplumber
import pandas as pd
import os
import argparse

def extract_tables_from_pdf(file_path):
    tables_ = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            tables_ += tables     
    return tables_

def extract_text_from_pdf(file_path):
    tables_ = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            texts = page.extract_text_lines()
            extracted_txt = [i.get("text") for i in texts]
            tables_ += extracted_txt
    return tables_

def combine_related_dataframes(data_dict):
    combined_dict = {}

    for key in data_dict.keys():
        base_key = key.split(' – ')[0]  # Extract the base key (e.g., 'Employee Details')

        if base_key not in combined_dict:
            combined_dict[base_key] = data_dict[key]
        else:
            # Concatenate the DataFrames along rows (axis=0)
            combined_dict[base_key] = pd.concat([combined_dict[base_key], data_dict[key]], axis=0)

    return combined_dict


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
    
    pdf_file_path = args.path_doc
    output_path = args.output_path

    tables_with_titles = extract_tables_from_pdf(pdf_file_path)
    text_with_titles = extract_text_from_pdf(pdf_file_path)


    df_tabls = [pd.DataFrame(tab[1:], columns=tab[0]) for tab in tables_with_titles]

    df_table_val = []
    for df_ in df_tabls:
        col = list(df_.columns)
        col_string = ' '.join(col)
        df_table_val.append(col_string)
        data = list(df_.iloc[0].values.tolist())
        data_string = ' '.join(data)
        df_table_val.append(data_string)


    titles = 0
    count = 0
    output = {}
    for i in range(len(text_with_titles)):
        if text_with_titles[i] in df_table_val and (count == 0):
            output[text_with_titles[i-1]] = df_tabls[titles]
            titles += 1
            count = 1
        elif count == 1:
            count = 0
    
    
    # Combine related DataFrames based on keys
    combined_data_dict = combine_related_dataframes(output)
    excel_writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    for key,value in combined_data_dict.items():
        value.to_excel(excel_writer, sheet_name=key, index=False)
    excel_writer.close()

if __name__ == "__main__":
    main()


#python pdf_to_excel_converter.py "C:/Users/PrasanaKumar/Documents/cmp_src/EmployeeDetails2.pdf" "C:/Users/PrasanaKumar/Documents/cmp_src/Output.xlsx"
