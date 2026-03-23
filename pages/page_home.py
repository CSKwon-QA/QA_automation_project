# pages/page_home.py

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # 1. 요소의 이름표(Locator) 저장
        self.logo_id = (AppiumBy.ID, 'com.instagram.android:id/title_logo')
        self.like_button_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_button_like')
        self.save_button_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_button_save')
        self.comment_button_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_button_comment')
        self.comment_sheet_id = (AppiumBy.ID, 'android:id/list')
        self.feed_profile_id = (AppiumBy.ID, 'com.instagram.android:id/row_feed_photo_profile_name')
        self.home_tab_id = (AppiumBy.ID, 'com.instagram.android:id/tab_icon')
        self.story_avatar_id = (AppiumBy.ID, 'com.instagram.android:id/avatar_image_view')

    # 2. 요소가 있는지 확인하는 행동(Method) 정의
    def check_logo_is_visible(self):
        print("\n 로고가 화면에 나타날 때까지 최대 5초 기다립니다...")
        try:
            # 로고가 뜰 때까지만 기다리는 '명시적 대기(Explicit Wait)'
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.logo_id)
            )
            print("인스타그램 로고 발견 성공")
            return True
        except:
            print("5초가 지나도 로고를 찾을 수 없습니다.")
            return False

    def swipe_down_to_refresh(self):
        print("\n[Action] 홈 화면 새로고침(Pull-to-Refresh) 스와이프를 수행합니다.")

        # 현재 연결된 기기의 화면 전체 크기(가로, 세로)를 가져옵니다.
        size = self.driver.get_window_size()

        # 화면 중앙 상단에서 하단으로 스와이프하기 위한 좌표 비율 계산
        start_x = size['width'] / 2
        start_y = size['height'] * 0.3  # 화면 상단 30% 지점
        end_x = size['width'] / 2
        end_y = size['height'] * 0.8  # 화면 하단 80% 지점

        # 계산된 좌표를 바탕으로 스와이프 실행 (1000ms = 1초 동안 드래그)
        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def scroll_down_feed(self):
        print("\n[Action] 홈 화면 피드를 아래로 스크롤합니다.")

        size = self.driver.get_window_size()

        # 화면 하단에서 상단으로 스와이프하기 위한 좌표 비율 계산
        start_x = size['width'] / 2
        start_y = size['height'] * 0.8  # 화면 하단 80% 지점에서 시작
        end_x = size['width'] / 2
        end_y = size['height'] * 0.3  # 화면 상단 30% 지점에서 끝남

        # 스와이프 실행
        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def click_like_button(self):
        print("\n[Action] 첫 번째 게시물의 좋아요 버튼을 클릭합니다.")
        try:
            # 버튼이 화면에 나타나고 클릭 가능해질 때까지 최대 5초 대기
            like_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.like_button_id)
            )
            like_btn.click()
            print("[Check] 좋아요 버튼 클릭 완료")
            return True
        except Exception as e:
            print(f"[Error] 좋아요 버튼을 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False

    def cancel_like(self):
        print("\n[Action] 활성화된 좋아요 버튼을 다시 클릭하여 취소합니다.")
        try:
            like_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.like_button_id)
            )
            like_btn.click()
            print("[Check] 좋아요 취소 클릭 완료")
            return True
        except Exception as e:
            print(f"[Error] 활성화된 좋아요 버튼을 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False

    def click_save_button(self):
        print("\n[Action] 게시물의 북마크(저장) 버튼을 클릭합니다.")
        try:
            save_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.save_button_id)
            )
            save_btn.click()
            print("[Check] 북마크 버튼 클릭 완료")
            return True
        except Exception as e:
            print(f"[Error] 북마크 버튼을 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False

    def click_comment_button(self):
        print("\n[Action] 피드 게시물의 댓글 아이콘을 클릭합니다.")
        try:
            comment_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.comment_button_id)
            )
            comment_btn.click()
            print("[Check] 댓글 창 호출 클릭 완료")
            return True
        except Exception as e:
            print(f"[Error] 댓글 버튼을 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False

    def check_comment_sheet_is_visible(self):
        print("\n[Action] 댓글 바텀 시트 노출 상태를 검증합니다.")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.comment_sheet_id)
            )
            print("[Check] 댓글 바텀 시트 정상 노출 확인")
            return True
        except Exception:
            print("[Error] 지정된 시간 내에 바텀 시트가 노출되지 않았습니다.")
            return False

    def close_bottom_sheet(self):
        print("\n[Action] 시스템 '뒤로 가기' 2회 호출 (키보드 및 시트 종료).")
        try:
            # 첫 번째 뒤로 가기: OS 키보드 내리기
            self.driver.back()
            time.sleep(1)
            # 두 번째 뒤로 가기: 바텀 시트 닫기
            self.driver.back()
            print("[Check] 바텀 시트 종료 완료")
            return True
        except Exception as e:
            print(f"[Error] 바텀 시트 종료 액션 실패: {e}")
            return False

    def click_feed_profile(self):
        print("\n[Action] 피드 게시물 작성자의 프로필을 클릭하여 진입합니다.")
        try:
            profile_elem = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.feed_profile_id)
            )
            profile_elem.click()
            print("[Check] 게시물 작성자 프로필 클릭 완료")
            return True
        except Exception as e:
            print(f"[Error] 프로필 요소를 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False

    def click_home_tab_to_top(self):
        print("\n[Action] 하단 네비게이션 바의 '홈' 탭을 클릭하여 피드 최상단으로 이동합니다.")
        try:
            # 하단 탭 아이콘들을 모두 찾아 리스트로 가져온 뒤, 첫 번째(인덱스 0) '홈' 탭을 클릭합니다.
            tab_elems = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.home_tab_id)
            )
            tab_elems[0].click()
            print("[Check] 홈 탭 클릭 및 최상단 이동 완료")
            return True
        except Exception as e:
            print(f"[Error] 홈 탭 요소를 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False

    def click_friend_story(self):
        print("\n[Action] 상단 스토리 트레이에서 친구의 스토리를 클릭합니다.")
        try:
            # 스토리 동그라미들을 모두 리스트로 가져옵니다.
            story_elems = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.story_avatar_id)
            )
            # 0번 인덱스는 '내 스토리(Your Story)'이므로, 1번 인덱스(첫 번째 친구 스토리)를 클릭합니다.
            if len(story_elems) > 1:
                story_elems[1].click()
            else:
                # 만약 친구 스토리가 하나도 없다면 예외적으로 첫 번째를 클릭합니다.
                story_elems[0].click()

            print("[Check] 스토리 진입 완료")
            return True
        except Exception as e:
            print(f"[Error] 스토리를 찾을 수 없거나 클릭할 수 없습니다: {e}")
            return False