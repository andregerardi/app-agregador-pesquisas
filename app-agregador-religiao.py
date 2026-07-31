########################################################################
##configuração da página, texto exibido na aba e dados no item 'about'##
########################################################################

import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import image as image
from PIL import Image
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
         'About': "##### Cientista de dados: Dirceu André Gerardi. \n **E-mail:** andregerardi3@gmail.com"
     }
 )

#####---####3

premium_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&family=Poppins:wght@600;700;800&display=swap');

:root{
  --bg: #F7F6F3;            /* papel quente, estilo editorial */
  --surface: #FFFFFF;
  --ink: #1A1A2E;
  --muted: #6E6E85;
  --primary: #14213D;       /* navy profundo */
  --primary-2: #233A63;
  --accent: #FF6B35;        /* laranja elétrico — remete ao FA7A35 original */
  --accent-2: #00A8CC;      /* ciano — remete ao rgb(0,165,200) original */
  --border: #E9E7E0;
  --shadow-sm: 0 1px 3px rgba(20,33,61,.08), 0 4px 14px rgba(20,33,61,.05);
  --shadow-md: 0 8px 30px rgba(20,33,61,.12);
  --radius: 16px;
}
 
/* ---------- Base ---------- */
html, body, [class*="css"]{
  font-family:'Inter',-apple-system,sans-serif !important;
  color:var(--ink) !important;
}
.stApp{
  background:
    radial-gradient(1200px 500px at 50% -10%, rgba(0,168,204,.07), transparent 60%),
    var(--bg) !important;
}
.block-container{ padding-top:1.4rem !important; padding-bottom:3rem !important; max-width:1250px !important; }
p[style]{ line-height:1.7 !important; }
 
/* ---------- Hero (usa as classes do BLOCO B) ---------- */
.hero{
  background:linear-gradient(135deg, var(--primary) 0%, var(--primary-2) 60%, #2E4A7A 100%);
  border-radius:24px;
  padding:52px 40px 44px 40px;
  text-align:center;
  box-shadow:var(--shadow-md);
  position:relative;
  overflow:hidden;
  margin-bottom:8px;
}
.hero::before{
  content:'';
  position:absolute; inset:0;
  background:
    radial-gradient(600px 200px at 20% 0%, rgba(255,107,53,.18), transparent 60%),
    radial-gradient(500px 220px at 85% 100%, rgba(0,168,204,.20), transparent 60%);
  pointer-events:none;
}
.hero .kicker{
  display:inline-block;
  font-family:'JetBrains Mono',monospace;
  font-size:.72rem; font-weight:700; letter-spacing:.18em;
  text-transform:uppercase;
  color:var(--accent-2);
  background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.15);
  padding:6px 14px; border-radius:999px;
  margin-bottom:18px;
}
.hero h1{
  font-family:'Poppins', sans-serif !important;
  font-weight:800;
  font-size:clamp(1.8rem, 4vw, 2.9rem);
  line-height:1.12;
  color:#fff !important;
  margin:0 0 14px 0;
  letter-spacing:-.02em;
}
.hero .sub{
  color:rgba(255,255,255,.72);
  font-size:1.02rem; font-weight:500;
  max-width:640px; margin:0 auto;
}
.hero .share{ margin-top:26px; }
.hero .share span.lbl{
  display:block; font-size:.72rem; letter-spacing:.14em; text-transform:uppercase;
  color:rgba(255,255,255,.45); margin-bottom:10px;
}
.hero .share a{
  display:inline-flex; align-items:center; justify-content:center;
  width:42px; height:42px; border-radius:12px;
  background:rgba(255,255,255,.09);
  border:1px solid rgba(255,255,255,.16);
  margin:0 5px;
  transition:transform .15s ease, background .15s ease;
}
.hero .share a:hover{ transform:translateY(-3px); background:rgba(255,255,255,.18); }
.hero .share svg{ width:20px; height:20px; }
 
/* ---------- Faixa do seletor de turno (BLOCO C) ---------- */
.turn-band{
  text-align:center;
  margin:6px 0 2px 0;
}
.turn-band .lbl{
  font-family:'JetBrains Mono',monospace;
  font-size:.72rem; font-weight:700; letter-spacing:.18em; text-transform:uppercase;
  color:var(--muted);
}
/* radio horizontal vira "pills" */
div[role="radiogroup"]{
  display:flex !important; justify-content:center; gap:10px; flex-wrap:wrap;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:999px;
  padding:6px;
  width:fit-content; margin:10px auto 0 auto;
  box-shadow:var(--shadow-sm);
}
div[role="radiogroup"] label{
  border-radius:999px !important;
  padding:8px 22px !important;
  margin:0 !important;
  cursor:pointer;
  transition:background .15s ease;
}
div[role="radiogroup"] label:has(input:checked){
  background:var(--primary);
  box-shadow:var(--shadow-sm);
}
div[role="radiogroup"] label:has(input:checked) p{ color:#fff !important; font-weight:700 !important; }
div[role="radiogroup"] label p{ color:var(--ink) !important; font-weight:600 !important; }
div[role="radiogroup"] label > div:first-child{ display:none !important; } /* esconde a bolinha */
 
/* ---------- Títulos de turno (h2 inline) ---------- */
h2[style]{
  font-family:'Fraunces',serif !important;
  font-weight:800 !important;
  font-size:1.9rem !important;
  color:var(--primary) !important;
  background:transparent !important;
  text-align:center !important;
  position:relative;
  padding-bottom:14px !important;
}
h2[style]::after{
  content:'';
  display:block; width:64px; height:4px; border-radius:2px;
  background:linear-gradient(90deg, var(--accent), var(--accent-2));
  margin:12px auto 0 auto;
}
 
/* ---------- Seções numeradas (h3 centrado com fundo #FFD662) ---------- */
h3[style*="FFD662"]{
  background:transparent !important;
  color:var(--primary) !important;
  font-family:'Fraunces',serif !important;
  font-weight:700 !important;
  font-size:1.45rem !important;
  text-align:center !important;
  border:none !important;
  padding:8px 0 !important;
}
 
h3{
  background: var(--surface) !important;
  color: var(--ink) !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 700 !important;
  font-size: 1.05rem !important;
  padding: 15px 20px 15px 22px !important;
  border-radius: var(--radius) !important;
  border: 1px solid var(--border) !important;
  border-left: 4px solid var(--accent) !important;
  box-shadow: var(--shadow-sm) !important;
  margin-top: 1.1rem !important;
}

/* garante que qualquer conteúdo interno não “desapareça” */
h3 *{
  color: inherit !important;
}

/* SVG seguro */
h3 svg{
  fill: var(--accent) !important;
  vertical-align: -6px;
  margin-right: 8px;
  width: 24px;
  height: 22px;
}
 
/* ---------- Banner "Informações sobre o agregador" (h4 laranja) ---------- */
h4[style*="background-color"]{
  background:var(--primary) !important;
  color:#fff !important;
  font-family:'Inter',sans-serif !important;
  font-weight:700 !important;
  font-size:1rem !important;
  letter-spacing:.02em;
  padding:15px 22px !important;
  border-radius:var(--radius) !important;
  box-shadow:var(--shadow-sm) !important;
  border-left:4px solid var(--accent) !important;
}
h4[style*="background-color"] b{ color:#fff !important; }
 
/* ---------- h6 das estatísticas ---------- */
h6[style]{
  font-family:'JetBrains Mono',monospace !important;
  font-size:.72rem !important;
  font-weight:700 !important;
  letter-spacing:.1em; text-transform:uppercase;
  color:var(--accent-2) !important;
  border:none !important;
}
 
/* ---------- Notas <h7> ---------- */
h7[style]{
  display:block !important;
  font-size:.78rem !important;
  line-height:1.5rem !important;
  color:var(--muted) !important;
  border-left:2px solid var(--border) !important;
  padding-left:10px !important;
}
 
/* ---------- st.metric: cards ---------- */
[data-testid="stMetric"]{
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--radius);
  padding:16px 8px;
  box-shadow:var(--shadow-sm);
  text-align:center;
  transition:transform .15s ease, box-shadow .15s ease, border-color .15s ease;
}
[data-testid="stMetric"]:hover{
  transform:translateY(-3px);
  box-shadow:var(--shadow-md);
  border-color:var(--accent);
}
[data-testid="stMetricLabel"]{
  color:var(--muted) !important;
  font-size:.72rem !important; font-weight:700 !important;
  letter-spacing:.08em; text-transform:uppercase;
}
[data-testid="stMetricValue"]{
  font-family:'Fraunces',serif !important;
  font-weight:800 !important;
  color:var(--primary) !important;
}
 
/* ---------- Fotos dos candidatos: circulares ---------- */
[data-testid="stImage"] img{
  border-radius:50% !important;
  border:3px solid var(--surface);
  box-shadow:var(--shadow-sm);
}
 
/* ---------- Expanders ---------- */
details{
  background:var(--surface) !important;
  border:1px solid var(--border) !important;
  border-radius:var(--radius) !important;
  box-shadow:var(--shadow-sm) !important;
  overflow:hidden;
}
summary{ font-weight:600 !important; color:var(--primary) !important; }
summary:hover{ color:var(--accent) !important; }
 
/* ---------- Checkbox ---------- */
[data-testid="stCheckbox"] label p{ font-weight:600 !important; color:var(--primary) !important; }
 
/* ---------- Selectbox ---------- */
[data-testid="stSelectbox"] > div > div{
  border-radius:12px !important;
  border:1px solid var(--border) !important;
  background:var(--surface) !important;
  box-shadow:var(--shadow-sm) !important;
}
 
/* ---------- DataFrame / download ---------- */
[data-testid="stDataFrame"]{ border-radius:var(--radius) !important; overflow:hidden !important; box-shadow:var(--shadow-sm) !important; }
[data-testid="stDownloadButton"] button{
  background:var(--primary) !important; color:#fff !important;
  border:none !important; border-radius:12px !important; font-weight:600 !important;
}
[data-testid="stDownloadButton"] button:hover{ background:var(--accent) !important; }
 
/* ---------- Gráficos Plotly: moldura de card ---------- */
[data-testid="stPlotlyChart"]{
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--radius);
  padding:10px;
  box-shadow:var(--shadow-sm);
}
 
/* ---------- Divisórias ---------- */
hr{ border:none !important; border-top:1px solid var(--border) !important; margin:2rem 0 !important; }
 
/* ---------- Caption final ---------- */
[data-testid="stCaptionContainer"]{ color:var(--muted) !important; text-align:center !important; }

@media (prefers-color-scheme: dark) {
  :root{
    --bg: #0E1117;
    --surface: #1A1D24;
    --ink: #E6E6E6;
    --muted: #A0A0B2;
    --primary: #E6E6E6;
    --border: #2A2E39;
  }
}
</style>
"""
st.markdown(premium_css, unsafe_allow_html=True)
 
#####---####3

st.markdown("""
     <div class="hero">
       <span class="kicker">Eleições Nacionais</span>
       <h1>Agregador de pesquisas eleitorais<br>por religião</h1>
       <p class="sub">Consolidação das pesquisas de intenção de voto e rejeição para as eleições presidenciais de 2022, com recorte por segmento religioso.</p>
       <div class="share">
         <span class="lbl">Compartilhe</span>
         <a href="https://www.facebook.com/sharer/sharer.php?u=https://cebrap.org.br/agregador-de-pesquisas-eleitorais-por-religiao/" title="Facebook" rel="nofollow noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 42 42"><path d="M17.78 27.5V17.008h3.522l.527-4.09h-4.05v-2.61c0-1.182.33-1.99 2.023-1.99h2.166V4.66c-.375-.05-1.66-.16-3.155-.16-3.123 0-5.26 1.905-5.26 5.405v3.016h-3.53v4.09h3.53V27.5h4.223z" fill="#fff"></path></svg></a>
         <a href="https://twitter.com/intent/tweet?text=Agregador de Pesquisas Eleitorais por religião&url=https://cebrap.org.br/agregador-de-pesquisas-eleitorais-por-religiao&hashtags=Agregador,religião,eleições2022,datascience" title="Twitter" rel="nofollow noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 39 39"><path d="M28 8.557a9.913 9.913 0 0 1-2.828.775 4.93 4.93 0 0 0 2.166-2.725 9.738 9.738 0 0 1-3.13 1.194 4.92 4.92 0 0 0-3.593-1.55 4.924 4.924 0 0 0-4.794 6.049c-4.09-.21-7.72-2.17-10.15-5.15a4.942 4.942 0 0 0-.665 2.477c0 1.71.87 3.214 2.19 4.1a4.968 4.968 0 0 1-2.23-.616v.06c0 2.39 1.7 4.38 3.952 4.83-.414.115-.85.174-1.297.174-.318 0-.626-.03-.928-.086a4.935 4.935 0 0 0 4.6 3.42 9.893 9.893 0 0 1-6.114 2.107c-.398 0-.79-.023-1.175-.068a13.953 13.953 0 0 0 7.55 2.213c9.056 0 14.01-7.507 14.01-14.013 0-.213-.005-.426-.015-.637.96-.695 1.795-1.56 2.455-2.55z" fill="#fff"></path></svg></a>
         <a href="https://api.whatsapp.com/send?text=Agregador de Pesquisas Eleitorais por religião - https://cebrap.org.br/agregador-de-pesquisas-eleitorais-por-religiao/" title="WhatsApp" rel="nofollow noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -5 40 40"><path stroke="#fff" stroke-width="2" fill="none" d="M 11.579798566743314 24.396926207859085 A 10 10 0 1 0 6.808479557110079 20.73576436351046"></path><path d="M 7 19 l -1 6 l 6 -1" stroke="#fff" stroke-width="2" fill="none"></path><path d="M 10 10 q -1 8 8 11 c 5 -1 0 -6 -1 -3 q -4 -3 -5 -5 c 4 -2 -1 -5 -1 -4" fill="#fff"></path></svg></a>
       </div>
     </div>""", unsafe_allow_html=True)

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
start_date = dt.datetime(2022,8,16) # data de oito meses atras

### dados pesquisas
## retirei do banco as pesquisas da 'prpesquisas' em função dos questionamentos públicos quanto ao método

##import image logo
@st.cache_data(persist=True)
def load_image():
    agre = Image.open('palacio-da-alvorada-interior-black-so-agregador-branco.jpg')
    return agre
agre = load_image()

@st.cache_data(persist=True)
def load_dados():
    ## importa o banco
    banco =  pd.read_excel(r'resultados_pesquisas_lula_bolsonaro_religião.xlsx')
    ## lista de instituições a se considerar no banco (retirei 'prpesquisas')
    list_of_institutions = ['fsb','futura','mda','voxpopuli','quaest','ipec','poderdata','datafolha','idea','ipespe']
    ## retorna o banco filtrado
    df = banco.query('nome_instituto in @list_of_institutions')
    ## resseta o index
    df = df.reset_index(drop=True)
    return df
df = load_dados()


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
        expander = st.expander('Descubra aqui como o agregador foi construído',)
        expander.markdown(f"""
        <!DOCTYPE html>
        <html>
        <body>

        <p style='text-align: center; font-family:Segoe UI;'><b>Explicação:</b></p>
        
        <p style='text-align: justify; font-family:Segoe UI;'>1. O banco de dados é atualizado constantemente com informações sobre a intenção de voto e a rejeição dos candidatos por religião.</p>
        <p style='text-align: justify; font-family:Segoe UI;'>2. Os institutos de pesquisa consultados são: { ', '.join(set(df['nome_instituto'])).title().replace('Mda','MDA').replace('Fsb','FSB').replace('Idea','Idea Big Data').replace('Voxpopuli','Vox Populi').replace('poderdata','Poder Data').replace('Prpesquisas','Paraná Pesquisas')};</p>
        <p style='text-align: justify; font-family:Segoe UI;'>3. O agregador de pesquisas por religião compila os dados de levantamentos nacionais realizados pelos institutos. Para as eleições de 2022 e 2026 os dados foram coletados a partir de janeiro;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>4. O agregador permite também a pesquisa por Instituto separadamente. Não nos responsabilizamos pelas amostras ou técnicas utilizadas pelos diversos institutos;</p> 
        <p style='text-align: justify; font-family:Segoe UI;'>5. Para a composição do banco de dados são consideradas apenas pesquisas nacionais, bem como informações dos candidatos no primeiro e no segundo turnos das eleições presidenciais.</p>
        <p style='text-align: justify; font-family:Segoe UI;'>6. Devido à irregularidade na coleta e ao tamanho da amostra, dados referentes a segmentos demograficamente minoritários tal como candomblé/umbanda e outros apresentam margens de erro maiores, uma vez que a amostra destas religiões não é representativa do conjunto da população brasileira. Assim, quando possível, decidiu-se incluí-las na categoria "Outras religiosidades". Os institutos de pesquisa não divulgaram as intenções de voto da categoria espíritas no segundo das eleições, por esse motivo não há gráficos do segmento;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>7. Vale destacar que os dados censitários, principais referências para a construção da amostragem das pesquisas, estão defasados. Os valores de amostragem variam conforme os critérios próprios de cada instituto de pesquisa. Os institutos em 2022 utilizara dados o IBGE de 2010, da PNAD de 2021 e 2022 e do TSE. As informações de corte religioso nem sempre estão disponíveis nas pesquisas compartilhadas publicamente ou não constam nos documentos registrados no sistema <a href="https://www.tse.jus.br/eleicoes/pesquisa-eleitorais/consulta-as-pesquisas-registradas">PesqeEle</a> matido pelo do TSE, dado que não é obrigatório, segundo o artigo 33 da <a href="https://www.tse.jus.br/legislacao/codigo-eleitoral/lei-das-eleicoes/sumario-lei-das-eleicoes-lei-nb0-9.504-de-30-de-setembro-de-1997">Lei nº 9.504/1997</a>. Para termos uma noção do universo amostrado pelos institutos: os <i>católicos</i> variaram entre {int(df['am_cat'].agg('min'))}% e {int(df['am_cat'].agg('max'))}% dos entrevistados; os <i>evangélicos</i>, entre {int(df['am_ev'].agg('min'))}% e {int(df['am_ev'].agg('max'))}%; os <i>espíritas</i>, entre {int(df['am_espi'].agg('min'))}% e {int(df['am_espi'].agg('max'))}%; o <i>candomblé/umbanda</i>, entre {int(df['am_umb_can'].agg('min'))}% e {int(df['am_umb_can'].agg('max'))}%; <i>"outras religiosidades</i>, entre {int(df['am_out'].agg('min'))}% e {int(df['am_out'].agg('max'))}%; os <i>sem religião</i>, entre {int(df['am_non'].agg('min'))}% e {int(df['am_non'].agg('max'))}%; e <i>os ateus</i>, entre {int(df['am_ateu'].agg('min'))}% e {int(df['am_ateu'].agg('max'))}%.</p>
        <p style='text-align: justify; font-family:Segoe UI;'>8. Em relação às pesquisas, considerou-se a última data quando os entrevistadores colheram as respostas e não a data da divulgação, que por interesses diversos, podem ser adiadas por semanas;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>9. Partindo da data da última coleta das pesquisas, calculou-se a média móvel de diversas variáveis correspondendo a {m_m} dias. Para o caso da rejeição geral utilizou-se a média móvel de {m_m15} dias;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>10. Para obter a média móvel foram usados dados de uma série temporal e aplicado o seguinte código Python <code>rolling().mean()</code>. Uma explicação detalhada da utilização deste código pode ser <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html">vista aqui</a>;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>11. Ao calcular a média móvel de {m_m} dias, por exemplo, os {m_m} primeiros resultados são omitidos da série temporal e não aparecem nos gráficos. O objetivo principal da aplicação deste método é reduzir as oscilações no intuito de deixar as linhas dos gráficos mais fluídas. Exitem algumas técnicas estatíticas que reduzem o ruído dos dados da série temporal, tais como <i>weighted moving average, kernel smoother</i>, entre outras;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>12. O resumo das médias móveis apresentado no primeiro e no segundo turnos considera e mostra o último valor da média obtida para cada candidato. O dado é atualizado automaticamente à medida que novas pesquisas são inseridas no banco de dados;</p>
        <p style='text-align: justify; font-family:Segoe UI;'>13. Para deixar os gráficos limpos optou-se por não inserir a margem de erro na linha da média móvel. Nos recortes por religião a margem de erro nas eleições de 2022 variou entre 2% até 8,5%, de acordo com os institutos. Uma lista com as informações amostrais de cada pesquisa, por eleição, incluindo a margem de erro, pode ser obtida no item "pesquisas eleitorais utilizadas";</p>
        <p style='text-align: justify; font-family:Segoe UI;'>14. As imagens dos candidatos utilizadas provêm das seguintes fontes: <a href="https://oglobo.globo.com/epoca/o-que-dizem-os-autores-dos-programas-dos-presidenciaveis-sobre-combate-as-mudancas-climaticas-23128520">Ciro Gomes</a>, <a href="https://www.dw.com/pt-br/o-brasil-na-imprensa-alem%C3%A3-29-05/a-48968730/">Lula</a>, <a href="https://www.poder360.com.br/poderdata/poderdata-lula-tem-50-contra-40-de-bolsonaro-no-2o-turno/">Bolsonaro</a>.</p>

        </body>
        </html>
        """,unsafe_allow_html=True)

        ### lista de pesquisas
        expander3 = st.expander("Verifique as pesquisas eleitorais utilizadas")
        expander3.write("""#### Lista de pesquisas""")
        lista = df[['nome_instituto', 'data', 'registro_tse','entrevistados', 'margem_erro', 'confiança', 'tipo_coleta']]
        lista = lista.fillna(0).astype({'nome_instituto': 'str', 
                                        
                                        'registro_tse': 'str', 
                                        'entrevistados':'int',
                                        'margem_erro':'str',
                                        'confiança':'int', 
                                        'tipo_coleta':'str'})
        expander3.dataframe(lista)

        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=None).encode('utf-8-sig')

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
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Institutos analisados:</h6> <p style='text-align: center';>{ ', '.join(set(df['nome_instituto'])).title().replace('Mda','MDA').replace('Fsb','FSB').replace('Idea','Idea Big Data').replace('Voxpopuli','Vox Populi').replace('poderdata','Poder Data')}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Institutos por tipo de sondagem:</h6> <p style='text-align: center';>
                <i>Telefone:</i> {', '.join(set(df[df['tipo_coleta']=='telefone'].nome_instituto)).title().replace('Mda','MDA').replace('Fsb','FSB').replace('Idea','Idea Big Data').replace('Voxpopuli','Vox Populi').replace('Prpesquisas','Paraná Pesquisas')}<br>
                <br><i>Presencial:</i> {', '.join(set(df[df['tipo_coleta']=='presencial'].nome_instituto)).title().replace('Mda','MDA').replace('Fsb','FSB').replace('Idea','Idea Big Data').replace('Voxpopuli','Vox Populi').replace('Prpesquisas','Paraná Pesquisas')}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Total de pesquisas mapeadas:</h6> 
            <p style='color:#000000;font-weight:700;font-size:18px;text-align: center';>
            {len(df)-1}<br>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Número de pesquisas segundo método de coleta:</h6><p style='text-align: center';>
                Telefone: {df[df['tipo_coleta'] == 'telefone'].shape[0]}
                <br>Presencial: {df[df['tipo_coleta']=='presencial'].tipo_coleta.value_counts()[0]}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Contador de pesquisas para dados gerais:</h6> 
            <p style='color:#000000;font-weight:700;font-size:18px;text-align: center';>
            1º turno: {len(df[df['lul_ger_1t']>=1])}<br>
            2º turno: {len(df[df['lul_ger_2t']>=1])}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Contador de pesquisas com perguntas sobre religião:</h6> 
            <p style='color:#000000;font-weight:700;font-size:18px;text-align: center';>
            1º turno: {len(df[df['lul_cat_1t']>=1])}<br>
            2º turno: {len(df[df['lul_cat_2t']>=1])}</p>
            <h6 style='text-align: center; color: rgb(37, 117, 232);font-family:Segoe UI;'>Total de pesquisas com amostra sobre religião:</h6><p style='text-align: center';>
            Católicos e evangélicos: {len(df[df['lul_cat_1t']>=1])}
            <br>Espíritas: {len(df[df['lul_espi_1t']>=1])}
            <br>Outras religiões: {len(df[df['lul_out_1t']>=1])}
            <br>Sem religião: {len(df[df['lul_non_1t']>=1])}
            </p>
        """, unsafe_allow_html=True)

        ### Como citar o agregador ####
    with col2:
        expander2 = st.expander("Veja como citar o agregador")
        expander2.markdown(f"""
        <p style='text-align: center; font-family:Segoe UI;'>GERARDI, Dirceu André; ALMEIDA, Ronaldo de. <b>Agregador de pesquisas eleitorais por religião</b>: consolidação de dados de pesquisas eleitorais com recorte religioso às eleições presidenciais de 2022. APP versão 1.0. São Paulo, 2022. Disponível em: https://cebrap.org.br/projetos/. Acesso em: 00/00/000.</p>
        """, unsafe_allow_html=True)

    with col3:
        expander5 = st.expander("Sobre nós")
        expander5.markdown(f"""
        <h6 style='text-align: center; color: #41AF50;'>Projeto vinclulado ao <br> Núcleo de Religiões no Mundo Contemporâneo (Cebrap)<br>
        <br>Laboratório de Antroplogia da Religião (LAR/Unicanp)<br>
        <h6 style='text-align: center; color: #54595F;'>Coordenação:</h6><p style='text-align: center;'>Dirceu André Gerardi<br>(FGV LAW/FGV PROJETOS/CEBRAP)<br><a href="mailto: andregerardi3@gmail.com">email<br></a><br>Ronaldo de Almeida<br>(UNICAMP/CEBRAP/LAR)<br><a href="mailto: ronaldormalmeida@gmail.com">email</a></p></p>
        """, unsafe_allow_html=True)
    st.markdown("---")

########################################################################
######## ELEIÇÕES 2026 - CARGA DE DADOS E FUNÇÕES DE VISUALIZAÇÃO ######
########################################################################

## ---------------------------------------------------------------------
## 1) Configurações do banco de 2026
## ---------------------------------------------------------------------
## arquivo local (deve ficar na mesma pasta do app)
ARQUIVO_2026 = 'agregador-pesquisas-eleitorais-2026-final.xlsx'

## planilha do Google aberta para edição (usada primeiro, quando acessível).
## Se a leitura on-line falhar, o app carrega automaticamente o arquivo local acima.
URL_2026 = 'https://docs.google.com/spreadsheets/d/1XrwMEJYBt5-l7U8S6sUUBU80sd1xQqlA/export?format=xlsx'

## institutos excluídos do banco de 2026 (mesmo critério adotado em 2022)
INSTITUTOS_FORA_2026 = ['prpesquisas']

## candidatos de 2026: Ciro Gomes foi suprimido; entram Caiado, Zema e Renan.
## Para alterar o nome exibido, a cor da linha ou a escala dos pontos, edite aqui.
CAND_2026 = {
    'lul':    {'nome': 'Lula',           'cor': 'rgba(215, 0, 0, 0.8)', 'escala': 'peach'},
    'bol':    {'nome': 'Bolsonaro',      'cor': 'royalblue',            'escala': 'ice'},
    'caiado': {'nome': 'Ronaldo Caiado', 'cor': '#FF6B35',              'escala': 'Oranges'},
    'zema':   {'nome': 'Romeu Zema',     'cor': 'seagreen',             'escala': 'Greens'},
    'renan':  {'nome': 'Renan',          'cor': '#7B4FBF',              'escala': 'Purples'},
}

## segmentos religiosos (sufixos das colunas da planilha)
SEG_2026 = {
    'ger':     'Geral',
    'cat':     'Católicos',
    'ev':      'Evangélicos',
    'espi':    'Espíritas',
    'umb_can': 'Umbanda/Candomblé',
    'out':     'Outras religiosidades',
    'non':     'Sem religião',
    'ateu':    'Ateus',
}

## imagens de perfil (opcionais). Basta acrescentar o arquivo na pasta e mapear aqui.
IMG_2026 = {
    'lul': 'lula_perfil.jpg',
    'bol': 'bolso_image.jpeg',
}


@st.cache_data(ttl=600, show_spinner='Carregando os dados das eleições de 2026...')
def load_dados_2026():
    """Carrega o banco de 2026 (Google Sheets com fallback para o arquivo local)."""
    origem = 'planilha do Google'
    try:
        banco = pd.read_excel(URL_2026)
    except Exception:
        banco = pd.read_excel(ARQUIVO_2026)
        origem = 'arquivo local'

    banco.columns = [str(c).strip() for c in banco.columns]

    if 'nome_instituto' in banco.columns:
        banco['nome_instituto'] = banco['nome_instituto'].astype(str).str.strip().str.lower()
        banco = banco[~banco['nome_instituto'].isin(INSTITUTOS_FORA_2026)]

    if 'data' in banco.columns:
        banco['data'] = pd.to_datetime(banco['data'], errors='coerce')
        banco = banco.sort_values('data')

    banco = banco.reset_index(drop=True)
    return banco, origem


## ---------------------------------------------------------------------
## 2) Funções auxiliares (tolerantes a colunas vazias/ausentes)
## ---------------------------------------------------------------------
def tem_dados_2026(dfx, col):
    """True quando a coluna existe e possui ao menos um valor numérico maior que 1."""
    if col not in dfx.columns:
        return False
    return (pd.to_numeric(dfx[col], errors='coerce') > 1).sum() > 0


def serie_2026(dfx, col):
    """Devolve (eixo x, série y) apenas com as pesquisas que coletaram o dado."""
    y = pd.to_numeric(dfx[col], errors='coerce')
    mask = y > 1
    return dfx.loc[mask, 'sigla'], y[mask]


def mm_2026(y):
    """Média móvel de m_m pesquisas. min_periods=1 evita série vazia enquanto o banco é pequeno."""
    return y.rolling(m_m, min_periods=1).mean()


def ultimo_valor_2026(dfx, col):
    """Última média móvel registrada para a coluna (ou None, se não houver dado)."""
    if not tem_dados_2026(dfx, col):
        return None
    _, y = serie_2026(dfx, col)
    if len(y) == 0:
        return None
    return round(float(mm_2026(y).iloc[-1]), 1)


def candidatos_com_dados_2026(dfx, sufixo):
    """Lista de prefixos de candidatos que possuem dados para o sufixo informado."""
    return [p for p in CAND_2026 if tem_dados_2026(dfx, f'{p}_{sufixo}')]


def religioes_disponiveis_2026(dfx, molde):
    """Religiões com dados; 'molde' é uma string com {seg}, ex.: '{seg}_1t'."""
    disponiveis = []
    for seg, rotulo in SEG_2026.items():
        if seg == 'ger':
            continue
        if any(tem_dados_2026(dfx, f'{p}_' + molde.format(seg=seg)) for p in CAND_2026):
            disponiveis.append(rotulo)
    return disponiveis


def seg_por_rotulo_2026(rotulo):
    for seg, nome in SEG_2026.items():
        if nome == rotulo:
            return seg
    return None


def marca_dagua_2026(fig, y_logo=1.05, y_agre=1.05, x_logo=.99, x_agre=.87):
    fig.add_layout_image(dict(
        source='https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png',
        xref='paper', yref='paper', x=x_logo, y=y_logo,
        sizex=0.1, sizey=0.1, xanchor='right', yanchor='bottom'))
    fig.add_layout_image(dict(
        source=agre, xref='paper', yref='paper', x=x_agre, y=y_agre,
        sizex=0.12, sizey=0.12, xanchor='right', yanchor='bottom'))
    return fig


## ---------------------------------------------------------------------
## 3) Blocos visuais reaproveitáveis
## ---------------------------------------------------------------------
def resumo_2026(dfx, turno='1t', rejeicao=False):
    """Métricas (geral e por religião) de cada candidato, exibidas em checkbox."""
    sufixo_final = f'rej_{turno}' if rejeicao else turno

    for pref, cfg in CAND_2026.items():
        disponiveis = [(rotulo, f'{pref}_{seg}_{sufixo_final}')
                       for seg, rotulo in SEG_2026.items()
                       if tem_dados_2026(dfx, f'{pref}_{seg}_{sufixo_final}')]
        if not disponiveis:
            continue

        chave = f'chk_2026_{pref}_{sufixo_final}'
        if not st.checkbox(cfg['nome'], key=chave):
            continue

        colunas = st.columns(len(disponiveis) + 1)

        ## imagem do candidato (quando houver arquivo disponível)
        try:
            colunas[0].image(Image.open(IMG_2026[pref]), width=100)
        except Exception:
            colunas[0].markdown(
                f"<p style='font-family:Segoe UI;font-weight:700;color:#303030;'>{cfg['nome']}</p>",
                unsafe_allow_html=True)

        for i, (rotulo, col) in enumerate(disponiveis, start=1):
            valor = ultimo_valor_2026(dfx, col)
            colunas[i].metric(label=rotulo, value=f'{valor}%' if valor is not None else '—')
        st.markdown('---')


def grafico_linhas_2026(dfx, sufixo, titulo, y_max=70, col_bra_nulo=None, nota_extra=''):
    """Gráfico de média móvel com todos os candidatos que possuem dados para o sufixo."""
    presentes = candidatos_com_dados_2026(dfx, sufixo)
    if not presentes:
        st.info('Ainda não há pesquisas com esse recorte no banco de 2026.')
        return

    fig = go.Figure()
    rank = 1
    for pref in presentes:
        cfg = CAND_2026[pref]
        x, y = serie_2026(dfx, f'{pref}_{sufixo}')
        media = mm_2026(y)

        fig.add_trace(go.Scatter(
            x=x, y=y, mode='markers', name=f"Pesquisas - {cfg['nome']}",
            marker=dict(size=6, color=y, colorscale=cfg['escala']), legendrank=rank + 1))

        fig.add_trace(go.Scatter(
            x=x, y=media, mode='lines+markers', name=cfg['nome'],
            line=dict(color=cfg['cor'], width=2.5), legendrank=rank))

        fig.add_annotation(
            x=list(x)[-1], y=float(media.iloc[-1]),
            text=f'{media.iloc[-1]:.0f}%', showarrow=True, arrowhead=1, ax=40, ay=0,
            font=dict(size=18, color='black', family='Arial'))
        rank += 2

    if col_bra_nulo and tem_dados_2026(dfx, col_bra_nulo):
        x, y = serie_2026(dfx, col_bra_nulo)
        fig.add_trace(go.Scatter(
            x=x, y=y, mode='markers', name='Pesquisas - brancos, nulos, NS e NR',
            marker=dict(size=6, color=y, colorscale='Greys'), legendrank=rank + 1))
        fig.add_trace(go.Scatter(
            x=x, y=mm_2026(y), mode='lines+markers', name='Brancos, nulos, NS e NR',
            line=dict(color='grey', width=2.5), legendrank=rank))

    fig.update_layout(
        autosize=True, width=1100, height=800, template='plotly_white+xgridoff',
        margin=dict(r=80, l=80, b=2, t=160),
        title=f'<i>{titulo}<i>',
        plot_bgcolor='rgb(255, 255, 255)', paper_bgcolor='rgb(255, 255, 255)',
        xaxis_title='Mês, ano e instituto de pesquisa',
        yaxis_title='Intenção de voto (%)',
        font=dict(family='arial', size=13),
        legend=dict(yanchor='auto', y=1.10, xanchor='auto', x=0.35,
                    orientation='h', font_family='arial'))
    fig.update_xaxes(tickangle=300, rangeslider_visible=False, title_font_family='Arial')
    fig.update_yaxes(range=[0, y_max])
    marca_dagua_2026(fig)

    st.plotly_chart(fig, use_container_width=True)

    ultima_data = pd.to_datetime(dfx['data']).dropna()
    ultima_data = ultima_data.iloc[-1].strftime('%d-%m-%Y') if len(ultima_data) else 's/d'
    st.markdown(f"""
    <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: método utilizado: média móvel de {m_m} pesquisas.</h7><br>
    <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: os valores indicados no gráfico correspondem à última média da série temporal, registrada em {ultima_data}.</h7><br>
    <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: enquanto o banco de 2026 é pequeno, a média móvel é calculada com as pesquisas disponíveis.</h7><br>
    {nota_extra}
    """, unsafe_allow_html=True)


def grafico_instituto_2026(dfx, instituto, seg, turno):
    """Compara, por instituto, o resultado geral e o do segmento religioso escolhido."""
    fonte = dfx[dfx['nome_instituto'] == instituto]
    rotulo = SEG_2026.get(seg, seg)

    fig = go.Figure()
    plotou = False
    rank = 1
    for pref, cfg in CAND_2026.items():
        col_rel = f'{pref}_{seg}_{turno}'
        col_ger = f'{pref}_ger_{turno}'
        if not tem_dados_2026(fonte, col_rel):
            continue
        plotou = True
        fig.add_trace(go.Scatter(
            x=fonte['sigla'], y=pd.to_numeric(fonte[col_rel], errors='coerce'),
            mode='lines+markers', name=f"{cfg['nome']} - {rotulo.lower()}",
            line=dict(color=cfg['cor'], width=2.5), legendrank=rank))
        if tem_dados_2026(fonte, col_ger):
            fig.add_trace(go.Scatter(
                x=fonte['sigla'], y=pd.to_numeric(fonte[col_ger], errors='coerce'),
                mode='lines+markers', name=f"{cfg['nome']} - geral",
                line=dict(color=cfg['cor'], width=1, dash='dot'), legendrank=rank + 1))
        rank += 2

    if not plotou:
        st.info(f'O instituto {instituto.title()} não divulgou dados de {rotulo.lower()} nesse turno.')
        return

    fig.update_layout(
        width=800, height=800, template='plotly_white+xgridoff',
        margin=dict(r=70, l=80, b=4, t=160),
        title=f"Intenção de voto 'geral' e de '{rotulo.lower()}' por candidato segundo '{instituto.title()}'",
        plot_bgcolor='rgb(255, 255, 255)', paper_bgcolor='rgb(255, 255, 255)',
        xaxis_title='Mês, ano e instituto de pesquisa',
        yaxis_title='Intenção de voto (%)',
        font=dict(family='arial', size=13),
        legend=dict(yanchor='auto', y=1.13, xanchor='auto', x=0.35,
                    orientation='h', font_family='arial'))
    fig.update_xaxes(tickangle=300, title_font_family='arial')
    fig.update_yaxes(range=[0, 70])
    marca_dagua_2026(fig, y_logo=1.03, y_agre=1.08, x_logo=1.05, x_agre=1.05)

    st.plotly_chart(fig, use_container_width=True)


def cabecalho_2026(texto, cor='#e6e6e6', alinhamento='left'):
    st.markdown(f"""
    <h3 style='text-align: {alinhamento}; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: {cor};'>{texto}</h3><br>
    """, unsafe_allow_html=True)


## ---------------------------------------------------------------------
## 4) Página completa das eleições de 2026
## ---------------------------------------------------------------------
def render_2026():
    df26, origem_26 = load_dados_2026()

    st.markdown("""
    <h2 style='text-align: center; color: #303030; font-family:tahoma; text-rendering: optimizelegibility;'>Eleições 2026</h2>
    """, unsafe_allow_html=True)

    ## ------------------ informações do banco de 2026 ------------------
    with st.container():
        col3, col4, col5 = st.columns([.5, 4, .5])
        with col4:
            expander_26 = st.expander('Informações sobre o banco de 2026')
            institutos_26 = ', '.join(sorted(set(df26['nome_instituto']))).title()
            expander_26.markdown(f"""
            <p style='text-align: justify; font-family:Segoe UI;'>1. O banco de 2026 é atualizado continuamente e reúne as pesquisas nacionais com recorte religioso;</p>
            <p style='text-align: justify; font-family:Segoe UI;'>2. Candidatos acompanhados: { ', '.join([c['nome'] for c in CAND_2026.values()]) };</p>
            <p style='text-align: justify; font-family:Segoe UI;'>3. Institutos considerados: {institutos_26};</p>
            <p style='text-align: justify; font-family:Segoe UI;'>4. Total de pesquisas mapeadas: {len(df26)};</p>
            <p style='text-align: justify; font-family:Segoe UI;'>5. Fonte dos dados: {origem_26}.</p>
            """, unsafe_allow_html=True)

            expander_lista_26 = st.expander('Verifique as pesquisas eleitorais utilizadas (2026)')
            colunas_lista = [c for c in ['nome_instituto', 'data', 'registro_tse', 'entrevistados',
                                         'margem_erro', 'confiança', 'tipo_coleta'] if c in df26.columns]
            lista_26 = df26[colunas_lista].fillna(0)
            expander_lista_26.dataframe(lista_26)
            expander_lista_26.download_button(
                label='Baixe a lista em CSV',
                data=lista_26.to_csv(index=None).encode('utf-8-sig'),
                file_name='lista_2026.csv',
                mime='text/csv',
                key='download_lista_2026')
            expander_lista_26.caption('*Fontes*: TSE e Institutos de Pesquisa')

    st.markdown('---')

    ## ------------------ seletor de turno ------------------
    with st.container():
        st.markdown(
            "<div class='turn-band'><span class='lbl'>Explore os dados por turno</span></div>",
            unsafe_allow_html=True)

        turno_26 = st.radio(
            label='',
            options=['Primeiro Turno', 'Segundo Turno'],
            horizontal=True,
            label_visibility='collapsed',
            key='turno_2026')

    st.markdown('---')

    ####################
    ## primeiro turno ##
    ####################
    if turno_26 == 'Primeiro Turno':

        st.markdown("""
        <h2 style='text-align: center; color: #303030; font-family:tahoma; text-rendering: optimizelegibility;'>Primeiro Turno</h2><br>
        """, unsafe_allow_html=True)
        st.markdown('---')

        cabecalho_2026('1. Intenção de voto:', cor='#FFD662', alinhamento='center')
        st.markdown('---')

        ## resumo por candidato
        with st.container():
            cabecalho_2026('Resumo - intenção de voto geral e por religião segundo candidato:')
            resumo_2026(df26, turno='1t')

        ## intenção de voto geral
        with st.container():
            cabecalho_2026('Intenção de voto geral:')
            if st.checkbox('Selecione para visualizar o gráfico da intenção de voto geral',
                           key='graf_ger_1t_2026'):
                grafico_linhas_2026(
                    df26, 'ger_1t',
                    'Média móvel das intenções de voto de candidatos à presidência (1º turno)',
                    y_max=70, col_bra_nulo='bra_nul_ns_nr_ger_1t')
        st.markdown('---')

        ## intenção de voto por religião
        with st.container():
            cabecalho_2026('Intenção de voto por religião:')
            opcoes_rel = religioes_disponiveis_2026(df26, '{seg}_1t')
            relig_26 = st.selectbox('Selecione a religião:',
                                    options=['--Escolha a opção--'] + opcoes_rel,
                                    key='rel_1t_2026')
            if relig_26 != '--Escolha a opção--':
                seg = seg_por_rotulo_2026(relig_26)
                grafico_linhas_2026(
                    df26, f'{seg}_1t',
                    f'Média móvel das intenções de voto entre {relig_26.lower()} (1º turno)',
                    y_max=80)
        st.markdown('---')

        ## por instituto
        with st.container():
            cabecalho_2026('Intenção de voto por instituto de pesquisa:')
            col1_26, col2_26 = st.columns(2)
            with col1_26:
                inst_26 = st.selectbox('Selecione o instituto de pesquisa:',
                                       options=['--Escolha o instituto--'] + sorted(set(df26['nome_instituto'])),
                                       key='inst_1t_2026')
            with col2_26:
                rel_inst_26 = st.selectbox('Escolha a religião:',
                                           options=['--Escolha a religião--'] + religioes_disponiveis_2026(df26, '{seg}_1t'),
                                           key='rel_inst_1t_2026')
            if inst_26 != '--Escolha o instituto--' and rel_inst_26 != '--Escolha a religião--':
                grafico_instituto_2026(df26, inst_26, seg_por_rotulo_2026(rel_inst_26), '1t')
        st.markdown('---')

        ## rejeição
        cabecalho_2026('2. Rejeição', cor='#FFD662', alinhamento='center')
        st.markdown('---')

        with st.container():
            cabecalho_2026('Resumo - rejeição geral e por religião segundo candidato:')
            resumo_2026(df26, turno='1t', rejeicao=True)

        with st.container():
            cabecalho_2026('Rejeição geral:')
            if st.checkbox('Selecione para visualizar o gráfico da rejeição',
                           key='graf_rej_1t_2026'):
                grafico_linhas_2026(
                    df26, 'ger_rej_1t',
                    'Média móvel da rejeição dos candidatos à presidência (1º turno)',
                    y_max=100)
        st.markdown('---')

        with st.container():
            cabecalho_2026('Rejeição por religião:')
            opcoes_rej = religioes_disponiveis_2026(df26, '{seg}_rej_1t')
            rel_rej_26 = st.selectbox('Selecione a religião:',
                                      options=['--Escolha a opção--'] + opcoes_rej,
                                      key='rel_rej_1t_2026')
            if rel_rej_26 != '--Escolha a opção--':
                seg = seg_por_rotulo_2026(rel_rej_26)
                grafico_linhas_2026(
                    df26, f'{seg}_rej_1t',
                    f'Média móvel da rejeição entre {rel_rej_26.lower()} (1º turno)',
                    y_max=100)
        st.markdown('---')

    ###################
    ## segundo turno ##
    ###################
    if turno_26 == 'Segundo Turno':

        st.markdown("""
        <h2 style='text-align: center; color: #303030; font-family:tahoma; text-rendering: optimizelegibility;'>Segundo Turno</h2><br>
        """, unsafe_allow_html=True)
        st.markdown('---')

        cabecalho_2026('1. Intenção de voto:', cor='#FFD662', alinhamento='center')
        st.markdown('---')

        with st.container():
            cabecalho_2026('Resumo - intenção de voto por candidato:')
            resumo_2026(df26, turno='2t')

        with st.container():
            cabecalho_2026('Intenção de voto geral:')
            if st.checkbox('Clique para visualizar', key='graf_ger_2t_2026'):
                grafico_linhas_2026(
                    df26, 'ger_2t',
                    'Média móvel das intenções de voto de candidatos à presidência (2º turno)',
                    y_max=80, col_bra_nulo='bra_nul_ns_nr_ger_2t')
        st.markdown('---')

        with st.container():
            cabecalho_2026('Intenção de voto por religião:')
            opcoes_rel_2t = religioes_disponiveis_2026(df26, '{seg}_2t')
            relig_2t_26 = st.selectbox('Selecione a religião:',
                                       options=['--Escolha a opção--'] + opcoes_rel_2t,
                                       key='rel_2t_2026')
            if relig_2t_26 != '--Escolha a opção--':
                seg = seg_por_rotulo_2026(relig_2t_26)
                grafico_linhas_2026(
                    df26, f'{seg}_2t',
                    f'Média móvel das intenções de voto entre {relig_2t_26.lower()} (2º turno)',
                    y_max=90)
        st.markdown('---')

        with st.container():
            cabecalho_2026('Intenção de voto por instituto de pesquisa:')
            col1_2t, col2_2t = st.columns(2)
            with col1_2t:
                inst_2t_26 = st.selectbox('Selecione o instituto de pesquisa:',
                                          options=['--Escolha o instituto--'] + sorted(set(df26['nome_instituto'])),
                                          key='inst_2t_2026')
            with col2_2t:
                rel_inst_2t_26 = st.selectbox('Escolha a religião:',
                                              options=['--Escolha a religião--'] + religioes_disponiveis_2026(df26, '{seg}_2t'),
                                              key='rel_inst_2t_2026')
            if inst_2t_26 != '--Escolha o instituto--' and rel_inst_2t_26 != '--Escolha a religião--':
                grafico_instituto_2026(df26, inst_2t_26, seg_por_rotulo_2026(rel_inst_2t_26), '2t')
        st.markdown('---')

    st.markdown("""
    <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 1: os gráficos reproduzem os dados divulgados pelos institutos de pesquisa a partir do recorte religioso. Em alguns casos os institutos não coletam tais informações.</h7><br>
    <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 2: os recortes e candidatos sem pesquisas registradas no banco não são exibidos.</h7>
    """, unsafe_allow_html=True)

    st.caption(f"""
    <br><br>
    Site publicado em: 15/05/2022.<br>
    Lançamento: 03/08/2022.<br>
    Última atualização: {end_date.strftime(format='%d/%m/%Y')}
    """, unsafe_allow_html=True)


########################################################################
######## SELETOR DE ELEIÇÃO (2022 / 2026) ##############################
########################################################################

st.markdown("""
<style>
.election-band{ text-align:center; margin:6px 0 2px 0; }
.election-band .lbl{
  font-family:'JetBrains Mono',monospace;
  font-size:.72rem; font-weight:700; letter-spacing:.18em; text-transform:uppercase;
  color:var(--muted,#6E6E85);
}
div[data-testid="stButton"] > button{
  border-radius:999px !important;
  padding:10px 26px !important;
  font-weight:700 !important;
  width:100%;
  border:1px solid var(--border,#E9E7E0) !important;
  background:var(--surface,#FFFFFF) !important;
  color:var(--ink,#1A1A2E) !important;
  box-shadow:0 1px 3px rgba(20,33,61,.08);
  transition:transform .15s ease, border-color .15s ease;
}
div[data-testid="stButton"] > button:hover{
  transform:translateY(-2px);
  border-color:var(--accent,#FF6B35) !important;
}
div[data-testid="stButton"] > button[kind="primary"]{
  background:var(--primary,#14213D) !important;
  color:#FFFFFF !important;
  border-color:var(--primary,#14213D) !important;
}
</style>
""", unsafe_allow_html=True)

## guarda a eleição escolhida entre os reruns do Streamlit
if 'eleicao' not in st.session_state:
    st.session_state['eleicao'] = None


def _escolhe_eleicao(ano):
    st.session_state['eleicao'] = ano


with st.container():
    st.markdown(
        "<div class='election-band'><span class='lbl'>Escolha a eleição</span></div>",
        unsafe_allow_html=True)

    col_a, col_b, col_c, col_d = st.columns([1.2, 1, 1, 1.2])
    with col_b:
        st.button('Eleições 2022', key='btn_eleicao_2022',
                  on_click=_escolhe_eleicao, args=('2022',),
                  type='primary' if st.session_state['eleicao'] == '2022' else 'secondary')
    with col_c:
        st.button('Eleições 2026', key='btn_eleicao_2026',
                  on_click=_escolhe_eleicao, args=('2026',),
                  type='primary' if st.session_state['eleicao'] == '2026' else 'secondary')

st.markdown('---')

## nenhuma eleição escolhida ainda: o app para aqui
if st.session_state['eleicao'] is None:
    st.markdown("""
    <p style='text-align:center; font-family:Segoe UI; color:#6E6E85;'>
    Selecione <b>Eleições 2022</b> ou <b>Eleições 2026</b> para explorar os dados por turno.</p>
    """, unsafe_allow_html=True)
    st.stop()

## bloco das eleições de 2026: renderiza a página própria e encerra a execução
if st.session_state['eleicao'] == '2026':
    render_2026()
    st.stop()

########################################################################
######## BLOCO DAS ELEIÇÕES 2022 (código original, abaixo) #############
########################################################################


########################################################################
#### seletor para escolher o perído do primeiro ou do segundo turno#####
########################################################################
 
with st.container():
    st.markdown(
        "<div class='turn-band'><span class='lbl'>Explore os dados por turno</span></div>",
        unsafe_allow_html=True
    )

    options_turn = st.radio(
        label="",
        options=["Primeiro Turno", "Segundo Turno"],
        horizontal=True,
        label_visibility="collapsed",
    )

st.markdown("---")

############-#########

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
            col0, col, col1, col2, col3, col4, col5 = st.columns(7)
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
            col0, col, col1, col2, col3, col4, col5 = st.columns(7)
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
            col0, col, col1, col2, col3, col4, col5 = st.columns(7)
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
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia <i>{list(df.data)[-1].strftime(format='%d-%m-%Y')}</i></h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
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
            fig.add_trace(go.Scatter(y=df[df['lul_ger_1t']>1].lul_ger_1t, x=df[df['lul_ger_1t']>1].sigla, mode='markers', name='Int. voto Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ger_1t']>1].lul_ger_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean(), x=df[df['lul_ger_1t']>1].sigla,mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_ger_1t']>1].sigla)[-1], y=list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_ger_1t']>1].lul_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## Bolsonaro [df['']]
            fig.add_trace(go.Scatter(y=df[df['bol_ger_1t']>1].bol_ger_1t, x=df[df['bol_ger_1t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ger_1t']>1].bol_ger_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean(), x=df[df['bol_ger_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_ger_1t']>1].sigla)[-1], y=list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_ger_1t']>1].bol_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Ciro

            fig.add_trace(go.Scatter(y=df[df['ciro_ger_1t']>1].ciro_ger_1t, x=df[df['ciro_ger_1t']>1].sigla, mode='markers', name='Int. voto Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_ger_1t']>1].ciro_ger_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean(), x=df[df['ciro_ger_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_ger_1t']>1].sigla)[-1], y=list(df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_ger_1t']>1].ciro_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))


            # ## Brancos e Nulos e não sabe e não respondeu

            # fig.add_trace(go.Scatter(y=df.bra_nul_ns_nr_ger_1t, x=df.sigla, mode='markers', name='brancos_nulos_ns_nr',
            #                         marker=dict(
            #                         size=5,
            #                         color=df.bra_nul_ns_nr_ger_1t, #set color equal to a variable
            #                         colorscale='Greys')))

            # fig.add_trace(go.Scatter(y=df.bra_nul_ns_nr_ger_1t.rolling(m_m).mean(), x=df.sigla, mode='lines', name='Brancos, nulos, NS e NR',
            #                         line=dict(color='grey', width=2.5)))

            # fig.add_annotation(x=list(df.sigla)[-1], y=list(df.bra_nul_ns_nr_ger_1t.rolling(m_m).mean())[-1] ,text=f"{int(list(df.bra_nul_ns_nr_ger_1t.rolling(m_m).mean())[-1])}%",
            #             showarrow=True,
            #             arrowhead=1,
            #             ax = 40, ay = -8,
            #             font=dict(size=20, color="black", family="Arial"))

            ## Brancos e Nulos, NS e NR

            fig.add_trace(go.Scatter(y=df[df['bra_nul_ns_nr_ger_1t']>1].bra_nul_ns_nr_ger_1t, x=df[df['bra_nul_ns_nr_ger_1t']>1].sigla, mode='markers', name='Brancos, nulos NS e NR',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bra_nul_ns_nr_ger_1t']>1].bra_nul_ns_nr_ger_1t, #set color equal to a variable
                                    colorscale='Greys'),legendrank=8))

            fig.add_trace(go.Scatter(y=df[df['bra_nul_ns_nr_ger_1t']>1].bra_nul_ns_nr_ger_1t.rolling(m_m).mean(), x=df[df['bra_nul_ns_nr_ger_1t']>1].sigla, mode='lines', name='Brancos, nulos NS e NR',
                                    line=dict(color='grey', width=2.5),legendrank=7))

            fig.add_annotation(x=list(df[df['bra_nul_ns_nr_ger_1t']>1].sigla)[-1], y=list(df[df['bra_nul_ns_nr_ger_1t']>1].bra_nul_ns_nr_ger_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bra_nul_ns_nr_ger_1t']>1].bra_nul_ns_nr_ger_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -0.5,
                        font=dict(size=20, color="black", family="Arial"))

            fig.update_layout(autosize=True, width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=160),
            title="<i>Média móvel das intenções de voto de candidatos à presidência (1º turno)<i>",
            title_xanchor="auto",
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            font=dict(family="arial",size=13),
                            legend_title_text='<br><br><br><br><br><br><br>',
                            legend=dict(
                orientation="v",
                font_family="arial",))
            
            #moro desiste
            fig.add_vline(x=str("mar/22_poderdata_3"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mar/22_poderdata_3", y=57,text="Moro<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #dória desiste
            fig.add_vline(x=str("mai/22_poderdata_2"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mai/22_poderdata_2", y=57,text="Dória<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #candidaturas
            fig.add_annotation(x="jul/22_ipespe", y=6,text="Candidatura<br>Ciro (PDT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=45,text="Candidatura<br>Lula (PT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -30,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_futura", y=32,text="Candidatura<br>Bolsonaro (PL)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 80,font=dict(size=10, color="black", family="Arial"))
            #linha inicio campanha
            fig.add_annotation(x="ago/22_fsb", y=57,text="Início da<br>Campanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_fsb"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_ipec_2", y=57,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=57,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            ##resultado 1o turno
            fig.add_annotation(x="out/22_datafolha", y=57,text="<b>Resultado<br>1º turno</b>",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_datafolha", y=52,text="Lula = 48,4%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_datafolha", y=38,text="Bolsonaro = 43,2%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_datafolha", y=13,text="Ciro = 3,0%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("out/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)


            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            fig.update_yaxes(range=[0,60]) ## exibe o intervalo de y a ser exibido no gráfico

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.05,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.87, y=1.05,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: *Método utilizado:* média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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
            fig.add_trace(go.Scatter(y=df[df['lul_cat_1t']>1].lul_cat_1t, x=df[df['lul_cat_1t']>1].sigla, mode='markers', name='Int. voto Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_cat_1t']>1].lul_cat_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean(), x=df[df['bol_cat_1t']>1].sigla,mode='lines', name='Lula',
                                    line=dict(color='rgba(200, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_cat_1t']>1].sigla)[-1], y=list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_cat_1t']>1].lul_cat_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df[df['bol_cat_1t']>1].bol_cat_1t, x=df[df['bol_cat_1t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_cat_1t']>1].lul_cat_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean(), x=df[df['bol_cat_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_cat_1t']>1].sigla)[-1], y=list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_cat_1t']>1].bol_cat_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Ciro

            fig.add_trace(go.Scatter(y=df[df['ciro_cat_1t']>1].ciro_cat_1t, x=df[df['ciro_cat_1t']>1].sigla, mode='markers', name='Int. voto Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_cat_1t']>1].ciro_cat_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean(), x=df[df['ciro_cat_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_cat_1t']>1].sigla)[-1], y=list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_cat_1t']>1].ciro_cat_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            ## Brancos e Nulos

            fig.add_trace(go.Scatter(y=df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t, x=df[df['bra_nulo_cat_1t']>1].sigla, mode='markers', name='Brancos e Nulos',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t, #set color equal to a variable
                                    colorscale='Greys'),legendrank=8))

            fig.add_trace(go.Scatter(y=df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t.rolling(m_m).mean(), x=df[df['bra_nulo_cat_1t']>1].sigla, mode='lines', name='Brancos, nulos',
                                    line=dict(color='grey', width=2.5),legendrank=7))

            fig.add_annotation(x=list(df[df['bra_nulo_cat_1t']>1].sigla)[-1], y=list(df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bra_nulo_cat_1t']>1].bra_nulo_cat_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))


            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=110),
            title=("""
            <i>Média móvel das intenções de voto de católicos por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',

                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend_title_text='<br><br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                orientation="v",
                font_family="arial"))

            fig.add_annotation(x="mar/22_poderdata_3", y=25,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_poderdata_2", y=28,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #fig.add_annotation(x="jun/22_datafolha", y=26,text="Datena<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=9,text="Candidatura<br>Ciro (PDT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -30,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=46,text="Candidatura<br>Lula (PT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -50,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_datafolha", y=29,text="Candidatura<br>Bolsonaro (PL)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 60,font=dict(size=10, color="black", family="Arial"))
            #linha inicio campanha
            fig.add_vline(x=str("ago/22_quaest"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_ipec_2", y=60,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=60,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)


            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            fig.update_yaxes(range=[0,65]) ## exibe o intervalo de y a ser exibido no gráfico

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.08,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)

            ## info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais e {len(df[df['lul_cat_1t']>1])} para os católicos.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Evangélica':
            fig = go.Figure()
            ## lula
            fig.add_trace(go.Scatter(y=df[df['lul_ev_1t']>1].lul_ev_1t, x=df[df['lul_ev_1t']>1].sigla, mode='markers', name='Int. voto Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ev_1t']>1].lul_ev_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean(), x=df[df['bol_ev_1t']>1].sigla,mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_ev_1t']>1].sigla)[-1], y=list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_ev_1t']>1].lul_ev_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))
            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df[df['bol_ev_1t']>1].bol_ev_1t, x=df[df['bol_ev_1t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ev_1t']>1].bol_ev_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean(), x=df[df['bol_ev_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_ev_1t']>1].sigla)[-1], y=list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_ev_1t']>1].bol_ev_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))
            ## Ciro
            fig.add_trace(go.Scatter(y=df[df['ciro_ev_1t']>1].ciro_ev_1t, x=df[df['ciro_ev_1t']>1].sigla, mode='markers', name='Int. voto Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_ev_1t']>1].ciro_ev_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean(), x=df[df['ciro_ev_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_ev_1t']>1].sigla)[-1], y=list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_ev_1t']>1].ciro_ev_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))

            ## Brancos e Nulos

            fig.add_trace(go.Scatter(y=df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t, x=df[df['bra_nulo_ev_1t']>1].sigla, mode='markers', name='Brancos e nulos',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t, #set color equal to a variable
                                    colorscale='Greys'),legendrank=8))

            fig.add_trace(go.Scatter(y=df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t.rolling(m_m).mean(), x=df[df['bra_nulo_ev_1t']>1].sigla, mode='lines', name='Brancos e nulos',
                                    line=dict(color='grey', width=2.5),legendrank=7))

            fig.add_annotation(x=list(df[df['bra_nulo_ev_1t']>1].sigla)[-1], y=list(df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bra_nulo_ev_1t']>1].bra_nulo_ev_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=110),
            title=("""
            <i>Média móvel das intenções de voto de evangélicos por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend_title_text='<br><br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                orientation="v",
                font_family="arial",))

            fig.add_annotation(x="mar/22_poderdata_3", y=28,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_poderdata_2", y=28,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #fig.add_annotation(x="jun/22_datafolha", y=27,text="Datena<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=5,text="Candidatura<br>Ciro (PDT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=31,text="Candidatura<br>Lula (PT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 80,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_fsb_2", y=46,text="Candidatura<br>Bolsonaro (PL)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -40,font=dict(size=10, color="black", family="Arial"))
            #linha inicio campanha
            fig.add_vline(x=str("ago/22_quaest"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_poderdata_3", y=57,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_poderdata_3"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=57,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            fig.update_yaxes(range=[0,60]) ## exibe o intervalo de y a ser exibido no gráfico

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.08,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)

            ## info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais e {len(df[df['lul_ev_1t']>1])} para os evangélicos.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Espírita':
            fig = go.Figure()
            ## lula
            fig.add_trace(go.Scatter(y=df[df['lul_espi_1t']>1].lul_espi_1t, x=df[df['lul_espi_1t']>1].sigla, mode='markers', name='Int. voto Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_espi_1t']>1].lul_espi_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean(), x=df[df['bol_espi_1t']>1].sigla,mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_espi_1t']>1].sigla)[-1], y=list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_espi_1t']>1].lul_espi_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df[df['bol_espi_1t']>1].bol_espi_1t, x=df[df['bol_espi_1t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_espi_1t']>1].bol_espi_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean(), x=df[df['bol_espi_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_espi_1t']>1].sigla)[-1], y=list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_espi_1t']>1].bol_espi_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                            ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Ciro

            fig.add_trace(go.Scatter(y=df[df['ciro_espi_1t']>1].ciro_espi_1t, x=df[df['ciro_espi_1t']>1].sigla, mode='markers', name='Int. voto Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_espi_1t']>1].ciro_espi_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean(), x=df[df['ciro_espi_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_espi_1t']>1].sigla)[-1], y=list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_espi_1t']>1].ciro_espi_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            # Brancos e Nulos
            ## inseri o filtro do lula na barra x para poder incluir o valor tipo padrão

            fig.add_trace(go.Scatter(y=df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t, x=df[df['bra_nulo_espi_1t']>1].sigla, mode='markers', name='Brancos e nulos',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t, #set color equal to a variable
                                    colorscale='Greys'),legendrank=8))

            fig.add_trace(go.Scatter(y=df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t.rolling(m_m).mean(), x=df[df['bra_nulo_espi_1t']>1].sigla, mode='lines', name='Brancos e nulos',
                                    line=dict(color='grey', width=2.5),legendrank=7))

            fig.add_annotation(x=list(df[df['lul_espi_1t']>1].sigla)[-1], y=list(df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bra_nulo_espi_1t']>1].bra_nulo_espi_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=110),
            title=("""
            <i>Média móvel das intenções de voto de espíritas por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend_title_text='<br><br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                orientation="v",
                font_family="arial",))

            fig.add_annotation(x="mar/22_poderdata_3", y=28,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_poderdata_2", y=22,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #linha inicio campanha
            fig.add_vline(x=str("ago/22_quaest"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_poderdata_3", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_poderdata_3"), line_width=.2, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.08,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)

            ## info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais e {len(df[df['lul_espi_1t']>1])} para os espíritas.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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
    #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_umb_can_1t']>1].data)[-1], y=list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_umb_can_1t']>1].lul_umb_can_1t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['bol_umb_can_1t']>1].data)[-1], y=list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_umb_can_1t']>1].bol_umb_can_1t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['ciro_umb_can_1t']>1].data)[-1], y=list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_umb_can_1t']>1].ciro_umb_can_1t.rolling(m_m).mean())[-1])}%",
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

    #     fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
    #     st.plotly_chart(fig,use_container_width=True)

    # if relig == 'Ateu':
    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_1t']>1].lul_ateu_1t, x=df[df['lul_ateu_1t']>1].data, mode='markers', name='int_vot_ateu_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_ateu_1t']>1].lul_ateu_1t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean(), x=df[df['bol_ateu_1t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_ateu_1t']>1].data)[-1], y=list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_ateu_1t']>1].lul_ateu_1t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['bol_ateu_1t']>1].data)[-1], y=list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_ateu_1t']>1].bol_ateu_1t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['ciro_ateu_1t']>1].data)[-1], y=list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_ateu_1t']>1].ciro_ateu_1t.rolling(m_m).mean())[-1])}%",
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

    #     fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
    #     st.plotly_chart(fig,use_container_width=True)

    if relig == 'Sem Religião':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_non_1t']>1].lul_non_1t, x=df[df['lul_non_1t']>1].sigla, mode='markers', name='Int. voto Lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_non_1t']>1].lul_non_1t, #set color equal to a variable
                                colorscale='peach'),legendrank=2))

        fig.add_trace(go.Scatter(y=df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean(), x=df[df['bol_non_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

        fig.add_annotation(x=list(df[df['lul_non_1t']>1].sigla)[-1], y=list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_non_1t']>1].lul_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_non_1t']>1].bol_non_1t, x=df[df['bol_non_1t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_non_1t']>1].bol_non_1t, #set color equal to a variable
                                colorscale='ice'),legendrank=4))

        fig.add_trace(go.Scatter(y=df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean(), x=df[df['bol_non_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5),legendrank=3))

        fig.add_annotation(x=list(df[df['bol_non_1t']>1].sigla)[-1], y=list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_non_1t']>1].bol_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_non_1t']>1].ciro_non_1t, x=df[df['ciro_non_1t']>1].sigla, mode='markers', name='Int. voto Ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_non_1t']>1].ciro_non_1t, #set color equal to a variable
                                colorscale='Greens'),legendrank=6))

        fig.add_trace(go.Scatter(y=df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean(), x=df[df['ciro_non_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5),legendrank=5))

        fig.add_annotation(x=list(df[df['ciro_non_1t']>1].sigla)[-1], y=list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_non_1t']>1].ciro_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos e Nulos

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t, x=df[df['bra_nulo_non_1t']>1].sigla, mode='markers', name='Brancos e nulos',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t, #set color equal to a variable
                                colorscale='Greys'),legendrank=8))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t.rolling(m_m).mean(), x=df[df['bra_nulo_non_1t']>1].sigla, mode='lines', name='Brancos e nulos',
                                line=dict(color='grey', width=2.5),legendrank=7))

        fig.add_annotation(x=list(df[df['bra_nulo_non_1t']>1].sigla)[-1], y=list(df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bra_nulo_non_1t']>1].bra_nulo_non_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=110),
        title=("""
        <i>Média móvel das intenções de voto dos sem religião por candidato à presidência (1º turno)<i><br>
        """),
        plot_bgcolor='rgb(255, 255, 255)',
        paper_bgcolor='rgb(255, 255, 255)',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend_title_text='<br><br><br><br><br><br><br>',
                        font=dict(family="arial",size=13),
                        legend=dict(
            orientation="v",
            font_family="arial",))

        fig.add_annotation(x="mar/22_poderdata_3", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_poderdata_2", y=20,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        #fig.add_annotation(x="jun/22_poderdata", y=20,text="Datena<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="jul/22_fsb_2", y=7,text="Candidatura<br>Ciro (PDT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="jul/22_fsb_2", y=54,text="Candidatura<br>Lula (PT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -30,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="jul/22_fsb_2", y=20,text="Candidatura<br>Bolsonaro (PL)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        #linha inicio campanha
        fig.add_vline(x=str("ago/22_fsb"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        #linha debate
        fig.add_annotation(x="ago/22_fsb_4", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("ago/22_fsb_4"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        #linha 7 de setembro
        fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

        fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.02,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.08,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        st.plotly_chart(fig,use_container_width=True)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais e {len(df[df['lul_non_1t']>1])} para sem religião.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
        """, unsafe_allow_html=True)

    if relig == 'Outras Religiosidades':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_out_1t']>1].lul_out_1t, x=df[df['lul_out_1t']>1].sigla, mode='markers', name='Int. voto Lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_out_1t']>1].lul_out_1t, #set color equal to a variable
                                colorscale='peach'),legendrank=2))

        fig.add_trace(go.Scatter(y=df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean(), x=df[df['bol_out_1t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

        fig.add_annotation(x=list(df[df['lul_out_1t']>1].sigla)[-1], y=list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_out_1t']>1].lul_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_out_1t']>1].bol_out_1t, x=df[df['bol_out_1t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_out_1t']>1].bol_out_1t, #set color equal to a variable
                                colorscale='ice'),legendrank=4))

        fig.add_trace(go.Scatter(y=df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean(), x=df[df['bol_out_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5),legendrank=3))

        fig.add_annotation(x=list(df[df['bol_out_1t']>1].sigla)[-1], y=list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_out_1t']>1].bol_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Ciro

        fig.add_trace(go.Scatter(y=df[df['ciro_out_1t']>1].ciro_out_1t, x=df[df['ciro_out_1t']>1].sigla, mode='markers', name='Int. voto Ciro',
                                marker=dict(
                                size=5,
                                color=df[df['ciro_out_1t']>1].ciro_out_1t, #set color equal to a variable
                                colorscale='Greens'),legendrank=6))

        fig.add_trace(go.Scatter(y=df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean(), x=df[df['ciro_out_1t']>1].sigla, mode='lines', name='Ciro Gomes',
                                line=dict(color='seagreen', width=2.5),legendrank=5))

        fig.add_annotation(x=list(df[df['ciro_out_1t']>1].sigla)[-1], y=list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_out_1t']>1].ciro_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos e Nulos

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t, x=df[df['bra_nulo_out_1t']>1].sigla, mode='markers', name='Brancos e nulos',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t, #set color equal to a variable
                                colorscale='Greys'),legendrank=8))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t.rolling(m_m).mean(), x=df[df['bra_nulo_out_1t']>1].sigla, mode='lines', name='Brancos e nulos',
                                line=dict(color='grey', width=2.5),legendrank=7))

        fig.add_annotation(x=list(df[df['bra_nulo_out_1t']>1].sigla)[-1], y=list(df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bra_nulo_out_1t']>1].bra_nulo_out_1t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 20,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=110),
        title=("""
        <i>Média móvel das intenções de voto de outras religiões por candidato à presidência (1º turno)<i><br>
        """),
        plot_bgcolor='rgb(255, 255, 255)',
        paper_bgcolor='rgb(255, 255, 255)',
                        xaxis_title='Mês, ano e instituto de pesquisa',
                        yaxis_title='Intenção de voto (%)',
                        legend_title_text='<br><br><br><br><br><br><br>',
                        font=dict(family="arial",size=13),
                        legend=dict(
            orientation="v",
            font_family="arial"))

        fig.add_annotation(x="mar/22_futura", y=20,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_annotation(x="mai/22_futura", y=20,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        #fig.add_annotation(x="jun/22_ipespe", y=22,text="Datena<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        #linha inicio campanha
        fig.add_vline(x=str("ago/22_fsb"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        #linha debate
        fig.add_annotation(x="ago/22_ipec_2", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("ago/22_ipec_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        #linha 7 de setembro
        fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)


        fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.02,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.08,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        st.plotly_chart(fig,use_container_width=True)

        ## info
        st.markdown(f"""
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Para o cálculo da média móvel da intenção de voto geral utilizamos {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais e {len(df[df['lul_out_1t']>1])} para outras religiosidades.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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
                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'cat'
                rel = 'católicos'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)',  
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)

            if rel == 'Evangélica':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'ev'
                rel = 'evangélicos'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)

            if rel == 'Espírita':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'espi'
                rel = 'espíritas'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
                                        xaxis_title='Mês, ano e instituto de pesquisa',
                                        yaxis_title='Intenção de voto (%)',
                                        font=dict(family="arial",size=13),
                                        legend=dict(
                            yanchor="auto",
                            y=1.15,
                            xanchor="auto",
                            x=0.4,
                            orientation="v",
                            font_family="arial",))
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            if rel == 'Sem Religião':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'non'
                rel = 'sem religião'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            if rel == 'Outras Religiosidades':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'out'
                rel = 'outras religiões'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=70, l=80, b=4, t=160),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel}' por candidato segundo inst. '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
                                        xaxis_title='Mês, ano e instituto de pesquisa',
                                        yaxis_title='Intenção de voto (%)',
                                        font=dict(family="arial",size=13),
                                        legend=dict(
                            yanchor="auto",
                            y=1.13,
                            xanchor="auto",
                            x=0.4,
                            orientation="h",
                            font_family="arial",))
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,60])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=1.05, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=1.05, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            
            # if rel == 'Umbanda/Candomblé':

            #     fonte = df.query(f"nome_instituto =='{inst}'")
            #     religi_escolhida = 'umb_can'
            #     rel = 'umbanda e candomblé'

            #     fig = go.Figure()
            #     ##lula
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
            #     ##bolsonaro
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
            #                             line=dict(color='royalblue', width=2.5),legendrank=2))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
            #                             line=dict(color='royalblue', width=1, dash='dot')))
            #     ##ciro gomes
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
            #                             line=dict(color='green', width=2.5),legendrank=3))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
            #                             line=dict(color='green', width=1, dash='dot')))

            #     fig.update_layout(width = 1000, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            #             title=(f"""
            #             Intenção de voto 'geral' de adeptos da '{rel}' por candidato segundo '{inst.title()}' (1º turno)
            #             <br>
            #             <br>
            #             """),
            #                             xaxis_title='Mês, ano e instituto de pesquisa',
            #                             yaxis_title='Intenção de voto (%)',
            #                             font=dict(family="arial",size=13),
            #                             legend=dict(
            #                 yanchor="auto",
            #                 y=1.15,
            #                 xanchor="auto",
            #                 x=0.4,
            #                 orientation="h",
            #                 font_family="arial",))
            #     fig.update_xaxes(tickangle = 300,title_font_family="arial")
            #     fig.update_yaxes(range=[0,90])

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
            #             xref="paper", yref="paper",
            #             x=.99, y=1.03,
            #             sizex=0.1, sizey=0.1,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source=agre,
            #             xref="paper", yref="paper",
            #             x=.99, y=1.08,
            #             sizex=0.12, sizey=0.12,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )
                
            #     st.plotly_chart(fig,use_container_width=True)
            

            # if rel == 'Ateu':

            #     fonte = df.query(f"nome_instituto =='{inst}'")
            #     religi_escolhida = 'ateu'
            #     rel = 'ateus'

            #     fig = go.Figure()
            #     ##lula
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
            #     ##bolsonaro
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
            #                             line=dict(color='royalblue', width=2.5),legendrank=2))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
            #                             line=dict(color='royalblue', width=1, dash='dot')))
            #     ##ciro gomes
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
            #                             line=dict(color='green', width=2.5),legendrank=3))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
            #                             line=dict(color='green', width=1, dash='dot')))

            #     fig.update_layout(width = 810, height = 700, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            #             title=(f"""
            #             Intenção de voto 'geral' de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
            #             <br>
            #             <br>
            #             """),
            #                             xaxis_title='Mês, ano e instituto de pesquisa',
            #                             yaxis_title='Intenção de voto (%)',
            #                             font=dict(family="arial",size=13),
            #                             legend=dict(
            #                 yanchor="auto",
            #                 y=1.15,
            #                 xanchor="auto",
            #                 x=0.4,
            #                 orientation="h",
            #                 font_family="arial",))
            #     fig.update_xaxes(tickangle = 300,title_font_family="arial")
            #     fig.update_yaxes(range=[-0.5,95])

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
            #             xref="paper", yref="paper",
            #             x=1.05, y=1.03,
            #             sizex=0.1, sizey=0.1,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source=agre,
            #             xref="paper", yref="paper",
            #             x=1.05, y=1.08,
            #             sizex=0.12, sizey=0.12,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )
                
            #     st.plotly_chart(fig,use_container_width=True)
                

        st.markdown(f"""
        <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 1: Os gráficos reproduzem os dados divulgados pelos institutos de pesquisa a partir do recorte religioso. Em alguns casos os institutos não coletam tais informações.</h7>
        <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 2: Os gráficos com linhas descontinuadas indicam que o instituto não coletou a informação em determinada pesquisa. Um exemplo pode ser visto a partir da combinação "Paraná Pesquisas" e "católicos".</h7>
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
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia <i>{list(df.data)[-1].strftime(format='%d-%m-%Y')}</i></h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da <i>rejeição</i> dos candidatos utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais.</h7><br>
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
            fig.add_trace(go.Scatter(y=df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t, x=df[df['lul_ger_rej_1t']>1].sigla, mode='markers', name='Rejeição Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m15).mean(), x=df[df['lul_ger_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_ger_rej_1t']>1].sigla)[-1], y=list(df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m15).mean())[-1],text=f"{int(list(df[df['lul_ger_rej_1t']>1].lul_ger_rej_1t.rolling(m_m15).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t, x=df[df['bol_ger_rej_1t']>1].sigla, mode='markers', name='Rejeição Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m15).mean(), x=df[df['bol_ger_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_ger_rej_1t']>1].sigla)[-1], y=list(df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m15).mean())[-1],text=f"{int(list(df[df['bol_ger_rej_1t']>1].bol_ger_rej_1t.rolling(m_m15).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t, x=df[df['ciro_ger_rej_1t']>1].sigla, mode='markers', name='Rejeição Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m15).mean(), x=df[df['ciro_ger_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_ger_rej_1t']>1].sigla)[-1], y=list(df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m15).mean())[-1],text=f"{int(list(df[df['ciro_ger_rej_1t']>1].ciro_ger_rej_1t.rolling(m_m15).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1100, height = 700, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=110),
            title=("""
            <i>Média móvel da rejeição geral de candidatos à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            legend_title_text='<br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                orientation="v",
                font_family="arial",))
            ## moro desiste
            fig.add_annotation(x="mar/22_pr_pesq", y=75,text="Moro<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("mar/22_pr_pesq"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            ## dória desiste
            fig.add_annotation(x="mai/22_datafolha", y=70,text="Dória<br>desiste",showarrow=False,arrowhead=3,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("mai/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #fig.add_annotation(x="jun/22_poderdata", y=37,text="Datena<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = -20, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=38,text="Candidatura<br>Ciro (PDT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = -60, ay = 80,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=38,text="Candidatura<br>Lula (PT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 50,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_futura", y=56,text="Candidatura<br>Bolsonaro<br>(PL)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -30,font=dict(size=10, color="black", family="Arial"))
            ## inicio eleição
            fig.add_annotation(x="ago/22_fsb", y=75,text="Início da<br>Campanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_fsb"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_ipec_2", y=75,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=75,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            fig.update_yaxes(range=[0,80])

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.07,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.88, y=1.07,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )
            st.plotly_chart(fig,use_container_width=True)

            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: <i>Método utilizado:</i> média móvel de {m_m15} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da rejeição utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 5: Mesmo com a aplicação da média móvel de 15 dias, o recorte temporal da rejeição geral de Ciro Gomes manteve-se oscilante. Trabalhamos com a hipótese de que a rejeição de Gomes associa-se à inclusão de concorrentes da 3a via como alternativas, espaço disputado por Gomes. Portanto, supomos que a variação da rejeição de Ciro Gomes seja um efeito da inclusão ou desistência de outras candiaturas.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 6: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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
        
        relig = st.selectbox('Selecione a religião:',options=['--Escolha a opção--','Católica ', 'Evangélica ', 'Espírita ', 'Sem Religião ', 'Outras Religiosidades '])

        if relig == 'Católica ':

            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t, x=df[df['lul_cat_rej_1t']>1].sigla, mode='markers', name='Rejeição Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean(), x=df[df['lul_cat_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_cat_rej_1t']>1].sigla)[-1], y=list(df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_cat_rej_1t']>1].lul_cat_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t, x=df[df['bol_cat_rej_1t']>1].sigla, mode='markers', name='Rejeição Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean(), x=df[df['bol_cat_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_cat_rej_1t']>1].sigla)[-1], y=list(df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_cat_rej_1t']>1].bol_cat_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t, x=df[df['ciro_cat_rej_1t']>1].sigla, mode='markers', name='Rejeição Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean(), x=df[df['ciro_cat_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_cat_rej_1t']>1].sigla)[-1], y=list(df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_cat_rej_1t']>1].ciro_cat_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Média Móvel da rejeição de católicos por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                
                orientation="v",
                font_family="arial",))
            #moro desiste
            fig.add_vline(x=str("mar/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mar/22_datafolha", y=68,text="Moro<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #dória desiste
            fig.add_vline(x=str("mai/22_futura"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mai/22_futura", y=68,text="Dória<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #início da campanha
            fig.add_annotation(x="ago/22_ipec", y=68,text="Início da<br>Camapanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_ipec_2", y=63,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec_2"), line_width=.2, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=63,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.10,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)

             # info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: <i>Método utilizado:</i> média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da rejeição de católicos utilizamos {len(df[df['lul_cat_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 5: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Evangélica ':
            
            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t, x=df[df['lul_ev_rej_1t']>1].sigla, mode='markers', name='Rejeição Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean(), x=df[df['lul_ev_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_ev_rej_1t']>1].sigla)[-1], y=list(df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_ev_rej_1t']>1].lul_ev_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t, x=df[df['bol_ev_rej_1t']>1].sigla, mode='markers', name='Rejeição Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean(), x=df[df['bol_ev_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_ev_rej_1t']>1].sigla)[-1], y=list(df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_ev_rej_1t']>1].bol_ev_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t, x=df[df['ciro_ev_rej_1t']>1].sigla, mode='markers', name='Rejeição Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean(), x=df[df['ciro_ev_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_ev_rej_1t']>1].sigla)[-1], y=list(df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_ev_rej_1t']>1].ciro_ev_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Média Móvel da rejeição de evangélicos por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                
                orientation="v",
                font_family="arial",))

            #moro desiste
            fig.add_vline(x=str("mar/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mar/22_datafolha", y=65,text="Moro<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #dória desiste
            fig.add_vline(x=str("mai/22_futura"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mai/22_futura", y=65,text="Dória<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #início da campanha
            fig.add_annotation(x="ago/22_ipec", y=65,text="Início da<br>Camapanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)            
            #linha debate
            fig.add_annotation(x="ago/22_ipec_2", y=60,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_ipec_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=60,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.10,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)

             # info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: <i>Método utilizado:</i> média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da rejeição de evangélicos utilizamos {len(df[df['lul_ev_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 5: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Espírita ':
            
            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t, x=df[df['lul_espi_rej_1t']>1].sigla, mode='markers', name='Rejeição Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean(), x=df[df['lul_espi_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_espi_rej_1t']>1].sigla)[-1], y=list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_espi_rej_1t']>1].lul_espi_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 8,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t, x=df[df['bol_espi_rej_1t']>1].sigla, mode='markers', name='Rejeição Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t.rolling(m_m).mean(), x=df[df['bol_espi_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_espi_rej_1t']>1].sigla)[-1], y=list(df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_espi_rej_1t']>1].bol_espi_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t, x=df[df['ciro_espi_rej_1t']>1].sigla, mode='markers', name='Rejeição Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t.rolling(m_m).mean(), x=df[df['ciro_espi_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_espi_rej_1t']>1].sigla)[-1], y=list(df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_espi_rej_1t']>1].ciro_espi_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Média Móvel da rejeição de espíritas por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
    
                orientation="v",
                font_family="arial",))

            fig.add_annotation(x="mar/22_datafolha", y=30,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_futura", y=25,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #início da campanha
            fig.add_annotation(x="ago/22_datafolha", y=70,text="Início da<br>Camapanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_poderdata_3", y=75,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_poderdata_3"), line_width=.2, line_dash="dot", line_color="black", opacity=.5)
            
            
            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.10,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)
            
             # info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: <i>Método utilizado:</i> média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da rejeição de espíritas utilizamos {len(df[df['lul_espi_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
            """, unsafe_allow_html=True)

        if relig == 'Outras Religiosidades ':
            
            fig = go.Figure()
                
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_out_rej_1t']>1].lul_out_rej_1t, x=df[df['lul_out_rej_1t']>1].sigla, mode='markers', name='Rejeição Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_out_rej_1t']>1].lul_out_rej_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean(), x=df[df['lul_out_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_out_rej_1t']>1].sigla)[-1], y=list(df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_out_rej_1t']>1].lul_out_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_out_rej_1t']>1].bol_out_rej_1t, x=df[df['bol_out_rej_1t']>1].sigla, mode='markers', name='Rejeição Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_out_rej_1t']>1].bol_out_rej_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean(), x=df[df['bol_out_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=2))

            fig.add_annotation(x=list(df[df['bol_out_rej_1t']>1].sigla)[-1], y=list(df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_out_rej_1t']>1].bol_out_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t, x=df[df['ciro_out_rej_1t']>1].sigla, mode='markers', name='Rejeição Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean(), x=df[df['ciro_out_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_out_rej_1t']>1].sigla)[-1], y=list(df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_out_rej_1t']>1].ciro_out_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Média Móvel da rejeição de outras religiões por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Rejeição (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                orientation="v",
                font_family="arial",))

            #moro desiste
            fig.add_vline(x=str("mar/22_futura"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mar/22_futura", y=80,text="Moro<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #dória desiste
            fig.add_vline(x=str("mai/22_futura"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mai/22_futura", y=75,text="Dória<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #inicio campanha
            fig.add_vline(x=str("ago/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="ago/22_datafolha", y=80,text="Início da<br>Campanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #linha debate
            fig.add_annotation(x="ago/22_poderdata_3", y=75,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_poderdata_3"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=75,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.10,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)

             # info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da rejeição de outras religiões utilizamos {len(df[df['lul_out_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
            """, unsafe_allow_html=True)
            
        if relig == 'Sem Religião ':
            
            fig = go.Figure()
                    
            ## lula

            fig.add_trace(go.Scatter(y=df[df['lul_non_rej_1t']>1].lul_non_rej_1t, x=df[df['lul_non_rej_1t']>1].sigla, mode='markers', name='Rejeição Lula',
                                    marker=dict(
                                    size=5,
                                    color=df[df['lul_non_rej_1t']>1].lul_non_rej_1t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean(), x=df[df['lul_non_rej_1t']>1].sigla, mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_non_rej_1t']>1].sigla)[-1], y=list(df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['lul_non_rej_1t']>1].lul_non_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -20,
                        font=dict(size=20, color="black", family="Arial"))


            ## bolsonaro

            fig.add_trace(go.Scatter(y=df[df['bol_non_rej_1t']>1].bol_non_rej_1t, x=df[df['bol_non_rej_1t']>1].sigla, mode='markers', name='Rejeição Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['bol_non_rej_1t']>1].bol_non_rej_1t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean(), x=df[df['bol_non_rej_1t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_non_rej_1t']>1].sigla)[-1], y=list(df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['bol_non_rej_1t']>1].bol_non_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## ciro gomes

            fig.add_trace(go.Scatter(y=df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t, x=df[df['ciro_non_rej_1t']>1].sigla, mode='markers', name='Rejeição Ciro',
                                    marker=dict(
                                    size=5,
                                    color=df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t, #set color equal to a variable
                                    colorscale='Greens'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean(), x=df[df['ciro_non_rej_1t']>1].sigla,mode='lines', name='Ciro',
                                    line=dict(color='seagreen', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['ciro_non_rej_1t']>1].sigla)[-1], y=list(df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean())[-1],text=f"{int(list(df[df['ciro_non_rej_1t']>1].ciro_non_rej_1t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 20,
                        font=dict(size=20, color="black", family="Arial"))

            ## detalhes

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            title=("""
            <i>Média Móvel da rejeição dos sem religião por candidato à presidência (1º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)',
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            legend_title_text='<br><br><br><br><br><br>',
                            yaxis_title='Rejeição (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                orientation="v",
                font_family="arial",))

            #moro desiste
            fig.add_vline(x=str("mar/22_futura"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mar/22_futura", y=70,text="Moro<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #dória desiste
            fig.add_vline(x=str("mai/22_futura"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="mai/22_futura", y=70,text="Dória<br>desiste",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            ## campanha
            fig.add_vline(x=str("ago/22_datafolha"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            fig.add_annotation(x="ago/22_datafolha", y=70,text="Início da<br>Campanha",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #linha debate
            fig.add_annotation(x="ago/22_poderdata_3", y=70,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_poderdata_3"), line_width=.2, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=70,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.10,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            st.plotly_chart(fig,use_container_width=True)
            # info
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Método utilizado: média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df[df['lul_ger_rej_1t']>1].data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: Para o cálculo da rejeição dos sem religião utilizamos {len(df[df['lul_non_rej_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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
                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'cat_rej'
                rel = 'católicos'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)

            if rel == ' Evangélica ':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'ev_rej'
                rel = 'evangélicos'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)

            if rel == ' Espírita ':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'espi_rej'
                rel = 'espíritas'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            if rel == ' Sem Religião ':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'non_rej'
                rel = 'sem religião'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            if rel == ' Outras Religiosidades ':

                fonte = df.query(f"nome_instituto =='{inst}'")
                religi_escolhida = 'out_rej'
                rel = 'outras religiões'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                ##ciro gomes
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
                                        line=dict(color='green', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
                                        line=dict(color='green', width=1, dash='dot')))

                fig.update_layout(width = 800, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=70, l=80, b=4, t=160),
                        title=(f"""
                        Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
                                        xaxis_title='Mês, ano e instituto de pesquisa',
                                        yaxis_title='Intenção de voto (%)',
                                        font=dict(family="arial",size=13),
                                        legend=dict(
                            yanchor="auto",
                            y=1.13,
                            xanchor="auto",
                            x=0.4,
                            orientation="h",
                            font_family="arial",))
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,60])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=1.05, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=1.05, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            
            # if rel == ' Umbanda/Candomblé ':

            #     fonte = df.query(f"nome_instituto =='{inst}'")
            #     religi_escolhida = 'umb_can_rej'
            #     rel = 'umbanda e candomblé'

            #     fig = go.Figure()
            #     ##lula
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
            #     ##bolsonaro
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
            #                             line=dict(color='royalblue', width=2.5),legendrank=2))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
            #                             line=dict(color='royalblue', width=1, dash='dot')))
            #     ##ciro gomes
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
            #                             line=dict(color='green', width=2.5),legendrank=3))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
            #                             line=dict(color='green', width=1, dash='dot')))

            #     fig.update_layout(width = 1000, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            #             title=(f"""
            #             Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
            #             <br>
            #             <br>
            #             """),
            #                             xaxis_title='Mês, ano e instituto de pesquisa',
            #                             yaxis_title='Intenção de voto (%)',
            #                             font=dict(family="arial",size=13),
            #                             legend=dict(
            #                 yanchor="auto",
            #                 y=1.15,
            #                 xanchor="auto",
            #                 x=0.4,
            #                 orientation="h",
            #                 font_family="arial",))
            #     fig.update_xaxes(tickangle = 300,title_font_family="arial")
            #     fig.update_yaxes(range=[0,90])

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
            #             xref="paper", yref="paper",
            #             x=.99, y=1.03,
            #             sizex=0.1, sizey=0.1,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source=agre,
            #             xref="paper", yref="paper",
            #             x=.99, y=1.08,
            #             sizex=0.12, sizey=0.12,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )
                
            #     st.plotly_chart(fig,use_container_width=True)
            

            # if rel == ' Ateu ':

            #     fonte = df.query(f"nome_instituto =='{inst}'")
            #     religi_escolhida = 'ateu_rej'
            #     rel = 'ateus'

            #     fig = go.Figure()
            #     ##lula
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_1t'], mode='lines+markers', name=f"Lula - {rel}",
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_1t'],mode='lines+markers', name=f"Lula - geral", 
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
            #     ##bolsonaro
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_1t'], mode='lines+markers', name=f"Bolsonaro - {rel}",
            #                             line=dict(color='royalblue', width=2.5),legendrank=2))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_1t'],mode='lines+markers', name=f"Bolsonaro - geral", 
            #                             line=dict(color='royalblue', width=1, dash='dot')))
            #     ##ciro gomes
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'ciro_{religi_escolhida}_1t'], mode='lines+markers', name=f"Ciro Gomes - {rel}",
            #                             line=dict(color='green', width=2.5),legendrank=3))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['ciro_ger_1t'],mode='lines+markers', name=f"Ciro Gomes - geral", 
            #                             line=dict(color='green', width=1, dash='dot')))

            #     fig.update_layout(width = 810, height = 700, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            #             title=(f"""
            #             Rejeição 'geral' e de '{rel}' por candidato segundo '{inst.title()}' (1º turno)
            #             <br>
            #             <br>
            #             """),
            #                             xaxis_title='Mês, ano e instituto de pesquisa',
            #                             yaxis_title='Intenção de voto (%)',
            #                             font=dict(family="arial",size=13),
            #                             legend=dict(
            #                 yanchor="auto",
            #                 y=1.15,
            #                 xanchor="auto",
            #                 x=0.4,
            #                 orientation="h",
            #                 font_family="arial",))
            #     fig.update_xaxes(tickangle = 300,title_font_family="arial")
            #     fig.update_yaxes(range=[-0.5,95])

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
            #             xref="paper", yref="paper",
            #             x=1.05, y=1.03,
            #             sizex=0.1, sizey=0.1,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source=agre,
            #             xref="paper", yref="paper",
            #             x=1.05, y=1.08,
            #             sizex=0.12, sizey=0.12,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )
                
            #     st.plotly_chart(fig,use_container_width=True)
                

        st.markdown(f"""
        <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 1: O percentual da <i>rejeição</i> dos candidatos foi obtida pela resposta de eleitores que declaram "não votar de jeito nenhum” em determinado incumbente.</h7><br>
        <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 2: Os gráficos reproduzem os dados divulgados pelos institutos de pesquisa a partir do recorte religioso.</h7>
        """, unsafe_allow_html=True)
    st.markdown("---")

#################################################
##avaliação ruim e péssima do governo bolsonaro##   FICARÁ BLOQUEADO ATÉ O INÍCIO DAS ELEIÇÕES.
#################################################

    # st.markdown(f"""
    #     <h3 style='text-align: center; color: #303030; font-family:segoe UI; text-rendering: optimizelegibility;background-color: #FFD662;'>3. Avaliação do governo Bolsonaro</h3>
    #     """, unsafe_allow_html=True)
    # st.markdown("---")

    # ####################
    # ##resumo avaliação##
    # ####################

    # with st.container():
    #     st.markdown(f"""
    #     <br>
    #     <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EDF1FF;'>Resumo - avaliação ruim e péssima geral e por religião: </h3><br>
    #     <br>
    #     """, unsafe_allow_html=True)


    #     adm_bolsonaro = st.checkbox(' Selecione para visualizar os dados da avalização do governo Bolsonaro.')

    #     if adm_bolsonaro:

    #         ## coluna 1
    #         bol = Image.open('bolso_image.jpeg')
    #         col0,col, col1, col2, col3, col4 = st.columns(6)
    #         col0.image(bol,width=100)
    #         col.metric(label="Geral", value=f"{round(list(df[df['ava_gov_bol_GERAL']>1].ava_gov_bol_GERAL.rolling(m_m).mean())[-1],1)}%") 
    #         col1.metric(label="Católicos", value=f"{round(list(df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean())[-1],1)}%") 
    #         col2.metric(label="Evangélicos", value=f"{round(list(df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean())[-1],1)}%") 
    #         col3.metric(label="Outros", value=f"{round(list(df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean())[-1],1)}%") 
    #         col4.metric(label="Sem Religião", value=f"{round(list(df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean())[-1],1)}%")
    #         #col3.metric(label="Espíritas", value=f"{round(list(df[df['ava_gov_bol_espi']>1].ava_gov_bol_espi.rolling(m_m).mean())[-1],1)}%") 
    #         st.markdown(f"""
    #         <br>
    #         <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
    #         <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia <i>{list(df[df['ava_gov_bol_GERAL']>1].data)[-1].strftime(format='%d-%m-%Y')}</i></h7><br>
    #         <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Para a produção dos dados da <i>aprovação</i> do governo bolsonaro utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais. Destacamos a reprovação por segmento religioso através da soma dos percentuais das respostas 'ruim e péssimo'.</h7><br>
    #         <br>
    #         """, unsafe_allow_html=True)
    #     st.markdown("---")

############################
###Avaliação por religião###
############################

    # with st.container():
    #     st.markdown(f"""
    #     <h3 style='text-align: left; color: #303030; font-family:Segoe UI; text-rendering: optimizelegibility; background-color: #EDF1FF;'><svg xmlns="http://www.w3.org/2000/svg" width="30" height="26" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 18">
    #     <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
    #     </svg> Avaliação ruim e péssima por religião:</h3><br>
    #     """, unsafe_allow_html=True)

    #     aval_vote_med_move = st.checkbox('Selecione para visualizar o gráfico da avaliação do governo Bolsonaro')

    #     if aval_vote_med_move:

    #         fig = go.Figure()

    #         ## católicos

    #         fig.add_trace(go.Scatter(y=df.ava_gov_bol_cat, x=df.sigla, mode='markers', name='aval_cat',
    #                                 marker=dict(
    #                                 size=5,
    #                                 color=df.ava_gov_bol_cat, #set color equal to a variable
    #                                 colorscale='peach')))

    #         fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean(), x=df[df['ava_gov_bol_cat']>1].sigla, mode='lines', name='católicos',
    #                                 line=dict(color='#802b00', width=2.5)))

    #         fig.add_annotation(x=list(df[df['ava_gov_bol_cat']>1].sigla)[-1], y=list(df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['ava_gov_bol_cat']>1].ava_gov_bol_cat.rolling(m_m).mean())[-1])}%",
    #                     showarrow=True,
    #                     arrowhead=1,
    #                     ax = 40, ay = 0,
    #                     font=dict(size=20, color="black", family="Arial"))


    #         ## evangélicos

    #         fig.add_trace(go.Scatter(y=df.ava_gov_bol_ev, x=df.sigla, mode='markers', name='aval_ev',
    #                                 marker=dict(
    #                                 size=5,
    #                                 color=df.ava_gov_bol_ev, #set color equal to a variable
    #                                 colorscale='tropic')))

    #         fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean(), x=df[df['ava_gov_bol_ev']>1].sigla,mode='lines', name='evangélicos',
    #                                 line=dict(color='#80ccff', width=2.5)))

    #         fig.add_annotation(x=list(df[df['ava_gov_bol_ev']>1].sigla)[-1], y=list(df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['ava_gov_bol_ev']>1].ava_gov_bol_ev.rolling(m_m).mean())[-1])}%",
    #                     showarrow=True,
    #                     arrowhead=1,
    #                     ax = 40, ay = 0,
    #                     font=dict(size=20, color="black", family="Arial"))

    #         ## outras religiões

    #         fig.add_trace(go.Scatter(y=df.ava_gov_bol_out, x=df.sigla, mode='markers', name='aval_out',
    #                                 marker=dict(
    #                                 size=5,
    #                                 color=df.ava_gov_bol_out, #set color equal to a variable
    #                                 colorscale='Greens')))

    #         fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean(), x=df[df['ava_gov_bol_out']>1].sigla,mode='lines', name='outras religiões',
    #                                 line=dict(color='#808080', width=2.5)))

    #         fig.add_annotation(x=list(df[df['ava_gov_bol_out']>1].sigla)[-1], y=list(df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['ava_gov_bol_out']>1].ava_gov_bol_out.rolling(m_m).mean())[-1])}%",
    #                     showarrow=True,
    #                     arrowhead=1,
    #                     ax = 40, ay = 0,
    #                     font=dict(size=20, color="black", family="Arial"))


    #         ## sem religião 

    #         fig.add_trace(go.Scatter(y=df.ava_gov_bol_non, x=df.sigla, mode='markers', name='aval_sem_religião',
    #                                  marker=dict(
    #                                  size=5,
    #                                  color=df.ava_gov_bol_non, #set color equal to a variable
    #                                  colorscale='Greens')))

    #         fig.add_trace(go.Scatter(y=df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean(), x=df[df['ava_gov_bol_non']>1].sigla,mode='lines', name='aval_sem_religião',
    #                                  line=dict(color='seagreen', width=2.5)))

    #         fig.add_annotation(x=list(df[df['ava_gov_bol_non']>1].sigla)[-1], y=list(df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['ava_gov_bol_non']>1].ava_gov_bol_non.rolling(m_m).mean())[-1])}%",
    #                      showarrow=True,
    #                      arrowhead=1,
    #                      ax = 40, ay = 0,
    #                      font=dict(size=20, color="black", family="Arial"))

    #         ## detalhes

    #         fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
    #         title=("""
    #         <i>Avaliação negativa de Bolsonaro por religião (1º turno)<i><br>
    #         """),
    #                         xaxis_title='Mês, ano e instituto de pesquisa',
    #                         yaxis_title='Rejeição (%)',
    #                         font=dict(family="arial",size=13),
    #                         legend=dict(
    #             yanchor="auto",
    #             y=1.1,
    #             xanchor="auto",
    #             x=0.5,
    #             orientation="h",
    #             font_family="arial",))

    #         fig.add_annotation(x="mar/22_fsb", y=35,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
    #         fig.add_annotation(x="mai/22_fsb", y=32,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))

    #         fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

    #         # Add image
    #         fig.add_layout_image(
    #             dict(
    #                 source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
    #                 xref="paper", yref="paper",
    #                 x=.99, y=1.12,
    #                 sizex=0.1, sizey=0.1,
    #                 xanchor="right", yanchor="bottom"
    #             )
    #         )

    #         # Add image
    #         fig.add_layout_image(
    #             dict(
    #                 source=agre,
    #                 xref="paper", yref="paper",
    #                 x=.99, y=1.20,
    #                 sizex=0.12, sizey=0.12,
    #                 xanchor="right", yanchor="bottom"
    #             )
    #         )

    #         st.plotly_chart(fig,use_container_width=True)

            
    #         ## info
    #     st.markdown(f"""
    #     <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado para o cálculo: média móvel de {m_m} dias.</h7><br>
    #     <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Para a produção dos gráficos sobre a <i>aprovação</i> do governo bolsonaro utilizamos {len(df[df['lul_ger_rej_1t']>1])} pesquisas eleitorais. Destacamos a reprovação por segmento religioso através do registro das respostas 'ruim e péssimo'.</h7><br>
    #     """, unsafe_allow_html=True)
    #     st.markdown("---")


#############################################################################################################################
                                                        ### segundo turno ######
#############################################################################################################################

if options_turn == 'Segundo Turno':

    st.markdown(f"""
        <h2 style='text-align: center; color: #303030; font-family:tahoma; text-rendering: optimizelegibility'>Segundo Turno</h2>
        <br>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"""
        <h3 style='text-align: center; color: #303030; font-family:segoe UI; text-rendering: optimizelegibility;background-color: #FFD662;'>1. Intenção de voto:</h3>
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
            col2.metric(label="Evangélicos", value=f"{round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1],1) - round(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1],1),1)}")
            col3.metric(label="Espíritas", value=f"{round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)}%") #, delta=f"{round(round(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1],1)-round(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1],1),1)}")
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
            col0, col, col1, col2, col3, col4, col5 = st.columns(7)
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
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: Método utilizado: média móvel de {m_m} dias.</h7> \n
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no resumo correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Para o cálculo do resumo da média móvel das intenções de voto geral ao segundo turno utilizou-se {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
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
            fig.add_trace(go.Scatter(y=df.lul_ger_2t, x=df.sigla, mode='markers', name='Int. voto Lula',
                                    marker=dict(
                                    size=5,
                                    color=df.lul_ger_2t, #set color equal to a variable
                                    colorscale='peach'),legendrank=2))

            fig.add_trace(go.Scatter(y=df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean(), x=df[df['bol_ger_2t']>1].sigla,mode='lines', name='Lula',
                                    line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

            fig.add_annotation(x=list(df[df['lul_ger_2t']>1].sigla)[-1], y=list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_ger_2t']>1].lul_ger_2t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Bolsonaro
            fig.add_trace(go.Scatter(y=df.bol_ger_2t, x=df.sigla, mode='markers', name='Int. voto Bolsonaro',
                                    marker=dict(
                                    size=5,
                                    color=df.lul_ger_2t, #set color equal to a variable
                                    colorscale='ice'),legendrank=4))

            fig.add_trace(go.Scatter(y=df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean(), x=df[df['bol_ger_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                    line=dict(color='skyblue', width=2.5),legendrank=3))

            fig.add_annotation(x=list(df[df['bol_ger_2t']>1].sigla)[-1], y=list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_ger_2t']>1].bol_ger_2t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                    ax = 40, ay = 0,
                        font=dict(size=20, color="black", family="Arial"))

            ## Brancos, Nulos, NS, NR 

            fig.add_trace(go.Scatter(y=df.bra_nul_ns_nr_ger_2t, x=df.sigla, mode='markers', name='Brancos, nulos, NS e NR',
                                    marker=dict(
                                    size=5,
                                    color=df.bra_nul_ns_nr_ger_2t, #set color equal to a variable
                                    colorscale='gray'),legendrank=6))

            fig.add_trace(go.Scatter(y=df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t.rolling(m_m).mean(), x=df[df['bra_nul_ns_nr_ger_2t']>1].sigla, mode='lines', name='Brancos, nulos, NS e NR',
                                    line=dict(color='gray', width=2.5),legendrank=5))

            fig.add_annotation(x=list(df[df['bra_nul_ns_nr_ger_2t']>1].sigla)[-1], y=list(df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bra_nul_ns_nr_ger_2t']>1].bra_nul_ns_nr_ger_2t.rolling(m_m).mean())[-1])}%",
                        showarrow=True,
                        arrowhead=1,
                        ax = 40, ay = -8,
                        font=dict(size=20, color="black", family="Arial"))

            fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=2, t=150),
            title=("""
            <i>Média móvel das intenções de voto de candidatos à presidência (2º turno)<i><br>
            """),
            plot_bgcolor='rgb(255, 255, 255)',
            paper_bgcolor='rgb(255, 255, 255)', 
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            font=dict(family="arial",size=13),
                            legend_title_text='<br><br><br><br><br><br>',
                            legend=dict(
                
                orientation="v",
                font_family="arial"))

            fig.add_annotation(x="mar/22_poderdata_3", y=33,text="Moro<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="mai/22_poderdata_2", y=34,text="Dória<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            #fig.add_annotation(x="jun/22_fsb_2", y=35,text="Datena<br>desiste",showarrow=True,arrowhead=1,yanchor="bottom",ax = -15, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_ipespe", y=52,text="Candidatura<br>Lula (PT)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = -30,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="jul/22_futura", y=35,text="Candidatura<br>Bolsonaro<br>(PL)",showarrow=True,arrowhead=1,yanchor="bottom",ax = 0, ay = 56,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_quaest"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha debate
            fig.add_annotation(x="ago/22_quaest_2", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("ago/22_quaest_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            #linha 7 de setembro
            fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
            ##linha 2o turno
            fig.add_annotation(x="out/22_ipec", y=65,text="<b>Resultado<br>1º turno</b>",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_ipec", y=58,text="Votos 1º turno:<br>Lula=48,4%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_ipec", y=30,text="Votos 1º turno:<br>Bolsonaro=43,2%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("out/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
            ##resultado 2o turno
            fig.add_annotation(x="out/22_datafolha_6", y=65,text="<b>Resultado<br>2º turno</b>",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_datafolha_6", y=58,text="Votos 2º turno:<br>Lula=50,9%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_annotation(x="out/22_datafolha_6", y=30,text="Votos 2º turno:<br>Bolsonaro=49,1%",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
            fig.add_vline(x=str("out/22_datafolha_6"), line_width=.5, line_dash="dot", line_color="black", opacity=.4)

            fig.update_xaxes(tickangle = 300,rangeslider_visible=False,title_font_family="Arial")

            # Add image
            fig.add_layout_image(
                dict(
                    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                    xref="paper", yref="paper",
                    x=.99, y=1.02,
                    sizex=0.1, sizey=0.1,
                    xanchor="right", yanchor="bottom"
                )
            )

            # Add image
            fig.add_layout_image(
                dict(
                    source=agre,
                    xref="paper", yref="paper",
                    x=.99, y=1.08,
                    sizex=0.12, sizey=0.12,
                    xanchor="right", yanchor="bottom"
                )
            )

            fig.update_yaxes(range=[0,70])

            st.plotly_chart(fig,use_container_width=True)
            st.markdown(f"""
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: *Método utilizado:* média móvel de {m_m} dias.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral ao segundo turno utilizou-se {len(df[df['lul_ger_1t']>1])} pesquisas eleitorais.</h7><br>
            <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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
        fig.add_trace(go.Scatter(y=df.lul_cat_2t, x=df.sigla, mode='markers', name='Lula ',
                                marker=dict(
                                size=5,
                                color=df.lul_cat_2t, #set color equal to a variable
                                colorscale='peach'),legendrank=2))

        fig.add_trace(go.Scatter(y=df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean(), x=df[df['bol_cat_2t']>1].sigla,mode='lines', name='Int. voto Lula',
                                line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

        fig.add_annotation(x=list(df[df['lul_cat_2t']>1].sigla)[-1], y=list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_cat_2t']>1].lul_cat_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df.bol_cat_2t, x=df.sigla, mode='markers', name='Int. voto Bolsonaro',
                                marker=dict(
                                size=5,
                                color=df.lul_cat_2t, #set color equal to a variable
                                colorscale='ice'),legendrank=4))

        fig.add_trace(go.Scatter(y=df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean(), x=df[df['bol_cat_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5),legendrank=3))

        fig.add_annotation(x=list(df[df['bol_cat_2t']>1].sigla)[-1], y=list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_cat_2t']>1].bol_cat_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos, Nulos 

        fig.add_trace(go.Scatter(y=df.bra_nulo_cat_2t, x=df.sigla, mode='markers', name='Brancos e nulos',
                                marker=dict(
                                size=5,
                                color=df.bra_nulo_cat_2t, #set color equal to a variable
                                colorscale='gray'),legendrank=6))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_cat_2t']>1].bra_nulo_cat_2t.rolling(m_m).mean(), x=df[df['bra_nulo_cat_2t']>1].sigla, mode='lines', name='Brancos e nulos',
                                line=dict(color='gray', width=2.5),legendrank=5))

        fig.add_annotation(x=list(df[df['bra_nulo_cat_2t']>1].sigla)[-1], y=list(df[df['bra_nulo_cat_2t']>1].bra_nulo_cat_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bra_nulo_cat_2t']>1].bra_nulo_cat_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff',margin=dict(r=80, l=80, b=2, t=150),
                            title="""
                            <i>Média móvel das intenções de voto de católicos por candidato à presidência (2º turno)<i><br>
                            """,
                            plot_bgcolor='rgb(255, 255, 255)',
                            paper_bgcolor='rgb(255, 255, 255)', 
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                
                orientation="v",
                font_family="arial"))

        fig.add_vline(x=str("ago/22_quaest"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        #linha debate
        fig.add_annotation(x="ago/22_quaest_2", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("ago/22_quaest_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)       
        #linha 7 de setembro
        fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        ##linha 2o turno
        fig.add_annotation(x="out/22_ipec", y=65,text="Pesquisas<br>2º turno",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("out/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        

        fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
        fig.update_yaxes(range=[0,70])


       # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.05,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.13,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )

        st.plotly_chart(fig,use_container_width=True)


    if relig2t == 'Evangélica ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df.lul_ev_2t, x=df.sigla, mode='markers', name='Int. voto Lula',
                                marker=dict(
                                size=5,
                                color=df.lul_ev_2t, #set color equal to a variable
                                colorscale='peach'),legendrank=2))

        fig.add_trace(go.Scatter(y=df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean(), x=df[df['bol_ev_2t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

        fig.add_annotation(x=list(df[df['lul_ev_2t']>1].sigla)[-1], y=list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_ev_2t']>1].lul_ev_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))
        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df.bol_ev_2t, x=df.sigla, mode='markers', name='Int. voto Bolsonaro',
                                marker=dict(
                                size=5,
                                color=df.lul_ev_2t, #set color equal to a variable
                                colorscale='ice'),legendrank=4))

        fig.add_trace(go.Scatter(y=df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean(), x=df[df['bol_ev_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5),legendrank=3))

        fig.add_annotation(x=list(df[df['bol_ev_2t']>1].sigla)[-1], y=list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_ev_2t']>1].bol_ev_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))
        
        ## Brancos, Nulos 

        fig.add_trace(go.Scatter(y=df.bra_nulo_ev_2t, x=df.sigla, mode='markers', name='Brancos e nulos',
                                marker=dict(
                                size=5,
                                color=df.bra_nulo_ev_2t, #set color equal to a variable
                                colorscale='gray'),legendrank=6))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_ev_2t']>1].bra_nulo_ev_2t.rolling(m_m).mean(), x=df[df['bra_nulo_ev_2t']>1].sigla, mode='lines', name='Brancos e nulos',
                                line=dict(color='gray', width=2.5),legendrank=5))

        fig.add_annotation(x=list(df[df['bra_nulo_ev_2t']>1].sigla)[-1], y=list(df[df['bra_nulo_ev_2t']>1].bra_nulo_ev_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bra_nulo_ev_2t']>1].bra_nulo_ev_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff',margin=dict(r=80, l=80, b=2, t=150),
                            title="""
                            <i>Média móvel das intenções de voto de evangélicos por candidato à presidência (2º turno)<i><br>
                            """,
                            plot_bgcolor='rgb(255, 255, 255)',
                            paper_bgcolor='rgb(255, 255, 255)', 
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                
                orientation="v",
                font_family="arial"))
            
        fig.add_vline(x=str("ago/22_quaest"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        #linha debate
        fig.add_annotation(x="ago/22_quaest_2", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("ago/22_quaest_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        #linha 7 de setembro
        fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        ##linha 2o turno
        fig.add_annotation(x="out/22_ipec", y=65,text="Pesquisas<br>2º turno",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("out/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)

        fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
        fig.update_yaxes(range=[0,70])


        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.05,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.13,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )      

        st.plotly_chart(fig,use_container_width=True)

    if relig2t == 'Sem Religião ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df.lul_non_2t, x=df.sigla, mode='markers', name='Int. voto Lula',
                                marker=dict(
                                size=5,
                                color=df.lul_non_2t, #set color equal to a variable
                                colorscale='peach'),legendrank=2))

        fig.add_trace(go.Scatter(y=df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean(), x=df[df['bol_non_2t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

        fig.add_annotation(x=list(df[df['lul_non_2t']>1].sigla)[-1], y=list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_non_2t']>1].lul_non_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df.bol_non_2t, x=df.sigla, mode='markers', name='Int. voto Bolsonaro',
                                marker=dict(
                                size=5,
                                color=df.lul_non_2t, #set color equal to a variable
                                colorscale='ice'),legendrank=4))

        fig.add_trace(go.Scatter(y=df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean(), x=df[df['bol_non_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5),legendrank=3))

        fig.add_annotation(x=list(df[df['bol_non_2t']>1].sigla)[-1], y=list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_non_2t']>1].bol_non_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Brancos, Nulos 

        fig.add_trace(go.Scatter(y=df.bra_nulo_non_2t, x=df.sigla, mode='markers', name='Brancos e nulos',
                                marker=dict(
                                size=5,
                                color=df.bra_nulo_non_2t, #set color equal to a variable
                                colorscale='gray'),legendrank=6))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_non_2t']>1].bra_nulo_non_2t.rolling(m_m).mean(), x=df[df['bra_nulo_non_2t']>1].sigla, mode='lines', name='Brancos e nulos',
                                line=dict(color='gray', width=2.5),legendrank=5))

        fig.add_annotation(x=list(df[df['bra_nulo_non_2t']>1].sigla)[-1], y=list(df[df['bra_nulo_non_2t']>1].bra_nulo_non_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bra_nulo_non_2t']>1].bra_nulo_non_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff',margin=dict(r=80, l=80, b=2, t=150),
                            title="""
                            <i>Média móvel das intenções de voto dos sem religião por candidato à presidência (2º turno)<i><br>
                            """,
                            plot_bgcolor='rgb(255, 255, 255)',
                            paper_bgcolor='rgb(255, 255, 255)', 
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            legend_title_text='<br><br><br><br><br><br>',
                            yaxis_title='Intenção de voto (%)',
                            font=dict(family="arial",size=13),
                            legend=dict(
                
                orientation="v",
                font_family="arial"))

        fig.add_vline(x=str("ago/22_quaest"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        #linha debate
        fig.add_annotation(x="ago/22_quaest_2", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("ago/22_quaest_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        #linha 7 de setembro
        fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        ##linha 2o turno
        fig.add_annotation(x="out/22_ipec", y=65,text="Pesquisas<br>2º turno",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("out/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)

        fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
        fig.update_yaxes(range=[0,70])


        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.05,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.13,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )      

        st.plotly_chart(fig,use_container_width=True)

    if relig2t == 'Outras Religiosidades ':
        fig = go.Figure()
        ## lula
        fig.add_trace(go.Scatter(y=df[df['lul_out_2t']>1].lul_out_2t, x=df[df['lul_out_2t']>1].sigla, mode='markers', name='Int. voto Lula',
                                marker=dict(
                                size=5,
                                color=df[df['lul_out_2t']>1].lul_out_2t, #set color equal to a variable
                                colorscale='peach'),legendrank=2))

        fig.add_trace(go.Scatter(y=df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean(), x=df[df['bol_out_2t']>1].sigla,mode='lines', name='Lula',
                                line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))

        fig.add_annotation(x=list(df[df['lul_out_2t']>1].sigla)[-1], y=list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_out_2t']>1].lul_out_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))

        ## Bolsonaro
        fig.add_trace(go.Scatter(y=df[df['bol_out_2t']>1].bol_out_2t, x=df[df['bol_out_2t']>1].sigla, mode='markers', name='Int. voto Bolsonaro',
                                marker=dict(
                                size=5,
                                color=df[df['bol_out_2t']>1].lul_out_2t, #set color equal to a variable
                                colorscale='ice'),legendrank=4))

        fig.add_trace(go.Scatter(y=df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean(), x=df[df['bol_out_2t']>1].sigla,mode='lines', name='Bolsonaro',
                                line=dict(color='skyblue', width=2.5),legendrank=3))

        fig.add_annotation(x=list(df[df['bol_out_2t']>1].sigla)[-1], y=list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_out_2t']>1].bol_out_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = 0,
                    font=dict(size=20, color="black", family="Arial"))
        
        ## Brancos, Nulos 

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_out_2t']>1].bra_nulo_out_2t, x=df[df['bra_nulo_out_2t']>1].sigla, mode='markers', name='Brancos e nulos',
                                marker=dict(
                                size=5,
                                color=df[df['bra_nulo_out_2t']>1].bra_nulo_out_2t, #set color equal to a variable
                                colorscale='gray'),legendrank=6))

        fig.add_trace(go.Scatter(y=df[df['bra_nulo_out_2t']>1].bra_nulo_out_2t.rolling(m_m).mean(), x=df[df['bra_nulo_out_2t']>1].sigla, mode='lines', name='Brancos e nulos',
                                line=dict(color='gray', width=2.5),legendrank=5))

        fig.add_annotation(x=list(df[df['bra_nulo_out_2t']>1].sigla)[-1], y=list(df[df['bra_nulo_out_2t']>1].bra_nulo_out_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bra_nulo_out_2t']>1].bra_nulo_out_2t.rolling(m_m).mean())[-1])}%",
                    showarrow=True,
                    arrowhead=1,
                    ax = 40, ay = -8,
                    font=dict(size=20, color="black", family="Arial"))

        fig.update_layout(width = 1100, height = 800, template = 'plotly_white+xgridoff',margin=dict(r=80, l=80, b=2, t=150),
                            title="""
                            <i>Média móvel das intenções de voto de católicos por candidato à presidência (2º turno)<i><br>
                            """,
                            plot_bgcolor='rgb(255, 255, 255)',
                            paper_bgcolor='rgb(255, 255, 255)', 
                            xaxis_title='Mês, ano e instituto de pesquisa',
                            yaxis_title='Intenção de voto (%)',
                            legend_title_text='<br><br><br><br><br><br>',
                            font=dict(family="arial",size=13),
                            legend=dict(
                
                orientation="v",
                font_family="arial"))
        #linha inicio da campanha
        fig.add_vline(x=str("ago/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)
        #linha debate
        fig.add_annotation(x="ago/22_ipec_2", y=65,text="1º Debate<br>na TV",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("ago/22_ipec_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        #linha 7 de setembro
        fig.add_annotation(x="set/22_datafolha_2", y=65,text="7 de<br>setembro",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("set/22_datafolha_2"), line_width=.3, line_dash="dot", line_color="black", opacity=.5)
        ##linha 2o turno
        fig.add_annotation(x="out/22_ipec", y=65,text="Pesquisas<br>2º turno",showarrow=False,arrowhead=1,yanchor="bottom",ax = 0, ay = 40,font=dict(size=10, color="black", family="Arial"))
        fig.add_vline(x=str("out/22_ipec"), line_width=.5, line_dash="dot", line_color="black", opacity=.5)

        fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
        fig.update_yaxes(range=[0,70])


        # Add image
        fig.add_layout_image(
            dict(
                source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                xref="paper", yref="paper",
                x=.99, y=1.05,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )
        )

        # Add image
        fig.add_layout_image(
            dict(
                source=agre,
                xref="paper", yref="paper",
                x=.99, y=1.13,
                sizex=0.12, sizey=0.12,
                xanchor="right", yanchor="bottom"
            )
        )      

        st.plotly_chart(fig,use_container_width=True)

        # if relig2t == 'Espírita ':
    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_espi_2t']>1].lul_espi_2t, x=df[df['lul_espi_2t']>1].data, mode='markers', name='int_vot_espi_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_espi_2t']>1].lul_espi_2t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean(), x=df[df['bol_espi_2t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_espi_2t']>1].data)[-1], y=list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_espi_2t']>1].lul_espi_2t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['bol_espi_2t']>1].data)[-1], y=list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_espi_2t']>1].bol_espi_2t.rolling(m_m).mean())[-1])}%",
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

    #     fig.update_xaxes(tickangle = 300,rangeslider_visible=False)

    #     st.plotly_chart(fig,use_container_width=True)

    # if relig2t == 'Umbanda/Candomblé ':

    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_umb_can_2t']>1].lul_umb_can_2t, x=df[df['lul_umb_can_2t']>1].data, mode='markers', name='int_vot_umb_can_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_umb_can_2t']>1].lul_umb_can_2t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean(), x=df[df['bol_umb_can_2t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_umb_can_2t']>1].data)[-1], y=list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_umb_can_2t']>1].lul_umb_can_2t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['bol_umb_can_2t']>1].data)[-1], y=list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_umb_can_2t']>1].bol_umb_can_2t.rolling(m_m).mean())[-1])}%",
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

    #     fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
    #     st.plotly_chart(fig,use_container_width=True)

    # if relig2t == 'Ateu ':
    #     fig = go.Figure()
    #     ## lula
    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_2t']>1].lul_ateu_2t, x=df[df['lul_ateu_2t']>1].data, mode='markers', name='int_vot_ateu_lula',
    #                             marker=dict(
    #                             size=5,
    #                             color=df[df['lul_ateu_2t']>1].lul_ateu_2t, #set color equal to a variable
    #                             colorscale='peach')))

    #     fig.add_trace(go.Scatter(y=df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean(), x=df[df['bol_ateu_2t']>1].data,mode='lines', name='Lula',
    #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5)))

    #     fig.add_annotation(x=list(df[df['lul_ateu_2t']>1].data)[-1], y=list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['lul_ateu_2t']>1].lul_ateu_2t.rolling(m_m).mean())[-1])}%",
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

    #     fig.add_annotation(x=list(df[df['bol_ateu_2t']>1].data)[-1], y=list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1] ,text=f"{int(list(df[df['bol_ateu_2t']>1].bol_ateu_2t.rolling(m_m).mean())[-1])}%",
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

    #     fig.update_xaxes(tickangle = 300,rangeslider_visible=False)
    #     st.plotly_chart(fig,use_container_width=True)

        st.caption('**Obs.:** Em alguns casos, a combinção de dados retornará um gráfico em branco. \n Isso indica que instituto de pesquisa selecionado não coletou dados da categoria.')

    st.markdown(f"""
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 1: *Método utilizado:* média móvel de {m_m} dias.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 2: Os valores indicados no gráfico correspondem a última média da série temporal registrada no dia *{list(df.data)[-1].strftime(format='%d-%m-%Y')}*</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 3: Para o cálculo da média móvel da intenção de voto geral ao segundo turno utilizou-se {len(df[df['lul_ger_2t']>1])} pesquisas eleitorais.</h7><br>
        <h7 style='text-align: left; color:#606060;font-family:arial'>Nota 4: A linha pontilhada indica o período de início da campanha eleitoral oficial (15/08).</h7><br>
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

                fonte = df.query(f"nome_instituto =='{inst2}'")
                religi_escolhida = 'cat'
                rel2 = 'católicos'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                
                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)


            if rel2== 'Evangélica':

                fonte = df.query(f"nome_instituto =='{inst2}'")
                religi_escolhida = 'ev'
                rel2= 'evangélicos'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                
                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)


            if rel2== 'Espírita':

                fonte = df.query(f"nome_instituto =='{inst2}'")
                religi_escolhida = 'espi'
                rel2= 'espíritas'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                
                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            

            if rel2== 'Sem Religião':

                fonte = df.query(f"nome_instituto =='{inst2}'")
                religi_escolhida = 'non'
                rel2= 'sem religião'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
                                        line=dict(color='royalblue', width=2.5),legendrank=2))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot')))
                
                fig.update_layout(width = 800, height = 700, template = 'plotly_white', margin=dict(r=80, l=80, b=4, t=150),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
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
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,70])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=.99, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=.99, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            

            if rel2== 'Outras Religiosidades':

                fonte = df.query(f"nome_instituto =='{inst2}'")
                religi_escolhida = 'out'
                rel2= 'outras religiões'

                fig = go.Figure()
                ##lula
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
                                        line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot'),legendrank=2))
                ##bolsonaro
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
                                        line=dict(color='royalblue', width=2.5),legendrank=3))
                fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
                                        line=dict(color='royalblue', width=1, dash='dot'),legendrank=4))
                
                fig.update_layout(width = 800, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=70, l=80, b=4, t=160),
                        title=(f"""
                        Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
                        <br>
                        <br>
                        """),
                        plot_bgcolor='rgb(255, 255, 255)',
                        paper_bgcolor='rgb(255, 255, 255)', 
                                        xaxis_title='Mês, ano e instituto de pesquisa',
                                        yaxis_title='Intenção de voto (%)',
                                        font=dict(family="arial",size=13),
                                        legend=dict(
                            yanchor="auto",
                            y=1.13,
                            xanchor="auto",
                            x=0.4,
                            orientation="h",
                            font_family="arial",))
                fig.update_xaxes(tickangle = 300,title_font_family="arial")
                fig.update_yaxes(range=[0,60])

                # Add image
                fig.add_layout_image(
                    dict(
                        source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
                        xref="paper", yref="paper",
                        x=1.05, y=1.03,
                        sizex=0.1, sizey=0.1,
                        xanchor="right", yanchor="bottom"
                    )
                )

                # Add image
                fig.add_layout_image(
                    dict(
                        source=agre,
                        xref="paper", yref="paper",
                        x=1.05, y=1.08,
                        sizex=0.12, sizey=0.12,
                        xanchor="right", yanchor="bottom"
                    )
                )
                
                st.plotly_chart(fig,use_container_width=True)
            
            
            # if rel2== 'Umbanda/Candomblé':

            #     fonte = df.query(f"nome_instituto =='{inst2}'")
            #     religi_escolhida = 'umb_can'
            #     rel2= 'umbanda e candomblé'

            #     fig = go.Figure()
            #     ##lula
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
            #     ##bolsonaro
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
            #                             line=dict(color='royalblue', width=2.5),legendrank=2))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
            #                             line=dict(color='royalblue', width=1, dash='dot')))
            #
            #     fig.update_layout(width = 1000, height = 800, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            #             title=(f"""
            #             Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
            #             <br>
            #             <br>
            #             """),
            #                             xaxis_title='Mês, ano e instituto de pesquisa',
            #                             yaxis_title='Intenção de voto (%)',
            #                             font=dict(family="arial",size=13),
            #                             legend=dict(
            #                 yanchor="auto",
            #                 y=1.15,
            #                 xanchor="auto",
            #                 x=0.4,
            #                 orientation="h",
            #                 font_family="arial",))
            #     fig.update_xaxes(tickangle = 300,title_font_family="arial")
            #     fig.update_yaxes(range=[0,90])

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
            #             xref="paper", yref="paper",
            #             x=.99, y=1.03,
            #             sizex=0.1, sizey=0.1,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source=agre,
            #             xref="paper", yref="paper",
            #             x=.99, y=1.08,
            #             sizex=0.12, sizey=0.12,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )
                
            #     st.plotly_chart(fig,use_container_width=True)
            

            # if rel2== 'Ateu':

            #     fonte = df.query(f"nome_instituto =='{inst2}'")
            #     religi_escolhida = 'ateu'
            #     rel2= 'ateus'

            #     fig = go.Figure()
            #     ##lula
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'lul_{religi_escolhida}_2t'], mode='lines+markers', name=f"Lula - {rel2}",
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=2.5),legendrank=1))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['lul_ger_2t'],mode='lines+markers', name=f"Lula - geral", 
            #                             line=dict(color='rgba(215, 0, 0, 0.8)', width=1, dash='dot')))
            #     ##bolsonaro
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte[f'bol_{religi_escolhida}_2t'], mode='lines+markers', name=f"Bolsonaro - {rel2}",
            #                             line=dict(color='royalblue', width=2.5),legendrank=2))
            #     fig.add_trace(go.Scatter(x=fonte['sigla'], y=fonte['bol_ger_2t'],mode='lines+markers', name=f"Bolsonaro - geral", 
            #                             line=dict(color='royalblue', width=1, dash='dot')))

            #     fig.update_layout(width = 810, height = 700, template = 'plotly_white+xgridoff', margin=dict(r=80, l=80, b=4, t=150),
            #             title=(f"""
            #             Intenção de voto 'geral' e de '{rel2}' por candidato segundo '{inst2.title()}' (2º turno)
            #             <br>
            #             <br>
            #             """),
            #                             xaxis_title='Mês, ano e instituto de pesquisa',
            #                             yaxis_title='Intenção de voto (%)',
            #                             font=dict(family="arial",size=13),
            #                             legend=dict(
            #                 yanchor="auto",
            #                 y=1.15,
            #                 xanchor="auto",
            #                 x=0.4,
            #                 orientation="h",
            #                 font_family="arial",))
            #     fig.update_xaxes(tickangle = 300,title_font_family="arial")
            #     fig.update_yaxes(range=[-0.5,95])

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
            #             xref="paper", yref="paper",
            #             x=1.05, y=1.03,
            #             sizex=0.1, sizey=0.1,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )

            #     # Add image
            #     fig.add_layout_image(
            #         dict(
            #             source=agre,
            #             xref="paper", yref="paper",
            #             x=1.05, y=1.08,
            #             sizex=0.12, sizey=0.12,
            #             xanchor="right", yanchor="bottom"
            #         )
            #     )
                
            #     st.plotly_chart(fig,use_container_width=True)
        
        st.markdown(f"""
        <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 1: Os gráficos reproduzem os dados divulgados pelos institutos de pesquisa a partir do recorte religioso. Em alguns casos os institutos não coletam tais informações.</h7><br>
        <h7 style='text-align: center; color:#606060;font-family:arial'>Nota 2: Os gráficos com linhas descontinuadas indicam que o instituto não coletou a informação em determinada pesquisa. Um exemplo pode ser visto a partir da combinação "Paraná Pesquisas" e "católicos".</h7>
        """, unsafe_allow_html=True)

    st.markdown("---")



st.caption(f"""
<br>
<br>
Site publicado em: 15/05/2022.<br>
Lançamento: 03/08/2022.<br>
Última atualização: {end_date.strftime(format='%d/%m/%Y')}
""", unsafe_allow_html=True)
