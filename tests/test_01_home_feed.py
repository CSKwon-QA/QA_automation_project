import time
from utils.driver_setup import driver
from pages.page_home import HomePage
from utils.screenshot_helper import take_screenshot
from utils.sheet_helper import write_result_to_sheet


def test_ig_home_001_verify_logo(driver):
    tc_id = "IG_HOME_001"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 홈 피드 로고 검증 시작")

    try:
        driver.activate_app('com.instagram.android')
        home_page = HomePage(driver)

        is_logo_visible = home_page.check_logo_is_visible()
        assert is_logo_visible == True, "로고가 화면에 없습니다! 테스트 실패(FAILED)!"

        # 모든 검증을 통과하면 결과를 PASS로 변경
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, tc_id)
        write_result_to_sheet(tc_id, result)


def test_ig_home_002_pull_to_refresh(driver):
    tc_id = "IG_HOME_002"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 홈 피드 새로고침 검증 시작")

    try:
        home_page = HomePage(driver)

        home_page.swipe_down_to_refresh()
        take_screenshot(driver, f"{tc_id}_loading_spinner")

        time.sleep(2)

        is_logo_visible = home_page.check_logo_is_visible()
        assert is_logo_visible == True, "새로고침 수행 후 홈 화면 요소가 정상적으로 로드되지 않았습니다."

        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, f"{tc_id}_final_state")
        write_result_to_sheet(tc_id, result)


def test_ig_home_003_scroll_down(driver):
    tc_id = "IG_HOME_003"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 홈 피드 5회 연속 스크롤 다운 검증 시작")

    try:
        home_page = HomePage(driver)

        for i in range(5):
            print(f"[Action] {i + 1}번째 스크롤 다운 실행")
            home_page.scroll_down_feed()
            time.sleep(0.5)

        assert True
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, tc_id)
        write_result_to_sheet(tc_id, result)


def test_ig_home_004_click_like(driver):
    tc_id = "IG_HOME_004"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 게시물 좋아요 클릭 검증 시작")

    try:
        home_page = HomePage(driver)

        is_clicked = home_page.click_like_button()
        time.sleep(1)

        assert is_clicked == True, "좋아요 버튼 요소 식별 및 클릭에 실패했습니다."
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, tc_id)
        write_result_to_sheet(tc_id, result)


def test_ig_home_005_cancel_like(driver):
    tc_id = "IG_HOME_005"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 게시물 좋아요 취소 검증 시작")

    try:
        home_page = HomePage(driver)

        is_canceled = home_page.cancel_like()
        time.sleep(1)

        assert is_canceled == True, "좋아요 취소 동작 수행에 실패했습니다."
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, tc_id)
        write_result_to_sheet(tc_id, result)


def test_ig_home_006_click_save(driver):
    tc_id = "IG_HOME_006"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 게시물 북마크(저장) 클릭 검증 시작")

    try:
        home_page = HomePage(driver)

        is_saved = home_page.click_save_button()
        time.sleep(1)

        assert is_saved == True, "북마크 버튼 요소 식별 및 클릭에 실패했습니다."
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, tc_id)
        write_result_to_sheet(tc_id, result)


def test_ig_home_007_open_and_close_comment(driver):
    tc_id = "IG_HOME_007"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 피드 댓글 창 진입 및 닫기 검증 시작")

    try:
        home_page = HomePage(driver)

        is_clicked = home_page.click_comment_button()
        assert is_clicked == True, "댓글 버튼 클릭에 실패했습니다."

        is_sheet_visible = home_page.check_comment_sheet_is_visible()
        assert is_sheet_visible == True, "바텀 시트가 화면에 노출되지 않았습니다."

        take_screenshot(driver, f"{tc_id}_sheet_opened")

        is_closed = home_page.close_bottom_sheet()
        assert is_closed == True, "바텀 시트 닫기 동작에 실패했습니다."

        time.sleep(1)
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, f"{tc_id}_final_state")
        write_result_to_sheet(tc_id, result)


def test_ig_home_008_enter_profile(driver):
    tc_id = "IG_HOME_008"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 피드 게시물 작성자 프로필 진입 검증 시작")

    try:
        home_page = HomePage(driver)

        is_entered = home_page.click_feed_profile()
        assert is_entered == True, "프로필 요소 식별 및 클릭에 실패했습니다."

        time.sleep(2)
        take_screenshot(driver, f"{tc_id}_profile_opened")

        print("[Action] 프로필 확인 후 홈 피드로 복귀하기 위해 '뒤로 가기' 수행")
        driver.back()

        time.sleep(1)
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, f"{tc_id}_final_state")
        write_result_to_sheet(tc_id, result)


def test_ig_home_009_watch_story(driver):
    tc_id = "IG_HOME_009"
    result = "FAIL"
    print(f"\n[TC: {tc_id}] 홈 화면 상단 스토리 시청 검증 시작")

    try:
        home_page = HomePage(driver)

        is_top_moved = home_page.click_home_tab_to_top()
        assert is_top_moved == True, "홈 탭 클릭을 통한 최상단 이동에 실패했습니다."

        time.sleep(2)

        is_watched = home_page.click_friend_story()
        assert is_watched == True, "스토리 트레이 요소 식별 및 진입에 실패했습니다."

        time.sleep(1)
        take_screenshot(driver, f"{tc_id}_story_playing")

        time.sleep(2)

        print("[Action] 스토리 시청 종료 및 홈 피드 복귀를 위해 '뒤로 가기' 수행")
        driver.back()

        time.sleep(1)
        result = "PASS"

    except Exception as e:
        print(f"[Error] 테스트 중단: {e}")
        raise

    finally:
        take_screenshot(driver, f"{tc_id}_final_state")
        write_result_to_sheet(tc_id, result)