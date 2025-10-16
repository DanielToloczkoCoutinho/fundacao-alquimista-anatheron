'use client'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-red-900 to-orange-900">
      <div className="text-center text-white">
        <h1 className="text-6xl font-bold mb-4">Erro</h1>
        <p className="text-xl mb-4">Algo deu errado</p>
        <button
          onClick={reset}
          className="bg-white text-red-900 px-6 py-3 rounded-lg font-bold"
        >
          Tentar novamente
        </button>
      </div>
    </div>
  )
}
