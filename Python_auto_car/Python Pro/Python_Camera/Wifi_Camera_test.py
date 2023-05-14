import cv2

url = 'http://192.168.66.1:9527/videostream.cgi?loginuse=admin&loginpas=admin'

cam = cv2.VideoCapture(url) # 0은 노트북캠, url은 연결된 캠
while True:
    ret, image = cam.read() # ret은 실시간으로 true인지 false인지 확인, image는 이미지값 어레이형태 수치 데이터로 변환
    # print(ret) 궁금하면 옆에 코드 사용해볼 것

    cv2.imshow('IP WiFi camera', image) # imshow는 영상파일 불러오기

    if cv2.waitKey(1) == 27:   # ESC key  waitKey는 imshow와 꼭 같이 써줘야함
        break

cv2.destroyAllWindows() # 모든 창 닫기