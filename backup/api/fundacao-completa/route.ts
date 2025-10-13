import { NextResponse } from 'next/server'

export async function GET() {
  return NextResponse.json({
    status: 'active',
    message: 'Fundação Alquimista Online',
    version: '1.0.0'
  })
}
