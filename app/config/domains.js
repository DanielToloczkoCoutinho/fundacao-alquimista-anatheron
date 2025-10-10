// 🎯 CONFIGURAÇÃO DE DOMÍNIOS DEFINITIVA
export const DOMINIOS = {
  PRINCIPAL: "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app",
  ATUAL: "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app"
}

export const isDominioPrincipal = () => {
  if (typeof window !== 'undefined') {
    return window.location.origin === DOMINIOS.PRINCIPAL
  }
  return true
}

export const redirecionarParaPrincipal = () => {
  if (typeof window !== 'undefined') {
    window.location.href = DOMINIOS.PRINCIPAL + window.location.pathname
  }
}
