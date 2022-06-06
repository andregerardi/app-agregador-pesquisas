import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from PIL import Image
import openpyxl
import plotly.graph_objects as go
import datetime as dt


st.set_page_config(page_title='Agregador de pesquisas eleitorais por religião', layout='wide')

st.header('**Agregador de pesquisas por religião**')
st.write("##### Consolida pesquisas de institutos para as eleições presidenciais de 2022.")

#st.subheader('Eleições 2022')

## MÉDIA MÓVEL
m_m = 7

### dados de tempo
end_date = dt.datetime.today() # data atual
start_date = dt.datetime(2022,1,1) # data de oito meses atras

### dados pesquisas
df = pd.read_excel('resultados_pesquisas_lula_bolsonaro_religião.xlsx')
df.sigla = df.sigla.astype(str)

### organiza os dados da pesquisa
#df.data = df.data.sort_values(ascending=True)

### define sigla como index
#df.set_index('sigla',inplace = True)

### diferença 1o turno
df['dif_cat_1t'] = pd.DataFrame(df['lul_cat_1t'] - df['bol_cat_1t'])
df['dif_ev_1t'] = pd.DataFrame(df['bol_ev_1t'] - df['lul_ev_1t'])

## média móvel 7 dias - 1T
df['lula_ger_avg'] = df.lul_ger_1t.rolling(m_m).mean()
df['bolso_ger_avg'] = df.bol_ger_1t.rolling(m_m).mean()

## dados segundo turno
df2t = df[df['lul_ger_2t']>1] ## sumprime dados missing
df2tR = df[df['lul_cat_2t']>1] ## suprime dados missing

### diferença 2o turno
df2t['dif_cat_2t'] = pd.DataFrame(df2t['lul_cat_2t'] - df2t['bol_cat_2t'])
df2t['dif_ev_2t'] = pd.DataFrame(df2t['bol_ev_2t'] - df2t['lul_ev_2t'])

## média móvel 7 dias - 2T
df2t['lula_ger_avg_2t'] = df2t.lul_ger_2t.rolling(m_m).mean()
df2t['bolso_ger_avg_2t'] = df2t.bol_ger_2t.rolling(m_m).mean()

## total de pesquisas utilizadas pelo agregador
st.text("""
\n
\n
 """)
st.markdown(f"**Institutos de pesquisa** - _{ ', '.join(set(df['nome_instituto'].T)).title()}_")
st.markdown(f'**Contador de pesquisas eleitorais** -> {len(df)}')

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


    ################################
    ## gráfico Média movel primeiro turno###
    ################################

    with st.container():
        st.write("##### **Gráfico - Intenções de voto gerais**:")
        st.caption(f'Método utilizado no cálculo: média móvel de {m_m} dias.')

        int_vote_med_move = st.checkbox('1º Turno')

        if int_vote_med_move:
            fig = go.Figure()
            ## lula
            fig.add_trace(go.Scatter(y=df.lul_ger_1t, x=df.sigla, mode='markers', name='int_vot_geral_lula',
                                    marker=dict(
                                    size=5,
                                    color=df.lul_ger_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df.lul_ger_1t.rolling(m_m).mean(), x=df.sigla,mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.lul_ger_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df.lul_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=12, color="black", family="Arial"))

            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df.bol_ger_1t, x=df.sigla, mode='markers', name='int_vot_geral_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df.lul_ger_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df.bol_ger_1t.rolling(m_m).mean(), x=df.sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.bol_ger_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df.bol_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=14, color="black", family="Arial"))

            ## Ciro

            fig.add_trace(go.Scatter(y=df.ciro_ger_1t, x=df.sigla, mode='markers', name='int_vot_geral_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df.ciro_ger_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df.ciro_ger_1t.rolling(m_m).mean(), x=df.sigla, mode='lines', name='Ciro Gomes',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.ciro_ger_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df.ciro_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=14, color="black", family="Arial"))

            fig.update_layout(width = 1000, height = 800, template = 'none',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5, 
                orientation="h"))

            #fig.add_annotation(x="mar/22_poderdata_3", y=29,text="Moro desistiu",showarrow=True,arrowhead=1,yanchor="bottom",font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,
            rangeslider_visible=True)

            st.plotly_chart(fig)

    st.markdown("---")

    ############################################
    ## média movel dos candidatos por segmento##
    ############################################

    with st.container():
        st.write('##### **Resumo - intenção de voto por candidato ao 1º turno**:')
        st.caption(f'Método utilizado: média móvel de {m_m} dias.')
        st.caption(f"Os dados informam a média da última pesquisa mapeada: instituto _{list(df.nome_instituto)[-1]}_ do dia _{list(df.data)[-1].strftime(format='%d-%m-%Y')}_.")


        int_vot_lula = st.checkbox('Lula')

        if int_vot_lula:

            ## coluna 1
            lul = Image.open('lula-oculos.jpg')
            col0, col, col1, col2, col3 = st.columns(5)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(list(df.lul_ger_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df.lul_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df.bol_ger_1t.rolling(m_m).mean())[-1],1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df.lul_cat_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df.lul_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df.bol_cat_1t.rolling(m_m).mean())[-1],1)}")
            col2.metric(label="Evangélicos", value=f"{round(list(df.lul_ev_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df.lul_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df.bol_ev_1t.rolling(m_m).mean())[-1],1),1)}") 
            col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            col4, col5, col6, col7, col8 = st.columns(5)
            col4.metric(label="",value="")
            col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            col6.metric(label="Ateu", value=f"{round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            col7.metric(label="Sem Religião", value=f"{round(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1)}")
            col8.metric(label="Outros", value=f"{round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.caption('* Dados na cor verde indicam a vantagem de Lula em relação a Bolsonaro, e vermelho, desvantagem.')
            st.markdown("---")


        int_vot_bolsonaro = st.checkbox('Bolsonaro')

        if int_vot_bolsonaro:

            ## coluna 1
            bol = Image.open('bolsonaro_capacete.jpg')
            col0,col, col1, col2, col3 = st.columns(5)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df.bol_ger_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df.bol_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df.lul_ger_1t.rolling(m_m).mean())[-1],1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df.bol_cat_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df.bol_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df.lul_cat_1t.rolling(m_m).mean())[-1],1)}%")
            col2.metric(label="Evangélicos", value=f"{round(list(df.bol_ev_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df.bol_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df.lul_ev_1t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            col4, col5, col6, col7, col8 = st.columns(5)
            col4.metric(label="",value="")
            col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            col6.metric(label="Ateu", value=f"{round(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            col7.metric(label="Sem Religião", value=f"{round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],1)}")
            col8.metric(label="Outros", value=f"{round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.caption('* Dados na cor verde indicam a vantagem de Bolsonaro em relação a Lula, e vermelho, desvantagem.')
            st.markdown("---")

        int_vot_ciro = st.checkbox('Ciro Gomes')

        if int_vot_ciro:

            ## coluna 1
            bol = Image.open('ciro_oculos.jpg')
            col0,col, col1, col2, col3 = st.columns(5)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df.ciro_ger_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df.ciro_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df.bol_ger_1t.rolling(m_m).mean())[-1],1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df.ciro_cat_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df.ciro_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df.bol_cat_1t.rolling(m_m).mean())[-1],1)}%")
            col2.metric(label="Evangélicos", value=f"{round(list(df.ciro_ev_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df.ciro_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df.bol_ev_1t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['ciro_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            col4, col5, col6, col7, col8 = st.columns(5)
            col4.metric(label="",value="")
            col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            col6.metric(label="Ateu", value=f"{round(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            col7.metric(label="Sem Religião", value=f"{round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1),1)}")
            col8.metric(label="Outros", value=f"{round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.caption('* Dados na cor verde indicam a vantagem de Ciro em relação a Bolsonaro, e vermelho, desvantagem.')

    st.markdown("---")


    ################################################################## 
    ## container - gráfico geral católicos e evangélicos - modelo 1 ##
    ################################################################## 
    
    with st.container():
        st.write("##### **Gráfico - intenção de voto por religião**:")
        st.caption(f'Método utilizado: média móvel de {m_m} dias.')

        relig = st.selectbox('Selecione a religião:',options=['','Católica', 'Evangélica', 'Espírita', 'Umbanda/Candomblé', 'Ateu', 'Sem Religião', 'Outras Religiosidades'])
        
    if relig == 'Católica':

        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_cat_1t']>1].lul_cat_1t, x=df[df['lul_cat_1t']>1].sigla, mode='markers', name='int_vot_cat_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_cat_1t']>1].lul_cat_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean(), x=df[df['bol_cat_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_cat_1t']>1].sigla)[-1], y=int(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_cat_1t']>1].bol_cat_1t, x=df[df['bol_cat_1t']>1].sigla, mode='markers', name='int_vot_cat_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_cat_1t']>1].lul_cat_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean(), x=df[df['bol_cat_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_cat_1t']>1].sigla)[-1], y=int(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_cat_1t']>1].ciro_cat_1t, x=df[df['ciro_cat_1t']>1].sigla, mode='markers', name='int_vot_cat_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_cat_1t']>1].ciro_cat_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean(), x=df[df['ciro_cat_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_cat_1t']>1].sigla)[-1], y=int(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

        st.plotly_chart(fig)

    if relig == 'Evangélica':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_ev_1t']>1].lul_ev_1t, x=df[df['lul_ev_1t']>1].data, mode='markers', name='int_vot_ev_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_ev_1t']>1].lul_ev_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean(), x=df[df['bol_ev_1t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_ev_1t']>1].data)[-1], y=int(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))
        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_ev_1t']>1].bol_ev_1t, x=df[df['bol_ev_1t']>1].data, mode='markers', name='int_vot_ev_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_ev_1t']>1].lul_ev_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean(), x=df[df['bol_ev_1t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_ev_1t']>1].data)[-1], y=int(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))
        ## Ciro
        fig.add_trace(go.Scatter(y=df[df['ciro_ev_1t']>1].ciro_ev_1t, x=df[df['ciro_ev_1t']>1].data, mode='markers', name='int_vot_ev_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_ev_1t']>1].ciro_ev_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean(), x=df[df['ciro_ev_1t']>1].data, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_ev_1t']>1].data)[-1], y=int(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

        st.plotly_chart(fig)

    if relig == 'Espírita':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_espi_1t']>1].lul_espi_1t, x=df[df['lul_espi_1t']>1].data, mode='markers', name='int_vot_espi_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_espi_1t']>1].lul_espi_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean(), x=df[df['bol_espi_1t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_espi_1t']>1].data)[-1], y=int(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_espi_1t']>1].bol_espi_1t, x=df[df['bol_espi_1t']>1].data, mode='markers', name='int_vot_espi_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_espi_1t']>1].lul_espi_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean(), x=df[df['bol_espi_1t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_espi_1t']>1].data)[-1], y=int(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_espi_1t']>1].ciro_espi_1t, x=df[df['ciro_espi_1t']>1].data, mode='markers', name='int_vot_espi_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_espi_1t']>1].ciro_espi_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean(), x=df[df['ciro_espi_1t']>1].data, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_espi_1t']>1].data)[-1], y=int(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

        st.plotly_chart(fig)

    if relig == 'Umbanda/Candomblé':

        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_umb_can_1t']>1].lul_umb_can_1t, x=df[df['lul_umb_can_1t']>1].data, mode='markers', name='int_vot_umb_can_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_umb_can_1t']>1].lul_umb_can_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean(), x=df[df['bol_umb_can_1t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_umb_can_1t']>1].data)[-1], y=int(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_umb_can_1t']>1].bol_umb_can_1t, x=df[df['bol_umb_can_1t']>1].data, mode='markers', name='int_vot_umb_can_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_umb_can_1t']>1].lul_umb_can_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean(), x=df[df['bol_umb_can_1t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_umb_can_1t']>1].data)[-1], y=int(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t, x=df[df['ciro_umb_can_1t']>1].data, mode='markers', name='int_vot_umb_can_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean(), x=df[df['ciro_umb_can_1t']>1].data, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_umb_can_1t']>1].data)[-1], y=int(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
        st.plotly_chart(fig)

    if relig == 'Ateu':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_ateu_1t']>1].lul_ateu_1t, x=df[df['lul_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_ateu_1t']>1].lul_ateu_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean(), x=df[df['bol_ateu_1t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_ateu_1t']>1].data)[-1], y=int(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_ateu_1t']>1].bol_ateu_1t, x=df[df['bol_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_ateu_1t']>1].lul_ateu_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean(), x=df[df['bol_ateu_1t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_ateu_1t']>1].data)[-1], y=int(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        """fig.add_trace(go.Scatter(y=df[df['ciro_ateu_1t']>1].ciro_ateu_1t, x=df[df['ciro_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_ateu_1t']>1].ciro_ateu_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean(), x=df[df['ciro_ateu_1t']>1].data, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_ateu_1t']>1].data)[-1], y=int(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))"""

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
        st.plotly_chart(fig)

    if relig == 'Sem Religião':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_non_1t']>1].lul_non_1t, x=df[df['lul_non_1t']>1].data, mode='markers', name='int_vot_non_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_non_1t']>1].lul_non_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean(), x=df[df['bol_non_1t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_non_1t']>1].data)[-1], y=int(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_non_1t']>1].bol_non_1t, x=df[df['bol_non_1t']>1].data, mode='markers', name='int_vot_non_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_non_1t']>1].lul_non_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean(), x=df[df['bol_non_1t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_non_1t']>1].data)[-1], y=int(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_non_1t']>1].ciro_non_1t, x=df[df['ciro_non_1t']>1].data, mode='markers', name='int_vot_non_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_non_1t']>1].ciro_non_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean(), x=df[df['ciro_non_1t']>1].data, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_non_1t']>1].data)[-1], y=int(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

        st.plotly_chart(fig)

    if relig == 'Outras Religiosidades':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_out_1t']>1].lul_out_1t, x=df[df['lul_out_1t']>1].data, mode='markers', name='int_vot_out_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_out_1t']>1].lul_out_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean(), x=df[df['bol_out_1t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_out_1t']>1].data)[-1], y=int(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_out_1t']>1].bol_out_1t, x=df[df['bol_out_1t']>1].data, mode='markers', name='int_vot_out_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_out_1t']>1].lul_out_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean(), x=df[df['bol_out_1t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_out_1t']>1].data)[-1], y=int(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_out_1t']>1].ciro_out_1t, x=df[df['ciro_out_1t']>1].data, mode='markers', name='int_vot_out_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_out_1t']>1].ciro_out_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean(), x=df[df['ciro_out_1t']>1].data, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_out_1t']>1].data)[-1], y=int(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'none',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend=dict(
            yanchor="auto",
            y=1.1,
            xanchor="auto",
            x=0.5, 
            orientation="h"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
        st.plotly_chart(fig)
            
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
        plt.plot(df[df['nome_instituto']==inst].lul_cat_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=2,alpha=0.6, label="lul_cat_1t")
        plt.plot(df[df['nome_instituto']==inst].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="Lula_intenção_voto_geral_1t")

        plt.plot(df[df['nome_instituto']==inst].bol_cat_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=2, label="bol_cat_1t")
        plt.plot(df[df['nome_instituto']==inst].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="Bolsonaro_intenção_voto_geral_1t")

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
        plt.plot(df[df['nome_instituto']==inst].lul_ev_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=2,alpha=0.6, label="lul_ev_1t")
        plt.plot(df[df['nome_instituto']==inst].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="Lula_intenção_voto_geral_1t")

        plt.plot(df[df['nome_instituto']==inst].bol_ev_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=2, label="bol_ev_1t")
        plt.plot(df[df['nome_instituto']==inst].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="Bolsonaro_intenção_voto_geral_1t")

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

if options_turn == 'Segundo Turno':

    ################################
    ## Média movel segundo turno###
    ################################

    with st.container():
        st.write("##### **Gráfico - Intenções de voto gerais**:")
        st.caption(f'Método utilizado no cálculo: média móvel de {m_m} dias.')

        int_vote_med_move_2t = st.checkbox('2º Turno')

        if int_vote_med_move_2t:

            fig = go.Figure()
            ## lula
            fig.add_trace(go.Scatter(y=df[df['lul_ger_2t']>1].lul_ger_2t, x=df.sigla, mode='markers', name='int_vot_geral_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ger_2t']>1].lul_ger_2t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean(), x=df[df['bol_ger_2t']>1].sigla,mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_ger_2t']>1].sigla)[-1], y=int(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=12, color="black", family="Arial"))

            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df[df['bol_ger_2t']>1].bol_ger_2t, x=df.sigla, mode='markers', name='int_vot_geral_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ger_2t']>1].lul_ger_2t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean(), x=df[df['bol_ger_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_ger_2t']>1].sigla)[-1], y=int(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        font=dict(size=14, color="black", family="Arial"))

            fig.update_layout(width = 1000, height = 800, template = 'none',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5, 
                orientation="h"))

            #fig.add_annotation(x="mar/22_poderdata_3", y=29,text="Moro desistiu",showarrow=True,arrowhead=1,yanchor="bottom",font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

            st.plotly_chart(fig)

    st.markdown("---")

############################
### intenção de voto média##
############################

    with st.container():
        st.write('##### **Resumo - intenção de voto por candidato ao 2º turno**:')
        st.caption(f'Método utilizado: média móvel de {m_m} dias.')
        st.caption(f"Os dados informam a média da última pesquisa mapeada: instituto _{list(df.nome_instituto)[-1]}_ do dia _{list(df.data)[-1].strftime(format='%d-%m-%Y')}_.")

        int_vot_lula = st.checkbox('Lula ')

        if int_vot_lula:
            ## coluna 1
            lul = Image.open('lula-malhando2.jpg')
            col0, col, col1, col2, col3 = st.columns(5)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1],1),1)}")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1),1)}") 
            col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            col4, col5, col6, col7, col8 = st.columns(5)
            col4.metric(label="",value="")
            col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1],1),1)}")
            col6.metric(label="Ateu", value=f"{round(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1],1),1)}")
            col7.metric(label="Sem Religião", value=f"{round(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1],1),1)}")
            col8.metric(label="Outros", value=f"{round(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.caption('* Dados na cor verde indicam a vantagem de Lula em relação a Bolsonaro, e vermelho, desvantagem.')
            st.markdown("---")

        int_vot_bolsonaro = st.checkbox('Bolsonaro ')

        if int_vot_bolsonaro:
            ## coluna 1
            bol = Image.open('bolsonaro_boxe.jpg')
            col0, col, col1, col2, col3 = st.columns(5)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1],1),1)}")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1),1)}") 
            col3.metric(label="Espíritas", value=f"{round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1)-round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            col4, col5, col6, col7, col8 = st.columns(5)
            col4.metric(label="",value="")
            col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1],1),1)}")
            col6.metric(label="Ateu", value=f"{round(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1],1),1)}")
            col7.metric(label="Sem Religião", value=f"{round(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1],1),1)}")
            col8.metric(label="Outros", value=f"{round(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.caption('* Dados na cor verde indicam a vantagem de Bolsonaro em relação a Lula, e vermelho, desvantagem.')

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




