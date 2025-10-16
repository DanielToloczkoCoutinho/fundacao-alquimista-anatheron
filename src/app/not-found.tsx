export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-900 to-blue-900">
      <div className="text-center text-white">
        <h1 className="text-6xl font-bold mb-4">404</h1>
        <p className="text-xl mb-8">Página não encontrada</p>
        <a href="/" className="bg-white text-purple-900 px-6 py-3 rounded-lg font-bold">
          Voltar para Home
        </a>
      </div>
    </div>
  )
}
