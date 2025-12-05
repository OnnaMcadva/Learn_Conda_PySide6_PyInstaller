
---

## 🟢 Build `*.exe` for PySide6 + Conda + PyInstaller (Windows)

### Project Structure

```
project/
 ├── main.py
 ├── model_train_new.py
 ├── train_backend.py
 └── environment.yml
```

---

### Init conda for PowerShell

```powershell
conda init powershell
```

After this, close PowerShell and open it again. This only needs to be done once.

---

### 1️⃣ Create Conda Environment

```powershell
# conda env remove -n train_efdet_win -y 
conda env create -f environment.yml
# conda create -n train_efdet_win python=3.9 -y
conda activate train_efdet_win
# conda remove --force PySide6 PySide6-Essentials PySide6-Addons shiboken6 -y
```

To deactivate:

```powershell
conda deactivate
```

---

### 2️⃣ Install PyInstaller (& PySide6 ???)

```powershell
pip install pyinstaller
# pip install --force-reinstall PySide6
# pip install --force-reinstall --no-cache-dir PySide6==6.10.1
```

---

### 3️⃣ Build Executable

From project root:

```powershell
pyinstaller --noconfirm --onefile --windowed main.py
# pyinstaller --noconfirm --onefile --windowed main.py --collect-all PySide6
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

