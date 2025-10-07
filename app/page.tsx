export default function Home() {
  return (
    <main>
      <h1 style={{ color: '#00ff88' }}>🏛️ Fundação Alquimista</h1>
      <p>Sistema Online 🚀</p>
      <nav>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li><a href="/dashboard" style={{ color: '#00ff88' }}>📊 Dashboard</a></li>
          <li><a href="/admin" style={{ color: '#00ff88' }}>🛡️ Admin</a></li>
          <li><a href="/public" style={{ color: '#00ff88' }}>🌍 Public</a></li>
          <li><a href="/auth/signin" style={{ color: '#00ff88' }}>🔐 Login</a></li>
        </ul>
      </nav>
    </main>
  )
}
