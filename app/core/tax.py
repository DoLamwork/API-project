# Bảng thuế TNCN lũy tiến từng phần
TAX_BRACKETS = [
    (5_000_000, 0.05),
    (10_000_000, 0.10),
    (18_000_000, 0.15),
    (32_000_000, 0.20),
    (52_000_000, 0.25),
    (80_000_000, 0.30),
    (float('inf'), 0.35),
]

def calculate_personal_income_tax(taxable_income):
    remaining = taxable_income
    tax = 0.0
    prev_limit = 0

    for limit, rate in TAX_BRACKETS:
        if remaining <= 0:
            break
        taxable_part = min(remaining, limit - prev_limit)
        tax += taxable_part * rate
        remaining -= taxable_part
        prev_limit = limit

    return round(tax)
