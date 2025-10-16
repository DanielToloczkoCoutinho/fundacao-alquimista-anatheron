export function useToast() {
  return {
    toast: (message: string) => console.log('Toast:', message)
  };
}
