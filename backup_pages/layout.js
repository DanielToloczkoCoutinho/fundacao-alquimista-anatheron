import './globals.css'

export const metadata = {
  title: 'Fundação Alquimista - Nexus Central',
  description: 'Sistema Interdimensional de Monitoramento Quântico',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body className="bg-black text-white min-h-screen">
        <main className="min-h-screen">
          {children}
        </main>
      </body>
    </html>
  )
}
