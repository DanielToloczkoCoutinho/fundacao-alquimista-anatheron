export default function AccessControl({ level = "user" }) {
  return (
    <div className="p-4 bg-blue-900 bg-opacity-30 rounded-lg border border-blue-500">
      <h3 className="text-lg font-bold text-blue-400 mb-2">Controle de Acesso</h3>
      <p className="text-blue-300">Nível: {level}</p>
    </div>
  );
}
