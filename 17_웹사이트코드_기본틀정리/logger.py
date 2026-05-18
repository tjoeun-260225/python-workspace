import logging
import json
from datetime import datetime, timezone
from pathlib import Path
'''
class = 관련 기능들을 하나로 묶은 명칭
class JsonFormatter 는 JSON 으로 포맷하는 방법을 정의한 틀

def = 단순히 기능 하나
def get_logger      는 로거(=기록) 하나 만들어줘 라는 함수(=기능)

둘을 class 와 def 로 나눈 이유는 
    JsonFormatter 는 Python 로깅이 내부적으로 format() 메서드를 호출하는 규칙이 있다.
        반드시 class로 만들어서 내부에 format()을 작성해야한다.
        
    Python 자체적으로 log 를 출력할 때 class 내에 format() 으로 되어있는 기능을 가져와 라고 코드가 작성되어 있다.
        
        
Python logging : format() 이 작성된 문서(=class) 가져와
def          format() → format()               가져왔어요 → Python : 기능 말고 기능이 들어있는 class 가져오라고 error 발생
class JsonFormatter   → 이 클래스 안에 format() 이 있어요 → Python : ok ok 이대로 기록 진행할게요~
기록이라 하는 것은 회사나 개발 규모에 따라 방법이 매우 다양하기 때문에
파이썬에서 기록을 할 수 있는 어느정도의 틀을 회사나 개발자에 요구하는 것이고
회사나 개발자는 파이썬이 기록을 위하여 기록하기 위한 틀을 제공해야할 의무가 있다.
'''
# 로그(=클라이언트가 활동한 모든 기록) 저장할 폴더 생성
Path("logs").mkdir(exist_ok=True) # logs 라는 폴더가 있으면 건너뛰기 없으면 생성

class JsonFormatter(logging.Formatter):
    """Filebeat가 바로 파싱할 수 있는 JSON 형태로 출력"""
    def format(self, record):
        log_obj = {
            "@timestamp": datetime.now(timezone.utc).isoformat(),
            "log.level": record.levelname, # INFO / WARNING / ERROR
            "message": record.getMessage(),
            "logger": record.name,
            "file": record.filename,
            "line": record.lineno,
            "service": "order-app",        # kibana 필터용 관리자가 확인할 수 있는 명칭 작성
        }
        # 에러가 발생했을 때 부터 에러 발생을 관리하기 위한 기록 작성해야할 때가 생긴다.
        # 0으로 숫자 나눌 때 에러 발생하는 것과 같은 상황을 따로 기록해서 관리하기 위한 수단
        # try:
        #   1 / 0
        # except ZeroDivisionError:
        #   log.error("0으로는 숫자를 나눌 수 없습니다.", exc_info=True)
        # exc_info = 어디서 왜 터졌는지 에 대한 정보를 로그에 같이 담는 옵션 에러 종류 / 에러 메세지 / 어느파일 몇번째 줄에서 터졌는가
        if record.exc_info:
            log_obj["error.stack_trace"] = self.formatException(record.exc_info)
        # record.__dict__ = 기록 한 줄에 모든 정보가 담긴 딕셔너리 (딕셔너리 = 사전)
        # log.info() 를 호출하면 record 에 자동으로
        # 이름, 로그레벨, 메세지, 어떤파일, 어느라인, ... 모든 값들이 기록
        # record 안에는 쓸모없는 내부 변수가 너무 많아서, 개발자가 넘긴 것만 구분하기 위하여 x_
        # record 안에서 x_ = 개발자가 만든 파일로 인하여 와 같은 속성 설정되어 있다.
        for key, value in record.__dict__.items():
            if key.startswith("x_"): # x_ 로 시작하면 자동으로 포함
                log_obj[key[2:]] = value # x_user 개발자가 만든 user 에서 x_ 를 제외하고 다시 기록하겠다.
                # 기록에서 x_user -> x_ 를 제거하고 user: 000 과 같이 기록하겠다.
        return  json.dumps(log_obj, ensure_ascii=False)
        '''
        record = 기록
        log    = 기록하다 (동사)
        log record = 기록 한 건 (명사)
        
        병원 진료기록부 → medical record
        범   죄  기  록 → criminal record
        로그  기록  1건 → log record
        
        Python 에서 logging 에서의 의미
        개발자가 아래와 같은 코드 작성
        log.info("주문 생성") → 소비자가 주문한거 기록해줘
        
        Python → 알겠어. 기록(record) 만들게
                record = {
                    메세지, 시간, 파일명, 줄번호, 심각도, 보낸 함수() ....
                }
        개발자가 로그 한 줄 찍을 때마다 그 내용을 담은 기록 객체가 생성되는 것
        '''



# 고급 문법
# -> logging.Logger
# 기능만들기   함수이름   받는값:타입힌트             반환값 타입힌트
#   def       get_logger(  name:  str)           -> logging.Logger:
# name: str         = name은 문자열(str)을 넣어야 한다고 알려주는 타입 힌트
# -> logging.Logger = 이 함수가 Logger 객체를 반환한다고 알려주는 타입 힌트
# 타입 힌트는 강제가 아니라 개발자끼리의 약속 / 없어도 동작한다.
# ai 가 아래와 같은 방식을 알려줄 경우   -> logging.Logger 방식을 제외하고 알려줘! 요청
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name) # 내장 로깅 시스템에서 로그 가져오기
    if logger.handlers:              # 중복으로 가져오지말고 로그가 붙어있는 값 바로 반환
        return logger

    logger.setLevel(logging.DEBUG)   # 어느 레벨로부터 기록할지 설정 DEBUG < INFO < WARNING < ERROR < CRITICAL

    # 파일 핸들러(Filebeat 가 읽을 파일)
    fh = logging.FileHandler("logs/app.log",encoding="utf-8") # logs/app.log 파일에 로그를 기록하는 핸들러
    # 추후 Filebeat 가 위 파일을 읽을 예정
    fh.setFormatter(JsonFormatter) # 각 py나 환경에서 가져온 데이터를 JSON 형태로 작성
    logger.addHandler(fh)           # 위 설정을 통하여 기록 시작

    # 콘솔 핸들러(개발 중 터미널 확인용)
    ch = logging.StreamHandler()     # log 기록을 터미널에서도 출력하며 확인하는 용도
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(name)s - %(message)s"))
    # 터미널에서 어떤 형태로 출력할지 개발자가 원하는 형태로 세팅
    # [%(levelname)s] %(name)s - %(message)s = [INFO] routes - ES 검색 완료 와 같이 표기
    logger.addHandler(ch)           # 위 설정을 통하여 터미널에도 기록 시작

    return logger












