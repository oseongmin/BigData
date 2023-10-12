import urllib.request

url ='https://pt.daelim.ac.kr/eXPortal/css/dl/images/portal_daelim_logo.png'
urllib.request.urlretrieve(url, 'daelim.png')
print('저장 완료')


