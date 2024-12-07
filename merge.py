import os
from PyPDF2 import PdfMerger


input_folder = "input_pdf"     
output_folder = "merged_pdf"   
output_filename = "merged_document.pdf"  

pdf_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.pdf')]
pdf_files.sort()  

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

merger = PdfMerger()

print("PDF 파일 병합 중...")
for pdf in pdf_files:
    print(f"추가 중: {pdf}")
    merger.append(pdf)

output_path = os.path.join(output_folder, output_filename)
merger.write(output_path)
merger.close()

print(f"PDF 병합 완료! 병합된 파일: {output_path}")

