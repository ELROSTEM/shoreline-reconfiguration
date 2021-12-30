from typing import Container

import leafmap.kepler as leafmap
import streamlit as st
from streamlit.state.session_state import SessionStateStatProvider


def increment_counter():
    st.session_state.page += 1
def decrement_counter():
    st.session_state.page -= 1


def app():
    st.title("Story Board")

    #Page monitoring
    if 'page' not in st.session_state:
        st.session_state.page = 0
    if st.session_state.page == -1:
        st.session_state.page = 2
    elif st.session_state.page == 3:
        st.session_state.page = 0

    #----------------------------------------------------------
    #Page zero
    if st.session_state.page == 0:
        page_0 = st.container()
        with page_0:
            
            st.header("Sea Level Rise in NYC")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                    In the last decade, the speed at which New York’s sea level is rising has increased and is now rising by as much as 1 inch every 7-8 years.1 Around Battery Park, it took the sea level 48 years to rise by 6 inches.1 Scientists forecast that in just the next 14 years, the sea level will have risen by another 6 inches.8

                    Scientists are not certain how fast the ocean will warm and ice will melt. They expect water levels to continue to rise faster, but are not sure just how fast. Therefore scientists from the National Oceanic and Atmospheric Administration (NOAA) and the US Army Corps of Engineers (USACE) have made predictions based on ranges from low to high.

                    Below you can see the range of the NOAA and USACE high and intermediate forecasts for various locations around New York.9 Currently, the USACE high forecast, seen as the darkest red line, is the most likely projection.

                    NOTE* This is copied the image is also copies
                """)
            with col2:
                st.image('https://assets.sealevelrise.org/2018/10/315b03518bdc8ad603b0ef7919ed2b5f-SLR-speeding-up-New-York-English.png')

            st.subheader("So what does it look like?")


            map_data = 'https://data.cityofnewyork.us/resource/myk6-g6eq.GeoJSON'
            #Width for leafmap kepler has a problem because there is not if statement for width lets gooo we can implement this create pull request gogogo first open source
            #Kepler gl should download itsself when keplergl leafmap is imported

            # leafmap.update_package()
            map = leafmap.Map(center=[40.7, -74], height=600, zoom=11,
                max_zoom=16,
                pitch=45,
                bearing=0)
            map.add_geojson(map_data, layer_name="sea-level-rise")
            map.to_streamlit(800, 600)

            



    #----------------------------------------------------------
    #Page one
    elif st.session_state.page == 1:
        page_1 = st.container()
        with page_1:

            st.header("Structures For Sea Level Rise")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""Shore consolidation works: They are made on the beach to resist direct wave actions. It's important to avoid erosion in their foundation area or in the front beach. Not an popular choice since it hinder natural aspect of the beaches and the tourist use.
                Transverse works: To stop the transport of sediments along the beach, which implies the development of upstream accumulation and erosion on their downstream sides.
                Longitudinal works: They interferes the wave propagation by intercepting the incident energy flow. Part of this energy is distributed widely, a portion is dissipated in the mass of the building, the rest of the energy is transmitted through/over the dikes.
                Example works:""")
            with col2:
                st.image("https://blogger.googleusercontent.com/img/a/AVvXsEghrCZBwvvTKyS8dHGW1zgkSfK9nv7BfRsq9qBWdUbo5xk_-dG0Pn2Mbeu0jsnmZpNrDMXNhp4g9h7lun3ti1QyDzSVAZdtT-WraYBWp9CrUxBjC2nKHuk2ZFAIvMcsOeWcUG75KqE3ricav9-cfAb1h89wF6RQnvRRzj2YaqS1kCocBLqw2Q-fxiboqQ=s350")
                st.caption("Sea dikes are onshore structures with the principal function of protecting low-lying areas against flooding. Sea dikes are usually built as a mound of fine materials like sand and clay with a gentle seaward slope in order to reduce the wave runup and the erodible effect of the waves. The surface of the dike is armored with grass, asphalt, stones, or concrete slabs (USACE, 2005).")
    #----------------------------------------------------------
    #Page two
    elif st.session_state.page == 2:
        page_2 = st.container()
        with page_2:
            st.title("This is the third page")

    but1, but2 = st.columns(2)
    but1.button('<- Previous Page', on_click=decrement_counter)
    but2.button('Next Page ->', on_click=increment_counter)




