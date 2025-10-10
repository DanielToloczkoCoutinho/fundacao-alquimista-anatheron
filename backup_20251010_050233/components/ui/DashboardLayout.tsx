export default function DashboardLayout({ children }) {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="container mx-auto p-4">
        {children}
      </div>
    </div>
  );
}
