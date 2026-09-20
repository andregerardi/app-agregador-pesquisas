// Ponte mínima com o Streamlit (protocolo de "custom components").
// Evita a dependência streamlit-component-lib (e o apache-arrow que vem junto):
// como o Python envia apenas JSON, as três mensagens abaixo bastam.

const dentroDoStreamlit = window.parent !== window

function enviar(type, dados = {}) {
  window.parent.postMessage({ isStreamlitMessage: true, type, ...dados }, '*')
}

export const Streamlit = {
  dentroDoStreamlit,

  /** Registra o callback que recebe os argumentos enviados pelo Python. */
  aoRenderizar(callback) {
    window.addEventListener('message', (evento) => {
      if (evento.data?.type === 'streamlit:render') callback(evento.data.args ?? {})
    })
    enviar('streamlit:componentReady', { apiVersion: 1 })
  },

  /** Ajusta a altura do iframe ao conteúdo (o Streamlit não faz isso sozinho). */
  ajustarAltura(altura) {
    enviar('streamlit:setFrameHeight', { height: Math.ceil(altura) })
  },

  /** Devolve um valor ao Python (retorno da função do componente). */
  enviarValor(valor) {
    enviar('streamlit:setComponentValue', { value: valor, dataType: 'json' })
  },
}
