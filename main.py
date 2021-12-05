# -*- coding: utf-8 -*-
import add_face 
import comparison
import facelist
#import sys

while(True):
        num = int(input('1. 학생 목록\n2. 학생 사진 추가\n3. 유사도 검사\n4. 종료\n'))
        if num==1:
            print("학생 목록 선택\n")
            facelist.main()
        elif num==2:
            print("학생 사진 추가 선택\n")
            photo = input('추가할 학생사진을 넣어주세요\n')
            add_face.main(photo)
            #add_face.main(sys.argv[0]) 
        elif num==3:
            print("유사도 검사 선택\n")
            fileName = input('입력받을 사진을 넣어주세요\n')
            comparison.main(fileName)
        elif num==4:
            print("종료\n")
            break
        else:
            print("1~4의 숫자로 다시 입력하세요\n")        
