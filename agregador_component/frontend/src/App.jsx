import React, { useState } from 'react'
import Info, { Hero } from './pages/Info.jsx'
import Eleicao2022 from './pages/Eleicao2022.jsx'
import Eleicao2026 from './pages/Eleicao2026.jsx'
import { Divisor } from './components/ui.jsx'

export default function App({ payload }) {
  const { config, e2022, e2026 } = payload
  const [eleicao, setEleicao] = useState(null) // fica só no navegador: trocar é instantâneo, sem rerun

  return (
    <main className="pagina">
      <Hero />
      <Divisor />
      <Info rows={e2022.rows} mM={config.m_m} mM15={config.m_m15} />
      <Divisor />

      <div className="eleicoes">
        <span className="rotulo-mono">Escolha a eleição</span>
        <div className="eleicoes-botoes">
          {['2022', '2026'].map((ano) => (
            <button key={ano} type="button" className={eleicao === ano ? 'botao-eleicao ativa' : 'botao-eleicao'} aria-pressed={eleicao === ano} onClick={() => setEleicao(ano)}>
              Eleições {ano}
            </button>
          ))}
        </div>
      </div>
      <Divisor />

      {eleicao === null && (
        <p className="aviso">Selecione <b>Eleições 2022</b> ou <b>Eleições 2026</b> para explorar os dados por turno.</p>
      )}
      {eleicao === '2022' && <Eleicao2022 dados={e2022} config={config} />}
      {eleicao === '2026' && <Eleicao2026 dados={e2026} config={config} />}

      <footer className="rodape">
        Site publicado em: 15/05/2022.<br />
        Lançamento: 03/08/2022.<br />
        Última atualização: {config.atualizacao}
      </footer>
    </main>
  )
}
