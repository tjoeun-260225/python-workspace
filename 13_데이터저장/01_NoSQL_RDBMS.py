'''
RDBMS
- 관계형 데이터 베이스 (= 표 형태의 데이터 베이스)
- 수학적으로 관계 = 표 = 틀 형태
- Table, Row, Column, Join, 스키마 고정
- Oracle, Mysql, MariaDB, SQLite, PostgreSql 대부분의 sql


NoSQL
- Not Only SQL
- SQL만 사용하는게 아니다.
- 2000년대 초 - 인터넷이 폭발적으로 성장 Mysql 같은 전통 DB가 무거워 버티지 못하는 현상 발생
- 구글, 아마존이 자체 DB를 만들기 시작
- 2009년 Johan Oskarsson 개발자가 새로운 DB들을 모아서 발표하는 모임 열었음
         트위터 해시태그로 짧은 이름이 필요했고, 그때 #NoSQL 을 작성
- 마케팅 / 해시태그 용으로 즉흥적으로 만든 이름이 전 세계 표준 용어가 된 것

NoSQL은 종류별로 나뉨
- 문서형(Document) = JSON 문서로 저장
   MongoDB, Firbase FireStore(Google), CouchDB

- 키-값형(Key-Value) = 딕셔너리처럼 Key:Value 만 저장, 엄청 빠름
   Redis(캐싱용으로 거의 모든 회사 사용), DynamoDB(AWS)

- 컬럼형(Column) = 대용량 데이터 분석에 강함
   Cassandra(넷플리스, 인스타그램이 사용), HBase

- 그래프형(Graph) = 관계 / 연결 데이터에 특화
   Neo4j(친구추천, 사기탐지 같은 곳에서 사용)

요약
MongoDB    : 일반백엔드 스타트업
Redis      : 세션, 캐싱, 실시간
Cassandra  : 로그, 대용량 시계열
DynamoDB   : AWS 인프라 기반 서비스
'''














