'''
Index = Table
Document = Row
Field = Column
Shard = 분산 조각
Node = 서버 1대
Cluster = Node 들의 집합 / 포도송이 처럼 묶인 서버 무리

text    = 형태소 분석 o 문장 긴 글 검색      상품명 상품 설명 에서 조회할 때 사용
keyword = 형태소 분석 x 정확히 일치해야할 때 카테고리 / 브랜드
integer = 정  수 숫자                       가격 / 재고
float   = 실  수 숫자                       평점
date    = 날  짜                            등록일

 es.indices.create(index="pokemon", body={
        "mappings": {
            "properties": {
                "name": {"type": "text"},    # match 검색용
                "type": {"type": "keyword"}, # term  검색용
                "desc": {"type": "text"},    # match 검색용
            }
        }
    })

es.search(index="pokemon", body={"query": {"match_all": {}}})
es.get(index="pokemon", id=4) # id에 정확히 어떤 데이터가 들어있는지 100% 알고 있을 때
# 네이버쇼핑 기준으로 12913569330 이 상품이 무엇인지 소비자가 100% 알고 있을 때 사용
# get 을 쓸 때는 개발자가 id 일부 데이터를 조회하고 코드 수정하거나 코드 상태 확인할 때 사용

# 소비자가 작성한 검색 기준으로 데이터 제공
# 주로 소비자는 검색 = search() 을 할 것!
# 코드에서 자주 사용하게 될 것은 search()
# search 내부에는 term match match_all 과 같은 검색관련 기능 내장






역색인 - 단어 기준 조회 - 어느 문서에 있는지 확인

쿼리 DSL = match match_all term range bool 페이지네이션 코드
DSL(Domain Specific Language) = 엘라스틱 서치에서 검색할 때 JSON 형식의 검색 문법
-- Domain   : 분야 영역
-- Specific : 특화된 , 그것만을 위한
-- Language : 언어
엘라스틱서치만의 기능언어들



create() - nosql json 형태를 생성 sql table 생성하는 것과 같은 기능
index()  - nosql json 데이터 추가 sql table 내에 데이터 저장하는 것과 같은 기능
get()    - id로 직접 데이터를 꺼내는 방식 색인 필요없이 바로 조회
search() - 역색인 테이블을 검색하는 거라 색인이 완료되어야 나온다.
         - 바로 search 를 이용해서 데이터 추가된 것을 조회하고 싶다면
           search() 전에 refresh() 새로고침 작업을 해주어야 한다.
'''

from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# 1. 연결 확인
# ping - pong  ping - pong 주고 받으며 연결상태 확인하는 기능
print(es.ping())  # True 답변이 오면 연결 성공

# 2. 인덱스 생성(매핑 포함)
def 인덱스생성():
    print("======================== 인덱스 생성 시작 ========================")
    es.indices.create(index="pokemon", body={
        "mappings": {  # mapper.xml 과 비슷하다.
            "properties": {  # create 해주는 table () 와 비슷하다.
                "name": {"type": "text"},  # 형태소 분석 o → match 검색용  컬럼이름 : {컬럼속성:컬럼도메인}
                "type": {"type": "keyword"},  # 형태소 분석 x → term  검색용  컬럼이름 : {컬럼속성:컬럼도메인}
                "hp": {"type": "integer"},  # 숫         자 → range 검색용
                "desc": {"type": "text"},  # 형태소 분석 o → match 검색용  컬럼이름 : {컬럼속성:컬럼도메인}
            }
        }
    })
    print("======================== 인덱스 생성 완료 ========================")

# 3. 문서 넣기
def 데이터저장():
    print("======================== 데이터 저장 시작 ========================")
    es.index(index="pokemon", id=1, body={"name": "이상해씨", "type": "풀", "hp": 45, "desc": "등에 씨앗이 있다"})
    es.index(index="pokemon", id=4, body={"name": "파이리", "type": "불꽃", "hp": 39, "desc": "꼬리 끝 불꽃이 생명력을 나타낸다"})
    es.index(index="pokemon", id=7, body={"name": "꼬부기", "type": "물", "hp": 44, "desc": "등껍질로 적의 공격을 막는다"})
    es.index(index="pokemon", id=25, body={"name": "피카츄", "type": "전기", "hp": 35, "desc": "볼 주머니에서 전기를 방전한다"})
    es.index(index="pokemon", id=6, body={"name": "리자몽", "type": "불꽃", "hp": 78, "desc": "날개로 날며 강력한 불꽃을 내뿜는다"})
    es.index(index="pokemon", id=9, body={"name": "거북왕", "type": "물", "hp": 79, "desc": "대포로 물대포를 쏜다"})
    print("======================== 데이터 저장 완료 ========================")
# 4. 문서 조회(Read)
# id 로 한 개 조회
# 4번 째에 존재하는 데이터 조회
def 데이터일부조회():
    print("======================== 데이터 하나 조회 시작 ========================")
    result = es.get(index="pokemon", id=4)
    print(result["_source"])
    # {'name': '파이리', 'type': '불꽃', 'hp': 39, 'desc': '꼬리 끝 불꽃이 생명력을 나타낸다'}
    print("======================== 데이터 하나 조회 완료 ========================")

# 전체 조회
# 4-1. for 문을 이용한 전체 조회
def 데이터전체조회():
    print("======================== 데이터 전체 조회 시작 ========================")
    result = es.search(index="pokemon", body={"query": {"match_all": {}}})
    print(result)
    '''
    ################### refresh 를 넣지 않아 데이터가 조회되지 않은 상태 ###################
    {
    'took': 1, 
    'timed_out': False, 
    '_shards': {
        'total': 1, 
        'successful': 1, 
        'skipped': 0, 
        'failed': 0
        }, 
    'hits': 
        {
            'total': 
                {
                    'value': 0, 
                    'relation': 
                    'eq'
                }, 
            'max_score': None, 
            'hits': []}
        }
    
    
################### refresh 를 넣지 않고, 어느정도 형태소 정리가 끝난다음 데이터 전체 조회 ###################
{
'took': 1,                  # 검색 걸린 시간 ms
'timed_out': False,         # 타임 아웃 여부
'_shards': {                # 샤드 처리 결과 (데이터 처리 결과)
        'total': 1,       
        'successful': 1, 
        'skipped': 0, 
        'failed': 0
}, 
'hits': {                 # 실제 검색 결과
    'total':{
        value': 6,        # 총 문서 수
        'relation': 'eq'
        }, 
    'max_score': 1.0, 
    'hits': [            # 실제 데이터 배열
    {
        '_index': 'pokemon', 
        '_id': '1', 
        '_score': 1.0, 
        '_source': {
            'name': '이상해씨', 
            'type': '풀', 
            'hp': 45, 
            'desc': '등에 씨앗이 있다'
        }
    }, {
        '_index': 'pokemon', 
        '_id': '4', 
        '_score': 1.0, 
        '_source': {
            'name': '파이리', 
            'type': '불꽃', 
            'hp': 39, 
            'desc': '꼬리 끝 불꽃이 생명력을 나타낸다'
        }
    }, {
        '_index': 'pokemon', 
        '_id': '7', 
        '_score': 1.0, 
        '_source': {
            'name': '꼬부기', 
            'type': '물', 
            'hp': 44, 
            'desc': '등껍질로 적의 공격을 막는다'
            }
    }, {'_index': 'pokemon', '_id': '25', '_score': 1.0, '_source': {'name': '피카츄', 'type': '전기', 'hp': 35, 'desc': '볼 주머니에서 전기를 방전한다'}}, {'_index': 'pokemon', '_id': '6', '_score': 1.0, '_source': {'name': '리자몽', 'type': '불꽃', 'hp': 78, 'desc': '날개로 날며 강력한 불꽃을 내뿜는다'}}, {'_index': 'pokemon', '_id': '9', '_score': 1.0, '_source': {'name': '거북왕', 'type': '물', 'hp': 79, 'desc': '대포로 물대포를 쏜다'}}]}}
    '''
    print("======================== 데이터 전체 조회 완료 ========================")

#데이터전체조회()
def 하나씩_꺼내서_전체데이터_조회():
    전체조회데이터 = es.search(index="pokemon", body={"query": {"match_all": {}}})
    for 데이터한개 in 전체조회데이터["hits"]["hits"]:
        print(데이터한개["_source"])
       # print(전체조회데이터["hits"]["hits"]["_source"])

    '''
    'hits': {                 # 실제 검색 결과
        'hits': [            # 실제 데이터 배열
        {   '_source': {
                'name': '이상해씨', 
                'type': '풀', 
                'hp': 45, 
                'desc': '등에 씨앗이 있다'
            }
        }
    '''


# 데이터 조회 정리
def 데이터조회정리():
    es.get(index="pokemon", id=4)
    # get table 에서 id 하나만 작성해서 개발자가 데이터 구조확인이나 id 로 특수 작업 진행할 때 사용

    es.search(index="pokemon", body={"query": {"match_all": {}}})
    # search(     table 에서   소비자가 원하는데이터를 조회할 때 사용
    #                                               조회할 때 카테고리 / 브랜드 처럼 단어가 명확한가?
    #                                               제목이나 설명에서 단어를 찾아야 하는가?
    #                                               데이터를 하나 찾아서 수정해야하는가? 와 같은 작업
# 4-2 bulk 를 이용하는 전체 조회 (응용)
