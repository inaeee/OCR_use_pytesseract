try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


#tesseract path
pytesseract.pytesseract.tessreact_cmd=r'C:\Program Files\Tesseract-OCR'


#simple image to string
#영어 사진은 lang 안써도 되지만, 한글 사진은 lang을 써야지 한글로 판독하여 나타냄
print(pytesseract.image_to_string(Image.open('engkor_2.jpeg')))
print('\n\n')


#korean text image to string
print(pytesseract.image_to_string(Image.open('engkor_2.jpeg'), lang='eng+kor'))


#Pytesseract의 영상 변환을 우회하려면 상대적 또는 절대적 영상 경로만 사용하십시오.
#이 경우 Tesseract 지원 이미지를 제공하십시오. 그렇지 않으면 Tesseract가 오류를 반환함
#lang 적용 안됨 = 영어만
print(pytesseract.image_to_string('engkor_1.png'))


#여러 이미지 파일 경로 목록이 포함된 단일 파일을 사용하여 일괄 처리합니다.
#images.txt파일안에 이미지 목록들
print(pytesseract.image_to_string('images.txt'))


#일정 시간 후 tesseract 작업을 시간 초과/종료합니다.
try:
    print(pytesseract.image_to_string('eng_4.png', timeout=2))
    print(pytesseract.image_to_string('eng_4.png', timeout=0.5))
except RuntimeError as timeout_error:
    pass


#경계 상자 추정치를 가져옵니다.
print(pytesseract.image_to_boxes(Image.open('engkor_4.jpg'), lang='eng+kor'))



#상자, 고백, 줄 및 페이지 번호를 포함한 자세한 데이터를 가져옵니다.
print(pytesseract.image_to_data(Image.open('eng_1.png')))


#방향 및 스크립트 검색에 대한 정보를 가져옵니다.
print(pytesseract.image_to_osd(Image.open('engkor_2.jpeg')))


#검색 가능한 PDF를 가져옵니다.pdf로 저장하
pdf=pytesseract.image_to_pdf_or_hocr('engkor_4.jpg', extension='pdf')
with open('engkor_4.pdf','w+b') as f:
    f.write(pdf)
#pdf 유형은 기본적으로 바이트입니다.


# HOCR 출력을 가져옵니다.
hocr=pytesseract.image_to_pdf_or_hocr('eng_1.png',extension='hocr')
print(hocr)
