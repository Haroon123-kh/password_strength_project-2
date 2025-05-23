import streamlit as st
import re
import random

# Common weak passwords
common_passwords = ["password", "123456", "password123", "admin", "qwerty", "letmein"]

# Password strength checker
def password_strength(password):
    score = 0
    feedback = []

    if password.lower() in common_passwords:
        return 1, ["❌ Ye password bohat aam hai. Aik naya aur behtar password use karein."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Kam az kam 8 characters ka password use karein.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔸 Aik bada (uppercase) letter zaroor shaamil karein.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Aik chhota (lowercase) letter zaroor shaamil karein.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Kam az kam aik number (0-9) zaroor hona chahiye.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("🔸 Aik special character (!@#$%^&*) zaroor shaamil karein.")

    return score, feedback

# Classify password score
def classify_score(score):
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Generate strong password
def generate_strong_password(length=12):
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    while True:
        password = ''.join(random.choices(all_chars, k=length))
        score, _ = password_strength(password)
        if score == 5:
            return password

# Streamlit App
st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker (GUI)")
st.write("Apna password neeche likhiye aur uski security check karein.")

password = st.text_input("Password likhiye", type="password")

if password:
    score, feedback = password_strength(password)
    strength = classify_score(score)

    st.markdown(f"### 🔎 Strength: **{strength}**")

    if score < 5:
        st.warning("💡 Apke password ko behtar banane ke liye mashware:")
        for tip in feedback:
            st.markdown(f"- {tip}")
        st.info(f"🔁 Yeh aik strong password ka suggestion hai: **{generate_strong_password()}**")
    else:
        st.success("✅ Mubarak ho! Aapka password strong hai.")
