from app.core.tax import calculate_personal_income_tax

def gross_to_net(gross, num_dependents=0):
    bhxh = gross * 0.08
    bhyt = gross * 0.015
    bhtn = gross * 0.01
    ins_total = bhxh + bhyt + bhtn

    pre_tax_income = gross - ins_total

    gtc_ban_than = 11_000_000
    gtc_phu_thuoc = 4_400_000 * num_dependents
    taxable_income = max(0, pre_tax_income - gtc_ban_than - gtc_phu_thuoc)

    tax = calculate_personal_income_tax(taxable_income)
    net = pre_tax_income - tax

    return {
        "gross": gross,
        "bhxh": bhxh,
        "bhyt": bhyt,
        "bhtn": bhtn,
        "pre_tax_income": pre_tax_income,
        "gtc_ban_than": gtc_ban_than,
        "gtc_phu_thuoc": gtc_phu_thuoc,
        "taxable_income": taxable_income,
        "tax": tax,
        "net": net
    }

def net_to_gross(net, num_dependents=0, precision=1000):
    """
    Tính lương GROSS từ NET bằng phương pháp tìm kiếm nhị phân.
    """
    low = net
    high = net * 2  # Giả định upper bound
    result = None

    while low <= high:
        mid = (low + high) // 2
        calculated = gross_to_net(mid, num_dependents)
        net_calculated = calculated["net"]

        if abs(net_calculated - net) <= precision:
            result = calculated
            break
        elif net_calculated < net:
            low = mid + 1
        else:
            high = mid - 1

    if result:
        result["estimated_gross"] = mid
        return result
    else:
        return {"error": "Không tìm được GROSS phù hợp"}
