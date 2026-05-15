'''
# 보안 켤 때만
docker compose down -v
# yml에서 xpack.security.enabled=true 로 수정 후
docker compose up -d

# kibana_system 비번 설정 (이때만 필요)
curl -X POST "http://localhost:9200/_security/user/kibana_system/_password" \
  -H "Content-Type: application/json" \
  -u elastic:changeme123 \
  -d '{"password": "changeme123"}'

'''
# create_role_user.py
import requests

ES = "http://localhost:9200"
AUTH = ("elastic", "changeme123")  # 보안 ON일 때만 auth 필요

role = {
    "indices": [
        {
            "names": ["korea-cities"],
            "privileges": ["read", "view_index_metadata"]
        }
    ],
    "cluster": ["monitor"]
}

res = requests.put(f"{ES}/_security/role/korea_readonly", json=role, auth=AUTH)
print("Role 생성:", res.json())

user = {
    "password": "user1234!",
    "roles": ["korea_readonly"],
    "full_name": "Korea Reader"
}

res = requests.put(f"{ES}/_security/user/korea_user", json=user, auth=AUTH)
print("User 생성:", res.json())


'''
# 읽기 테스트 (성공)
curl -u korea_user:user1234! "http://localhost:9200/korea-cities/_search?pretty"

# 삭제 시도 (403 에러 확인)
curl -X DELETE -u korea_user:user1234! "http://localhost:9200/korea-cities"
'''