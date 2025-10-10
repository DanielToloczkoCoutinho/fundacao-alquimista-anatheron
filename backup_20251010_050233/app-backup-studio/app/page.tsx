'use client';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-8">
      <h1 className="text-6xl font-bold mb-8">🌟 Fundação Alquimista Ativada!</h1>
      <p className="text-2xl mb-8">Sistema de Realidade Virtual Quântica</p>
      <div className="space-x-4">
        <button 
          onClick={() => router.push('/laboratorios')} 
          className="bg-indigo-600 px-6 py-3 rounded-lg hover:bg-indigo-700"
        >
          Laboratórios
        </button>
        <button 
          onClick={() => router.push('/vr')} 
          className="bg-green-600 px-6 py-3 rounded-lg hover:bg-green-700"
        >
          Módulo Zero VR
        </button>
      </div>
    </div>
  );
}
