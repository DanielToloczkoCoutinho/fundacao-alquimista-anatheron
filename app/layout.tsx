export const metadata = {
  title: 'Fundação Alquimista',
  description: 'Sistema Online',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body style={{ 
        margin: 0, 
        padding: '2rem', 
        fontFamily: 'Arial, sans-serif',
        background: '#0a0a0a',
        color: 'white'
      }}>
        {children}
      </body>
    </html>
  )
}
