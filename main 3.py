import pdfplumber


def text_extract_pdf(pdf_files):
    pdf = pdfplumber.open(pdf_files)
    full_text = []
    for i, page in enumerate(pdf.pages):
        text = page.extract_text_simple().split('\n')
        compiled_txt = [i.strip() for i in text if i.strip() not in [" ",'']]
        full_text += compiled_txt
    return full_text

form_value = text_extract_pdf("macro-forms.pdf")
form_ = text_extract_pdf("macro-forms1.pdf")

# Function to find common consecutive elements
def find_common_elements(list1, list2):
    common_elements = []
    i = 0
    while i < len(list1) and i < len(list2):
        if list1[i] == list2[i]:
            common_elements.append(list1[i])
        else:
            break
        i += 1
    return ' '.join(common_elements)

form_field_section = []
for item_a, item_b in zip(form_, form_value):
    a = item_a.split()
    b = item_b.split()

    words_a = item_a.split()
    words_b = item_b.split()
    common = find_common_elements(words_a, words_b)
    if common:
        form_field_section.append(common)

fields = {}
for i in range(len(form_field_section)):
    key = form_field_section[i]
    value = form_value[i].replace(key,"").strip()
    fields[key] = value


print(fields)











