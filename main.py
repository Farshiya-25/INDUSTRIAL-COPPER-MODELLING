import pandas as pd
import streamlit as st
import pickle

df = pd.read_csv(r"C:\Users\Abdul\Downloads\Copper_Set.xlsx - Result 1.csv")


st.set_page_config(layout="wide")
st.header(":blue[INDUSTRIAL COPPER MODELLING]", divider="violet")

page1,page2 = st.tabs([":violet[Predict selling price]",":violet[Predict status]"])

with page1:
    col1,col2,col3 = st.columns([5,2,5])


    with col1:
        st.write(' ')
        status = st.selectbox("select status as Won=1 and Lost=0",options=[0,1],key="status1")
        item_type = st.selectbox("select item type",df['item type'].unique(),key="item_type1")
        country = st.selectbox("select country",df['country'].unique(),key="country1")
        application = st.selectbox("select application",df['application'].unique(),key="application1")
        product_ref = st.selectbox("select product reference",df['product_ref'].unique(),key="product_ref1")
        if item_type == "W":
            w=1
            wi=0
            s=0
            others=0
            pl=0
            ipl=0
            slawr=0
        elif item_type == "WI":
            w=0
            wi=1
            s=0
            others=0
            pl=0
            ipl=0
            slawr=0
        elif item_type == "S":
            w=0
            wi=0
            s=1
            others=0
            pl=0
            ipl=0
            slawr=0
        elif item_type == "Others":
            w=0
            wi=0
            s=0
            others=1
            pl=0
            ipl=0
            slawr=0
        elif item_type == "PL":
            w=0
            wi=0
            s=0
            others=0
            pl=1
            ipl=0
            slawr=0
        elif item_type == "IPL":
            w=0
            wi=0
            s=0
            others=0
            pl=0
            ipl=1
            slawr=0
        elif item_type == "SLAWR":
            w=0
            wi=0
            s=0
            others=0
            pl=0
            ipl=0
            slawr=1


    with col3:
        st.write(' ')
        quantity_tons = st.number_input("Enter quantity tons (min:0.00001 & max:1000000.00)",key="quantity_tons1")
        thickness = st.number_input("Enter thickness (min:0.18 & max:2500.0)",key="thickness1")
        width = st.number_input("Enter width (min:1.0 & max:2990.0)",key="width1")
        customer = st.number_input("Enter customer (min:12458.0 & max:2147483647.0)",key="customer1")



    submitted = st.button("Predict Price",key="predict_button1")

      
    if submitted:
        my_input = [status,country,application,product_ref,
                    quantity_tons,thickness,width,customer,w,wi,s,others,pl,ipl,slawr]  
        
        with open("Pricepredicting1.pkl","rb") as ft:
            loaded_model = pickle.load(ft)
        
        output = loaded_model.predict([my_input])
        st.write("Predicted price is:",output[0])


with page2:
    col1,col2,col3 = st.columns([5,2,5])


    with col1:
        st.write(' ')
        item_type = st.selectbox("select item type",df['item type'].unique(),key="item_type2")
        country = st.selectbox("select country",df['country'].unique(),key="country2")
        application = st.selectbox("select application",df['application'].unique(),key="application2")
        product_ref = st.selectbox("select product reference",df['product_ref'].unique(),key="product_ref2")
        if item_type == "W":
            w=1
            wi=0
            s=0
            others=0
            pl=0
            ipl=0
            slawr=0
        elif item_type == "WI":
            w=0
            wi=1
            s=0
            others=0
            pl=0
            ipl=0
            slawr=0
        elif item_type == "S":
            w=0
            wi=0
            s=1
            others=0
            pl=0
            ipl=0
            slawr=0
        elif item_type == "Others":
            w=0
            wi=0
            s=0
            others=1
            pl=0
            ipl=0
            slawr=0
        elif item_type == "PL":
            w=0
            wi=0
            s=0
            others=0
            pl=1
            ipl=0
            slawr=0
        elif item_type == "IPL":
            w=0
            wi=0
            s=0
            others=0
            pl=0
            ipl=1
            slawr=0
        elif item_type == "SLAWR":
            w=0
            wi=0
            s=0
            others=0
            pl=0
            ipl=0
            slawr=1


    with col3:
        st.write(' ')
        quantity_tons = st.number_input("Enter quantity tons (min:0.00001 & max:1000000.00)",key="quantity_tons2")
        thickness = st.number_input("Enter thickness (min:0.18 & max:2500.0)",key="thickness2")
        width = st.number_input("Enter width (min:1.0 & max:2990.0)",key="width2")
        customer = st.number_input("Enter customer (min:12458.0 & max:2147483647.0)",key="customer2")
        selling_price = st.number_input("Enter selling price (min:1.0 & max:100001015)",key="selling_price2")



    submitted = st.button("Predict Status",key="predict_button2")

      
    if submitted:
        my_input = [country,application,product_ref,
                    quantity_tons,thickness,width,customer,selling_price,w,wi,s,others,pl,ipl,slawr]  
        
        with open("Statuspredicting1.pkl","rb") as ft:
            loaded_model = pickle.load(ft)
        
        output = loaded_model.predict([my_input])
        if output[0] == 1:
            st.write("Predicted status : WON")
        else:
            st.write("Predicted status : LOST")




