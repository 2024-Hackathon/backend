MY_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nextpage',
        'USER': 'user',
        'PASSWORD': '1234',
        # 장고를 도커로 실행 시
        'HOST': 'mysql',
        # 장고를 로컬로 실행 시
        # 'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# 장고를 도커로 실행 시
MY_DATABASE_URL = "bolt://user:nextpage@neo4j:7687"

# 장고를 로컬로 실행 시
# MY_DATABASE_URL = "bolt://user:nextpage@localhost:7687"

MY_SECRET = 'django-insecure-ei+38+!!u%a_!&(*ylom1tsl^akvni(-)j1p*qzicx%o%=d=2q'