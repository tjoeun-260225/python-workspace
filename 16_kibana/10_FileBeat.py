''''
Filebeat
- Elastic Stack 의 경량 로그 수집기로 서버의 로그 파일을 모니터링하고
ElasticSearch 나 Logstash로 전달하는 역할

[로그 파일] → [FileBeat] → [Logstash / Elasticsearch] → [Kibana]


구성 요소
1. Input(입력)
로그(=기록)를 어디서 읽을지 정의
filebeat.inputs:            # input 내의 작성 하는 속성은 굉장히 많다.
    - type: log             # 입력 타입 (log, filestream, tcp, udp 등)
      enabled: true
      path:                 # log 파일이 위치하고, 읽을 모든 파일의 경로 설정
        - /var/log/*.log    # 기록이 저장된 경로 *.log .log 로 끝나는 모든 파일 이름 조회
        - /var/log/app/*.log
      fields:
        env: production     # dev(개발단계) - stg(배포 전 테스트) - prod(운영중)
        service: 프로젝트이름

2. Output(출력)
수집한 로그를 어디로 보낼지 정의

# 1번 : elasticsearch 로 직접 전송
output.elasticsearch:
    hosts: ["localhost:9200"]       # hosts 는 개발 환경에 따라 변경될 수 있다.
    index: "my-log-%{+yyyy.MM.dd}" # index 는 개발 환경에 따라 변경될 수 있다.

# 2번 : 기록된 로그를 다시 한 번 데이터 작업처리 후 조회하기 위하여 Logstash 로 전송
output.logstash:
    hosts: ["localhost:5044"]

3. Processors(전처리)
로그를 전송하기 전에 가공
processors:             # 만약 FileBeat를 사용하는 회사라면 회사 내규에 따라 다르게 설정
    - add_host_metadata: ~ # 호스트 정보 자동 추가
    - add_cloud_metadata: ~ # 클라우드 메타데이터 추가
    - drop_fields:
        fields: ["agent_ephemeral_id"] # 불필요한 필드 제거
    - rename:
        fields:
            - from: "log.level"
              to : "severity"
4. Modules(모듈)
filebeat.modules:
    - module: mysql
      access:
        enabled: true
        var.paths: ["/var/log/mysql/access.log"]
      error:
        enabled: true
자주 사용하는 서비스 (MySQL 등)의 설정을 미리 패키징한 것
'''










