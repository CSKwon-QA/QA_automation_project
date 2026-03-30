import os
import time


def take_screenshot(driver, tc_name):
    """
    테스트가 끝날 때 화면을 캡처하여 screenshots 폴더에 저장하는 함수
    """
    folder_path = "screenshots"

    # 1. screenshots 폴더가 없으면 자동으로 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 2. 파일 이름 만들기 (예: IG_HOME_001_20260330_153022.png)
    # 뒤에 시간을 붙여서 사진이 덮어씌워지는 것을 방지합니다.
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_name = f"{folder_path}/{tc_name}_{timestamp}.png"

    # 3. 앱피움으로 스크린샷
    driver.save_screenshot(file_name)
    print(f"\n 스크린샷 저장 완료: {file_name}")