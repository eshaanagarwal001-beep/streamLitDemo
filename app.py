i```python
import streamlit as st
import random

st.set_page_config(
    page_title="⚡ Harry Potter World",
    page_icon="🪄",
    layout="wide"
)

# Background styling
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #FFD700;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.title("⚡ Welcome to the Wizarding World ⚡")

st.image(
    "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200",
    use_container_width=True
)

st.markdown("""
### 🪄 Mischief Managed!

Step through Platform 9¾ and enter a world of magic, adventure, friendship,
and the occasional dark wizard.

🏰 Explore Hogwarts  
🦉 Meet magical creatures  
⚡ Learn spells  
🐍 Discover your Hogwarts House
""")

st.divider()

# House Selection
st.header("🎩 The Sorting Hat")

house = st.selectbox(
    "Which House do you belong to?",
    ["🦁 Gryffindor", "🦅 Ravenclaw", "🦡 Hufflepuff", "🐍 Slytherin"]
)

st.success(f"The Sorting Hat has chosen: {house}")

st.divider()

# Houses
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🦁 Gryffindor", "Bravery")
    st.write("Daring, nerve, and chivalry.")

with col2:
    st.metric("🦅 Ravenclaw", "Wisdom")
    st.write("Learning, wit, and creativity.")

with col3:
    st.metric("🦡 Hufflepuff", "Loyalty")
    st.write("Patience and hard work.")

with col4:
    st.metric("🐍 Slytherin", "Ambition")
    st.write("Cunning and determination.")

st.divider()

# Magical Spell Generator
st.header("✨ Random Spell Generator")

spells = [
    "Expelliarmus ⚔️",
    "Lumos 💡",
    "Expecto Patronum 🦌",
    "Wingardium Leviosa 🪶",
    "Alohomora 🔑",
    "Accio 📚",
    "Protego 🛡️",
    "Stupefy 💥"
]

if st.button("🪄 Cast a Spell"):
    st.balloons()
    st.success(random.choice(spells))

st.divider()

# Magical Creatures
st.header("🐉 Magical Creatures")

c1, c2, c3 = st.columns(3)

with c1:
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=500"
    )
    st.caption("🐉 Dragon")

with c2:
    st.image(
        "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=500"
    )
    st.caption("🦉 Owl")

with c3:
    st.image(
        "https://images.unsplash.com/photo-1511497584788-876760111969?w=500"
    )
    st.caption("🦄 Unicorn")

st.divider()

# Favorite Characters
st.header("⭐ Legendary Wizards")

characters = [
    "⚡ Harry Potter",
    "🧠 Hermione Granger",
    "😎 Sirius Black",
    "🪄 Albus Dumbledore",
    "🐺 Remus Lupin",
    "🔥 Severus Snape"
]

selected = st.multiselect(
    "Choose your favorites:",
    characters
)

if selected:
    st.write("Excellent choices!")
    st.write(selected)

st.divider()

st.markdown("""
## ⚡ Famous Quote

> *"Happiness can be found even in the darkest of times,
> if one only remembers to turn on the light."*  
> — Albus Dumbledore

""")

st.snow()

st.caption("🪄 Built with Streamlit • Mischief Managed")
```
