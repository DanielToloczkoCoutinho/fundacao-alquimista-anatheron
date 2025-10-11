'use client';
import { Suspense, lazy } from 'react';

// Componentes que podem ser carregados lentamente
export const LazyThreeJS = lazy(() => import('./quantum/ThreeJSWrapper'));
export const LazyQuantum = lazy(() => import('./quantum/QuantumVisualizer'));
export const LazyVR = lazy(() => import('./quantum/VRViewer'));

export function LazyLoader({ children, fallback = null }) {
  return (
    <Suspense fallback={fallback || <div className="text-center p-8">🌀 Carregando...</div>}>
      {children}
    </Suspense>
  );
}

export function LoadingFallback() {
  return (
    <div className="flex items-center justify-center min-h-64">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-yellow-500"></div>
      <span className="ml-3 text-yellow-300">Carregando módulo...</span>
    </div>
  );
}
