import streamlit as st

def main():
    st.logo("logo.png")
    st.header("About Me")
    col1, col2 = st.columns(2)
    with col1:

        user_choice = st.selectbox("Click what you want to view", ["Education", "Certifications", "Skills", "Experience"])
        if user_choice == "Education":
            st.write("1.Emobilis Technology Training Institute")
            st.write("Course: Data Science")
            st.write("Duration : September 2024 - December 2024")
            st.divider()
            st.write("2. Zetech University")
            st.write("Course: BSc Information Technology")
            st.write("Duration: Sep 2020 - Nov 2024")

        elif user_choice == "Certifications":
            st.write("1.Huawei Talent Academy")
            st.write("Internet of Things (IoT)")
            st.divider()
            st.write("2: Cisco")
            st.write("Big Data Analytics")
            st.divider()
            st.write("3: Cisco")
            st.write("Certified Cisco Network Associate")
        elif user_choice == "Skills":
            st.write("1: Software development")
            st.write("2: Data analytics")
            st.write("3: Database administration")
            st.write("4: Web development")
        elif user_choice == "Experience":
            st.write("1: Skyline DT Sacco")
            st.write("Title: Attache")
            st.divider()
            st.write("2: Merino real estate")
            st.write("Title: Attache")

    with col2:
        st.subheader("Contact Me")
        fname = st.text_input("Enter your first name")
        lname = st.text_input("Enter your last name")
        email = st.text_input("Enter your email")
        msg = st.text_area("Enter message")
        if st.button("Submit"):
            st.toast("Form submitted")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Karori Portfolio",
        page_icon="📝",
        layout="wide",
    )
    main()
