'use client';
'use client';
"use client";
'use client';
'use client';
'use client';
'use client';


import { Metadata } from 'next';
import { useState, useEffect } from 'react';


async function fetchData() {
  try {
    const res = await fetch('https://fundacao-alquimista-pdvlacpuf.vercel.app/api/fundacao-completa', {
      headers: {
        Authorization: 'Bearer fundacao-alquimista-quantum-secret-2025-966hz-luxnet',
      },
      cache: 'no-store',
    });
    if (!res.ok) throw new Error('Falha ao carregar dados');
    return await res.json();
  } catch (error) {
    console.error('Erro ao buscar dados:', error);
    return { documentos: [] };
  }
}

export default function Docs() {
  const [data, setData] = useState({ documentos: [] });

  useEffect(() => {
    fetchData().then((result) => {
      setData(result);
    });
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-4xl font-bold mb-4">Documentos - Matriz LUX.NET</h1>
      <ul className="list-disc pl-6">
        {data.documentos.slice(0, 100).map((file: string, index: number) => (
          <li key={index}>{file}</li>
        ))}
      </ul>
    </div>
  );
}
