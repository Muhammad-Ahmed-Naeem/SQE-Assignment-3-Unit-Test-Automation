import validators


def main():
    print("=" * 45)
    print(" Python Validators Library - Quick Demo")
    print("=" * 45)

    # 1. Test 'between'
    num = 15
    res_between = validators.between(num, min_val=10, max_val=20)
    print(f"\n[between] Checking if {num} is between 10 and 20:")
    print(f"Result: {res_between}")

    bad_num = 25
    res_bad_between = validators.between(bad_num, min_val=10, max_val=20)
    print(f"[between] Checking if {bad_num} is between 10 and 20:")
    print(f"Result: {res_bad_between}")

    # 2. Test 'length'
    word = "FastUniversity"
    res_len = validators.length(word, min_val=5, max_val=20)
    print(f"\n[length] Checking if '{word}' length (14) is in range [5, 20]:")
    print(f"Result: {res_len}")

    # 3. Test 'email'
    good_email = "ahmad.naeem@student.fast.edu.pk"
    print(f"\n[email] Checking '{good_email}':")
    print(f"Result: {validators.email(good_email)}")

    bad_email = "ahmadnaeemexample.com"
    print(f"[email] Checking '{bad_email}':")
    print(f"Result: {validators.email(bad_email)}")
    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()
