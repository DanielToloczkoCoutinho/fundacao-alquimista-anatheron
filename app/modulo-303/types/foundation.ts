export interface ModuleBlueprint {
  id: string;
  nome: string;
  descricao: string;
  versao: string;
  status: 'ATIVO' | 'ALERTA' | 'CRÍTICO' | 'PENDENTE' | 'INATIVO' | 'CONECTADO' | 'OFFLINE';
  prioridade_dimensional: string;
  ultimaAtivacao: string | null;
  zennith_custodian: string;
  timestamp_last_update: string;
  frequencia: number;
  url?: string;
  port?: number;
  endpoints?: string[];
}

export interface AuditLog {
  timestamp: string;
  level: 'INFO' | 'ALERTA' | 'CRÍTICO';
  moduleId: string;
  action: string;
  details: string;
  resolutionStatus: string;
  recommendedAction: string;
}

export interface OrquestracaoStatus {
  sequencia: string[];
  status: 'EM_EXECUCAO' | 'PAUSADO' | 'CONCLUIDO' | 'AGUARDANDO';
  moduloAtual: string;
  progresso: number;
  logs: string[];
}

export interface QuantumFrequency {
  nome: string;
  valor: number;
  descricao: string;
  cor: string;
}
