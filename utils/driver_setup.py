import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


# @pytest.fixture는 테스트가 시작될 때 이 함수를 먼저 실행해 달라는 약속(데코레이터)입니다.
@pytest.fixture
def driver():
    print("\n🚀 [Appium] 인스타그램 자동화 테스트 준비 중...")

    # 1. 옵션 설정 (어떤 폰에서, 어떤 앱을 켤 것인가?)
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'

    # 인스타그램 전용 패키지명과 액티비티명
    options.app_package = 'com.instagram.android'
    options.app_activity = 'com.instagram.android.activity.MainTabActivity'

    # 매우 중요: 매번 로그아웃되는 것을 방지 (현재 로그인 상태 유지)
    options.no_reset = True

    # 2. Appium 서버에 연결하여 스마트폰 제어 권한 얻기
    driver = webdriver.Remote('127.0.0.1:4723', options=options)

    # 테스트 파일들에게 driver(제어권)를 넘겨줌
    yield driver

    # 3. 모든 테스트가 끝나면 깔끔하게 종료
    print("\n🏁 [Appium] 테스트 종료 및 앱 닫기")
    driver.quit()

