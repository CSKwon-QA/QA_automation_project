# tests/test_01_home_feed.py

# driver와 HomePage를 가져옵니다.
from utils.driver_setup import driver
from pages.page_home import HomePage


def test_ig_home_001_verify_logo(driver):
    print("\n[TC: IG_HOME_001] 홈 피드 로고 검증 시작")

    # 1. 사전 조건: 인스타그램 앱 강제 호출 (백그라운드 방지)
    driver.activate_app('com.instagram.android')

    # 2. 객체 생성: HomePage 부품 상자 열기
    home_page = HomePage(driver)

    # 3. 행동 실행: 로고가 있는지 확인하고 결과를 is_logo_visible 변수에 담음 (True 또는 False)
    is_logo_visible = home_page.check_logo_is_visible()

    # 4. 검증 (Assert)
    # 결과가 무조건 True여야만 테스트를 'PASSED' 처리합니다.
    assert is_logo_visible == True, "로고가 화면에 없습니다! 테스트 실패(FAILED)!"


# 기존 test_ig_home_001_verify_logo 함수 아래에 추가합니다.
import time


def test_ig_home_002_pull_to_refresh(driver):
    print("\n[TC: IG_HOME_002] 홈 피드 새로고침 검증 시작")

    home_page = HomePage(driver)

    # 1. 스와이프 액션 실행
    home_page.swipe_down_to_refresh()

    # 새로고침 로딩 스피너가 돌고 피드가 재정렬될 시간을 잠시 대기합니다.
    time.sleep(2)

    # 2. 검증: 새로고침 후에도 앱이 크래시 나지 않고 홈 로고가 정상 노출되는지 확인
    is_logo_visible = home_page.check_logo_is_visible()

    assert is_logo_visible == True, "새로고침 수행 후 홈 화면 요소가 정상적으로 로드되지 않았습니다."


def test_ig_home_003_scroll_down(driver):
    print("\n[TC: IG_HOME_003] 홈 피드 5회 연속 스크롤 다운 검증 시작")

    home_page = HomePage(driver)

    # 1. 5회 반복하여 스크롤 다운 액션 실행
    for i in range(5):
        print(f"[Action] {i + 1}번째 스크롤 다운 실행")
        home_page.scroll_down_feed()
        time.sleep(2)  # 다음 게시물이 로드되도록 2초 대기

    # 2. 크래시 없이 5회 스크롤이 완료되었는지 확인
    assert True


def test_ig_home_004_click_like(driver):
    print("\n[TC: IG_HOME_004] 게시물 좋아요 클릭 검증 시작")

    home_page = HomePage(driver)

    # 좋아요 버튼 클릭 메서드 호출
    is_clicked = home_page.click_like_button()

    # 1초 대기 (UI 상태 변경 확인용)
    time.sleep(1)

    # 정상적으로 클릭되었는지 검증
    assert is_clicked == True, "좋아요 버튼 요소 식별 및 클릭에 실패했습니다."


def test_ig_home_005_cancel_like(driver):
    print("\n[TC: IG_HOME_005] 게시물 좋아요 취소 검증 시작")

    home_page = HomePage(driver)

    # 1. 좋아요 취소 액션 실행 (4번 TC에서 누른 동일한 버튼을 다시 클릭)
    is_canceled = home_page.cancel_like()

    # UI가 빈 하트로 원복될 시간을 명시적으로 대기
    time.sleep(1)

    # 2. 정상적으로 클릭 액션이 수행되었는지 검증
    assert is_canceled == True, "좋아요 취소 동작 수행에 실패했습니다."


def test_ig_home_006_click_save(driver):
    print("\n[TC: IG_HOME_006] 게시물 북마크(저장) 클릭 검증 시작")

    home_page = HomePage(driver)

    # 1. 북마크 버튼 클릭 액션 실행
    is_saved = home_page.click_save_button()

    # 북마크 아이콘 색상 변경 및 하단 스낵바 노출 대기
    time.sleep(1)

    # 2. 정상적으로 클릭 액션이 수행되었는지 검증
    assert is_saved == True, "북마크 버튼 요소 식별 및 클릭에 실패했습니다."


def test_ig_home_007_open_and_close_comment(driver):
    print("\n[TC: IG_HOME_007] 피드 댓글 창 진입 및 닫기 검증 시작")

    home_page = HomePage(driver)

    # 1. 댓글 창 열기 클릭
    is_clicked = home_page.click_comment_button()
    assert is_clicked == True, "댓글 버튼 클릭에 실패했습니다."

    # 2. 바텀 시트 노출 상태 검증
    is_sheet_visible = home_page.check_comment_sheet_is_visible()
    assert is_sheet_visible == True, "바텀 시트가 화면에 노출되지 않았습니다."

    # 3. 댓글 창 닫기 (뒤로 가기 2회)
    is_closed = home_page.close_bottom_sheet()
    assert is_closed == True, "바텀 시트 닫기 동작에 실패했습니다."

    time.sleep(1)


def test_ig_home_007_open_and_close_comment(driver):
    print("\n[TC: IG_HOME_007] 피드 댓글 창 진입 및 닫기 검증 시작")

    home_page = HomePage(driver)

    # 1. 댓글 창 열기 클릭
    is_clicked = home_page.click_comment_button()
    assert is_clicked == True, "댓글 버튼 클릭에 실패했습니다."

    # 2. 바텀 시트 노출 상태 검증 (찾아오신 android:id/list 검증)
    is_sheet_visible = home_page.check_comment_sheet_is_visible()
    assert is_sheet_visible == True, "바텀 시트가 화면에 노출되지 않았습니다."

    # 3. 댓글 창 닫기 (pages에 정의된 뒤로 가기 2번 실행)
    is_closed = home_page.close_bottom_sheet()
    assert is_closed == True, "바텀 시트 닫기 동작에 실패했습니다."

    # 피드 화면으로 복귀 후 안정화를 위한 1초 대기
    time.sleep(1)


def test_ig_home_008_enter_profile(driver):
    print("\n[TC: IG_HOME_008] 피드 게시물 작성자 프로필 진입 검증 시작")

    home_page = HomePage(driver)

    # 1. 게시물 상단의 작성자 프로필 클릭
    is_entered = home_page.click_feed_profile()
    assert is_entered == True, "프로필 요소 식별 및 클릭에 실패했습니다."

    # 프로필 화면으로 전환될 때까지 애니메이션 대기
    time.sleep(2)

    # 2. 다음 테스트(스토리, DM 등) 진행을 위해 다시 홈 피드로 원복
    print("\n[Action] 프로필 확인 후 홈 피드로 복귀하기 위해 '뒤로 가기'를 수행합니다.")
    driver.back()

    # 홈 피드로 화면이 완전히 돌아올 때까지 대기
    time.sleep(1)


def test_ig_home_009_watch_story(driver):
    print("\n[TC: IG_HOME_009] 홈 화면 상단 스토리 시청 검증 시작")

    home_page = HomePage(driver)

    # 1. 사전 작업: 이전 테스트에서 내려온 피드를 단숨에 최상단으로 복구 (홈 탭 클릭)
    is_top_moved = home_page.click_home_tab_to_top()
    assert is_top_moved == True, "홈 탭 클릭을 통한 최상단 이동에 실패했습니다."

    # 최상단으로 스크롤이 올라가고 스토리 트레이가 렌더링될 때까지 대기
    time.sleep(2)

    # 2. 친구 스토리 클릭 (내 스토리 진입 방지 로직 적용)
    is_watched = home_page.click_friend_story()
    assert is_watched == True, "스토리 트레이 요소 식별 및 진입에 실패했습니다."

    # 3. 스토리 시청 상태 유지 (3초 시청)
    time.sleep(3)

    # 4. 스토리 닫기 및 홈 화면 복귀
    print("\n[Action] 스토리 시청을 종료하고 홈 피드로 복귀하기 위해 시스템 '뒤로 가기'를 수행합니다.")
    driver.back()

    # 화면이 완전히 닫히고 복귀될 때까지 대기
    time.sleep(1)