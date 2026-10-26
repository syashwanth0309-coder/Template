from pathlib import Path
import os
import secrets
BASE_DIR = Path(__file__).resolve().parent.parent
# Persist a random local development key without shipping a shared secret.
key_file = BASE_DIR / ".local-secret-key"
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    if not key_file.exists():
        key_file.write_text(secrets.token_urlsafe(50), encoding="utf-8")
    SECRET_KEY = key_file.read_text(encoding="utf-8").strip()
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = [v.strip() for v in os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,[::1],testserver").split(",") if v.strip()]
INSTALLED_APPS = ["django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles", "enquiry"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware", "django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF = "Profile.urls"
TEMPLATES = [{"BACKEND":"django.template.backends.django.DjangoTemplates", "DIRS":[BASE_DIR / "template"], "APP_DIRS":True, "OPTIONS":{"context_processors":["django.template.context_processors.request", "django.contrib.auth.context_processors.auth", "django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION = "Profile.wsgi.application"
DATABASES = {"default":{"ENGINE":"django.db.backends.sqlite3", "NAME":BASE_DIR / "db.sqlite3"}}
AUTH_PASSWORD_VALIDATORS = [{"NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},{"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"},{"NAME":"django.contrib.auth.password_validation.CommonPasswordValidator"},{"NAME":"django.contrib.auth.password_validation.NumericPasswordValidator"}]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATA_UPLOAD_MAX_MEMORY_SIZE = 65536
