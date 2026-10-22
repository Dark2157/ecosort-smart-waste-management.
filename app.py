
import streamlit as st

st.set_page_config(
    page_title="EcoSort | Smart Waste Management",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5faf5;
}
h1, h2, h3 {
    color: #205c37;
}
div.stButton > button {
    border-radius: 9px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 EcoSort")
st.subheader("Smart Waste Management & Environmental Education")
st.write(
    "Learn how to segregate waste, reduce pollution, "
    "recycle resources and build a cleaner future."
)

st.sidebar.title("🌍 EcoSort Navigation")
page = st.sidebar.radio(
    "Choose a page",
    [
        "Home",
        "Learn Waste Management",
        "Waste Segregation Guide",
        "Composting Guide",
        "Environmental Impact",
        "Eco Quiz",
        "Green Challenges",
        "About EcoSort"
    ]
)

if page == "Home":
    st.success("Small actions. Cleaner surroundings. Greener future.")

    a, b, c = st.columns(3)
    a.metric("Core Principle", "5 Rs")
    b.metric("Main Goal", "Less Waste")
    c.metric("Future Vision", "Sustainability")

    st.header("Welcome to EcoSort")
    st.write("""
    Waste becomes a serious problem when it is mixed,
    dumped carelessly or sent for inappropriate disposal.

    EcoSort is an educational platform that helps people
    understand responsible waste management.
    """)

    st.subheader("Explore EcoSort")
    st.markdown("""
    - 📚 Learn the fundamentals of waste management
    - ♻️ Understand wet and dry waste segregation
    - 🌿 Discover home composting
    - 🌎 Learn how waste affects our environment
    - 🧠 Test your knowledge with an interactive quiz
    - ✅ Take practical green challenges
    """)

    st.info("Tip: Start with the Waste Segregation Guide.")

elif page == "Learn Waste Management":
    st.header("📚 Learn Waste Management")

    lessons = {
        "1. Introduction to Waste": """
Waste is any material that is discarded after use.
Poor waste management can cause pollution, bad odours,
blocked drains and health problems.

Responsible management includes reducing waste,
segregating it, reusing materials and treating waste safely.
""",
        "2. The 5 Rs": """
REFUSE: Avoid unnecessary items and single-use products.

REDUCE: Buy only what you need and prevent waste.

REUSE: Use containers, bags and other items again.

REPAIR: Fix products instead of replacing them immediately.

RECYCLE: Send suitable materials to recycling systems.
""",
        "3. Waste Segregation": """
Segregation means separating waste according to its type
at the point where it is generated.

Keep wet waste separate from dry recyclables.
Keep sanitary, hazardous and electronic waste separate
and follow local collection instructions.
""",
        "4. Plastic Pollution": """
Plastic can persist in the environment for a long time.
Plastic litter can harm animals and pollute waterways.

Avoid unnecessary plastic, reuse suitable products and
send accepted plastics through authorised collection systems.
""",
        "5. Electronic Waste": """
Old phones, chargers, batteries and computers may contain
valuable materials and substances that need safe handling.

Do not burn or dismantle e-waste yourself.
Use authorised collection or recycling channels.
""",
        "6. Circular Economy": """
A circular economy aims to keep products and materials
in use for longer through repair, reuse and recycling.

It helps reduce the demand for new raw materials and
limits the amount of waste sent for disposal.
"""
    }

    lesson = st.selectbox("Choose a lesson", list(lessons.keys()))
    st.markdown(lessons[lesson])
    st.caption("Learn one topic today and practise it at home.")

elif page == "Waste Segregation Guide":
    st.header("♻️ Waste Segregation Guide")

    st.warning(
        "Follow your local municipal collection rules. "
        "Bin colours and accepted materials can vary."
    )

    with st.expander("🍌 Wet / Biodegradable Waste"):
        st.write("""
        Examples:
        - Fruit and vegetable peels
        - Leftover food
        - Tea leaves and coffee grounds
        - Garden leaves

        What to do: Keep it separate and compost suitable
        organic waste where practical.
        """)

    with st.expander("📦 Dry Recyclable Waste"):
        st.write("""
        Examples:
        - Clean paper and cardboard
        - Accepted plastic packaging
        - Glass bottles and metal cans

        What to do: Keep recyclables reasonably clean and dry.
        Follow your local recycler's acceptance rules.
        """)

    with st.expander("🩹 Sanitary and Domestic Special Waste"):
        st.write("""
        Examples:
        - Sanitary pads and diapers
        - Expired household products
        - Broken household items requiring special handling

        What to do: Wrap and separate sanitary waste as
        required by local rules. Never mix it with compost.
        """)

    with st.expander("🔋 E-waste and Batteries"):
        st.write("""
        Examples:
        - Phones and chargers
        - Computers and electronic accessories
        - Used batteries

        What to do: Keep separate and use authorised
        e-waste or battery collection facilities.
        Never burn batteries or put them in a fire.
        """)

elif page == "Composting Guide":
    st.header("🌿 Simple Home Composting")

    st.write("Composting converts suitable organic waste into a useful soil amendment.")

    steps = [
        "Choose a ventilated compost bin.",
        "Add fruit and vegetable scraps in suitable quantities.",
        "Mix with dry leaves, shredded cardboard or other suitable dry material.",
        "Maintain moisture similar to a wrung-out sponge.",
        "Turn or mix periodically to provide air.",
        "Allow the material to decompose before using finished compost."
    ]

    for i, step in enumerate(steps, 1):
        st.write(f"**Step {i}:** {step}")

    st.info(
        "Avoid meat, dairy and oily foods in a basic home "
        "compost setup unless the system is designed for them."
    )

elif page == "Environmental Impact":
    st.header("🌎 Why Waste Management Matters")

    st.subheader("Effects of Poor Waste Disposal")
    st.markdown("""
    - **Soil pollution:** Improperly dumped waste can contaminate land.
    - **Water pollution:** Litter and leachate can reach water bodies.
    - **Air pollution:** Open burning releases harmful pollutants.
    - **Climate impact:** Organic waste in landfills can generate methane.
    - **Public health:** Piles of waste can attract pests and block drains.
    """)

    st.subheader("How We Can Help")
    st.markdown("""
    - Carry reusable bags and bottles.
    - Avoid wasting food.
    - Segregate waste at home and college.
    - Repair, reuse and recycle suitable materials.
    - Never burn waste or dump it into waterways.
    """)

elif page == "Eco Quiz":
    st.header("🧠 EcoSort Knowledge Quiz")
    st.write("Answer all five questions and test your knowledge.")

    questions = [
        (
            "1. What should you do before recycling suitable packaging?",
            ["Mix it with food waste", "Follow local rules and clean it if needed",
             "Burn it", "Throw it into a river"],
            "Follow local rules and clean it if needed"
        ),
        (
            "2. Which is usually suitable for composting?",
            ["Fruit peels", "A mobile phone", "A battery", "Glass"],
            "Fruit peels"
        ),
        (
            "3. What is the purpose of waste segregation?",
            ["To mix all waste", "To make recycling and treatment easier",
             "To increase litter", "To burn more waste"],
            "To make recycling and treatment easier"
        ),
        (
            "4. Where should old electronics go?",
            ["Into a river", "Into compost", "To an authorised e-waste collection point",
             "Into a fire"],
            "To an authorised e-waste collection point"
        ),
        (
            "5. Which action helps reduce waste?",
            ["Buying unnecessary items", "Using disposable items every time",
             "Repairing and reusing products", "Littering"],
            "Repairing and reusing products"
        )
    ]

    with st.form("eco_quiz"):
        answers = []
        for question, options, correct in questions:
            answer = st.radio(question, options, key=question)
            answers.append(answer)

        submitted = st.form_submit_button("Check My Score")

    if submitted:
        score = sum(
            answer == question[2]
            for answer, question in zip(answers, questions)
        )
        st.session_state["eco_score"] = score
        st.subheader(f"Your score: {score} / {len(questions)}")

        if score == len(questions):
            st.balloons()
            st.success("Excellent! You're an EcoSort champion.")
        elif score >= 3:
            st.success("Good work! Keep learning and practising.")
        else:
            st.info("Review the learning sections and try again.")

        with st.expander("View correct answers"):
            for question, options, correct in questions:
                st.write(f"**{question}**")
                st.write(f"Correct answer: {correct}")

elif page == "Green Challenges":
    st.header("✅ Your Green Action Challenges")
    st.write("Select actions you plan to practise. Start small and build habits.")

    challenges = [
        "Carry a reusable water bottle.",
        "Avoid unnecessary single-use plastic.",
        "Separate wet and dry waste.",
        "Reuse paper when possible.",
        "Avoid wasting food.",
        "Learn where local e-waste is collected.",
        "Keep your surroundings litter-free.",
        "Encourage a friend to segregate waste.",
        "Reuse a bag while shopping.",
        "Try composting suitable kitchen scraps."
    ]

    if "completed_challenges" not in st.session_state:
        st.session_state["completed_challenges"] = []

    for challenge in challenges:
        checked = challenge in st.session_state["completed_challenges"]
        new_value = st.checkbox(challenge, value=checked, key=challenge)

        if new_value and challenge not in st.session_state["completed_challenges"]:
            st.session_state["completed_challenges"].append(challenge)
        elif not new_value and challenge in st.session_state["completed_challenges"]:
            st.session_state["completed_challenges"].remove(challenge)

    completed = len(st.session_state["completed_challenges"])
    st.progress(completed / len(challenges))
    st.write(f"Challenges selected: {completed} / {len(challenges)}")

elif page == "About EcoSort":
    st.header("🌱 About EcoSort")

    st.write("""
    EcoSort is a Smart Waste Management and Environmental
    Education project developed to encourage responsible
    waste segregation and sustainable daily habits.
    """)

    st.subheader("Project Objectives")
    st.markdown("""
    1. Educate users about different waste categories.
    2. Explain practical waste segregation methods.
    3. Encourage recycling, reuse and composting.
    4. Raise awareness about environmental pollution.
    5. Make learning interactive through quizzes and challenges.
    """)

    st.subheader("Technology Used")
    st.markdown("""
    - Python
    - Streamlit
    - Interactive web interface
    """)

    st.caption(
        "EcoSort is an educational project. It does not use AI "
        "or a camera to identify waste."
    )

    st.subheader("Useful Official Resources")
    st.markdown("""
    - [Central Pollution Control Board](https://cpcb.nic.in/)
    - [Ministry of Environment, Forest and Climate Change](https://moef.gov.in/)
    - [Swachh Bharat Mission - Urban](https://sbmurban.org/)
    """)

st.sidebar.divider()
st.sidebar.caption("EcoSort | Learn • Segregate • Reuse • Recycle")
st.sidebar.caption("A cleaner environment starts with us.")
