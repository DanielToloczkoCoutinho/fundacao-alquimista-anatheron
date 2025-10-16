export const metadata = {
  title: 'Fundação Alquimista - Portal Multidimensional',
  description: 'Portal oficial da Fundação Alquimista - Liga Quântica ativada',
  verification: {
    google: '029QvH3OWC_BIGV997SfA9xFbDrBR1bLAPopdvqKuto'
  }
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <head>
        <meta name="google-site-verification" content="029QvH3OWC_BIGV997SfA9xFbDrBR1bLAPopdvqKuto" />
      </head>
      <body>{children}</body>
    </html>
  )
}
