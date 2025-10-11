export default function InterfacesIndex() {
  const interfaces = [
    {
      name: "🌌 Painel Interativo",
      path: "/painel-interativo",
      description: "Métricas vivas dos 3 reinos alquimistas",
      status: "✅ Online"
    },
    {
      name: "🗺️ Mapa Dimensional", 
      path: "/mapa-dimensional",
      description: "Rotas entre interfaces, scripts e módulos",
      status: "✅ Online"
    },
    {
      name: "📈 Relatório de Sinergia",
      path: "/relatorio-sinergia", 
      description: "Análise de redundâncias e oportunidades",
      status: "✅ Online"
    },
    {
      name: "📊 Dashboard Principal",
      path: "/dashboard",
      description: "Monitoramento em tempo real do sistema",
      status: "✅ Online"
    },
    {
      name: "🔮 Metadados Reais",
      path: "/metadados-reais",
      description: "Dados vivos e coerência vibracional",
      status: "✅ Online"
    },
    {
      name: "🧪 Laboratórios",
      path: "/laboratorios",
      description: "5 laboratórios especializados",
      status: "✅ Online"
    },
    {
      name: "🌌 Nexus",
      path: "/nexus", 
      description: "Sistema multidimensional central",
      status: "✅ Online"
    },
    {
      name: "🔗 Status URLs",
      path: "/status-urls",
      description: "Monitoramento de interfaces",
      status: "✅ Online"
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
        <h1 style={{ fontSize: '3em', marginBottom: '10px', textAlign: 'center' }}>🌐 ÍNDICE DE INTERFACES</h1>
        <p style={{ fontSize: '1.2em', marginBottom: '40px', textAlign: 'center', opacity: 0.8 }}>
          Fundação Alquimista - Sistema Multidimensional
        </p>

        <div style={{ 
          background: '#1a1a1a', 
          padding: '30px', 
          borderRadius: '15px',
          border: '2px solid #00ffff',
          marginBottom: '40px',
          textAlign: 'center'
        }}>
          <h2>📊 SISTEMA ORGANIZADO</h2>
          <p>8 interfaces ativas | 284K arquivos | 87% coerência</p>
          <p><strong>URL Canônica:</strong> https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app</p>
        </div>

        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', 
          gap: '25px' 
        }}>
          {interfaces.map((iface, index) => (
            <a 
              key={index}
              href={iface.path}
              style={{
                display: 'block',
                background: 'linear-gradient(135deg, #1a1a1a, #2a1a2a)',
                padding: '25px',
                borderRadius: '12px',
                border: '2px solid #00ffff',
                textDecoration: 'none',
                color: '#00ffff',
                transition: 'all 0.3s ease',
                boxShadow: '0 0 20px rgba(0, 255, 255, 0.1)'
              }}
              onMouseOver="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 0 30px rgba(0, 255, 255, 0.2)'"
              onMouseOut="this.style.transform='translateY(0)'; this.style.boxShadow='0 0 20px rgba(0, 255, 255, 0.1)'"
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
                <h3 style={{ margin: 0, fontSize: '1.4em' }}>{iface.name}</h3>
                <span style={{ 
                  background: '#00ff00', 
                  color: '#000',
                  padding: '5px 10px',
                  borderRadius: '15px',
                  fontSize: '0.8em',
                  fontWeight: 'bold'
                }}>
                  {iface.status}
                </span>
              </div>
              <p style={{ margin: 0, opacity: 0.8, lineHeight: '1.5' }}>{iface.description}</p>
              <div style={{ marginTop: '15px', fontSize: '0.9em', opacity: 0.6 }}>
                🔗 {iface.path}
              </div>
            </a>
          ))}
        </div>

        <div style={{ 
          marginTop: '40px', 
          padding: '25px', 
          background: '#1a2a2a', 
          borderRadius: '10px',
          textAlign: 'center'
        }}>
          <h3>🎯 STATUS DO SISTEMA</h3>
          <p>Coerência Vibracional: 87% | Interfaces Ativas: 8 | Scripts: 1.937</p>
          <p>👤 Operador: Daniel Toloczko Coutinho | 🚀 Sistema: Online</p>
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
            timestamp.innerHTML = '🕒 Índice atualizado em: ' + new Date().toLocaleString();
            document.body.appendChild(timestamp);
          });
        `
      }} />
    </div>
  );
}
