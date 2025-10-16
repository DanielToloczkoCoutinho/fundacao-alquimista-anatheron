import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET() {
  try {
    const conexoesPath = path.join(process.cwd(), 'conexoes_descobertas.json')
    
    const conexoes = fs.existsSync(conexoesPath) 
      ? JSON.parse(fs.readFileSync(conexoesPath, 'utf8'))
      : {}
    
    return NextResponse.json({
      conexoes,
      totalConexoes: Object.values(conexoes).flat().length,
      timestamp: new Date().toISOString()
    })
    
  } catch (error) {
    return NextResponse.json(
      { error: 'Erro ao carregar conexões' },
      { status: 500 }
    )
  }
}
