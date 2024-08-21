# open() 함수는 텍스트 모드로 작동함, TextIOWrapper 객체 반환함
# 유니코드 샌드위치 모델 

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)
print(fp.write("""
i want to go cafe with my girlfriend
then, i will read the book, and having good time!!
""")) # 저장한 유니코드 문자수를 반환
fp.close()

import os
print(os.stat('cafe.txt').st_size)
fp2 = open('cafe.txt')
print(fp2.encoding)
print(fp2.read())




