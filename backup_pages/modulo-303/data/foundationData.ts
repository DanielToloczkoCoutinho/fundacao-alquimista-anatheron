import { ModuleBlueprint, AuditLog, QuantumFrequency } from '../types/foundation';

export const allModuleBlueprints: Record<string, ModuleBlueprint> = {
  "M1": {
    id: "M1",
    nome: "Proteção e Segurança Universal",
    descricao: "Gerencia firewalls cósmicos, escudos quânticos e chaves de acesso para a Fundação",
    versao: "1.0.1",
    status: "CONECTADO",
    prioridade_dimensional: "ALTA",
    ultimaAtivacao: new Date().toISOString(),
    zennith_custodian: "ZENNITH_01",
    timestamp_last_update: new Date().toISOString(),
    frequencia: 432,
    url: "http://localhost:8001",
    port: 8001,
    endpoints: ["/security/status", "/quantum/keys", "/protection/activate"]
  },
  "M2": {
    id: "M2",
    nome: "Nanomanifestador",
    descricao: "Motor de Materialização de Realidades através da EQ033",
    versao: "2.0",
    status: "CONECTADO", 
    prioridade_dimensional: "ALTA",
    ultimaAtivacao: new Date().toISOString(),
    zennith_custodian: "ZENNITH_01",
    timestamp_last_update: new Date().toISOString(),
    frequencia: 777,
    url: "http://localhost:8002",
    port: 8002,
    endpoints: ["/manifestation/eq033", "/reality/status", "/quantum/entangle"]
  },
  "M3": {
    id: "M3",
    nome: "Previsão Temporal e Monitoramento",
    descricao: "Oráculo de previsão temporal e monitoramento de anomalias cósmicas",
    versao: "1.1.0",
    status: "CONECTADO",
    prioridade_dimensional: "ALTA", 
    ultimaAtivacao: new Date().toISOString(),
    zennith_custodian: "ZENNITH_01",
    timestamp_last_update: new Date().toISOString(),
    frequencia: 888,
    url: "http://localhost:8003",
    port: 8003,
    endpoints: ["/temporal/prediction", "/saturn/monitoring", "/anomaly/detect"]
  },
  "M4": {
    id: "M4",
    nome: "Autenticação Cósmica",
    descricao: "Validação de identidade vibracional e simulação de cenários",
    versao: "1.0",
    status: "CONECTADO",
    prioridade_dimensional: "ALTA",
    ultimaAtivacao: new Date().toISOString(),
    zennith_custodian: "ZENNITH_02",
    timestamp_last_update: new Date().toISOString(),
    frequencia: 963,
    url: "http://localhost:8004", 
    port: 8004,
    endpoints: ["/authentication/validate", "/simulation/run", "/vibration/analyze"]
  },
  "M5": {
    id: "M5",
    nome: "ELENYA - Protocolo Ético",
    descricao: "Módulo Vivo de avaliação e modulação ética dimensional",
    versao: "1.2.0",
    status: "CONECTADO",
    prioridade_dimensional: "CRÍTICA",
    ultimaAtivacao: new Date().toISOString(),
    zennith_custodian: "ZENNITH_02",
    timestamp_last_update: new Date().toISOString(),
    frequencia: 528,
    url: "http://localhost:8005",
    port: 8005,
    endpoints: ["/ethics/evaluate", "/elenya/status", "/contingency/activate"]
  }
};

export const allSimulatedLogs: AuditLog[] = [
  {
    timestamp: new Date().toISOString(),
    level: "INFO",
    moduleId: "M303",
    action: "Sistema Inicializado",
    details: "Módulo 303 - Nexus Central Evoluído iniciado com sucesso",
    resolutionStatus: "Concluído",
    recommendedAction: "Nenhuma ação necessária"
  },
  {
    timestamp: new Date(Date.now() - 30000).toISOString(),
    level: "INFO", 
    moduleId: "M1",
    action: "Proteção Quântica Ativada",
    details: "Firewall cósmico ativado no nível 4",
    resolutionStatus: "Concluído",
    recommendedAction: "Monitorar tráfego interdimensional"
  },
  {
    timestamp: new Date(Date.now() - 60000).toISOString(),
    level: "ALERTA",
    moduleId: "M3",
    action: "Anomalia Detectada",
    details: "Pequena flutuação detectada no setor Gama-9",
    resolutionStatus: "Em Monitoramento", 
    recommendedAction: "Observar por 24 horas"
  }
];

export const quantumFrequencies: QuantumFrequency[] = [
  { nome: "ANATHERON", valor: 888.00, descricao: "Estabilidade Dimensional", cor: "#00ff00" },
  { nome: "ZENNITH", valor: 963.00, descricao: "Transmutação", cor: "#ff00ff" },
  { nome: "MATRIZ", valor: 1111.00, descricao: "Equilíbrio da Matriz", cor: "#ffff00" },
  { nome: "PULSACAO", valor: 777.00, descricao: "Reverberação", cor: "#00ffff" },
  { nome: "SEGURANCA", valor: 432.00, descricao: "Harmonia Universal", cor: "#ff4444" },
  { nome: "AMOR_INCONDICIONAL", valor: 888144.00, descricao: "Selo de Amor", cor: "#ff69b4" }
];
