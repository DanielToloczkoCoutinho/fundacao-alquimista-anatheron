export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body style={{ margin: 0, fontFamily: "Arial" }}>
        <nav style={{ padding: "20px", background: "#1a1a1a", color: "white" }}>
          🌌 Fundação Alquimista
        </nav>
        <main>{children}</main>
      </body>
    </html>
  )
}
