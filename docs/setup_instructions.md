# Task 1: Open-Source Project Selection & Local Environment Setup

**Application Name:** `python-validators/validators`  
**GitHub Repository:** [https://github.com/python-validators/validators](https://github.com/python-validators/validators)  
**Group Repository:** [https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation](https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation)  

---

## 1. Project Selection Rationale

For this assignment, we selected **`python-validators/validators`**, a pure-Python validation library.

### Why this project was chosen:
1. **Clear Modular Boundaries:** The codebase is organized into cleanly separated validator modules (`between.py`, `length.py`, `email.py`, `domain.py`, `ip_address.py`, `card.py`), making it straightforward to divide among group members.
2. **Textbook Suitability for ECP and BVA:** The functions evaluate input ranges, character counts, and string patterns against formal specifications (RFCs and standards). This allows natural derivation of Equivalence Class Partitions and Boundary Values.
3. **Pure Python Architecture:** The library has zero external system dependencies (no external SQL servers, microservices, or complex build tools), allowing rapid local setup and reliable test execution across different machines.

---

## 2. Step-by-Step Local Environment Setup

Follow these steps to replicate the local development environment:

### Step 2.1: Clone the Repository
```powershell
git clone https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation.git
cd SQE-Assignment-3-Unit-Test-Automation
```

### Step 2.2: Create and Activate Virtual Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# (If using CMD: .\venv\Scripts\activate.bat)
# (If using bash: source venv/bin/activate)
```

### Step 2.3: Install Dependencies
```powershell
# Install the validators package in editable mode
pip install -e .

# Install test automation and reporting dependencies
pip install -r requirements.txt
```

### Step 2.4: Verify the Installation
Verify that the test suite runs and all tests pass:
```powershell
# Run all tests cleanly
pytest -q

# Run tests in parallel across CPU cores
pytest -n auto -q
```
*Expected Result:* All tests discover and pass in under 2 seconds.

---

## 3. Setup Demonstration Video

As required by **Task 1**, a short video recording demonstrates the complete local setup and execution.

* **Video File Location:** `docs/setup_video.mp4` *(or see link below)*
* **Video Link (Drive / YouTube Unlisted):** `[INSERT YOUR VIDEO LINK HERE]`
* **Demonstrated Activities:**
  1. Activating the virtual environment (`.\venv\Scripts\Activate.ps1`).
  2. Verifying Python and package versions (`pip list`).
  3. Running the automated test suite with `pytest`.
  4. Demonstrating parallel test execution with `pytest -n auto`.

### Screen Recording Script (1–2 minutes)
1. **0:00 – 0:20:** Show the cloned project folder in VS Code / PowerShell. State your name (**M. Ahmad Naeem - 23F-3113** and **Saim Naveed - 24F-3043**) and announce the selected project: `python-validators/validators`.
2. **0:20 – 0:45:** Activate `venv` by running `.\venv\Scripts\Activate.ps1` and run `pip list` to show `pytest`, `pytest-xdist`, `openpyxl`, etc.
3. **0:45 – 1:15:** Run `pytest -q` to show 1,516 tests passing cleanly.
4. **1:15 – 1:30:** Run `pytest -n auto -q` to show parallel multi-core execution. Conclude the video.
