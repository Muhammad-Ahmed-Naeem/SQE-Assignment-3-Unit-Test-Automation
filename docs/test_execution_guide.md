# Task 4: Test Suite Configuration & Execution Guide

**Tester:** M. Ahmad Naeem (`23F-3113`)  
**Assignment:** SQE Assignment 3 – Test Automation Solution  
**Configuration File:** `pytest.ini`

---

## 1. Overview of Test Configuration (`pytest.ini`)

The project uses `pytest.ini` at the root directory to implement all requirements of **Task 4**:
1. **Parallel Execution:** Integration with `pytest-xdist` to run tests concurrently across multiple worker processes (`-n auto`).
2. **Suite Division & Markers:** Registered custom markers (`smoke`, `regression`, `bva`, `ecp`, `exception`, `data_driven`, `range_suite`, `email_suite`, `ahmad_suite`).
3. **Execution Ordering:** Integration with `pytest-order` using `@pytest.mark.order(n)` to enforce sequential execution dependencies.
4. **Data-Driven Parameterization:** Leveraging `@pytest.mark.parametrize` for evaluating multiple boundary conditions without duplicating code.

---

## 2. Test Execution Commands & Suites

Ensure the virtual environment is activated before running tests:
```powershell
.\venv\Scripts\Activate.ps1
```

### 2.1 Run All Tests for Ahmad's Suite
Runs all 63 unit, boundary, and data-driven tests developed by M. Ahmad Naeem:
```powershell
pytest -m ahmad_suite -v
```

### 2.2 Run Tests in Parallel (Multi-Core Execution)
Uses `pytest-xdist` to distribute tests across CPU cores:
```powershell
pytest -m ahmad_suite -n auto -q
```

### 2.3 Run Specific Test Suites (Marker Groups)

| Suite / Objective | Command | Test Count | Description |
| :--- | :--- | :---: | :--- |
| **Smoke Suite** | `pytest -m smoke -v` | 3 | Fast critical path sanity checks |
| **Boundary Value Analysis (BVA)** | `pytest -m bva -v` | 25 | All boundary limit and transition tests |
| **Equivalence Class Partitioning (ECP)** | `pytest -m ecp -v` | 22 | All valid and invalid equivalence class tests |
| **Data-Driven CSV Suite** | `pytest -m data_driven -v` | 13 | Automated tests consuming `data/test_data_ahmad.csv` |
| **Module 1 Range Suite** | `pytest -m range_suite -v` | 32 | All `between` and `length` tests |
| **Module 2 Email Suite** | `pytest -m email_suite -v` | 18 | All RFC email format and boundary tests |

### 2.4 Verify Test Execution Ordering (`pytest-order`)
To see the explicit execution order in action (Order 1 through 35):
```powershell
pytest tests/test_range_length_ahmad.py tests/test_email_ahmad.py -v
```

### 2.5 Run Data-Driven External CSV Tests (Task 3)
```powershell
pytest tests/test_data_driven_ahmad.py -v
```
