# SQE Assignment 3: Automated Unit Testing Solution Summary Report

**Course:** Software Quality Engineering (CS / SE)  
**Assignment:** Assignment 3 – Build Unit Test Automation Solution  
**Target Open-Source Application:** [`python-validators/validators`](https://github.com/python-validators/validators)  
**Repository:** [https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation](https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation)  
**Submission Due Date:** Oct 21, 2026  

---

## 1. Group Information & Task Allocation

| Student Name | Roll Number | Assigned Modules & Scope | Git Branch Identifier |
| :--- | :---: | :--- | :--- |
| **M. Ahmad Naeem** | `23F-3113` | • Module 1: `validators.between` & `validators.length`<br>• Module 2: `validators.email`<br>• Task 3: CSV Data-Driven Suite & Excel Test Cases<br>• Task 4: Parallel (`pytest-xdist`) & Suite Configuration | `Ahmad` |
| **Saim Naveed** | `24F-3043` | • Module 2: `validators.domain`<br>• Module 3: `validators.ip_address` & `validators.card`<br>• Task 3 & 4 Partner Test Suites | `Saim` |

---

## 2. Project Selection Rationale (Task 1)

**`python-validators/validators`** was selected as our open-source project because:
1. **Modular Architecture:** Source code is cleanly decomposed into discrete modules (`between.py`, `length.py`, `email.py`, `domain.py`, `ip_address.py`, `card.py`).
2. **Textbook Black-Box Testing Alignment:** Functions take strictly typed and structured input data evaluated against RFC specifications and numeric constraints, providing ideal scenarios for **Equivalence Class Partitioning (ECP)** and **Boundary Value Analysis (BVA)**.
3. **Pure Python Portability:** The core package has zero external database or server dependencies, allowing clean setup and rapid test execution across any environment.

---

## 3. Test Design Methodology: ECP & BVA (Task 2)

### 3.1 Module 1: `validators.between`
* **ECP Partitions:** Valid nominal range $[10, 20]$, lower bound, upper bound, open ranges (`min_val` only, `max_val` only), floats, datetime objects, values below minimum, values above maximum, inverted bounds exception (`min_val > max_val`).
* **BVA Boundaries:** Tested $min-1$ (9), $min$ (10), $min+1$ (11), nominal (15), $max-1$ (19), $max$ (20), $max+1$ (21).

### 3.2 Module 1: `validators.length`
* **ECP Partitions:** String length within range $[5, 10]$, exact length matching ($min=max$), open bounds, empty string ($len=0$), negative bounds exception (`min_val < 0`).
* **BVA Boundaries:** Tested length 4 (min-1), length 5 (min), length 6 (min+1), length 9 (max-1), length 10 (max), length 11 (max+1), length 0 (empty string).

### 3.3 Module 2: `validators.email`
* **ECP Partitions:** Standard valid emails, multi-level subdomains, allowed special characters (`+`, `.`, `_`, `-`), numeric components, missing `@`, multiple `@`, missing local username, missing domain, invalid domain spaces.
* **BVA Boundaries:** Local username length limits tested at 64 characters (max boundary) vs 65 characters (max+1 invalid), single character username (min boundary).

---

## 4. External Data-Driven Testing & Excel Specification (Task 3)

* **External CSV Dataset:** Stored at `data/test_data_ahmad.csv`, providing 13 external test vectors for `between`, `length`, and `email`.
* **Automated Runner:** Implemented in `tests/test_data_driven_ahmad.py`, which dynamically parses the CSV file and executes parameterized assertions.
* **Excel Workbook:** Documented in `data/test_cases.xlsx` (Sheet: `Ahmad_TestCases`), presenting 18 formatted test case specifications including Test IDs, Pre-conditions, Inputs, Expected Outputs, Actual Outputs, and Execution Status.

---

## 5. Test Automation Framework & Configuration (Task 4)

Configured through `pytest.ini` with modern plugins:
1. **Parallel Execution (`pytest-xdist`):** Automated multi-core execution (`pytest -m ahmad_suite -n auto`), running 63 tests in parallel in under 2 seconds.
2. **Suite Partitioning via Custom Markers:**
   * `pytest -m smoke`: 3 critical path tests.
   * `pytest -m bva`: 25 boundary value tests.
   * `pytest -m ecp`: 22 equivalence class tests.
   * `pytest -m data_driven`: 13 external CSV tests.
   * `pytest -m range_suite`: 32 Module 1 tests.
   * `pytest -m email_suite`: 18 Module 2 tests.
3. **Execution Ordering (`pytest-order`):** Enforces deterministic sequential execution using `@pytest.mark.order(1)` through `@pytest.mark.order(35)`.
4. **Test Parameterization:** Uses `@pytest.mark.parametrize` for data-driven boundary evaluations.

---

## 6. Execution Summary & Metrics

```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0
plugins: order-1.5.0, xdist-3.8.0
collecting ... collected 1579 items / 1516 deselected / 63 selected

tests/test_range_length_ahmad.py ................................        [ 50%]
tests/test_email_ahmad.py ...................                            [ 80%]
tests/test_data_driven_ahmad.py .............                           [100%]

===================== 63 passed, 1516 deselected in 0.24s =====================
```
* **Total Automated Tests Authored (Ahmad):** 63 tests
* **Pass Rate:** 100% (0 failures, 0 errors, 0 warnings)
* **Execution Time:** ~0.24 seconds (sequential) / ~2.08 seconds (parallel multi-core)
