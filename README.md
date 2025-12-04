# 🟢 Instrukce: vytvoření `*.exe` pro PySide6 + YOLO + TensorFlow na Windows

Projekt:

```
project/
 ├── main.py
 ├── model_train_new.py
 ├── train_backend.py
 └── environment.yml
```

---

## 1️⃣ Příprava Conda-okolí

1. Vytvoř prostředí z `environment.yml`:

```powershell
conda env create -f environment.yml
```

2. Aktivuj ho:

```powershell
conda activate train_efdet_win
```

3. Ujisti se, že všechny závislosti jsou nainstalovány:

```powershell
python -m pip list
```

---

## 2️⃣ Instalace PyInstaller

PyInstaller umožňuje zabalit Python-projekt do `*.exe`.

```powershell
pip install pyinstaller==5.14.0
```

> ⚠️ Tip: někdy nové verze PyInstalleru nefungují dobře s PySide6, proto je verze 5.14 stabilní pro Windows.

---

## 3️⃣ Příprava main.py

Ujisti se, že v `main.py` je **správné pořadí a QApplication je vytvořen uvnitř main**:

```python
import sys
from model_train_new import YOLOTrainWindow
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = YOLOTrainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

## 4️⃣ Balení PySide6 GUI s backendem do `*.exe`

V PowerShellu (z kořenové složky projektu):

```powershell
pyinstaller --noconfirm --onefile --windowed main.py
```

Vysvětlení parametrů:

* `--onefile` → zabalí do jednoho exe
* `--windowed` → odstraní konzolové okno (pro GUI)
* `--noconfirm` → automaticky přepíše staré sestavení

---

## 5️⃣ Přidání dalších souborů (pokud je potřeba)

1. Pokud máš modely, YAML soubory, obrázky, přidej je přes `--add-data`:

```powershell
pyinstaller --noconfirm --onefile --windowed main.py --add-data "models;models"
```

> Formát: `"zdroj;složka_v_exe"`
> Na Windows oddělovač `;`, na Linux/macOS `:`

2. Pokud backend používá ultralytics/TensorFlow — PyInstaller obvykle automaticky přidá `.pyd` soubory, ale někdy jsou potřeba další DLL (obvykle ve složce `venv/Library/bin`).

---

## 6️⃣ Po sestavení

Po spuštění PyInstalleru se objeví:

```
dist/
 └── main.exe
build/
 └── ... dočasné soubory PyInstalleru ...
main.spec
```

Spusť exe:

```powershell
.\dist\main.exe
```

---

## 7️⃣ Tipy pro Windows + TensorFlow + PySide6

1. **Nainstaluj pouze `opencv-python` nebo `opencv-python-headless`**, ne oba současně. Pro GUI je lepší `opencv-python`.
2. Pro velké projekty TensorFlow + PySide6 je lepší balit `--onefile`, jinak exe bude 200-300 MB.
3. Někdy PyInstaller nevidí dynamické moduly YOLO (`ultralytics`), pak přidej do `main.spec`:

```python
hiddenimports=['ultralytics', 'ultralytics.yolo']
```

A přestav:

```powershell
pyinstaller main.spec
```
