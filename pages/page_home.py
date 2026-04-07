import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # 명시적 대기(Explicit Wait)의 기본 최대 시간을 5초에서 3초로 단축하여 빠른 실패 유도
        self.wait = WebDriverWait(self.driver, 3)

        # 1. 요소의 이름표(Locator) 저장
        self.logo_id = (AppiumBy.ID, 'com.instagram.android:id/title_logo')
        self.like_button_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_button_like')
        self.save_button_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_button_save')
        self.comment_button_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_button_comment')
        self.comment_sheet_id = (AppiumBy.ID, 'android:id/list')
        self.feed_profile_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_photo_profile_name')
        self.home_tab_id = (AppiumBy.ID, 'com.instagram.android:id/tab_icon')
        self.story_avatar_id = (AppiumBy.ID, 'com.instagram.android:id/avatar_image_view')

    def check_logo_is_visible(self):
        print("\n[Action] 로고 노출 확인")
        try:
            self.wait.until(EC.presence_of_element_located(self.logo_id))
            return True
        except:
            return False

    def swipe_down_to_refresh(self):
        print("\n[Action] 홈 화면 새로고침(Pull-to-Refresh)")
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.3
        end_x = size['width'] / 2
        end_y = size['height'] * 0.8

        # [최적화] 1000ms(1초) -> 400ms(0.4초)로 스와이프 속도 단축
        self.driver.swipe(start_x, start_y, end_x, end_y, 400)

    def scroll_down_feed(self):
        print("\n[Action] 피드 스크롤 다운")
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.8
        end_x = size['width'] / 2
        end_y = size['height'] * 0.3

        # [최적화] 1000ms(1초) -> 300ms(0.3초)로 스와이프 속도 대폭 단축
        self.driver.swipe(start_x, start_y, end_x, end_y, 300)

    def click_like_button(self):
        print("\n[Action] 좋아요 버튼 클릭")
        try:
            like_btn = self.wait.until(EC.element_to_be_clickable(self.like_button_id))
            like_btn.click()
            return True
        except Exception:
            return False

    def cancel_like(self):
        print("\n[Action] 좋아요 취소")
        try:
            like_btn = self.wait.until(EC.element_to_be_clickable(self.like_button_id))
            like_btn.click()
            return True
        except Exception:
            return False

    def click_save_button(self):
        print("\n[Action] 북마크 버튼 클릭")
        try:
            save_btn = self.wait.until(EC.element_to_be_clickable(self.save_button_id))
            save_btn.click()
            return True
        except Exception:
            return False

    def click_comment_button(self):
        print("\n[Action] 댓글 아이콘 클릭")
        try:
            comment_btn = self.wait.until(EC.element_to_be_clickable(self.comment_button_id))
            comment_btn.click()
            return True
        except Exception:
            return False

    def check_comment_sheet_is_visible(self):
        print("\n[Action] 댓글 바텀 시트 검증")
        try:
            self.wait.until(EC.presence_of_element_located(self.comment_sheet_id))
            return True
        except Exception:
            return False

    def close_bottom_sheet(self):
        print("\n[Action] 바텀 시트 종료")
        try:
            self.driver.back()
            # [최적화] OS 키보드/시트 내려가는 대기 시간 단축: 1초 -> 0.3초
            time.sleep(0.3)
            self.driver.back()
            return True
        except Exception:
            return False

    def click_feed_profile(self):
        print("\n[Action] 작성자 프로필 진입")
        try:
            profile_elem = self.wait.until(EC.element_to_be_clickable(self.feed_profile_id))
            profile_elem.click()
            return True
        except Exception:
            return False

    def click_home_tab_to_top(self):
        print("\n[Action] 홈 탭 클릭 (최상단 이동)")
        try:
            tab_elems = self.wait.until(EC.presence_of_all_elements_located(self.home_tab_id))
            tab_elems[0].click()
            return True
        except Exception:
            return False

    def click_friend_story(self):
        print("\n[Action] 친구 스토리 시청")
        try:
            story_elems = self.wait.until(EC.presence_of_all_elements_located(self.story_avatar_id))
            if len(story_elems) > 1:
                story_elems[1].click()
            else:
                story_elems[0].click()
            return True
        except Exception:
            return False