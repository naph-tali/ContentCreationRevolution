@echo off
REM Create or reuse venv and activate
if not exist venv (
	python -m venv venv
)
call venv\Scripts\activate

REM Upgrade pip and install build helpers into this venv
python -m pip install --upgrade pip setuptools wheel setuptools_scm

REM Install Pillow using the already-installed build helpers to avoid isolated-build errors
pip install --no-build-isolation pillow==10.0.0

REM Install remaining requirements (requirements.txt is in project root)
pip install -r requirements.txt

echo Done. If you still see build errors, install OS-level build dependencies (e.g., Visual C++ Build Tools, zlib, libjpeg) or run this script from an elevated prompt.

