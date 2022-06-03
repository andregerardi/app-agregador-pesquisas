import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from PIL import Image
import openpyxl
import plotly.graph_objects as go


st.set_page_config(page_title='Agregador de pesquisas eleitorais por religião', layout='wide')

st.header('**Agregador de pesquisas**')
st.write("##### Consolida pesquisas de institutos a partir da religião dos entrevistados")

#st.subheader('Eleições 2022')

### dados de tempo
end_date = dt.datetime.today() # data atual
start_date = dt.datetime(2022,1,1) # data de oito meses atras

### dados pesquisas
df = pd.read_excel('resultados_pesquisas_lula_bolsonaro_religião.xlsx')
df.sigla = df.sigla.astype(str)
#df.set_index('sigla',inplace = True)

### diferença 1o turno
df['dif_cat_1t'] = pd.DataFrame(df['lula_cat_1t'] - df['bolsonaro_cat_1t'])
df['dif_ev_1t'] = pd.DataFrame(df['bolsonaro_ev_1t'] - df['lula_ev_1t'])

## média móvel 7 dias - 1T
df['lula_ger_avg'] = df.lula_geral_1t.rolling(7).mean()
df['bolso_ger_avg'] = df.bolsonaro_geral_1t.rolling(7).mean()

## dados segundo turno
df2t = df[df['lula_geral_2t']>1]

### diferença 2o turno
df2t['dif_cat_2t'] = pd.DataFrame(df2t['lula_cat_2t'] - df2t['bolsonaro_cat_2t'])
df2t['dif_ev_2t'] = pd.DataFrame(df2t['bolsonaro_ev_2t'] - df2t['lula_ev_2t'])

## média móvel 7 dia - 2T
df2t['lula_ger_avg_2t'] = df2t.lula_geral_2t.rolling(7).mean()
df2t['bolso_ger_avg_2t'] = df2t.bolsonaro_geral_2t.rolling(7).mean()

## total de pesquisas utilizadas pelo agregador
st.text("""
\n
\n
 """)
st.text(f'Contador de enquetes: {len(df)}')

st.markdown("---")

########################################################################
#### seletor para escolher o perído do primeiro ou do segundo turno#####
########################################################################

with st.container():
    st.write("##### **Selecione o turno:**")
    options_turn = st.selectbox('Opções',options=['','Primeiro Turno', 'Segundo Turno'])
    st.markdown("---")
if options_turn == 'Primeiro Turno':


############ 
### métricas da média de intenção de votos nos candidatos - priemeiro turno
############

########################
### primeiro turno #####
########################

    with st.container():
        st.write('##### **Intenção de voto média dos candidatos**:')
        
        int_vot_lula = st.checkbox('Lula')

        if int_vot_lula:
            lul = Image.open('lula-oculos.jpg')
            col0, col, col1, col2 = st.columns(4)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(df.lula_geral_1t.mean(),0)}%", delta=f"{round(df.lula_geral_1t.mean(),0) - round(df.bolsonaro_geral_1t.mean(),0)}%")
            col1.metric(label="Católicos", value=f"{round(df.lula_cat_1t.mean(),0)}%", delta=f"{round(df.lula_cat_1t.mean(),0)-round(df.bolsonaro_cat_1t.mean(),0)}")
            col2.metric(label="Evangélicos", value=f"{round(df.lula_ev_1t.mean(),0)}%") # , delta=f"{round(df.lula_ev_1t.mean(),0)-round(df.bolsonaro_ev_1t.mean(),0)}"
        
        int_vot_bolsonaro = st.checkbox('Bolsonaro')

        if int_vot_bolsonaro:
            bol = Image.open('bolsonaro_capacete.jpg')
            col0,col, col1, col2 = st.columns(4)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(df.bolsonaro_geral_1t.mean(),0)}%") #, delta=f"{round(df.bolsonaro_geral_1t.mean(),0)-round(df.lula_geral_1t.mean(),0)}"
            col1.metric(label="Católicos", value=f"{round(df.bolsonaro_cat_1t.mean(),0)}%") # , delta=f"{round(df.bolsonaro_cat_1t.mean(),0)-round(df.lula_cat_1t.mean(),0)}"
            col2.metric(label="Evangélicos", value=f"{round(df.bolsonaro_ev_1t.mean(),0)}%", delta=f"{round(df.bolsonaro_ev_1t.mean(),0)-round(df.lula_ev_1t.mean(),0)}")
    st.markdown("---")

    ################################
    ## Média movel primeiro turno###
    ################################

    with st.container():
        st.write("##### **_Gráfico das intenções de voto por religião_**:")

        int_vote_med_move = st.checkbox('Média móvel 1º Turno')

        if int_vote_med_move:
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=df.lula_geral_1t, x=df.sigla, mode='markers', name='int_vot_geral_lula',
                                    marker=dict(
                                    size=5,
                                    color=df.lula_geral_1t, #set color equal to a variable
                                    colorscale='peach')))
            fig.add_trace(go.Scatter(y=df.lula_ger_avg, x=df.sigla,mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.lula_ger_avg)[-1]),text=f"{int(list(df.lula_ger_avg)[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=12, color="black", family="Arial"))

            fig.add_trace(go.Scatter(y=df.bolsonaro_geral_1t, x=df.sigla, mode='markers', name='int_vot_geral_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df.lula_geral_1t, #set color equal to a variable
                                    colorscale='ice')))
            
            fig.add_trace(go.Scatter(y=df.bolso_ger_avg, x=df.sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.bolso_ger_avg)[-1]),text=f"{int(list(df.bolso_ger_avg)[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=14, color="black", family="Arial"))

            fig.update_layout(width = 1000, height = 700, template = 'plotly_white',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5, 
                orientation="h"
            ))

            fig.update_xaxes(tickangle = 280,
                rangeslider_visible=True)

            st.plotly_chart(fig)

    st.markdown("---")

    ############ 
    ## container - gráfico geral católicos e evangélicos - modelo 1
    ############ 
    with st.container():
        st.write("##### **_Gráfico das intenções de voto por religião_**:")

        relig = st.selectbox('Selecione a religião:',options=['','Católica', 'Evangélica'])
        
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
        st.write(f"Em 2022, a intenção de voto _geral_ de Bolsonaro foi de {round(df[df['ano']==2022].bolsonaro_geral_1t.mean(),0)}% em média, e no segmento _católico_, de {round(df[df['ano']==2022].bolsonaro_cat_1t.mean(),0)}%.")
        st.write(f"Lula, no mesmo período, obteve intenção de voto _geral_ de {round(df[df['ano']==2022].lula_geral_1t.mean(),0)}% , e entre os católicos_ {round(df[df['ano']==2022].lula_cat_1t.mean(),0)}%.")
        st.write(f"A diferença das intenções de voto entre Lula e Bolsonaro foram as seguintes:") 
        st.write(f"Geral = > {round(df.lula_geral_1t.mean(),0) -round(df.bolsonaro_geral_1t.mean(),0)}%.")
        st.write(f"Católicos = > {round(df.lula_cat_1t.mean(),0) -round(df.bolsonaro_cat_1t.mean(),0)}%.")
        

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
        st.write("##### **_Gráfico por instituto de pesquisa e religião_**:")

        col, col1 = st.columns(2)
        with col:
            inst = st.selectbox('Selecione o instituto de pesquisa:',options=institutos)
        with col1:
            rel = st.selectbox('Escolha a religião:',options=['','Católica', 'Evangélica'])

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

if options_turn == 'Segundo Turno':

########################
### segundo turno ######
########################

### intenção de voto média
    with st.container():
        st.write('### **Dados do 2º turno**:')
        st.write('##### **_Média da intenção de voto_**')

        int_vot_lula = st.checkbox('Lula ')

        if int_vot_lula:
            lul = Image.open('lula-malhando2.jpg')
            col0, col, col1, col2 = st.columns(4)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(df[df['ano']==2022].lula_geral_2t.mean(),0)}%", delta=f"{round(df[df['ano']==2022].lula_geral_2t.mean(),0)-round(df[df['ano']==2022].bolsonaro_geral_2t.mean(),0)}%")
            col1.metric(label="Católicos", value=f"{round(df[df['ano']==2022].lula_cat_2t.mean(),0)}%", delta=f"{round(df[df['ano']==2022].lula_cat_2t.mean(),0)-round(df[df['ano']==2022].bolsonaro_cat_2t.mean(),0)}")
            col2.metric(label="Evangélicos", value=f"{round(df[df['ano']==2022].lula_ev_2t.mean(),0)}%", delta=f"{round(df[df['ano']==2022].lula_ev_2t.mean(),0)-round(df[df['ano']==2022].bolsonaro_ev_2t.mean(),0)}")
        
        int_vot_bolsonaro = st.checkbox('Bolsonaro ')

        if int_vot_bolsonaro:
            bol = Image.open('bolsonaro_boxe.jpg')
            col0,col, col1, col2 = st.columns(4)
            col0.image(bol,width=90)
            col.metric(label="Geral", value=f"{round(df[df['ano']==2022].bolsonaro_geral_2t.mean(),0)}%", delta=f"{round(df[df['ano']==2022].bolsonaro_geral_2t.mean(),0)-round(df[df['ano']==2022].lula_geral_2t.mean(),0)}%")
            col1.metric(label="Católicos", value=f"{round(df[df['ano']==2022].bolsonaro_cat_2t.mean(),0)}%", delta=f"{round(df[df['ano']==2022].bolsonaro_cat_2t.mean(),0)-round(df[df['ano']==2022].lula_cat_2t.mean(),0)}")
            col2.metric(label="Evangélicos", value=f"{round(df[df['ano']==2022].bolsonaro_ev_2t.mean(),0)}%", delta=f"{round(df[df['ano']==2022].bolsonaro_ev_2t.mean(),0)-round(df[df['ano']==2022].lula_ev_2t.mean(),0)}")
    
    st.markdown("---")


    ################################
    ## Média movel segundo turno###
    ################################

    with st.container():
        st.write("##### **_Gráfico das intenções de voto por religião_**:")

        int_vote_med_move_2t = st.checkbox('Média móvel 2º Turno')

        if int_vote_med_move_2t:

            fig = go.Figure()
            fig.add_trace(go.Scatter(y=df2t.lula_geral_2t, x=df2t.sigla, mode='markers', name='int_vot_geral_lula',
                                    marker=dict(
                                    size=5,
                                    color=df2t.lula_geral_2t, #set color equal to a variable
                                    colorscale='peach')))
            fig.add_trace(go.Scatter(y=df2t.lula_ger_avg_2t, x=df2t.sigla,mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df2t.sigla)[-1], y=int(list(df2t.lula_ger_avg_2t)[-1]),text=f"{int(list(df2t.lula_ger_avg_2t)[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=12, color="black", family="Arial"))

            fig.add_trace(go.Scatter(y=df2t.bolsonaro_geral_2t, x=df2t.sigla, mode='markers', name='int_vot_geral_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df2t.lula_geral_2t, #set color equal to a variable
                                    colorscale='ice')))
            
            fig.add_trace(go.Scatter(y=df2t.bolso_ger_avg_2t, x=df2t.sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.update_layout(width = 1000, height = 800, template = 'plotly_white',
                            #title='Média móvel das intenções de voto geral por candidato (7 dias)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)')

            fig.add_annotation(x=list(df2t.sigla)[-1], y=int(list(df2t.bolso_ger_avg_2t)[-1]),text=f"{int(list(df2t.bolso_ger_avg)[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=12, color="black", family="Arial"))

            fig.update_layout(legend=dict(
                yanchor="auto",
                y=1.2,
                xanchor="auto",
                x=0.5, 
                orientation="h"
            ))

            fig.update_xaxes(tickangle = 280,
                            rangeslider_visible=True)

            fig.show()

    st.markdown("---")

st.write("""
\n
\n
\n
 """)
st.write("""
\n
\n
\n
 """)
st.write("""
\n
\n
\n
 """)

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
expander.caption("""
**_Explicação:_**
1. No levantamento de dados para o agregador, consideramos a última da em que os entrevistadores colheram as respostas e não a data de divulgação da pesquisa.
 """)

### Como citar o agregador
expander2 = st.expander("Como citar o agregador")
expander2.write("""
     descrever.
 """)




