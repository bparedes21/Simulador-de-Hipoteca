import streamlit as st
import pandas as pd
import requests
from calc_hipoteca import * 

st.set_page_config(
    page_title="Calcular interes: ",
    page_icon="✅",
    layout="wide",
)
#https://www.eluniverso.com/noticias/2020/03/01/nota/7761018/tasas-interes-ecuador-vivienda/
st.markdown('<h1  div style="text-align: center;">Simulador de cuota de hipoteca</div>', unsafe_allow_html=True)
st.markdown("<h4  div style='text-align: center;background-color: white;color:black;'>"+"Sistema de amortización francés"+"</div>", unsafe_allow_html=True)
#st.title('Simulador de cuota de hipoteca')
st.markdown("<h5  div style='text-align: left;background-color: white;color:black;'>"+"1 -Seleccionar el número de cuotas (meses)? que desea aplicar y el interes (anual)"+"</div>", unsafe_allow_html=True)
#st.title('Simulador de cuota de hipoteca')

option = st.selectbox(
    '',
    ('Ninguna','120 meses (10 años) con un 15 % anual','180 meses (15 años) con un 13 % anual','240 meses (20 años) con un 10 % anual'))


if(option=='Ninguna'):
    st.write(':red[Selecciona el numero de cuotas]') 
    st.markdown("<h3  div style='text-align: left;background-color: grey;color:white;'>"+"Monto a solicitar"+"</div>", unsafe_allow_html=True)
    st.markdown("<h3  div style='text-align: center;background-color: black;color:white;'>"+"$..."+"</div>", unsafe_allow_html=True)

else:
    st.markdown("<h5  div style='text-align: left;background-color: white;color:green;'>"+"Seleccionaste: "+option+" de interes."+"</div>", unsafe_allow_html=True)
    st.markdown("<h5  div style='text-align: left;background-color: white;color:black;'>"+"2 -Seleccionar tipo de periodo"+"</div>", unsafe_allow_html=True)
    
    option1= st.selectbox(
    '',
    ('Mensual','Bimestral','Trimestral','Cuatrimestral','Semestral'))
    st.markdown("<h5  div style='text-align: left;background-color: white;color:green;'>"+"Seleccionaste tipo de periodo de pago: "+option1+" "+"</div>", unsafe_allow_html=True)

if(option!='Ninguna'):
    col1, col2 = st.columns([2, 1])
    col3, col4, col5 = st.columns([1,1,1])
    with col1:

        
        number = st.number_input('Insert a number')
        monto_hipoteca_moneda=float(number)
       
        monto_hipoteca_moneda_str='{:,.0f}'.format(monto_hipoteca_moneda)
        monto_hipoteca_moneda_strreplace=formato_miles(monto_hipoteca_moneda_str)
        
        st.markdown("<h2  div style='text-align: center;background-color: black;color:white;'>"+"$"+monto_hipoteca_moneda_strreplace+"</div>", unsafe_allow_html=True)
        st.markdown("<h5  div style='text-align: left;background-color: white;color:black;'>"+"- Presione para ver la tabla"+"</div>", unsafe_allow_html=True)
        
        df_hipoteca,sum_Cuota_fija,CUOTA_F=Calcular_hipoteca_amortizacion_metodo_frances(option,option1,monto_hipoteca_moneda)
        agree = st.checkbox('') 
        #mostrar tabla
        if agree:
            st.table(df_hipoteca) 

    with col2:  
    
        valor_inmueble=(monto_hipoteca_moneda*100)/80
        valor_inmueble_str='{:,.0f}'.format(valor_inmueble)
        
        valor_inmueble_strreplace = formato_miles(valor_inmueble_str)
        

      
        no_financiado=valor_inmueble-monto_hipoteca_moneda
        no_financiado_str='{:,.0f}'.format(no_financiado)
       
        no_financiado_strreplace=formato_miles(no_financiado_str)
        
        sum_Cuota_fija_str='{:.0f}'.format(sum_Cuota_fija)
        Sum_num_float_strreplace=formato_miles(str(sum_Cuota_fija_str))

        CUOTA_F_STR='{:.0f}'.format(CUOTA_F)
        CUOTA_F_STR_FLOAT=formato_miles(CUOTA_F_STR)
        

        st.markdown("<h4  div style='text-align: center;background-color: white;color:black;'>"+"Resumen del crédito: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"VALOR DEL INMUEBLE: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"&#127971;100% &#128175;$"+valor_inmueble_strreplace+"</div>", unsafe_allow_html=True)

        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"MONTO DEL CRÉDITO: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"&#128186;80% &#128394;$"+monto_hipoteca_moneda_strreplace+"</div>", unsafe_allow_html=True)

        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"MONTO NO FINANCIADO: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"&#128092; 20% &#128176;$"+no_financiado_strreplace+"</div>", unsafe_allow_html=True)

        
        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"TERMINAS PAGANDO: "+"</div>", unsafe_allow_html=True)
        
        
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"$ "+Sum_num_float_strreplace+"</div>", unsafe_allow_html=True)
        
        st.markdown("<h5  div style='text-align: left;background-color: GreenYellow;color:black;'>"+"VALOR DE LA CUOTA: "+"</div>", unsafe_allow_html=True)
        st.markdown("<h2  div style='text-align: center;background-color: Cyan	;color:black;'>"+"$ "+CUOTA_F_STR_FLOAT+"</div>", unsafe_allow_html=True)

        