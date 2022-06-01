import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from PIL import Image
import openpyxl


st.set_page_config(page_title='Agregador de pesquisas eleitorais por religião', layout='wide')

st.header('Agregador de pesquisas eleitorais por religião')
#st.subheader('Eleições 2022')

### dados de tempo
end_date = dt.datetime.today() # data atual
start_date = dt.datetime(2022,1,1) # data de oito meses atras

### dados pesquisas
df = pd.read_excel('resultados_pesquisas_lula_bolsonaro_religião.xlsx')
df.sigla = df.sigla.astype(str)
df.set_index('sigla',inplace = True)

### diferença 1o turno
df['dif_cat_1t'] = pd.DataFrame(df['lula_cat_1t'] - df['bolsonaro_cat_1t'])
df['dif_ev_1t'] = pd.DataFrame(df['bolsonaro_ev_1t'] - df['lula_ev_1t'])

### diferença 2o turno
df['dif_cat_2t'] = pd.DataFrame(df['lula_cat_2t'] - df['bolsonaro_cat_2t'])
df['dif_ev_2t'] = pd.DataFrame(df['bolsonaro_ev_2t'] - df['lula_ev_2t'])

st.markdown("---")

############ 
### métricas da média de intenção de votos nos candidatos - priemeiro turno
############

########################
### primeiro turno #####
########################

with st.container():
    st.write('### **Dados do Primeiro Turno**:')
    st.write('##### **_Média da intenção de voto_**')

    int_vot_lula = st.checkbox('Lula')

    if int_vot_lula:
        lul = Image.open('lula-oculos.jpg')
        col0, col, col1, col2 = st.columns(4)
        col0.image(lul,width=85)
        col.metric(label="Geral", value=f"{round(df[df['ano']==2022].lula_geral_1t.mean(),0)}%")
        col1.metric(label="Católicos", value=f"{round(df[df['ano']==2022].lula_cat_1t.mean(),0)}%")
        col2.metric(label="Evangélicos", value=f"{round(df[df['ano']==2022].lula_ev_1t.mean(),0)}%")

    int_vot_bolsonaro = st.checkbox('Bolsonaro')

    if int_vot_bolsonaro:
        bol = Image.open('bolsonaro_capacete.jpg')
        col0,col, col1, col2 = st.columns(4)
        col0.image(bol,width=90)
        col.metric(label="Geral", value=f"{round(df[df['ano']==2022].bolsonaro_geral_1t.mean(),0)}%")
        col1.metric(label="Católicos", value=f"{round(df[df['ano']==2022].bolsonaro_cat_1t.mean(),0)}%")
        col2.metric(label="Evangélicos", value=f"{round(df[df['ano']==2022].bolsonaro_ev_1t.mean(),0)}%")

############ 
## container - gráfico geral católicos e evangélicos - modelo 1
############ 
with st.container():
    st.write("##### Selecione as informações para visualização dos gráficos:")

    st.write("""
        \n
     """)
    relig = st.selectbox('Religião:',options=['','Católica', 'Evangélica'])
    
if relig == 'Católica':
    plt.figure(figsize=(17,8)) 
    plt.title("Intenção de voto de 'católicos' para presidente" + "\n", fontdict={'fontsize':18})
    plt.plot(df.lula_cat_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=2,alpha=0.6, label="Lula_cat_1t")
    plt.plot(df.lula_geral_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="Lula_intenção_voto_geral_1t")

    plt.plot(df.bolsonaro_cat_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=2, label="Bolsonaro_cat_1t")
    plt.plot(df.bolsonaro_geral_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=5, color='skyblue', linewidth=1, label="Bolsonaro_intenção_voto_geral_1t")

    plt.style.use('ggplot')
    plt.xlabel('mês/ano e instituto de pesquisa')
    plt.xticks(rotation=80)
    plt.ylabel('Intenção de voto em %')
    plt.legend(fontsize=9, facecolor='w')

    #Lula
    plt.axhline(round(df['lula_cat_1t'].mean(),0), color='firebrick', linestyle='dashed', linewidth=.5)
    plt.text(35.5,round(df['lula_cat_1t'].mean(),0)+.5, f"média_lula_cat_1t={round(df['lula_cat_1t'].mean(),0)}%")
    #Bolsonaro
    plt.axhline(round(df['bolsonaro_cat_1t'].mean(),0), color='skyblue', linestyle='dashed', linewidth=.5)
    plt.text(35.5,round(df['bolsonaro_cat_1t'].mean(),0)+.5, f"média_bolsonaro_cat_1t={round(df['bolsonaro_cat_1t'].mean(),0)}%")


    plt.axvspan('fev/21_ipec', 'dez/21_quaest', facecolor="#929591", alpha=0.1)
    #plt.axvspan('dez/21_quaest','mai_22_datafolha', facecolor="#929591", alpha=0.2)

    plt.rcParams['axes.facecolor'] = 'white'

    st.pyplot(plt)
    
    st.write('**Comentários:**')
    st.write(f"Em 2022, a intenção de voto _geral_1t_ de Bolsonaro foi de {round(df[df['ano']==2022].bolsonaro_geral_1t.mean(),0)}% em média, e no segmento _cat_1tólico_ de {round(df[df['ano']==2022].bolsonaro_cat_1t.mean(),0)}%.")
    st.write(f"Lula, no mesmo período, obteve intenção de voto _geral_1t_ de {round(df[df['ano']==2022].lula_geral_1t.mean(),0)}% em média, e no segmento _cat_1tólico_ {round(df[df['ano']==2022].lula_cat_1t.mean(),0)}%.")
    st.write(f"A diferença das intenções de voto entre Lula e Bolsonaro foram as seguintes:") 
    st.write(f"Geral = > {round(df[df['ano']==2022].lula_geral_1t.mean(),0) -round(df[df['ano']==2022].bolsonaro_geral_1t.mean(),0)}%.")
    st.write(f"Católicos = > {round(df[df['ano']==2022].lula_cat_1t.mean(),0) -round(df[df['ano']==2022].bolsonaro_cat_1t.mean(),0)}%.")
    

if relig == 'Evangélica':
    plt.figure(figsize=(17,8)) 
    plt.title("Intenção de voto de 'evangélicos' para presidente" + "\n", fontdict={'fontsize':18})
    plt.plot(df.lula_ev_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=2,alpha=0.6, label="Lula_ev_1t")
    plt.plot(df.lula_geral_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="Lula_intenção_voto_geral_1t")

    plt.plot(df.bolsonaro_ev_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=2, label="Bolsonaro_ev_1t")
    plt.plot(df.bolsonaro_geral_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=5, color='skyblue', linewidth=1, label="Bolsonaro_intenção_voto_geral_1t")

    plt.style.use('ggplot')
    plt.xlabel('mês/ano e instituto de pesquisa')
    plt.xticks(rotation=80)
    plt.ylabel('Intenção de voto em %')
    plt.legend(fontsize=9, facecolor='w')

    #Lula
    plt.axhline(round(df['lula_ev_1t'].mean(),0), color='firebrick', linestyle='dashed', linewidth=.5)
    plt.text(35.5,round(df['lula_ev_1t'].mean(),0)+.5, f"média_lula_ev_1t={round(df['lula_ev_1t'].mean(),0)}%")
    #Bolsonaro
    plt.axhline(round(df['bolsonaro_ev_1t'].mean(),0), color='skyblue', linestyle='dashed', linewidth=.5)
    plt.text(35.5,round(df['bolsonaro_ev_1t'].mean(),0)+.5, f"média_bolsonaro_ev_1t={round(df['bolsonaro_ev_1t'].mean(),0)}%")


    plt.axvspan('fev/21_ipec', 'dez/21_quaest', facecolor="#929591", alpha=0.1)
    #plt.axvspan('dez/21_quaest','mai_22_datafolha', facecolor="#929591", alpha=0.2)

    plt.rcParams['axes.facecolor'] = 'white' 
    st.pyplot(plt)
    
    st.write('**Comentários:**')
    st.write(f"Em 2022, a intenção de voto _geral_1t_ de Bolsonaro foi de {round(df[df['ano']==2022].bolsonaro_geral_1t.mean(),0)}% em média, e no segmento _ev_1tangélico_ de {round(df[df['ano']==2022].bolsonaro_ev_1t.mean(),0)}%.")
    st.write(f"Lula, no mesmo período, obteve intenção de voto _geral_1t_ de {round(df[df['ano']==2022].lula_geral_1t.mean(),0)}% em média, e no segmento evangélico {round(df[df['ano']==2022].lula_ev_1t.mean(),0)}%.")
    st.write(f"A diferença das intenções de voto entre Lula e Bolsonaro foram as seguintes:") 
    st.write(f"Geral = > {round(df[df['ano']==2022].lula_geral_1t.mean(),0) -round(df[df['ano']==2022].bolsonaro_geral_1t.mean(),0)}%.")
    st.write(f"Evangélicos = > {round(df[df['ano']==2022].lula_ev_1t.mean(),0) -round(df[df['ano']==2022].bolsonaro_ev_1t.mean(),0)}%.")
    
st.markdown("---")

##############
### dados por instituto de pesquisa    
##############

institutos = list(set(df['nome_instituto']))
institutos.insert(0, '')

with st.container():
    col, col1 = st.columns(2)
    with col:
        inst = st.selectbox('Instituto de pesquisa:',options=institutos)
    with col1:
        rel = st.selectbox('Religiao:',options=['','Católica', 'Evangélica'])

if rel == 'Católica':
    
    plt.figure(figsize=(17,4)) 
    plt.title(f"Intenção de voto de 'católicos' para presidente - '{inst}'" + "\n", fontdict={'fontsize':18})
    plt.plot(df[df['nome_instituto']==inst].lula_cat_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=2,alpha=0.6, label="Lula_cat_1t")
    plt.plot(df[df['nome_instituto']==inst].lula_geral_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="Lula_intenção_voto_geral_1t")

    plt.plot(df[df['nome_instituto']==inst].bolsonaro_cat_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=2, label="Bolsonaro_cat_1t")
    plt.plot(df[df['nome_instituto']==inst].bolsonaro_geral_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="Bolsonaro_intenção_voto_geral_1t")

    plt.style.use('ggplot')
    plt.xlabel('mês/ano e instituto de pesquisa')
    plt.xticks(rotation=80)
    plt.ylabel('Intenção de voto em %')
    plt.legend(fontsize=9, facecolor='w')

    plt.rcParams['axes.facecolor'] = 'white'

    st.pyplot(plt)
    
if rel == 'Evangélica':
    
    plt.figure(figsize=(17,4)) 
    plt.title(f"Intenção de voto de 'evangélicos' para presidente - '{inst}'" + "\n", fontdict={'fontsize':18})
    plt.plot(df[df['nome_instituto']==inst].lula_ev_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=2,alpha=0.6, label="Lula_ev_1t")
    plt.plot(df[df['nome_instituto']==inst].lula_geral_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="Lula_intenção_voto_geral_1t")

    plt.plot(df[df['nome_instituto']==inst].bolsonaro_ev_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=2, label="Bolsonaro_ev_1t")
    plt.plot(df[df['nome_instituto']==inst].bolsonaro_geral_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="Bolsonaro_intenção_voto_geral_1t")

    plt.style.use('ggplot')
    plt.xlabel('mês/ano e instituto de pesquisa')
    plt.xticks(rotation=80)
    plt.ylabel('Intenção de voto em %')
    plt.legend(fontsize=9, facecolor='w')

    plt.rcParams['axes.facecolor'] = 'white'

    st.pyplot(plt)

st.markdown("---") 

########################
### segundo turno ######
########################

### intenção de voto média
with st.container():
    st.write('### **Dados do Segundo Turno**:')
    st.write('##### **_Média da intenção de voto_**')

    int_vot_lula = st.checkbox('Lula ')

    if int_vot_lula:
        lul = Image.open('lula-malhando2.jpg')
        col0, col, col1, col2 = st.columns(4)
        col0.image(lul,width=100)
        col.metric(label="Geral", value=f"{round(df[df['ano']==2022].lula_geral_2t.mean(),0)}%")
        col1.metric(label="Católicos", value=f"{round(df[df['ano']==2022].lula_cat_2t.mean(),0)}%")
        col2.metric(label="Evangélicos", value=f"{round(df[df['ano']==2022].lula_ev_2t.mean(),0)}%")

    int_vot_bolsonaro = st.checkbox('Bolsonaro ')

    if int_vot_bolsonaro:
        bol = Image.open('bolsonaro_boxe.jpg')
        col0,col, col1, col2 = st.columns(4)
        col0.image(bol,width=90)
        col.metric(label="Geral", value=f"{round(df[df['ano']==2022].bolsonaro_geral_2t.mean(),0)}%")
        col1.metric(label="Católicos", value=f"{round(df[df['ano']==2022].bolsonaro_cat_2t.mean(),0)}%")
        col2.metric(label="Evangélicos", value=f"{round(df[df['ano']==2022].bolsonaro_ev_2t.mean(),0)}%")
st.markdown("---")



### Pesquisas utilizadas pelo agregador

## importa a lista de pesquisas utilizadas pelo agregador
lista_pesquisas = pd.read_excel('lista pesquisas.xlsx', header=0)[0:10]
## filtra dados
lista_pesquisas = lista_pesquisas.fillna(0)
## plota o quadro
expander3 = st.expander("Pesquisas eleitorais utilizadas pelo agregador")
expander3.write("""#### Lista de pesquisas""")
expander3.dataframe(lista_pesquisas)
expander3.caption('*Fonte*: TSE')


### Metodologia utilizada pelo agregador
expander = st.expander("Entenda a metodologia utilizada")
expander.write("""
     descrever
 """)

### Como citar o agregador
expander2 = st.expander("Como citar o agregador")
expander2.write("""
     descrever.
 """)




