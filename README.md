
---

## 🟢 Build `*.exe` for PySide6 + YOLO + TensorFlow (Windows)

### Project Structure

```
project/
 ├── main.py
 ├── model_train_new.py
 ├── train_backend.py
 └── environment.yml
```

---

### 1️⃣ Create Conda Environment

```powershell
conda env create -f environment.yml
conda activate train_efdet_win
```

To deactivate:

```powershell
conda deactivate
```

---

### 2️⃣ Install PyInstaller

```powershell
pip install pyinstaller==6.17.0
```

---

### 3️⃣ Build Executable

From project root:

```powershell
pyinstaller --noconfirm --onefile --windowed main.py
```

Add additional files if needed:

```powershell
pyinstaller --noconfirm --onefile --windowed main.py --add-data "models;models"
```

If PyInstaller misses dynamic modules (YOLO/ultralytics), edit `main.spec`:

```python
hiddenimports=['ultralytics', 'ultralytics.yolo']
pyinstaller main.spec
```

---

### 4️⃣ Run

```powershell
.\dist\main.exe
```

---

### Tips

* Use either `opencv-python` or `opencv-python-headless` (not both).
* `--onefile` reduces clutter for large projects.
* Include any extra `.pyd` or DLLs if needed for TensorFlow/YOLO.

---
