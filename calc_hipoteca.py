import pandas as pd
"""
def Calcular_hipoteca(option,monto_hipoteca_moneda):
    #C= V / (1-(1/(1+i))^N)/i)
    lista_Interes_periodo=[]
    lista_total_faltante=[]
    lista_cuota_sin_interes=[]
    lista_cuota_con_interes=[]

    if(option=='120 meses (10 años) con un 15 % anual'):
        #numero_de_cuotas_list=range[1,120]
        interes_hipoteca_anual=15
        
        numero_de_cuotas_list=list(range(1,120))
        #numero_de_cuotas_list=range[1,120]
        interes_hipoteca_anual=15
        cuotas_mensuales=120
        numero_de_cuotas_list=list(range(1,cuotas_mensuales+1))

        #calculo periodo
        interes_hipoteca_mensual=interes_hipoteca_anual/12
        #print("interes_hipoteca_mensual",interes_hipoteca_mensual)

        dividendo=(((((interes_hipoteca_mensual)/100)+1)**cuotas_mensuales))*((interes_hipoteca_mensual)/100)
        divisor=((((interes_hipoteca_mensual)/100)+1)**cuotas_mensuales)-1
        resultado_dividendo=dividendo/divisor
            
        periodo=(monto_hipoteca_moneda*resultado_dividendo)
        #print("Periodo",periodo)
        total_credito=(periodo*cuotas_mensuales)
        #print("total credito",total_credito)
        intereses_a_pagar=(total_credito-monto_hipoteca_moneda)
        interes_mensual=(intereses_a_pagar/cuotas_mensuales)
        #print("interes_mensual",interes_mensual)
        cuota_sin_interes=(periodo-interes_mensual)
        #print("cuota sin interes",cuota_sin_interes)

        interes_mensual_redondeo=round(interes_mensual,2)
        #calculo interes
        #Interes_periodo=periodo*tanto_por_ciento
        #cuota_sin_interes=periodo-Interes_periodo
        #st.write(':green[periodo:]', periodo)
        #st.write(':green[Interes_periodo:]', Interes_periodo)
        #st.write(':green[cuota_sin_interes:]', cuota_sin_interes)
        #print("n de cuotas",len(numero_de_cuotas_list))
        interes_acumulado=[interes_mensual*i for i in numero_de_cuotas_list]
        cuotas_acumuladas=[cuota_sin_interes*i for i in numero_de_cuotas_list]
        
        #print("n de interes_acumulado",sum(interes_acumulado))
        list_resta_monto=[round((monto_hipoteca_moneda-i),2) for i in cuotas_acumuladas]

        #st.write(':green[periodo:]', periodo)
        #st.write(':green[Interes_periodo:]', Interes_periodo)
        #st.write(':green[cuota_sin_interes:]', cuota_sin_interes)
        #calculo_interes
        lista_Interes_periodo = [interes_mensual_redondeo] * cuotas_mensuales
        
        cuota_sin_interes_redondeo=round(cuota_sin_interes,2)
        lista_cuota_sin_interes=[cuota_sin_interes_redondeo]*cuotas_mensuales

        cuota_con_interes_redondeo=round(periodo,2)
        lista_cuota_con_interes=[cuota_con_interes_redondeo]*cuotas_mensuales    
        lista_total_faltante=-cuota_sin_interes_redondeo
        cuotas_acumuladas_redondeo = [round(num,2) for num in cuotas_acumuladas]
        cuotas_acumuladas_redondeo_reversed=reversed(cuotas_acumuladas_redondeo)

        interes_acumulado_redondeo = [round(num,2) for num in interes_acumulado]
        interes_acumulado_redondeo_reversed=reversed(interes_acumulado_redondeo)
        columnas =["Mes","Cuota ($)","Amortización ($)","Intereses ($)","Saldo_a_pagar"]
        df_hipoteca=pd.DataFrame(list(zip(numero_de_cuotas_list,lista_cuota_con_interes,cuotas_acumuladas_redondeo_reversed,interes_acumulado_redondeo_reversed,list_resta_monto)),columns=columnas)
        return df_hipoteca   
"""
def Calcular_hipoteca_amortizacion_metodo_frances(option,monto_hipoteca_moneda):
    #C= V / (1-(1/(1+i))^N)/i)
    lista_Interes_periodo=[]
    lista_total_faltante=[]
    lista_cuota_sin_interes=[]
    lista_cuota_con_interes=[]
    if(option=='120 meses (10 años) con un 15 % anual'):
        #numero_de_cuotas_list=range[1,120]
        
        numero_de_cuotas_list=list(range(1,120))
        #numero_de_cuotas_list=range[1,120]
        interes_hipoteca_anual=15
        cuotas_mensuales=120

    elif(option=='180 meses (15 años) con un 13 % anual'):
        #numero_de_cuotas_list=range[1,180]
        numero_de_cuotas_list=list(range(1,180))
        interes_hipoteca_anual=13
    
        cuotas_mensuales=180

    else:
        numero_de_cuotas_list=list(range(1,240))
        interes_hipoteca_anual=10
        cuotas_mensuales=240

    numero_de_cuotas_list=list(range(1,cuotas_mensuales+1))
    total_credito=monto_hipoteca_moneda
    interes_hipoteca_mensual=interes_hipoteca_anual/12
    
    cuota_a_amortizar=total_credito/cuotas_mensuales
    lista_cuota_sin_interes=[cuota_a_amortizar]*cuotas_mensuales

    for i in numero_de_cuotas_list:

        #calculo periodo
        
        #print("interes_hipoteca_mensual",interes_hipoteca_mensual)
            
        interes_mensual=(total_credito*interes_hipoteca_mensual)/100
        lista_Interes_periodo.append(round(interes_mensual,2))
        print("Periodo interes",interes_mensual)
        
        total_credito=(total_credito-cuota_a_amortizar)
        lista_total_faltante.append(round(total_credito,2))
        print("total credito",total_credito)
    
        cuota_con_interes=(cuota_a_amortizar+interes_mensual)
        lista_cuota_con_interes.append(round(cuota_con_interes,2))
        
    columnas =["Mes","Cuota ($)","Amortización ($)","Intereses ($)","Saldo_a_pagar"]
    df_hipoteca=pd.DataFrame(list(zip(numero_de_cuotas_list,lista_cuota_con_interes,lista_cuota_sin_interes, lista_Interes_periodo,lista_total_faltante)),columns=columnas)
    return df_hipoteca 