import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

# Expanded knowledge base
knowledge_base = {
    'symptoms': {
        'fever': {
            'conditions': ['flu', 'common cold', 'malaria', 'typhoid', 'dengue', 'COVID-19', 'pneumonia'],
            'actions': 'Take rest and drink plenty of fluids. If persistent, consult a doctor.'
        },
        'cough': {
            'conditions': ['flu', 'common cold', 'pneumonia', 'bronchitis', 'asthma', 'tuberculosis', 'COVID-19'],
            'actions': 'Consult a doctor and consider getting a chest X-ray.'
        },
        'headache': {
            'conditions': ['flu', 'migraine', 'sinusitis', 'stress', 'hypertension', 'brain tumor', 'meningitis'],
            'actions': 'Take pain relievers and rest in a quiet, dark room.'
        },
        'rash': {
            'conditions': ['allergy', 'eczema', 'measles', 'chickenpox', 'psoriasis', 'shingles', 'scarlet fever'],
            'actions': 'Avoid allergens and moisture on the affected area.'
        },
        'fatigue': {
            'conditions': ['flu', 'anemia', 'depression', 'thyroid disorder', 'diabetes', 'chronic fatigue syndrome', 'cancer'],
            'actions': 'Get plenty of sleep and consider iron-rich foods.'
        },
        'chest pain': {
            'conditions': ['heart attack', 'angina', 'acid reflux', 'anxiety', 'pneumonia', 'pulmonary embolism'],
            'actions': 'Seek emergency medical attention immediately.'
        },
        'shortness of breath': {
            'conditions': ['asthma', 'pneumonia', 'COPD', 'heart failure', 'COVID-19', 'pulmonary embolism'],
            'actions': 'Consult a doctor and avoid physical exertion.'
        },
        'nausea': {
            'conditions': ['food poisoning', 'pregnancy', 'gastritis', 'migraine', 'vertigo', 'gastroenteritis'],
            'actions': 'Stay hydrated and eat bland food. Consult a doctor if it persists.'
        },
        'vomiting': {
            'conditions': ['food poisoning', 'gastroenteritis', 'pregnancy', 'appendicitis', 'migraine', 'hepatitis'],
            'actions': 'Stay hydrated and avoid solid food until symptoms improve.'
        },
        'diarrhea': {
            'conditions': ['food poisoning', 'gastroenteritis', 'irritable bowel syndrome (IBS)', 'cholera', 'Crohn\'s disease', 'celiac disease'],
            'actions': 'Stay hydrated and avoid dairy or fatty foods.'
        },
        'sore throat': {
            'conditions': ['common cold', 'strep throat', 'tonsillitis', 'COVID-19', 'laryngitis'],
            'actions': 'Gargle with salt water and drink warm fluids.'
        },
        'runny nose': {
            'conditions': ['common cold', 'allergic rhinitis', 'sinus infection', 'COVID-19', 'hay fever'],
            'actions': 'Use a saline nasal spray and stay hydrated.'
        },
        'back pain': {
            'conditions': ['muscle strain', 'slipped disc', 'arthritis', 'kidney infection', 'sciatica', 'spinal stenosis'],
            'actions': 'Rest and apply hot or cold compress. Seek medical advice if persistent.'
        },
        'joint pain': {
            'conditions': ['arthritis', 'gout', 'injury', 'lupus', 'rheumatoid arthritis'],
            'actions': 'Apply ice and rest. Consult a doctor if pain persists.'
        },
        'dizziness': {
            'conditions': ['vertigo', 'anemia', 'low blood pressure', 'dehydration', 'migraine', 'inner ear infection', 'hypoglycemia'],
            'actions': 'Sit or lie down until the dizziness passes.'
        },
        'weight loss': {
            'conditions': ['diabetes', 'hyperthyroidism', 'cancer', 'malabsorption syndrome', 'anorexia', 'tuberculosis'],
            'actions': 'Consult a doctor for a thorough medical examination.'
        },
        'itching': {
            'conditions': ['allergy', 'scabies', 'liver disease', 'eczema', 'psoriasis', 'ringworm'],
            'actions': 'Avoid scratching and use anti-itch creams.'
        },
        'swelling': {
            'conditions': ['injury', 'infection', 'heart failure', 'kidney disease', 'lymphedema'],
            'actions': 'Elevate the affected area and apply cold compress.'
        },
        'blurred vision': {
            'conditions': ['diabetes', 'cataracts', 'glaucoma', 'migraine', 'macular degeneration', 'retinal detachment'],
            'actions': 'Consult an ophthalmologist immediately.'
        },
        'abdominal pain': {
            'conditions': ['appendicitis', 'gastritis', 'ulcer', 'gallstones', 'pancreatitis', 'intestinal obstruction'],
            'actions': 'Avoid solid food and consult a doctor if the pain persists.'
        },
        'bloating': {
            'conditions': ['irritable bowel syndrome (IBS)', 'lactose intolerance', 'gastritis', 'constipation', 'Celiac disease'],
            'actions': 'Avoid foods that cause gas and stay hydrated.'
        },
        'yellow skin': {
            'conditions': ['hepatitis', 'liver disease', 'jaundice', 'pancreatic cancer', 'bile duct obstruction'],
            'actions': 'Seek immediate medical attention for possible liver issues.'
        },
        'night sweats': {
            'conditions': ['tuberculosis', 'HIV', 'menopause', 'lymphoma', 'hyperthyroidism', 'brucellosis'],
            'actions': 'Consult a doctor to investigate the underlying cause.'
        },
        'frequent urination': {
            'conditions': ['diabetes', 'urinary tract infection (UTI)', 'prostate issues', 'bladder infection', 'interstitial cystitis'],
            'actions': 'Drink plenty of water and consult a doctor.'
        },
        'dark urine': {
            'conditions': ['dehydration', 'hepatitis', 'liver disease', 'kidney stones', 'hematuria'],
            'actions': 'Drink plenty of fluids and consult a doctor if it persists.'
        },
        'hair loss': {
            'conditions': ['alopecia', 'hypothyroidism', 'stress', 'lupus', 'vitamin deficiency', 'scalp infection'],
            'actions': 'Consult a doctor for a proper diagnosis and treatment.'
        },
        'dry skin': {
            'conditions': ['eczema', 'psoriasis', 'dehydration', 'hypothyroidism', 'dermatitis'],
            'actions': 'Use moisturizers and stay hydrated.'
        },
        'confusion': {
            'conditions': ['stroke', 'dementia', 'hypoglycemia', 'head injury', 'brain tumor'],
            'actions': 'Seek immediate medical attention if confusion is sudden or severe.'
        },
        'numbness': {
            'conditions': ['stroke', 'multiple sclerosis', 'nerve damage', 'diabetic neuropathy'],
            'actions': 'Consult a doctor, especially if numbness is sudden or persistent.'
        },
        'palpitations': {
            'conditions': ['anxiety', 'hyperthyroidism', 'arrhythmia', 'heart disease', 'electrolyte imbalance'],
            'actions': 'Try to relax, but consult a doctor if palpitations are frequent.'
        },
        'cold hands and feet': {
            'conditions': ['Raynaud\'s disease', 'anemia', 'hypothyroidism', 'poor circulation', 'frostbite'],
            'actions': 'Keep warm and consult a doctor if the condition persists.'
        },
        'memory loss': {
            'conditions': ['dementia', 'Alzheimer\'s disease', 'stroke', 'depression', 'brain injury', 'Parkinson\'s disease'],
            'actions': 'Consult a doctor for a neurological examination.'
        },
        'tremors': {
            'conditions': ['Parkinson\'s disease', 'essential tremor', 'multiple sclerosis', 'anxiety', 'hyperthyroidism'],
            'actions': 'Consult a neurologist for a thorough examination.'
        },
        'difficulty swallowing': {
            'conditions': ['stroke', 'esophagitis', 'GERD', 'tonsillitis', 'throat cancer'],
            'actions': 'Consult a doctor for an endoscopic examination.'
        },
        'constipation': {
            'conditions': ['irritable bowel syndrome (IBS)', 'dehydration', 'hypothyroidism', 'colon cancer', 'bowel obstruction'],
            'actions': 'Increase fiber intake, drink water, and consult a doctor if persistent.'
        },
        'increased thirst': {
            'conditions': ['diabetes', 'dehydration', 'kidney disease', 'hypercalcemia'],
            'actions': 'Drink plenty of fluids and consult a doctor for further evaluation.'
        },
        'red eyes': {
            'conditions': ['conjunctivitis', 'glaucoma', 'eye injury', 'dry eye syndrome', 'uveitis'],
            'actions': 'Use lubricating eye drops and consult an eye doctor if it persists.'
        },
        'bleeding gums': {
            'conditions': ['gingivitis', 'scurvy', 'blood disorder', 'leukemia', 'vitamin deficiency'],
            'actions': 'Practice good oral hygiene and consult a dentist.'
        },
        'muscle pain': {
            'conditions': ['muscle strain', 'fibromyalgia', 'polymyalgia rheumatica', 'rhabdomyolysis'],
            'actions': 'Rest and consult a doctor if pain persists.'
        },
        'high blood pressure': {
            'conditions': ['hypertension', 'kidney disease', 'pheochromocytoma', 'Cushing syndrome'],
            'actions': 'Consult a doctor to manage high blood pressure.'
        },
        'abnormal bleeding': {
            'conditions': ['bleeding disorders', 'liver disease', 'leukemia', 'vitamin K deficiency'],
            'actions': 'Consult a hematologist or doctor to address the underlying cause.'
        },
        'difficulty breathing': {
            'conditions': ['asthma', 'chronic obstructive pulmonary disease (COPD)', 'pulmonary fibrosis', 'anaphylaxis'],
            'actions': 'Seek emergency medical care if breathing difficulties are severe.'
        },
        'seizures': {
            'conditions': ['epilepsy', 'stroke', 'brain tumor', 'head injury', 'high fever'],
            'actions': 'Seek immediate medical attention if experiencing seizures.'
        },
        'yellow eyes': {
            'conditions': ['jaundice', 'hepatitis', 'liver disease', 'gallbladder disease'],
            'actions': 'Consult a doctor for liver function tests and evaluation.'
        },
        'loss of appetite': {
            'conditions': ['gastroenteritis', 'depression', 'chronic illness', 'stomach cancer'],
            'actions': 'Consult a doctor if loss of appetite persists or is accompanied by other symptoms.'
        },
        'unexplained weight gain': {
            'conditions': ['hypothyroidism', 'Cushing syndrome', 'congestive heart failure', 'polycystic ovary syndrome (PCOS)'],
            'actions': 'Consult a doctor for a proper diagnosis and management plan.'
        },
        'persistent cough': {
            'conditions': ['chronic bronchitis', 'whooping cough', 'postnasal drip', 'lung cancer'],
            'actions': 'Consult a doctor for further evaluation and treatment.'
        },
        'ear pain': {
            'conditions': ['ear infection', 'earwax buildup', 'temporal mandibular joint (TMJ) disorder', 'sinus infection'],
            'actions': 'Consult a doctor or ENT specialist for proper diagnosis.'
        },
        'difficulty concentrating': {
            'conditions': ['ADHD', 'depression', 'anxiety', 'sleep disorders', 'chronic fatigue syndrome'],
            'actions': 'Consult a healthcare provider for a thorough evaluation.'
        },
        'skin lesions': {
            'conditions': ['skin cancer', 'herpes simplex', 'shingles', 'ringworm', 'lupus'],
            'actions': 'Consult a dermatologist for examination and treatment.'
        },
        'bad breath': {
            'conditions': ['halitosis', 'gum disease', 'stomach issues', 'diabetes', 'kidney disease'],
            'actions': 'Maintain good oral hygiene and consult a doctor if persistent.'
        }
    }
}

def diagnose_conditions(symptoms):
    possible_conditions = set()
    actions = []

    for symptom in symptoms:
        if symptom in knowledge_base['symptoms']:
            symptom_conditions = knowledge_base['symptoms'][symptom]['conditions']
            symptom_action = knowledge_base['symptoms'][symptom]['actions']
            possible_conditions.update(symptom_conditions)
            actions.append(symptom_action)

    return list(possible_conditions), actions

# GUI using Tkinter
def main():
    def diagnose():
        selected_symptoms = [symptom_listbox.get(idx) for idx in symptom_listbox.curselection()]
        if selected_symptoms:
            possible_conditions, actions = diagnose_conditions(selected_symptoms)

            if possible_conditions:
                result_conditions = "Possible conditions:\n" + "\n".join(f"- {condition}" for condition in possible_conditions)
                result_actions = "\n\nRecommended actions:\n" + "\n".join(f"- {action}" for action in actions)
                result_text = result_conditions + result_actions
                result_display.config(state=tk.NORMAL)
                result_display.delete(1.0, tk.END)
                result_display.insert(tk.INSERT, result_text)
                result_display.config(state=tk.DISABLED)
            else:
                messagebox.showinfo("No Match", "No matching conditions found for the symptoms entered.")
        else:
            messagebox.showwarning("Input Error", "Please select at least one symptom.")
    
    def clear_selections():
        symptom_listbox.selection_clear(0, tk.END)
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.config(state=tk.DISABLED)

    # Setting up the GUI
    root = tk.Tk()
    root.title("Medical Diagnosis Expert System")
    root.geometry("650x500")
    root.configure(bg="#f0f0f0")

     # Title label
    title_label = tk.Label(root, text="Symptom-Based Medical Diagnosis", font=("Arial", 16, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)
    
    # Information section
    info_label = tk.Label(root, text=(
        "Welcome to the Medical Diagnosis Expert System.\n"
        "This tool helps you identify possible conditions based on symptoms.\n"
        "It is not a substitute for professional medical advice.\n"
        "If symptoms persist or worsen, seek medical attention."
    ), font=("Arial", 10), bg="#f0f0f0", justify="center")
    info_label.pack(pady=10)


    # Symptom selection label
    symptom_label = tk.Label(root, text="Select symptoms:", bg="#f0f0f0")
    symptom_label.pack()

    # Symptom list box with scrollbar
    symptom_frame = tk.Frame(root)
    symptom_frame.pack(pady=5)

    symptom_listbox = tk.Listbox(symptom_frame, selectmode=tk.MULTIPLE, height=8, width=50)
    scrollbar = tk.Scrollbar(symptom_frame, orient=tk.VERTICAL)
    symptom_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=symptom_listbox.yview)

    # Add symptoms to the listbox
    symptoms = list(knowledge_base['symptoms'].keys())
    for symptom in symptoms:
        symptom_listbox.insert(tk.END, symptom)

    symptom_listbox.pack(side=tk.LEFT)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Diagnose and Clear buttons
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)

    diagnose_button = tk.Button(button_frame, text="Diagnose", command=diagnose, bg="#4CAF50", fg="white", width=15)
    diagnose_button.grid(row=0, column=0, padx=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_selections, bg="#f44336", fg="white", width=15)
    clear_button.grid(row=0, column=1, padx=10)

    # Diagnosis result display
    result_label = tk.Label(root, text="Diagnosis Result:", bg="#f0f0f0")
    result_label.pack()

    result_display = scrolledtext.ScrolledText(root, height=8, width=70, wrap=tk.WORD, state=tk.DISABLED, bg="#e0e0e0")
    result_display.pack(pady=5)

    # Warning message label below the result box
    warning_label = tk.Label(root, text="⚠️ If symptoms persist or worsen, seek medical attention immediately.", 
                             font=("Arial", 10, "bold"), fg="red", bg="#f0f0f0")
    warning_label.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
