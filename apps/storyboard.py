
import streamlit as st


def increment_counter():
    st.session_state.count += 1
def decrement_counter():
    st.session_state.count -= 1


def app():
    st.title("Ryan Is So Cool")

    if 'count' not in st.session_state:
        st.session_state.count = 0

    if st.session_state.count == 0:
        col1, col2 = st.columns(2)

        with col1:
            st.header("Sea Dikes cool cool")
            st.write("""Shore consolidation works: They are made on the beach to resist direct wave actions. It's important to avoid erosion in their foundation area or in the front beach. Not an popular choice since it hinder natural aspect of the beaches and the tourist use.
            Transverse works: To stop the transport of sediments along the beach, which implies the development of upstream accumulation and erosion on their downstream sides.
            Longitudinal works: They interferes the wave propagation by intercepting the incident energy flow. Part of this energy is distributed widely, a portion is dissipated in the mass of the building, the rest of the energy is transmitted through/over the dikes.
            Example works:""")
        with col2:
            st.image("https://blogger.googleusercontent.com/img/a/AVvXsEghrCZBwvvTKyS8dHGW1zgkSfK9nv7BfRsq9qBWdUbo5xk_-dG0Pn2Mbeu0jsnmZpNrDMXNhp4g9h7lun3ti1QyDzSVAZdtT-WraYBWp9CrUxBjC2nKHuk2ZFAIvMcsOeWcUG75KqE3ricav9-cfAb1h89wF6RQnvRRzj2YaqS1kCocBLqw2Q-fxiboqQ=s350")
            st.write("Sea dikes are onshore structures with the principal function of protecting low-lying areas against flooding. Sea dikes are usually built as a mound of fine materials like sand and clay with a gentle seaward slope in order to reduce the wave runup and the erodible effect of the waves. The surface of the dike is armored with grass, asphalt, stones, or concrete slabs (USACE, 2005).")
    elif st.session_state.count == 1:
        col1, col2 = st.columns(2)

        with col1:
            st.header("Ryan cool")
            st.write("""this new page wow so cool very cool acutally this should be written differently in code it should have like diff app files and stuff but it works. Everything I build is 90 percent broken anyways""")
        with col2:
            st.image("https://blogger.googleusercontent.com/img/a/AVvXsEiUXAsj6siTp_sUd4PcqaNwtT3GTwtXAqo8Ab_71hig_aiUD0CplmAffB43oXdg-2cqNkhUenAXgzogDtxR0eAC4sHfq2oPImNvK6wIbfJJZZx9fKxTAwIvb5f9oAGhdjkKqYntegtn0HzBBn39wmUkS6aqGXaLPSLWDqmDPnIDQ_bno00dlPQBdQHmaQ=s773")
            st.write("look at this water thing its like so cool")
    else:
        st.title("Sorry site broken I thought 2 pages would be enough too lazy ik")


    but1, but2 = st.columns(2)
    but1.button('Previous Page', on_click=decrement_counter)
    but2.button('Next Page', on_click=increment_counter)

