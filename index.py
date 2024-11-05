import streamlit as st

def main():
    st.logo("ktm.jpg")

    dummy1, title_col, dummy2 = st.columns([2, 3, 2])
    with title_col:
        st.header("Vincent Matu ")
        st.caption("Software Developer| Data Scientist | Data Engineer")

    col1, col2 = st.columns(2)

    with col1:
        st.write("My name is Vincent Matu. I am a Software Developer and Data scientist by profession.")
        st.write("I studied at eMobilis Technical institute where they make you the best version of yourself.")
        st.write("In this life everything you do is a wager of what will happen the day to follow.")

    with col2:
        dm1, ac_col1, dm2=st.columns(3)
        with col2:
            st.image("ktm.jpg", width=(1000))

    st.subheader("Links")
    column1, column2 = st.columns(2)
    with column1:
        st.write("Github: https://github.com/")
        st.write("LinkedIn: https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit")
        st.write("IG: https://www.instagram.com/")
    with column2:
        st.write("X: https://x.com/?lang=en&mx=2 ")
        st.write("Email: https://mail.google.com/mail/u/0/#inbox ")




if __name__ == "__main__":
    st.set_page_config(
        page_title="Vincent's Portfolio",
        page_icon= "📝",
        layout= "wide",
        initial_sidebar_state= "expanded"
    )
    main()