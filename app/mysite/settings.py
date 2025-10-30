from pathlib import Path
import environ
import os
import sys  # ← OK

# ==============================
# 環境変数設定
# ==============================
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))

# ==============================
# セキュリティ設定
# ==============================
SECRET_KEY = env('SECRET_KEY', default='test-secret-key')  # ← ここ追加！
DEBUG = env.bool('DEBUG', default=True)                    # ← ここ追加！
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])   # ← ここ追加！

# ==============================
# アプリケーション設定
# ==============================
INSTALLED_APPS = [
    'polls.apps.PollsConfig',   # ← ★あなたのアプリ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ==============================
# ミドルウェア設定
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ★重要
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ★重要
    'django.contrib.messages.middleware.MessageMiddleware',  # ★重要
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================
# URL・テンプレート設定
# ==============================
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # ここにテンプレートフォルダを追加してもOK
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# ==============================
# データベース設定
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': env('MYSQL_HOST'),
        'PORT': env('MYSQL_PORT'),
        'NAME': env('MYSQL_NAME'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
    }
}

# テストのときだけ SQLite に切り替え
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

# ==============================
# 国際化・タイムゾーンなど
# ==============================
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

# ==============================
# 静的ファイル設定
# ==============================
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
