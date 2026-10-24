# Task 2: Equivalence Class Partitioning (ECP) & Boundary Value Analysis (BVA) Notes

**Tester:** M. Ahmad Naeem (`23F-3113`)  
**Assigned Modules:**
* **Module 1: Range & Length Validation** (`validators.between` & `validators.length`)
* **Module 2: Contact & Domain Validation** (`validators.email`)

---

## 1. Module 1 — Function 1: `validators.between(value, min_val=None, max_val=None)`

### 1.1 Function Overview & Specification
The `between` function validates whether a given comparable value (integer, float, datetime) falls within an optional inclusive lower (`min_val`) and upper (`max_val`) bound:
* Returns `True` if `min_val <= value <= max_val`.
* Returns `ValidationError` if the value falls outside the specified bounds.
* Returns `False` / `ValidationError` if `value is None`.
* Raises `ValueError` if `min_val > max_val`.
* Raises `TypeError` if there is a type mismatch during comparison.

---

### 1.2 Equivalence Class Partitioning (ECP) — `between`

| Partition ID | Input Condition / Partition Description | Class Type | Representative Test Data | Expected Output |
| :--- | :--- | :---: | :--- | :--- |
| **ECP-BET-01** | Value strictly inside closed range $[10, 20]$ | Valid | `value = 15, min_val = 10, max_val = 20` | `True` |
| **ECP-BET-02** | Value equal to lower boundary ($value = min\_val$) | Valid | `value = 10, min_val = 10, max_val = 20` | `True` |
| **ECP-BET-03** | Value equal to upper boundary ($value = max\_val$) | Valid | `value = 20, min_val = 10, max_val = 20` | `True` |
| **ECP-BET-04** | Only `min_val` specified; $value \ge min\_val$ | Valid | `value = 100, min_val = 50, max_val = None` | `True` |
| **ECP-BET-05** | Only `max_val` specified; $value \le max\_val$ | Valid | `value = 25, min_val = None, max_val = 50` | `True` |
| **ECP-BET-06** | Neither bound specified ($min\_val=None, max\_val=None$) | Valid | `value = 42, min_val = None, max_val = None` | `True` |
| **ECP-BET-07** | Floating point numbers within bounds | Valid | `value = 13.5, min_val = 10.2, max_val = 15.8` | `True` |
| **ECP-BET-08** | Datetime objects within datetime bounds | Valid | `value = 2026-05-15, min = 2026-01-01, max = 2026-12-31` | `True` |
| **ECP-BET-09** | Value strictly below lower bound ($value < min\_val$) | Invalid | `value = 5, min_val = 10, max_val = 20` | `ValidationError` |
| **ECP-BET-10** | Value strictly above upper bound ($value > max\_val$) | Invalid | `value = 25, min_val = 10, max_val = 20` | `ValidationError` |
| **ECP-BET-11** | Value is `None` | Invalid | `value = None, min_val = 0, max_val = 100` | `ValidationError` |
| **ECP-BET-12** | Inverted bounds ($min\_val > max\_val$) | Exception | `value = 15, min_val = 30, max_val = 10` | Raises `ValueError` |
| **ECP-BET-13** | Incompatible data types (comparison mismatch) | Exception | `value = "string", min_val = 10, max_val = 20` | Raises `TypeError` |

---

### 1.3 Boundary Value Analysis (BVA) — `between`
*Range Under Test: $[10, 20]$*

| Boundary Point | Value | Calculation | Expected Result | Justification |
| :--- | :---: | :---: | :---: | :--- |
| **Min - 1** | `9` | $min - 1$ | `ValidationError` | Just outside lower boundary |
| **Min (Lower Bound)** | `10` | $min$ | `True` | Exactly on inclusive lower bound |
| **Min + 1** | `11` | $min + 1$ | `True` | Just inside lower boundary |
| **Nominal Value** | `15` | $(min + max) / 2$ | `True` | Typical valid middle value |
| **Max - 1** | `19` | $max - 1$ | `True` | Just inside upper boundary |
| **Max (Upper Bound)** | `20` | $max$ | `True` | Exactly on inclusive upper bound |
| **Max + 1** | `21` | $max + 1$ | `ValidationError` | Just outside upper boundary |
| **Float Boundary (Just below)** | `9.999` | $min - \epsilon$ | `ValidationError` | High precision boundary test |
| **Float Boundary (Just above)** | `10.001`| $min + \epsilon$ | `True` | High precision boundary test |

---

## 2. Module 1 — Function 2: `validators.length(value, min_val=None, max_val=None)`

### 2.1 Function Overview & Specification
The `length` function validates whether the length of a string `value` falls within the inclusive range $[min\_val, max\_val]$:
* Returns `True` if `min_val <= len(value) <= max_val`.
* Returns `ValidationError` if string length is out of range.
* Raises `ValueError` if `min_val < 0` or `max_val < 0`.

---

### 2.2 Equivalence Class Partitioning (ECP) — `length`

| Partition ID | Input Condition / Partition Description | Class Type | Representative Test Data | Expected Output |
| :--- | :--- | :---: | :--- | :--- |
| **ECP-LEN-01** | String length strictly within range $[5, 10]$ | Valid | `value = "abcdef", min_val = 5, max_val = 10` | `True` |
| **ECP-LEN-02** | String length equal to `min_val` | Valid | `value = "hello", min_val = 5, max_val = 10` | `True` |
| **ECP-LEN-03** | String length equal to `max_val` | Valid | `value = "abcdefghij", min_val = 5, max_val = 10` | `True` |
| **ECP-LEN-04** | Exact length constraint ($min\_val == max\_val$) | Valid | `value = "pass", min_val = 4, max_val = 4` | `True` |
| **ECP-LEN-05** | Only `min_val` specified; $len(value) \ge min\_val$ | Valid | `value = "longstringhere", min_val = 5` | `True` |
| **ECP-LEN-06** | Only `max_val` specified; $len(value) \le max\_val$ | Valid | `value = "short", max_val = 10` | `True` |
| **ECP-LEN-07** | Empty string (`""`) with $min\_val = 0$ | Valid | `value = "", min_val = 0, max_val = 5` | `True` |
| **ECP-LEN-08** | String length strictly less than `min_val` | Invalid | `value = "tiny", min_val = 5, max_val = 10` | `ValidationError` |
| **ECP-LEN-09** | String length strictly greater than `max_val` | Invalid | `value = "thisstringistoolong", min = 5, max = 10` | `ValidationError` |
| **ECP-LEN-10** | Empty string (`""`) when $min\_val \ge 1$ | Invalid | `value = "", min_val = 1, max_val = 10` | `ValidationError` |
| **ECP-LEN-11** | Negative `min_val` specified ($min\_val < 0$) | Exception | `value = "test", min_val = -1, max_val = 5` | Raises `ValueError` |
| **ECP-LEN-12** | Negative `max_val` specified ($max\_val < 0$) | Exception | `value = "test", min_val = 1, max_val = -5` | Raises `ValueError` |

---

### 2.3 Boundary Value Analysis (BVA) — `length`
*Target String Length Range: $[5, 10]$*

| Boundary Point | String Length | Sample Input String | Expected Result | Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Min - 1** | `4` | `"four"` | `ValidationError` | Just below minimum required length |
| **Min (Lower Bound)** | `5` | `"five5"` | `True` | Exactly at minimum required length |
| **Min + 1** | `6` | `"six666"` | `True` | Just above minimum required length |
| **Nominal Value** | `7` | `"seven77"` | `True` | Typical valid length |
| **Max - 1** | `9` | `"nine99999"` | `True` | Just below maximum allowed length |
| **Max (Upper Bound)** | `10` | `"ten1010100"` | `True` | Exactly at maximum allowed length |
| **Max + 1** | `11` | `"eleven11111"` | `ValidationError` | Just above maximum allowed length |
| **Zero Length** | `0` | `""` | `ValidationError` | Absolute minimum string boundary |

---

## 3. Module 2 — Function 3: `validators.email(value, ...)`

### 3.1 Function Overview & Specification
The `email` function validates whether an input string conforms to RFC 1034, RFC 5321, and RFC 5322 email syntax rules:
* Must contain exactly one `@` symbol separating `username_part` and `domain_part`.
* RFC 5321 length limits:
  * Maximum username length = **64 characters**.
  * Maximum domain length = **253 characters**.
* Must possess valid domain and Top-Level Domain (TLD) structure.

---

### 3.2 Equivalence Class Partitioning (ECP) — `email`

| Partition ID | Input Condition / Partition Description | Class Type | Representative Test Data | Expected Output |
| :--- | :--- | :---: | :--- | :--- |
| **ECP-EML-01** | Standard format (`user@domain.com`) | Valid | `test.user@example.com` | `True` |
| **ECP-EML-02** | Email with multi-level subdomain | Valid | `ahmad@mail.fast.edu.pk` | `True` |
| **ECP-EML-03** | Allowed special characters in local part (`+`, `.`, `_`, `-`) | Valid | `ahmad.naeem+sqe@work-domain.org` | `True` |
| **ECP-EML-04** | Numeric local part and domain | Valid | `233113@domain123.com` | `True` |
| **ECP-EML-05** | IPv4 address literal domain (`ipv4_address=True`) | Valid | `admin@[192.168.1.1]` | `True` |
| **ECP-EML-06** | Missing `@` symbol | Invalid | `ahmadexample.com` | `ValidationError` |
| **ECP-EML-07** | Multiple `@` symbols | Invalid | `ahmad@@example.com`, `a@b@c.com` | `ValidationError` |
| **ECP-EML-08** | Empty local part (missing username) | Invalid | `@example.com` | `ValidationError` |
| **ECP-EML-09** | Empty domain part (missing domain) | Invalid | `ahmad@` | `ValidationError` |
| **ECP-EML-10** | Empty string (`""`) or whitespace only | Invalid | `""`, `"   "` | `ValidationError` |
| **ECP-EML-11** | Invalid characters in domain part (spaces, underscores) | Invalid | `user@ex ample.com`, `user@exam_ple.com` | `ValidationError` |
| **ECP-EML-12** | Missing Top-Level Domain (single label without simple_host) | Invalid | `user@localdomain` | `ValidationError` |
| **ECP-EML-13** | Local part exceeds 64 characters | Invalid | `{"a"*65}@example.com` | `ValidationError` |
| **ECP-EML-14** | Domain part exceeds 253 characters | Invalid | `user@{"a"*250}.com` | `ValidationError` |

---

### 3.3 Boundary Value Analysis (BVA) — `email`

#### Local Part (Username) Length Boundary Analysis (Limit: 64 characters)
*Base Domain: `@example.com`*

| Boundary Point | Username Length | Test Email Input | Expected Result | Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Min - 1 (Empty)** | `0` | `@example.com` | `ValidationError` | Username cannot be empty |
| **Min Boundary** | `1` | `a@example.com` | `True` | Smallest valid single-character username |
| **Nominal Value** | `10` | `ahmadnaeem@example.com` | `True` | Typical username length |
| **Max - 1** | `63` | `{"a"*63}@example.com` | `True` | Exactly 1 character below RFC limit |
| **Max Boundary** | `64` | `{"a"*64}@example.com` | `True` | Exactly at RFC 5321 maximum limit |
| **Max + 1** | `65` | `{"a"*65}@example.com` | `ValidationError` | Exceeds RFC 5321 limit by 1 char |

#### Domain Part Length Boundary Analysis (Limit: 253 characters)
*Base Username: `user@`*

| Boundary Point | Domain Length | Test Email Input | Expected Result | Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Max - 1** | `252` | `user@` + valid 252-char domain | `True` | 1 character below RFC maximum |
| **Max Boundary** | `253` | `user@` + valid 253-char domain | `True` | Exactly at RFC 1034/5321 limit |
| **Max + 1** | `254` | `user@` + valid 254-char domain | `ValidationError` | Exceeds RFC limit by 1 character |
