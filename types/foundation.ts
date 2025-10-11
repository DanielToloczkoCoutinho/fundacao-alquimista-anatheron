export interface ModuleBlueprint {
  id: string;
  nome: string;
  status: string;
  frequencia: string;
}

export interface OrquestracaoStatus {
  modulosAtivos: number;
  coerencia: string;
  dimensoes: number;
}

export interface AuditLog {
  timestamp: string;
  acao: string;
  modulo: string;
}

export interface QuantumFrequency {
  valor: string;
  unidade: string;
  estabilidade: string;
}

export interface AuthUser {
  id: string;
  name: string;
  role: 'admin' | 'founder' | 'operator';
  email: string;
}
