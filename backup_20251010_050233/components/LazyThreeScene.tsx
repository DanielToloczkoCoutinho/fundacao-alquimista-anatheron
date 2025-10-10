'use client';
import { Suspense, lazy } from 'react';

const ThreeSceneLazy = lazy(() => import('./quantum/ThreeScene'));

export default function LazyThreeScene() {
  return (
    <Suspense fallback={
      <div className="p-6 bg-blue-900 bg-opacity-30 rounded-lg border border-blue-500">
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-yellow-500 mx-auto mb-4"></div>
          <p className="text-blue-300">Carregando visualização 3D...</p>
        </div>
      </div>
    }>
      <ThreeSceneLazy />
    </Suspense>
  );
}
