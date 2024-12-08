import os
from PyPDF2 import PdfMerger
from datetime import datetime
from django.utils.dateparse import parse_datetime

bulletins_folder = "_media/bulletins"

pdf_files = [os.path.join(bulletins_folder, f) for f in os.listdir(bulletins_folder) if f.endswith('.pdf')]

if len(pdf_files) < 2:
    print("병합할 PDF 파일이 충분하지 않습니다. 최소 2개의 PDF 파일이 필요합니다.")
else:
    pdf_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
    latest_files = pdf_files[:2] 

    # 파일 이름에서 날짜 추출 (예: "2024-12-09")
    dates = []
    for pdf in latest_files:
        filename = os.path.basename(pdf)
        try:
            date_str = filename.split('_')[0]  
            parsed_date = parse_datetime(date_str) or datetime.strptime(date_str, '%Y-%m-%d')
            dates.append(parsed_date)
        except Exception as e:
            print(f"날짜 파싱 오류: {filename}, {e}")

    if dates:
        latest_date = max(dates)
        merged_filename = latest_date.strftime('%Y-%m-%d') + " 주보 보기.pdf"
    else:
        merged_filename = "merged_document.pdf"  

    merger = PdfMerger()

    print("PDF 파일 병합 중...")
    for pdf in latest_files:
        print(f"추가 중: {pdf}")
        merger.append(pdf)

    merged_file_path = os.path.join(bulletins_folder, merged_filename)
    
    merger.write(merged_file_path)
    merger.close()

    print(f"PDF 병합 완료! 병합된 파일: {merged_file_path}")

    for pdf in latest_files:
        try:
            os.remove(pdf)
            print(f"삭제 완료: {pdf}")
        except Exception as e:
            print(f"파일 삭제 중 오류 발생: {pdf}, {e}")
