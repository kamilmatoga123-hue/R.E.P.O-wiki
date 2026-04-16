Projekt aplikacji webowej stworzonej w Django, zawierającej bazę wiedzy o grze oraz forum dla użytkowników.


1. INSTALACJA I URUCHOMIENIE

w CMD:
KROK 1: Stwórz i aktywuj środowisko wirtualne:
   python -m venv venv  albo py -m venv venv
   # Windows:
   venv\Scripts\activate

KROK 2: Zainstaluj Django:
   pip install django

KROK 3: Zainstaluj requirements.txt:
   pip install -r requirements.txt

KROK 4: Wejdz do folderu myproject
   cd myproject

KROK 5: Uruchom migracje (stwórz strukturę bazy danych):
   py manage.py migrate

KROK 6: Wczytaj dane startowe (potwory, przedmioty itp.):
   py manage.py loaddata info_data.json

KROK 7: Stwórz konto administratora:
   py manage.py createsuperuser

KROK 8: Uruchom serwer:
   py manage.py runserver

Adres aplikacji: http://127.0.0.1:8000/


2. ZARZĄDZANIE DANYMI


Dane z sekcji INFO (monsters, items itp.) są przechowywane w pliku info_data.json. 
Aby zaktualizować ten plik po zmianach w panelu admina, użyj komendy:

python -X utf8 manage.py dumpdata info --indent 2 > info_data.json

