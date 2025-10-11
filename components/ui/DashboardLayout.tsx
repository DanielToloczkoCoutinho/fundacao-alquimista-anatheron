import { ReactNode } from 'react';

interface DashboardLayoutProps {
  children: ReactNode;
}

export default function DashboardLayout({ children }: DashboardLayoutProps) {
  return (
    <div style={{ 
      minHeight: '100vh',
      background: '#0a0a0a',
      color: '#ffffff',
      fontFamily: 'monospace'
    }}>
      <header style={{
        padding: '20px',
        background: '#1a1a1a',
        borderBottom: '2px solid #00ffff',
        textAlign: 'center'
      }}>
        <h1 style={{ margin: 0, color: '#00ffff' }}>🏗️ Dashboard Layout</h1>
        <p style={{ margin: '5px 0 0 0', opacity: 0.8 }}>Layout simplificado</p>
      </header>
      
      <main style={{
        padding: '20px',
        maxWidth: '1200px',
        margin: '0 auto'
      }}>
        {children}
      </main>
      
      <footer style={{
        padding: '20px',
        background: '#1a1a1a',
        borderTop: '2px solid #00ffff',
        textAlign: 'center',
        marginTop: '40px'
      }}>
        <p style={{ margin: 0, opacity: 0.8 }}>Fundação Alquimista © 2025</p>
      </footer>
    </div>
  );
}
