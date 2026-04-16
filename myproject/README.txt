Projekt aplikacji webowej stworzonej w Django, zawierającej bazę wiedzy o grze oraz forum dla użytkowników.

========================================================================
1. INSTALACJA I URUCHOMIENIE
========================================================================
KROK 1: Stwórz i aktywuj środowisko wirtualne:
   python -m venv venv
   # Windows:
   .venv\Scripts\activate
   # MacOS:
   source .venv/bin/activate

KROK 2: Zainstaluj Django:
   pip install django

KROK 3: Uruchom migracje (stwórz strukturę bazy danych):
   python manage.py migrate

KROK 4: Wczytaj dane startowe (potwory, przedmioty itp.):
   python manage.py loaddata info_data.json

KROK 5: Stwórz konto administratora:
   python manage.py createsuperuser

KROK 6: Uruchom serwer:
   python manage.py runserver

Adres aplikacji: http://127.0.0.1:8000/

========================================================================
2. ZARZĄDZANIE DANYMI
========================================================================

Dane z sekcji INFO (monsters, items itp.) są przechowywane w pliku info_data.json. 
Aby zaktualizować ten plik po zmianach w panelu admina, użyj komendy:

python -X utf8 manage.py dumpdata info --indent 2 > info_data.json

