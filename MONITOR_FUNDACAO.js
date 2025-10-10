// 📊 SISTEMA DE MONITORAMENTO CONTÍNUO DA FUNDAÇÃO
// Monitora todos os sistemas 24/7

class MonitorFundacao {
  constructor() {
    this.sistemas = [
      { nome: 'Portal Central', url: '/central', status: 'pending' },
      { nome: 'Revelação Real', url: '/revelacao-real', status: 'pending' },
      { nome: 'Metadados Reais', url: '/metadados-reais', status: 'pending' },
      { nome: 'Verificador Conexões', url: '/verificador-conexoes', status: 'pending' },
      { nome: 'Árvore da Vida', url: '/arvore-da-vida', status: 'pending' }
    ];
    this.intervalo = 300000; // 5 minutos
  }

  async iniciarMonitoramento() {
    console.log('🔍 INICIANDO MONITORAMENTO DA FUNDAÇÃO...');
    
    setInterval(() => {
      this.verificarSistemas();
    }, this.intervalo);
  }

  async verificarSistemas() {
    const baseURL = 'https://fundacao-alquimista-anatheron-qcaqxopuo.vercel.app';
    
    for (let sistema of this.sistemas) {
      try {
        const response = await fetch(`${baseURL}${sistema.url}`);
        sistema.status = response.ok ? 'online' : 'offline';
        sistema.ultimaVerificacao = new Date().toISOString();
      } catch (error) {
        sistema.status = 'error';
        sistema.erro = error.message;
      }
    }

    this.gerarRelatorio();
  }

  gerarRelatorio() {
    const online = this.sistemas.filter(s => s.status === 'online').length;
    const total = this.sistemas.length;
    
    console.log(`📊 RELATÓRIO ${new Date().toLocaleString('pt-BR')}:`);
    console.log(`   ✅ ${online}/${total} sistemas online`);
    
    this.sistemas.forEach(sistema => {
      const status = sistema.status === 'online' ? '✅' : '❌';
      console.log(`   ${status} ${sistema.nome}: ${sistema.status}`);
    });
  }
}

module.exports = MonitorFundacao;
