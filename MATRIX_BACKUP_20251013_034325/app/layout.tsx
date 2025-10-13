// LAYOUT ROBUSTO - ZERO CONFLITOS
export const metadata = {
  title: 'Fundação Alquimista - Matriz LUX.NET',
  description: 'Sistema de Gestão Quântica consolidado',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body style={{ 
        margin: 0, 
        padding: 0,
        overflowX: 'hidden'
      }}>
        {children}
      </body>
    </html>
  );
}
