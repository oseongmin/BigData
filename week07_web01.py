import urllib.request
#
# url ='https://pt.daelim.ac.kr/eXPortal/css/dl/images/portal_daelim_logo.png'
# urllib.request.urlretrieve(url, 'daelim.png') #웹에서 가져온 이미지를 보조기억장치에 저장
# print('저장 완료')
url ='https://pt.daelim.ac.kr/eXPortal/css/dl/images/portal_daelim_logo.png'
logo = urllib.request.urlopen(url).read() #이미지를 다운받아서 메모리에 저장

with open('daelim.png', 'wb') as file: #원본 이미지가 png 포맷이므로 테그스타 아닌 바이너리 형식으로 설정
    file.write(logo)    #실제 보조기억장치에 쓰기
    print('저장완료')
