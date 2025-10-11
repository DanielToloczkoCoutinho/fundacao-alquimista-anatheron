import { ReactNode } from 'react';

interface LazyLoaderProps {
  children: ReactNode;
}

export default function LazyLoader({ children }: LazyLoaderProps) {
  return (
    <div style={{ 
      padding: '20px', 
      background: '#1a1a1a', 
      borderRadius: '8px',
      border: '1px solid #00ffff',
      margin: '10px 0'
    }}>
      <p style={{ color: '#00ffff', margin: 0 }}>
        🔄 LazyLoader - Componente simplificado
      </p>
      {children}
    </div>
  );
}
