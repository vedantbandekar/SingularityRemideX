import streamlit as st

st.markdown("## Complete Medicine Care Solution")
st.markdown(
    """
    A **smart and user-friendly platform** to help users  
    manage **medicine intake schedules**, track **expiry dates**,  
    and gain **awareness about medicines** they consume.
    """
)

st.markdown('<div class="green-btn">', unsafe_allow_html=True)
st.button("Get Started")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("⏰ Smart Reminders\n\nNever miss a dose")

with c2:
    st.info("📦 Expiry Alerts\n\nAvoid expired medicines")

with c3:
    st.warning("ℹ️ Medicine Awareness\n\nKnow what you consume")
