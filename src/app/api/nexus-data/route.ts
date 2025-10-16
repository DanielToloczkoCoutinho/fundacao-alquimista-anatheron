import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET() {
  try {
    const nexusPath = path.join(process.cwd(), 'nexus_mapeamento_refinado.json')
    
    if (!fs.existsSync(nexusPath)) {
      return NextResponse.json({
        nexusMestres: {},
        message: 'Dados dos nexus não encontrados'
      })
    }
    
    const nexusData = JSON.parse(fs.readFileSync(nexusPath, 'utf8'))
    
    return NextResponse.json({
      nexusMestres: nexusData,
      timestamp: new Date().toISOString()
    })
    
  } catch (error) {
    return NextResponse.json(
      { error: 'Erro ao carregar dados dos nexus' },
      { status: 500 }
    )
  }
}
