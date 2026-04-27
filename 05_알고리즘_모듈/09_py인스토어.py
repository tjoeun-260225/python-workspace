'''
PyInstaller
- 파이썬 파일을 다른 사람도 실행할 수 있는 파일로 변환해주는 도구
- PyInstaller로 만든 exe 파일은 파이썬 없이도 실행 가능

만들어진 파일은 dist 폴더 생성되며, build 폴더와 spec 은 exe 파일을 만들기 위한 중간단계 명세서
spec 만 있어도 exe 파일을 언제든지 다시 만들 수 있다.
pip install pyinstaller

속성
--onfile 은 하나의 파일로 작업할 수 있게 해주는 속성
--noconsole 검정 cmd 화면 없애기
--name=""   exe 파일 명칭 붙이기
--icon=아이콘.ico 하면 아이콘 변경 가능

-- 윈도우에서 만들면 윈도우용 파일, 맥에서 만들면 맥북용 파일 생성

cmd 창에서 작성할 명령어
pyinstaller --onfile --noconsole py파일이름.py
'''
