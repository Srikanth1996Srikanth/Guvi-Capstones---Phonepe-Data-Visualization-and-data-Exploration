import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector as conn
import plotly.express as px
import plotly.graph_objects as go


# opening mysql using create engine module
# mydb = create_engine("mysql+mysqlconnector://root:<password>@127.0.0.1:3306/pulse")

conn = sql.connect(host="127.0.0.1",
                   user="root",
                   password="9965543275@Sri",
                   database= "Phonepe",
                   port = "3306"
                  )

# cursor = mysql.connector.connect(**config)
cursor = conn.cursor()

# cursor.execute("Select * from aggregated_transaction WHERE State='Tamilnadu'")
# rows = cursor.fetchall()
# for i in rows:
#     print(i)

st.set_page_config(page_title='Phonepe Pulse', page_icon = 'phonepe.jpg', layout='wide')
st.title(':violet[PhonePe Pulse Data Visualization]')

head1,head2=st.columns([0.18,3])
with head1:
    image = Image.open('phonepe.jpg')
    st.image(image, width=60)
with head2:
    tit1,tit2=st.columns([0.456,2])
    with tit1:
        st.markdown("<h2 style= 'color: #9932CC;font-size: 34px;'>PhonePe Pulse  </h2>", unsafe_allow_html=True)
    # with tit2:
        # st.markdown("<h2 style= 'color: #9932CC;font-weight: normal;font-size: 34px;'>The Best of Progress</h2>", unsafe_allow_html=True)
# st.write('')
# st.write('')
# left,optioncontainer,right=st.columns([0.2,3,0.2])

selected=option_menu(menu_title='', options=['Home','Map','Insights'],icons=['house','globe2','graph-up-arrow'],orientation='horizontal',styles={
            "container": {"padding": "0!important", "background-color": "white","size":"cover"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#391C59"},
            "nav-link-selected": {"background-color": "#691592"}  })
st.write('')
# st.write('')
# st.write('')

if selected == 'Home':
    col1,col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=c_1H6vivsiA")
        st.download_button(label="Download PhonePe App!",
                       data="https://www.phonepe.com/app-download/")

        st.title('GitHub')
        st.write('')
        st.write('A home for the data that powers the PhonePe Pulse website.')
        st.write('')
        url = 'https://github.com/PhonePe/pulse#readme'

        if st.button('GitHub'):
            webbrowser.open_new_tab(url)

    with col2:
        st.write(
        "The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.")

        st.write(
        "When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?"
        "This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.")

        st.write(
        "This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.")

        st.write(
        "PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.")

        st.title('Data APIs')
        # st.write('')
        st.write("""
            This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.
            """)
        # st.write('')
        aggcol, mapcol, topcol = st.columns([2.1, 1.4, 1.3])
        with aggcol:
            st.subheader('Aggregated')
            # st.write('')
            st.write('Aggregated values of various payment categories as shown under Categories section')
            # st.write('')
        with mapcol:
            st.subheader('Map')
            # st.write('')
            st.write('Total values at the State and District levels')
            # st.write('')
        with topcol:
            st.subheader('Top')
            # st.write('')
            st.write('Totals of top States / Districts / Pin Codes')
            # st.write('')


if selected=='Map':
    col1, col2 = st.columns([1, 1])
    with col1:
        optcol,yearcol,qurcol,noncol=st.columns([0.5,0.2,0.2,0.1])
        with optcol:
            option=st.selectbox(label='Select Type',options=['Transaction','Users'])
        with yearcol:
            year=st.selectbox(label='Select Year',options=['2018','2019','2020','2021','2022'])
        with qurcol:
            quarter=st.selectbox(label='Select Quarter',options=['1','2','3','4'])
        with noncol:
            st.write('')
        if option=='Transaction':

            st.markdown("<h2 style= 'color: #05C3DE;font-weight: normal;font-size: 48px;'><b>Transaction Map</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepe_pulse.maptran where Year={} and Quarter={} '.format(year, quarter)
            cursor.execute(select)
            result = cursor.fetchall()
            maptranstate = []
            for i in (result):
                maptranstate.append(i[2:5])
            statenamelst=[]
            statecountlst=[]
            stateamountlst=[]
            for i in maptranstate:
                    statenamelst.append(i[0])
                    statecountlst.append(i[1])
                    stateamountlst.append(i[2])



            lat=[10.0001051,15.9240905,28.0937702,26.4073841,25.6440845,30.72984395,21.6637359,20.7181749499999,28.6517178,15.3004543,22.3850051,29,31.81676015,32.7185614,23.4559809,14.5203896,10.3528744,33.9456407,10.8132489,23.8143419,18.9068356,24.7208818,25.5379432,23.2146169,26.1630556,20.5431241,10.91564885,30.9293211,26.8105777,27.601029,10.9094334,17.8495919,23.7750823,27.1303344,30.0417376,22.9964948]
            log =[93.0000194,80.1863809,94.5921326,93.2551303,85.906508,76.7841456701605,81.8406351,70.9323834101063,77.2219388,74.0855134,71.745261,76,77.3493205196885,74.8580917,85.2557301,75.7223521,76.5120396,77.6568576,73.6804620941119,77.5340719,75.6741579,93.9229386,91.2999102,92.8687612,94.5884911,84.6897321,79.8069487984423,75.5004841,73.7684549,88.4541363868014,78.3665347,79.1151663,91.7025091,80.859666,79.089691,87.6855882]


            df = pd.DataFrame({'lat':lat,'lon':log, 'statenamelst': statenamelst,'count':statecountlst,'amount':stateamountlst})
            df['count'] = df['count'].astype('int64')
            df['amount'] = df['amount'].astype('int64')

            fig = px.scatter_geo(df,size='count',lat='lat',lon='lon',color='count',hover_name='statenamelst'
                                 ,hover_data=(['count','amount']),scope='asia',size_max=20,width=600,height=400,color_continuous_scale=["orange", "yellow", "red"])
            fig.update_geos(visible=False, resolution=50, scope="asia",
                showcountries=True, countrycolor="Black",
                showsubunits=True, subunitcolor="black",fitbounds='locations',showland=True,landcolor='rgb(153,50,204)')
            fig.update_layout(
                {'plot_bgcolor': 'rgb(34,13,56)', 'paper_bgcolor': 'rgb(34,13,56)',},margin={"r":0,"t":0,"l":0,"b":0},coloraxis_colorbar=dict(
                len=0.5,
                xanchor="right", x=0.97,
                yanchor='bottom', y=0.28,
                thickness=20,))
            fig.add_trace(go.Scattergeo(lon=df["lon"],
                                        lat=df["lat"],
                                        text=df["statenamelst"],
                                        textposition="middle center",
                                        mode='text',
                                        showlegend=False,opacity=0.6))
            fig.update_traces(marker=dict(symbol="octagon",
                                          line=dict(width=2.4,
                                                    color='black')),
                              selector=dict(mode='markers'))

            st.plotly_chart(fig)

        elif option=='Users':
            st.markdown("<h2 style= 'color: #C98BDB;font-weight: normal;font-size: 48px;'><b>Users Map</b></h2>",unsafe_allow_html=True)

            select = 'select * from phonepe_pulse.mapuser where Year={} and Quarter={} '.format(year, quarter)
            cursor.execute(select)
            result = cursor.fetchall()
            mapuserstate = []
            mapuserstatenamelst=[]
            mapuserregistelst=[]
            mapuserappopenlst=[]
            for i in (result):
                mapuserstate.append(i[2:5])
            for i in mapuserstate:
                mapuserstatenamelst.append(i[0])
                mapuserregistelst.append(i[1])
                mapuserappopenlst.append(i[2])

            lat = [10.0001051, 15.9240905, 28.0937702, 26.4073841, 25.6440845, 30.72984395, 21.6637359,
                   20.7181749499999, 28.6517178, 15.3004543, 22.3850051, 29, 31.81676015, 32.7185614, 23.4559809,
                   14.5203896, 10.3528744, 33.9456407, 10.8132489, 23.8143419, 18.9068356, 24.7208818, 25.5379432,
                   23.2146169, 26.1630556, 20.5431241, 10.91564885, 30.9293211, 26.8105777, 27.601029, 10.9094334,
                   17.8495919, 23.7750823, 27.1303344, 30.0417376, 22.9964948]
            log = [93.0000194, 80.1863809, 94.5921326, 93.2551303, 85.906508, 76.7841456701605, 81.8406351,
                   70.9323834101063, 77.2219388, 74.0855134, 71.745261, 76, 77.3493205196885, 74.8580917, 85.2557301,
                   75.7223521, 76.5120396, 77.6568576, 73.6804620941119, 77.5340719, 75.6741579, 93.9229386, 91.2999102,
                   92.8687612, 94.5884911, 84.6897321, 79.8069487984423, 75.5004841, 73.7684549, 88.4541363868014,
                   78.3665347, 79.1151663, 91.7025091, 80.859666, 79.089691, 87.6855882]

            df = pd.DataFrame({'lat': lat, 'lon': log, 'statenamelst': mapuserstatenamelst, 'registered': mapuserregistelst,'appopens':mapuserappopenlst})
            df['lat']=df['lat'].astype('float')
            df['lon'] = df['lon'].astype('float')
            df['registered'] = df['registered'].astype('int64')
            df['appopens']=df['appopens'].astype('int64')

            fig = px.scatter_geo(df, size='registered', lat='lat', lon='lon', color='registered', hover_name='statenamelst'
                                 ,hover_data=(['registered','appopens']),scope='asia', size_max=20, width=600, height=400,
                                 color_continuous_scale=["orange", "yellow", "red"],opacity=0.79)

            fig.update_geos(visible=False, resolution=50, scope="asia",
                            showcountries=True, countrycolor="white",
                            showsubunits=True, subunitcolor="white", fitbounds='locations', showland=True,
                            landcolor='rgb(153,50,204)')
            fig.update_layout(
                {'plot_bgcolor': 'rgb(34,13,56)', 'paper_bgcolor': 'rgb(34,13,56)', },
                margin={"r": 0, "t": 0, "l": 0, "b": 0},coloraxis_colorbar=dict(
                len=0.5,
                xanchor="right", x=0.97,
                yanchor='bottom', y=0.28,
                thickness=20,))
            fig.add_trace(go.Scattergeo(lon=df["lon"],
                                        lat=df["lat"],
                                        text=df["statenamelst"],
                                        textposition="middle center",
                                        mode='text',
                                        showlegend=False, opacity=0.6))

            fig.update_traces(marker=dict(symbol="octagon",
                                          line=dict(width=2.4,
                                                    color='Black')),
                              selector=dict(mode='markers'))

            st.plotly_chart(fig)
