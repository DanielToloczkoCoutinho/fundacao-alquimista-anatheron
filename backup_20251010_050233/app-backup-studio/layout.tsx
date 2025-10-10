export const metadata = {
  title: 'Fundação Alquimista Quântica',
  description: 'Sistema de Realidade Virtual Quântica',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt">
      <body className="bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white">
        {children}
      </body>
    </html>
  );
}
