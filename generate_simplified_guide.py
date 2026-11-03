"""
generate_simplified_guide.py
Generates both a Word (.docx) and Markdown (.md) document titled:
"LandfillPlume-AI: The Plain-English Guide to Research Paper Phrases & Complex Concepts"
Explaining heavy technical academic phrases in simple, conversational language with real-world analogies,
practical code examples, and 'Viva / Mentor Defense' cheat-sheets.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = r"C:\Users\rghos\OneDrive - Vivekananda Institute of Professional Studies\PROJECTS\Christ\Machine Learning\Poisonous Gas Identification Research Paper"
DOCX_OUT = os.path.join(BASE_DIR, "RESEARCH_PHRASES_SIMPLIFIED_GUIDE.docx")
MD_OUT = os.path.join(BASE_DIR, "RESEARCH_PHRASES_SIMPLIFIED_GUIDE.md")

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_callout_box(doc, title, content_paragraphs, border_color="E34A32", bg_color="F8FAFC"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="none"/><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:bottom w:val="none"/><w:right w:val="none"/></w:tblBorders>')
    tblPr.append(borders)
    
    # Title paragraph
    p0 = cell.paragraphs[0]
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(4)
    r_t = p0.add_run(title)
    r_t.bold = True
    r_t.font.name = "Arial"
    r_t.font.size = Pt(10.5)
    r_t.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    # Subsequent paragraphs
    for p_text in content_paragraphs:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(p_text)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    
    # Blank space after table
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)

def build_documents():
    doc = docx.Document()
    
    # Page Margins: 0.8 in
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Document Title Block
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("LandfillPlume-AI: The Plain-English Translation Guide")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(20)
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("De-jargonizing Complex Research Phrases, Mathematical Formulations, and Examiner Viva Questions")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = RGBColor(0xE3, 0x4A, 0x32)
    r_sub.bold = True

    # Introductory Note
    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.space_after = Pt(12)
    p_intro.paragraph_format.line_spacing = 1.15
    r_i = p_intro.add_run(
        "Academic papers must be written in formal, rigorous language for IEEE standards and peer-reviewers. "
        "However, when explaining your project to mentors, external examiners, or interviewers, using pure jargon without understanding can be risky. "
        "This guide translates every heavy phrase in your paper into clear, everyday concepts, relatable analogies, and 30-second viva answers."
    )
    r_i.font.name = "Calibri"
    r_i.font.size = Pt(10)
    r_i.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # List of Topics
    topics = [
        {
            "num": "1",
            "phrase": "Physics-Informed Machine Learning (PIML) & Physics-Informed Feature Engineering",
            "where": "Title, Abstract, Section II-C, and Section III-B",
            "plain": "Teaching real-world laws of nature (fluid dynamics, geography, and thermodynamics) to a machine learning model instead of letting it guess purely from random spreadsheet numbers.",
            "analogy": "Imagine teaching a child to catch an apple falling from a tree:\n• A 'Pure Black-Box AI' watches 10,000 video clips of falling apples and memorizes pixel patterns. If you drop the apple on a windy day or on a hill, it gets completely confused because it has no idea gravity exists!\n• A 'Physics-Informed AI (PIML)' is already given the law of gravity (g = 9.8 m/s²) and wind resistance formulas. The AI only has to learn the small, unpredictable flutter of the leaves.\nIn our project, we didn't just give the AI raw temperatures and wind numbers; we hardcoded atmospheric advection, compass geometry, and nocturnal thermal inversion formulas into the features.",
            "math": "Traditional Pure-Data ML: Y = f(X_raw) where X_raw = [Temp, Humidity, WindSpeed, WindDirection].\nPhysics-Informed ML (PIML) Formulation (Karniadakis et al., Nature Reviews Physics, 2021):\nY = f(X_raw, Φ_physics(X))\nWhere Φ_physics embeds governing transport equations:\n1. Advection Conservation: (u, v) = (-WS*sin(WD), -WS*cos(WD))\n2. Geographic Plume Vector: cos(WD - 130°)\n3. Boundary Stagnation: Alignment * exp(-0.25*WS)\n4. Ventilation Volume: [WS * (T + 273.15)] / (P + ε)",
            "why": "Pure machine learning models suffer from 'physical hallucinations'—for example, predicting a massive toxic gas spike when the wind is blowing backward away from the landfill, or failing to predict nighttime choking episodes because vehicle traffic is zero. PIML forces the AI to obey physical reality.",
            "viva": "Examiner: 'What exactly makes your project Physics-Informed Machine Learning (PIML) rather than standard machine learning?'\nAnswer: 'Standard machine learning treats environmental sensor data as arbitrary tabular numbers with no awareness of spatial geography or fluid dynamics. Following the PIML paradigm of Karniadakis et al. (2021), we embedded governing principles of atmospheric advection and boundary-layer thermodynamics directly into our feature representation. We projected polar wind angles into orthogonal Cartesian velocity vectors (u, v) to eliminate circular discontinuities, formulated a half-wave rectified geometric alignment vector centered on Ghazipur's 130° azimuth, and constructed stagnation proxies. This physically constrained our models, preventing unphysical hallucinations and achieving R² = 0.9293.'"
        },
        {
            "num": "2",
            "phrase": "Cartesian Wind Vector Components (u, v)",
            "where": "Abstract & Section III-B (Physics-Informed Feature Engineering)",
            "plain": "Converting standard weather wind reports (like 'Wind from 135° at 2 m/s') into simple horizontal 'Left/Right' (East/West) and 'Up/Down' (North/South) speeds.",
            "analogy": "Imagine walking on a circular running track. Degree 359° is one step before Degree 0°. They are right next to each other! But to a computer reading numbers, 359 and 0 look completely opposite. If you tell a robot to make a cut, it gets confused. By splitting wind into 'East-West speed (u)' and 'North-South speed (v)', the speed numbers change smoothly with no sudden jumps.",
            "math": "u = -WS * sin(π * WD / 180)  [East-West speed]\nv = -WS * cos(π * WD / 180)  [North-South speed]\n(The minus sign is standard meteorology because wind direction is where the wind COMES FROM, not where it is heading).",
            "why": "Standard Decision Trees (Random Forest, XGBoost) fail badly when dealing with angles near 360°/0°. Decomposing into u and v eliminates this 'circular wrap-around discontinuity' and gives models realistic fluid motion physics.",
            "viva": "Examiner: 'Why did you decompose wind into u and v instead of feeding wind direction directly?'\nAnswer: 'Wind direction has a circular boundary problem where 360° and 0° are physically identical but mathematically far apart. Tree models create artificial splits at boundary thresholds. Projecting wind into Cartesian orthogonal vectors (u, v) creates smooth, continuous numerical features that reflect actual atmospheric fluid advection.'"
        },
        {
            "num": "3",
            "phrase": "130.0° Geometric Plume Alignment Index",
            "where": "Abstract & Section III-B (Physics-Informed Feature Engineering)",
            "plain": "A custom score from 0.0 to 1.0 that answers one simple question: 'Is the wind blowing directly from the Ghazipur garbage dump toward our monitoring station right now?'",
            "analogy": "Imagine standing in front of a giant leaf blower. If the blower points straight at your face, you get 100% of the blast (Index = 1.0). If it turns sideways, you get 0% (Index = 0.0). Ghazipur is located at an angle of 130° (South-East) relative to Anand Vihar. When the wind blows from 130°, the toxic plume hits the station directly.",
            "math": "Angle Difference: Δθ = min(|Wind_Dir - 130°|, 360° - |Wind_Dir - 130°|)\nAlignment Index = max(0, cos(Δθ))\n• Wind at 130° -> cos(0°) = 1.0 (Direct hit!)\n• Wind at 220° (90° crosswind) -> cos(90°) = 0.0 (Zero landfill impact)\n• Wind from opposite direction -> 0.0 (Clean baseline)",
            "why": "Without this index, an ML algorithm has no idea where the Ghazipur landfill is located on a map. This index injects real-world geography directly into the mathematical model.",
            "viva": "Examiner: 'What is this 130.0° index and how did you choose 130°?'\nAnswer: '130° is the precise geographic azimuth from the DPCC Anand Vihar sensor station back to the Ghazipur landfill centroid (2.8 km away). The alignment index uses cosine similarity to quantify how directly the wind vector aligns with this corridor, giving our models an explicit physical indicator of landfill plume advection.'"
        },
        {
            "num": "4",
            "phrase": "Atmospheric Ventilation and Stagnation Proxies",
            "where": "Abstract, Section III-B, and Section IV-A",
            "plain": "Formulas that calculate whether toxic air is blowing away or trapped like a poison bubble over neighborhoods because the air is still and heavy.",
            "analogy": "If you spray perfume inside a windy garden, you smell almost nothing because it disperses instantly. But if you spray perfume in a closed, cold basement with no windows or fans, the scent lingers and concentrates for hours. In Delhi, winter nights act like that closed room: calm wind + cold ground = toxic gases pool on the ground.",
            "math": "Dispersion Index = Alignment_Index * exp(-0.25 * Wind_Speed)\nVentilation Index Proxy = [Wind_Speed * (Temp + 273.15)] / (Pressure + ε)\n• Direct alignment + Calm wind (0.5 m/s) -> Index peaks near 1.0 (Maximum Danger).\n• Direct alignment + Strong wind (5.0 m/s) -> Index drops near 0.2 (Diluted by wind).",
            "why": "A direct wind direction alone does not mean high pollution; if the wind is fast, it blows the smoke away. Stagnation proxies teach the model that 'low wind speed + direct dump alignment' is the most dangerous combination.",
            "viva": "Examiner: 'Why do you need a stagnation proxy if the model already has wind speed as an input?'\nAnswer: 'Atmospheric dispersion is non-linear. High concentrations occur through the multiplicative interaction of direct plume alignment and low ventilation volume. The stagnation proxy combines alignment and aerodynamic attenuation into a single physics-informed proxy, avoiding recursive lead-time error in gradient boosters.'"
        },
        {
            "num": "5",
            "phrase": "Real-Time Local SHAP Waterfall Decomposition",
            "where": "Abstract, Section III-D, and Web Dashboard",
            "plain": "A step-by-step breakdown receipt that shows exactly why the AI predicted a specific number right now (e.g., 'Base average is 40 µg/m³; +18 µg/m³ because wind is from Ghazipur; +12 µg/m³ because it's 3 AM; -5 µg/m³ because humidity is low -> Final Forecast: 65 µg/m³').",
            "analogy": "Think of an itemized grocery bill. Your total bill is $65. The receipt explains: Bread: +$40 (base average), Eggs: +$18 (wind from Ghazipur), Milk: +$12 (cold night), Coupon discount: -$5 (low humidity). A 'waterfall plot' visually stacks these positive and negative contributors like a cascading waterfall from start to finish.",
            "math": "Based on cooperative game theory (Shapley values from Lloyd Shapley, Nobel Prize in Economics):\nPrediction f(x) = Base_Value φ0 + ∑ φi(feature_i)\nEach feature is treated as a 'player' in a team game, and is awarded credit (Shapley value φ) based on its exact marginal contribution to the prediction.",
            "why": "Machine learning models are usually 'black boxes'—they give an answer, but nobody knows why. If an AI triggers an evacuation siren, city officials need legal and scientific proof of *why* it triggered. Local SHAP provides that audit trail for every single 15-minute prediction.",
            "viva": "Examiner: 'What is a SHAP waterfall plot and why did you use it?'\nAnswer: 'TreeSHAP decomposes a single tree-ensemble prediction into additive Shapley values. The waterfall plot visually shows the step-by-step transition from the dataset base expectation to the current output, explicitly quantifying how much the Ghazipur alignment, thermal inversion, and lag momentum pushed the forecast up or down.'"
        },
        {
            "num": "6",
            "phrase": "Satellite-Ground Sensor Fusion (Multimodal Telemetry)",
            "where": "Title, Abstract, and Section III-A",
            "plain": "Combining space satellite cameras that take big pictures once every few weeks with ground sensors on street poles that take measurements every 15 minutes.",
            "analogy": "Satellites are like police helicopters: they can see the whole city and spot the exact smoking factory from above, but they only fly over once a week. Ground stations are like security guards standing on the sidewalk: they take your temperature every 15 minutes, but they have no idea what is happening 5 miles away. We combined both so the system has 24/7 continuous awareness plus high-altitude bird's-eye confirmation.",
            "math": "We harmonized 23 episodic satellite overpass records from NASA EMIT (ISS) and ESA EnMAP (point-source flux in kg/hr) with 70,176 continuous ground-level rows from DPCC Anand Vihar (concentrations in µg/m³ and ppm).",
            "why": "Ground sensors cannot prove *who* emitted the gas (they just smell smoke). Satellites prove the dump is emitting 4,890 kg/hr of methane, but miss daily spikes due to orbital revisits. Fusion solves both problems.",
            "viva": "Examiner: 'How did you fuse satellite data with ground data given their vast difference in revisit times?'\nAnswer: 'Satellites provide episodic point-source emission rates (Q in kg/hr) that calibrate and validate our physical dispersion vectors, while ground CAAQMS stations provide the high-frequency 15-minute time-series for continuous ML training. This decoupled spatial source verification from real-time temporal forecasting.'"
        },
        {
            "num": "7",
            "phrase": "Methane Super-Emitters & Integrated Methane Enhancement (IME)",
            "where": "Abstract & Section II-A",
            "plain": "A 'super-emitter' is a single place (like Ghazipur) that leaks an enormous, absurd amount of gas. 'IME' is the math formula used by NASA satellites to weigh the toxic cloud from space.",
            "analogy": "If 100 people are in a room and 1 person makes 90% of the noise, that person is a super-emitter. Global studies show less than 1% of waste sites create over 50% of all landfill methane. NASA flies overhead, measures the brightness of infrared light absorbed by the methane cloud, outlines its perimeter, and calculates its weight in kilograms.",
            "math": "Q = (IME / L) * U_eff\n• IME = Total mass of methane detected inside the cloud (kg)\n• L = Length of the cloud along the wind axis (meters)\n• U_eff = Effective wind speed pushing the cloud (m/s)\n• Q = Emission rate in kg/hr (Ghazipur reached 4,890.2 kg/hr).",
            "why": "Bottom-up government estimates (like WasteMAP) guess emissions based on waste weight and severely underestimate reality (by 1.4x to 6.3x). Satellite IME gives the true physical emission flux.",
            "viva": "Examiner: 'What is the IME method and why is it significant?'\nAnswer: 'Integrated Methane Enhancement integrates the total enhanced methane column mass retrieved by imaging spectrometers above background levels. Dividing by the plume length and multiplying by advective wind velocity yields an empirical mass flux rate (kg/hr), revealing that Ghazipur emits up to 4,890 kg/hr—vastly higher than static inventory assumptions.'"
        },
        {
            "num": "8",
            "phrase": "Nocturnal Planetary Boundary Layer Trapping & Thermal Inversion",
            "where": "Abstract, Section II-B, and Section IV-A",
            "plain": "Why air pollution is at its worst while you sleep (between 2:00 AM and 6:00 AM) rather than during daytime rush-hour traffic.",
            "analogy": "During a sunny day, the hot ground warms the air, and hot air rises like a hot air balloon, carrying toxic fumes high into the sky and blowing them away. At night, the ground cools down very fast. A cold blanket of air sits on the ground, trapped underneath a warm lid of air above it (thermal inversion). The 65-meter Ghazipur dump leaks poison gas into this tiny trapped space, and the gas spreads sideways into bedroom windows.",
            "math": "• Boundary Layer Height (PBLH): Shrinks from ~1,500 meters at 14:00 IST down to <300 meters at 04:00 IST.\n• Result: Mean NH3 spikes to 79.8 µg/m³ at 04:00 IST, then drops by 59.8% to 32.1 µg/m³ by 14:00 IST once solar heating restarts vertical convective mixing.",
            "why": "Most people assume vehicle traffic at 9 AM and 6 PM creates peak air toxicity. Our data proves the worst lethal exposure happens between 2 AM and 6 AM, when residents are asleep with closed doors.",
            "viva": "Examiner: 'Why does your paper claim the highest pollution occurs at night instead of peak daytime traffic?'\nAnswer: 'Surface radiational cooling under calm nocturnal winds compresses the planetary boundary layer to below 300 meters, forming a thermal inversion lid over the 65m dumpsite. Without solar convective mixing, continuous anaerobic landfill emissions are trapped in the lowest air layer, causing ammonia concentrations to peak at 79.8 µg/m³ between 02:00 and 06:00 IST.'"
        },
        {
            "num": "9",
            "phrase": "Collinear Ridge Regression vs. Gradient Boosted Trees",
            "where": "Section III-C & Section IV-B",
            "plain": "Why a simple, regularized math line (Ridge Regression) beat advanced fancy algorithms like XGBoost and LightGBM when predicting Ammonia and Benzene.",
            "analogy": "Imagine two students taking an exam with tricky, noisy questions. Student A (XGBoost) memorizes every tiny detail and tries to fit complicated curves through every random blip; on the new test, they get fooled by the noise. Student B (Ridge Regression) looks for the solid general trend and holds back from overreacting. Because chemical gases and weather move together (collinearity), the conservative student wins.",
            "math": "Loss_Ridge = ∑ (y - ŷ)^2 + α * ∑ (w_j)^2\n• The L2 penalty (α=1.0) shrinks weights and prevents volatile coefficients when features like temperature, humidity, and lag memory are highly correlated (collinear).\n• Scores: Benzene R² = 0.9002 (Ridge) vs 0.812 (XGBoost); NH3 R² = 0.8462 (Ridge) vs 0.795 (XGBoost). For non-linear PM2.5, LightGBM won with R² = 0.9293.",
            "why": "It shows examiners that we did not just blindly run 'deep learning' or 'XGBoost on everything'—we picked the mathematically appropriate model for each chemical gas.",
            "viva": "Examiner: 'Why did Ridge Regression outperform complex gradient boosted trees for Benzene and Ammonia?'\nAnswer: 'Volatile aromatic hydrocarbons and ammonia exhibit high multicollinearity with meteorological variables. Gradient boosting decision trees overfit to micro-turbulent eddies in the training sequence. L2-regularized Ridge regression penalizes large coefficient magnitudes, providing superior out-of-time generalization on collinear advective features.'"
        },
        {
            "num": "10",
            "phrase": "Persona-Adaptive Vulnerability Multipliers & Clean-Air Micro-Routing",
            "where": "Section IV-C & Web Dashboard (Health Alert)",
            "plain": "Instead of telling an entire city 'Air is Bad', the system gives personalized health warnings (e.g. an asthmatic child gets an emergency alarm earlier than a healthy athlete) and gives turn-by-turn map directions to walk away from the poison plume toward clean green parks.",
            "analogy": "If rain starts falling, a person in a raincoat is fine, but someone with a fresh paper document needs immediate shelter. Similarly, elderly citizens, pregnant mothers, and asthmatic children suffer severe damage at lower gas thresholds. The system multiplies risk based on who you are, and guides you toward upwind parks (like Sanjay Lake or Akshardham riverbanks) where exposure drops by up to 94%.",
            "math": "Clinical Risk Score = Concentration_Forecast * Persona_Multiplier * Exposure_Duration\n• Multiplier = 2.5x for Asthmatics/COPD; 2.0x for Elderly/Pediatrics; 1.0x for Healthy Adults.\n• Micro-routing computes the negative gradient vector of the plume cone, routing citizens into clean-air corridors.",
            "why": "Generic city-wide daily AQI averages (e.g. 'Delhi AQI = 350') are useless during a 45-minute toxic spike. Actionable clinical intelligence requires localized escape vectors.",
            "viva": "Examiner: 'How does your clinical routing engine reduce exposure by 88% to 94%?'\nAnswer: 'Landfill plumes follow a narrow Gaussian downwind dispersion corridor (110°–150° SE). By projecting active wind vectors in real time, our A* routing engine navigates pedestrians perpendicular to the plume axis into crosswind or upwind micro-environments—such as the Akshardham Yamuna green belt—cutting inhaled toxic dosage by up to 94%.'"
        },
        {
            "num": "11",
            "phrase": "Chronological Out-of-Time Train-Test Partition (No Data Leakage)",
            "where": "Section III-C & Table III",
            "plain": "Testing the AI strictly on the future (the last 2 months of the year) after training only on the past (the first 10 months), rather than mixing random days together.",
            "analogy": "If you are preparing for next Monday's stock market, you cannot use tomorrow's newspaper to study. If you shuffle a deck of time-series data randomly (k-fold random split), Monday is in the training set and Tuesday is in the test set. The AI 'cheats' because it already knows the future. A strict chronological cut proves the model works in the real world on tomorrow's unseen data.",
            "math": "• Total dataset: 70,176 records (15-min intervals over 2 years).\n• Training set: First 80% (56,140 rows, earlier chronological window).\n• Testing set: Final 20% (14,036 rows, strictly isolated future window). Zero random shuffling.",
            "why": "Standard random cross-validation produces artificially high, fraudulent R² scores in air quality papers due to auto-regressive leakage. Our chronological benchmark is 100% scientifically honest and leak-free.",
            "viva": "Examiner: 'How did you prevent data leakage during model validation?'\nAnswer: 'We strictly avoided random k-fold shuffling because 15-minute time series data contains strong autoregressive correlation. We enforced a chronological out-of-time 80/20 train/test split, ensuring the model was evaluated exclusively on future unseen time horizons without look-ahead bias.'"
        }
    ]

    # Render each topic into docx
    for t in topics:
        p_num = doc.add_paragraph()
        p_num.paragraph_format.space_before = Pt(14)
        p_num.paragraph_format.space_after = Pt(2)
        r_n = p_num.add_run(f"PHRASE #{t['num']}: {t['phrase']}")
        r_n.bold = True
        r_n.font.name = "Arial"
        r_n.font.size = Pt(13)
        r_n.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p_loc = doc.add_paragraph()
        p_loc.paragraph_format.space_before = Pt(0)
        p_loc.paragraph_format.space_after = Pt(6)
        r_l = p_loc.add_run(f"Found in: {t['where']}")
        r_l.italic = True
        r_l.font.name = "Calibri"
        r_l.font.size = Pt(9.5)
        r_l.font.color.rgb = RGBColor(0xE3, 0x4A, 0x32)

        content = [
            f"1. In Plain English (The 30-Second Summary):\n{t['plain']}",
            f"2. Real-World Analogy:\n{t['analogy']}",
            f"3. The Math & Physics Behind It:\n{t['math']}",
            f"4. Why We Needed It (What breaks without it?):\n{t['why']}",
            f"5. What to Say to an Examiner / Mentor (Viva Cheat-Sheet):\n{t['viva']}"
        ]
        create_callout_box(doc, f"Concept Breakdown & Defense Guide", content, border_color="E34A32", bg_color="F8FAFC")

    # Save docx
    doc.save(DOCX_OUT)
    print(f"[SUCCESS] Generated DOCX at: {DOCX_OUT}")

    # Build Markdown Version
    md_lines = [
        "# 📘 LandfillPlume-AI: The Plain-English Guide to Research Paper Phrases & Complex Concepts",
        "",
        "> **Purpose**: This document translates the formal academic terminology from *`RESEARCH_PAPER 3.docx`* into simple, conversational explanations with relatable real-world analogies, mathematical formulas, and exact viva answers for examiners and mentors.",
        "",
        "---",
        ""
    ]

    for t in topics:
        md_lines.extend([
            f"## 📌 Phrase #{t['num']}: {t['phrase']}",
            f"**Paper Section**: *{t['where']}*",
            "",
            f"### 💡 1. In Plain English (The 30-Second Summary)",
            f"{t['plain']}",
            "",
            f"### 🚗 2. Real-World Everyday Analogy",
            f"> {t['analogy']}",
            "",
            f"### 📐 3. The Math & Physics Behind It",
            "```text",
            f"{t['math']}",
            "```",
            "",
            f"### ⚠️ 4. Why We Needed It (What breaks without it?)",
            f"{t['why']}",
            "",
            f"### 🎓 5. What to Say to an Examiner or Mentor (Viva Defense)",
            "```markdown",
            f"{t['viva']}",
            "```",
            "",
            "---",
            ""
        ])

    with open(MD_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"[SUCCESS] Generated Markdown at: {MD_OUT}")

if __name__ == "__main__":
    build_documents()
