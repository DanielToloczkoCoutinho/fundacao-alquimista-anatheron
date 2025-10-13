import { NextResponse } from 'next/server'

export async function GET() {
  return NextResponse.json({ status: 'active', message: 'Auth em desenvolvimento' })
}

export async function POST() {
  return NextResponse.json({ status: 'active', message: 'Login em desenvolvimento' })
}
