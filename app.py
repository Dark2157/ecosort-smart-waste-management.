
import streamlit as st

st.set_page_config(
    page_title="EcoSort | Smart Waste Management",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- DESIGN --------------------
st.markdown("""
<style>
.stApp {
    background: #f5faf5;
    color: #193321;
}
[data-testid="stSidebar"] {
    background: #e7f2e7;
}
h1, h2, h3 {
    color: #205c37 !important;
}
.hero {
    padding: 28px;
    border-radius: 18px;
    background: linear-gradient(120deg, #dff3df, #f1f9e9);
    border: 1px solid #c9e3c9;
    margin-bottom: 20px;
}
.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 8px;
}
.small-note {
    color: #55705c;
    font-size: 0.9rem;
}
div.stButton > button {
    border-radius: 9px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SESSION PROGRESS --------------------
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None
if "completed_challenges" not in st.session_state:
    st.session_state.completed_challenges = []
if "action_plan" not in st.session_state:
    st.session_state.action_plan = []

# -------------------- NAVIGATION --------------------
st.sidebar.markdown("# 🌱 EcoSort")
st.sidebar.caption("Smart Waste Management & Environmental Education")
st.sidebar.divider()

pages = [
    "Home Dashboard",
    "Learning Library",
    "Wet Waste",
    "Dry Waste & Recycling",
    "Sanitary & Special Waste",
    "Composting Guide",
    "Waste Treatment Methods",
    "Environmental Impact",
    "India Rules & Resources",
    "Eco Quiz",
    "Eco Challenges",
    "My Green Action Plan",
    "About EcoSort",
]

page = st.sidebar.radio("Explore EcoSort", pages)
st.sidebar.divider()
st.sidebar.caption("♻️ Learn • Segregate • Reduce • Reuse")

# -------------------- CONTENT DATA --------------------
lessons = {
    "Introduction to Waste Management": """
Waste management is the collection, segregation, transport,
processing and safe disposal of waste.

Poor waste management can pollute air, soil and water,
block drains, attract pests and harm public health.

Good waste management begins where waste is generated:
at home, in college, in offices and in public places.
""",
    "The 5 Rs": """
**Refuse:** Avoid unnecessary items and single-use products.

**Reduce:** Buy thoughtfully and prevent waste.

**Reuse:** Use suitable products more than once.

**Repair:** Fix items instead of replacing them unnecessarily.

**Recycle:** Send accepted materials to appropriate recycling systems.

The best option is usually to prevent waste before it is created.
""",
    "Waste Segregation": """
Segregation means separating waste into different categories
at the point where it is generated.

Keep wet waste separate from dry recyclables.
Keep sanitary, hazardous and electronic waste separate
and follow the collection instructions in your locality.

Mixing waste can contaminate recyclable materials and make
safe treatment more difficult.
""",
    "Plastic Pollution": """
Plastic litter can remain in the environment for a long time.
It can injure wildlife, pollute waterways and break down into
smaller pieces, including microplastics.

Choose reusable alternatives when practical, avoid unnecessary
packaging and follow local plastic collection and recycling rules.
Never burn plastic waste in the open.
""",
    "E-waste and Batteries": """
Electronic waste includes discarded phones, computers,
chargers, cables and other electrical or electronic products.

Batteries may contain materials that require careful handling.
Do not burn, dismantle or throw batteries into fires.

Keep e-waste separate and use authorised collection or
recycling channels.
""",
    "Landfills and Waste Treatment": """
A landfill is a managed site for disposing of waste that cannot
be prevented, reused, recycled or otherwise recovered.

Poorly managed dumping sites can cause odour, leachate,
air pollution and methane emissions.

Waste prevention, segregation, recycling and suitable treatment
can reduce the amount sent for final disposal.
""",
    "Circular Economy": """
A circular economy aims to keep materials and products in use
for as long as possible.

Repair, refill, share, reuse and recycle where appropriate.
These practices can reduce demand for virgin resources and
limit waste generation.

Products should be designed and used with their entire
life cycle in mind.
""",
    "Waste and Public Health": """
Open dumping and blocked drains can encourage pests and
contribute to unhealthy surroundings.

Open burning can release harmful smoke and pollutants.
Unsafe handling of sanitary waste, chemicals and batteries
can also create risks.

Use appropriate protective measures and follow local
collection and disposal guidance.
""",
}

challenges = [
    "Carry a reusable water bottle.",
    "Use a reusable shopping bag.",
    "Segregate wet and dry waste at home.",
    "Avoid wasting food today.",
    "Reuse paper when possible.",
    "Learn where your local e-waste is collected.",
    "Keep your classroom or study area litter-free.",
    "Encourage a friend to segregate waste.",
    "Avoid unnecessary single-use packaging.",
    "Try composting suitable kitchen scraps.",
]

# -------------------- HOME DASHBOARD --------------------
if page == "Home Dashboard":
    st.markdown("""
    <div class="hero">
        <h1>🌱 Welcome to EcoSort</h1>
        <p><b>Small actions. Cleaner surroundings. Greener future.</b></p>
        <p>An interactive learning platform for responsible
        waste management and environmental awareness.</p>
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)
    a.metric("Learning Topics", len(lessons))
    b.metric("Green Challenges", len(challenges))
    c.metric("Challenges Completed", len(st.session_state.completed_challenges))

    st.header("Your journey towards a greener future")
    left, right = st.columns(2)

    with left:
        st.subheader("📚 Learn")
        st.write("Understand waste categories, the 5 Rs, pollution and circular economy.")
        st.subheader("♻️ Segregate")
        st.write("Learn how to handle wet waste, dry recyclables and special waste.")
        st.subheader("🌿 Take Action")
        st.write("Explore composting and choose practical environmental habits.")

    with right:
        st.subheader("🧠 Test Yourself")
        st.write("Complete the Eco Quiz and check your understanding.")
        st.subheader("✅ Build Better Habits")
        st.write("Track the green challenges you choose to complete.")
        st.subheader("🌎 Understand the Impact")
        st.write("Discover how responsible waste management helps communities.")

    st.info("Start with the Learning Library, then explore the segregation guides.")

# -------------------- LEARNING LIBRARY --------------------
elif page == "Learning Library":
    st.title("📚 Learning Library")
    st.write("Choose a topic to understand waste management step by step.")

    selected_lesson = st.selectbox("Select a lesson", list(lessons.keys()))
    st.markdown(lessons[selected_lesson])

    st.divider()
    st.subheader("Quick learning check")

    question = st.radio(
        "What should generally happen before waste is sent for disposal?",
        [
            "Mix all types of waste together",
            "Prevent waste and separate suitable materials",
            "Burn everything",
            "Dump everything into a water body",
        ],
        key="library_check",
    )

    if st.button("Check answer", key="library_answer"):
        if question == "Prevent waste and separate suitable materials":
            st.success("Correct! Prevention and segregation help improve waste management.")
        else:
            st.warning("Try again. Think about reducing waste and keeping materials separate.")

# -------------------- WET WASTE --------------------
elif page == "Wet Waste":
    st.title("🍌 Wet Waste Management")
    st.write("Wet waste often includes biodegradable organic materials.")

    st.subheader("Common examples")
    st.markdown("""
    - Fruit and vegetable peels
    - Leftover food
    - Tea leaves and coffee grounds
    - Suitable garden leaves and plant trimmings
    """)

    st.subheader("How to manage it")
    st.markdown("""
    1. Keep wet waste separate from dry recyclables.
    2. Avoid mixing it with batteries, chemicals or sanitary waste.
    3. Compost suitable organic material where practical.
    4. Follow your local municipal collection arrangements.
    """)

    st.info("Not every organic item belongs in every composting system. Follow the system's instructions.")

# -------------------- DRY WASTE --------------------
elif page == "Dry Waste & Recycling":
    st.title("📦 Dry Waste & Recycling")

    st.subheader("Common recyclable materials")
    st.markdown("""
    - Clean paper and cardboard
    - Accepted plastic packaging
    - Glass bottles and jars
    - Metal cans and suitable scrap metal
    """)

    st.subheader("Good recycling habits")
    st.markdown("""
    1. Keep dry recyclables separate from wet waste.
    2. Empty containers and clean them when required.
    3. Keep paper and cardboard dry.
    4. Check which materials your local recycler accepts.
    5. Use authorised collection systems for materials needing special handling.
    """)

    st.warning("Recycling acceptance varies by location and material. Check local instructions.")

# -------------------- SANITARY & SPECIAL WASTE --------------------
elif page == "Sanitary & Special Waste":
    st.title("🩹 Sanitary & Special Waste")

    st.subheader("Sanitary waste")
    st.write("""
    Examples include sanitary pads and diapers. Wrap and separate
    them according to local collection guidance. Do not place them
    in compost intended for gardens.
    """)

    st.subheader("Household hazardous waste")
    st.write("""
    Some cleaners, paints, solvents, pesticides and similar products
    require special handling. Keep them in their original labelled
    containers where safe, and follow local disposal instructions.
    Do not pour hazardous products into drains unless their label
    and local guidance explicitly permit it.
    """)

    st.subheader("Batteries and electronic waste")
    st.write("""
    Keep used batteries and discarded electronics separate.
    Do not burn, crush or dismantle them. Use authorised collection
    points or recycling services.
    """)

# -------------------- COMPOSTING --------------------
elif page == "Composting Guide":
    st.title("🌿 Home Composting Guide")
    st.write("Composting allows suitable organic material to decompose into a useful soil amendment.")

    steps = [
        ("Choose a container", "Use a suitable bin with ventilation and drainage appropriate to the system."),
        ("Add organic material", "Add fruit and vegetable scraps and other accepted organic materials."),
        ("Balance the mixture", "Mix with dry leaves or shredded untreated cardboard."),
        ("Maintain moisture", "Aim for moisture similar to a wrung-out sponge."),
        ("Provide air", "Turn or mix the material periodically when the method requires it."),
        ("Allow time", "Let the material decompose before using finished compost."),
    ]

    for number, (heading, detail) in enumerate(steps, start=1):
        st.markdown(f"**Step {number}: {heading}**")
        st.write(detail)

    st.warning("""
    A basic home compost bin generally excludes meat, dairy and oily foods.
    Follow the instructions for your specific composting method.
    """)

# -------------------- TREATMENT METHODS --------------------
elif page == "Waste Treatment Methods":
    st.title("🏭 Waste Treatment Methods")

    methods = {
        "Composting": "Biological decomposition of suitable organic waste under managed conditions.",
        "Biomethanation": "Microorganisms break down organic material without oxygen, producing biogas and digestate.",
        "Material Recovery": "Useful materials are sorted and recovered for reuse or recycling.",
        "Recycling": "Accepted waste materials are processed into material that can be used again.",
        "Waste-to-Energy": "Certain residual waste may be processed for energy recovery under suitable pollution controls.",
        "Sanitary Landfilling": "Engineered disposal for residual waste that cannot reasonably be recovered or treated further.",
    }

    for method, description in methods.items():
        with st.expander(method):
            st.write(description)

    st.info("Treatment choice depends on waste composition, local infrastructure, cost and environmental safeguards.")

# -------------------- ENVIRONMENTAL IMPACT --------------------
elif page == "Environmental Impact":
    st.title("🌎 Environmental Impact")

    impacts = [
        ("🌱 Soil", "Improperly dumped waste can degrade land and contaminate soil."),
        ("💧 Water", "Litter and leachate can pollute water bodies."),
        ("🌬️ Air", "Open waste burning releases harmful smoke and pollutants."),
        ("🌡️ Climate", "Organic waste in landfills can generate methane."),
        ("🏥 Public Health", "Unmanaged waste can attract pests and contribute to blocked drains."),
        ("🐾 Wildlife", "Animals can ingest litter or become entangled in waste."),
    ]

    for heading, description in impacts:
        with st.expander(heading):
            st.write(description)

    st.subheader("Actions that make a difference")
    st.markdown("""
    - Prevent unnecessary waste.
    - Reuse and repair suitable products.
    - Segregate waste at its source.
    - Recycle materials accepted by local services.
    - Compost suitable organic waste.
    - Never burn waste or dump it into drains and waterways.
    """)

# -------------------- INDIA RESOURCES --------------------
elif page == "India Rules & Resources":
    st.title("🇮🇳 India: Rules & Resources")

    st.write("""
    Waste management in India is governed by national legislation,
    rules and local implementation arrangements. Requirements can
    change, so consult official sources for current guidance.
    """)

    st.subheader("Official resources")
    st.markdown("""
    - [Central Pollution Control Board (CPCB)](https://cpcb.nic.in/)
    - [Ministry of Environment, Forest and Climate Change (MoEFCC)](https://moef.gov.in/)
    - [Swachh Bharat Mission - Urban](https://sbmurban.org/)
    - [Maharashtra Pollution Control Board (MPCB)](https://mpcb.gov.in/)
    """)

    st.subheader("Responsible practices")
    st.markdown("""
    - Follow the waste collection system provided by your municipality.
    - Separate waste as instructed by local authorities.
    - Use authorised channels for e-waste and batteries.
    - Check official notifications for applicable rules and updates.
    """)

    st.caption("This page is for education and is not a substitute for official legal guidance.")

# -------------------- QUIZ --------------------
elif page == "Eco Quiz":
    st.title("🧠 EcoSort Knowledge Quiz")
    st.write("Answer all eight questions and check your knowledge.")

    questions = [
        ("What is the best first step in waste management?",
         ["Burn all waste", "Prevent unnecessary waste", "Dump waste", "Mix everything"],
         "Prevent unnecessary waste"),
        ("Which is usually suitable for a basic compost bin?",
         ["Fruit peels", "Batteries", "Glass", "Electronic devices"],
         "Fruit peels"),
        ("Why is waste segregation important?",
         ["It improves suitable recovery and treatment", "It increases litter",
          "It makes all waste hazardous", "It prevents recycling"],
         "It improves suitable recovery and treatment"),
        ("Where should old electronics be taken?",
         ["A river", "A fire", "An authorised e-waste collection point", "A compost bin"],
         "An authorised e-waste collection point"),
        ("Which action supports reuse?",
         ["Discarding a usable bag", "Using a suitable bag again",
          "Burning paper", "Buying unnecessary items"],
         "Using a suitable bag again"),
        ("What should you do with dry paper for recycling?",
         ["Keep it dry and follow local collection rules", "Soak it in oil",
          "Mix it with batteries", "Burn it"],
         "Keep it dry and follow local collection rules"),
        ("What can open waste burning cause?",
         ["Cleaner air", "Air pollution", "More recycling", "Less smoke"],
         "Air pollution"),
        ("What does a circular economy aim to do?",
         ["Keep products and materials in use longer", "Create more litter",
          "End all repair", "Mix all materials together"],
         "Keep products and materials in use longer"),
    ]

    with st.form("ecosort_quiz_form"):
        answers = []
        for i, (question, options, correct) in enumerate(questions):
            answer = st.radio(question, options, key=f"quiz_{i}")
            answers.append(answer)

        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        score = sum(
            answer == item[2]
            for answer, item in zip(answers, questions)
        )
        st.session_state.quiz_score = score

        st.subheader(f"Your score: {score} / {len(questions)}")

        if score == len(questions):
            st.balloons()
            st.success("Perfect score! You're an EcoSort champion.")
        elif score >= 6:
            st.success("Great work! You have a strong understanding of the topic.")
        elif score >= 4:
            st.info("Good start. Review the Learning Library to improve.")
        else:
            st.warning("Keep learning and try again.")

        with st.expander("Review correct answers"):
            for question, options, correct in questions:
                st.write(f"**{question}**")
                st.write(f"Correct answer: {correct}")

# -------------------- CHALLENGES --------------------
elif page == "Eco Challenges":
    st.title("✅ Eco Challenges")
    st.write("Choose the environmental habits you have completed.")

    for i, challenge in enumerate(challenges):
        is_checked = challenge in st.session_state.completed_challenges
        checked = st.checkbox(
            challenge,
            value=is_checked,
            key=f"challenge_{i}",
        )

        if checked and challenge not in st.session_state.completed_challenges:
            st.session_state.completed_challenges.append(challenge)
        elif not checked and challenge in st.session_state.completed_challenges:
            st.session_state.completed_challenges.remove(challenge)

    total = len(challenges)
    completed = len(st.session_state.completed_challenges)

    st.divider()
    st.progress(completed / total)
    st.write(f"**Progress: {completed} of {total} challenges**")

    if completed == total:
        st.balloons()
        st.success("Amazing! You've checked off every green challenge.")

    if st.button("Reset challenge selections"):
        st.session_state.completed_challenges = []
        st.rerun()

# -------------------- ACTION PLAN --------------------
elif page == "My Green Action Plan":
    st.title("📝 My Green Action Plan")
    st.write("Create a practical plan for your home, college or community.")

    with st.form("action_plan_form"):
        activity = st.text_input(
            "What action will you take?",
            placeholder="Example: Separate wet and dry waste at home",
        )
        frequency = st.selectbox(
            "How often?",
            ["Daily", "Weekly", "Monthly", "One-time activity"],
        )
        location = st.selectbox(
            "Where?",
            ["Home", "College", "Community", "Other"],
        )
        submit_plan = st.form_submit_button("Add to My Plan")

    if submit_plan:
        if activity.strip():
            st.session_state.action_plan.append({
                "activity": activity.strip(),
                "frequency": frequency,
                "location": location,
            })
            st.success("Action added to your plan.")
        else:
            st.warning("Please enter an action first.")

    st.subheader("My commitments")

    if not st.session_state.action_plan:
        st.info("Your plan is empty. Add your first green action above.")
    else:
        for i, item in enumerate(st.session_state.action_plan, start=1):
            st.markdown(f"**{i}. {item['activity']}**")
            st.caption(f"{item['frequency']} • {item['location']}")

# -------------------- ABOUT --------------------
elif page == "About EcoSort":
    st.title("🌱 About EcoSort")

    st.markdown("""
    <div class="hero">
        <h2>EcoSort — Smart Waste Management & Environmental Education</h2>
        <p>Learn how to segregate waste, reduce pollution and build sustainable habits.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Project objectives")
    st.markdown("""
    1. Educate users about different categories of waste.
    2. Explain practical waste segregation.
    3. Encourage reuse, recycling and composting.
    4. Raise awareness about pollution and public health.
    5. Make learning interactive through quizzes and challenges.
    """)

    st.subheader("Technology used")
    st.markdown("""
    - **Python:** Application logic
    - **Streamlit:** Interactive web interface
    - **GitHub:** Source code hosting
    - **Streamlit Community Cloud:** Online deployment
    """)

    st.subheader("Project scope")
    st.write("""
    EcoSort is an educational platform. It does not use a camera
    or AI model to identify waste. It helps users learn about
    responsible waste management and environmental practices.
    """)

    st.caption("EcoSort • Learn today, protect tomorrow.")
