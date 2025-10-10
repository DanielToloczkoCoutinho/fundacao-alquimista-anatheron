'use client';

export default function EnergyLab({ metricas = {} }) {
  return (
    <div className="p-6 bg-green-900 bg-opacity-30 rounded-lg border border-green-500">
      <h3 className="text-2xl font-bold mb-4 text-green-400">⚡ EnergyLab</h3>
      <p className="text-green-300 mb-4">
        Sistema de Energia Quântica e Dobramento Proteico
      </p>
      <div className="space-y-3">
        <div className="flex justify-between">
          <span>Dobramento Proteico:</span>
          <span className="text-green-400">{metricas.dobramentoProteico || 94.7}%</span>
        </div>
        <div className="flex justify-between">
          <span>Fotossíntese Quântica:</span>
          <span className="text-green-400">{metricas.fotossinteseQuantica || 96.9}%</span>
        </div>
        <div className="flex justify-between">
          <span>Eficiência Energética:</span>
          <span className="text-green-400">{metricas.eficienciaEnergetica || 97.9}%</span>
        </div>
      </div>
    </div>
  );
}
