import pandas as pd

def formato_miles(txt):
    formato_txt=txt.replace(",",".",2)
    return formato_txt

def calcular_capital (interes_hipoteca_mensual,monto_hipoteca_moneda,periodos_meses):
    
   
    #calculo periodo

    #print("interes_hipoteca_mensual",interes_hipoteca_mensual)
  
    meses=periodos_meses

    dividendo=((((((interes_hipoteca_mensual/100))+1)**meses))*((interes_hipoteca_mensual/100)))
    divisor=((((interes_hipoteca_mensual/100))+1)**meses)-1

    resultado_dividendo= dividendo /divisor

    periodo=(monto_hipoteca_moneda*resultado_dividendo )
    return periodo

def Calcular_hipoteca_amortizacion_metodo_frances(opcion,opcion_periodo,monto_hipoteca_moneda):
    #C= V / (1-(1/(1+i))^N)/i)
    lista_Interes_periodo=[]
    lista_total_faltante=[]
    lista_cuota_sin_interes=[]
    lista_cuota_con_interes=[]
    
    periodo_tiempo=0
    if(opcion=='120 meses (10 años) con un 15 % anual'):
        #numero_de_cuotas_list=range[1,180]
        
        interes_hipoteca_anual=15
    
        años_hipoteca=10

    elif(opcion=='180 meses (15 años) con un 13 % anual'):
        #numero_de_cuotas_list=range[1,180]
        
        interes_hipoteca_anual=13
    
        años_hipoteca=15

    else:
        
        interes_hipoteca_anual=10
    
        años_hipoteca=20

    if (opcion_periodo=='Mensual'):

        periodo_tiempo=años_hipoteca*12
        interes_hipoteca_periodo=interes_hipoteca_anual/periodo_tiempo
    #anual 12/ bimestral 2 =6
    elif (opcion_periodo=='Bimestral'):

        periodo_tiempo=años_hipoteca*6
        interes_hipoteca_periodo=interes_hipoteca_anual/periodo_tiempo

    #anual 12/ Trimestral 3 =4
    elif (opcion_periodo=='Trimestral'):
        periodo_tiempo=años_hipoteca*4
        interes_hipoteca_periodo=interes_hipoteca_anual/periodo_tiempo
    #anual 12/ Trimestral 4 =3

    elif (opcion_periodo=='Cuatrimestral'):
        periodo_tiempo=años_hipoteca*3
        interes_hipoteca_periodo=interes_hipoteca_anual/periodo_tiempo

    #anual 12/ semestral 6 =2
    else:
        periodo_tiempo=años_hipoteca*2
        interes_hipoteca_periodo=interes_hipoteca_anual/periodo_tiempo

    periodo_tiempo_int=int(periodo_tiempo)
    numero_de_cuotas_list=list(range(1,periodo_tiempo_int+1))
    total_credito=monto_hipoteca_moneda
    
    periodo=calcular_capital (interes_hipoteca_periodo,monto_hipoteca_moneda,periodo_tiempo)
    CUOTA_F=round(periodo,2)
    for i in numero_de_cuotas_list:

            
        interes_mensual=(total_credito*interes_hipoteca_periodo)/100
        lista_Interes_periodo.append(round(interes_mensual,2))
        capital= periodo-interes_mensual
        total_credito=(total_credito-capital)
        lista_total_faltante.append(round(total_credito,2))
        cuota_sin_interes=periodo-interes_mensual
        lista_cuota_con_interes.append(round(periodo,2))
        lista_cuota_sin_interes.append(round(cuota_sin_interes,2))
            
        
    columnas =["Mes","Cuota_fija ($)","Capital ($)","Intereses ($)","Saldo_a_pagar"]
    df_hipoteca=pd.DataFrame(list(zip(numero_de_cuotas_list,lista_cuota_con_interes,lista_cuota_sin_interes, lista_Interes_periodo,lista_total_faltante)),columns=columnas)
    sum_Cuota_fija=df_hipoteca["Cuota_fija ($)"].sum()
    return df_hipoteca ,sum_Cuota_fija,CUOTA_F