export default function Laboratorios() {
  return (
    <div className="min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-8">🧪 Laboratórios Quânticos</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-purple-800 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-4">Lab 001 - Síntese Dimensional</h2>
          <p className="text-purple-200">Status: Ativo</p>
        </div>
        <div className="bg-blue-800 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-4">Lab 002 - Transmutação Alquímica</h2>
          <p className="text-blue-200">Status: Calibrando</p>
        </div>
        <div className="bg-green-800 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-4">Lab 003 - Portal VR</h2>
          <p className="text-green-200">Status: Online</p>
        </div>
      </div>
    </div>
  );
}
