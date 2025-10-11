export default function InterfacesDocs() {
  const interfaceDocs = [
    {
      name: "🌌 Painel Interativo",
      path: "/painel-interativo",
      purpose: "Monitoramento em tempo real dos 3 reinos alquimistas",
      features: ["Métricas vivas", "Status vibracional", "Sinergia entre reinos"],
      dataSources: ["status_deploy.json", "ciclos_espectrais.js"],
      status: "Produção"
    },
    {
      name: "🗺️ Mapa Dimensional", 
      path: "/mapa-dimensional",
      purpose: "Visualização das rotas entre componentes do sistema",
      features: ["Grafo de conexões", "Tipos de componentes", "Interatividade"],
      dataSources: ["Estrutura App Router", "Scripts críticos"],
      status: "Produção"
    },
    {
      name: "📈 Relatório de Sinergia",
      path: "/relatorio-sinergia",
      purpose: "Análise de redundâncias e oportunidades de otimização", 
      features: ["Identificação de redundâncias", "Núcleos órfãos", "Zonas de expansão"],
      dataSources: ["Inventário sistema", "Análise arquitetural"],
      status: "Produção"
    },
    {
      name: "📊 Dashboard Principal",
      path: "/dashboard",
      purpose: "Interface principal de monitoramento do sistema",
      features: ["Visão geral", "Métricas chave", "Alertas"],
      dataSources: ["Sistema em tempo real"],
      status: "Produção"
    },
    {
      name: "🔮 Metadados Reais", 
      path: "/metadados-reais",
      purpose: "Apresentação dos dados vivos e coerência vibracional",
      features: ["Dados dinâmicos", "Coerência em tempo real", "Status operacional"],
      dataSources: ["Metadados do sistema"],
      status: "Produção"
    },
    {
      name: "🧪 Laboratórios",
      path: "/laboratorios", 
      purpose: "Portal para os 5 laboratórios especializados",
      features: ["Energy Lab", "Neural Lab", "Communication Lab", "Healing Lab", "Zenith Lab"],
      dataSources: ["Laboratórios especializados"],
      status: "Produção"
    },
    {
      name: "🌌 Nexus",
      path: "/nexus",
      purpose: "Sistema multidimensional central da fundação", 
      features: ["Integração multidimensional", "Portal central", "Navegação unificada"],
      dataSources: ["Sistema completo"],
      status: "Produção"
    },
    {
      name: "🔗 Status URLs",
      path: "/status-urls",
      purpose: "Monitoramento e verificação de todas as interfaces",
      features: ["Verificação de URLs", "Status de disponibilidade", "Alertas"],
      dataSources: ["Verificação em tempo real"],
      status: "Produção"
    }
  ];

  return (
    <div style={{ 
      padding: '40px', 
      background: '#0a0a0a', 
      color: '#00ffff',
      fontFamily: 'Courier New, monospace',
      minHeight: '100vh'
    }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <h1 style={{ fontSize: '3em', marginBottom: '10px', textAlign: 'center' }}>📚 DOCUMENTAÇÃO</h1>
        <p style={{ fontSize: '1.2em', marginBottom: '40px', textAlign: 'center', opacity: 0.8 }}>
          Interfaces da Fundação Alquimista - Especificações e Propósitos
        </p>

        <div style={{ 
          background: '#1a1a1a', 
          padding: '30px', 
          borderRadius: '15px',
          border: '2px solid #00ffff',
          marginBottom: '40px'
        }}>
          <h2 style={{ textAlign: 'center' }}>🏗️ ARQUITETURA DO SISTEMA</h2>
          <p style={{ textAlign: 'center' }}>
            <strong>8 Interfaces Ativas</strong> | <strong>Next.js App Router</strong> | <strong>Deploy Vercel</strong><br/>
            <strong>URL Base:</strong> https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app
          </p>
        </div>

        {interfaceDocs.map((doc, index) => (
          <div 
            key={index}
            style={{
              background: 'linear-gradient(135deg, #1a1a1a, #2a1a2a)',
              padding: '30px',
              borderRadius: '12px',
              border: '2px solid #00ffff',
              marginBottom: '25px',
              boxShadow: '0 0 20px rgba(0, 255, 255, 0.1)'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '20px' }}>
              <div>
                <h2 style={{ margin: '0 0 10px 0', fontSize: '1.8em' }}>{doc.name}</h2>
                <p style={{ margin: 0, opacity: 0.8, fontSize: '1.1em' }}>{doc.purpose}</p>
              </div>
              <span style={{ 
                background: doc.status === 'Produção' ? '#00ff00' : '#ffaa00', 
                color: '#000',
                padding: '5px 15px',
                borderRadius: '20px',
                fontSize: '0.9em',
                fontWeight: 'bold'
              }}>
                {doc.status}
              </span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
              <div>
                <h3 style={{ margin: '0 0 10px 0', color: '#00ffff' }}>🎯 Funcionalidades</h3>
                <ul style={{ margin: 0, paddingLeft: '20px', opacity: 0.9 }}>
                  {doc.features.map((feature, idx) => (
                    <li key={idx} style={{ marginBottom: '5px' }}>{feature}</li>
                  ))}
                </ul>
              </div>
              
              <div>
                <h3 style={{ margin: '0 0 10px 0', color: '#00ffff' }}>📡 Fontes de Dados</h3>
                <ul style={{ margin: 0, paddingLeft: '20px', opacity: 0.9 }}>
                  {doc.dataSources.map((source, idx) => (
                    <li key={idx} style={{ marginBottom: '5px' }}>{source}</li>
                  ))}
                </ul>
              </div>
            </div>

            <div style={{ marginTop: '20px', padding: '15px', background: 'rgba(0,255,255,0.1)', borderRadius: '8px' }}>
              <strong>🔗 Rota:</strong> {doc.path} | <strong>🌐 URL Completa:</strong> https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app{doc.path}
            </div>
          </div>
        ))}

        <div style={{ 
          marginTop: '40px', 
          padding: '25px', 
          background: '#1a2a2a', 
          borderRadius: '10px',
          textAlign: 'center'
        }}>
          <h3>📖 ESPECIFICAÇÕES TÉCNICAS</h3>
          <p><strong>Framework:</strong> Next.js 15 | <strong>Deploy:</strong> Vercel | <strong>Arquitetura:</strong> App Router</p>
          <p><strong>Estilo:</strong> CSS-in-JS | <strong>Interatividade:</strong> Client-side Scripting</p>
          <p><strong>Organização:</strong> 8 interfaces documentadas e ativas</p>
        </div>
      </div>

      <script dangerouslySetInnerHTML={{
        __html: `
          document.addEventListener('DOMContentLoaded', function() {
            const timestamp = document.createElement('div');
            timestamp.style.marginTop = '30px';
            timestamp.style.padding = '15px';
            timestamp.style.background = '#1a1a1a';
            timestamp.style.borderRadius = '8px';
            timestamp.style.textAlign = 'center';
            timestamp.style.fontSize = '0.9em';
            timestamp.innerHTML = '📅 Documentação atualizada em: ' + new Date().toLocaleString();
            document.body.appendChild(timestamp);
          });
        `
      }} />
    </div>
  );
}
