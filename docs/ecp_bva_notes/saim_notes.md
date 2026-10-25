# ECP and BVA Test Notes

**Student Name:** Saim Naveed  
**Roll Number:** 24F-3043  
**Assigned Functions:**
- `validators.domain` (Module 2: Contact & Domain)
- `validators.ipv4` (Module 3: Network)
- `validators.card_number` & `validators.visa` (Module 3: Financial Cards)

---

## 1. Domain Validation (`validators.domain`)

### Equivalence Class Partitioning (ECP)

| Class ID | Partition Description | Type | Test Input | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| DOM-ECP-01 | Standard commercial domain (.com) | Valid | `"google.com"` | `True` |
| DOM-ECP-02 | Country code TLD domain | Valid | `"bbc.co.uk"` | `True` |
| DOM-ECP-03 | Multi-level subdomain | Valid | `"dev.portal.example.org"` | `True` |
| DOM-ECP-04 | Domain containing valid hyphen | Valid | `"my-cool-site.net"` | `True` |
| DOM-ECP-05 | Missing top-level domain (single label) | Invalid | `"localhost"` | `ValidationError` |
| DOM-ECP-06 | Leading hyphen in label | Invalid | `"-example.com"` | `ValidationError` |
| DOM-ECP-07 | Trailing hyphen in label | Invalid | `"example-.com"` | `ValidationError` |
| DOM-ECP-08 | Invalid characters (underscore or spaces) | Invalid | `"bad_domain.com"`, `"bad site.com"` | `ValidationError` |
| DOM-ECP-09 | URL with protocol instead of domain | Invalid | `"https://example.com"` | `ValidationError` |
| DOM-ECP-10 | Empty string input | Invalid | `""` | `ValidationError` |

### Boundary Value Analysis (BVA)

| Boundary Point | Value Tested | Expected Result | Reason |
| :--- | :--- | :--- | :--- |
| Min label length (1 char) | `"a.com"` | `True` | Smallest valid label |
| Below min label length (0 char) | `".com"` | `ValidationError` | Label cannot be empty |
| Max label length - 1 (62 chars) | `("a" * 62) + ".com"` | `True` | Just below 63-char limit |
| Max label length (63 chars) | `("a" * 63) + ".com"` | `True` | Exact RFC 1034 label limit |
| Max label length + 1 (64 chars) | `("a" * 64) + ".com"` | `ValidationError` | Exceeds 63-char limit |

---

## 2. IPv4 Validation (`validators.ipv4`)

### Equivalence Class Partitioning (ECP)

| Class ID | Partition Description | Type | Test Input | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| IP-ECP-01 | Standard valid public IPv4 address | Valid | `"8.8.8.8"` | `True` |
| IP-ECP-02 | Standard private class C IP | Valid | `"192.168.1.1"` | `True` |
| IP-ECP-03 | Localhost loopback IP | Valid | `"127.0.0.1"` | `True` |
| IP-ECP-04 | Valid CIDR subnet notation | Valid | `"192.168.1.0/24"` | `True` |
| IP-ECP-05 | Incomplete IP (missing octets) | Invalid | `"192.168.1"` | `ValidationError` |
| IP-ECP-06 | Too many octets (5 octets) | Invalid | `"192.168.1.1.1"` | `ValidationError` |
| IP-ECP-07 | Non-numeric characters in octet | Invalid | `"192.168.1.abc"` | `ValidationError` |
| IP-ECP-08 | Empty string | Invalid | `""` | `ValidationError` |

### Boundary Value Analysis (BVA)

| Boundary Point | Octet / CIDR Value | Test Input | Expected Result | Reason |
| :--- | :--- | :--- | :--- | :--- |
| Min octet bound (0) | 0 | `"0.0.0.0"` | `True` | Lowest possible octet value |
| Below min octet (-1) | -1 | `"-1.0.0.1"` | `ValidationError` | Negative octets invalid |
| Nominal octet (127) | 127 | `"127.0.0.1"` | `True` | Middle range octet |
| Max octet bound (255) | 255 | `"255.255.255.255"` | `True` | Highest possible octet value |
| Above max octet (256) | 256 | `"256.0.0.1"` | `ValidationError` | Exceeds 8-bit octet boundary |
| CIDR prefix min (0) | /0 | `"10.0.0.0/0"` | `True` | Lowest valid subnet mask |
| CIDR prefix max (32) | /32 | `"10.0.0.1/32"` | `True` | Highest valid host subnet mask |
| CIDR prefix max + 1 (33) | /33 | `"10.0.0.1/33"` | `ValidationError` | Out of IPv4 32-bit mask bounds |

---

## 3. Financial Card Validation (`validators.card_number` & `validators.visa`)

### Equivalence Class Partitioning (ECP)

| Class ID | Partition Description | Type | Test Input | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| CRD-ECP-01 | Valid generic card number passing Luhn check | Valid | `"4242424242424242"` | `True` |
| CRD-ECP-02 | Another valid card number passing Luhn | Valid | `"4111111111111111"` | `True` |
| CRD-ECP-03 | Valid Visa card format (starts with 4, len 16) | Valid | `"4012888888881881"` | `True` |
| CRD-ECP-04 | Card number with failing Luhn checksum | Invalid | `"4242424242424241"` | `ValidationError` |
| CRD-ECP-05 | Mastercard number passed to visa validator | Invalid | `"5105105105105100"` | `ValidationError` |
| CRD-ECP-06 | Non-numeric string input | Invalid | `"4242abcd42424242"` | `ValidationError` |
| CRD-ECP-07 | Empty string input | Invalid | `""` | `ValidationError` |

### Boundary Value Analysis (BVA)

| Boundary Point | Length / Digit Tested | Test Input | Expected Result | Reason |
| :--- | :--- | :--- | :--- | :--- |
| Card min length (13 digits) | 13 digits with valid Luhn | `"4012888888881"` | `True` | Valid 13-digit card |
| Visa length boundary (not 16) | 13 digits | `"4012888888881"` | `ValidationError` | Visa requires exact length 16 |
| Visa standard length (16 digits) | 16 digits | `"4242424242424242"` | `True` | Standard 16-digit Visa card |
| Card below min length | 11 digits | `"40128888888"` | `ValidationError` | Card too short |
