# Ders isimleri, notlar ve kredileri tabloya aktardım 
# Sadece kredili dersler ve ağırlıklı notlar dikkate alındı.

# Derslerin not ve kredi bilgileri:
courses = [
    {"name": "CHEM105", "grade": "P", "credit": 4},
    {"name": "MATH101", "grade": "BB", "credit": 4},
    {"name": "CMPE150", "grade": "DD", "credit": 3},
    {"name": "PHYS121", "grade": "DC", "credit": 4},
    {"name": "EC101", "grade": "CC", "credit": 3},
    {"name": "CMPE160", "grade": "DC", "credit": 4},
    {"name": "MATH102", "grade": "DD", "credit": 4},
    {"name": "EC102", "grade": "CB", "credit": 3},
    {"name": "PHYS201", "grade": "DD", "credit": 4},
    {"name": "CMPE220", "grade": "DD", "credit": 3},
    {"name": "MATH201", "grade": "CC", "credit": 4},
    {"name": "CMPE250", "grade": "CB", "credit": 4},
    {"name": "EE210", "grade": "CC", "credit": 3},
    {"name": "CMPE230", "grade": "DD", "credit": 4},
    {"name": "EE212", "grade": "BB", "credit": 3},
    {"name": "CMPE240", "grade": "CB", "credit": 4},
    {"name": "MATH202", "grade": "CC", "credit": 4},
    {"name": "CMPE300", "grade": "DC", "credit": 3},
    {"name": "CMPE322", "grade": "CB", "credit": 4},
    {"name": "CMPE344", "grade": "CC", "credit": 4},
    {"name": "CMPE321", "grade": "BB", "credit": 4},
    {"name": "CMPE362", "grade": "CC", "credit": 4},
    {"name": "CMPE350", "grade": "DC", "credit": 3},
    {"name": "CMPE352", "grade": "BA", "credit": 2},
    {"name": "CMPE483", "grade": "BB", "credit": 3},
    {"name": "CMPE443", "grade": "CB", "credit": 4},
    {"name": "CMPE451", "grade": "BB", "credit": 2},
    {"name": "CMPE475", "grade": "CB", "credit": 3},
    {"name": "CMPE49T", "grade": "CB", "credit": 3},
    {"name": "CMPE485", "grade": "CB", "credit": 3},
    {"name": "CMPE496", "grade": "BA", "credit": 3},
    {"name": "ESC307", "grade": "BA", "credit": 3},
]

# Not ağırlıkları tablosu.
grade_weights = {
    "AA": 4.00,
    "BA": 3.50,
    "BB": 3.00,
    "CB": 2.50,
    "CC": 2.00,
    "DC": 1.50,
    "DD": 1.00,
    "F": 0.00,
    "P": None,  # Ağırlıksız dersler.
}

# GPA hesaplama.
total_credits = 0
total_weighted_scores = 0

for course in courses:
    grade = course["grade"]
    credit = course["credit"]
    weight = grade_weights.get(grade, 0)
    
    if weight is not None:  # Ağırlıksız dersleri dışarıda bırak.
        total_credits += credit
        total_weighted_scores += weight * credit

        

gpa = total_weighted_scores / total_credits if total_credits > 0 else 0
print("GPA calculated as : " ,gpa)
