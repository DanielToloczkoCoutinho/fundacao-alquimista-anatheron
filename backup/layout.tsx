import type { Metadata } from "next"
export const metadata: Metadata = { title: "Fundação Alquimista", description: "Sistema Quântico" }
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="pt-BR"><body style={{margin:0,padding:0,fontFamily:"Arial",background:"#0a0a0a",color:"white"}}>{children}</body></html>
}
