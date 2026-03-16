import time
from utils.driver_setup import driver


def test_01_open_instagram(driver):
    print("\n 인스타그램을 화면 맨 앞으로 끌고 옵니다")

    driver.activate_app('com.instagram.android')

    # 눈으로 확인할 수 있게 5초 멈춰두기
    print("화면 띄우고 5초 대기 중...")
    time.sleep(5)

    print("성공")