import streamlit as st
from streamlit_card import card

def main():
    st.header("Projects Done")
    st.write("Here are some of the projects done")

    st.subheader("Data Science Projects")

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            title="Goat Analysis",
            text="Ronaldo and Messi G/A",
            image="db7.png",
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                },
                "title": {
                    "font-size": "24px",
                    "font-weight": "bold",
                    "color": "#ffffff"
                }
            },
            url="https://footballgoatanalysis.streamlit.app/"
        )
    with col2:
        card(
            title="2024 Spotify Analysis",
            text="Most streamed songs 2024",
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                },
                "title": {
                    "font-size": "24px",
                    "font-weight": "bold",
                    "color": "#ffffff"
                }
            },
            url="https://footballgoatanalysis.streamlit.app/"
        )
    with col3:
        card(
            title="Bikes Analysis",
            text="Analysis on bike models",
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                },
                "title": {
                    "font-size": "24px",
                    "font-weight": "bold",
                    "color": "#ffffff"
                }
            },
            url="https://footballgoatanalysis.streamlit.app/"
        )

    st.subheader("Web Development Projects")
    cola, colb, colc = st.columns(3)

    with cola:
        card(
            title="My Portfolio",
            text="My website",
            image="db7.png",
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                },
                "title": {
                    "font-size": "24px",
                    "font-weight": "bold",
                    "color": "#ffffff"
                }
            },
            url="https://footballgoatanalysis.streamlit.app/"
        )
    with colb:
        card(
            title="Skyline DT Training Portal",
            text="A portal for Skyline Sacco for onboarding new staff",
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                },
                "title": {
                    "font-size": "24px",
                    "font-weight": "bold",
                    "color": "#ffffff"
                }
            },
            url="https://footballgoatanalysis.streamlit.app/"
        )
    with colc:
        card(
            title="Wema Salon Site",
            text="A booking site for Wema Salon",
            styles={
                "card": {
                    "width": "100%",
                    "height": "150px",
                },
                "title": {
                    "font-size": "24px",
                    "font-weight": "bold",
                    "color": "#ffffff"
                }
            },
            url="https://footballgoatanalysis.streamlit.app/"
        )

if __name__ == "__main__":
    st.set_page_config(
        page_title="Projects",
        page_icon="📝",
        layout="wide",
    )
    main()
