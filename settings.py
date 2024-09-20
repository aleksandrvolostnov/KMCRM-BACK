from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'
SECRET_KEY = 'django-insecure-%-ywc0y-56$w486k^$)k#g!=s@k%$dox5gm8ya=aiu3qdqocvg'

DEBUG = True

ALLOWED_HOSTS = ['oz-km-crm.vercel.app','av22.pythonanywhere.com','10.255.0.1','192.168.5.214', 'localhost', '127.0.0.1', '192.168.0.112' ]
#'oz-km-crm.vercel.app',
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm',
    'rest_framework'

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Добавьте эту строку
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS_ALL = False  # Установите в False, чтобы разрешить только перечисленные домены

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    "http://av22.pythonanywhere.com",# Замените на адрес вашего фронтенда
    'https://oz-km-crm.vercel.app',
    'http://192.168.5.214:8080',
    'http://10.255.0.1:8080',
    'http://10.255.0.1:8081'
    # Добавьте другие домены, если необходимо
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    'http://av22.pythonanywhere.com',
    'http://127.0.0.1:8080',
    'http://10.255.0.1:8080',
    'https://oz-km-crm.vercel.app',
    'http://192.168.5.214:8080',
    'http://10.255.0.1:8081'

]

print(CORS_ALLOWED_ORIGINS)  # Выводим значения в консоль

CSRF_COOKIE_SECURE = True  # Установите в True для HTTPS
CSRF_COOKIE_SAMESITE = 'Lax'  # Если нужно ограничить передачу CSRF токена на разные сайты, установите 'Strict'

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

ROOT_URLCONF = 'crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_HTTPONLY = True