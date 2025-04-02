import asyncio
import websockets
import json

async def test_websocket(req, data, uri):
    print(f"💁‍♂️{req} 요청")
    async with websockets.connect(uri) as websocket:
        # JSON 데이터 전송
        await websocket.send(json.dumps(data))
        print("✅데이터 전송 완료")

        # 서버의 응답 대기
        response = await websocket.recv()
        response = response.encode('utf-8').decode('unicode_escape')
        print("서버 응답:", response)

if __name__ == "__main__":
    # baseurl = "ws://35.239.36.53:8000/"
    baseurl = "ws://localhost:8000/"
    # 보낼 JSON 데이터 구성
    # 로그인
    data = {
      "login_type": "kakao",
      "user_id": "dummy@kakao.com",
      "user_pw": "dummy_password",
      "access_token": "dummy_access_token"
    }
    asyncio.run(test_websocket("로그인", data, baseurl + "api/auth/login"))
    # 회원가입
    data = {
        "login_type": "kakao",
        "user_name": "홍길동",
        "user_ID": "Hongildon@kakao.com",
        "user_PW": "",
        "access_token": "sdfjklweru38249",
        "user_birth_date": "1996-03-04",
        "user_education_level": 2,
        "desired_company": 0,
        "desired_job": "dev_2//3//5",
        "job_prep_period_year": 1,
        "job_prep_period_month": 5,
        "job_prep_status": "0//1//5",
        "job_difficulties": "3//6//8//9//10",
        "interested_routine": True
    }
    asyncio.run(test_websocket("회원가입", data, baseurl + "api/register"))
    # 사용자 정보
    data = {
        "user_key": "dummy_key_001",
        "user_name": "홍길동"
    }
    asyncio.run(test_websocket("사용자 정보", data, baseurl + "api/user-info"))
    # 루틴 리스트
    data = {
        "user_key": "dummy_key_001",
        "user_name": "홍길동",
        "request_date": "2025-03-19"
    }
    asyncio.run(test_websocket("루틴 리스트", data, baseurl + "api/routine_list"))
    # 루틴 추가
    data = {
        "user_key": "dummy_user_001",
        "task_name": "Morning Workout",
        "task_category": "Fitness",
        "repeat_type": "daily",
        "execute_days": ["Monday", "Wednesday", "Friday"],
        "execute_description": "Perform a 30-minute workout session",
        "execute_time": "06:30:00",  # 시간은 HH:MM:SS 형식의 문자열로 제공
        "use_timer": True,
        "time_filter": 15,
        "start_date": "2025-03-19"
    }
    asyncio.run(test_websocket("루틴 추가", data, baseurl + "api/task/add"))
    # 성공 루틴
    data = {
        "user_key": "dummy_user_001",
        "user_name": "홍길동",
        "success_user_id": "success_id_001"
    }
    asyncio.run(test_websocket("성공 루틴", data, baseurl + "api/success_routine"))
    # 성공 루틴 좋아요
    data = {
        "user_key": "dummy_user_001",
        "user_name": "홍길동",
        "success_user_id": "success_id_001",
        "liked": True
    }
    asyncio.run(test_websocket("성공 루틴 좋아요", data, baseurl + "api/success_routine_like"))
    # 성공 루틴 가져오기
    data = {
        "user_key": "dummy_user_001",
        "success_user_id": "success_id_001",
        "copy_type": "full"
    }
    asyncio.run(test_websocket("성공 루틴 가져오기", data, baseurl + "api/success_routine_copy"))
    # 주간 통계
    data = {
        "user_key": "dummy_user_001",
        "statistics_type": "weekly",
        "start_date": "2025-03-19",
        "end_date": "2025-03-25"
    }
    asyncio.run(test_websocket("주간 통계", data, baseurl + "api/statistic/weekly"))
    # 월간 통계
    data = {
        "user_key": "dummy_user_001",
        "statistics_type": "monthly",
        "month": "2025-03-01"  # 날짜 형식의 문자열로 제공
    }
    asyncio.run(test_websocket("월간 통계", data, baseurl + "api/statistic/monthly"))
    # 프로필 조회
    data = {
        "user_key": "dummy_user_001",
        "user_name": "홍길동"
    }
    asyncio.run(test_websocket("프로필 조회", data, baseurl + "api/user/profile"))
    # 프로필 수정
    data = {
        "user_key": "dummy_user_001",
        "user_name": "홍길동",
        "profile_image": "https://example.com/profile.jpg",
        "bio": "This is a sample bio for testing."
    }
    asyncio.run(test_websocket("프로필 수정", data, baseurl + "api/user/profile/update"))