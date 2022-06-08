from matplotlib import image
import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from PIL import Image
import openpyxl
import plotly.graph_objects as go
import datetime as dt


########################################################################
##configuração da página, texto exibido na aba e dados no item 'about'##
########################################################################

st.set_page_config(
     page_title="Agregador de pesquisas eleitorais por religião",
     page_icon="chart_with_upwards_trend",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "##### Desenvolvedor: Dirceu André Gerardi. \n **E-mail:** andregerardi3@gmail.com  \n **Git:** https://github.com/andregerardi/"
     }
 )

## subtítulos do cabeçalho
st.header('**Agregador de pesquisas por religião**')
st.write("##### Consolida pesquisas de institutos para as eleições presidenciais de 2022.")

##retira o made streamlit no fim da página##
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#################
## configurações#
#################

## MÉDIA MÓVEL
m_m = 7

### dados de tempo
end_date = dt.datetime.today() # data atual
start_date = dt.datetime(2022,1,1) # data de oito meses atras

### dados pesquisas
df = pd.read_excel('resultados_pesquisas_lula_bolsonaro_religião.xlsx')
df.sigla = df.sigla.astype(str)

## insere o total de pesquisas eleitorais
st.markdown(f'**Contador de pesquisas eleitorais** -> {len(df)}')
st.markdown(f"**Institutos analisados** -> _{', '.join(set(df['nome_instituto'].T)).title()}_.")
st.markdown("---")

########################################################################
#### seletor para escolher o perído do primeiro ou do segundo turno#####
########################################################################


st.write("""
\n
\n
\n
 """)
st.text("""
\n
\n
 """)

with st.container():
    st.write("##### **Selecione o turno da eleição:**")
    options_turn = st.selectbox('',options=['clique e selecione o turno','Primeiro Turno', 'Segundo Turno'])
    st.markdown("---")

########################
### primeiro turno #####
########################

if options_turn == 'Primeiro Turno':

    ########################################
    ## gráfico média movel primeiro turno###
    ########################################

    with st.container():
        st.write("##### **Gráfico - Intenção de voto geral**:")

        int_vote_med_move = st.checkbox('Clique para visualizar')

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

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

            st.plotly_chart(fig)
            
        st.caption(f'**Método utilizado no cálculo**: média móvel de {m_m} dias.')
        st.caption(f'Os valores indicados no gráfico correspondem à última média da série temporal.')
    st.markdown("---")

    ############################################
    ## média movel dos candidatos por segmento##
    ############################################

    with st.container():
        st.write('##### **Resumo - intenção de voto por candidato**:')

        int_vot_lula = st.checkbox('Lula')

        if int_vot_lula:

            ## coluna 1
            lul = Image.open('lula_perfil.jpg')
            col0, col, col1, col2, col3 = st.columns(5)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1)}")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1),1)}") 
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
            bol = Image.open('bolso_image.jpeg')
            col0,col, col1, col2, col3 = st.columns(5)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],1)}%")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],1),1)}")
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
            ciro = Image.open('ciro_perfil.jpg')
            col0,col, col1, col2, col3 = st.columns(5)
            col0.image(ciro,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1)}%")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['ciro_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            col4, col5, col6, col7, col8 = st.columns(5)
            col4.metric(label="",value="")
            col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            col6.metric(label="Ateu", value=f"{round(list(df[df['ciro_ateu_1t']>=1].ciro_ateu_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            col7.metric(label="Sem Religião", value=f"{round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1),1)}")
            col8.metric(label="Outros", value=f"{round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.caption('* Dados na cor verde indicam a vantagem de Ciro em relação a Bolsonaro, e vermelho, desvantagem.')

        st.caption(f'**Método utilizado:** média móvel de {m_m} dias.')
        st.caption(f"Os dados informam a última média da série temporal registrada no dia _{list(df.data)[-1].strftime(format='%d-%m-%Y')}_.")

    st.markdown("---")


    ################################################################## 
    ## container - gráfico geral católicos e evangélicos - modelo 1 ##
    ################################################################## 
    
    with st.container():
        st.write("##### **Gráfico - intenção de voto por religião, ateus e sem religião**:")

        relig = st.selectbox('Selecione a religião:',options=['Escolha a opção','Católica', 'Evangélica', 'Espírita', 'Umbanda/Candomblé', 'Ateu', 'Sem Religião', 'Outras Religiosidades'])
        
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
        fig.add_trace(go.Scatter(y=df[df['lul_ev_1t']>1].lul_ev_1t, x=df[df['lul_ev_1t']>1].sigla, mode='markers', name='int_vot_ev_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_ev_1t']>1].lul_ev_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean(), x=df[df['bol_ev_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_ev_1t']>1].sigla)[-1], y=int(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))
        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_ev_1t']>1].bol_ev_1t, x=df[df['bol_ev_1t']>1].sigla, mode='markers', name='int_vot_ev_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_ev_1t']>1].lul_ev_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean(), x=df[df['bol_ev_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_ev_1t']>1].sigla)[-1], y=int(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))
        ## Ciro
        fig.add_trace(go.Scatter(y=df[df['ciro_ev_1t']>1].ciro_ev_1t, x=df[df['ciro_ev_1t']>1].sigla, mode='markers', name='int_vot_ev_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_ev_1t']>1].ciro_ev_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean(), x=df[df['ciro_ev_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_ev_1t']>1].sigla)[-1], y=int(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1])}%",
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
        fig.add_trace(go.Scatter(y=df[df['lul_out_1t']>1].lul_out_1t, x=df[df['lul_out_1t']>1].sigla, mode='markers', name='int_vot_out_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_out_1t']>1].lul_out_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean(), x=df[df['bol_out_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_out_1t']>1].sigla)[-1], y=int(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_out_1t']>1].bol_out_1t, x=df[df['bol_out_1t']>1].sigla, mode='markers', name='int_vot_out_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_out_1t']>1].lul_out_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean(), x=df[df['bol_out_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_out_1t']>1].sigla)[-1], y=int(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=14, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_out_1t']>1].ciro_out_1t, x=df[df['ciro_out_1t']>1].sigla, mode='markers', name='int_vot_out_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_out_1t']>1].ciro_out_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean(), x=df[df['ciro_out_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_out_1t']>1].sigla)[-1], y=int(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1])}%",
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
    
    ## info
    st.caption(f'**Método utilizado:** média móvel de {m_m} dias.')
    st.caption('**Obs.:** Em alguns casos, a combinção de dados retornará um gráfico em branco. \n Isso indica que instituto de pesquisa selecionado não coletou dados da categoria.')
    st.markdown("---")

    #####################################
    ### dados por instituto de pesquisa##    
    #####################################

    institutos = list(set(df['nome_instituto']))
    institutos.insert(0, '')

    with st.container():
        st.write("##### **Gráfico - intenção de voto por instituto de pesquisa e religião, ateus e sem religião**:")

        col, col1 = st.columns(2)
        with col:
            inst = st.selectbox('Selecione o instituto de pesquisa:',options=institutos)
        with col1:
            rel = st.selectbox('Escolha a religião:',options=['','Católica', 'Evangélica', 'Espírita', 'Umbanda/Candomblé', 'Ateu', 'Sem Religião', 'Outras Religiosidades'])

        col1, col2, col3 = st.columns([.5,3,.5])

        with col2:
            if rel == 'Católica':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'católicos' para presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_cat_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_cat")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_cat_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_cat_1t")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_cat_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_cat_1t")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )
        
            if rel == 'Evangélica':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'evangélicos' para presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_ev_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ev")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_ev_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ev_1t")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_ev_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_ev_1t")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )
        
            if rel == 'Espírita':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'espírita/kradecista' para presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_espi_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_espi")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_espi_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_espi_1t")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_espi_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_espi_1t")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )

            if rel == 'Umbanda/Candomblé':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'umbandistas e candonblecistas' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_umb_can_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_umb_can")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_umb_can_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_umb_can")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_umb_can_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_umb_can")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              
    
            if rel == 'Ateu':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'ateus' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_ateu_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ateu")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_ateu_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ateu")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_ateu_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_ateu")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              
    
            if rel == 'Sem Religião':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'sem religião' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_non_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_non")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_non_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_non")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_non_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_non")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              

            if rel == 'Outras Religiosidades':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'outras religiosidades' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_out_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_outras")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_out_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_outras")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_out_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_outras")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()
                
                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              
    
    
    st.markdown("---") 

########################
### segundo turno ######
########################

if options_turn == 'Segundo Turno':

    ################################
    ## Média movel segundo turno###
    ################################

    with st.container():
        st.write("##### **Gráfico - Intenções de voto geral**:")
        st.caption(f'Método utilizado no cálculo: média móvel de {m_m} dias.')

        int_vote_med_move_2t = st.checkbox('Clique paa visualizar')

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
            fig.update_yaxes(range=[0,70])

            st.plotly_chart(fig)

    st.markdown("---")

############################
### intenção de voto média##
############################

    with st.container():
        st.write('##### **Resumo - intenção de voto por candidato**:')
        st.caption(f'Método utilizado: média móvel de {m_m} dias.')
        st.caption(f"Os dados informam a média da última pesquisa registrada no dia _{list(df.data)[-1].strftime(format='%d-%m-%Y')}_.")

        int_vot_lula = st.checkbox('Lula ')

        if int_vot_lula:
            ## coluna 1
            lul = Image.open('lula_perfil.jpg')
            col0, col, col1, col2, col3 = st.columns(5)
            col0.image(lul,width=105,channels="B")
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
            bol = Image.open('bolso_image.jpeg')
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


    #########################################
    ##intenção de voto por religião 2 truno##
    #########################################

    with st.container():
        st.write("##### **Gráfico - intenção de voto por religião, ateus e sem religião**:")
        st.caption(f'Método utilizado: média móvel de {m_m} dias.')

        relig2t = st.selectbox('Selecione a religião:',options=['','Católica ', 'Evangélica ', 'Espírita ', 'Umbanda/Candomblé ', 'Ateu ', 'Sem Religião ', 'Outras Religiosidades '])
        
    if relig2t == 'Católica ':

        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_cat_2t']>1].lul_cat_2t, x=df[df['lul_cat_2t']>1].sigla, mode='markers', name='int_vot_cat_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_cat_2t']>1].lul_cat_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean(), x=df[df['bol_cat_2t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_cat_2t']>1].sigla)[-1], y=int(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_cat_2t']>1].bol_cat_2t, x=df[df['bol_cat_2t']>1].sigla, mode='markers', name='int_vot_cat_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_cat_2t']>1].lul_cat_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean(), x=df[df['bol_cat_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_cat_2t']>1].sigla)[-1], y=int(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1])}%",
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

    if relig2t == 'Evangélica ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_ev_2t']>1].lul_ev_2t, x=df[df['lul_ev_2t']>1].sigla, mode='markers', name='int_vot_ev_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_ev_2t']>1].lul_ev_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean(), x=df[df['bol_ev_2t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_ev_2t']>1].sigla)[-1], y=int(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))
        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_ev_2t']>1].bol_ev_2t, x=df[df['bol_ev_2t']>1].sigla, mode='markers', name='int_vot_ev_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_ev_2t']>1].lul_ev_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean(), x=df[df['bol_ev_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_ev_2t']>1].sigla)[-1], y=int(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1])}%",
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

    if relig2t == 'Espírita ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_espi_2t']>1].lul_espi_2t, x=df[df['lul_espi_2t']>1].data, mode='markers', name='int_vot_espi_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_espi_2t']>1].lul_espi_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean(), x=df[df['bol_espi_2t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_espi_2t']>1].data)[-1], y=int(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_espi_2t']>1].bol_espi_2t, x=df[df['bol_espi_2t']>1].data, mode='markers', name='int_vot_espi_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_espi_2t']>1].lul_espi_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean(), x=df[df['bol_espi_2t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_espi_2t']>1].data)[-1], y=int(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1])}%",
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

    if relig2t == 'Umbanda/Candomblé ':

        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_umb_can_2t']>1].lul_umb_can_2t, x=df[df['lul_umb_can_2t']>1].data, mode='markers', name='int_vot_umb_can_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_umb_can_2t']>1].lul_umb_can_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean(), x=df[df['bol_umb_can_2t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_umb_can_2t']>1].data)[-1], y=int(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_umb_can_2t']>1].bol_umb_can_2t, x=df[df['bol_umb_can_2t']>1].data, mode='markers', name='int_vot_umb_can_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_umb_can_2t']>1].lul_umb_can_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean(), x=df[df['bol_umb_can_2t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_umb_can_2t']>1].data)[-1], y=int(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1])}%",
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

    if relig2t == 'Ateu ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_ateu_2t']>1].lul_ateu_2t, x=df[df['lul_ateu_2t']>1].data, mode='markers', name='int_vot_ateu_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_ateu_2t']>1].lul_ateu_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean(), x=df[df['bol_ateu_2t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_ateu_2t']>1].data)[-1], y=int(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_ateu_2t']>1].bol_ateu_2t, x=df[df['bol_ateu_2t']>1].data, mode='markers', name='int_vot_ateu_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_ateu_2t']>1].lul_ateu_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean(), x=df[df['bol_ateu_2t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_ateu_2t']>1].data)[-1], y=int(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1])}%",
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

    if relig2t == 'Sem Religião ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_non_2t']>1].lul_non_2t, x=df[df['lul_non_2t']>1].data, mode='markers', name='int_vot_non_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_non_2t']>1].lul_non_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean(), x=df[df['bol_non_2t']>1].data,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_non_2t']>1].data)[-1], y=int(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_non_2t']>1].bol_non_2t, x=df[df['bol_non_2t']>1].data, mode='markers', name='int_vot_non_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_non_2t']>1].lul_non_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean(), x=df[df['bol_non_2t']>1].data,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_non_2t']>1].data)[-1], y=int(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1])}%",
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

    if relig2t == 'Outras Religiosidades ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_out_2t']>1].lul_out_2t, x=df[df['lul_out_2t']>1].sigla, mode='markers', name='int_vot_out_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_out_2t']>1].lul_out_2t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean(), x=df[df['bol_out_2t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_out_2t']>1].sigla)[-1], y=int(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    font=dict(size=12, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_out_2t']>1].bol_out_2t, x=df[df['bol_out_2t']>1].sigla, mode='markers', name='int_vot_out_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_out_2t']>1].lul_out_2t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean(), x=df[df['bol_out_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_out_2t']>1].sigla)[-1], y=int(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1])}%",
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


    #####################################
    ### dados por instituto de pesquisa##    
    #####################################

    institutos = list(set(df['nome_instituto']))
    institutos.insert(0, '')

    with st.container():
        st.write("##### **Gráfico - intenção de voto por instituto de pesquisa e religião, ateus e sem religião**:")

        col, col1 = st.columns(2)
        with col:
            inst2 = st.selectbox('Selecione o instituto de pesquisa:',options=institutos)
        with col1:
            rel2 = st.selectbox('Escolha a religião:',options=['','Católica', 'Evangélica', 'Espírita', 'Umbanda/Candomblé', 'Ateu', 'Sem Religião', 'Outras Religiosidades'])

        col1, col2, col3 = st.columns([.5,3,.5])

        with col2:
            if rel2 == 'Católica':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'católicos' para presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_cat_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_cat")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_cat_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_cat_2t")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )

            if rel2 == 'Evangélica':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'evangélicos' para presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ev_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ev")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_ev_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ev_2t")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )

            if rel2 == 'Espírita':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'espírita/kradecista' para presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_espi_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_espi")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_espi_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_espi_2t")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )

            if rel2 == 'Umbanda/Candomblé':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'umbandistas e candonblecistas' à presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_umb_can_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_umb_can")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_umb_can_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_umb_can")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              

            if rel2 == 'Ateu':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'ateus' à presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ateu_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ateu")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_ateu_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ateu")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              

            if rel2 == 'Sem Religião':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'sem religião' à presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_non_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_non")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_non_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_non")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              

            if rel2 == 'Outras Religiosidades':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Intenção de voto de 'outras religiosidades' à presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst2)].lul_out_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_outras")
                plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

                plt.plot(df[(df['nome_instituto']==inst2)].bol_out_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_outras")
                plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Intenção de voto em %')
                plt.rcParams.update({'axes.facecolor':'white'})

                plt.grid(color='black', linestyle='-', linewidth=.08)
                plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

                #axes = plt.gca()
                #axes.xaxis.grid()

                grafico = plt.savefig("grafico.png",bbox_inches='tight')

                st.pyplot(plt)

                with open(f"grafico.png", "rb") as file:
                    st.download_button(
                            label="Baixar o gráfico",
                            data=file,
                            file_name="grafico.png",
                            mime="image/png"
                            )              

    st.markdown("---") 

###############################################################################
## importa e plota o quadro com a lista de pesquisas utilizadas pelo agregador##
################################################################################
st.write("##### Informações sobre o agregador:")
st.write("""
\n
\n
\n
 """)

with st.container():
    col, col1, col2 = st.columns(3)
    
    with col:
        expander3 = st.expander("Pesquisas eleitorais utilizadas")
        expander3.write("""#### Lista de pesquisas""")
        lista = df[['nome_instituto', 'data', 'registro_tse','entrevistados', 'margem_erro', 'confiança']].fillna(0).astype({'nome_instituto': 'str', 'data': 'datetime64', 'registro_tse': 'str', 'entrevistados':'int','margem_erro':'str','confiança':'int'})
        expander3.dataframe(lista)

        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8-sig')

        csv = convert_df(lista)

        expander3.download_button(
            label="Baixe a lista em CSV",
            data=csv,
            file_name='lista.csv',
            mime='text/csv',
        )
        expander3.caption('*Fontes*: TSE e Institutos de Pesquisa')


### Metodologia utilizada pelo agregador ###
    with col1:
        expander = st.expander("Metodologia")
        expander.caption(f"""
        **_Explicação:_**
        1. O banco de dados é composto por informações de {len(df)} institutos de pesquisa;
        2. Os institutos consultados são: _{ ', '.join(set(df['nome_instituto'].T)).title()}_;
        3. Para o levantamento consideramos a intenção de voto estimulada de Lula, Bolsonaro e Ciro Gomes. Selecionamos a intenção de voto geral e a partir o recorte religioso, ateus e sem religião;
        4. No levantamento de dados do agregador, em relação as pesquisas, consideramos a última data em que os entrevistadores colheram as respostas e não a data da divulgação da pesquisa.
        5. Partindo da data das pequisas calculou-se o média móvel de diversas variáveis corresponendo à {m_m} dias. 
        6. Para obter a média móvel usamos dados de uma série temporal e aplicamos seguinte código Python `rolling().mean()`. Uma explicação detalhada da utilização deste código pode ser [vista aqui](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html).
        7. Ao calcular a média móvel os {m_m} primeiros resultados não são exibidos nos gráficos, e o objetivo principal é minimizar as oscilações dexando os gráficos mais limpos.
        8. O resumo das médias moveis considera o último valor obtido para cada candidato. O dado será atualizado à media que novas informações forem inseridas no banco de dados.
        8. Os institutos de pesquisa, por motívos internos, não incluem dados do recorte religioso, de ateus e sem religião, em todas as ondas pequisadas. Por esse motivo, em alguns casos, os gráficos por instituto de pesquisa não exibem as informações selecionadas.
        9. Para deixar os gráficos limpos optou-se por não inserir a margem de erro na linha da média móvel.
        """)

### Como citar o agregador ####
    with col2:
        expander2 = st.expander("Como citar")
        expander2.markdown(f"""
            **GERARDI**, Dirceu André; **ALMEIDA**, Ronaldo. Agregador de pesquisas eleitorais por religião: consolidação de dados de pesquisas com recorte religioso às eleições presidenciais de 2022. Versão 1.0. São Paulo: Streamlit, 2022. Disponível em: https://cebrap.org.br/projetos/. Acesso em: 00/00/000.
        """)

st.markdown("---")

