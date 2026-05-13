# Q1. 역색인(Inverted Index)이 일반 색인보다 검색이 빠른 이유를 한 문장으로 설명해 보세요.
# 답: 일반 색인은 문서를 하나씩 열어서 단어를 찾지만, 역색인은 단어 기준 검색
#
# Q2. Elasticsearch의 Index / Document / Field 를 RDB 용어로 각각 뭐라고 부르나요?
# 답: Index = Table, Document = Row, Field = Column
#
# Q3. match 검색과 term 검색의 차이는 무엇인가요? (힌트: 형태소 분석)
# 답: match 형태소 분석을 거쳐서 검새
#     term  형태소 분석 없이 입력한 값과 정확히 일치하는 것만 찾음
#     text  필드는 match keyword 필드는 term 사용

# Q4. docker compose down 과 docker compose stop 의 차이는 무엇인가요?
# 답: stop → 컨테이너를 중지 / 컨테이넌 삭제되지 않고 중지만 하는상태
#     down → 컨테이너를 중지하고 삭제까지 한다. 다시 실행하려면 새로 만들어야 한다.