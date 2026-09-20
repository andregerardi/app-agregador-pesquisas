import React, { useEffect, useRef, useState } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { Streamlit } from './streamlit.js'
import './styles.css'

function Raiz() {
  const [payload, setPayload] = useState(null)
  const [erro, setErro] = useState(null)
  const ref = useRef(null)

  // 1) recebe os dados: do Python (produção) ou de /dev-payload.json (npm run dev)
  useEffect(() => {
    if (Streamlit.dentroDoStreamlit) {
      Streamlit.aoRenderizar((args) => setPayload(args.payload))
    } else {
      fetch('./dev-payload.json')
        .then((r) => r.json())
        .then(setPayload)
        .catch(() => setErro('Fora do Streamlit: gere o arquivo public/dev-payload.json com "python exportar_payload.py".'))
    }
  }, [])

  // 2) mantém a altura do iframe igual à do conteúdo
  useEffect(() => {
    if (!ref.current) return
    const obs = new ResizeObserver(() => Streamlit.ajustarAltura(ref.current.scrollHeight + 24))
    obs.observe(ref.current)
    return () => obs.disconnect()
  }, [])

  return (
    <div ref={ref}>
      {erro && <p className="aviso">{erro}</p>}
      {!erro && !payload && <p className="aviso">Carregando os dados das pesquisas…</p>}
      {payload && <App payload={payload} />}
    </div>
  )
}

createRoot(document.getElementById('root')).render(<Raiz />)
