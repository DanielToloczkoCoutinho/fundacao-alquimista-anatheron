import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';
export async function GET() {
  const baseDir = path.join(process.cwd(), 'public/fundacao-completa');
  try {
    const docs = await fs.readdir(path.join(baseDir, 'docs'), { recursive: true });
    const scripts = await fs.readdir(path.join(baseDir, 'scripts-alquimicos'), { recursive: true });
    const modulos = await fs.readdir(path.join(baseDir, 'modulos'), { recursive: true });
    return NextResponse.json({
      documentos: docs.filter(f => f.endsWith('.md')).slice(0, 1000),
      scripts: scripts.filter(f => f.endsWith('.sh') || f.endsWith('.py')).slice(0, 1000),
      modulos: modulos.slice(0, 1000)
    });
  } catch (error) {
    return NextResponse.json({ error: 'Falha ao carregar dados', details: error.message }, { status: 500 });
  }
}
