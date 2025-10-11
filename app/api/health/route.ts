import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    status: "healthy",
    sistema: "Fundação Alquimista",
    timestamp: new Date().toISOString(),
    versao: "3.0.0",
    ambiente: process.env.NODE_ENV || "development"
  });
}
