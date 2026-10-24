# SQE Assignment 3: Task Distribution & Allocation Matrix

**Course:** Software Quality Engineering (CS / SE)  
**Assignment:** Assignment 3 – Build Unit Test Automation Solution  
**Target Open-Source Application:** [`python-validators/validators`](https://github.com/python-validators/validators)  
**Repository:** [https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation](https://github.com/Muhammad-Ahmed-Naeem/SQE-Assignment-3-Unit-Test-Automation)

---

## 1. Group Members Information

| Student Name | Roll Number | Role | Git / Branch Identifier |
| :--- | :---: | :---: | :--- |
| **M. Ahmad Naeem** | `23F-3113` | Group Lead & Tester | `Muhammad-Ahmed-Naeem` / `ahmad/*` |
| **Saim Naveed** | `24F-3043` | Group Member & Tester | `saim/*` |

---

## 2. Identified Application Modules & Function Allocation

The project is decomposed into three distinct modules with a balanced 50/50 division of responsibilities (3 functions allocated per member):

| Module Name | Module Path | Function Under Test | Assigned Member |
| :--- | :--- | :--- | :---: |
| **Module 1: Range & Length Validation** | `src/validators/between.py`<br>`src/validators/length.py` | • `between(value, min_val, max_val)`<br>• `length(value, min_val, max_val)` | **M. Ahmad Naeem**<br>(`23F-3113`) |
| **Module 2: Contact & Domain Validation** | `src/validators/email.py`<br>`src/validators/domain.py` | • `email(value, ipv4_address, ...)`<br>• `domain(value, consider_tld)` | **M. Ahmad Naeem** (`email`)<br>**Saim Naveed** (`domain`) |
| **Module 3: Structured Network & Card Validation** | `src/validators/ip_address.py`<br>`src/validators/card.py` | • `ipv4(value, cidr, strict, private)`<br>• `card_number(value)` / `visa(value)` | **Saim Naveed**<br>(`24F-3043`) |

---

## 3. Detailed Task Allocation Matrix

| Assignment Task | M. Ahmad Naeem (`23F-3113`) | Saim Naveed (`24F-3043`) |
| :--- | :--- | :--- |
| **Task 1: Environment Setup & Video** | • Clone repo, create virtual environment (`venv`).<br>• Install dependencies and configure `requirements.txt`.<br>• Record local setup demo video. | • Clone repo, verify local environment setup.<br>• Validate local test suite execution. |
| **Task 2: ECP & BVA Notes** | • Formulate ECP partitions & BVA boundaries for `between`, `length`, and `email`.<br>• Commit notes to `docs/ecp_bva_notes/ahmad_notes.md`. | • Formulate ECP partitions & BVA boundaries for `domain`, `ipv4`, and `card`.<br>• Commit notes to `docs/ecp_bva_notes/saim_notes.md`. |
| **Task 2: Automated Unit Tests** | • 8–10 unit tests for `between`<br>• 8–10 unit tests for `length`<br>• 8–10 unit tests for `email`<br>• Implementation in `tests/test_range_length_ahmad.py` and `tests/test_email_ahmad.py`. | • 8–10 unit tests for `domain`<br>• 8–10 unit tests for `ipv4`<br>• 8–10 unit tests for `card`<br>• Implementation in `tests/test_domain_saim.py`, `tests/test_ipv4_saim.py`, and `tests/test_card_saim.py`. |
| **Task 3: Excel Sheet & Data-Driven CSV** | • External CSV dataset: `data/test_data_ahmad.csv`.<br>• Automated data-driven tests consuming external CSV.<br>• Document test cases in `data/test_cases.xlsx` (Sheet: `Ahmad_TestCases`). | • External CSV dataset: `data/test_data_saim.csv`.<br>• Automated data-driven tests consuming external CSV.<br>• Document test cases in `data/test_cases.xlsx` (Sheet: `Saim_TestCases`). |
| **Task 4: Pytest Configuration & Test Suites** | • Parallel test execution setup (`pytest-xdist`) in `pytest.ini`.<br>• Group test suites with custom markers (`@pytest.mark.ahmad_suite`, `@pytest.mark.range_tests`, `@pytest.mark.email_tests`). | • Execution ordering configuration (`pytest-order`).<br>• Test parameterization suites and markers (`@pytest.mark.saim_suite`, `@pytest.mark.domain_tests`, etc.). |
| **Summary Report** | • Author project overview, methodology, and setup report. | • Author test execution results and contribution verification report. |

---

## 4. Git Commit & Traceability Protocol

To fulfill the rubric requirement that *"Commit history on Git should show each individual's activity"*:
1. Each member works on their designated feature branch or commits using their respective Git credentials:
   * **M. Ahmad Naeem:** Commits authored with `muhammad.ahmed.prof@gmail.com`.
   * **Saim Naveed:** Commits authored with his Git profile.
2. Commit messages must follow structured prefixes:
   * `[Task 1]` Setup and configuration
   * `[Task 2][Ahmad]` ECP/BVA notes and test suites for Module 1 complete & Module 2 Email task
   * `[Task 2][Saim]` ECP/BVA notes and test suites for Module 2 Domain task & Module 3 Complete
   * `[Task 3]` External CSV and Excel test cases
   * `[Task 4]` Pytest configuration (parallel, ordering, suites)
