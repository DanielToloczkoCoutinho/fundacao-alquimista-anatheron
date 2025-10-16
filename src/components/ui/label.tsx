export function Label({ children, className }: any) {
  return <label className={`block text-sm font-medium ${className}`}>{children}</label>;
}
