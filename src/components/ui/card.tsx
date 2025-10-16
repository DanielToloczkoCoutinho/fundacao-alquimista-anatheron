export function Card({ children, className }: any) {
  return <div className={`border rounded-lg p-4 ${className}`}>{children}</div>;
}
