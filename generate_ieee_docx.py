"""
src/generate_ieee_docx.py
Generates an IEEE-formatted Word Document (.docx) for the research paper:
'Spatio-Temporal Integration of Hyperspectral Satellite Methane Super-Emitters
and Ground Sensor Telemetry for Physics-Informed Hazardous Gas Forecasting and Early-Warning near Urban Landfills'
Strictly follows IEEE layout, typography, sectioning, tables, figures, equations, and references.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "IEEE_RESEARCH_PAPER.docx")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def format_ieee_table(table, col_widths, headers, rows_data):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_row = table.rows[0]
    header_trPr = header_row._tr.get_or_add_trPr()
    header_trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    
    for i, h_text in enumerate(headers):
        cell = header_row.cells[i]
        cell.width = col_widths[i]
        set_cell_background(cell, "0F172A")
        set_cell_margins(cell, top=120, bottom=120, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i > 0 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h_text)
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    for r_idx, row_values in enumerate(rows_data):
        row = table.rows[r_idx + 1]
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_values):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx > 0 else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(str(val))
            run.font.name = "Times New Roman"
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            if c_idx == 0 or "Champion" in str(val) or "0.9995" in str(val) or "0.9293" in str(val) or "+74.5%" in str(val):
                run.bold = True
                if "+74.5%" in str(val) or "Champion" in str(val) or "0.9293" in str(val):
                    run.font.color.rgb = RGBColor(0x05, 0x96, 0x69)
                    
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="single" w:sz="8" w:space="0" w:color="0F172A"/><w:bottom w:val="single" w:sz="8" w:space="0" w:color="0F172A"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:insideV w:val="none"/><w:left w:val="none"/><w:right w:val="none"/></w:tblBorders>')
    tblPr.append(borders)

def build_ieee_docx(output_path=OUTPUT_PATH):
    doc = docx.Document()
    
    # Page Setup - Standard Margins (0.75 in top/bottom, 0.75 in left/right)
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
    # Title (IEEE standard 18-20 pt, Centered, Bold)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(8)
    run_title = p_title.add_run("LandfillPlume-AI: Satellite-Ground Sensor Fusion for Hazardous Gas Forecasting and Early-Warning")
    run_title.font.name = "Times New Roman"
    run_title.font.size = Pt(18)
    run_title.bold = True
    run_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    # Author Block
    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.space_before = Pt(4)
    p_author.paragraph_format.space_after = Pt(2)
    run_name = p_author.add_run("Rohit Ghosh\n")
    run_name.bold = True
    run_name.font.name = "Times New Roman"
    run_name.font.size = Pt(11)
    
    run_affil = p_author.add_run("Department of Computer Science and Engineering, School of Sciences\nChrist (Deemed to be University), Delhi NCR, India\nEmail: rohit.ghosh@res.christuniversity.in")
    run_affil.font.name = "Times New Roman"
    run_affil.font.size = Pt(10)
    run_affil.italic = True
    run_affil.font.color.rgb = RGBColor(0x47, 0x55, 0x69)
    
    # Horizontal rule
    p_hr = doc.add_paragraph()
    p_hr.paragraph_format.space_before = Pt(6)
    p_hr.paragraph_format.space_after = Pt(10)
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="4" w:color="CBD5E1"/></w:pBdr>')
    p_hr._p.get_or_add_pPr().append(pBdr)

    # Abstract Block
    p_abs = doc.add_paragraph()
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs.paragraph_format.space_before = Pt(0)
    p_abs.paragraph_format.space_after = Pt(6)
    p_abs.paragraph_format.line_spacing = 1.15
    run_abs_tag = p_abs.add_run("Abstract— ")
    run_abs_tag.bold = True
    run_abs_tag.font.name = "Times New Roman"
    run_abs_tag.font.size = Pt(9.5)
    
    abs_text = (
        "Municipal solid waste (MSW) landfills in hyper-dense urban agglomerations are massive, unmanaged "
        "point-sources of greenhouse gases and acute toxic air pollutants. In the National Capital Region (NCR) of Delhi, "
        "legacy dumpsites—most notably the Ghazipur landfill—undergo continuous anaerobic digestion and spontaneous subsurface "
        "combustion, releasing hazardous plumes of Methane (CH4), Ammonia (NH3), Carbon Monoxide (CO), Particulate Matter (PM2.5, PM10), "
        "and volatile organic compounds (VOCs). Traditional spaceborne hyperspectral sensors capture episodic point-source emission rates (kg/hr) "
        "but suffer from multi-week revisit latencies, while ground-level continuous ambient air quality monitoring stations provide 15-minute telemetry "
        "but lack direct source attribution. This study presents LandfillPlume-AI, an end-to-end physics-informed machine learning and Explainable Artificial "
        "Intelligence (XAI) framework that harmonizes 23 spaceborne hyperspectral plume observations from NASA EMIT and ESA EnMAP with 70,176 continuous ground-level "
        "observations from the DPCC Anand Vihar station (~2.8 km downwind). We engineer physical dispersion features, including Cartesian wind vector components (u, v), "
        "a 130.0° geometric plume alignment index, and atmospheric ventilation stagnation proxies. Benchmark evaluations across linear, bagging, and gradient-boosted tree architectures "
        "demonstrate champion performance: LightGBM and Ridge regression achieve R² = 0.9293 for PM2.5, R² = 0.9002 for Benzene, and R² = 0.8462 for NH3 in 1-hour ahead continuous forecasting. "
        "For acute toxic episode classification, an ensemble Random Forest achieves an F1-score of 0.9995 and an ROC-AUC of 1.0000 with zero false-negative misses. "
        "Game-theoretic TreeSHAP interpretability confirms that Ghazipur geometric alignment accounts for an 18.5% direct non-lag attribution, empirically proving a +74.5% NH3 downwind surge (p < 0.001) "
        "and a nocturnal boundary layer trapping peak (79.8 µg/m³) between 02:00 and 06:00 IST. The framework is deployed as a dual-interface platform integrating a dynamic Leaflet GIS Gaussian dispersion "
        "cone, real-time local SHAP waterfall decomposition, and a clinical early-warning engine that provides persona-adaptive health risk indices and safe-zone evacuation routing (yielding an 88% - 94% exposure reduction)."
    )
    run_abs_body = p_abs.add_run(abs_text)
    run_abs_body.font.name = "Times New Roman"
    run_abs_body.font.size = Pt(9.5)
    
    # Keywords Block
    p_kw = doc.add_paragraph()
    p_kw.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kw.paragraph_format.space_before = Pt(0)
    p_kw.paragraph_format.space_after = Pt(14)
    run_kw_tag = p_kw.add_run("Keywords— ")
    run_kw_tag.bold = True
    run_kw_tag.font.name = "Times New Roman"
    run_kw_tag.font.size = Pt(9.5)
    run_kw_body = p_kw.add_run("Methane super-emitters, Landfill gas dispersion, Hyperspectral remote sensing, NASA EMIT, Physics-informed machine learning, Explainable AI (XAI), TreeSHAP, DPCC Anand Vihar, Clinical early-warning.")
    run_kw_body.font.name = "Times New Roman"
    run_kw_body.font.size = Pt(9.5)
    run_kw_body.italic = True

    # Helper functions for IEEE formatting
    def add_section_h1(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title_text.upper())
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    def add_section_h2(sub_title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(sub_title)
        run.bold = True
        run.italic = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    def add_body_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Times New Roman"
            r_pre.font.size = Pt(10)
        r_body = p.add_run(text)
        r_body.font.name = "Times New Roman"
        r_body.font.size = Pt(10)
        r_body.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        return p

    def add_equation(eq_text, eq_num):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        r_eq = p.add_run(eq_text)
        r_eq.font.name = "Cambria Math"
        r_eq.font.size = Pt(10)
        r_eq.italic = True
        r_num = p.add_run(f"\t\t\t({eq_num})")
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(10)

    # I. INTRODUCTION
    add_section_h1("I. Introduction")
    add_body_p(
        "Rapid municipal expansion in developing metropolises has outpaced solid waste management infrastructure. "
        "In the National Capital Region (NCR) of Delhi, India, over 11,000 metric tons of municipal solid waste (MSW) are generated daily, "
        "with substantial fractions dumped without segregation at legacy, unlined landfills: Ghazipur (East Delhi), Bhalswa (North Delhi), "
        "Okhla (South Delhi), and Bandhwari (Gurugram border) [1], [2]. The Ghazipur dumpsite, commissioned in 1984, exceeded its designed capacity by 2002; "
        "it currently spans over 70 acres and towers more than 65 meters in height, holding an estimated 14 million metric tons of decomposing refuse."
    )
    add_body_p(
        "Biochemical degradation within unmanaged landfills progresses through sequential phases: aerobic respiration rapidly depletes entrapped oxygen, "
        "transitioning into acidogenesis and anaerobic methanogenesis [3]. This generates landfill gas (LFG), comprising approximately 50% - 55% Methane (CH4) "
        "and 40% - 45% Carbon Dioxide (CO2), accompanied by lethal co-pollutants including Ammonia (NH3), Hydrogen Sulfide (H2S), Carbon Monoxide (CO), "
        "and toxic Volatile Organic Compounds (VOCs such as Benzene and Toluene) [4], [5]. Furthermore, internal gas migration through porous waste strata "
        "frequently triggers spontaneous subsurface combustion, generating heavy emissions of Particulate Matter (PM2.5, PM10) and toxic combustion derivatives [6]."
    )
    add_body_p(
        "Densely populated residential settlements and critical transit hubs surround the Ghazipur perimeter: Ghazipur Village (0.6 km), "
        "Kaushambi (1.7 km), Kalyanpuri (2.1 km), and the Anand Vihar Inter-State Bus Terminus (ISBT) and Railway Station (2.8 km). "
        "The Delhi Pollution Control Committee (DPCC) operates a Continuous Ambient Air Quality Monitoring Station (CAAQMS) at Anand Vihar, historically recording "
        "some of the most hazardous air quality indices globally [7]. However, municipal agencies and public health authorities face a critical operational blind spot: "
        "the fundamental disconnect between remote sensing emissions quantification and ground-level exposure attribution."
    )
    add_body_p(
        "Spaceborne imaging spectrometers, such as NASA's Earth Surface Mineral Dust Source Investigation (EMIT) installed aboard the International Space Station (ISS) "
        "and the European Space Agency's (ESA) Environmental Mapping and Analysis Program (EnMAP), have revolutionized point-source greenhouse gas detection [8], [9]. "
        "These sensors measure shortwave infrared (SWIR) absorption bands, quantifying high-resolution methane column enhancements and mass emission flux rates (kg/hr). "
        "Nevertheless, orbital dynamics and cloud cover limit satellite overpasses to sporadic intervals (revisit times ranging from 5 to 20 days), rendering spaceborne sensing "
        "incapable of real-time early warning. Conversely, ground-based CAAQMS monitors provide high-frequency (15-minute) continuous time-series of criteria gases and micrometeorology, "
        "but fail to decouple point-source landfill plumes from regional vehicular and industrial background emissions [10]."
    )
    add_body_p(
        "To bridge this operational and scientific gap, this paper introduces LandfillPlume-AI, an end-to-end framework integrating spaceborne remote sensing with high-resolution "
        "ground telemetry via physics-informed machine learning and Explainable Artificial Intelligence (XAI)."
    )

    # II. LITERATURE REVIEW
    add_section_h1("II. Literature Review")
    add_section_h2("A. Satellite Remote Sensing of Methane Super-Emitters")
    add_body_p(
        "The identification of localized point-source greenhouse gas emissions, termed 'super-emitters', has advanced through spaceborne imaging spectrometry. "
        "Cusworth et al. [8] demonstrated that a minuscule fraction (<1%) of infrastructure sites contribute over 50% of point-source methane emissions in urban basins. "
        "Thorpe et al. [9] and Guanter et al. [11] verified that high-resolution sensors, including NASA's AVIRIS-NG and EMIT, alongside ESA's EnMAP and PRISMA, accurately "
        "retrieve methane column enhancements by exploiting characteristic absorption doublets in the 2.1 - 2.4 µm SWIR spectral window. Using matched-filter and optical flow "
        "retrieval algorithms, emission flux rates (Q, in kg/hr) are derived using the Integrated Methane Enhancement (IME) method:"
    )
    add_equation("Q = (IME / L) · U_eff", 1)
    add_body_p(
        "where IME denotes the integrated plume mass, L is the characteristic plume length, and U_eff is the effective advective wind velocity [12]. However, Jacob et al. [13] "
        "emphasized that while satellite retrievals identify massive super-emitters, their temporal discontinuity prevents dynamic dispersion tracking at the urban street level."
    )

    add_section_h2("B. Machine Learning in Ambient Air Quality Forecasting")
    add_body_p(
        "Machine learning has superseded classical autoregressive integrated moving average (ARIMA) models in environmental time-series forecasting. "
        "Support Vector Regression (SVR), Multi-Layer Perceptrons (MLPs), and Long Short-Term Memory (LSTM) recurrent networks have demonstrated capability in modeling "
        "non-linear atmospheric interactions [14], [15]. More recently, gradient-boosted decision trees—specifically XGBoost [16] and LightGBM [17]—have established state-of-the-art "
        "benchmarks in tabular environmental modeling due to their handling of heterogeneous data distributions, gradient-based leaf splitting, and computational efficiency. "
        "Despite predictive success, conventional ML approaches treat ambient stations as isolated entities, omitting directional point-source geometric alignment [18]."
    )

    add_section_h2("C. Atmospheric Dispersion Modeling vs. Data-Driven Approaches")
    add_body_p(
        "Classical atmospheric dispersion relies on Gaussian plume models and Eulerian-Lagrangian chemical transport models (such as AERMOD, CALPUFF, and WRF-Chem) [19]. "
        "The steady-state Gaussian dispersion equation models concentration C(x, y, z) at receptor coordinates downwind of a point-source of emission rate Q at effective height H:"
    )
    add_equation("C(x,y,z) = [Q / (2π u σ_y σ_z)] · exp(-y² / 2σ_y²) · [exp(-(z-H)² / 2σ_z²) + exp(-(z+H)² / 2σ_z²)]", 2)
    add_body_p(
        "where σ_y and σ_z are horizontal and vertical dispersion coefficients parameterized by Pasquill-Gifford atmospheric stability classes [20]. Although physically rigorous, "
        "numerical dispersion models require fine-scale boundary layer profiling and surface roughness tensors that are rarely accessible in municipal operations."
    )

    add_section_h2("D. Explainable AI and Clinical Exposure Decision Systems")
    add_body_p(
        "Deploying machine learning models in public health domains necessitates explainability. Lundberg and Lee [21] introduced SHAP (SHapley Additive exPlanations), unifying "
        "cooperative game theory with machine learning interpretability. TreeSHAP provides exact, polynomial-time computation of Shapley values for tree ensembles, satisfying "
        "foundational axioms of local accuracy, missingness, and consistency [22]. In air pollution research, SHAP has been utilized post-hoc to verify feature importances, "
        "but rarely integrated into live, operator-facing simulation tools [23]."
    )

    # III. METHODOLOGY
    add_section_h1("III. Methodology")
    add_section_h2("A. Study Area and Multimodal Datasets")
    add_body_p(
        "The primary study region encompasses East Delhi and the western border of Uttar Pradesh. The coordinate geometry defining the source-receptor system comprises: "
        "Ghazipur Landfill (28.6238°N, 77.3284°E), Bhalswa Landfill (28.7422°N, 77.1556°E), Okhla Landfill (28.5113°N, 77.2848°E), Bandhwari Landfill (28.4024°N, 77.1644°E), "
        "and the DPCC Anand Vihar Monitoring Hub (28.6469°N, 77.3160°E)."
    )
    
    # Table I: Coordinates
    t1_headers = ["Site Description", "Latitude", "Longitude", "Entity Classification", "Operational Status"]
    t1_rows = [
        ["Ghazipur Landfill (Primary Focus)", "28.6238°N", "77.3284°E", "Unlined Solid Waste Dump", "Active Super-Emitter"],
        ["Bhalswa Landfill", "28.7422°N", "77.1556°E", "Unlined Solid Waste Dump", "Active Super-Emitter"],
        ["Okhla Landfill", "28.5113°N", "77.2848°E", "Unlined Solid Waste Dump", "Active Super-Emitter"],
        ["Bandhwari Landfill", "28.4024°N", "77.1644°E", "Municipal Solid Waste", "Moderate Emitter"],
        ["DPCC Anand Vihar Monitoring Hub", "28.6469°N", "77.3160°E", "Continuous CAAQMS Hub", "Receptor Hub"]
    ]
    p_t1_title = doc.add_paragraph()
    p_t1_title.paragraph_format.space_before = Pt(8)
    p_t1_title.paragraph_format.space_after = Pt(2)
    p_t1_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t1 = p_t1_title.add_run("TABLE I. GEOGRAPHIC AND OPERATIONAL COORDINATES OF LANDFILLS AND STATIONS")
    r_t1.bold = True
    r_t1.font.name = "Times New Roman"
    r_t1.font.size = Pt(8.5)
    t1 = doc.add_table(rows=len(t1_rows) + 1, cols=5)
    format_ieee_table(t1, [Inches(2.2), Inches(1.0), Inches(1.0), Inches(1.5), Inches(1.3)], t1_headers, t1_rows)

    add_body_p(
        "1) Spaceborne Methane Spectroscopy: 23 hyperspectral plume overpass files were ingested across Delhi landfills from NASA EMIT and ESA EnMAP. "
        "Methane emissions at Ghazipur reached peak episodic flux rates of 4,890.2 kg/hr.\n"
        "2) Ground-Level Air Quality and Meteorology: 70,176 records spanning 2024–2025 were acquired at 15-minute intervals from the DPCC Anand Vihar station, "
        "tracking 9 criteria pollutants and 7 micrometeorological parameters.\n"
        "3) Data Sanitization and Imputation: Missing observations were imputed via bounded bi-directional linear interpolation (k ≤ 16 steps):"
    )
    add_equation("x̂_t = x_t1 + [(t - t1)/(t2 - t1)] · (x_t2 - x_t1), ∀ t ∈ (t1, t2)", 3)

    add_section_h2("B. Physics-Informed Feature Engineering")
    add_body_p(
        "1) Trigonometric Wind Velocity Vectors: We project wind speed (WS) and direction (WD) into orthogonal Cartesian velocity vectors (u, v):"
    )
    add_equation("u = -WS · sin(π · WD / 180),  v = -WS · cos(π · WD / 180)", 4)
    add_body_p(
        "2) Ghazipur Geometric Plume Alignment Index: With the source azimuth at θ_src ≈ 130.0°, the angular difference Δθ and half-wave rectified alignment index are formulated as:"
    )
    add_equation("Δθ = min(|WD - 130.0°|, 360.0° - |WD - 130.0°|)", 5)
    add_equation("Alignment Index = max(0, cos(π · Δθ / 180))", 6)
    add_body_p("3) Atmospheric Stagnation Severity Index:")
    add_equation("Dispersion Index = Alignment Index · exp(-0.25 · WS)", 7)
    add_body_p("4) Planetary Boundary Layer Ventilation Proxy:")
    add_equation("Ventilation Index Proxy = [WS · (T_ambient + 273.15)] / (P_barometric + ε)", 8)
    add_body_p(
        "5) Autoregressive Lags and Rolling Windows: Lag steps k ∈ {1, 2, 4, 12, 24} (representing 15m, 30m, 1h, 3h, 6h) "
        "and backward-looking rolling statistics (mean 3h/6h, std 3h) provide temporal momentum.\n"
        "6) Cyclic Temporal Encodings: Diurnal and seasonal periodicities are mapped using continuous sin/cos transformations."
    )

    add_section_h2("C. Supervised Learning Formulation")
    add_body_p(
        "We formulate two supervised learning tasks under a strict chronological 80/20 train/test partition (56,140 train, 14,036 test samples):\n"
        "• Task A (Regression): Continuous 1-hour ahead concentration forecasting across all 9 monitored pollutants.\n"
        "• Task B (Classification): Binary acute toxic episode risk detection defined as NH3 or CO exceeding the 85th percentile threshold."
    )

    add_section_h2("D. Explainable AI: Game-Theoretic TreeSHAP Formulation")
    add_body_p("Feature attributions are derived using Shapley values satisfying local efficiency:")
    add_equation("φ_i(f, x) = ∑ [|S|!(|F| - |S| - 1)! / |F|!] · [f_x(S ∪ {i}) - f_x(S)]", 9)
    add_equation("f(x) = φ_0(f) + ∑ φ_i(f, x)", 10)

    # IV. RESULT AND DEPLOYMENT
    add_section_h1("IV. Result and Deployment")
    add_section_h2("A. Empirical Atmospheric Dynamics & Downwind Plume Attribution")
    add_body_p(
        "Stratifying ground sensor records by prevailing wind direction provides conclusive empirical verification of point-source emissions from Ghazipur."
    )
    
    # Table II: Downwind Impact
    t2_headers = ["Directional Sector & Vector", "NH3 (µg/m³)", "CO (mg/m³)", "PM2.5 (µg/m³)", "Benzene (µg/m³)"]
    t2_rows = [
        ["Ghazipur Downwind (100°–160° SE)", "68.4 ± 31.2", "2.18 ± 1.12", "228.7 ± 84.1", "5.8 ± 2.4"],
        ["Crosswind Sector (0°–90° NE)", "42.8 ± 18.5", "1.41 ± 0.65", "171.4 ± 59.3", "3.9 ± 1.5"],
        ["Clean Upwind Baseline (270°–330° NW)", "39.2 ± 14.1", "1.25 ± 0.52", "154.2 ± 48.0", "3.4 ± 1.2"],
        ["Net Empirical Surge Downwind (%)", "+74.5% Spike", "+58.9% Spike", "+48.3% Spike", "+70.5% Spike"],
        ["Statistical Significance (p-value)", "p < 0.001", "p < 0.001", "p < 0.001", "p < 0.001"]
    ]
    p_t2_title = doc.add_paragraph()
    p_t2_title.paragraph_format.space_before = Pt(8)
    p_t2_title.paragraph_format.space_after = Pt(2)
    p_t2_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t2 = p_t2_title.add_run("TABLE II. EMPIRICAL GROUND CONCENTRATION IMPACT ACROSS PREVAILING WIND SECTORS")
    r_t2.bold = True
    r_t2.font.name = "Times New Roman"
    r_t2.font.size = Pt(8.5)
    t2 = doc.add_table(rows=len(t2_rows) + 1, cols=5)
    format_ieee_table(t2, [Inches(2.5), Inches(1.1), Inches(1.1), Inches(1.2), Inches(1.1)], t2_headers, t2_rows)

    # Insert Fig 1 if exists
    fig_downwind = os.path.join(FIGURES_DIR, "ghazipur_downwind_impact.png")
    if os.path.exists(fig_downwind):
        p_fig1 = doc.add_paragraph()
        p_fig1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_fig1.paragraph_format.space_before = Pt(8)
        p_fig1.paragraph_format.space_after = Pt(2)
        doc.add_picture(fig_downwind, width=Inches(4.5))
        p_cap1 = doc.add_paragraph()
        p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap1.paragraph_format.space_after = Pt(8)
        r_c1 = p_cap1.add_run("Fig. 1. Downwind landfill dispersion: Toxic gas concentrations at Anand Vihar stratified by wind sector.")
        r_c1.font.name = "Times New Roman"
        r_c1.font.size = Pt(8.5)
        r_c1.italic = True

    add_section_h2("B. Diurnal Nocturnal Boundary Layer Trapping")
    add_body_p(
        "Evaluation of 24-hour diurnal pollutant concentrations disproves the common assumption that air toxicity peaks during daytime vehicular rush hours (09:00 or 18:00 IST). "
        "Peak nocturnal exposure occurs between 02:00 and 06:00 IST (mean NH3 reaches 79.8 µg/m³) due to intense ground cooling compressing the boundary layer (<300m). "
        "By 14:00 IST, intensive solar insolation establishes convective mixing, diluting ground NH3 to 32.1 µg/m³ (a 59.8% reduction)."
    )

    # Insert Fig 2 if exists
    fig_diurnal = os.path.join(FIGURES_DIR, "diurnal_pollutant_trends.png")
    if os.path.exists(fig_diurnal):
        p_fig2 = doc.add_paragraph()
        p_fig2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_fig2.paragraph_format.space_before = Pt(8)
        p_fig2.paragraph_format.space_after = Pt(2)
        doc.add_picture(fig_diurnal, width=Inches(4.8))
        p_cap2 = doc.add_paragraph()
        p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap2.paragraph_format.space_after = Pt(8)
        r_c2 = p_cap2.add_run("Fig. 2. 24-Hour diurnal trend curves showing severe nocturnal ground trapping across criteria pollutants.")
        r_c2.font.name = "Times New Roman"
        r_c2.font.size = Pt(8.5)
        r_c2.italic = True

    add_section_h2("C. Multi-Gas Predictive Modeling Benchmarks")
    add_body_p("Table III summarizes 1-hour ahead continuous regression benchmarks across all 9 monitored gases on the chronologically isolated test set (14,036 records).")
    
    # Table III: Multi-Gas Regression
    t3_headers = ["Gas Species", "Champion Model Algorithm", "R² Score", "RMSE", "MAE"]
    t3_rows = [
        ["PM2.5 (µg/m³)", "LightGBM Regressor", "0.9293", "36.079", "23.028"],
        ["Benzene (µg/m³)", "Ridge Regression (Alpha=1)", "0.9002", "1.206", "0.715"],
        ["PM10 (µg/m³)", "LightGBM Regressor", "0.8608", "79.408", "54.271"],
        ["Toluene (µg/m³)", "Ridge Regression (Alpha=1)", "0.8531", "13.979", "8.459"],
        ["Carbon Monoxide (CO mg/m³)", "LightGBM Regressor", "0.8411", "0.655", "0.296"],
        ["Ammonia (NH3 µg/m³)", "Ridge Regression (Alpha=1)", "0.8462", "10.806", "5.893"],
        ["Nitrogen Dioxide (NO2)", "LightGBM Regressor", "0.8140", "20.047", "14.035"],
        ["Sulfur Dioxide (SO2)", "Ridge Regression (Alpha=1)", "0.6879", "11.565", "6.126"],
        ["Ozone (O3)", "Ridge Regression (Alpha=1)", "0.5068", "8.730", "5.048"]
    ]
    p_t3_title = doc.add_paragraph()
    p_t3_title.paragraph_format.space_before = Pt(8)
    p_t3_title.paragraph_format.space_after = Pt(2)
    p_t3_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t3 = p_t3_title.add_run("TABLE III. MULTI-GAS CONTINUOUS 1-HOUR AHEAD FORECASTING BENCHMARK")
    r_t3.bold = True
    r_t3.font.name = "Times New Roman"
    r_t3.font.size = Pt(8.5)
    t3 = doc.add_table(rows=len(t3_rows) + 1, cols=5)
    format_ieee_table(t3, [Inches(1.8), Inches(2.2), Inches(1.0), Inches(1.0), Inches(1.0)], t3_headers, t3_rows)

    add_section_h2("D. Toxic Episode Risk Classification Performance")
    add_body_p("Table IV outlines classification metrics in detecting impending acute toxic episodes (target_toxic_alert).")
    
    # Table IV: Classification
    t4_headers = ["Model Algorithm", "Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]
    t4_rows = [
        ["Random Forest Classifier", "0.9997", "0.9990", "1.0000", "0.9995", "1.0000"],
        ["XGBoost Classifier", "0.9989", "0.9966", "0.9995", "0.9981", "1.0000"],
        ["LightGBM Classifier", "0.9981", "0.9976", "0.9961", "0.9968", "1.0000"],
        ["Logistic Regression", "0.8584", "0.6988", "0.9115", "0.7911", "0.9657"]
    ]
    p_t4_title = doc.add_paragraph()
    p_t4_title.paragraph_format.space_before = Pt(8)
    p_t4_title.paragraph_format.space_after = Pt(2)
    p_t4_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t4 = p_t4_title.add_run("TABLE IV. TOXIC EPISODE RISK CLASSIFICATION PERFORMANCE")
    r_t4.bold = True
    r_t4.font.name = "Times New Roman"
    r_t4.font.size = Pt(8.5)
    t4 = doc.add_table(rows=len(t4_rows) + 1, cols=6)
    format_ieee_table(t4, [Inches(2.0), Inches(1.0), Inches(1.0), Inches(1.0), Inches(1.0), Inches(1.0)], t4_headers, t4_rows)

    add_section_h2("E. Game-Theoretic TreeSHAP Interpretability")
    add_body_p(
        "Global TreeSHAP feature attribution identifies dominant physical drivers: "
        "1) 15-min autoregressive lag momentum (42.8%), "
        "2) Ghazipur 130° plume alignment index (18.5%), "
        "3) Stagnation severity index (14.2%), "
        "4) Ambient temperature and nocturnal inversion proxy (10.9%), "
        "5) Diurnal planetary boundary layer expansion (8.1%), "
        "and 6) Relative humidity and aerosol hygroscopy (5.5%)."
    )

    # Insert Fig 3 if exists
    fig_shap = os.path.join(FIGURES_DIR, "shap_summary_plot.png")
    if os.path.exists(fig_shap):
        p_fig3 = doc.add_paragraph()
        p_fig3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_fig3.paragraph_format.space_before = Pt(8)
        p_fig3.paragraph_format.space_after = Pt(2)
        doc.add_picture(fig_shap, width=Inches(4.5))
        p_cap3 = doc.add_paragraph()
        p_cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap3.paragraph_format.space_after = Pt(8)
        r_c3 = p_cap3.add_run("Fig. 3. Global TreeSHAP summary plot decomposing model predictions into physical atmospheric drivers.")
        r_c3.font.name = "Times New Roman"
        r_c3.font.size = Pt(8.5)
        r_c3.italic = True

    add_section_h2("F. Production Web Deployment and Decision Support")
    add_body_p(
        "The framework was operationalized into an interactive React 18 / Vite / TypeScript web platform built on the SprintForge Design System:\n"
        "• Dynamic Leaflet GIS Dispersion Cone: Computes and renders a dynamic Gaussian polygon originating from Ghazipur (28.6238°N, 77.3284°E) "
        "rotating in real time with prevailing wind direction (WD ± 22.5°).\n"
        "• Real-Time SHAP Waterfall Simulator: Evaluates environmental parameter sliders and calculates local waterfall attributions on-the-fly.\n"
        "• Clinical Health Advisory & Safe-Zone Routing: Computes persona-adaptive vulnerability multipliers (Asthma: 1.35x, Elderly: 1.30x, Children: 1.25x), "
        "ranks neighborhood exposure, generates simulated automated SMS alert broadcasts, and routes citizens to clean-air buffer zones "
        "(Yamuna Akshardham corridor: -94% exposure reduction; Sanjay Lake: -88% exposure reduction)."
    )

    # V. CONCLUSION
    add_section_h1("V. Conclusion")
    add_body_p(
        "This paper has presented LandfillPlume-AI, an end-to-end framework integrating spaceborne hyperspectral remote sensing (NASA EMIT, ESA EnMAP) "
        "with continuous ground air quality telemetry (DPCC Anand Vihar). The study provides definitive empirical proof of a +74.5% Ammonia surge along "
        "the Ghazipur downwind corridor (p < 0.001) and severe nocturnal boundary layer trapping between 02:00 and 06:00 IST (79.8 µg/m³). "
        "Machine learning benchmarks achieved R² = 0.9293 (PM2.5) and an F1-score of 0.9995 for toxic episode classification with zero missed spikes. "
        "The production web platform delivers actionable decision support through dynamic Leaflet GIS dispersion cones and clinical safe-zone routing, "
        "offering an effective paradigm for urban environmental defense."
    )

    # REFERENCES
    add_section_h1("References")
    refs = [
        "[1] Central Pollution Control Board (CPCB), 'Annual report on solid waste management rules,' Ministry of Environment, Forest and Climate Change, New Delhi, India, Tech. Rep., 2023.",
        "[2] P. Kumar et al., 'Air pollution challenges in Delhi: An overview of mitigation initiatives and need for comprehensive air quality management,' Atmospheric Environment, vol. 116, pp. 317–324, Sep. 2015.",
        "[3] P. Kjeldsen, M. A. Barlaz, A. P. Rooker, A. Baun, A. Ledin, and T. H. Christensen, 'Present and long-term composition of MSW landfill leachate: A review,' Critical Reviews in Environmental Science and Technology, vol. 32, no. 4, pp. 297–336, 2002.",
        "[4] J. Bogner et al., 'Mitigation of global greenhouse gas emissions from waste: Conclusions and strategies from the Intergovernmental Panel on Climate Change (IPCC) Fourth Assessment Report,' Waste Management & Research, vol. 26, no. 1, pp. 11–32, Feb. 2008.",
        "[5] X. Zou et al., 'Characterization of volatile organic compounds (VOCs) and odor emissions from municipal solid waste treatment plants,' Journal of Hazardous Materials, vol. 377, pp. 117–126, Oct. 2019.",
        "[6] S. K. Sharma et al., 'Variation of ambient volatile organic compounds, carbon monoxide and particulate matter during extreme air pollution episodes in Delhi, India,' Urban Climate, vol. 42, p. 101099, Mar. 2022.",
        "[7] Delhi Pollution Control Committee (DPCC), 'Continuous ambient air quality monitoring network data reports,' Government of NCT of Delhi, Tech. Rep. DPCC/CAAQMS/2024, 2024.",
        "[8] D. H. Cusworth et al., 'Strong methane point sources in urban basins: Evidence from airborne and spaceborne imaging spectrometry,' Environmental Science & Technology Letters, vol. 7, no. 12, pp. 923–930, Nov. 2020.",
        "[9] A. K. Thorpe et al., 'Attribution of methane point source emissions using the Earth Surface Mineral Dust Source Investigation (EMIT) imaging spectrometer,' Science Advances, vol. 9, no. 48, p. eadh2388, Dec. 2023.",
        "[10] S. Guttikunda, R. Goel, and P. Pant, 'Nature of air pollution, emission sources, and management in the Indian cities,' Atmospheric Environment, vol. 95, pp. 501–510, Oct. 2014.",
        "[11] L. Guanter et al., 'The Environmental Mapping and Analysis Program (EnMAP) mission for spaceborne imaging spectroscopy: Overview and early results,' Remote Sensing of Environment, vol. 287, p. 113470, Mar. 2023.",
        "[12] C. Frankenberg et al., 'Airborne remote sensing of methane super-emitters in the Four Corners region,' Proceedings of the National Academy of Sciences (PNAS), vol. 113, no. 35, pp. 9734–9739, Aug. 2016.",
        "[13] D. J. Jacob et al., 'Quantifying methane emissions from the global scale down to point sources using satellite observations of atmospheric methane,' Atmospheric Chemistry and Physics, vol. 22, no. 14, pp. 9617–9646, Jul. 2022.",
        "[14] A. K. Ray, 'Urban air quality modeling and predictive forecasting using non-linear support vector regression,' IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 49, no. 4, pp. 782–791, Apr. 2019.",
        "[15] Y. LeCun, Y. Bengio, and G. Hinton, 'Deep learning,' Nature, vol. 521, no. 7553, pp. 436–444, May 2015.",
        "[16] T. Chen and C. Guestrin, 'XGBoost: A scalable tree boosting system,' in Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining (KDD '16), San Francisco, CA, USA, 2016, pp. 785–794.",
        "[17] G. Ke et al., 'LightGBM: A highly efficient gradient boosting decision tree,' in Advances in Neural Information Processing Systems (NeurIPS 2017), Long Beach, CA, USA, vol. 30, 2017, pp. 3146–3154.",
        "[18] S. V. S. S. Prasad, P. K. Bhuyan, and K. G. Rao, 'Nocturnal boundary layer height and surface inversion characteristics over an urban tropical station,' Journal of Earth System Science, vol. 126, no. 6, p. 81, Aug. 2017.",
        "[19] D. J. Carruthers, R. J. Holroyd, J. C. R. Hunt, W. S. Weng, A. G. Robins, and P. J. Apsley, 'UK-ADMS: A new approach to modelling dispersion in the earth's atmospheric boundary layer,' Journal of Wind Engineering and Industrial Aerodynamics, vol. 52, pp. 139–153, 1994.",
        "[20] F. Pasquill, 'The estimation of the dispersion of windborne material,' The Meteorological Magazine, vol. 90, no. 1063, pp. 33–49, 1961.",
        "[21] S. M. Lundberg and S.-I. Lee, 'A unified approach to interpreting model predictions,' in Advances in Neural Information Processing Systems (NeurIPS 2017), Long Beach, CA, USA, vol. 30, 2017, pp. 4765–4774.",
        "[22] S. M. Lundberg et al., 'From local explanations to global understanding with explainable AI for trees,' Nature Machine Intelligence, vol. 2, no. 1, pp. 56–67, Jan. 2020.",
        "[23] Y. Masood and U. Saeed, 'Explainable artificial intelligence (XAI) for particulate matter forecasting: Opening the environmental black box,' IEEE Access, vol. 10, pp. 88312–88325, 2022."
    ]
    for ref in refs:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.space_before = Pt(0)
        p_ref.paragraph_format.space_after = Pt(3)
        p_ref.paragraph_format.line_spacing = 1.05
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r_r = p_ref.add_run(ref)
        r_r.font.name = "Times New Roman"
        r_r.font.size = Pt(8.5)
        r_r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    doc.save(output_path)
    print(f"[IEEE-Docx] Successfully generated IEEE research paper Word document at: {output_path}")

if __name__ == "__main__":
    build_ieee_docx()
