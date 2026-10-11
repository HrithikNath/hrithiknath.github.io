#!/usr/bin/env python3
"""
Static site generator for hrithiknath's academic website.

Usage:   python build.py
Output:  index.html  (next to this file)

Edit the CONTENT section below, run the script, then commit index.html.
GitHub Pages serves the generated file.

Mini-markup available inside any text string:
    **bold**      *italic*      [link text](https://url)      "\n" -> <br>
"""
import re
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def _link(m):
    text, url = m.group(1), m.group(2)
    ext = ' target="_blank" rel="noopener noreferrer"' if url.startswith("http") else ""
    return f'<a href="{url}"{ext}>{text}</a>'


def md(text):
    """Tiny markdown subset -> safe HTML."""
    s = escape(text, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    return s.replace("\n", "<br>")


def a(label, url):
    """Anchor for data-driven links (label/url are plain text)."""
    ext = ' target="_blank" rel="noopener noreferrer"' if url.startswith("http") else ""
    return f'<a href="{escape(url)}"{ext}>{escape(label)}</a>'


def p(text):
    return f"<p>{md(text)}</p>"


def h3(text):
    return f"<h3>{md(text)}</h3>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ps(lines):
    return "".join(p(x) for x in lines)


def prose(inner):
    return f'<div class="prose">{inner}</div>'


def bracket_links(links):
    """[Label] - [Label]  (bold brackets, used for certificates etc.)"""
    return " - ".join(
        f"<strong>[</strong>{a(l, u)}<strong>]</strong>" for l, u in links
    )


def pub_item(item):
    """One publication/paper/poster entry -> <li> contents."""
    out = md(item["text"])
    doi, links = item.get("doi"), item.get("links", [])
    if doi:
        out += f"<br><em>DOI: {escape(doi)}</em>"
    if links:
        out += (" || " if doi else " ") + " - ".join(f"[{a(l, u)}]" for l, u in links)
    return out


# --------------------------------------------------------------------------
# CONTENT
# --------------------------------------------------------------------------

SITE = {
    "name": "Hrithik Nath",
    "title": "Hrithik Nath | Civil & Environmental Engineering",
    "description": (
        "Hrithik Nath — Graduate Research Assistant at the University of Missouri. "
        "Research, publications, education, teaching, and achievements in civil "
        "and environmental engineering."
    ),
    "theme_color": "#234d38",
    "eyebrow": "Graduate Research Assistant · University of Missouri",
    "tagline": "Exploring environmental systems through research on microplastics, "
               "water resources, and environmental health.",
    "caption": "Research · Water · Environment",
    "sidebar_bottom": ["Civil & Environmental Engineering", "University of Missouri",
                       "Columbia, Missouri, USA"],
    "scholar": "https://scholar.google.com/citations?user=HK8PINkAAAAJ&hl=en",
    "researchgate": "https://www.researchgate.net/profile/Hrithik-Nath",
    "email": "hrithiknath@missouri.edu",
}

CEE_URL = "https://engineering.missouri.edu/departments/cee/"
ARROW = "**↗**"


def bio():
    return prose(ps([
        "**Welcome!** I’m Hrithik Nath, a graduate student in the Department of Civil and Environmental Engineering at the University of Missouri (MU), pursuing my Master of Science in Civil Engineering with a research focus on microplastic pollution in environmental systems.",
        "I previously served as a Lecturer and Program Coordinator in the Department of Civil Engineering at the University of Creative Technology Chittagong (UCTC) and hold a BSc in Civil Engineering from Khulna University of Engineering & Technology (KUET). This website shares my academic journey, research interests, and professional milestones. Feel free to explore, collaborate, or reach out!",
        "**My Journey!** My academic path began at KUET, where I developed a strong foundation in civil and environmental engineering. After graduation, I worked at the Bangladesh Institute of Social Research (BISR) Trust as a Research Associate, contributing to projects intersecting public health and environmental concerns.",
        "In 2021, I joined UCTC as a Lecturer, and later took on the role of Program Coordinator for the Civil Engineering Department. My responsibilities included course instruction, departmental coordination, and mentoring undergraduate students on innovative research projects aimed at solving local environmental challenges.",
        "Having now transitioned to graduate studies in the U.S., I bring with me a deep-rooted commitment to interdisciplinary research and sustainable development.",
        "**Research Interests!** My current research focuses on microplastic contamination in riverine and aquatic environments, with an emphasis on quantification techniques and organic matter removal methods. This work is central to my MS thesis at the University of Missouri and aims to improve detection and analysis of microplastics to inform mitigation strategies.",
        "Previously, I worked with a range of environmental research topics including hydrology and meteorology—with a particular focus on rainfall variability and climate resilience—as well as groundwater quality assessment and ecological risk analysis using geochemical methods. I also explored aspects of urban environmental health, examining how air pollution affects respiratory functions, especially among vulnerable populations exposed to traffic-related emissions.",
        "**Let's Connect!** This website serves as a space to share my academic journey, research contributions, and professional milestones. Feel free to explore and reach out for any questions, collaboration opportunities, or simply to connect.",
    ]))


def education():
    courses = [
        "Fall'25 - CV_ENG 8225 - Aquatic Chemistry - Dr Maryam Salehi Esfandarani",
        "Fall'25 - CV_ENG 8250 - Biochemical Treatment Process - Dr Zhiqiang Hu",
        "Spring'26 - CV_ENG 7211 - Air Pollution Control Systems - Dr Maryam Salehi Esfandarani",
        "Spring'26 - CV_ENG 8240 - Physicochemical Treatment Processes - Dr Maria Fidalgo",
        "Summer'26 - STAT 7710 - Introduction to Mathematical Statistics - Dr Philip Deming",
    ]
    return prose(
        h3("MS in Civil Engineering (August 2025 - May 2027)")
        + ps([
            f"Department of Civil and Environmental Engineering [{ARROW}]({CEE_URL})",
            "W1024, Thomas and Nell Lafferre Hall",
            "College of Engineering - University of Missouri (MU)",
            "Columbia, Missouri (MO) 65211, United States of America (USA)",
            "Grade: GPA 4.00 out of 4.00",
        ])
        + h3("List of Courses:")
        + ul(md(c) for c in courses)
        + h3("BSc in Civil Engineering (March 2015 - December 2020)")
        + ps([
            "Department of Civil Engineering",
            "Khulna University of Engineering & Technology (KUET), Khulna, Bangladesh",
            "Grade: CGPA 3.57 out of 4.00",
            "Key Courses: Environmental Engineering, Geotechnical Engineering, Hydrology",
        ])
        + h3("Higher Secondary Education (HSC): Class XI-XII (2013-2015)")
        + ps([
            "Class of 2015",
            "Chattogram College, Chattogram, Bangladesh",
            "Group: Science",
            "Grade: GPA 5.00 out of 5.00 (With Golden A+)",
        ])
        + h3("Secondary Education (SSC): Class VI-X (2008-2013)")
        + ps([
            "Class of 2013",
            "Feni Government Pilot High School, Feni, Bangladesh",
            "Group: Science",
            "Grade: GPA 5.00 out of 5.00 (With Golden A+)",
        ])
    )


# (batch, group, title, students)
THESES = [
    ("9th", "01", "Comprehensive Assessment of Carcinogenic and Non-carcinogenic Health Risk in an Urban Dumpsite due to Heavy Metal Exposure.", "Abu Salem Md Abdullah, Md.Saiful Islam, Rashedul Islam Swapnil"),
    ("9th", "02", "Comprehensive Assessment of Environmental Pollution and Ecological Risk in an Urban Dumpsite due to Heavy Metal Pollution.", "Sajeeb Hasan, Mohammad Zonaid, Rupan Das"),
    ("8th", "01", "Spatial Trends and Co-officiant of Rainfall Variability in North-Western zone of Bangladesh (1994-2023).", "Bishwajit Chatterjee, Md Sultan Mahmud, Md Abdulla Al Bakir"),
    ("8th", "02", "Assessment of Air Pollutions and Non-Carcinogenic Health Risks from PM2.5 Exposure in Major cities of Bangladesh (2015-2022).", "Md. Yeasir Arafat, Jasim Uddin Rana, Mohammad Ridon"),
    ("8th", "03", "ARIMA-Based Forecasting of Annual and Seasonal Rainfall in the Southeastern Districts of Bangladesh.", "Liton Acherjee, Titu Shil, Mohammad Raihan Uddin"),
    ("8th", "04", "Health Risk Assessment of Heavy Metals in Soil Near an Unregulated Dumpsite: A Case Study from Khulna, Bangladesh.", "Mohashin Ahammad Chowdhury, Shaiful Islam, Md Shahin Alom, Ismail Bin Aziz Alvi"),
    ("8th", "05", "Assessment of Heavy Metal Contamination in/around an Open Landfill Soils in Khulna, Bangladesh.", "Kawsar Chanam Munna, Kazi Aynoon Nishad, Supti Kana Deve, Md Chotan"),
    ("7th", "01", "Noise-Induced Annoyance in Chattogram Schools: A Case Study on Opening and Closing Hours.", "Sakia Amin, Jalal Uddin Papon"),
    ("7th", "02", "Assessing Temporal and Spatial Trends of Rainfall in Northern Bangladesh (1993–2022): A Mann-Kendall Approach.", "Debashis Chowdhury, Md Hobaib"),
    ("7th", "03", "Spatiotemporal Analysis of Humidity Trends in Southeastern Bangladesh (1993–2022): A Mann-Kendall Approach.", "Riaz Uddin Masum, M Saifullah Kutubi"),
    ("6th", "01", "Health Risk Assessment of Heavy Metals in Soil Near an Unregulated Dumpsite: A Case Study from Feni, Bangladesh.", "MD. Arif Hossen, MD. Sazzad Hossain, Raju Devnath, MD. Khales Ahmed Roxy"),
    ("6th", "02", "Assessment of Heavy Metal Contamination and Ecological Risk in Soils of a Legacy Municipal Dumpsite in Feni, Bangladesh.", "N.K.M. Munna Talukder, Md. Rashedul Islam, Md. Jubayer , Md Mosharrof Hossain, Md. Abu Faysal"),
    ("6th", "03", "Spatiotemporal Analysis of Rainfall Trends in Northwestern Bangladesh Using the Mann-Kendall Approach.", "Tapan Rudra, Shohel Rana, Ranel Chakma, Md. Shipon Rana"),
    ("6th", "04", "Characterization and Quality Assessment of Construction Stone Chips for Sustainable Infrastructure Development.", "Rahul Acharjee, Sujan Kumar Ghosh, Parvin Akter, Mohammad Naimul Hossain, Apu Chakraborty, Md Sharif Hossain"),
    ("6th", "05", "Historical Change in Land Use Land Cover due to Rapid Refugee Settlement in Kutupalong, Cox’s Bazar.", "Md. Hasan Tarek, Didarul Alam"),
    ("5th", "01", "Assessment of Index-Based Traffic Noise Annoyance Level at Major Road Intersections in a Tourist City: A Case Study towards Environmental Sustainability.", "Md Iqbal Hossain, Rukon Uddin, Abdulla Al Mamun, Md Mohaiminul Islam, Md Saiful Islam"),
    ("5th", "02", "Temporal and Spatial Variability of Rainfall in Southeast Bangladesh: A 42-Year Analysis.", "Md. Tarequr Rahman, Md. Abdul Mannan, Md. Jaber Hosen, Anikman Barua"),
    ("4th", "01", "Safety Awareness and Risk Factors regarding Accidental Campfire among Refugees of Rohingya Camp: A Knowledge, Attitude, and Practice (KAP) Survey.", "Bishwajit Karmaker, Hasmoth Ullah, MD. Younus"),
    ("4th", "02", "Magnitude and Impact Analysis of Traffic Noise Pollution at Port City Chattogram, Bangladesh.", "MD. Monsur Ali, MD. Nazim Uddin, Mohammed Ahsanul Islam Fahim, Nazimul Islam, Abdullah Al Parvez"),
    ("4th", "03", "Investigating the Impacts of Ambient Air Pollution on The Pulmonary Health of Rickshaw Pullers in a Developing City.", "Tasjid Ahsan Chowdhury, Mohammed Ibrahim Sakib, Rubel Das, Sabuj Nath"),
]

UCTC_ADDRESS = [
    "Department of Civil Engineering",
    "School of Science and Engineering",
    "University of Creative Technology Chittagong (UCTC)",
    "Bahaddarhat, 4212, Chattogram, Bangladesh",
]


def experience():
    thesis_items = [
        f"{b} Batch - Group {g}: {escape(t, quote=False)} <em>({escape(s, quote=False)})</em>"
        for b, g, t, s in THESES
    ]
    return prose(
        h3("Graduate Research Assistant (August 2025 - Present)")
        + ps([
            "SWERL - Salehi Water and Environmental Research Lab [{a}](https://mshfp.mufaculty.umsystem.edu/home/about)".format(a=ARROW),
            "Supervisor: Dr Maryam Salehi Esfandarani",
            "Graduate Office: E1503 in Thomas and Nell Lafferre Hall",
            f"Department of Civil and Environmental Engineering [{ARROW}]({CEE_URL})",
            "College of Engineering - University of Missouri (MU)",
            "Columbia, MO 65211, United States of America (USA)",
            "**Lecturer (July 2021 - Present)** | Study Leave",
        ])
        + ps(UCTC_ADDRESS)
        + ps([
            "During my tenure as a Lecturer in the Department of Civil Engineering at the University of Creative Technology Chittagong (UCTC), I was engaged in both teaching and academic supervision, contributing to the academic development of undergraduate students. I taught several core and advanced courses in the domains of Hydrology, Environmental Engineering, Numerical Methods, Geotechnical Engineering, and Irrigation & Flood Control. In each of these courses, I aimed to connect theoretical knowledge with practical applications by using real-world examples, problem-solving exercises, and hands-on discussions.",
            "I also supervised undergraduate research projects, providing students with step-by-step guidance in topic development, data acquisition, analysis, and report writing. Many of these projects aligned with my own research interests in hydrology, environmental assessment, and geotechnical analysis. I emphasized analytical thinking and scientific rigor, helping students to develop both their technical skills and academic writing capabilities.",
            "Apart from my teaching responsibilities, I participated in various departmental activities such as curriculum enhancement, exam moderation, and academic event coordination. I supported initiatives aimed at increasing student engagement in research, technical competitions, and professional development workshops. I also contributed to fostering a learning environment that encouraged curiosity, collaboration, and continuous growth.",
            "My role at UCTC allowed me to develop and refine my academic and professional skills. It strengthened my passion for teaching and mentoring while reinforcing my commitment to contributing meaningfully to civil and environmental engineering education.",
        ])
        + h3("Key Courses as Instructor:")
        + ul(md(f"{c} (Autumn 2021 - Spring 2025)") for c in [
            "Environmental Engineering II", "Hydrology", "Geotechnical Engineering I",
            "Numerical Methods", "Geotechnical Engineering Sessional I",
        ])
        + h3("Undergraduate Thesis Mentorship Experience:")
        + ul(thesis_items)
        + h3("Program Coordinator (March 2022 - June 2025)")
        + ps(UCTC_ADDRESS)
        + ps([
            "In addition to my teaching and supervisory responsibilities, I served as a Program Coordinator in the Department of Civil Engineering at the University of Creative Technology Chittagong (UCTC). This role involved a combination of academic planning, quality assurance, and administrative oversight to ensure the smooth functioning of the undergraduate program.",
            "One of my core responsibilities was preparing semester-wise teaching plans and detailed class schedules in coordination with fellow faculty members. I worked closely with academic staff to allocate courses effectively, considering both faculty expertise and student needs. Ensuring the logical flow of course offerings and balancing academic loads were essential components of this task.",
            "I also played an active role in monitoring the quality of class delivery throughout the semester. This included following up on lesson plans, coordinating substitute arrangements when needed, and collecting feedback to identify areas for pedagogical improvement. My efforts were directed toward maintaining consistency in instructional standards and enhancing the overall academic experience for students.",
            "Beyond academic coordination, I handled a range of departmental administrative duties. These included organizing meetings, maintaining academic records, facilitating communication between students and the department, and assisting with internal evaluations and accreditation-related documentation. My work as Program Coordinator helped streamline processes and foster a more organized and responsive academic environment within the department.",
        ])
        + h3("Junior Engineer (December 2020 - July 2021)")
        + ps([
            "Division of Water & Environment",
            "Bangladesh Institute of Social Research (BISR) Consultants Limited",
            "Lalmatia, 1207, Dhaka, Bangladesh",
            "Shortly after completing my undergraduate studies in Civil Engineering, I began my professional journey as a Junior Design Engineer in the Water and Environmental Division of the Bangladesh Institute of Social Research (BISR). This role provided me with valuable practical experience and laid the foundation for my future academic and research interests in water resources and environmental management.",
            "During my time at BISR, I was involved in preparing detailed appraisal reports for flood control and management in various sub-project areas. These reports required a thorough understanding of local hydrological conditions, flood patterns, and infrastructure planning. I collaborated with senior engineers and field experts to evaluate site-specific challenges and recommend suitable interventions for effective flood mitigation.",
            "Another key aspect of my role was conducting engineering feasibility studies for ongoing sub-projects. These studies included technical assessments, cost estimations, and environmental considerations necessary for successful implementation. The work demanded both analytical precision and the ability to synthesize field data into actionable recommendations.",
            "Additionally, I was responsible for planning canal excavation routes in designated rural areas to ensure efficient irrigation. This involved surveying land features, understanding existing agricultural practices, and designing routes that would maximize water distribution while minimizing environmental disruption. Through this work, I gained hands-on experience in integrating engineering solutions with community needs in the context of sustainable water management.",
            "This position offered me a strong introduction to field-based civil engineering projects and helped me develop a practical outlook toward hydrological and environmental challenges in Bangladesh’s rural landscape.",
        ])
        + h3("Project:")
        + ul([md("Small-Scale Water Resource Development Project (SSWRDP)\nClient: Local Govt. Engineering Department (LGED)")])
    )


# --- Publications ---------------------------------------------------------
# Each entry: text (mini-markup), optional doi, optional links [(label, url)]

DRIVE = "https://drive.google.com/"

JOURNALS = [
    dict(text="**Nath, H.**, Zolfaghari, S., Maurer-Jones, M.A., Darbha, G.K., Salehi, M., 2026. Organic Matter Removal in Microplastic Extraction from Environmental Samples: Challenges and Methodological Solutions. Journal of Hazardous Materials. (Elsevier)",
         doi="10.1016/j.jhazmat.2026.142998",
         links=[("Link to Journal", "https://doi.org/10.1016/j.jhazmat.2026.142998"),
                ("Read", "https://drive.google.com/file/d/1uUb3H51BlP4hQ5k03u39T4jZ1IaWliI6/view?usp=drive_link")]),
    dict(text="**Nath, H.**, Adhikary, S.K., Roy, S., Akhter, S., Bithi, U.H., Salam, M.A., Islam, A.R.M.T., Siddique, M.A.B., 2025. Utilizing PMF and Monte Carlo-based models to evaluate toxic metals enrichment pathways, sources, and public health risks in an unplanned urbanized dumpsite soil. Environmental Science: Advances. (RSC: Royal Society of Chemistry)",
         doi="10.1039/D5VA00141B",
         links=[("Link to Journal", "https://pubs.rsc.org/en/Content/ArticleLanding/2025/VA/D5VA00141B"),
                ("Read", "https://drive.google.com/file/d/1b0h-TKuMmUIFJ4ewlicbWmOwuWhmHRXa/view?usp=drive_link")]),
    dict(text="Altuwaijri, H. A., Al Kafy, A., Rahaman, Z. A., Miah, M. T., Raiyan, R., **Nath, H.**, Jodder, P. K., 2025. Predicting spatiotemporal dynamics of land use influenced thermal patterns using remote sensing-based machine learning algorithms. Rangeland Ecology and Management. (Elsevier)",
         doi="10.1016/j.rama.2025.06.017",
         links=[("Link", "https://www.sciencedirect.com/science/article/pii/S1550742425000867?via%3Dihub"),
                ("Download", "https://drive.google.com/uc?export=download&id=1OzouifBAf22WK5o5NYuFqiaVNzIYTYw7")]),
    dict(text="Altuwaijri, H.A., Kafy, A.A., Rahaman, Z.A., Fariha, J.N., Miah, M.T., Mishu, R.A., **Nath, H**., Sonet, M.S., 2025. Biophysical parameters and land surface temperature dynamics in arid urban environments: A comprehensive machine learning approach. Environmental Earth Sciences. (Springer)",
         doi="10.1007/s12665-025-12427-6",
         links=[("Link", "https://link.springer.com/article/10.1007/s12665-025-12427-6"),
                ("Download", "https://drive.google.com/uc?export=download&id=1Mjf2FHJhURoHSAwm137ypK3izvaigPrS")]),
    dict(text="Masum, M.M.H., Islam, M.B., Hossen, M.A., **Nath, H.**, Hoque, M.A., 2025. Navigating pollution: The impact of transportation modes on air and noise quality in Chattogram City, Bangladesh. Journal of Transport & Health. (Elsevier)",
         doi="10.1016/j.jth.2025.102112",
         links=[("Link", "https://www.sciencedirect.com/science/article/pii/S221414052500132X"),
                ("Download", "https://drive.google.com/uc?export=download&id=1ZxZFFPMtZrOKj0nMmO4_jUr9DAKpNC9U")]),
    dict(text="Partha, D. B., Yasmin, S., **Nath, H.**, 2025. Preterm Births Attributable to Criteria Air Pollutant Exposure in Bangladesh During 2015-2019. Environmental Pollution. (Elsevier)",
         doi="10.1016/j.envpol.2025.125742",
         links=[("Link", "https://www.sciencedirect.com/science/article/abs/pii/S0269749125001150?via%3Dihub"),
                ("Download", "https://drive.google.com/uc?export=download&id=15HOW_ciVtjPfQssj-u4_YQCQU3_jqqno")]),
    dict(text="**Nath, H.**, Adhikary, S.K., Alsulamy, S., Kafy, A.A., Rahaman, Z.A., Roy, S., Hossain, M.I., and Mamun, A.A., 2024. Assessment of Index-Based Traffic Noise Annoyance Level at Major Road Intersections in a Tourist City: A Case Study towards Environmental Sustainability. Heliyon. (Cell/Elsevier)",
         doi="10.1016/j.heliyon.2024.e40005",
         links=[("Link", "https://kwnsfk27.r.eu-west-1.awstrack.me/L0/https:%2F%2Fauthors.elsevier.com%2Fsd%2Farticle%2FS2405-8440%2824%2916036-7/1/01020192e8ea4873-0b44ce14-6da7-456c-8677-96751db4fa6c-000000/F8OPTXFy2o7h33prjBUJwjvrYb8=398"),
                ("Download", "https://drive.google.com/uc?export=download&id=1aV6HrQcK5VxePujiwNgwBEXJscMhZAKS")]),
    dict(text="Hossain, M.Z., Adhikary, S.K., **Nath, H.**, Kafy, A.A., Altuwaijri, H.A., Rahman, M.T., 2024. Integrated geospatial and analytical hierarchy process approach for assessing sustainable management of groundwater recharge potential in Barind Tract. Water. (MDPI)",
         doi="10.3390/w16202918",
         links=[("Link", "https://www.mdpi.com/2073-4441/16/20/2918"),
                ("Download", "https://drive.google.com/uc?export=download&id=1loC2BXwvf48mFT5XjpxB1oeEf0Wjnfci")]),
    dict(text="Saha, M., Kafy, A.A., Bakshi, A., **Nath, H.**, Alsulamy, S., Rahaman, Z.A., Saroar, M., 2024. The Urban-Air Quality Nexus: Assessing the Interplay of Land Cover Change and Air Pollution in Emerging South Asian Cities. Environmental Pollution. (Elsevier)",
         doi="10.1016/j.envpol.2024.124877",
         links=[("Link", "https://www.sciencedirect.com/science/article/pii/S0269749124015914?ref=pdf_download&fr=RR-2&rr=8c081f013bd03378"),
                ("Download", "https://drive.google.com/uc?export=download&id=18_CPjtkMP9BON7-1O3lQbPjizgEKhwSo")]),
    dict(text="Ashwini, K., Sil, B.S., Kafy, A.A., Altuwaijri, H.A., **Nath, H.**, Rahaman, Z.A., 2024. Harnessing machine learning algorithms to model the association between land use/land cover change and heatwave dynamics for enhanced environmental management. Land. (MDPI)",
         doi="10.3390/land13081273",
         links=[("Link", "https://www.mdpi.com/2073-445X/13/8/1273"),
                ("Download", "https://drive.google.com/uc?export=download&id=15HOW_ciVtjPfQssj-u4_YQCQU3_jqqno")]),
    dict(text="Salim, M.Z., Choudhari, N., Kafy, A.A., **Nath, H.**, Alsulamy, S., Rahaman, Z.A., Aldosary, A.S., Rahman, M.T., Al-Ramadan, B., 2024. A comprehensive review of navigating urbanization-induced climate change complexities for sustainable groundwater resources management in the Indian subcontinent. Groundwater for Sustainable Development. ([Elsevier](https://www.sciencedirect.com/journal/groundwater-for-sustainable-development))",
         doi="10.1016/j.gsd.2024.101115",
         links=[("Link", "https://doi.org/10.1016/j.gsd.2024.101115"),
                ("Download", "https://drive.google.com/uc?export=download&id=1q3QUBq9Y3h5veUUd5zFlnSZBtaiUth5J")]),
    dict(text="**Nath, H.**, Adhikary, S.K., Nath, S., Kafy, A.A., Islam, A.R.M.T., Alsulamy, S., Khedher, K.M. and Shohan, A.A.A., 2024. Long-Term Trends and Spatial Variability in Rainfall in the Southeast Region of Bangladesh: Implication for Sustainable Water Resources Management. Theoretical and Applied Climatology. ([Springer](https://link.springer.com/journal/704))",
         doi="10.1007/s00704-024-04843-8",
         links=[("Link", "https://doi.org/10.1007/s00704-024-04843-8"),
                ("Download", "https://drive.google.com/uc?export=download&id=196KIN8FOwasOJlsg_o2EF70kzR-Z7hLx")]),
    dict(text="Bahiru, T.K., Aldosary, A.S., Kafy, A.A., Rahman, M.T., **Nath, H.**, Kalaivani, S., Sarker, D., Alsulamy, S., Khedher, K.M., Shohan, A.A.A. and Ferdous, M.N., 2023. Geospatial approach in modeling linear, areal, and relief morphometric interactions in Dabus River basin ecology for sustainable water resource management. Groundwater for Sustainable Development. ([Elsevier](https://www.sciencedirect.com/journal/groundwater-for-sustainable-development))",
         doi="10.1016/j.gsd.2023.101067",
         links=[("Link", "https://doi.org/10.1016/j.gsd.2023.101067"),
                ("Download", "https://drive.google.com/u/0/uc?id=1gfimpyI8kclATbIIuDjvy0lwXlcjeGre&export=download")]),
    dict(text="**Nath, H.**, Kabir, M.H., Kafy, A.A., Rahaman, Z.A. and Rahman, M.T., 2023. Geotechnical properties and applicability of bentonite-modified local soil as landfill and environmental sustainability liners. Environmental and Sustainability Indicators. ([Elsevier](https://www.sciencedirect.com/journal/environmental-and-sustainability-indicators))",
         doi="10.1016/j.indic.2023.100241",
         links=[("Link", "https://doi.org/10.1016/j.indic.2023.100241"),
                ("Download", "https://drive.google.com/uc?export=download&id=1jGS46ADsDgJ8inMHYuJmlmThqQoiWwEb")]),
]

POSTERS = [
    dict(text="**Nath, H.**, Gopakumar, A. N., Azimi, P., Keshavarz, Z., Johnson, M., Nadeau, K., Allen, J. G., and Salehi, M., 2026. Studying Microplastics Abundance in Samples Collected from Homes Following a Southern California Wildfire. 1st Annual LA Fires Research Conference. January 14, 2026, University of California, Los Angeles, CA, USA."),
    dict(text="**Nath, H.**, Salehi, M., Zolfaghari, S., and Salehi, M., 2025. Organic Matter Removal Strategies for Accurate Microplastic Extraction from Soil Samples: Challenges and Methodological Solutions. American Chemical Society (ACS) Midwest Regional Meeting (MWRM), October 12–14, 2025, University of Missouri, Columbia, MO, USA."),
    dict(text="**Nath, H.**, Salehi, M., Zolfaghari, S., and Salehi, M., 2025. Organic Matter Removal for Microplastic Extraction from Soil Samples: Methods and Challenges. Mid-America Environmental Engineering Conference (MAEEC). October 11, 2025, Washington University, St. Louis, MO, USA."),
]

_RG_SG = "?_sg%5B0%5D=qMiE-Y4-K5c7KtCxIpGbVweYrYIjr5fj6W0l7k6CChR8aFaXeAhEFMIrEaVmUWcmv-qdGQfMUlhl3uoqIsV8hVeMBIYmS6enU5RKKgxK.4nSsIrrikOzXjiZ0GXK4__r_NoDdF8hWK55eEEyoZCr2TuXMH7LG41csIJj6VKAZfUF1iGf-JSubDH6iATKKRA&_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InByb2ZpbGUiLCJwcmV2aW91c1BhZ2UiOiJwcm9maWxlIiwicG9zaXRpb24iOiJwYWdlQ29udGVudCJ9fQ"
_RG = "https://www.researchgate.net/publication/"

CONFERENCES = [
    dict(text="Ratul, M.J.P., Adhikary, S.K., Akter, U., Dip, M.M.F., and **Nath, H.**, 2025. Performance Evaluation of ANN and LSTM Combined with Orangutan Algorithm for Enhanced Prediction of Streamflow. 2025 International Conference on Water, Energy and Environment (ICWEE), Australia.",
         doi="10.1007/978-3-032-18708-6_12",
         links=[("Proceedings Link", "https://doi.org/10.1007/978-3-032-18708-6_12")]),
    dict(text="Akter, U., Adhikary, S.K., Ratul, M.J.P., Dip, M.M.F., and **Nath, H.**, 2025. Enhanced Prediction of Reference Evapotranspiration Using an Innovative Metaheuristic Optimization Approach. 2025 International Conference on Water, Energy and Environment (ICWEE), Australia.",
         doi="10.1007/978-3-032-18708-6_50",
         links=[("Proceedings Link", "https://doi.org/10.1007/978-3-032-18708-6_50")]),
    dict(text="Ratul, N.J.P., Akter, U., Ghosh, S., Dip, M.M.F., **Nath, H.** and Adhikary, S.K., 2025. A Particle Swarm Optimization-Based Deep Learning Framework for Enhanced Prediction of River Water Level. 2025 International Conference on Quantum Photonics, Artificial Intelligence, and Networking (QPAIN), Rangpur, Bangladesh.",
         doi="10.1063/5.0247297",
         links=[("Proceedings Link", "https://ieeexplore.ieee.org/document/11172048"),
                ("Read", "https://drive.google.com/file/d/1e9rOZDDSWRI8AS04sOSCTdd1l38C0nLd/view?usp=drive_link")]),
    dict(text="**Nath, H.**, Roy, S., Hassan, Z. and Adhikary, S.K., 2024. Evaluation of Heavy Metal associated Risks in Soils of an Unplanned Dumpsite: A Public Health Concern. 7th International Conference on Advances in Civil Engineering (ICACE 2024), CUET, Chattogram, Bangladesh.",
         links=[("Proceedings Link", "https://link.springer.com/chapter/10.1007/978-981-95-1630-8_2"),
                ("Read", "https://drive.google.com/drive/u/0/folders/1BraI6BdX6WLFwBP-MnNvZoySbFRmfUCd")]),
    dict(text="**Nath, H.**, Amin, S., Uddin, J. and Adhikary, S.K., 2024. Noise-Induced Annoyance in Chattogram Schools: A Case Study on Opening and Closing Hours. 7th International Conference on Advances in Civil Engineering (ICACE 2024), CUET, Chattogram, Bangladesh.",
         links=[("ResearchGate Link", _RG + "387055796_Noise-Induced_Annoyance_During_School_Opening_and_Closing_Hours_in_Chattogram_City_Bangladesh"),
                ("Download", "https://drive.google.com/uc?export=download&id=1Dx3M7E8W56NGD6-RrbGFAUsUYdYTrorz")]),
    dict(text="Mondol, S.C., Adhikary, S.K., **Nath, H.**, and Pal, S.S., 2024. A Deep Learning Approach Using Long Short-Term Memory Networks for Enhanced Prediction of Rainfall in the Northeastern Region of Bangladesh. 7th International Conference on Civil Engineering for Sustainable Development (ICCESD 2024), KUET, Khulna, Bangladesh.",
         doi="10.1063/5.0247626",
         links=[("Link", "https://doi.org/10.1063/5.0247626"),
                ("Download", "https://drive.google.com/file/d/11qvEx3iSit694-uqxqdbVd_9ru5Ee3yl/view?usp=drive_link")]),
    dict(text="Hassan, M.Z., Das, P.P., Debnath, K.M.P., Jahan, I., and **Nath, H.**, 2024. Assessing Urban Waterlogging and Drainage Efficiency: A Case Study of Shahjalal Upashahar, Sylhet. 7th International Conference on Civil Engineering for Sustainable Development (ICCESD 2024), KUET, Khulna, Bangladesh.",
         links=[("Link", _RG + "379247946_ASSESSING_URBAN_WATERLOGGING_AND_DRAINAGE_EFFICIENCY_-A_CASE_STUDY_OF_SHAHJALAL_UPASHAHAR_SYLHET" + _RG_SG),
                ("Download", "https://drive.google.com/file/d/1DeTrllP-PrDSnAiPXmuDbCp8Q1lKDF27/view?usp=drive_link")]),
    dict(text="Kibria, G., Adhikary, S.K., and **Nath, H.**, 2024. Simulation of Water Logging Scenarios Using SWMM – A Case Study on Khulna City in Bangladesh. 7th International Conference on Civil Engineering for Sustainable Development (ICCESD 2024), KUET, Khulna, Bangladesh.",
         links=[("Link", _RG + "379280661_Simulation_of_Water_Logging_Scenarios_using_SWMM_A_Case_Study_on_Khulna_City_in_Bangladesh" + _RG_SG),
                ("Download", "https://drive.google.com/file/d/1hHunwHujIcdX72jKDDX7JIPNNSqHlK0D/view?usp=drive_link")]),
    dict(text="Sultana, L., Adhikary, S.K. and **Nath, H.**, 2024. Spatial Assessment of Agricultural Water Footprint of Dhaka Division in Bangladesh. 7th International Conference on Civil Engineering for Sustainable Development (ICCESD 2024), KUET, Khulna, Bangladesh.",
         doi="10.1063/5.0247297",
         links=[("Link", "https://doi.org/10.1063/5.0247297"),
                ("Download", "https://drive.google.com/uc?export=download&id=1Xdg7habPzemaFhAnvry-ArWE0Gf-rZbg")]),
    dict(text="Rana, M., Adhikary, S.K. and **Nath, H.**, 2023. Assessment of annual and seasonal climate change impact in Rajshahi district of Bangladesh using SDSM. 4th International Conference on Planning, Architecture and Civil Engineering (ICPACE 2023), RUET, Rajshahi, Bangladesh.",
         links=[("Link", _RG + "374696458_Assessment_of_Annual_and_Seasonal_Climate_Change_Impact_in_Rajshahi_District_of_Bangladesh_using_SDSM"),
                ("Download", "https://drive.google.com/uc?export=download&id=1bGhGKTfnBRVXAp_1iRnYgdTeR6757d0n")]),
    dict(text="**Nath, H.** and Rafizul, I. M., 2021. Spatial Variability of Metal Elements in Soils of a Waste Disposal Site in Khulna: A Geostatistical Study. 5th International Conference on Advances in Civil Engineering (ICACE-2020), CUET, Chattogram, Bangladesh.",
         doi="10.1007/978-981-16-5547-0_3",
         links=[("Proceedings Link", "https://doi.org/10.1007/978-981-16-5547-0_3"),
                ("Download", "https://drive.google.com/uc?export=download&id=1tak-oUcHQNxsuDRysKoIapATe0qr9MvE")]),
]

PEER_REVIEW = [
    "**Elsevier**: Sustainable Cities and Society *(3 Reviews)*, Advances in Space Research *(1 Review)*, Atmospheric Environment: X *(1 Review)*",
    "**Springer**: Theoretical and Applied Climatology *(1 Review)*, Earth Systems and Environment *(2 Review)*",
    "**Taylor & Francis**: Papers in Applied Geography *(1 Review)*",
]

# (name, role line)
MENTORS = [
    ("Dr Maryam Salehi", "Associate Professor, *Civil and Environmental Engineering, University of Missouri-Columbia*"),
    ("Dr Sajal Kumar Adhikary", "Professor, *Civil Engineering, Khulna University of Engineering & Technology (KUET)*"),
    ("Abdulla Al Kafy", "PhD Student, *Geography and Environment, University of Texas at Austin*"),
    ("Dr Md. Rafizul Islam", "Professor, *Civil Engineering, Khulna University of Engineering & Technology (KUET)*"),
    ("Dr Abu Reza Md Towfiqul Islam", "Associate Professor, *Disaster Science and Management, Environmental Science, Begum Rokeya University Rangpur (BRUR)*"),
]

COLLABORATORS = [
    "Maryam Salehi, PhD", "Sajal Kumar Adhikary, PhD", "Abdulla Al Kafy, PhD",
    "Md. Rafizul Islam, PhD", "Abu Reza Md Towfiqul Islam, PhD", "Debatosh Banik Partha, PhD",
]


def research():
    top = (
        "<p><strong>[</strong>" + f"<strong>{a('Google Scholar', SITE['scholar'])}</strong>"
        + "<strong>]</strong> <strong>[</strong>"
        + f"<strong>{a('ResearchGate', SITE['researchgate'])}</strong><strong>]</strong></p>"
    )
    drive_archive = a("Drive Archive", "https://drive.google.com/drive/folders/1GvxUkHeV-SbQG7OJuN_Pn2IC_A19J6gW?usp=drive_link")
    return prose(
        top
        + f"<h3>Peer-Reviewed Journal Articles <em>(</em><em>{drive_archive}</em><em>)</em></h3>"
        + ul(pub_item(j) for j in JOURNALS)
        + h3("Poster Presentations")
        + ul(pub_item(x) for x in POSTERS)
        + h3("Conference Papers")
        + ul(pub_item(x) for x in CONFERENCES)
        + h3("Peer-Review Activities")
        + ul(md(x) for x in PEER_REVIEW)
        + h3("*Sustainable Cities and Societies, Elsevier*")
        + h3("*Advances in Space Research, Elsevier*")
        + h3("Research Mentors")
        + "".join(h3(f"**{n}**") + p(r) for n, r in MENTORS)
        + h3("Collaborators and Co-authors")
        + ps(COLLABORATORS)
    )


# --- Achievements ---------------------------------------------------------
# (heading, [paragraphs], [(link label, url)])
ACHIEVEMENTS = [
    ("2026 | Paul F Kufrin Memorial Scholarship | $5,000", [
        "I was honored to receive the Paul F. Kufrin Memorial Scholarship, a competitive $5,000 graduate scholarship administered through the Missouri Water Center and the Department of Civil and Environmental Engineering at the University of Missouri. The scholarship was established by the Kufrin family and well-wishers in memory of Paul F. Kufrin, who was a graduate student in Civil and Environmental Engineering at Mizzou during 1977–78.",
        "The award recognizes graduate students specializing in environmental engineering who demonstrate strong academic achievement and a commitment to applied environmental engineering and real-world problem solving. At the time of receiving this scholarship, I was pursuing my M.S. in Civil Engineering at the University of Missouri while conducting research on microplastic contamination in post-wildfire environments as a Graduate Research Assistant in the Salehi Water and Environment Research Laboratory (SWERL). This recognition is particularly meaningful to me because it supports my efforts to address emerging environmental and public health challenges through applied research while continuing the legacy of a fellow Mizzou environmental engineering scholar.",
    ], []),
    ("2024 | Fetured in National News Paper - The Daily Star", [
        'One of my most significant research publications delved into the variability of rainfall trends in southeast Bangladesh. This groundbreaking study garnered attention and was prominently featured in the esteemed national newspaper "The Daily Star" on March 07, 2023, Thursday. The newspaper highlighted our findings in a special issue titled "Campus," further amplifying the impact and recognition of our research within the academic and broader community.',
    ], [("Newspaper Cutout", "https://drive.google.com/file/d/1wLVmkVFEOPFb_CYLuHPBqL1GvzbG4BV4/view?usp=drive_link"),
        ("E-Article", "https://www.thedailystar.net/campus/education/news/uctc-lecturer-hrithik-nath-publishes-groundbreaking-research-rainfall-trends-southeast-bangladesh-3561051")]),
    ("2021 | Best Conference Paper | ICACE 2020", [
        'I was the recipient of "Best Paper Award" for the Technical Paper Titled "Spatial Variability of Metal Elements in Soils of a Waste Disposal Site in Khulna: A Geostatistical Study" in the "Environmental Engineering Section" of the "5th International Conference on Advances in Civil Engineering (ICACE-2020)" held at Chittagong University of Engineering & Technology (CUET).',
    ], [("View Certificate", "https://drive.google.com/file/d/1J2sTi7f7OkPJiqsxslT0gwycHO_jYZzk/view?usp=sharing")]),
    ("2021 | Dean's Award | Faculty of Civil Engineering, KUET", [
        'I was the recipient of "Dean\'s List Award" for an outstanding academic record during the 2018-2019 academic session by the "Faculty of Civil Engineering" of Khulna University of Engineering & Technology (KUET).',
    ], [("View Certificate", "https://drive.google.com/file/d/10SquqEmEXfNB1R8UP5w5CiS_-qwBzgg9/view?usp=drivesdk")]),
    ("2015-2016 | Merit Order Scholarship | Department of Civil Engineering, KUET", [
        'I was the Recipient of "Merit Order Scholarship" throughout my undergraduate years (2016-2020) for maintaining merit positions inside the top 25 students by the "Department of Civil Engineering" of Khulna University of Engineering & Technology (KUET).',
    ], []),
    ("2013 | Merit Scholarship - General | Bangladesh Government", [
        'I was the recipient of "General Scholarship" for securing a merit position in the Secondary School Certificate (S.S.C.) examination in 2013 by the "Government of Bangladesh".',
    ], []),
    ("2013 | Regional First Runner-Up | Bangladesh Mathematical Olympiad", [
        'I was the recipient of "Regional First Runner-Up Award" in "Secondary" Category for securing the first position in the Regional Mathematical Olympiad in 2013 by the "Bangladesh Math Olympiad Committee."',
    ], [("View Certificate", "https://drive.google.com/file/d/1qD_sw9wQ4iOu1veoBzAkY3E_6H4ohrrf/view?usp=share_link")]),
    ("2012 | Regional First Runner-Up | Bangladesh Mathematical Olympiad", [
        'I was the Recipient of the "Regional First Runner-Up Award" in the "Secondary" Category for securing the first position in the Regional Mathematical Olympiad in 2012 by the "Bangladesh Math Olympiad Committee."',
    ], [("View Certificate", "https://drive.google.com/file/d/1qAPJIg-TBHrvd7C-A6GfXQdsbH_6G_Kg/view?usp=sharing")]),
    ("2010 | Merit Scholarship - Talent Pool | Bangladesh Government", [
        'I was the recipient of the "Talent-Pool Scholarship" for securing a position in the Junior School Certificate (S.S.C.) examination in 2010 by the "Government of Bangladesh."',
    ], []),
    ("2007 | Merit Scholarship - Talent Pool | Bangladesh Government", [
        'I was the recipient of the "Talent-Pool Scholarship" for securing a position in the Primary School Certificate (P.S.C.) examination in 2007 by the "Government of Bangladesh."',
    ], []),
    ("2011 | Regional First Runner-Up | Bangladesh Mathematical Olympiad", [
        'I was the Recipient of "Regional First Runner-Up" in "Junior" Category for securing the first position in the Regional Mathematical Olympiad in 2011 by the "Bangladesh Math Olympiad Committee."',
    ], [("View Certificate", "https://drive.google.com/file/d/1qEalRTKrb67WfliSFpJZH1KzlVhqvf9b/view?usp=sharing")]),
    ("2008 | Regional Champion | Bangladesh Mathematical Olympiad", [
        'I was the recipient of the "Regional Champion Award" in the "Primary" Category for securing the first position in the Regional Mathematical Olympiad in 2008 by the "Bangladesh Math Olympiad Committee."',
    ], [("View Certificate", "https://drive.google.com/file/d/1q99iqgQoLuFxbmKkibSZPkXnY-5rVQgI/view?usp=sharing")]),
]


def achievements():
    out = ""
    for heading, paras, links in ACHIEVEMENTS:
        out += h3(heading) + ps(paras)
        if links:
            out += f"<p>{bracket_links(links)}</p>"
    return prose(out)


# --- Contact --------------------------------------------------------------
EMAILS = ["hrithiknath@missouri.edu", "hrithiknath51@gmail.com", "hrithiknath.ce@gmail.com"]
SOCIAL = [
    ("LinkedIn ↗", "https://www.linkedin.com/in/hrithiknath/"),
    ("ResearchGate ↗", "https://www.researchgate.net/profile/Hrithik-Nath"),
    ("Facebook ↗", "https://www.facebook.com/hrithiknathjoy/"),
    ("Instagram ↗", "https://www.instagram.com/hrithiknathjoy/"),
]


def contact():
    emails = "<br>".join(a(e, f"mailto:{e}") for e in EMAILS)
    buttons = "".join(f'<a class="button" href="{u}" target="_blank" rel="noopener noreferrer">{escape(l)}</a>' for l, u in SOCIAL)
    return (
        '<div class="contact"><p>I welcome research conversations and collaboration opportunities.</p>'
        f'<p>{emails}</p><div class="buttons">{buttons}</div></div>'
    )


# Section order: (id, nav label, heading, body builder)
SECTIONS = [
    ("bio", "About", "About me", bio),
    ("education", "Education", "Education", education),
    ("experience", "Experience", "Experience & teaching", experience),
    ("research", "Research", "Research & publications", research),
    ("achievements", "Achievements", "Achievements & recognition", achievements),
    ("contact", "Contact", "Let’s connect", contact),
]

# --------------------------------------------------------------------------
# PAGE TEMPLATE
# --------------------------------------------------------------------------

def render():
    css = (ROOT / "src" / "style.css").read_text(encoding="utf-8").replace("\n", "")
    js = (ROOT / "src" / "script.js").read_text(encoding="utf-8")
    name = escape(SITE["name"])

    nav = "".join(f'<a href="#{i}">{escape(n)}</a>' for i, n, _, _ in SECTIONS)
    sidebar_bottom = "<br>".join(escape(x) for x in SITE["sidebar_bottom"])
    sections = ""
    for n, (sid, _, title, body) in enumerate(SECTIONS, start=1):
        sections += (
            f'<section id="{sid}" aria-labelledby="{sid}-title"><div class="section-title">'
            f'<span>{n:02d}</span><h2 id="{sid}-title">{escape(title)}</h2></div>{body()}</section>\n'
        )

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(SITE['title'])}</title><meta name="description" content="{escape(SITE['description'])}"><meta name="theme-color" content="{SITE['theme_color']}"><style>{css}</style></head><body><a class="skip" href="#main">Skip to content</a><aside><a class="brand" href="#home">{name}<span aria-hidden="true">.</span></a><button class="menu" aria-expanded="false" aria-controls="navigation">Menu</button><p class="caption">{escape(SITE['caption'])}</p><nav id="navigation" aria-label="Main navigation">{nav}</nav><div class="sidebar-bottom">{sidebar_bottom}</div></aside><main id="main"><header id="home" class="hero"><div><span class="eyebrow">{escape(SITE['eyebrow'])}</span><h1>{name}</h1><p class="intro">{escape(SITE['tagline'])}</p><div class="buttons"><a class="button primary" href="#research">Explore my research</a><a class="button" href="{escape(SITE['scholar'])}" target="_blank" rel="noopener noreferrer">Google Scholar ↗</a><a class="button" href="mailto:{SITE['email']}">Get in touch</a></div></div><div class="portrait" role="img" aria-label="{name} monogram" style="display:grid;place-items:center;font:64px Georgia,serif;color:#234d38">HN</div></header>
{sections}<footer>© <span id="year">{date.today().year}</span> {name}. All rights reserved. <a href="#home">Back to top ↑</a></footer></main><script>
{js}</script></body></html>
"""


if __name__ == "__main__":
    out = ROOT / "index.html"
    out.write_text(render(), encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size:,} bytes)")
