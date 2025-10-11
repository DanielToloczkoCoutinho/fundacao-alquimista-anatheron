import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    sistemas: {
      fundacao: { status: "✅ OPERACIONAL", modulos: 260 },
      zennith: { status: "✅ CONECTADO", dimensoes: 12 },
      studio: { status: "✅ ATIVO", interfaces: 330 },
      laboratorios: { status: "✅ FUNCIONANDO", count: 6 }
    },
    timestamp: new Date().toISOString()
  });
}
