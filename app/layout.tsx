import React from 'react';

export const metadata = {
  title: 'Fundação Alquimista - Liga Quântica',
  description: 'Montando o quebra-cabeça cósmico juntos',
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
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        minHeight: '100vh'
      }}>
        {children}
      </body>
    </html>
  );
}
