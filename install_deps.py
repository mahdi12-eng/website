
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = [
    "asgiref==3.11.1",
    "Django==5.2",
    "django-allauth==65.16.1",
    "django-crispy-forms==2.6",
    "django-debug-toolbar==6.3.0",
    "django-environ==0.13.0",
    "django-extensions==4.1",
    "django-filter==25.2",
    "django-sitemaps==1.0",
    "django-sites==0.11",
    "django_login==1.0",
    "djangorestframework==3.17.1",
    "pillow==12.2.0",
    "psycopg==3.3.4",
    "psycopg-binary==3.3.4",
    "PyJWT==2.12.1",
    "sqlparse==0.5.5",
    "tzdata==2026.2",
    "jazzmin"
]

for package in packages:
    try:
        print(f"Installing {package}...")
        install_package(package)
        print(f"✓ Installed {package}")
    except Exception as e:
        print(f"✗ Error installing {package}: {e}")

print("\n✅ All packages installed! Now run 'python manage.py runserver'!")
