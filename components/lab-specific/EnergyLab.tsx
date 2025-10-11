interface EnergyLabProps {
  dados?: {
    dobramentoProteico?: number;
    fotossinteseQuantica?: number;
    eficienciaEnergetica?: number;
  };
}

export default function EnergyLab({ dados = {} }: EnergyLabProps) {
  const {
    dobramentoProteico = 85,
    fotossinteseQuantica = 92,
    eficienciaEnergetica = 78
  } = dados;

  return (
    <div style={{ 
      padding: '20px', 
      background: '#1a2a1a', 
      borderRadius: '8px',
      border: '1px solid #00ff88',
      margin: '10px 0'
    }}>
      <h3 style={{ color: '#00ff88', margin: '0 0 15px 0' }}>🧪 Energy Lab</h3>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '10px' }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '1.5em', fontWeight: 'bold', color: '#00ff88' }}>
            {dobramentoProteico}%
          </div>
          <div style={{ fontSize: '0.8em', opacity: 0.8 }}>Dobramento Proteico</div>
        </div>
        
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '1.5em', fontWeight: 'bold', color: '#00ff88' }}>
            {fotossinteseQuantica}%
          </div>
          <div style={{ fontSize: '0.8em', opacity: 0.8 }}>Fotossíntese Quântica</div>
        </div>
        
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '1.5em', fontWeight: 'bold', color: '#00ff88' }}>
            {eficienciaEnergetica}%
          </div>
          <div style={{ fontSize: '0.8em', opacity: 0.8 }}>Eficiência Energética</div>
        </div>
      </div>
    </div>
  );
}
