# SQLAlchemy  = Python으로 DB를 다룰 수 있게 해주는 라이브러리
# 자동으로 SQL을 필요할 때 키며, 사용끝나면 자동으로 off 닫음 처리
# Springboot = JPA 와 유사한 방식으로
# SELECT * FROM order WHERE id = 1
# 과 같이 직접적으로 sql을 작성하는 mapper 방식이 아니라
# 내부에 내장되어 있는 SQL 형태를 호출하여 사용
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # 연결 준비 완료상태이지 아직 실제로 db 연결까지 모두 완료된 처리는 아니다.
# UserMapper userMapper = new UserMapper()
# SpringBoot @Autowired @RequiredArgsConstructor
'''
UserMapper userMapper = new UserMapper()
SpringBoot @Autowired @RequiredArgsConstructor

@RequiredArgsConstructor
@Service
public class UserService{
    @RequiredArgsConstructor
    UserMapper userMapper;

}
'''