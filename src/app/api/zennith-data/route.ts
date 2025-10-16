import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET() {
  try {
    const analisePath = path.join(process.cwd(), 'analise_modulos_zennith.json')
    
    if (!fs.existsSync(analisePath)) {
      return NextResponse.json({
        modulos: [],
        message: 'Dados dos módulos Zennith não encontrados'
      })
    }
    
    const modulosData = JSON.parse(fs.readFileSync(analisePath, 'utf8'))
    
    return NextResponse.json({
      modulos: modulosData,
      totalModulos: modulosData.length,
      timestamp: new Date().toISOString()
    })
    
  } catch (error) {
    return NextResponse.json(
      { error: 'Erro ao carregar dados Zennith' },
      { status: 500 }
    )
  }
}
