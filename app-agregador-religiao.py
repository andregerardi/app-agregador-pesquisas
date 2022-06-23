from ctypes import alignment
from ctypes.wintypes import RGB
import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import image as image
from PIL import Image
import openpyxl
import plotly.graph_objects as go
import datetime as dt
import plotly.express as px


########################################################################
##configuração da página, texto exibido na aba e dados no item 'about'##
########################################################################

st.set_page_config(
     page_title="Agregador de pesquisas eleitorais por religião",
     page_icon="chart_with_upwards_trend",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "##### Desenvolvedor: Dirceu André Gerardi. \n **E-mail:** andregerardi3@gmail.com"
     }
 )

# st.markdown("""
# <a href="https://www.facebook.com/sharer/sharer.php?u=https://cebrap.org.br/teste-app/" title="Agregador de Pesquisas Eleitorais por religião" rel="nofollow noopener" target="_blank" style="font-size:32px!important;box-shadow:none;display:inline-block;vertical-align:middle"><span class="heateor_sss_svg" style="background-color:#3c589a;width:50px;height:50px;display:inline-block;opacity:1;float:left;font-size:32px;box-shadow:none;display:inline-block;font-size:16px;padding:0 4px;vertical-align:middle;background-repeat:repeat;overflow:hidden;padding:0;cursor:pointer;box-sizing:content-box"><svg style="display:block;" focusable="false" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="-5 -5 42 42"><path d="M17.78 27.5V17.008h3.522l.527-4.09h-4.05v-2.61c0-1.182.33-1.99 2.023-1.99h2.166V4.66c-.375-.05-1.66-.16-3.155-.16-3.123 0-5.26 1.905-5.26 5.405v3.016h-3.53v4.09h3.53V27.5h4.223z" fill="#fff"></path></svg></span></a>
# <a href="https://twitter.com/intent/tweet?text=Agregador de Pesquisas Eleitorais por religião&nbsp;&url=https://cebrap.org.br/teste-app&nbsp;&hashtags=Agregador,eleições2022,datascience" title="Twitter" rel="nofollow noopener" target="_blank" style="font-size:32px!important;box-shadow:none;display:inline-block;vertical-align:middle"><span class="heateor_sss_svg heateor_sss_s__default heateor_sss_s_twitter" style="background-color:#55acee;width:50px;height:50px;display:inline-block;opacity:1;float:left;font-size:32px;box-shadow:none;display:inline-block;font-size:16px;padding:0 4px;vertical-align:middle;background-repeat:repeat;overflow:hidden;padding:0;cursor:pointer;box-sizing:content-box"><svg style="display:block;" focusable="false" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="-4 -4 39 39"><path d="M28 8.557a9.913 9.913 0 0 1-2.828.775 4.93 4.93 0 0 0 2.166-2.725 9.738 9.738 0 0 1-3.13 1.194 4.92 4.92 0 0 0-3.593-1.55 4.924 4.924 0 0 0-4.794 6.049c-4.09-.21-7.72-2.17-10.15-5.15a4.942 4.942 0 0 0-.665 2.477c0 1.71.87 3.214 2.19 4.1a4.968 4.968 0 0 1-2.23-.616v.06c0 2.39 1.7 4.38 3.952 4.83-.414.115-.85.174-1.297.174-.318 0-.626-.03-.928-.086a4.935 4.935 0 0 0 4.6 3.42 9.893 9.893 0 0 1-6.114 2.107c-.398 0-.79-.023-1.175-.068a13.953 13.953 0 0 0 7.55 2.213c9.056 0 14.01-7.507 14.01-14.013 0-.213-.005-.426-.015-.637.96-.695 1.795-1.56 2.455-2.55z" fill="#fff"></path></svg></span></a>
# <a href="https://api.whatsapp.com/send?text=Agregador de Pesquisas Eleitorais por religião - https://cebrap.org.br/teste-app/" title="Whatsapp" rel="nofollow noopener" target="_blank" style="font-size:32px!important;box-shadow:none;display:inline-block;vertical-align:middle"><span class="heateor_sss_svg" style="background-color:#55eb4c;width:50px;height:50px;display:inline-block;opacity:1;float:left;font-size:32px;box-shadow:none;display:inline-block;font-size:16px;padding:0 4px;vertical-align:middle;background-repeat:repeat;overflow:hidden;padding:0;cursor:pointer;box-sizing:content-box"><svg style="display:block;" focusable="false" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="-6 -5 40 40"><path class="heateor_sss_svg_stroke heateor_sss_no_fill" stroke="#fff" stroke-width="2" fill="none" d="M 11.579798566743314 24.396926207859085 A 10 10 0 1 0 6.808479557110079 20.73576436351046"></path><path d="M 7 19 l -1 6 l 6 -1" class="heateor_sss_no_fill heateor_sss_svg_stroke" stroke="#fff" stroke-width="2" fill="none"></path><path d="M 10 10 q -1 8 8 11 c 5 -1 0 -6 -1 -3 q -4 -3 -5 -5 c 4 -2 -1 -5 -1 -4" fill="#fff"></path></svg></span></a></div></div>
# <br>
# """,unsafe_allow_html=True)
    

## subtítulos do cabeçalho
image = Image.open('palacio-da-alvorada-interior-black.jpg')
col3,col4,col5 = st.columns([.5,3,1])
with col4:
    st.image(image, width=800)
st.markdown("""
<br>
<h4 style='text-align: center; color:#54595F;font-family:Segoe UI'>Consolidação de pesquisas para as eleições presidenciais de 2022</h4>
""", unsafe_allow_html=True)

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

## MÉDIA MÓVEL 7 dias
m_m = 7

## MÉDIA MÓVEL 15 DIAS (EXCLUSIVO PARA O GRÁFICO DE REJEIÇÃO GERAL)
m_m15 = 15

### dados de tempo
end_date = dt.datetime.today() # data atual
start_date = dt.datetime(2022,1,1) # data de oito meses atras

### dados pesquisas
df = pd.read_excel('resultados_pesquisas_lula_bolsonaro_religião.xlsx')
#df.sigla = df['sigla'].astype(str)

##import image logo
agre = Image.open('palacio-da-alvorada-interior-black-so-agregador-branco.jpg')

###############################################################################
## importa e plota o quadro com a lista de pesquisas utilizadas pelo agregador##
################################################################################
st.markdown("---")

with st.container():
    col3,col4,col5 = st.columns([.5,4,.5])
    with col4:
        st.markdown("""
        <br>
        <h4 style='text-align: center; color: #ffffff;font-family:font-family:poppins-sans-serif;background-color: #FA7A35;'><b>Informações sobre o agregador:<b></h4><br>
        """, unsafe_allow_html=True)

        ### primeiro expander, da metodologia
        expander = st.expander("Descubra aqui como o agregador foi construído")
        expander.markdown(f"""
        <!DOCTYPE html>
        <html>
        <body>

        <p style='text-align: center; font-family:Segoe UI;'><b>Explicação:</b></p>

        <p style='text-align: justify; font-family:Segoe UI;'>1. O banco de dados é atualizado constantemente. No momento, ele contém informações de {len(df)} pesquisas eleitorais;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>2. Os institutos de pesquisa consultados são: { ', '.join(set(df['nome_instituto'].T)).title()};</p>
        <p style='text-align: justify; font-family:Segoe UI;'>3. O agregador de pesquisas por religião compila os dados dos levantamentos realizados pelos institutos. Não nos responsabilizamos pelas amostras ou técnicas utilizadas pelos diversos institutos;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>4. Para a composição do banco de dados são consideradas apenas pesquisas nacionais, bem como informações dos três principais candidatos do 1º turno das eleições presidenciais: Lula, Bolsonaro e Ciro Gomes, e de Lula e Bolsonaro, no 2º turno. Levando em conta o recorte religioso, a partir de tais pesquisas, coletamos as intenção de voto dos candidatos nos dois turnos, assim como as intenções de voto e a rejeição gerais.;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>5. O percentual de <i>rejeição</i> dos candidatos obtivemos por meio da resposta de eleitores que declaram "não votar de jeito nenhum” em determinado candidato;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>6. O percentual de <i>reprovação da administração</i> do Presidente Jair Bolsonaro foi obtido a partir da soma da respostas "ruim" e "péssimo" para a questão destinada a avaliar a satisfação dos eleitores para com a administração do mandatário: "a administração do Presidente Jair Bolsonaro está sendo ótima, boa, regular, ruim ou péssima?";</p> 
        <p style='text-align: justify; font-family:Segoe UI;'>7. Os institutos de pesquisa, por motívos internos, não incluem dados do recorte religioso nas pesquisas realizadas. Portanto, a coleta de tais informações é inconstante;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>8. Devido a irregularidade na coleta e ao tamano da amostra, dados referentes a religiões demograficamente minoritárias como os espíritas, ateus, religiões afro-brasileiras, judaísmo, islamismo, budismo, entre outras, apresentam distorções estatísticas severas. Assim, decidiu-se incluí-las na categoria "outras religiosidades";</p>
        <p style='text-align: justify; font-family:Segoe UI;'>9. Vale destacar que os dados censitários, principais referências para a construção da amostragem das pesquisas, estão defasados. Os valores de amostragem variam conforme os critérios próprios de cada instituto de pesquisa. Os institutos utilizam dados o IBGE de 2010, da PNAD de 2021 e 2022 e do TSE. As informações amostrais de corte religioso nem sempre estão disponíveis nas pesquisas compartilhadas publicamente ou constam nos documentos registrados no sistema <a href="https://www.tse.jus.br/eleicoes/pesquisa-eleitorais/consulta-as-pesquisas-registradas"><b>PesqeEle</b></a>, do TSE, dado que não é obrigatório, segundo o artigo 33 da <a href="https://www.tse.jus.br/legislacao/codigo-eleitoral/lei-das-eleicoes/sumario-lei-das-eleicoes-lei-nb0-9.504-de-30-de-setembro-de-1997">Lei nº 9.504/1997</a>. Para termos uma noção do universo amostrado pelos institutos: Os <i>católicos</i> variaram entre {int(df['am_cat'].agg('min'))}% e {int(df['am_cat'].agg('max'))}% das amostras selecionadas; <i>evangélicos</i>, entre {int(df['am_ev'].agg('min'))}% e {int(df['am_ev'].agg('max'))}%; <i>espíritas</i>, entre {int(df['am_espi'].agg('min'))}% e {int(df['am_espi'].agg('max'))}%; <i>candomblé/umbanda</i>, entre {int(df['am_umb_can'].agg('min'))}% e {int(df['am_umb_can'].agg('max'))}%; <i>outras religiões</i> de {int(df['am_out'].agg('min'))}% e {int(df['am_out'].agg('max'))}%, os <i>sem religião</i>, entre {int(df['am_non'].agg('min'))}% e {int(df['am_non'].agg('max'))}% e <i>os ateus</i> apresentaram variação entre {int(df['am_ateu'].agg('min'))}% e {int(df['am_ateu'].agg('max'))}%.</p>
        <p style='text-align: justify; font-family:Segoe UI;'>10. Em relação às pesquisas, no levantamento de dados para o agregador, consideramos a última data quando os entrevistadores colheram as respostas e não a data da divulgação da pesquisa, que por interesses diversos, podem ser adiadas por semanas ou não publicadas;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>11. Partindo da data da última coleta das pesquisas calculou-se a média móvel de diversas variáveis correspondendo à {m_m} dias;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>12. Para obter a média móvel usamos dados de uma série temporal e aplicamos o seguinte código Python <code>rolling().mean()</code>. Uma explicação detalhada da utilização deste código pode ser <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html">vista aqui</a>;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>13. Ao calcular a média móvel, os {m_m} primeiros resultados são omitidos e não aparecem nos gráficos. O objetivo principal da aplicação deste método é reduzir as oscilações no intuito de deixar as linhas dos gráficos mais fluídas. Exitem outras outras técnicas estatíticas para a redução do ruído dos dados da série temporal, tais como <i>weighted moving average, kernel smoother</i>, entre outras;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>14. O resumo das médias móveis apresentado no primeiro e segundo turnos considera e apresenta o último valor da média obtida para cada candidato. O dado é atualizado automaticamente à medida que novas pesquisas são inseridas no banco de dados;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>15. Para deixar os gráficos limpos optou-se por não inserir a margem de erro na linha da média móvel, dado que nos recortes por religião varia entre 2% até 8,5%, de acordo com institutos. Uma lista com as informações amostrais de cada pesquisa, incluíndo a margem de erro, poderá ser obtida na aba "pesquisas eleitorais utilizadas";</p>
        <p style='text-align: justify; font-family:Segoe UI;'>16. As imagens dos candidatos que utilizamos provêm das seguintes fontes: <a href="https://oglobo.globo.com/epoca/o-que-dizem-os-autores-dos-programas-dos-presidenciaveis-sobre-combate-as-mudancas-climaticas-23128520">Ciro Gomes</a>, <a href="https://www.dw.com/pt-br/o-brasil-na-imprensa-alem%C3%A3-29-05/a-48968730/">Lula</a>, <a href="https://www.poder360.com.br/poderdata/poderdata-lula-tem-50-contra-40-de-bolsonaro-no-2o-turno/">Bolsonaro</a>.</p>

        </body>
        </html>
        """,unsafe_allow_html=True)

        ### lista de pesquisas
        expander3 = st.expander("Verifique as pesquisas eleitorais utilizadas")
        expander3.write("""#### Lista de pesquisas""")
        lista = df[['nome_instituto', 'data', 'registro_tse','entrevistados', 'margem_erro', 'confiança', 'tipo_coleta']].fillna(0).astype({'nome_instituto': 'str', 'data': 'datetime64', 'registro_tse': 'str', 'entrevistados':'int','margem_erro':'str','confiança':'int', 'tipo_coleta':'str'})
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

with st.container():
    col,col1,col2,col3, col4 = st.columns([.5,1.3,1.3,1.3,.5])
    with col1:
        expander4 = st.expander('Estatíticas do agregador')
        expander4.markdown(f"""<br>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Abrangencia das pesquisas:</h6> <p style='text-align: center';>Nacional</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Institutos analisados:</h6> <p style='text-align: center';>{', '.join(set(df['nome_instituto'].T)).title()}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Método de coleta das pesquisas:</h6><p style='text-align: center';>
                Telefone: {df[df['tipo_coleta']=='telefone'].tipo_coleta.value_counts()[0]}
                <br>Presencial: {df[df['tipo_coleta']=='presencial'].tipo_coleta.value_counts()[0]}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Contador de pesquisas para dados gerais:</h6> 
            <p style='color:#000000;font-weight:700;font-size:18px;text-align: center';>
            1º turno: {len(df[df['lul_ger_1t']>=1])}<br>
            2º turno: {len(df[df['lul_ger_2t']>=1])}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Contador de pesquisas com perguntas sobre religião:</h6> 
            <p style='color:#000000;font-weight:700;font-size:18px;text-align: center';>
            1º turno: {len(df[df['lul_cat_1t']>=1])}<br>
            2º turno: {len(df[df['lul_cat_2t']>=1])}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Total de pesquisas com amostra sobre religião:</h6><p style='text-align: center';>Católicos e evangélicos: {len(df[df['lul_cat_1t']>=1])}
            <br>Espíritas: {len(df[df['lul_espi_1t']>=1])}
            <br>Umbanda/Candomblé: {len(df[df['lul_umb_can_1t']>=1])}
            <br>Outras religiões: {len(df[df['lul_out_1t']>=1])}
            <br>Sem religião: {len(df[df['lul_non_1t']>=1])}
            <br>Ateus: {len(df[df['lul_ateu_1t']>=1])}
            </p>
        """, unsafe_allow_html=True)

        ### Como citar o agregador ####
    with col2:
        expander2 = st.expander("Veja como citar o agregador")
        expander2.markdown(f"""
        <p style='text-align: center; font-family:Segoe UI;'>GERARDI, Dirceu André; ALMEIDA, Ronaldo de. <b>Agregador de pesquisas eleitorais por religião</b>: consolidação de dados de pesquisas eleitorais com recorte religioso às eleições presidenciais de 2022. Versão 1.0. São Paulo, 2022. Disponível em: https://cebrap.org.br/projetos/. Acesso em: 00/00/000.</p>
        """, unsafe_allow_html=True)

    with col3:
        expander5 = st.expander("Sobre nós")
        expander5.markdown(f"""
        <h6 style='text-align: center; color: #41AF50;'>Projeto vinclulado ao <br> Núcleo de Religiões no Mundo Contemporâneo - Cebrap</h6>
        <h6 style='text-align: center; color: #54595F;'>Coordenação:</h6><p style='text-align: center;'>Dirceu André Gerardi<br>(LabDados FGV/CEBRAP)<br><a href="mailto: andregerardi3@gmail.com">email<br></a><br>Ronaldo de Almeida<br>(UNICAMP/CEBRAP/LAR)<br><a href="mailto: ronaldormalmeida@gmail.com">email</a></p></p>
        """, unsafe_allow_html=True)
    st.markdown("---")

########################################################################
#### seletor para escolher o perído do primeiro ou do segundo turno#####
########################################################################

with st.container():
    col3,col4,col5 = st.columns([.5,1.5,.5])
    with col4:
        st.markdown("<h4 style='text-align: center; color: #ffffff; font-family:font-family:poppins-sans-serif; background-color: rgb(0, 165, 200, 100);'>Selecione o turno da eleição para visualizar os dados:</h4>", unsafe_allow_html=True)
        options_turn = st.selectbox('',options=['--clique para selecionar--','Primeiro Turno', 'Segundo Turno'])
st.markdown("---")

########################
### primeiro turno #####
########################

if options_turn == 'Primeiro Turno':

    ######################
    ###compartilhamento###
    ######################

    st.markdown(f"""
        <h2 style='text-align: center; color: #303030; font-family:tahoma; text-rendering: optimizelegibility;'>Primeiro Turno</h2>
        <br>
        """, unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(f"""
        <h3 style='text-align: center; color: #303030; font-family:segoe UI; text-rendering: optimizelegibility;background-color: #FFD662;'>1. Intenção de voto:</h3>
        """, unsafe_allow_html=True)
    st.markdown("---")

    ############################################
    ## média movel dos candidatos por segmento##
    ############################################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'>Resumo - intenção de voto geral e por religião segundo candidato:</h3><br>
        """, unsafe_allow_html=True)

        int_vot_lula = st.checkbox('Lula')

        if int_vot_lula:

            ## coluna 1
            lul = Image.open('lula_perfil.jpg')
            col0,col, col1, col2, col3, col4, col5 = st.columns(7)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],1)}%") # delta=f"{round(round(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],1)}%") # delta=f"{round(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1)}")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],1)}%") # delta=f"{round(round(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            col4.metric(label="Outros", value=f"{round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1)}%") #delta=f"{round(round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            col5.metric(label="Sem Religião", value=f"{round(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],1)}%") # delta=f"{round(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1)}")
            #col5.metric(label="Rejeição", value=f"{round(list(df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            
            ## coluna 2agre
            #col4, col5, col6, col7, col8 = st.columns(5)
            #col4.metric(label="",value="")
            #col5.metric(label="Outros", value=f"{round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1)}%") #delta=f"{round(round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            #col6.metric(label="Ateu", value=f"{round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            #col7.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            #col8.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.markdown("---")

        int_vot_bolsonaro = st.checkbox('Bolsonaro')

        if int_vot_bolsonaro:

            ## coluna 1
            bol = Image.open('bolso_image.jpeg')
            col0,col, col1, col2, col3, col4, col5 = st.columns(7)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],1)}%")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            col4.metric(label="Outros", value=f"{round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],1),1)}")
            col5.metric(label="Sem Religião", value=f"{round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],1)}")
            #col6.metric(label="Rejeição", value=f"{round(list(df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            #col6.metric(label="Gestão:'ruim/péssima'", value=f"{round(list(df[df['ava_gov_bol_GERAL']>1].ava_gov_bol_GERAL.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")

            ## coluna 2
            #col4, col5, col6, col7, col8 = st.columns(5)
            #col4.metric(label="",value="")
            #col3.metric(label="Espíritas", value=f"{round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            #col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            #col6.metric(label="Ateu", value=f"{round(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            ## info
            st.markdown("---")

        int_vot_ciro = st.checkbox('Ciro Gomes')

        if int_vot_ciro:

            ## coluna 1
            ciro = Image.open('ciro_perfil.jpg')
            col0,col, col1, col2, col3, col4, col5 = st.columns(7)
            col0.image(ciro,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],1)}%")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['ciro_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")
            col4.metric(label="Outros", value=f"{round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            col5.metric(label="Sem Religião", value=f"{round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1),1)}")

            #col5.metric(label="Rejeição", value=f"{round(list(df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1],1),1)}")

            ## coluna 2
            #col4, col5, col6, col7, col8 = st.columns(5)
            #col4.metric(label="",value="")
            #col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],1),1)}")
            #col6.metric(label="Ateu", value=f"{round(list(df[df['ciro_ateu_1t']>=1].ciro_ateu_1t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],1),1)}")
            #col7.metric(label="Sem Religião", value=f"{round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],1),1)}")
            #col8.metric(label="Outros", value=f"{round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],1),1)}")
            #col3.metric(label="Espíritas", value=f"{round(list(df[df['ciro_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],1),1)}")


        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia <i>{list(df.data)[-1].strftime(format='%d-%m-%Y')}</i></h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
        """, unsafe_allow_html=True)

    st.markdown("---")

    #####################################################
    ## gráfico intenção de voto geral - primeiro turno###
    #####################################################


    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Intenção de voto geral:</h3><br>
        """, unsafe_allow_html=True)

        int_vote_med_move = st.checkbox('Selecione para visualizar o gráfico da intenção de voto geral')

        if int_vote_med_move:

            ##import image

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
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df.bol_ger_1t, x=df.sigla, mode='markers', name='int_vot_geral_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df.bol_ger_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df.bol_ger_1t.rolling(m_m).mean(), x=df.sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.bol_ger_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df.bol_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

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
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))


            ## Brancos e Nulos

            fig.add_trace(go.Scatter(y=df.bra_nul_ns_nr_ger_1t, x=df.sigla, mode='markers', name='brancos_nulos_ns_nr',
                                    marker=dict(
                                    size=5,
                                    color=df.bra_nul_ns_nr_ger_1t, #set color equal to a variable
                                    colorscale='Greys')))

            fig.add_trace(go.Scatter(y=df.bra_nul_ns_nr_ger_1t.rolling(m_m).mean(), x=df.sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                    line=dict(color='grey', width=2.5)))

            fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df.bra_nul_ns_nr_ger_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df.bra_nul_ns_nr_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            fig.update_layout(width = 1100, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Média móvel das intenções de voto de candidatos à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_poderdata_3", y=29,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_poderdata_2", y=32,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.18,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)

            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: *Método utilizado:* média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
            """, unsafe_allow_html=True)
    st.markdown("---")

    ###################################
    ## Intenção de voto por religião ##
    ###################################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Intenção de voto por religião:</h3><br>
        """, unsafe_allow_html=True)
        ## opções retiradas 'Umbanda/Candomblé', 'Ateu',
        relig = st.selectbox('Selecione a religião:',options=['--Escolha a opção--','Católica', 'Evangélica', 'Espírita', 'Sem Religião', 'Outras Religiosidades'])

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                       ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos e Nulos

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t, x=df[df['bra_nulo_cat_1t']>1].sigla, mode='markers', name='brancos_nulos_ns_nr',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t, #set color equal to a variable
                                colorscale='Greys')))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t.rolling(m_m).mean(), x=df[df['bra_nulo_cat_1t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                line=dict(color='grey', width=2.5)))

        fig.add_annotation(x=list(df[df['bra_nulo_cat_1t']>1].sigla)[-1], y=int(list(df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
        title=("""
        <i>Média móvel das intenções de voto de católicos por candidato à presidência - 1º turno<i><br>
        """),
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        font=dict(family="arial",size=13),
                        legend=dict(
            yanchor="auto",
            y=1.15,
            xanchor="auto",
            x=0.4,
            orientation="h",
            font_family="arial",))

        fig.add_annotation(x="mar/22_poderdata_3", y=25,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_poderdata_2", y=28,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.12,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.20,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

        st.plotly_chart(fig)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais, e para os católicos, {len(df[df['lul_cat_1t']>1])} pesquisas.</h7><br>
        """, unsafe_allow_html=True)

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))
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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))
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
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos e Nulos

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t, x=df[df['bra_nulo_ev_1t']>1].sigla, mode='markers', name='brancos_nulos_ns_nr',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t, #set color equal to a variable
                                colorscale='Greys')))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t.rolling(m_m).mean(), x=df[df['bra_nulo_ev_1t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                line=dict(color='grey', width=2.5)))

        fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
        title=("""
        <i>Média móvel das intenções de voto de evangélicos por candidato à presidência - 1º turno<i><br>
        """),
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        font=dict(family="arial",size=13),
                        legend=dict(
            yanchor="auto",
            y=1.15,
            xanchor="auto",
            x=0.4,
            orientation="h",
            font_family="arial",))

        fig.add_annotation(x="mar/22_poderdata_3", y=28,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_poderdata_2", y=28,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

        fig.update_xaxes(tickangle = 300,rangeslider_visible=True,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.12,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )
        
        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.20,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        st.plotly_chart(fig)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais, e para os evangélicos, {len(df[df['lul_ev_1t']>1])} pesquisas.</h7><br>
        """, unsafe_allow_html=True)

    if relig == 'Espírita':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_espi_1t']>1].lul_espi_1t, x=df[df['lul_espi_1t']>1].sigla, mode='markers', name='int_vot_espi_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_espi_1t']>1].lul_espi_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean(), x=df[df['bol_espi_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_espi_1t']>1].sigla)[-1], y=int(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_espi_1t']>1].bol_espi_1t, x=df[df['bol_espi_1t']>1].sigla, mode='markers', name='int_vot_espi_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_espi_1t']>1].lul_espi_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean(), x=df[df['bol_espi_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_espi_1t']>1].sigla)[-1], y=int(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                        ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_espi_1t']>1].ciro_espi_1t, x=df[df['ciro_espi_1t']>1].sigla, mode='markers', name='int_vot_espi_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_espi_1t']>1].ciro_espi_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean(), x=df[df['ciro_espi_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_espi_1t']>1].sigla)[-1], y=int(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        # Brancos e Nulos
        ## inseri o filtro do lula na barra x para poder incluir o valor tipo padrão

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t, x=df[df['bra_nulo_espi_1t']>1].sigla, mode='markers', name='brancos_nulos_ns_nr',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t, #set color equal to a variable
                                colorscale='Greys')))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t.rolling(m_m).mean(), x=df[df['bra_nulo_espi_1t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                line=dict(color='grey', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_espi_1t']>1].sigla)[-1], y=int(list(df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
        title=("""
        <i>Média móvel das intenções de voto de espíritas por candidato à presidência - 1º turno<i><br>
        """),
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        font=dict(family="arial",size=13),
                        legend=dict(
            yanchor="auto",
            y=1.15,
            xanchor="auto",
            x=0.4,
            orientation="h",
            font_family="arial",))

        fig.add_annotation(x="mar/22_poderdata_3", y=28,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_poderdata_2", y=28,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.12,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )
        
        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.20,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        fig.update_xaxes(tickangle = 280, rangeslider_visible=True)

        st.plotly_chart(fig)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais, e para os espíritas, {len(df[df['lul_espi_1t']>1])} pesquisas.</h7><br>
        """, unsafe_allow_html=True)


    # if relig == 'Umbanda/Candomblé':

    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_umb_can_1t']>1].lul_umb_can_1t, x=df[df['lul_umb_can_1t']>1].data, mode='markers', name='int_vot_umb_can_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_umb_can_1t']>1].lul_umb_can_1t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean(), x=df[df['bol_umb_can_1t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='firebrick', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_umb_can_1t']>1].data)[-1], y=int(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Bolsonaro
    #     fig.add_trace(go.Scatter(y=df[df['bol_umb_can_1t']>1].bol_umb_can_1t, x=df[df['bol_umb_can_1t']>1].data, mode='markers', name='int_vot_umb_can_bolsonaro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['bol_umb_can_1t']>1].lul_umb_can_1t, #set color equal to a variable
    #                             colorscale='ice')))

    #     fig.add_trace(go.Scatter(y=df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean(), x=df[df['bol_umb_can_1t']>1].data,mode='lines', name='Bolsonaro',
    #                             line=dict(color='skyblue', width=2.5)))

    #     fig.add_annotation(x=list(df[df['bol_umb_can_1t']>1].data)[-1], y=int(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Ciro

    #     fig.add_trace(go.Scatter(y=df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t, x=df[df['ciro_umb_can_1t']>1].data, mode='markers', name='int_vot_umb_can_ciro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t, #set color equal to a variable
    #                             colorscale='Greens')))

    #     fig.add_trace(go.Scatter(y=df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean(), x=df[df['ciro_umb_can_1t']>1].data, mode='lines', name='Ciro Gomes',
    #                             line=dict(color='seagreen', width=2.5)))

    #     fig.add_annotation(x=list(df[df['ciro_umb_can_1t']>1].data)[-1], y=int(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     fig.update_layout(width = 1000, height = 800, template = 'none',
    #                     xaxis_title='Mês, ano e instituto de pesquisa',
    #                     yaxis_title='Intenção de voto (%)',
    #                     legend=dict(
    #         yanchor="auto",
    #         y=1.1,
    #         xanchor="auto",
    #         x=0.5,
    #         orientation="h"))

    #     fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
    #     st.plotly_chart(fig)

    # if relig == 'Ateu':
    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_1t']>1].lul_ateu_1t, x=df[df['lul_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_ateu_1t']>1].lul_ateu_1t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean(), x=df[df['bol_ateu_1t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='firebrick', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_ateu_1t']>1].data)[-1], y=int(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                   #  ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Bolsonaro
    #     fig.add_trace(go.Scatter(y=df[df['bol_ateu_1t']>1].bol_ateu_1t, x=df[df['bol_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_bolsonaro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['bol_ateu_1t']>1].lul_ateu_1t, #set color equal to a variable
    #                             colorscale='ice')))

    #     fig.add_trace(go.Scatter(y=df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean(), x=df[df['bol_ateu_1t']>1].data,mode='lines', name='Bolsonaro',
    #                             line=dict(color='skyblue', width=2.5)))

    #     fig.add_annotation(x=list(df[df['bol_ateu_1t']>1].data)[-1], y=int(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Ciro

    #     """fig.add_trace(go.Scatter(y=df[df['ciro_ateu_1t']>1].ciro_ateu_1t, x=df[df['ciro_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_ciro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['ciro_ateu_1t']>1].ciro_ateu_1t, #set color equal to a variable
    #                             colorscale='Greens')))

    #     fig.add_trace(go.Scatter(y=df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean(), x=df[df['ciro_ateu_1t']>1].data, mode='lines', name='Ciro Gomes',
    #                             line=dict(color='seagreen', width=2.5)))

    #     fig.add_annotation(x=list(df[df['ciro_ateu_1t']>1].data)[-1], y=int(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                   #  ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))"""

    #     fig.update_layout(width = 1000, height = 800, template = 'none',
    #                     xaxis_title='Mês, ano e instituto de pesquisa',
    #                     yaxis_title='Intenção de voto (%)',
    #                     legend=dict(
    #         yanchor="auto",
    #         y=1.1,
    #         xanchor="auto",
    #         x=0.5,
    #         orientation="h"))

    #     fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
    #     st.plotly_chart(fig)

    if relig == 'Sem Religião':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_non_1t']>1].lul_non_1t, x=df[df['lul_non_1t']>1].sigla, mode='markers', name='int_vot_non_lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_non_1t']>1].lul_non_1t, #set color equal to a variable
                                colorscale='peach')))

        fig.add_trace(go.Scatter(y=df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean(), x=df[df['bol_non_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='firebrick', width=2.5)))

        fig.add_annotation(x=list(df[df['lul_non_1t']>1].sigla)[-1], y=int(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_non_1t']>1].bol_non_1t, x=df[df['bol_non_1t']>1].sigla, mode='markers', name='int_vot_non_bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_non_1t']>1].lul_non_1t, #set color equal to a variable
                                colorscale='ice')))

        fig.add_trace(go.Scatter(y=df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean(), x=df[df['bol_non_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5)))

        fig.add_annotation(x=list(df[df['bol_non_1t']>1].sigla)[-1], y=int(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_non_1t']>1].ciro_non_1t, x=df[df['ciro_non_1t']>1].sigla, mode='markers', name='int_vot_non_ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_non_1t']>1].ciro_non_1t, #set color equal to a variable
                                colorscale='Greens')))

        fig.add_trace(go.Scatter(y=df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean(), x=df[df['ciro_non_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5)))

        fig.add_annotation(x=list(df[df['ciro_non_1t']>1].sigla)[-1], y=int(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos e Nulos

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t, x=df[df['bra_nulo_non_1t']>1].sigla, mode='markers', name='brancos_nulos_ns_nr',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t, #set color equal to a variable
                                colorscale='Greys')))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t.rolling(m_m).mean(), x=df[df['bra_nulo_non_1t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                line=dict(color='grey', width=2.5)))

        fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
        title=("""
        <i>Média móvel das intenções de voto dos sem religião por candidato à presidência - 1º turno<i><br>
        """),
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        font=dict(family="arial",size=13),
                        legend=dict(
            yanchor="auto",
            y=1.15,
            xanchor="auto",
            x=0.4,
            orientation="h",
            font_family="arial",))

        fig.add_annotation(x="mar/22_poderdata_3", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_poderdata_2", y=20,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.12,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )
      
        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.20,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

        st.plotly_chart(fig)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais, e para os sem religião, {len(df[df['lul_non_1t']>1])} pesquisas.</h7><br>
        """, unsafe_allow_html=True)

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos e Nulos

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t, x=df[df['bra_nulo_out_1t']>1].sigla, mode='markers', name='brancos_nulos_ns_nr',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t, #set color equal to a variable
                                colorscale='Greys')))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t.rolling(m_m).mean(), x=df[df['bra_nulo_out_1t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                line=dict(color='grey', width=2.5)))

        fig.add_annotation(x=list(df.sigla)[-1], y=int(list(df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
        title=("""
        <i>Média móvel das intenções de voto de outras religiões por candidato à presidência - 1º turno<i><br>
        """),
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        font=dict(family="arial",size=13),
                        legend=dict(
            yanchor="auto",
            y=1.15,
            xanchor="auto",
            x=0.4,
            orientation="h",
            font_family="arial",))

        fig.add_annotation(x="mar/22_futura", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_futura", y=20,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.12,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.20,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
        st.plotly_chart(fig)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais, e para as outras religiosidades, {len(df[df['lul_out_1t']>1])} pesquisas.</h7><br>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    #####################################
    ### dados por instituto de pesquisa##
    #####################################

    institutos = list(set(df['nome_instituto']))
    institutos.insert(0, '--Escolha o instituto--')

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'>
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Intenção de voto por religião e candidato segundo instituto de pesquisa: </h3><br>
        """, unsafe_allow_html=True)

        col, col1 = st.columns(2)
        with col:
            inst = st.selectbox('Selecione o instituto de pesquisa:',options=institutos)
        with col1:
            ##dados retirados 'Espírita', 'Umbanda/Candomblé', 'Ateu',
            rel = st.selectbox('Escolha a religião:',options=['--Escolha a religião--','Católica', 'Evangélica', 'Espírita', 'Sem Religião', 'Outras Religiosidades'])

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
                plt.title(f"\n Intenção de voto de 'espíritas' para presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
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

            # if rel == 'Umbanda/Candomblé':

            #     df.set_index('sigla',inplace = True)

            #     plt.rcParams['figure.figsize'] = (12,7)
            #     plt.title(f"\n Intenção de voto de 'umbandistas e candonblecistas' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
            #     plt.plot(df[(df['nome_instituto']==inst)].lul_umb_can_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_umb_can")
            #     plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

            #     plt.plot(df[(df['nome_instituto']==inst)].bol_umb_can_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_umb_can")
            #     plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

            #     plt.plot(df[(df['nome_instituto']==inst)].ciro_umb_can_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_umb_can")
            #     plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

            #     plt.style.use('ggplot')
            #     plt.xlabel('mês/ano e instituto de pesquisa')
            #     plt.xticks(rotation=80,fontsize=12)
            #     plt.yticks(fontsize=14)
            #     plt.ylabel('Intenção de voto em %')
            #     plt.rcParams.update({'axes.facecolor':'white'})

            #     plt.grid(color='black', linestyle='-', linewidth=.08)
            #     plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

            #     #axes = plt.gca()
            #     #axes.xaxis.grid()

            #     grafico = plt.savefig("grafico.png",bbox_inches='tight')

            #     st.pyplot(plt)

            #     with open(f"grafico.png", "rb") as file:
            #         st.download_button(
            #                 label="Baixar o gráfico",
            #                 data=file,
            #                 file_name="grafico.png",
            #                 mime="image/png"
            #                 )

            # if rel == 'Ateu':

            #     df.set_index('sigla',inplace = True)

            #     plt.rcParams['figure.figsize'] = (12,7)
            #     plt.title(f"\n Intenção de voto de 'ateus' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
            #     plt.plot(df[(df['nome_instituto']==inst)].lul_ateu_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ateu")
            #     plt.plot(df[(df['nome_instituto']==inst)].lul_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

            #     plt.plot(df[(df['nome_instituto']==inst)].bol_ateu_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ateu")
            #     plt.plot(df[(df['nome_instituto']==inst)].bol_ger_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

            #     plt.plot(df[(df['nome_instituto']==inst)].ciro_ateu_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_ateu")
            #     plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_geral")

            #     plt.style.use('ggplot')
            #     plt.xlabel('mês/ano e instituto de pesquisa')
            #     plt.xticks(rotation=80,fontsize=12)
            #     plt.yticks(fontsize=14)
            #     plt.ylabel('Intenção de voto em %')
            #     plt.rcParams.update({'axes.facecolor':'white'})

            #     plt.grid(color='black', linestyle='-', linewidth=.08)
            #     plt.legend(fontsize=9, loc='best',ncol=3, borderaxespad=0.)

            #     #axes = plt.gca()
            #     #axes.xaxis.grid()

            #     grafico = plt.savefig("grafico.png",bbox_inches='tight')

            #     st.pyplot(plt)

            #     with open(f"grafico.png", "rb") as file:
            #         st.download_button(
            #                 label="Baixar o gráfico",
            #                 data=file,
            #                 file_name="grafico.png",
            #                 mime="image/png"
            #                 )

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

        st.markdown(f"""
        <h7 style='text-align: center; color: black; color:#606060;font-family:arial'>Nota 1: Os gráficos reproduzem os dados divulgados pelos institutos de pesquisa a partir do recorte religioso.</h7>
        """, unsafe_allow_html=True)
    st.markdown("---")


###########################
##rejeição primeiro turno##
###########################

    st.markdown(f"""
        <h3 style='text-align: center; color: #303030; font-family:segoe UI; text-rendering: optimizelegibility;background-color: #FFD662;'>2. Rejeição</h3>
        """, unsafe_allow_html=True)
    st.markdown("---")


    ####################
    ##resumo rejeição###
    ####################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EAE6DA;'>
        Resumo - Rejeição geral e por religião segundo candidato:</h3><br>
        """, unsafe_allow_html=True)

        rej_lula = st.checkbox('Lula ')

        if rej_lula:

            ## coluna 1
            lul = Image.open('lula_perfil.jpg')
            col0, col, col1, col2, col3, col4 = st.columns(6)
            col0.image(lul,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col1.metric(label="Católicos", value=f"{round(list(df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col3.metric(label="Outros", value=f"{round(list(df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col4.metric(label="Sem Religião", value=f"{round(list(df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            #col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            st.markdown("---")

        rej_bolsonaro = st.checkbox('Bolsonaro ')

        if rej_bolsonaro:

            ## coluna 1
            bol = Image.open('bolso_image.jpeg')
            col0,col, col1, col2, col3, col4 = st.columns(6)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col1.metric(label="Católicos", value=f"{round(list(df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col3.metric(label="Outros", value=f"{round(list(df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col4.metric(label="Sem Religião", value=f"{round(list(df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            #col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            st.markdown("---")

        rej_ciro = st.checkbox('Ciro Gomes ')

        if rej_ciro:

            ## coluna 1
            ciro = Image.open('ciro_perfil.jpg')
            col0,col, col1, col2, col3, col4 = st.columns(6)
            col0.image(ciro,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col1.metric(label="Católicos", value=f"{round(list(df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col3.metric(label="Outros", value=f"{round(list(df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            col4.metric(label="Sem Religião", value=f"{round(list(df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            #col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1],1)}%") 
            st.markdown("---")

        st.markdown(f"""
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia <i>{list(df.data)[-1].strftime(format='%d-%m-%Y')}</i></h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da <i>rejeição</i> dos candidatos utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais.</h7><br>
        """, unsafe_allow_html=True)


    st.markdown("---")


    ################################################
    ## gráfico da rejeição geral - primeiro turno###
    ################################################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EAE6DA;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Rejeição geral:</h3><br>
        """, unsafe_allow_html=True)

        rej_vote_med_move = st.checkbox('Selecione para visualizar o gráfico da rejeição')

        if rej_vote_med_move:

            ##import image

            fig = go.Figure()
            
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t, x=df[df['lul_ger_rej_1t']>1].sigla, mode='markers', name='rejeição_geral_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m15).mean(), x=df[df['lul_ger_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_ger_rej_1t']>1].sigla)[-1], y=int(list(df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m15).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t, x=df[df['bol_ger_rej_1t']>1].sigla, mode='markers', name='rejeição_geral_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m15).mean(), x=df[df['bol_ger_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_ger_rej_1t']>1].sigla)[-1], y=int(list(df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m15).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t, x=df[df['ciro_ger_rej_1t']>1].sigla, mode='markers', name='rejeição_geral_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m15).mean(), x=df[df['ciro_ger_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df[df['ciro_ger_rej_1t']>1].sigla)[-1], y=int(list(df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m15).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Rejeição geral dos candidatos à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_pr_pesq", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_datafolha", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.20,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)

            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: *Método utilizado:* média móvel de {m_m15} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da rejeição utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Mesmo com a aplicação da média móvel de 15 dias, o recorte temporal da rejeição geral de Ciro Gomes manteve-se oscilante. Trabalhamos com a hipótese de que a rejeição de Gomes associa-se a inclusão de concorrentes da 3a via como alternativas, espaço disputado por Gomes. Portanto, supomos que a variação da rejeição de Ciro Gomes seja um efeito da inclusão de novas candiaturas, tanto mais da desistência de outros concorrentes.</h7><br>
            """, unsafe_allow_html=True)
        st.markdown("---")


    ###########################
    ## rejeição por religião ##
    ###########################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EAE6DA;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Rejeição por religião:</h3><br>
        """, unsafe_allow_html=True)
        
        relig = st.selectbox('Selecione a religião:',options=['--Escolha a opção--','Católica ', 'Evangélica ', 'Espírita ', 'Outras Religiosidades ', 'Sem Religião ', ])

        if relig == 'Católica ':

            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t, x=df[df['lul_cat_rej_1t']>1].sigla, mode='markers', name='rejeição_cat_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean(), x=df[df['lul_cat_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_cat_rej_1t']>1].sigla)[-1], y=int(list(df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t, x=df[df['bol_cat_rej_1t']>1].sigla, mode='markers', name='rejeição_cat_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean(), x=df[df['bol_cat_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_cat_rej_1t']>1].sigla)[-1], y=int(list(df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t, x=df[df['ciro_cat_rej_1t']>1].sigla, mode='markers', name='rejeição_cat_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean(), x=df[df['ciro_cat_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df[df['ciro_cat_rej_1t']>1].sigla)[-1], y=int(list(df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Rejeição geral de católicos por candidato à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_datafolha", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_futura", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.20,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)

             # info
            st.markdown(f"""
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da rejeição de católicos utilizamos {len(df[df['lul_cat_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Evangélica ':
            
            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t, x=df[df['lul_ev_rej_1t']>1].sigla, mode='markers', name='rejeição_ev_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean(), x=df[df['lul_ev_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_ev_rej_1t']>1].sigla)[-1], y=int(list(df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t, x=df[df['bol_ev_rej_1t']>1].sigla, mode='markers', name='rejeição_ev_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean(), x=df[df['bol_ev_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_ev_rej_1t']>1].sigla)[-1], y=int(list(df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -5,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t, x=df[df['ciro_ev_rej_1t']>1].sigla, mode='markers', name='rejeição_ev_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean(), x=df[df['ciro_ev_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df[df['ciro_ev_rej_1t']>1].sigla)[-1], y=int(list(df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 25,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Rejeição geral de evangélicos por candidato à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_datafolha", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_futura", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.20,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)

             # info
            st.markdown(f"""
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da rejeição de evangélicos utilizamos {len(df[df['lul_ev_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Espírita ':
            
            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t, x=df[df['lul_espi_rej_1t']>1].sigla, mode='markers', name='rejeição_espi_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean(), x=df[df['lul_espi_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_espi_rej_1t']>1].sigla)[-1], y=int(list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t, x=df[df['bol_espi_rej_1t']>1].sigla, mode='markers', name='rejeição_espi_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t.rolling(m_m).mean(), x=df[df['bol_espi_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_espi_rej_1t']>1].sigla)[-1], y=int(list(df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t, x=df[df['ciro_espi_rej_1t']>1].sigla, mode='markers', name='rejeição_espi_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t.rolling(m_m).mean(), x=df[df['ciro_espi_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df[df['ciro_espi_rej_1t']>1].sigla)[-1], y=int(list(df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Rejeição geral de espíritas por candidato à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_datafolha", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_futura", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.20,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)
            
             # info
            st.markdown(f"""
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da rejeição de espíritas utilizamos {len(df[df['lul_espi_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Outras Religiosidades ':
            
            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_out_rej_1t']>1].lul_out_rej_1t, x=df[df['lul_out_rej_1t']>1].sigla, mode='markers', name='rejeição_out_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_out_rej_1t']>1].lul_out_rej_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean(), x=df[df['lul_out_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_out_rej_1t']>1].sigla)[-1], y=int(list(df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_out_rej_1t']>1].bol_out_rej_1t, x=df[df['bol_out_rej_1t']>1].sigla, mode='markers', name='rejeição_out_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_out_rej_1t']>1].bol_out_rej_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean(), x=df[df['bol_out_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_out_rej_1t']>1].sigla)[-1], y=int(list(df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t, x=df[df['ciro_out_rej_1t']>1].sigla, mode='markers', name='rejeição_out_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean(), x=df[df['ciro_out_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df[df['ciro_out_rej_1t']>1].sigla)[-1], y=int(list(df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Rejeição geral de outras religiões por candidato à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_datafolha", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_futura", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.20,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)

             # info
            st.markdown(f"""
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da rejeição de outras religiões utilizamos {len(df[df['lul_out_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            """, unsafe_allow_html=True)
            
        if relig == 'Sem Religião ':
            
            fig = go.Figure()
                    
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_non_rej_1t']>1].lul_non_rej_1t, x=df[df['lul_non_rej_1t']>1].sigla, mode='markers', name='rejeição_non_lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_non_rej_1t']>1].lul_non_rej_1t, #set color equal to a variable
                                    colorscale='peach')))

            fig.add_trace(go.Scatter(y=df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean(), x=df[df['lul_non_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='firebrick', width=2.5)))

            fig.add_annotation(x=list(df[df['lul_non_rej_1t']>1].sigla)[-1], y=int(list(df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_non_rej_1t']>1].bol_non_rej_1t, x=df[df['bol_non_rej_1t']>1].sigla, mode='markers', name='rejeição_non_bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_non_rej_1t']>1].bol_non_rej_1t, #set color equal to a variable
                                    colorscale='ice')))

            fig.add_trace(go.Scatter(y=df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean(), x=df[df['bol_non_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5)))

            fig.add_annotation(x=list(df[df['bol_non_rej_1t']>1].sigla)[-1], y=int(list(df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t, x=df[df['ciro_non_rej_1t']>1].sigla, mode='markers', name='rejeição_non_ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t, #set color equal to a variable
                                    colorscale='Greens')))

            fig.add_trace(go.Scatter(y=df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean(), x=df[df['ciro_non_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5)))

            fig.add_annotation(x=list(df[df['ciro_non_rej_1t']>1].sigla)[-1], y=int(list(df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1000, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Rejeição geral dos sem religião por candidato à presidência - 1º turno<i><br>
            """),
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h",
                font_family="arial",))

            fig.add_annotation(x="mar/22_datafolha", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_futura", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.12,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.20,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig)
            # info
            st.markdown(f"""
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da rejeição dos sem religião utilizamos {len(df[df['lul_non_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            """, unsafe_allow_html=True)
    
    st.markdown("---")


########################################################
## rejeição por religião e candidato segundo instituto##
########################################################

    institutos2 = list(set(df['nome_instituto']))
    institutos2.insert(0, ' --Escolha o instituto-- ')

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EAE6DA;'>
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Rejeição por religião e candidato segundo instituto de pesquisa: </h3><br>
        """, unsafe_allow_html=True)

        col, col1 = st.columns(2)
        with col:
            inst = st.selectbox('Selecione o instituto de pesquisa:',options=institutos2)
        with col1:
            ##dados retirados 'Espírita', 'Umbanda/Candomblé', 'Ateu',
            rel = st.selectbox('Escolha a religião:',options=[' --Escolha a religião-- ',' Católica ', ' Evangélica ', ' Outras Religiosidades ', ' Sem Religião '])

        col1, col2, col3 = st.columns([.5,3,.5])

        with col2:
            if rel == ' Católica ':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Rejeição de 'católicos' para presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_cat_rej_1t, data=df[df['lul_cat_rej_1t']>1], marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_cat")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_rej_1t, data=df[df['lul_ger_rej_1t']>1], marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_cat_rej_1t, data=df[df['bol_cat_rej_1t']>1], marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_cat_rej_1t")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_rej_1t, data=df[df['bol_ger_rej_1t']>1], marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_cat_rej_1t, data=df[df['ciro_cat_rej_1t']>1], marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_cat_rej_1t")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_rej_1t, data=df[df['ciro_ger_rej_1t']>1], marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_rej_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Rejeição em %')
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

            if rel == ' Evangélica ':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Rejeição de 'evangélicos' para presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_ev_rej_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ev")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_rej_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_ev_rej_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ev_rej_1t")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_rej_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_ev_rej_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_ev_rej_1t")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_rej_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_rej_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Rejeição em %')
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

            if rel == ' Outras Religiosidades ':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Rejeição de 'outras religiosidades' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_out_rej_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_outras")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_rej_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_out_rej_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_outras")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_rej_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_out_rej_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_outras")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_rej_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_rej_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Rejeição em %')
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
                
            if rel == ' Sem Religião ':

                df.set_index('sigla',inplace = True)

                plt.rcParams['figure.figsize'] = (12,7)
                plt.title(f"\n Rejeição de 'sem religião' à presidente - {inst.title()} 1º turno" + "\n", fontdict={'fontsize':18})
                plt.plot(df[(df['nome_instituto']==inst)].lul_non_rej_1t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_non")
                plt.plot(df[(df['nome_instituto']==inst)].lul_ger_rej_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].bol_non_rej_1t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_non")
                plt.plot(df[(df['nome_instituto']==inst)].bol_ger_rej_1t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_rej_geral")

                plt.plot(df[(df['nome_instituto']==inst)].ciro_non_rej_1t, data=df, marker='.', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=3, label="ciro_non")
                plt.plot(df[(df['nome_instituto']==inst)].ciro_ger_rej_1t, data=df, marker='.',linestyle='dashed', markerfacecolor='seagreen', markersize=8, color='seagreen', linewidth=1, label="ciro_rej_geral")

                plt.style.use('ggplot')
                plt.xlabel('mês/ano e instituto de pesquisa')
                plt.xticks(rotation=80,fontsize=12)
                plt.yticks(fontsize=14)
                plt.ylabel('Rejeição em %')
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


        st.markdown(f"""
        <h7 style='text-align: center; color: black; color:#606060;font-family:arial'>Nota 1: Os gráficos reproduzem os dados divulgados pelos institutos de pesquisa a partir do recorte religioso.</h7>
        """, unsafe_allow_html=True)
    st.markdown("---")

#################################################
##avaliação ruim e péssima do governo bolsonaro##   FICARÁ BLOQUEADO ATÉ O INÍCIO DAS ELEIÇÕES.
#################################################

#     st.markdown(f"""
#         <h3 style='text-align: center; color: #303030; font-family:segoe UI; text-rendering: optimizelegibility;background-color: #FFD662;'>3. Avaliação do governo Bolsonaro</h3>
#         """, unsafe_allow_html=True)
#     st.markdown("---")

#     ####################
#     ##resumo avaliação##
#     ####################

#     with st.container():
#         st.markdown(f"""
#         <br>
#         <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EDF1FF;'>Resumo - avaliação ruim e péssima geral e por religião: </h3><br>
#         <br>
#         """, unsafe_allow_html=True)


#         adm_bolsonaro = st.checkbox(' Selecione para visualizar os dados da avalização do governo Bolsonaro.')

#         if adm_bolsonaro:

#             ## coluna 1
#             bol = Image.open('bolso_image.jpeg')
#             col0,col, col1, col2, col3, col4 = st.columns(6)
#             col0.image(bol,width=100)
#             col.metric(label="Geral", value=f"{round(list(df[df['ava_gov_bol_GERAL']>1].ava_gov_bol_GERAL.rolling(m_m).mean())[-1],1)}%") 
#             col1.metric(label="Católicos", value=f"{round(list(df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean())[-1],1)}%") 
#             col2.metric(label="Evangélicos", value=f"{round(list(df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean())[-1],1)}%") 
#             col3.metric(label="Outros", value=f"{round(list(df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean())[-1],1)}%") 
#             col4.metric(label="Sem Religião", value=f"{round(list(df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean())[-1],1)}%")
#             #col3.metric(label="Espíritas", value=f"{round(list(df[df['ava_gov_bol_espi']>1].ava_gov_bol_espi.rolling(m_m).mean())[-1],1)}%") 
#             st.markdown(f"""
#             <br>
#             <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
#             <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia <i>{list(df[df['ava_gov_bol_GERAL']>1].data)[-1].strftime(format='%d-%m-%Y')}</i></h7><br>
#             <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para a produção dos dados da <i>aprovação</i> do governo bolsonaro utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais. Destacamos a reprovação por segmento religioso através da soma dos percentuais das respostas 'ruim e péssimo'.</h7><br>
#             <br>
#             """, unsafe_allow_html=True)
#         st.markdown("---")

# ############################
# ###Avaliação por religião###
# ############################

#     with st.container():
#         st.markdown(f"""
#         <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EDF1FF;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
#         <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
#         </svg> Avaliação ruim e péssima por religião:</h3><br>
#         """, unsafe_allow_html=True)

#         aval_vote_med_move = st.checkbox('Selecione para visualizar o gráfico da avaliação do governo Bolsonaro')

#         if aval_vote_med_move:

#             fig = go.Figure()

#             ## católicos

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat, x=df[df['ava_gov_bol_cat']>1].sigla, mode='markers', name='aval_cat',
#                                     marker=dict(
#                                     size=5,
#                                     color=df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat, #set color equal to a variable
#                                     colorscale='peach')))

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean(), x=df[df['ava_gov_bol_cat']>1].sigla, mode='lines', name='católicos',
#                                     line=dict(color='#802b00', width=2.5)))

#             fig.add_annotation(x=list(df[df['ava_gov_bol_cat']>1].sigla)[-1], y=int(list(df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean())[-1])}%",
#                         showarrow=True,
#                         arrowhead=1,
#                         ax = 40, ay = 0,
#                         font=dict(size=20, color="black", family="Arial"))


#             ## evangélicos

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev, x=df[df['ava_gov_bol_ev']>1].sigla, mode='markers', name='aval_ev',
#                                     marker=dict(
#                                     size=5,
#                                     color=df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev, #set color equal to a variable
#                                     colorscale='tropic')))

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean(), x=df[df['ava_gov_bol_ev']>1].sigla,mode='lines', name='evangélicos',
#                                     line=dict(color='#80ccff', width=2.5)))

#             fig.add_annotation(x=list(df[df['ava_gov_bol_ev']>1].sigla)[-1], y=int(list(df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean())[-1])}%",
#                         showarrow=True,
#                         arrowhead=1,
#                         ax = 40, ay = 0,
#                         font=dict(size=20, color="black", family="Arial"))

#             ## outras religiões

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_out']>1].ava_gov_bol_out, x=df[df['ava_gov_bol_out']>1].sigla, mode='markers', name='aval_out',
#                                     marker=dict(
#                                     size=5,
#                                     color=df[df['ava_gov_bol_out']>1].ava_gov_bol_out, #set color equal to a variable
#                                     colorscale='Greens')))

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean(), x=df[df['ava_gov_bol_out']>1].sigla,mode='lines', name='outras religiões',
#                                     line=dict(color='#808080', width=2.5)))

#             fig.add_annotation(x=list(df[df['ava_gov_bol_out']>1].sigla)[-1], y=int(list(df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean())[-1])}%",
#                         showarrow=True,
#                         arrowhead=1,
#                         ax = 40, ay = 0,
#                         font=dict(size=20, color="black", family="Arial"))


#             ## sem religião 

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_non']>1].ava_gov_bol_non, x=df[df['ava_gov_bol_non']>1].sigla, mode='markers', name='aval_sem_religião',
#                                      marker=dict(
#                                      size=5,
#                                      color=df[df['ava_gov_bol_non']>1].ava_gov_bol_non, #set color equal to a variable
#                                      colorscale='Greens')))

#             fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean(), x=df[df['ava_gov_bol_non']>1].sigla,mode='lines', name='aval_sem_religião',
#                                      line=dict(color='seagreen', width=2.5)))

#             fig.add_annotation(x=list(df[df['ava_gov_bol_non']>1].sigla)[-1], y=int(list(df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean())[-1])}%",
#                          showarrow=True,
#                          arrowhead=1,
#                          ax = 40, ay = 0,
#                          font=dict(size=20, color="black", family="Arial"))

#             ## detalhes

#             fig.update_layout(width = 1100, height = 800, template = 'plotly', margin=dict(r=80, l=80, b=4, t=150),
#             title=("""
#             <i>Avaliação negativa de Bolsonaro por religião - 1º turno<i><br>
#             """),
#                             xaxis_title='Mês, ano e instituto de pesquisa',
#                             yaxis_title='Rejeição (%)',
#                             font=dict(family="arial",size=13),
#                             legend=dict(
#                 yanchor="auto",
#                 y=1.1,
#                 xanchor="auto",
#                 x=0.5,
#                 orientation="h",
#                 font_family="arial",))

#             fig.add_annotation(x="mar/22_fsb", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
#             fig.add_annotation(x="mai/22_fsb", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

#             fig.update_xaxes(tickangle = 280,rangeslider_visible=True,title_font_family="Arial")

#             # Add image
#             fig.add_layout_image(
#                 dict(
#                     source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
#                     xref="paper", yref="paper",
#                     x=.99, y=1.12,
#                     sizex=0.1, sizey=0.1,
#                     xanchor="right", yanchor="bottom"
#                 )
#             )

#             # Add image
#             fig.add_layout_image(
#                 dict(
#                     source=agre,
#                     xref="paper", yref="paper",
#                     x=.99, y=1.20,
#                     sizex=0.12, sizey=0.12,
#                     xanchor="right", yanchor="bottom"
#                 )
#             )

#             st.plotly_chart(fig)

            
#             ## info
#         st.markdown(f"""
#         <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
#         <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Para a produção dos gráficos sobre a <i>aprovação</i> do governo bolsonaro utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais. Destacamos a reprovação por segmento religioso através do registro das respostas 'ruim e péssimo'.</h7><br>
#         """, unsafe_allow_html=True)
#         st.markdown("---")


#############################################################################################################################
                                                        ### segundo turno ######
#############################################################################################################################

if options_turn == 'Segundo Turno':

    st.markdown(f"""
        <h2 style='text-align: center; color: #303030; font-family:tahoma; text-rendering: optimizelegibility'>Segundo Turno</h2>
        <br>
        """, unsafe_allow_html=True)
    st.markdown("---")


##################
##resumo#########
#################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'>Resumo - intenção de voto por candidato</h3> \n
        <br>""", unsafe_allow_html=True)

        int_vot_lula = st.checkbox('Lula ')

        if int_vot_lula:
            ## coluna 1
            lul = Image.open('lula_perfil.jpg')
            col0, col, col1, col2, col3, col4, col5 = st.columns(7)
            col0.image(lul,width=105,channels="B")
            col.metric(label="Geral", value=f"{round(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1],1),1)}")
            col2.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Evangélicos", value=f"{round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1),1)}")
            col4.metric(label="Outros", value=f"{round(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1],1),1)}")
            col5.metric(label="Sem Religião", value=f"{round(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1],1),1)}")
            ## coluna 2
            #col4, col5, col6, col7, col8 = st.columns(5)
            #col4.metric(label="",value="")
            # col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1],1),1)}")
            # col6.metric(label="Ateu", value=f"{round(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1],1),1)}")
            # col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1),1)}")
            # ## info
            # st.caption('* Dados na cor verde indicam a vantagem de Lula em relação a Bolsonaro, e vermelho, desvantagem.')
            st.markdown("---")

        int_vot_bolsonaro = st.checkbox('Bolsonaro ')

        if int_vot_bolsonaro:
            ## coluna 1
            bol = Image.open('bolso_image.jpeg')
            col0, col, col1, col2, col3, col4 = st.columns(7)
            col0.image(bol,width=100)
            col.metric(label="Geral", value=f"{round(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1],1),1)}%")
            col1.metric(label="Católicos", value=f"{round(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1],1),1)}")
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1)-round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1),1)}")
            col4.metric(label="Outros", value=f"{round(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1],1),1)}")
            col5.metric(label="Sem Religião", value=f"{round(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1],1),1)}")
            # ## coluna 2
            # col4, col5, col6, col7, col8 = st.columns(5)
            # col4.metric(label="",value="")
            # col5.metric(label="Umbanda/Candomblé", value=f"{round(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1],1),1)}")
            # col6.metric(label="Ateu", value=f"{round(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1],1)}%", delta=f"{round(round(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1],1),1)}")
            # ## info
            # st.caption('* Dados na cor verde indicam a vantagem de Bolsonaro em relação a Lula, e vermelho, desvantagem.')
        st.markdown(f"""
        <br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7> \n
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
        <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo do resumo da média móvel das intenções de voto geral ao segundo turno utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
        """, unsafe_allow_html=True)
    st.markdown("---")


    ################################
    ## Média movel segundo turno###
    ################################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Intenção de voto geral</h3>
        <br>""", unsafe_allow_html=True)

        int_vote_med_move_2t = st.checkbox('Clique para visualizar')

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
                    ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Brancos e Nulos df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t

            fig.add_trace(go.Scatter(y=df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t, x=df[df['bra_nul_ns_nr_ger_2t']>1].sigla, mode='markers', name='brancos_nulos_ns_nr',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t, #set color equal to a variable
                                    colorscale='gray')))

            fig.add_trace(go.Scatter(y=df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t.rolling(m_m).mean(), x=df[df['bra_nul_ns_nr_ger_2t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                    line=dict(color='gray', width=2.5)))

            fig.add_annotation(x=list(df[df['bra_nul_ns_nr_ger_2t']>1].sigla)[-1], y=int(list(df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            fig.update_layout(width = 1000, height = 800, template = 'presentation',
                            title="<i>Média móvel das intenções de voto de candidatos à presidência - 2º turno<i><br>",
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            font=dict(family="arial",size=14),
                            legend=dict(
                yanchor="auto",
                y=1.1,
                xanchor="auto",
                x=0.5,
                orientation="h"))

            fig.add_annotation(x="mar/22_poderdata_3", y=32,text="Moro desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_poderdata_2", y=32,text="Dória desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

            fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
            fig.update_yaxes(range=[0,70])

            st.plotly_chart(fig)
            st.markdown(f"""
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 1: *Método utilizado:* média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral ao segundo turno utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>

            """, unsafe_allow_html=True)
    st.markdown("---")

############################
### intenção de voto média##
############################

    #########################################
    ##intenção de voto por religião 2 truno##
    #########################################

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Intenção de voto por religião:</h3>
        <br>""", unsafe_allow_html=True)
        ## opçoes deletadas 'Espírita ', 'Umbanda/Candomblé ', 'Ateu ',
        relig2t = st.selectbox('Selecione a religião:',options=['--Escolha a opção--','Católica ', 'Evangélica ', 'Sem Religião ', 'Outras Religiosidades '])

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1000, height = 800, template = 'presentation',
                            title="Clique sobre a legenda do gráfico para interagir com os dados <br>",
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            font=dict(family="arial",size=14),
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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))
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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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

    # if relig2t == 'Espírita ':
    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_espi_2t']>1].lul_espi_2t, x=df[df['lul_espi_2t']>1].data, mode='markers', name='int_vot_espi_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_espi_2t']>1].lul_espi_2t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean(), x=df[df['bol_espi_2t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='firebrick', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_espi_2t']>1].data)[-1], y=int(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                   #  ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Bolsonaro
    #     fig.add_trace(go.Scatter(y=df[df['bol_espi_2t']>1].bol_espi_2t, x=df[df['bol_espi_2t']>1].data, mode='markers', name='int_vot_espi_bolsonaro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['bol_espi_2t']>1].lul_espi_2t, #set color equal to a variable
    #                             colorscale='ice')))

    #     fig.add_trace(go.Scatter(y=df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean(), x=df[df['bol_espi_2t']>1].data,mode='lines', name='Bolsonaro',
    #                             line=dict(color='skyblue', width=2.5)))

    #     fig.add_annotation(x=list(df[df['bol_espi_2t']>1].data)[-1], y=int(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     fig.update_layout(width = 1000, height = 800, template = 'none',
    #                     xaxis_title='Mês, ano e instituto de pesquisa',
    #                     yaxis_title='Intenção de voto (%)',
    #                     legend=dict(
    #         yanchor="auto",
    #         y=1.1,
    #         xanchor="auto",
    #         x=0.5,
    #         orientation="h"))

    #     fig.update_xaxes(tickangle = 280,rangeslider_visible=True)

    #     st.plotly_chart(fig)

    # if relig2t == 'Umbanda/Candomblé ':

    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_umb_can_2t']>1].lul_umb_can_2t, x=df[df['lul_umb_can_2t']>1].data, mode='markers', name='int_vot_umb_can_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_umb_can_2t']>1].lul_umb_can_2t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean(), x=df[df['bol_umb_can_2t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='firebrick', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_umb_can_2t']>1].data)[-1], y=int(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                   #  ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Bolsonaro
    #     fig.add_trace(go.Scatter(y=df[df['bol_umb_can_2t']>1].bol_umb_can_2t, x=df[df['bol_umb_can_2t']>1].data, mode='markers', name='int_vot_umb_can_bolsonaro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['bol_umb_can_2t']>1].lul_umb_can_2t, #set color equal to a variable
    #                             colorscale='ice')))

    #     fig.add_trace(go.Scatter(y=df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean(), x=df[df['bol_umb_can_2t']>1].data,mode='lines', name='Bolsonaro',
    #                             line=dict(color='skyblue', width=2.5)))

    #     fig.add_annotation(x=list(df[df['bol_umb_can_2t']>1].data)[-1], y=int(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     fig.update_layout(width = 1000, height = 800, template = 'none',
    #                     xaxis_title='Mês, ano e instituto de pesquisa',
    #                     yaxis_title='Intenção de voto (%)',
    #                     legend=dict(
    #         yanchor="auto",
    #         y=1.1,
    #         xanchor="auto",
    #         x=0.5,
    #         orientation="h"))

    #     fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
    #     st.plotly_chart(fig)

    # if relig2t == 'Ateu ':
    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_2t']>1].lul_ateu_2t, x=df[df['lul_ateu_2t']>1].data, mode='markers', name='int_vot_ateu_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_ateu_2t']>1].lul_ateu_2t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean(), x=df[df['bol_ateu_2t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='firebrick', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_ateu_2t']>1].data)[-1], y=int(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                    # ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     ## Bolsonaro
    #     fig.add_trace(go.Scatter(y=df[df['bol_ateu_2t']>1].bol_ateu_2t, x=df[df['bol_ateu_2t']>1].data, mode='markers', name='int_vot_ateu_bolsonaro',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['bol_ateu_2t']>1].lul_ateu_2t, #set color equal to a variable
    #                             colorscale='ice')))

    #     fig.add_trace(go.Scatter(y=df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean(), x=df[df['bol_ateu_2t']>1].data,mode='lines', name='Bolsonaro',
    #                             line=dict(color='skyblue', width=2.5)))

    #     fig.add_annotation(x=list(df[df['bol_ateu_2t']>1].data)[-1], y=int(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1]),text=f"{int(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1])}%",
    #                 showarrow=True,
    #                 arrowhead=1,
                   #  ax = 40, ay = 0,
    #                 font=dict(size=20, color="black", family="Arial"))

    #     fig.update_layout(width = 1000, height = 800, template = 'none',
    #                     xaxis_title='Mês, ano e instituto de pesquisa',
    #                     yaxis_title='Intenção de voto (%)',
    #                     legend=dict(
    #         yanchor="auto",
    #         y=1.1,
    #         xanchor="auto",
    #         x=0.5,
    #         orientation="h"))

    #     fig.update_xaxes(tickangle = 280,rangeslider_visible=True)
    #     st.plotly_chart(fig)

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

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

        st.caption('**Obs.:** Em alguns casos, a combinção de dados retornará um gráfico em branco. \n Isso indica que instituto de pesquisa selecionado não coletou dados da categoria.')

    st.markdown(f"""
    <h7 style='text-align: left; color: black; color:#606060;font-family:arial'>1) *Método utilizado:* média móvel de {m_m} dias.</h7>
    """, unsafe_allow_html=True)
    st.markdown("---")


    #####################################
    ### dados por instituto de pesquisa##
    #####################################

    institutos = list(set(df['nome_instituto']))
    institutos.insert(0, '--Escolha a opção--')

    with st.container():
        st.markdown(f"""
        <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #e6e6e6;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
        <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
        </svg> Intenção de voto por instituto de pesquisa e religião:</h3> \n
        <br>""", unsafe_allow_html=True)

        col, col1 = st.columns(2)
        with col:
            inst2 = st.selectbox('Selecione o instituto de pesquisa:',options=institutos)
        with col1:
            ##dado retirado 'Espírita', 'Umbanda/Candomblé', 'Ateu',
            rel2 = st.selectbox('Escolha a religião:',options=['--Escolha a opção--','Católica', 'Evangélica', 'Sem Religião', 'Outras Religiosidades'])

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

            # if rel2 == 'Espírita':

            #     df.set_index('sigla',inplace = True)

            #     plt.rcParams['figure.figsize'] = (12,7)
            #     plt.title(f"\n Intenção de voto de 'espírita/kradecista' para presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
            #     plt.plot(df[(df['nome_instituto']==inst2)].lul_espi_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_espi")
            #     plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

            #     plt.plot(df[(df['nome_instituto']==inst2)].bol_espi_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_espi_2t")
            #     plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

            #     plt.style.use('ggplot')
            #     plt.xlabel('mês/ano e instituto de pesquisa')
            #     plt.xticks(rotation=80,fontsize=12)
            #     plt.yticks(fontsize=14)
            #     plt.ylabel('Intenção de voto em %')
            #     plt.rcParams.update({'axes.facecolor':'white'})

            #     plt.grid(color='black', linestyle='-', linewidth=.08)
            #     plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

            #     #axes = plt.gca()
            #     #axes.xaxis.grid()

            #     grafico = plt.savefig("grafico.png",bbox_inches='tight')

            #     st.pyplot(plt)

            #     with open(f"grafico.png", "rb") as file:
            #         st.download_button(
            #                 label="Baixar o gráfico",
            #                 data=file,
            #                 file_name="grafico.png",
            #                 mime="image/png"
            #                 )

            # if rel2 == 'Umbanda/Candomblé':

            #     df.set_index('sigla',inplace = True)

            #     plt.rcParams['figure.figsize'] = (12,7)
            #     plt.title(f"\n Intenção de voto de 'umbandistas e candonblecistas' à presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
            #     plt.plot(df[(df['nome_instituto']==inst2)].lul_umb_can_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_umb_can")
            #     plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

            #     plt.plot(df[(df['nome_instituto']==inst2)].bol_umb_can_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_umb_can")
            #     plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

            #     plt.style.use('ggplot')
            #     plt.xlabel('mês/ano e instituto de pesquisa')
            #     plt.xticks(rotation=80,fontsize=12)
            #     plt.yticks(fontsize=14)
            #     plt.ylabel('Intenção de voto em %')
            #     plt.rcParams.update({'axes.facecolor':'white'})

            #     plt.grid(color='black', linestyle='-', linewidth=.08)
            #     plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

            #     #axes = plt.gca()
            #     #axes.xaxis.grid()

            #     grafico = plt.savefig("grafico.png",bbox_inches='tight')

            #     st.pyplot(plt)

            #     with open(f"grafico.png", "rb") as file:
            #         st.download_button(
            #                 label="Baixar o gráfico",
            #                 data=file,
            #                 file_name="grafico.png",
            #                 mime="image/png"
            #                 )

            # if rel2 == 'Ateu':

            #     df.set_index('sigla',inplace = True)

            #     plt.rcParams['figure.figsize'] = (12,7)
            #     plt.title(f"\n Intenção de voto de 'ateus' à presidente - {inst2.title()} 1º turno" + "\n", fontdict={'fontsize':18})
            #     plt.plot(df[(df['nome_instituto']==inst2)].lul_ateu_2t, data=df, marker='.', markerfacecolor='firebrick', markersize=10, color='red', linewidth=3,alpha=0.6, label="lul_ateu")
            #     plt.plot(df[(df['nome_instituto']==inst2)].lul_ger_2t, data=df, marker='.',linestyle='dashed', markerfacecolor='firebrick', markersize=5, color='red', linewidth=1,alpha=0.6, label="lula_geral")

            #     plt.plot(df[(df['nome_instituto']==inst2)].bol_ateu_2t, data=df, marker='*', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=3, label="bol_ateu")
            #     plt.plot(df[(df['nome_instituto']==inst2)].bol_ger_2t, data=df, marker='*',linestyle='dashed', markerfacecolor='skyblue', markersize=8, color='skyblue', linewidth=1, label="bolsonaro_geral")

            #     plt.style.use('ggplot')
            #     plt.xlabel('mês/ano e instituto de pesquisa')
            #     plt.xticks(rotation=80,fontsize=12)
            #     plt.yticks(fontsize=14)
            #     plt.ylabel('Intenção de voto em %')
            #     plt.rcParams.update({'axes.facecolor':'white'})

            #     plt.grid(color='black', linestyle='-', linewidth=.08)
            #     plt.legend(fontsize=9, loc='best',ncol=2, borderaxespad=0.)

            #     #axes = plt.gca()
            #     #axes.xaxis.grid()

            #     grafico = plt.savefig("grafico.png",bbox_inches='tight')

            #     st.pyplot(plt)

            #     with open(f"grafico.png", "rb") as file:
            #         st.download_button(
            #                 label="Baixar o gráfico",
            #                 data=file,
            #                 file_name="grafico.png",
            #                 mime="image/png"
            #                 )

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
        st.caption(f'Os gráficos exibem os dados brutos divulgados pelos institutos de pesquisa.')

    st.markdown("---")




