import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ command }) => ({
  plugins: [react()],
  // './' é obrigatório: o Streamlit serve o componente a partir de um caminho interno
  // (/component/agregador_component.agregador/...), não da raiz do site.
  base: './',
  // public/ guarda só o dev-payload.json (dados de teste): não vai para o build
  publicDir: command === 'serve' ? 'public' : false,
  build: { outDir: 'build', chunkSizeWarningLimit: 2000 },
  server: { port: 3001 },
}))
