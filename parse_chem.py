import xml.etree.ElementTree as ET
import html

# Input questions and answers as a list of tuples (question_text, options, correct_option)
questions1_answers = [
   (r"What is the major product in the following reaction? \(\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}=\text{CH}_2 + \text{HBr}\)?", 
     [r"\(\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}_2-\text{CH}_2-\text{Br}\)", r"\(\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH(Br)}-\text{CH}_3\)", r"\(\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH(Br)}_2-\text{CH}_3\)", r"\(\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH(Br)}-\text{CH}_2-\text{Br}\)"], 
     "B"),
    (r"In the photo-electron emission, the energy of the emitted electron is", 
     [r"Greater than the incident photon", r"Same as that of the incident photon", r"Smaller than the incident photon", r"Proportional to the intensity of incident photon"], 
     "C"),
    (r"The equilibrium constant for the reaction, \(\text{N}_2(g) + 3\text{H}_2 \rightarrow 2\text{NH}_3(g)\) and \(\text{2N}_2(g) + 6\text{H}_2 \rightarrow 4\text{NH}_3(g)\) are \(K_1\) and \(K_2\) respectively. The relation between \(K_1\) and \(K_2\) is", 
     [r"\(K_2 = K_1^2\)", r"\(K_1 = K_2^2\)", r"\(K_2 = \sqrt{K_1}\)", r"\(K_1 = \sqrt{K_2}\)"], 
     "D"),
    (r"The compound that does not undergo hydrolysis by SN1 mechanism is", 
     [r"\(\text{C}_6\text{H}_5\text{CH}_2\text{Cl}\)", r"\(\text{C}_6\text{H}_5\text{CH(CH}_3\text{)Cl}\)", r"\(\text{C}_6\text{H}_5\text{Cl}\)", r"\(\text{CH}_3\text{CH}_2\text{Cl}\)"], 
     "C"),
    (r"The Henry's law constant for \(O_2\) dissolved in water is \(4.34 \times 10^4\) atm at a certain temperature. If the partial pressure of \(O_2\) in a gas mixture that is in equilibrium with water is \(0.434\) atm, what is the mole fraction of \(O_2\) in the solution?", 
     [r"\(1 \times 10^{-5}\)", r"\(1 \times 10^{-4}\)", r"\(2 \times 10^{-5}\)", r"\(1 \times 10^{-6}\)"], 
     "A"),
     (r"Match the following complexes (P) with the geometry (Q)", 
     [r"a)-(ii);b)-(iii);c)-(i);d)-(iv);e)-(v)", r"a)-(iii);b)-(v);c)-(iv);d)-(ii);e)-(i)", r"a)-(iv);b)-(iii);c)-(v);d)-(i);e)-(ii)", r"a)-(v);b)-(iv);c)-(ii);d)-(iii);e)-(i)"], 
     "B"),
    (r"Among the following which one is a non-reducing sugar?", 
     [r"Lactose", r"Glucose", r"Sucrose", r"Maltose"], 
     "C"),
    (r"If \(T\) is the surface tension of the soap solution, the amount of work done in blowing a soap bubble from diameter \(D\) to a diameter \(2D\) is", 
     [r"\(2\pi D^2T\)", r"\(4\pi D^2T\)", r"\(6\pi D^2T\)", r"\(8\pi D^2T\)"], 
     "C"),
    (r"The complex, \([\text{Pt(Py)(NH}_3)\text{BrCl}]\) will have how many geometrical isomers?", 
     [r"3", r"4", r"0", r"2"], 
     "A"),
    (r"The total number of possible isomers for the complex compound \([\text{Cu(NH}_3\text{)}_4][\text{PtCl}_4]\)", 
     [r"3", r"2", r"1", r"4"], 
     "D"),
    (r"Which one of the following polymers is a copolymer formed by condensation polymerisation?", 
     [r"Buna-S", r"Neoprene", r"Polythene", r"Melamine-formaldehyde"], 
     "D"),
    (r"Which one of the following sets forms the biodegradable polymer?", 
     [r"3-Hydroxybutanoic acid and 3-hydroxypentanoic acid", r"Acrylonitrile and 1,3-butadiene", r"Urea and formaldehyde", r"Ethylene glycol and terephthalic acid"], 
     "A"),
    (r"The antimicrobial drug that contains arsenic is", 
     [r"Prontosil", r"Salvarsan", r"Sulphapyridine", r"Ofloxacin"], 
     "B"),
    (r"Which one of the following statements is not correct?", 
     [r"All monosaccharides are reducing sugars", r"Lactose is commonly known as milk sugar", r"Glucose pentaacetate does not react with hydroxylamine", r"Glucose on oxidation with bromine water, gives saccharic acid"], 
     "E"),
    (r"Which one of the following is an antifertility drug?", 
     [r"Bithionol", r"Aspartame", r"Ofloxacin", r"Norethindrone"], 
     "D"),
    (r"Which one of the following is a greenhouse gas?", 
     [r"Methane", r"Acetylene", r"Ethane", r"Ethylene"], 
     "A"),
    (r"Which one of the following is not an isomer of 3-methylbut-1-yne?", 
     [r"2,3-Dimethylbuta-1,3-diene", r"Penta-1,3-diene", r"Pent-1-yne", r"2-Methylbuta-1,3-diene"], 
     "A"),
    (r"How many \(\sigma\) and \(\pi\) bonds are there in pent-3-ene-1-yne?", 
     [r"10\sigma, 3\pi", r"8\sigma, 10\pi", r"3\sigma, 10\pi", r"9\sigma, 5\pi"], 
     "A"),
    (r"Which one of the following is a secondary alcohol?", 
     [r"2-methylbutan-2-ol", r"3-methylbutan-2-ol", r"3-methylbutan-1-ol", r"2-methylbutan-1-ol"], 
     "B"),
    (r"An organic compound 'A' with molecular formula \(\text{C}_7\text{H}_6\text{O}\) forms 2,4-DNP derivative and reduces Tollens' reagent. When 'A' is heated with conc. \(\text{KOH}\), it gives sodium benzoate and compound 'B'. The compound 'B' is", 
     [r"Benzene", r"Benzaldehyde", r"Toluene", r"Benzyl alcohol"], 
     "D"),
     (r"Adsorption is accompanied by", 
     [r"decrease in enthalpy and decrease in entropy", r"increase in enthalpy and decrease in entropy", r"decrease in enthalpy and increase in entropy", r"increase in enthalpy and increase in entropy"], 
     "A"),
    (r"In the coagulation of a positive sol, the flocculating power of the ions \( \text{PO}_4^{3-}, \text{SO}_4^{2-} \) and \( \text{Cl}^- \) decreases in the order", 
     [r"\( \text{PO}_4^{3-} > \text{Cl}^- > \text{SO}_4^{2-} \)", r"\( \text{PO}_4^{3-} > \text{SO}_4^{2-} > \text{Cl}^- \)", r"\( \text{Cl}^- > \text{SO}_4^{2-} > \text{PO}_4^{3-} \)", r"\( \text{SO}_4^{2-} > \text{PO}_4^{3-} > \text{Cl}^- \)"], 
     "B"),
    (r"Which one of the following nitrates does not give the corresponding metallic oxide, nitrogen dioxide and oxygen on heating?", 
     [r"Lithium nitrate", r"Beryllium nitrate", r"Magnesium nitrate", r"Potassium nitrate"], 
     "E"),
    (r"3g urea is dissolved in 45g of water. The relative lowering of vapour pressure is", 
     [r"0.05", r"0.04", r"0.02", r"0.01"], 
     "C"),
    (r"Which of the following halogens always shows only one oxidation state?", 
     [r"Cl", r"Br", r"I", r"F"], 
     "D"),
     (r"Which of the following is not a Lewis base?", 
     [r"CH_4", r"C_2H_5OH", r"Acetone", r"Sec amine"], 
     "A"),
    (r"Methanol and ethanol can be distinguished by", 
     [r"Iodoform test", r"Schiff's reagent", r"KMnO_4/OH^-", r"K_2Cr_2O_7/H^+"], 
     "A"),
    (r"The ease of esterification of alcohols", 
     [r"3° > 2° > 1°", r"2° > 3° > 1°", r"1° > 2° > 3°", r"1° > 3° > 2°"], 
     "C"),
    (r"Bell metal is an alloy of", 
     [r"Cu & Sn", r"Cu & Zn", r"Cu & Al", r"Cu, Zn & Sn"], 
     "A"),
    (r"Carbon monoxide reduction process is used for the extraction of", 
     [r"Cu", r"Ag", r"Sn", r"Fe"], 
     "D")
    ]

questions_answers =[  (
        r"What is the major product in the following reaction? \( \text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}=CH_2 + \text{HBr} \)?",
        [r"a) \( \text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}_2-\text{CH}_2-\text{Br} \)", 
         r"b) \( \text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}(Br)-\text{CH}_3 \)", 
         r"c) \( \text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}(Br)_2-\text{CH}_3 \)", 
         r"d) \( \text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}(Br)-\text{CH}_2-\text{Br} \)"],
        "B"
    ),
    (
        r"In the photo-electron emission, the energy of the emitted electron is",
        [r"A. Greater than the incident photon", 
         r"B. Same as that of the incident photon", 
         r"C. Smaller than the incident photon", 
         r"D. Proportional to the intensity of the incident photon"],
        "C"
    ),
    (
        r"The equilibrium constant for the reaction, \( \text{N}_2(g) + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3(g) \) and \( 2\text{N}_2(g) + 6\text{H}_2 \rightleftharpoons 4\text{NH}_3(g) \) are \( K_1 \) and \( K_2 \) respectively. The relation between \( K_1 \) and \( K_2 \) is",
        [r"a) \( K_2 = K_1^2 \)", 
         r"b) \( K_1 = K_2^2 \)", 
         r"c) \( K_2 = vK_1 \)", 
         r"d) \( K_1 = vK_2 \)"],
        "D"
    ),
    (
        r"The compound that does not undergo hydrolysis by SN1 mechanism is",
        [r"a) \( \text{C}_6\text{H}_5\text{CH}_2\text{Cl} \)", 
         r"b) \( \text{C}_6\text{H}_5\text{CH}(\text{CH}_3)\text{Cl} \)", 
         r"c) \( \text{C}_6\text{H}_5\text{Cl} \)", 
         r"d) \( \text{CH}_3\text{CH}_2\text{Cl} \)"],
        "C"
    ),
    (
        r"The Henry's law constant for \( \text{O}_2 \) dissolved in water is \( 4.34 \times 10^4 \) atm at a certain temperature. If the partial pressure of \( \text{O}_2 \) in a gas mixture that is in equilibrium with water is \( 0.434 \) atm, what is the mole fraction of \( \text{O}_2 \) in the solution?",
        [r"a) \( 1 \times 10^{-5} \)", 
         r"b) \( 1 \times 10^{-4} \)", 
         r"c) \( 2 \times 10^{-5} \)", 
         r"d) \( 1 \times 10^{-6} \)"],
        "A"
    ),
     (
        r"Match the following complexes (P) with the geometry (Q)",
        [
            r"a) \( a \) - (ii); \( b \) - (iii); \( c \) - (i); \( d \) - (iv); \( e \) - (v)", 
            r"b) \( a \) - (iii); \( b \) - (v); \( c \) - (iv); \( d \) - (ii); \( e \) - (i)", 
            r"c) \( a \) - (iv); \( b \) - (iii); \( c \) - (v); \( d \) - (i); \( e \) - (ii)", 
            r"d) \( a \) - (v); \( b \) - (iv); \( c \) - (ii); \( d \) - (iii); \( e \) - (i)"
        ],
        "B"
    ),
    (
        r"Among the following, which one is a non-reducing sugar?",
        [r"a) Lactose", r"b) Glucose", r"c) Sucrose", r"d) Maltose"],
        "C"
    ),
    (
        r"If \( T \) is the surface tension of the soap solution, the amount of work done in blowing a soap bubble from diameter \( D \) to a diameter \( 2D \) is",
        [r"a) \( 2\pi D^2 T \)", r"b) \( 4\pi D^2 T \)", r"c) \( 6\pi D^2 T \)", r"d) \( 8\pi D^2 T \)"],
        "C"
    ),
    (
        r"The complex, \([ \text{Pt(Py)(NH}_3)_3 \text{)BrCl]}\) will have how many geometrical isomers?",
        [r"A. 3", r"B. 4", r"C. 0", r"D. 2"],
        "A"
    ),
    (
        r"The total number of possible isomers for the complex compound \([ \text{Cu(NH}_3)_4] [\text{PtCl}_4]\)",
        [r"A. 3", r"B. 2", r"C. 1", r"D. 4"],
        "D"
    ),
     (
        r"Which one of the following polymer is a copolymer formed by condensation polymerisation?",
        [
            r"(A) Buna-S",
            r"(B) Neoprene",
            r"(C) Polythene",
            r"(D) Melamine-formaldehyde",
            r"(E) Buna-N"
        ],
        "D"
    ),
    (
        r"Which one of the following sets forms the biodegradable polymer?",
        [
            r"(A) 3-Hydroxybutanoic acid and 3-hydroxypentanoic acid.",
            r"(B) Acrylonitrile and 1,3-butadiene.",
            r"(C) Urea and formaldehyde.",
            r"(D) Ethylene glycol and terephthalic acid.",
            r"(E) Adipic acid and hexamethylene diamine."
        ],
        "A"
    ),
    (
        r"The antimicrobial drug that contains arsenic is",
        [
            r"(A) Prontosil",
            r"(B) Salvarsan",
            r"(C) Sulphapyridine",
            r"(D) Ofloxacin",
            r"(E) Sulphanilamide"
        ],
        "B"
    ),
    (
        r"Which one of the following statements is not correct?",
        [
            r"(A) All monosaccharides are reducing sugars.",
            r"(B) Lactose is commonly known as milk sugar.",
            r"(C) Glucose pentaacetate does not react with hydroxylamine.",
            r"(D) Glucose does not give 2,4- DNP test.",
            r"(E) Glucose on oxidation with bromine water, gives saccharic acid."
        ],
        "E"
    ),
    (
        r"Which one of the following is an antifertility drug?",
        [
            r"(A) Bithionol",
            r"(B) Aspartame",
            r"(C) Ofloxacin",
            r"(D) Norethindrone",
            r"(E) Terpineol"
        ],
        "D"
    ),
        (
        r"Which one of the following is a greenhouse gas?",
        [
            r"(A) Methane",
            r"(B) Acetylene",
            r"(C) Ethane",
            r"(D) Ethylene",
            r"(E) Hydrogen sulphide"
        ],
        "A"
    ),
    (
        r"Which one of the following is not an isomer of 3-methylbut-1-yne?",
        [
            r"(A) 2,3-Dimethylbuta-1,3-diene",
            r"(B) Penta-1,3-diene",
            r"(C) Pent-1-yne",
            r"(D) 2-Methylbuta-1,3-diene",
            r"(E) Pent-2-yne"
        ],
        "A"
    ),
    (
        r"How many s and p bond are there in pent-3-ene-1-yne?",
        [
            r"(A) 10s, 3p",
            r"(B) 8s, 10p",
            r"(C) 3s, 10p",
            r"(D) 9s, 5p"
        ],
        "A"
    ),
    (
        r"Which one of the following is a secondary alcohol?",
        [
            r"(A) 2-methylbutan-2-ol",
            r"(B) 3-methylbutan-2-ol",
            r"(C) 3-methylbutan-1-ol",
            r"(D) 2-methylbutan-1-ol",
            r"(E) 2,2-dimethylbutan-1-ol"
        ],
        "B"
    ),
    (
        r"An organic compound 'A' with molecular formula C7H6O forms 2,4-DNP derivative and reduces Tollens' reagent. When 'A' is heated with conc. KOH, it gives sodium benzoate and compound 'B'. The compound 'B' is",
        [
            r"(A) Benzene",
            r"(B) Benzaldehyde",
            r"(C) Toluene",
            r"(D) Benzyl alcohol",
            r"(E) Acetophenone"
        ],
        "D"
    ),
     (
        r"Adsorption is accompanied by",
        [
            r"(A) decrease in enthalpy and decrease in entropy",
            r"(B) increase in enthalpy and decrease in entropy",
            r"(C) decrease in enthalpy and increase in entropy",
            r"(D) increase in enthalpy and increase in entropy",
            r"(E) no change in enthalpy and entropy"
        ],
        "A"
    ),
    (
        r"In the coagulation of a positive sol, the flocculating power of the ions PO4³, SO4² and CI decreases in the order",
        [
            r"(A) PO4> CI> SO4²",
            r"(B) PO4>SO4>Cl",
            r"(C) CI> SO4> PO4³",
            r"(D) SO4>PO4> Cl",
            r"(E) CI>PO4³> SO4²-"
        ],
        "B"
    ),
    (
        r"Which one of the following nitrates does not give the corresponding metallic oxide, nitrogen dioxide and oxygen on heating?",
        [
            r"(A) Lithium nitrate",
            r"(B) Beryllium nitrate",
            r"(C) Magnesium nitrate",
            r"(D) Calcium nitrate",
            r"(E) Potassium nitrate"
        ],
        "E"
    ),
    (
        r"3g urea is dissolved in 45 of water. The relative lowering of vapour pressure is",
        [
            r"A)0.05",
            r"B)0.04",
            r"C)0.02",
            r"D)0.01",
            r"E)0.1"
        ],
        "C"
    ),
    (
        r"Which of the following halogens always show only one oxidation state?",
        [
            r"A) Cl",
            r"B) Br",
            r"C) I",
            r"D) F",
            r"E) O"
        ],
        "D"
    ), (
        r"Which of the following is not a Lewis base?",
        [
            r"A) CH₄",
            r"B) C₂H₅OH",
            r"C) Acetone",
            r"D) Sec amine",
            r"E) None"
        ],
        "A"
    ),
    (
        r"Methanol and ethanol can be distinguished by",
        [
            r"A) Iodoform test",
            r"B) Schiff's reagent",
            r"C) KMnO₄/OH⁻",
            r"D) K₂Cr₂O₇/H⁺",
            r"E) Borsches reagent"
        ],
        "A"
    ),
    (
        r"The ease of esterification of alcohols is",
        [
            r"A) 3° > 2° > 1°",
            r"B) 2° > 3° > 1°",
            r"C) 1° > 2° > 3°",
            r"D) 1° > 3° > 2°",
            r"E) 3° > 1° > 2°"
        ],
        "C"
    ),
    (
        r"Bell metal is an alloy of",
        [
            r"A) Cu & Sn",
            r"B) Cu & Zn",
            r"C) Cu & Al",
            r"D) Cu, Zn & Sn",
            r"E) Cu & Ni"
        ],
        "A"
    ),
    (
        r"Carbon monoxide reduction process is used for the extraction of",
        [
            r"A) Cu",
            r"B) Ag",
            r"C) Sn",
            r"D) Fe",
            r"E) Au"
        ],
        "D"
    )

    ]
# Corresponding answers list
answers = [
    "B", "C", "D", "C", "A", 
    "B", "C", "C", "A", "D", 
    "D", "A", "B", "E", "D", 
    "A", "A", "A", "B", "D", 
    "A", "B", "E", "C", "D", 
    "A", "A", "C", "A", "D", 
    "B", "E", "B"
]

def create_question_xml(question_text, options, correct_option, question_number):
    question = ET.Element('question', type='multichoice')
    
    name = ET.SubElement(question, 'name')
    text = ET.SubElement(name, 'text')
    text.text = f'Chemistry Question {question_number}'

    questiontext = ET.SubElement(question, 'questiontext', format='html')
    text = ET.SubElement(questiontext, 'text')
    text.text = html.escape(question_text)

    defaultgrade = ET.SubElement(question, 'defaultgrade')
    defaultgrade.text = '4'

    penalty = ET.SubElement(question, 'penalty')
    penalty.text = '1'

    single = ET.SubElement(question, 'single')
    single.text = 'true'

    shuffleanswers = ET.SubElement(question, 'shuffleanswers')
    shuffleanswers.text = 'true'

    answernumbering = ET.SubElement(question, 'answernumbering')
    answernumbering.text = 'abc'

    for i, option in enumerate(options):
        answer = ET.SubElement(question, 'answer', fraction="100" if chr(65 + i) == correct_option else "0")
        text = ET.SubElement(answer, 'text')
        text.text = option
        
        feedback = ET.SubElement(answer, 'feedback')
        text = ET.SubElement(feedback, 'text')
        text.text = ""

    return question

def create_quiz_xml(questions_answers, answers):
    quiz = ET.Element('quiz')
    for i, (question_text, options, _) in enumerate(questions_answers):
        correct_option = answers[i]
        question = create_question_xml(question_text, options, correct_option, i + 1)
        quiz.append(question)
    return quiz

# Create XML structure
quiz_xml = create_quiz_xml(questions_answers, answers)

# Convert to a string
xml_str = ET.tostring(quiz_xml, encoding='unicode')

# Write to file
with open('moodle_chem_questions.xml', 'w', encoding='utf-8') as f:
    f.write(xml_str)

print("Moodle XML file has been created successfully.")
