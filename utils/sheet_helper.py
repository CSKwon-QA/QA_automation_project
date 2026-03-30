import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime


def write_result_to_sheet(tc_id, result):
    """
    미리 작성된 구글 시트에서 TC ID를 검색하여,
    해당 행(Row)의 결과(C열)와 실행 시간(D열)을 업데이트하는 함수
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    try:
        # 1. API 인증 및 구글 시트 파일 열기
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open("QA_Automation_Result").sheet1

        try:
            # 2. 시트 전체에서 tc_id (예: IG_HOME_001) 검색
            cell = sheet.find(tc_id)
            row_num = cell.row  # 찾은 TC ID가 몇 번째 줄(행)에 있는지 확인

            # 3. 현재 시간 가져오기
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 4. 해당 행의 7열(G칸)에 결과, 8열(H칸)에 시간 업데이트
            sheet.update_cell(row_num, 7, result)
            sheet.update_cell(row_num, 8, current_time)

            print(f"[Google Sheets] 결과 업데이트 완료: [{tc_id}] {result}")

        except gspread.exceptions.CellNotFound:
            # 시트에 해당 TC ID가 미리 적혀있지 않은 경우 에러 처리
            print(f"[Error] 시트에서 {tc_id} 항목을 찾을 수 없습니다. TC ID를 확인해주세요.")

    except Exception as e:
        print(f"[Error] 구글 시트 통신 중 오류 발생: {e}")