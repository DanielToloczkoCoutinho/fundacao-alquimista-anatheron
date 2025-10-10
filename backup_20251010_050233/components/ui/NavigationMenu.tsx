export default function NavigationMenu() {
  return (
    <nav className="flex space-x-4 p-4 bg-gray-800 rounded-lg">
      <a href="/" className="text-white hover:text-yellow-400">Home</a>
      <a href="/laboratorios" className="text-white hover:text-yellow-400">Laboratórios</a>
      <a href="/dashboard" className="text-white hover:text-yellow-400">Dashboard</a>
    </nav>
  );
}
