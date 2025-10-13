import { NextResponse } from 'next/server';

export async function GET() {
  // AUTENTICAÇÃO SIMPLES - SEM CHAVES COMPLEXAS
  return NextResponse.json({ 
    authenticated: true,
    user: 'Fundador',
    system: 'Fundação Alquimista',
    message: 'Acesso concedido ao sistema interno'
  });
}

export async function POST() {
  return NextResponse.json({ 
    success: true,
    message: 'Sistema operacional' 
  });
}
