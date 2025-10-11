'use client';

export default function CommunicationLab({ conexoes = [] }) {
  const defaultConexoes = [
    { nome: "Zennith Core", status: "connected", forca: 98 },
    { nome: "Quantum Network", status: "connected", forca: 95 },
    { nome: "Neural Interface", status: "connected", forca: 97 }
  ];

  const conexoesParaUsar = conexoes.length > 0 ? conexoes : defaultConexoes;

  return (
    <div className="p-6 bg-purple-900 bg-opacity-30 rounded-lg border border-purple-500">
      <h3 className="text-2xl font-bold mb-4 text-purple-400">📡 CommunicationLab</h3>
      <p className="text-purple-300 mb-4">
        Sistema de Comunicação Quântica e Interfaces Neurais
      </p>
      <div className="space-y-3">
        {conexoesParaUsar.map((conexao, index) => (
          <div key={index} className="flex justify-between items-center p-3 bg-gray-800 rounded">
            <span className="font-medium">{conexao.nome}</span>
            <span className="text-green-400">🟢 {conexao.forca || 95}%</span>
          </div>
        ))}
      </div>
    </div>
  );
}
