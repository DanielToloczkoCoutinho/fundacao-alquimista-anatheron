// 📊 SISTEMA DE MONITORAMENTO CONTÍNUO E REPORTING AVANÇADO
// [CÓDIGO ANTERIOR MANTER...]

      {
        nome: 'SISTEMAS_CRITICOS_ONLINE',
        valor: this.contarSistemasCriticosOnline(),
        unidade: 'sistemas', 
        limiteAlerta: 4 // Todos os sistemas críticos devem estar online
      },
      {
        nome: 'TEMPO_ATIVIDADE_ININTERRUPTA',
        valor: this.calcularUptime(),
        unidade: 'horas',
        limiteAlerta: 0.99 // 99% de disponibilidade
      }
    ];

    this.metricasTempoReal.set('ultimaColeta', metricas);
    return metricas;
  }

  // Processar alertas automáticos em caso de falhas
  async processarAlertas(statusSistemas, metricas) {
    const alertas = [];

    // Verificar sistemas offline
    statusSistemas.forEach(sistema => {
      if (!sistema.online && sistema.critico) {
        alertas.push(this.criarAlerta(
          'SISTEMA_CRITICO_OFFLINE',
          `Sistema crítico ${sistema.nome} está offline`,
          'ALTA',
          sistema
        ));
      }
    });

    // Verificar métricas fora do limite
    metricas.forEach(metrica => {
      if (metrica.valor > metrica.limiteAlerta) {
        alertas.push(this.criarAlerta(
          'METRICA_FORA_LIMITE',
          `Métrica ${metrica.nome} está em ${metrica.valor}${metrica.unidade} (limite: ${metrica.limiteAlerta})`,
          'MEDIA',
          metrica
        ));
      }
    });

    this.alertasAtivos = alertas;
    return alertas;
  }

  // Inicializar dashboards em tempo real
  inicializarDashboardsTempoReal() {
    const dashboards = {
      dashboardPrincipal: {
        nome: 'DASHBOARD PRINCIPAL DA FUNDAÇÃO',
        widgets: [
          {
            tipo: 'STATUS_SISTEMAS',
            titulo: 'Status dos Sistemas Críticos',
            atualizacao: 'TEMPO_REAL'
          },
          {
            tipo: 'METRICAS_CHAVE', 
            titulo: 'Métricas de Performance',
            atualizacao: 'TEMPO_REAL'
          },
          {
            tipo: 'ALERTAS_ATIVOS',
            titulo: 'Alertas e Notificações',
            atualizacao: 'INSTANTANEO'
          },
          {
            tipo: 'EVOLUCAO_TEMPO',
            titulo: 'Evolução Temporal',
            atualizacao: '5_MINUTOS'
          }
        ]
      },
      dashboardDNA: {
        nome: 'DASHBOARD ATIVAÇÃO DNA ESTELAR',
        widgets: [
          {
            tipo: 'PROGRESSO_ATIVACOES',
            titulo: 'Progresso das Ativações Globais',
            atualizacao: 'TEMPO_REAL'
          },
          {
            tipo: 'METRICAS_DNA',
            titulo: 'Métricas de Evolução do DNA',
            atualizacao: '15_MINUTOS'
          }
        ]
      }
    };

    this.dashboards.set('principal', dashboards);
    return dashboards;
  }

  // Atualizar dashboards com dados em tempo real
  async atualizarDashboards(statusSistemas, metricas, alertas) {
    const dadosDashboard = {
      statusSistemas,
      metricas, 
      alertas,
      timestamp: new Date().toISOString(),
      ciclo: Date.now()
    };

    // Atualizar todos os dashboards
    this.dashboards.forEach((dashboard, key) => {
      dashboard.ultimaAtualizacao = new Date().toISOString();
      dashboard.dados = dadosDashboard;
    });

    return dadosDashboard;
  }

  // Gerar relatórios periódicos consolidados
  gerarRelatorioCiclo(cicloId, statusSistemas, metricas, alertas) {
    const relatorio = {
      cicloId,
      timestamp: new Date().toISOString(),
      resumo: {
        sistemasMonitorados: statusSistemas.length,
        sistemasOnline: statusSistemas.filter(s => s.online).length,
        sistemasCriticosOnline: statusSistemas.filter(s => s.online && s.critico).length,
        alertasAtivos: alertas.length,
        disponibilidadeGeral: this.calcularDisponibilidadeGlobal()
      },
      detalhes: {
        statusSistemas,
        metricas,
        alertas
      },
      recomendacoes: this.gerarRecomendacoes(statusSistemas, alertas)
    };

    return relatorio;
  }

  // Métodos auxiliares
  calcularLatenciaMedia() {
    const ultimaVerificacao = this.sistemasMonitorados.get('ultimaVerificacao') || [];
    const tempos = ultimaVerificacao.filter(s => s.online).map(s => s.tempoResposta);
    return tempos.length > 0 ? tempos.reduce((a, b) => a + b, 0) / tempos.length : 0;
  }

  calcularDisponibilidadeGlobal() {
    const ultimaVerificacao = this.sistemasMonitorados.get('ultimaVerificacao') || [];
    const online = ultimaVerificacao.filter(s => s.online).length;
    const total = ultimaVerificacao.length;
    return total > 0 ? (online / total) * 100 : 0;
  }

  contarSistemasCriticosOnline() {
    const ultimaVerificacao = this.sistemasMonitorados.get('ultimaVerificacao') || [];
    return ultimaVerificacao.filter(s => s.online && s.critico).length;
  }

  calcularUptime() {
    // Implementação simplificada - na realidade seria baseado em histórico
    return 99.99;
  }

  criarAlerta(tipo, mensagem, severidade, dados) {
    const alerta = {
      id: this.alertasAtivos.length + 1,
      tipo,
      mensagem,
      severidade,
      dados,
      timestamp: new Date().toISOString(),
      status: 'ATIVO'
    };

    // Emitir notificação em tempo real
    this.emitirNotificacao(alerta);
    
    return alerta;
  }

  emitirNotificacao(alerta) {
    console.log(`🚨 ALERTA [${alerta.severidade}]: ${alerta.mensagem}`);
    // Na implementação real, isso enviaria notificações para sistemas de alerta
  }

  atualizarMetricaTempoReal(nomeSistema, dados) {
    this.metricasTempoReal.set(nomeSistema, {
      ...dados,
      historico: this.metricasTempoReal.get(nomeSistema)?.historico || []
    });
  }

  gerarRecomendacoes(statusSistemas, alertas) {
    const recomendacoes = [];

    if (alertas.length > 0) {
      recomendacoes.push('REVISAR_ALERTAS_ATIVOS');
    }

    const sistemasOffline = statusSistemas.filter(s => !s.online && s.critico);
    if (sistemasOffline.length > 0) {
      recomendacoes.push('RESTABELECER_SISTEMAS_CRITICOS_OFFLINE');
    }

    const latencia = this.calcularLatenciaMedia();
    if (latencia > 1000) {
      recomendacoes.push('OTIMIZAR_PERFORMANCE_REDE');
    }

    return recomendacoes;
  }

  // Método para gerar relatório gerencial
  gerarRelatorioGerencial(periodo = '24h') {
    return {
      periodo,
      timestamp: new Date().toISOString(),
      metricasChave: {
        disponibilidade: this.calcularDisponibilidadeGlobal(),
        latenciaMedia: this.calcularLatenciaMedia(),
        uptime: this.calcularUptime(),
        alertasResolvidos: this.alertasAtivos.filter(a => a.status === 'RESOLVIDO').length
      },
      analiseTendencia: 'EVOLUCAO_POSITIVA',
      pontosAtencao: this.alertasAtivos.filter(a => a.severidade === 'ALTA'),
      proximosPassos: this.gerarRecomendacoes(
        this.sistemasMonitorados.get('ultimaVerificacao') || [],
        this.alertasAtivos
      )
    };
  }
}

// 🧪 EXECUÇÃO DO SISTEMA DE MONITORAMENTO
console.log('📊 INICIANDO SISTEMA DE MONITORAMENTO CONTÍNUO...');

const monitor = new MonitoramentoContinuoReporting();

// Iniciar monitoramento
monitor.iniciarMonitoramento24_7()
  .then(status => {
    console.log('✅ MONITORAMENTO INICIADO:', status);
    
    // Gerar relatório inicial após 5 minutos
    setTimeout(() => {
      const relatorio = monitor.gerarRelatorioGerencial();
      console.log('📈 RELATÓRIO GERENCIAL INICIAL:', relatorio);
    }, 300000);
  })
  .catch(error => {
    console.error('❌ ERRO AO INICIAR MONITORAMENTO:', error);
  });

module.exports = MonitoramentoContinuoReporting;
