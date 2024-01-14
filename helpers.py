def categorize_imc(bmi, categories):
    for category, (lower, upper) in categories.items():
        if lower <= bmi <= upper:
            return category