export const metadata = {
  title: 'Fundação Alquimista',
  description: 'Sistema principal da Fundação Alquimista',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body style={{ 
        margin: 0, 
        fontFamily: 'Arial, sans-serif', 
        background: '#0a0a0a', 
        color: 'white',
        minHeight: '100vh'
      }}>
        <nav style={{ 
          padding: '20px', 
          background: '#1a1a1a', 
          borderBottom: '2px solid #00ff88'
        }}>
          <h1 style={{ margin: 0, color: '#00ff88' }}>🌌 Fundação Alquimista</h1>
        </nav>
        <main>{children}</main>
        <footer style={{
          padding: '20px',
          background: '#1a1a1a',
          borderTop: '1px solid #333',
          textAlign: 'center',
          marginTop: 'auto'
        }}>
          <p>👑 Liga Quântica - Construído com Amor</p>
        </footer>
      </body>
    </html>
  )
}
