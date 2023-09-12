import streamlit as st
import plotly.express as px
import pandas as pd
import folium
import pandas as pd
from plotly.graph_objs.layout import Grid
from streamlit_folium import folium_static
import matplotlib as plt
import plotly.graph_objs as go

st.set_page_config(page_title="Dashboard_2!!!", layout="wide")


st.title("Attribution Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


df = pd.read_csv('final_result.csv')
    #df['date'] = pd.to_datetime(df['start_date'])


#st.dataframe(df)


st.sidebar.header("Choose your filter: ")
zone = st.sidebar.multiselect("Pick your zone", df["Zone"].unique())
if not zone:
    df2 = df.copy()
else:
    df2 = df[df["Zone"].isin(zone)]

month = st.sidebar.multiselect("Pick your month", df["Month"].unique())
if not month:
    df2 = df.copy()
else:
    df2 = df[df["Month"].isin(month)]

Product_ID = st.sidebar.multiselect("Pick your Product_ID", df["Product_ID"].unique())
if not Product_ID:
    df2 = df.copy()
else:
    df2 = df[df["Product_ID"].isin(Product_ID)]

df1 = df2.query('Zone == @zone & Month == @month & Product_ID == @Product_ID')



st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #EEEEEE;
   border: 1px solid #CCCCCC;
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
   box-shadow: 4px 4px 0px rgba(0.3, 0.4, 0.5, 0.1);

}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: Black;
}
</style>
"""
            , unsafe_allow_html=True)

st.markdown(
    """
<style>
.stButton>button {
    border-radius: 0%;
    padding-top: 1px ;
padding-bottom: 1px;
color: #1D2364;
border:border:#000000;
border-radius:0px; 
border: 2px solid #1D2364;
    width: 90%


}
</style>
""",
    unsafe_allow_html=True,
)



col1, col2= st.columns([4,1])


df1['positive'] = (df1['Coef']>=0)
fig3 = px.bar(df1, x="Variable", y="Coef", labels={"Sales": "Amount"}, height=500, width=1000,
              template="gridon",color="positive",
              color_discrete_map={
                  True: 'green',
                  False: 'red'
              }
              )


fig3.update_layout(
    plot_bgcolor='white',
    title="Promo Feature Analysis", title_x=0.35,
    showlegend=False
)
#fig3.update(fig3, showlegend="false")

with col1:
    st.plotly_chart(fig3, use_container_width=True)




df["R2 Score"] = pd.to_numeric(df["R2 Score"], downcast="float")

#df['Adj R2 Score'].apply(lambda x: float(x))

#df1['Adj R2 Score'] = df1['Adj R2 Score'].round().astype('Int64')

Model_Accuracy =df1['R2 Score'].mean()
#Avg_promo_discount = float(filtered_df['cash_discount_per_case_off_invoice'].mean())

from numerize.numerize import numerize


with col2:
    with st.container():
        st.metric(label='Model Accuracy (in %)', value=round((Model_Accuracy)*100,4))



#fig = px.bar(data_canada, x='year', y='pop')

