# Object Detection Project

## Temat projektu

Wykrywanie obiektów na obrazach z użyciem OpenCV i TensorFlow.

## Cel projektu

Celem projektu jest stworzenie aplikacji umożliwiającej detekcję obiektów na statycznych obrazach
przy użyciu wytrenowanego modelu sieci neuronowej. Oczekiwanym rezultatem jest oznaczenie wykrytych obiektów ramkami oraz 
przypisanie im odpowiednich etykiet.

## Opis funkcjonalności

- Wczytywanie obrazu wejściowego z pliku
- Przetwarzanie obrazu
- Wykrywanie obiektów przy użyciu TensorFlow
- Oznaczenie wykrytych obiektów i zapis obrazu wyjściowego
- Obsługa różnych formatów obrazów (JPG, PNG)
- Wypisywanie wykrytych obiektów i ich nazw w terminalu

## Instrukcja uruchomienia projektu

### Wymagania

- Python 3.10 (zalecany przez pyenv)
- pip >= 21.0
- System: macOS ARM64, Linux, Windows

 **Uwaga:** 
Projekt wymaga Pythona w wersji 3.10.x. Inne wersje (np. 3.12, 3.13) mogą być niekompatybilne z TensorFlow i nie są wspierane.

### Instalacja

1. (Opcjonalnie) Zainstaluj pyenv aby zarządzać wersjami Pythona.
2. Ustaw wersję Pythona:

pyenv install 3.10.13
pyenv local 3.10.13


3. Utwórz i aktywuj środowisko wirtualne:

python -m venv venv
source venv/bin/activate

4. Zainstaluj zależności:

pip install --upgrade pip
pip install -r requirements.txt


Uwaga: Plik `requirements.txt` zawiera warunkową instalację TensorFlow w zależności od systemu i architektury CPU (np. tensorflow-macos dla Apple Silicon).

### Przykład uruchomienia

python src/main.py --image test.jpg --model models/frozen_inference_graph.pb --config models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt --labels coco.names --output output.jpg


## Użyte technologie

- Python 3.10
- OpenCV
- TensorFlow / TensorFlow-MacOS (dla M1/M2/M3)
- NumPy
- Pillow

## Analiza wymagań

### Wymagania funkcjonalne

- System umożliwia detekcję obiektów na obrazie.
- System umożliwia zapisanie obrazu z oznaczonymi obiektami.
- System umożliwia podanie ścieżki do obrazu wejściowego i wyjściowego.
- System przetwarza różne formaty obrazów.
- System wypisuje wykryte obiekty w terminalu.

### Wymagania niefunkcjonalne

- Kompatybilność z systemami: macOS ARM64, Linux, Windows.
- Wydajność: Detekcja obiektów w czasie ok. poniżej 7 sekund na jednym obrazie.
- Czytelność kodu (zgodność z PEP8).
- Modułowość – łatwa możliwość wymiany modelu TensorFlow.

### Interfejs użytkownika i funkcjonalności 

- Interfejs użytkownika to CLI (terminal). Obsługa odbywa się poprzez argumenty linii poleceń.
- System informuje użytkownika o wykrytych obiektach w terminalu oraz zapisuje wynikowy obraz.

## Cechy implementacyjne

- Struktura danych: lista obiektów klasy `DetectedObject` przechowująca nazwę, pewność i pozycję obiektu.
- Klasa i wyszukiwanie atrybutów: klasa `DetectedObject` z atrybutami, wyszukiwanie po `name`.
- Wykorzystanie API: OpenCV DNN API do detekcji obiektów.
- Organizacja kodu: kod podzielony na moduły: `src/main.py`, `src/detector.py`, `src/image_utils.py`.
- Błędy i wyjątki: obsługa błędów przy wczytywaniu plików i obrazów.
- Listy składane i generatory: używane przy przetwarzaniu detekcji.
- Elementy biblioteki standardowej: `argparse` do obsługi argumentów, `os` do operacji na plikach.
- Framework AI: wykorzystanie TensorFlow i NumPy.

## Testowanie

Projekt zawiera test jednostkowy sprawdzający poprawność działania detektora obiektów.

### Uruchamianie testów

Aby uruchomić test jednostkowy, wpisz w terminalu (będąc w katalogu głównym projektu):

python -m unittest tests/test_detector.py
text

Test sprawdza, czy:
- Detektor poprawnie ładuje model i plik z etykietami,
- Detekcja na przykładowym obrazie zwraca listę wykrytych obiektów,
- Każdy wykryty obiekt posiada wymagane atrybuty.

### Wyniki testów i ewentualne poprawki

- Jeśli test zakończy się komunikatem OK, oznacza to, że detektor działa poprawnie.
- W przypadku błędów (np. brak plików modelu, nieprawidłowa ścieżka do obrazu, brak bibliotek), terminal wyświetli szczegółowy komunikat.
  Wtedy należy:
  - Sprawdzić, czy wszystkie pliki (`frozen_inference_graph.pb`, `.pbtxt`, `coco.names`, obraz testowy) są w odpowiednich miejscach,
  - Upewnić się, że wszystkie wymagane biblioteki są zainstalowane,
  - Poprawić ścieżki w pliku testowym, jeśli to konieczne.

## Wnioski i możliwe usprawnienia

- Projekt działa poprawnie dla zdjęć statycznych.
- Można rozbudować aplikację o:
  - Graficzny interfejs użytkownika (GUI)
  - Obsługę wideo i kamery
  - Wsparcie dla innych modeli detekcji
  - Automatyczną analizę folderu ze zdjęciami
- Kod jest modularny i łatwy do rozbudowy.

###### Autor

# Jan Oszenda
# Python II
