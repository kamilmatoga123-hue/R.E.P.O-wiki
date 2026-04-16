Projekt aplikacji webowej stworzonej w Django, zawierającej bazę wiedzy o grze oraz forum dla użytkowników.


### 1. INSTALACJA I URUCHOMIENIE


   # Windows:

w CMD:
KROK 1:wejdz w R.E.P.O-wiki

KROK 2: Stwórz i aktywuj środowisko wirtualne:
   python -m venv venv  albo py -m venv venv
   
KROK 3: aktywuj skrypty
   venv\Scripts\activate

KROK 4: Zainstaluj Django:
   pip install django

KROK 5: Zainstaluj requirements.txt:
   pip install -r requirements.txt

KROK 6: Wejdz do folderu myproject
   cd myproject

KROK 7: Uruchom migracje (stwórz strukturę bazy danych):
   py manage.py migrate

KROK 8: Wczytaj dane startowe (potwory, przedmioty itp.):
   py manage.py loaddata info_data.json

KROK 9: Stwórz konto administratora:
   py manage.py createsuperuser

KROK 10: Uruchom serwer:
   py manage.py runserver

Adres aplikacji: http://127.0.0.1:8000/

# macOS:

Na systemie operacyjnym macOS aktywuje sie skrypty poprzez taka komende:

source venv\Scripts\activate


### 2. ZARZĄDZANIE DANYMI


Dane z sekcji INFO (monsters, items itp.) są przechowywane w pliku info_data.json. 
Aby zaktualizować ten plik po zmianach w panelu admina, użyj komendy:

python -X utf8 manage.py dumpdata info --indent 2 > info_data.json


### 3. Wyjscie z serwera:

Ctrl + C w konsoli


### 4.Zastosowane technologie:

Python – główny język programowania projektu.

Django – framework webowy (Back-end) odpowiedzialny za logikę aplikacji, bazę danych i routing.

SQLite3 – lekka, plikowa baza danych (standardowa w Django podczas tworzenia projektu).

HTML5 & CSS3 – do budowy struktury i wyglądu stron (znajdują się w Twoich folderach templates i static).

Pip – menedżer pakietów Pythona, użyty do zarządzania bibliotekami (widoczny w pliku requirements.txt).

venv (Virtual Environment) – narzędzie do izolacji środowiska projektu, zapewniające czystość bibliotek.

Git – system kontroli wersji używany do śledzenia zmian w kodzie.

GitHub – platforma do hostowania repozytorium i współpracy nad kodem.


### 5. Struktura projektu: 


```text
.
├── .gitignore
├── requirements.txt
├── README.md
└── myproject/
    ├── manage.py
    ├── myproject/      # Ustawienia projektu
    ├── Forum/          # Aplikacja forum
    ├── Info/           # Aplikacja informacyjna
    ├── Konta/          # Zarządzanie użytkownikami
    ├── static/         # CSS, JS, Obrazy
    └── templates/      # Pliki HTML

