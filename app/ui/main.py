import streamlit as st
from app.core.converter import gross_to_net

st.title("💼 Chuyển đổi lương GROSS ➝ NET (VNĐ)")
gross = st.number_input("Nhập lương GROSS", min_value=0, step=500_000, value=20_000_000)
num_dependents = st.number_input("Số người phụ thuộc", min_value=0, step=1, value=2)

if st.button("Tính lương NET"):
    result = gross_to_net(gross, num_dependents)

    st.subheader("📊 Diễn giải chi tiết:")
    st.write(f"Lương GROSS: {result['gross']:,} VNĐ")
    st.write(f" - Bảo hiểm xã hội (8%): {result['bhxh']:,} VNĐ")
    st.write(f" - Bảo hiểm y tế (1.5%): {result['bhyt']:,} VNĐ")
    st.write(f" - Bảo hiểm thất nghiệp (1%): {result['bhtn']:,} VNĐ")
    st.write(f"Thu nhập trước thuế: {result['pre_tax_income']:,} VNĐ")
    st.write(f" - Giảm trừ bản thân: {result['gtc_ban_than']:,} VNĐ")
    st.write(f" - Giảm trừ người phụ thuộc: {result['gtc_phu_thuoc']:,} VNĐ")
    st.write(f"Thu nhập chịu thuế: {result['taxable_income']:,} VNĐ")
    st.write(f"Thuế TNCN: {result['tax']:,} VNĐ")
    st.success(f"✅ Lương NET: {result['net']:,} VNĐ")
