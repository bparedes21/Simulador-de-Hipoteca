import streamlit as st
import pandas as pd
import requests
from calc_hipoteca import * 

st.set_page_config(
    page_title="Calcular interes: ",
    page_icon="✅",
    layout="wide",
)
#with st.sidebar: https://www.helpmycash.com/hipotecas/calcular-hipoteca/
#https://www.bancoprovincia.com.ar/hipotecarioTradicional/micro_simulador
st.markdown('<h1  div style="text-align: center;">Simulador de cuota de hipoteca</div>', unsafe_allow_html=True)
#st.title('Simulador de cuota de hipoteca')
option = st.selectbox(
    'Cual es el número de cuotas (meses)? que desea aplicar y el interes (anual)',
    ('Ninguna','120 meses (10 años) con un 15 % anual','180 meses (15 años) con un 13 % anual','240 meses (20 años) con un 10 % anual'))


if(option=='Ninguna'):
    st.write(':red[Selecciona el numero de cuotas]') 
    st.markdown("<h3  div style='text-align: left;background-color: grey;color:white;'>"+"Monto a solicitar"+"</div>", unsafe_allow_html=True)
    st.markdown("<h3  div style='text-align: center;background-color: black;color:white;'>"+"$..."+"</div>", unsafe_allow_html=True)

else:
    st.write(':green[Seleccionaste:]', option)

if(option!='Ninguna'):
    col1, col2 = st.columns([2, 1])
    col3, col4, col5 = st.columns([1,1,1])
    with col1:
        st.markdown('<h3  div style="text-align: center;background-color: grey;color:white;">Monto a solicitar:</div>', unsafe_allow_html=True)
        
        #col1.subheader("Monto a solicitar")
        monto_hipoteca = st.slider('Cual va a ser el monto de la hipoteca?',1000,  24850000, 1000)
        monto_hipoteca_moneda=float(monto_hipoteca)
        st.write(':green[monto_hipoteca_moneda:]', monto_hipoteca_moneda)

        monto_hipoteca_moneda_str='{:,.0f}'.format(monto_hipoteca)
        st.markdown("<h2  div style='text-align: center;background-color: black;color:white;'>"+"$"+monto_hipoteca_moneda_str+"</div>", unsafe_allow_html=True)
        
        
        
       
        agree = st.checkbox('Presione para ver la tabla')

        if agree:
            df_hipoteca=Calcular_hipoteca_amortizacion_metodo_frances(option,monto_hipoteca_moneda)
            st.table(df_hipoteca) 
            
    with col2:  
            #col2.subheader(":green[$ ]"+ monto_hipoteca_moneda)

        valor_inmueble=(monto_hipoteca_moneda*100)/80
        valor_inmueble_str='{:,.0f}'.format(valor_inmueble)

        no_financiado=valor_inmueble-monto_hipoteca_moneda
        no_financiado_str='{:,.0f}'.format(no_financiado)
        st.markdown("<h4  div style='text-align: center;background-color: white;color:black;'>"+"Resumen del crédito: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"VALOR DEL INMUEBLE: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"&#127971;100% &#128175;$"+valor_inmueble_str+"</div>", unsafe_allow_html=True)

        
        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"MONTO DEL CRÉDITO: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"&#128186;80% &#128394;$"+monto_hipoteca_moneda_str+"</div>", unsafe_allow_html=True)

        
        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"MONTO NO FINANCIADO: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"&#128092; 20% &#128176;$"+no_financiado_str+"</div>", unsafe_allow_html=True)

        #st.header(":green[$ ]",monto_hipoteca_moneda)
        
        