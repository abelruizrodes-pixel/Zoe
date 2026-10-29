import re

def clean_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    orig = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {path}")
    else:
        print(f"No changes in: {path}")

# 1. cv_es.html
es_replacements = [
    ("et en <strong>organización de viajes de negocios y turismo</strong>", "y en <strong>organización de viajes de negocios y turismo</strong>"),
    (" (Industrie- und Handelskammer)", ""),
    ("(Industrie- und Handelskammer)", ""),
    ("Industrie- und Handelskammer", "IHK"),
    ("Cámara de Comercio e Industria (IHK)", "Cámara de Comercio e Industria (IHK)"),
]
clean_file("cv_es.html", es_replacements)

# 2. cv_en.html
en_replacements = [
    ("with dual certified expertise Industrie- und Handelskammer en <strong>insurance advice/claims management</strong> et en <strong>business travel & tourism organisation</strong>",
     "with dual certified expertise in <strong>insurance advice/claims management</strong> and in <strong>business travel & tourism organisation</strong>"),
    ("conformity with the framework Industrie- und Handelskammer", "conformity with official regulatory and professional standards"),
    ("in accordance with the framework Industrie- und Handelskammer", "in accordance with official regulatory and professional standards"),
    ("State Vocational Training Industrie- und Handelskammer (Privat- und Geschäftsreisen) • Trèves", "State-Certified Vocational Training (IHK) • Trier"),
    (" (Industrie- und Handelskammer)", ""),
    ("(Industrie- und Handelskammer)", ""),
    ("Industrie- und Handelskammer", "Chamber of Commerce and Industry (IHK)"),
]
clean_file("cv_en.html", en_replacements)

# 3. cv.html
fr_replacements = [
    ("Zurich Gruppe Deutschland & Industrie- und Handelskammer • Trèves", "Zurich Gruppe Deutschland & Chambre de Commerce (IHK) • Trèves"),
    (" (Industrie- und Handelskammer)", ""),
    ("(Industrie- und Handelskammer)", ""),
    ("Industrie- und Handelskammer", "Chambre de Commerce (IHK)"),
]
clean_file("cv.html", fr_replacements)

# 4. cv_de.html
de_replacements = [
    ("en <strong>Versicherungsberatung/Schadensmanagement</strong> et en <strong>Organisation von Geschäftsreisen & Tourismus</strong>",
     "in <strong>Versicherungsberatung/Schadensmanagement</strong> und in <strong>Organisation von Geschäftsreisen & Tourismus</strong>"),
    ("Geprüfte Fachfrau für Versicherungsvermittlung (IHK)", "Geprüfte Versicherungsvermittlerin (IHK)"),
    (" (Fachfrau Industrie- und Handelskammer)", ""),
    (" (Industrie- und Handelskammer)", ""),
    ("(Industrie- und Handelskammer)", ""),
]
clean_file("cv_de.html", de_replacements)

# 5. cv_pt.html
pt_replacements = [
    ("com dupla especialização certificada Industrie- und Handelskammer en <strong>aconselhamento em seguros/gestão de sinistros</strong> et en <strong>organização de viagens de negócios e turismo</strong>",
     "com dupla especialização profissional certificada em <strong>aconselhamento em seguros/gestão de sinistros</strong> e em <strong>organização de viagens de negócios e turismo</strong>"),
    ("em conformidade com o quadro Industrie- und Handelskammer", "em conformidade com as normas regulamentares e padrões profissionais"),
    (" (Industrie- und Handelskammer)", ""),
    ("(Industrie- und Handelskammer)", ""),
    ("Industrie- und Handelskammer", "Câmara de Comércio e Indústria (IHK)"),
]
clean_file("cv_pt.html", pt_replacements)

# 6. cv_lb.html
lb_replacements = [
    ("nom Kader Industrie- und Handelskammer", "nom offiziellen a reglementaresche Kader"),
    ("Staatlech Staatlech Beruffsausbildung (IHK) (Privat- und Geschäftsreisen) • Trèves", "Staatlech Beruffsausbildung (IHK) • Tréier"),
    (" (Industrie- und Handelskammer)", ""),
    ("(Industrie- und Handelskammer)", ""),
    ("Industrie- und Handelskammer", "Handelskammer (IHK)"),
]
clean_file("cv_lb.html", lb_replacements)

# 7. i18n-de-fr.js
de_fr_replacements = [
    ('"hero.tagline": "Ich verbinde Kunden, Kulturen und Lösungen – mit zwei Abschlüssen der Industrie- und Handelskammer',
     '"hero.tagline": "Ich verbinde Kunden, Kulturen und Lösungen – mit zwei IHK-Abschlüssen'),
    ('"stats.ihk": "Abschlüsse der Industrie- und Handelskammer"', '"stats.ihk": "IHK-Abschlüsse"'),
    ('"about.p1": "Ich bin <strong>Kundenberaterin mit Abschluss der Industrie- und Handelskammer</strong>',
     '"about.p1": "Ich bin <strong>geprüfte Kundenberaterin (IHK)</strong>'),
    ('"skills.c2": "Versicherung (Industrie- und Handelskammer)"', '"skills.c2": "Versicherung (IHK)"'),
    ('"exp2.role": "Fachfrau für Versicherungsvermittlung (Industrie- und Handelskammer)"',
     '"exp2.role": "Versicherungsvermittlerin & Schadensmanagerin (IHK)"'),
    ('"edu1": "Fachfrau für Versicherungsvermittlung (Industrie- und Handelskammer) · Zurich Gruppe"',
     '"edu1": "Geprüfte Versicherungsvermittlerin (IHK) · Zurich Gruppe"'),
    # French side:
    ('"hero.tagline": "Je relie clients, cultures et solutions – avec deux diplômes de la Industrie- und Handelskammer',
     '"hero.tagline": "Je relie clients, cultures et solutions – avec deux certifications reconnues'),
    ('"stats.ihk": "Diplômes de la Industrie- und Handelskammer"', '"stats.ihk": "Diplômes d\'État certifiés"'),
    ('"about.p1": "Je suis <strong>conseillère clientèle certifiée par la Industrie- und Handelskammer</strong>',
     '"about.p1": "Je suis <strong>conseillère clientèle certifiée</strong>'),
    ('"skills.c2": "Assurance (Industrie- und Handelskammer)"', '"skills.c2": "Assurance & Sinistres"'),
    ('"exp2.role": "Intermédiaire en assurances certifiée par la Industrie- und Handelskammer"',
     '"exp2.role": "Conseillère en assurances & gestionnaire sinistres"'),
    ('"exp2.role": "Conseillère certifiée Industrie- und Handelskammer en assurances"',
     '"exp2.role": "Conseillère en assurances & gestionnaire sinistres"'),
    ('"edu1": "Intermédiaire en assurances (Industrie- und Handelskammer) · Zurich Gruppe"',
     '"edu1": "Certification Professionnelle en Assurances · Zurich Gruppe"'),
    ('"edu1": "Conseillère en assurances certifiée Industrie- und Handelskammer · Zurich Gruppe"',
     '"edu1": "Certification Professionnelle en Assurances · Zurich Gruppe"'),
]
clean_file("i18n-de-fr.js", de_fr_replacements)

# 8. i18n-en-es.js
en_es_replacements = [
    # English:
    ('"hero.tagline": "I connect clients, cultures and solutions – backed by two Industrie- und Handelskammer qualifications',
     '"hero.tagline": "I connect clients, cultures and solutions – backed by two state-certified qualifications'),
    ('"stats.ihk": "Industrie- und Handelskammer qualifications"', '"stats.ihk": "Certified Qualifications"'),
    ('"about.p1": "I am an <strong>Industrie- und Handelskammer-certified insurance intermediary</strong>',
     '"about.p1": "I am a <strong>certified insurance and claims advisor</strong>'),
    ('"skills.c2": "Insurance (Industrie- und Handelskammer)"', '"skills.c2": "Insurance & Claims"'),
    ('"exp2.role": "Industrie- und Handelskammer-certified Insurance Intermediary"',
     '"exp2.role": "Insurance Intermediary & Claims Specialist"'),
    ('"edu1": "Industrie- und Handelskammer Insurance Intermediary qualification · Zurich Gruppe"',
     '"edu1": "Certified Insurance Intermediary qualification · Zurich Gruppe"'),
    # Spanish:
    ('"hero.tagline": "Conecto clientes, culturas y soluciones, con dos cualificaciones Industrie- und Handelskammer',
     '"hero.tagline": "Conecto clientes, culturas y soluciones, con doble titulación oficial'),
    ('"stats.ihk": "Cualificaciones Industrie- und Handelskammer"', '"stats.ihk": "Titulaciones Oficiales"'),
    ('"about.p1": "Soy <strong>mediadora de seguros certificada por la Industrie- und Handelskammer</strong>',
     '"about.p1": "Soy <strong>mediadora de seguros y asesora certificada</strong>'),
    ('"skills.c2": "Seguros (Industrie- und Handelskammer)"', '"skills.c2": "Seguros y Siniestros"'),
    ('"exp2.role": "Mediadora de seguros certificada Industrie- und Handelskammer"',
     '"exp2.role": "Gestora de Siniestros y Mediadora de Seguros"'),
    ('"edu1": "Mediadora de seguros Industrie- und Handelskammer · Zurich Gruppe"',
     '"edu1": "Certificación Oficial en Mediación de Seguros · Zurich Gruppe"'),
]
clean_file("i18n-en-es.js", en_es_replacements)

# 9. i18n-lb-pt.js
lb_pt_replacements = [
    # Luxembourgish:
    ('"hero.tagline": "Ech verbanne Clienten, Kulturen a Léisungen – mat zwou Industrie- und Handelskammer-Qualifikatiounen',
     '"hero.tagline": "Ech verbanne Clienten, Kulturen a Léisungen – mat zwee staatlech unerkannte Beruffsabschlëss'),
    ('"stats.ihk": "Industrie- und Handelskammer-Qualifikatiounen"', '"stats.ihk": "Staatlech Diplomer"'),
    ('"about.p1": "Ech si <strong>Versécherungsvermëttlerin mat Industrie- und Handelskammer-Ofschloss</strong>',
     '"about.p1": "Ech si <strong>zertifizéiert Versécherungsvermëttlerin</strong>'),
    ('"skills.c2": "Versécherung (Industrie- und Handelskammer)"', '"skills.c2": "Versécherung & Schuedmanagement"'),
    ('"exp2.role": "Versécherungsvermëttlerin Industrie- und Handelskammer"',
     '"exp2.role": "Versécherungsvermëttlerin & Schuedmanagerin"'),
    ('"edu1": "Versécherungsvermëttlerin Industrie- und Handelskammer · Zurich Gruppe"',
     '"edu1": "Zertifizéiert Versécherungsvermëttlerin · Zurich Gruppe"'),
    # Portuguese:
    ('"hero.tagline": "Ligo clientes, culturas e soluções – com duas qualificações Industrie- und Handelskammer',
     '"hero.tagline": "Ligo clientes, culturas e soluções – com duas qualificações profissionais certificadas'),
    ('"stats.ihk": "Qualificações Industrie- und Handelskammer"', '"stats.ihk": "Qualificações Certificadas"'),
    ('"about.p1": "Sou <strong>mediadora de seguros certificada pela Industrie- und Handelskammer</strong>',
     '"about.p1": "Sou <strong>mediadora de seguros e consultora certificada</strong>'),
    ('"skills.c2": "Seguros (Industrie- und Handelskammer)"', '"skills.c2": "Seguros e Sinistros"'),
    ('"exp2.role": "Mediadora de seguros certificada Industrie- und Handelskammer"',
     '"exp2.role": "Mediadora de Seguros Certificada e Gestora de Sinistros"'),
    ('"edu1": "Mediadora de seguros Industrie- und Handelskammer · Zurich Gruppe"',
     '"edu1": "Certificação Profissional em Seguros · Zurich Gruppe"'),
]
clean_file("i18n-lb-pt.js", lb_pt_replacements)

# 10. Copy cv.html to artifact directory as well
import shutil
shutil.copy("cv.html", "/Users/ark/.gemini/antigravity/brain/21aa43c9-3f3a-49ab-bc58-d86edacd4596/cv_amarilnta_selmanai_luxembourg.html")
print("Synced cv.html to brain artifact directory.")
