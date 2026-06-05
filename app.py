
import streamlit as st
import random
import time

st.set_page_config(
    page_title="⚡ Interactive Wizarding World",
    page_icon="🪄",
    layout="wide"
)

HOUSE_DATA = {
    "Gryffindor 🦁": {
        "colors": ["#7F0909", "#FFC500"],
        "emoji": "🦁",
        "trait": "Bravery",
        "animation": "🔥",
        "message": "A roaring blaze of courage surrounds you!"
    },
    "Ravenclaw 🦅": {
        "colors": ["#0E1A40", "#946B2D"],
        "emoji": "🦅",
        "trait": "Wisdom",
        "animation": "✨",
        "message": "A storm of stars and ideas lights your path!"
    },
    "Hufflepuff 🦡": {
        "colors": ["#EEE117", "#000000"],
        "emoji": "🦡",
        "trait": "Loyalty",
        "animation": "🌼",
        "message": "Warm golden magic blooms around you!"
    },
    "Slytherin 🐍": {
        "colors": ["#1A472A", "#AAAAAA"],
        "emoji": "🐍",
        "trait": "Ambition",
        "animation": "🐍",
        "message": "Silver-green serpentine magic coils through the air!"
    }
}

SPELL_DATA = {
    "Lumos 💡": {
        "emoji": "💡",
        "effect": "The page glows with magical light.",
        "animation": "✨💡✨",
        "css": "box-shadow: 0 0 35px #FFFACD;"
    },
    "Expelliarmus ⚔️": {
        "emoji": "⚔️",
        "effect": "A red spark blasts across the room!",
        "animation": "💥⚔️💥",
        "css": "box-shadow: 0 0 35px #FF3131;"
    },
    "Expecto Patronum 🦌": {
        "emoji": "🦌",
        "effect": "A silver Patronus appears to protect you.",
        "animation": "🦌✨🦌✨",
        "css": "box-shadow: 0 0 35px #B9F2FF;"
    },
    "Wingardium Leviosa 🪶": {
        "emoji": "🪶",
        "effect": "Objects begin floating gracefully.",
        "animation": "🪶⬆️🪶⬆️",
        "css": "box-shadow: 0 0 35px #D8BFD8;"
    },
    "Alohomora 🔑": {
        "emoji": "🔑",
        "effect": "A hidden magical door unlocks.",
        "animation": "🔑🚪✨",
        "css": "box-shadow: 0 0 35px #FFD700;"
    },
    "Stupefy 💥": {
        "emoji": "💥",
        "effect": "A stunning spell flashes forward.",
        "animation": "💥💫💥",
        "css": "box-shadow: 0 0 35px #FF4500;"
    }
}

house = st.sidebar.radio("🎩 Choose your Hogwarts House", list(HOUSE_DATA.keys()))
spell = st.sidebar.selectbox("🪄 Choose a Spell", list(SPELL_DATA.keys()))

house_info = HOUSE_DATA[house]
spell_info = SPELL_DATA[spell]

primary, secondary = house_info["colors"]

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(135deg, {primary}, #111111 55%, {secondary});
    color: white;
}}

.magic-card {{
    padding: 2rem;
    border-radius: 24px;
    background: rgba(0, 0, 0, 0.55);
    border: 2px solid {secondary};
    {spell_info["css"]}
    animation: pulse 2s infinite alternate;
}}

.house-symbol {{
    font-size: 6rem;
    text-align: center;
    animation: float 2.5s ease-in-out infinite;
}}

.spell-burst {{
    font-size: 3rem;
    text-align: center;
    animation: burst 1.2s ease-in-out infinite;
}}

.floating {{
    position: fixed;
    top: -10%;
    font-size: 2rem;
    animation: fall 6s linear infinite;
}}

.floating:nth-child(1) {{ left: 10%; animation-delay: 0s; }}
.floating:nth-child(2) {{ left: 25%; animation-delay: 1s; }}
.floating:nth-child(3) {{ left: 40%; animation-delay: 2s; }}
.floating:nth-child(4) {{ left: 60%; animation-delay: 1.5s; }}
.floating:nth-child(5) {{ left: 80%; animation-delay: 0.5s; }}

@keyframes pulse {{
    from {{ transform: scale(1); }}
    to {{ transform: scale(1.02); }}
}}

@keyframes float {{
    0% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-18px); }}
    100% {{ transform: translateY(0px); }}
}}

@keyframes burst {{
    0% {{ transform: scale(0.9) rotate(0deg); opacity: 0.7; }}
    50% {{ transform: scale(1.25) rotate(8deg); opacity: 1; }}
    100% {{ transform: scale(0.9) rotate(0deg); opacity: 0.7; }}
}}

@keyframes fall {{
    0% {{ transform: translateY(-20vh) rotate(0deg); opacity: 1; }}
    100% {{ transform: translateY(120vh) rotate(360deg); opacity: 0; }}
}}
</style>

<div class="floating">{house_info["animation"]}</div>
<div class="floating">{spell_info["emoji"]}</div>
<div class="floating">{house_info["animation"]}</div>
<div class="floating">{spell_info["emoji"]}</div>
<div class="floating">{house_info["animation"]}</div>
""", unsafe_allow_html=True)

st.title("⚡ Interactive Wizarding World")
st.subheader("Your choices shape the magic around you 🪄")

st.markdown(f"""
<div class="magic-card">
    <div class="house-symbol">{house_info["emoji"]}</div>
    <h2 style="text-align:center;">Welcome to {house}</h2>
    <h3 style="text-align:center;">Core Trait: {house_info["trait"]}</h3>
    <p style="text-align:center; font-size:1.2rem;">{house_info["message"]}</p>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("🪄 Spell Chamber")
    st.markdown(f"""
    <div class="magic-card">
        <div class="spell-burst">{spell_info["animation"]}</div>
        <h2>{spell}</h2>
        <p style="font-size:1.2rem;">{spell_info["effect"]}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Cast Spell Again ✨"):
        if "Lumos" in spell:
            st.success("The screen glows brighter! 💡")
        elif "Expelliarmus" in spell:
            st.error("Your opponent's wand flies away! ⚔️")
        elif "Patronum" in spell:
            st.snow()
            st.info("A glowing Patronus charges forward! 🦌")
        elif "Leviosa" in spell:
            st.balloons()
            st.success("The feathers rise into the air! 🪶")
        elif "Alohomora" in spell:
            st.success("The secret door opens! 🔑")
        else:
            st.warning("A stunning flash erupts! 💥")

with col2:
    st.header("🎲 Magical Fate")

    magical_path = st.selectbox(
        "Choose your next adventure:",
        [
            "Forbidden Forest 🌲",
            "Quidditch Pitch 🧹",
            "Potions Class ⚗️",
            "Room of Requirement 🚪",
            "Hogsmeade 🍺"
        ]
    )

    if st.button("Reveal Destiny 🔮"):
        destinies = [
            f"As a {house}, you discover ancient magic in the {magical_path}.",
            f"Your {house_info['trait'].lower()} helps you master {spell}.",
            f"A mysterious owl delivers a message marked with {house_info['emoji']}.",
            f"You cast {spell} and unlock a hidden Hogwarts secret."
        ]
        st.success(random.choice(destinies))

st.divider()

st.header("🏆 House Energy Meter")

power = st.slider("Increase magical energy", 0, 100, 50)

if power < 30:
    st.info(f"{house_info['emoji']} Your magic is calm and quiet.")
elif power < 70:
    st.warning(f"{house_info['emoji']} Your magic is growing stronger.")
else:
    st.success(f"{house_info['emoji']} Full magical surge! {house_info['animation'] * 5}")

st.progress(power)

st.caption("🪄 Built with Streamlit • Mischief Managed")