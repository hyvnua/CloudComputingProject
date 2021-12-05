# Cloud Computing

2021년도 2학기 클라우드 컴퓨팅 프로젝트

# 프로젝트 명
+ 얼굴 비교를 통한 출석체크 프로그램

# 팀 구성 
+ 팀원 및 역할   
  + 전지혜(대표학생) : AWS S3 버킷에 업로드 가능한 사용자 웹페이지 제작, 사용자가 얼굴 비교 프로그램을 웹에서 이용할 수 있도록(json) 코드 작성
  + 김현화 : AWS Rekognition 얼굴 인식, 기존 사진과 사용자가 업로드 한 사진의 비교(유사도 확인) 프로그램

# 프로젝트 소개 및 개발 내용 소개
+ 위드코로나로 인해 비대면에서 대면으로 전환하는 수업이 증가하면서 직접 출석 체크를 해야하는 일이 증가하였다.
+ 간편한 출석체크와 함께 출석만 하고 집에 가는 이른바 출튀를 방지하기 위한 방법으로 사람이 직접 일일이 누가 왔는지 확인하는 것이 아닌 얼굴 인식만으로 출석 확인이 손쉽게 되도록 하기 위해 개발되었다.
# 프로젝트 개발 결과물 소개 (+다이어그램)
![image](https://user-images.githubusercontent.com/52689866/144739274-67fb55a4-0eb5-48c0-8cfe-fb30c98d5420.png)

# 개발 결과물을 사용하는 방법 소개 (+프로그램 구동 화면 스크릿 샷 첨부)
+ 파이썬 개발 환경에서 비교하고자 하는 원하는 사진을 불러오면 기존 s3 버킷에 이미지들과 유사도를 검사해 그 중 가장 비슷한 사람과의 유사도로 결과로 출력해준다.

# 개발 결과물의 필요성 및 활용방안
+ 학교의 선생님, 대학의 교수님들이 학생들의 출석을 확인하기 위해서, 나아가서는 학원과 회사의 관리를 맡고 있는 사람들이 학생들과 직원들의 근태 체크를 더욱 효율적으로 손쉽게 하기 위해 사용할 수 있다.

//# 프로젝트 주제 및 기대효과
//+ 주제 : 실시간 얼굴 인식 서비스를 통한 출석체크
//+ 기대효과
//  + 실시간 얼굴인식을 통해 학교에 대면/비대면 수업 시 출결을 확인할 수 있다.
//  + 나갈때도 얼굴인식을 통해 이미 출석한 학생들 중에서 중간에 나가는 학생을 파악해 출튀를 방지할 수 있다.


## 개발 환경
  + Python, AWS rekognition
