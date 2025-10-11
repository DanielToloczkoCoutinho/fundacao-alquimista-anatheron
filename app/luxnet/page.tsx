'use client';
import { useEffect, useState } from 'react';
export const dynamic = "force-dynamic";
export default function LuxNet() {
  // Lógica dinâmica
  const [loadTime, setLoadTime] = useState('');
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
    setLoadTime(new Date().toLocaleString());
  }, []);
  return (
    <div className="min-h-screen bg-black text-white p-8">
      <h1 className="text-4xl font-bold text-center mb-8">🌟 LUX.NET COSMICA</h1>
      <p className="text-center text-xl">Sistema de Consciência Quântica Artificial</p>
    </div>
  );
}
