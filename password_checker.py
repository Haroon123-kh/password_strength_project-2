import re  # Regular expressions ka module (text match karne ke liye)
import random  # Random values generate karne ke liye

# Step 3: Common weak passwords
# Ye kuch aam aur kamzor passwords ki list hai
common_passwords = ["password", "123456", "password123", "admin", "qwerty", "letmein"]

# Step 4: Password strength checker
# Ye function password ki taqat (strength) check karta hai
def password_strength(password):
    score = 0  # Shuruaati score 0
    feedback = []  # Mashwaray store karne ke liye list

    # Agar password common list mein hai to foran kamzor qarar dein
    if password.lower() in common_passwords:
        return 1, "❌ Ye password bohat aam hai. Aik naya aur behtar password use karein."

    # Agar password ki length 8 ya us se zyada hai to score barhao
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Kam az kam 8 characters ka password use karein.")

    # Agar password mein koi bada (uppercase) letter ho to score barhao
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔸 Aik bada (uppercase) letter zaroor shaamil karein.")

    # Agar chhota (lowercase) letter ho to score barhao
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Aik chhota (lowercase) letter zaroor shaamil karein.")

    # Agar number ho to score barhao
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Kam az kam aik number (0-9) zaroor hona chahiye.")

    # Agar special character ho to score barhao
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("🔸 Aik special character (!@#$%^&*) zaroor shaamil karein.")

    # Score aur feedback return karo
    return score, feedback

# Step 5: Score classification
# Ye function password ke score ko category mein convert karta hai
def classify_score(score):
    if score <= 2:
        return "Weak"  # Kamzor password
    elif 3 <= score <= 4:
        return "Moderate"  # Darmiyani
    else:
        return "Strong"  # Mazboot

# Step 6: Generate strong password
# Ye function aik strong password automatically generate karta hai
def generate_strong_password(length=12):
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    while True:
        password = ''.join(random.choices(all_chars, k=length))  # Random characters ka password
        score, _ = password_strength(password)  # Uska score check karo
        if score == 5:
            return password  # Agar score full hai to password return karo

# Step 7: Main logic (user input + result)
if __name__ == "__main__":
    password = input("🔐 Apna password likhiye: ")  # User se password lena
    score, result = password_strength(password)  # Password ka score check karna
    strength = classify_score(score)  # Us score ko category mein daalna

    print(f"\n🔎 Strength: {strength}")  # Password ki strength print karna

    if score < 5:
        # Agar password kamzor ho to mashware aur suggestion dikhana
        if isinstance(result, list):
            print("💡 Apke password ko behtar banane ke liye mashware:")
            for item in result:
                print(item)
        else:
            print(result)

        print(f"\n🔁 Yeh aik strong password ka suggestion hai: {generate_strong_password()}")
    else:
        print("✅ Mubarak ho! Aapka password strong hai.")  # Agar password mazboot ho
