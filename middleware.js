import { NextResponse } from 'next/server'

export function middleware(request) {
  // Forçar todas as rotas a serem dinâmicas
  const response = NextResponse.next()
  
  // Headers para evitar cache
  response.headers.set('x-middleware-cache', 'no-cache')
  response.headers.set('Cache-Control', 'no-store, must-revalidate')
  
  return response
}

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
}
