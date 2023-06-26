import requests

def save_image_from_url(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print('이미지가 성공적으로 저장되었습니다.')
    else:
        print('이미지를 다운로드할 수 없습니다.')

# 이미지를 저장할 경로와 파일명을 지정합니다.
file_path = 'SAVE.jpg'

# 이미지 URL을 입력합니다.
image_url = 'http://192.168.0.7/16'

# save_image_from_url 함수를 호출하여 이미지를 저장합니다.
save_image_from_url(image_url, file_path)
