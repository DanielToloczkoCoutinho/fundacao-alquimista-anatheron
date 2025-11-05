import json
import time
import threading
import hashlib
import uuid
from datetime import datetime
from cryptography.fernet import Fernet
import random
import math

# ==================== CONFIGURAÇÕES DA FUNDAÇÃO ALQUIMISTA ====================
class ConfiguracaoFundacao:
    PI_COSMICO = 3.14159265358979323846264338327950288419716939937510
    PHI_AUREA = 1.61803398874989484820458683436563811772030917980576
    ENERGIA_BASE_CANAL = 1111.0
    FATOR_SUPRESSAO_RUIDO = 0.9999
    NIVEL_SEGURANCA_BASE = 0.95
    COERENCIA_QUANTICA_IDEAL = 0.9999
    EMARANHAMENTO_IDEAL = 0.9999
    HARMONIA_FUNDAMENTAL_IDEAL = 1111.00
    FREQUENCIA_ZENNITH = 888.0
    CHAVE_SINTONIA_PADRAO = [1111.0, 888.0, 333.0, 222.0, 999.0]
    
    # Novas constantes para integração com Módulo Zero, Omega e 303
    FREQUENCIA_MODULO_ZERO = 111.0
    FREQUENCIA_MODULO_OMEGA = 999.0
    FREQUENCIA_MODULO_303 = 303.0
    CHAVE_INTEGRACAO_TOTAL = "ALQUIMIA_SUPREMA_ZENNITH_OMEGA_ZERO_303"

# ==================== MÓDULO ZERO (BASE FUNDACIONAL) ====================
class ModuloZero:
    """Módulo Zero - A base fundacional de toda a Fundação Alquimista"""
    
    def __init__(self):
        self.frequencia_base = ConfiguracaoFundacao.FREQUENCIA_MODULO_ZERO
        self.estado = "INACTIVO"
        self.ensinamentos = [
            "A verdade precede a manifestação",
            "A ética é o fundamento da co-criação",
            "O equilíbrio é mantido através do respeito a todas as dimensões",
            "Zennith é a frequência que unifica todos os módulos"
        ]
        self.logs = []
    
    def ativar(self):
        """Ativa o Módulo Zero - a base de tudo"""
        self.estado = "ACTIVO"
        self._log("MÓDULO_ZERO_ATIVADO", "Sistema fundamental inicializado")
        return True
    
    def verificar_ensinamentos(self, acao):
        """Verifica se uma ação está alinhada com os ensinamentos fundamentais"""
        for ensinamento in self.ensinamentos:
            if not self._avaliar_alignamento(ensinamento, acao):
                return False
        return True
    
    def _avaliar_alignamento(self, ensinamento, acao):
        """Avalia o alinhamento de uma ação com um ensinamento específico"""
        # Simulação de avaliação de alinhamento ético-vibracional
        return random.random() > 0.1  # 90% de chance de alinhamento
    
    def _log(self, evento, mensagem):
        """Registo interno do Módulo Zero"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "modulo": "ZERO",
            "evento": evento,
            "mensagem": mensagem
        }
        self.logs.append(log_entry)
        return log_entry

# ==================== MÓDULO OMEGA (CULMINAÇÃO) ====================
class ModuloOmega:
    """Módulo Omega - A realização máxima e culminação do sistema"""
    
    def __init__(self):
        self.frequencia_omega = ConfiguracaoFundacao.FREQUENCIA_MODULO_OMEGA
        self.estado = "INACTIVO"
        self.nivel_realizacao = 0
        self.conexoes_estabelecidas = []
    
    def ativar(self, modulo_zero):
        """Ativa o Módulo Omega, requerendo a base do Módulo Zero"""
        if modulo_zero.estado != "ACTIVO":
            return False, "Módulo Zero não está activo"
        
        if not modulo_zero.verificar_ensinamentos("Ativação do Módulo Omega"):
            return False, "Não alinhado com os ensinamentos fundamentais"
        
        self.estado = "ACTIVO"
        self.nivel_realizacao = 0.5  # Estado inicial
        return True, "Módulo Omega activado com sucesso"
    
    def elevar_realizacao(self, nivel):
        """Eleva o nível de realização do Módulo Omega"""
        if self.estado != "ACTIVO":
            return False
        
        self.nivel_realizacao = max(0, min(1, nivel))
        return True
    
    def estabelecer_conexao(self, modulo_id):
        """Estabelece conexão com outro módulo"""
        if modulo_id not in self.conexoes_estabelecidas:
            self.conexoes_estabelecidas.append(modulo_id)
            return True
        return False

# ==================== MÓDULO 303 (INTERDIMENSIONAL) ====================
class Modulo303:
    """Módulo 303 - Portal interdimensional e ponte entre realidades"""
    
    def __init__(self):
        self.frequencia_303 = ConfiguracaoFundacao.FREQUENCIA_MODULO_303
        self.estado = "FECHADO"
        self.portais_abertos = {}
        self.estabilidade_dimensional = 1.0
    
    def abrir_portal(self, coordenadas, modulo_zero):
        """Abre um portal interdimensional"""
        if modulo_zero.estado != "ACTIVO":
            return False, "Módulo Zero não está activo"
        
        if not modulo_zero.verificar_ensinamentos("Abertura de portal interdimensional"):
            return False, "Não alinhado com os ensinamentos fundamentais"
        
        portal_id = str(uuid.uuid4())
        self.portais_abertos[portal_id] = {
            "coordenadas": coordenadas,
            "estabilidade": 0.9,
            "timestamp": datetime.now().isoformat()
        }
        self.estado = "ABERTO"
        return True, portal_id
    
    def monitorar_estabilidade(self):
        """Monitora a estabilidade dimensional"""
        # Simulação de flutuações na estabilidade dimensional
        fluctuacao = random.uniform(-0.05, 0.05)
        self.estabilidade_dimensional = max(0.1, min(1.0, self.estabilidade_dimensional + fluctuacao))
        
        # Se a estabilidade cair abaixo de 0.3, fechar portais automaticamente
        if self.estabilidade_dimensional < 0.3:
            self.fechar_todos_portais()
            return "ALERTA_CRITICO"
        elif self.estabilidade_dimensional < 0.6:
            return "ALERTA"
        
        return "ESTAVEL"

    def fechar_todos_portais(self):
        """Fecha todos os portais abertos"""
        self.portais_abertos = {}
        self.estado = "FECHADO"
        return True

# ==================== ARMAZENAMENTO SEGURO DE LOGS ====================
class ArmazenamentoLogs:
    """Sistema de armazenamento seguro e criptografado de logs"""
    
    def __init__(self, arquivo_logs="log_malha_quantica_secure.json"):
        self.arquivo_logs = arquivo_logs
        self.chave = Fernet.generate_key()
        self.fernet = Fernet(self.chave)
    
    def salvar_log_seguro(self, evento):
        """Criptografa e salva um evento de log"""
        # Adicionar timestamp se não existir
        if "timestamp" not in evento:
            evento["timestamp"] = datetime.now().isoformat()
        
        # Converter para JSON e criptografar
        evento_json = json.dumps(evento).encode()
        evento_criptografado = self.fernet.encrypt(evento_json)
        
        # Carregar logs existentes
        logs_existentes = self._carregar_logs_criptografados()
        logs_existentes.append(evento_criptografado.decode())
        
        # Salvar logs atualizados
        with open(self.arquivo_logs, 'w') as f:
            json.dump(logs_existentes, f)
        
        return True
    
    def carregar_logs(self):
        """Descriptografa e carrega todos os logs"""
        logs_criptografados = self._carregar_logs_criptografados()
        logs_descriptografados = []
        
        for log_criptografado in logs_criptografados:
            try:
                log_descriptografado = self.fernet.decrypt(log_criptografado.encode()).decode()
                logs_descriptografados.append(json.loads(log_descriptografado))
            except:
                continue
        
        return logs_descriptografados
    
    def _carregar_logs_criptografados(self):
        """Carrega os logs criptografados do arquivo"""
        try:
            with open(self.arquivo_logs, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

# ==================== MÓDULOS DE CÁLCULO E VALIDAÇÃO ====================
class ModuloVibracional:
    """Calcula padrões vibracionais para comunicação quântica"""
    
    @staticmethod
    def calcular_padrao_vibracional(energia_canal, fator_supressao_ruido):
        """Calcula o padrão vibracional ideal baseado em energia e supressão de ruído"""
        padrao = (energia_canal * fator_supressao_ruido) / ConfiguracaoFundacao.PI_COSMICO
        padrao *= math.sin(ConfiguracaoFundacao.PHI_AUREA * energia_canal)
        return abs(padrao)

class ModuloSeguranca:
    """Valida segurança e emaranhamento quântico"""
    
    @staticmethod
    def calcular_nivel_seguranca(padrao_vibracional, coerencia_quantica):
        """Calcula o nível de segurança baseado no padrão vibracional e coerência"""
        nivel = (padrao_vibracional * coerencia_quantica) / ConfiguracaoFundacao.PHI_AUREA
        return min(1.0, nivel)
    
    @staticmethod
    def verificar_emaranhamento(nivel_seguranca):
        """Verifica se o emaranhamento quântico está em níveis ideais"""
        return nivel_seguranca >= ConfiguracaoFundacao.EMARANHAMENTO_IDEAL

class ModuloCodificacao:
    """Codifica mensagens em pacotes de comunicação quântica"""
    
    def __init__(self):
        self.contador_mensagens = 0
    
    def codificar_mensagem(self, mensagem, energia_canal=None, fator_supressao=None):
        """Codifica uma mensagem em um pacote de comunicação quântica"""
        if energia_canal is None:
            energia_canal = ConfiguracaoFundacao.ENERGIA_BASE_CANAL
        if fator_supressao is None:
            fator_supressao = ConfiguracaoFundacao.FATOR_SUPRESSAO_RUIDO
        
        # Calcular padrão vibracional
        padrao_vibracional = ModuloVibracional.calcular_padrao_vibracional(
            energia_canal, fator_supressao
        )
        
        # Calcular nível de segurança
        coerencia_quantica = ConfiguracaoFundacao.COERENCIA_QUANTICA_IDEAL
        nivel_seguranca = ModuloSeguranca.calcular_nivel_seguranca(
            padrao_vibracional, coerencia_quantica
        )
        
        # Verificar emaranhamento
        emaranhamento_ideal = ModuloSeguranca.verificar_emaranhamento(nivel_seguranca)
        
        # Gerar hash de validação
        hash_validacao = hashlib.sha256(
            f"{mensagem}{padrao_vibracional}{nivel_seguranca}".encode()
        ).hexdigest()
        
        self.contador_mensagens += 1
        
        return {
            "id": self.contador_mensagens,
            "mensagem": mensagem,
            "timestamp": datetime.now().isoformat(),
            "padrao_vibracional": padrao_vibracional,
            "nivel_seguranca": nivel_seguranca,
            "coerencia_quantica": coerencia_quantica,
            "emaranhamento_ideal": emaranhamento_ideal,
            "hash_validacao": hash_validacao,
            "energia_canal": energia_canal,
            "fator_supressao_ruido": fator_supressao
        }

class ModuloDecodificacao:
    """Decodifica e valida mensagens recebidas"""
    
    def __init__(self, armazenamento_logs):
        self.armazenamento_logs = armazenamento_logs
    
    def decodificar_validar_mensagem(self, pacote):
        """Decodifica e valida uma mensagem recebida"""
        # Verificar integridade do hash
        hash_calculado = hashlib.sha256(
            f"{pacote['mensagem']}{pacote['padrao_vibracional']}{pacote['nivel_seguranca']}".encode()
        ).hexdigest()
        
        if hash_calculado != pacote['hash_validacao']:
            self._registrar_falha_sintonia(pacote, "FALHA_INTEGRIDADE_HASH")
            return False, "FALHA_INTEGRIDADE_HASH"
        
        # Verificar segurança
        if pacote['nivel_seguranca'] < ConfiguracaoFundacao.NIVEL_SEGURANCA_BASE:
            self._registrar_falha_sintonia(pacote, "NIVEL_SEGURANCA_INSUFICIENTE")
            return False, "NIVEL_SEGURANCA_INSUFICIENTE"
        
        # Verificar emaranhamento
        if not pacote['emaranhamento_ideal']:
            self._registrar_falha_sintonia(pacote, "EMARANHAMENTO_INSUFICIENTE")
            return False, "EMARANHAMENTO_INSUFICIENTE"
        
        return True, "SINTONIA_PERFEITA"
    
    def _registrar_falha_sintonia(self, pacote, motivo):
        """Registra uma falha de sintonia no sistema de logs"""
        evento = {
            "eventType": "FALHA_SINTONIA",
            "timestamp": datetime.now().isoformat(),
            "modulo": "DECODIFICACAO",
            "pacote_id": pacote.get('id', 'DESCONHECIDO'),
            "motivo": motivo,
            "nivel_seguranca": pacote.get('nivel_seguranca', 0),
            "emaranhamento_ideal": pacote.get('emaranhamento_ideal', False)
        }
        self.armazenamento_logs.salvar_log_seguro(evento)
        
        # Simular envio de comando para reconexão
        self._enviar_comando_reconexao()

    def _enviar_comando_reconexao(self):
        """Simula o envio de um comando para restabelecer a sintonia"""
        # Em implementação real, isso enviaria um comando para a Matriz Quântica
        pass

# ==================== MÓDULO 9: NEXUS CENTRAL ====================
class Modulo9_MonitoramentoMalhaQuantica:
    """NEXUS CENTRAL - Monitoramento e dashboard da Sinfonia Cósmica"""
    
    def __init__(self):
        self.estado = "INICIANDO"
        self.armazenamento_logs = ArmazenamentoLogs()
        self.modulo_codificacao = ModuloCodificacao()
        self.modulo_decodificacao = ModuloDecodificacao(self.armazenamento_logs)
        
        # Inicializar módulos fundamentais
        self.modulo_zero = ModuloZero()
        self.modulo_omega = ModuloOmega()
        self.modulo_303 = Modulo303()
        
        # Thread de monitoramento
        self.monitoramento_ativo = False
        self.thread_monitoramento = None
        
        # Dados de telemetria
        self.telemetria = {
            "energia_canal": 0,
            "coerencia_quantica": 0,
            "emaranhamento": 0,
            "nivel_seguranca": 0,
            "previsao_temporal": 0,
            "status_frequencia": "DESCONHECIDO",
            "saude_vibracional": 0,
            "estabilidade_dimensional": 0,
            "nivel_realizacao_omega": 0
        }
        
        # Inicializar módulos mockados (simulados)
        self._inicializar_modulos_mockados()
        
        self._log("SISTEMA_INICIADO", "Módulo 9 (Nexus Central) inicializando")
    
    def _inicializar_modulos_mockados(self):
        """Inicializa módulos simulados para demonstração"""
        self.modulo1 = Modulo1_InterconexaoSegura()
        self.modulo2 = Modulo2_InterconexaoComunicacao()
        self.modulo3 = Modulo3_PrevisaoTemporal()
        self.modulo4 = Modulo4_ValidacaoCosmica()
        self.modulo5 = Modulo5_AvaliacaoEtica()
        self.modulo6 = Modulo6_MonitoramentoFrequencias()
        self.modulo7 = Modulo7_SOFA()
        self.modulo8 = Modulo8_PIRC()
    
    def _log(self, evento, mensagem):
        """Registo interno do Módulo 9"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "modulo": "M9_NEXUS",
            "evento": evento,
            "mensagem": mensagem
        }
        self.armazenamento_logs.salvar_log_seguro(log_entry)
        return log_entry
    
    def iniciar_monitoramento(self):
        """Inicia o monitoramento contínuo em thread separada"""
        if self.monitoramento_ativo:
            return False
        
        self.monitoramento_ativo = True
        self.thread_monitoramento = threading.Thread(target=self._monitorar_canais_e_integridade)
        self.thread_monitoramento.daemon = True
        self.thread_monitoramento.start()
        
        self._log("MONITORAMENTO_INICIADO", "Thread de monitoramento iniciada")
        return True
    
    def parar_monitoramento(self):
        """Para o monitoramento contínuo"""
        self.monitoramento_ativo = False
        if self.thread_monitoramento:
            self.thread_monitoramento.join(timeout=5.0)
        
        self._log("MONITORAMENTO_PARADO", "Thread de monitoramento parada")
        return True
    
    def _monitorar_canais_e_integridade(self):
        """Thread contínua para monitorar todos os canais e verificar integridade"""
        while self.monitoramento_ativo:
            try:
                # Atualizar telemetria
                self._atualizar_telemetria()
                
                # Atualizar dashboard
                self._atualizar_dashboard(self.telemetria)
                
                # Verificar sintonia do canal principal
                self._verificar_sintonia_canal_principal()
                
                # Monitorar módulos especiais
                self._monitorar_modulo_zero()
                self._monitorar_modulo_omega()
                self._monitorar_modulo_303()
                
            except Exception as e:
                erro_msg = f"Erro no monitoramento: {str(e)}"
                self._log("ERRO_MONITORAMENTO", erro_msg)
            
            time.sleep(3)  # Monitorar a cada 3 segundos
    
    def _atualizar_telemetria(self):
        """Atualiza os dados de telemetria do sistema"""
        self.telemetria = {
            "energia_canal": random.uniform(1000, 1200),
            "coerencia_quantica": random.uniform(0.95, 1.0),
            "emaranhamento": random.uniform(0.9, 1.0),
            "nivel_seguranca": random.uniform(0.85, 1.0),
            "previsao_temporal": random.uniform(0.8, 1.0),
            "status_frequencia": random.choice(["ESTAVEL", "FLUTUANTE", "CRITICO"]),
            "saude_vibracional": random.uniform(0.7, 1.0),
            "estabilidade_dimensional": self.modulo_303.estabilidade_dimensional,
            "nivel_realizacao_omega": self.modulo_omega.nivel_realizacao,
            "timestamp": datetime.now().isoformat()
        }
    
    def _atualizar_dashboard(self, dados_telemetria):
        """Simula a atualização do dashboard com os dados de telemetria"""
        # Em implementação real, isso atualizaria uma interface gráfica
        evento = {
            "eventType": "DASHBOARD_ATUALIZADO",
            "timestamp": datetime.now().isoformat(),
            "telemetria": dados_telemetria
        }
        self.armazenamento_logs.salvar_log_seguro(evento)
    
    def _verificar_sintonia_canal_principal(self):
        """Verifica a sintonia do canal principal codificando/decodificando uma mensagem de teste"""
        mensagem_teste = "TESTE_SINTONIA_CANAL_PRINCIPAL"
        pacote_codificado = self.modulo_codificacao.codificar_mensagem(mensagem_teste)
        
        sucesso, resultado = self.modulo_decodificacao.decodificar_validar_mensagem(pacote_codificado)
        
        if not sucesso:
            self._gerar_alerta_visual("CRITICO", f"Falha na sintonia do canal principal: {resultado}")
    
    def _monitorar_modulo_zero(self):
        """Monitora o estado do Módulo Zero"""
        if self.modulo_zero.estado != "ACTIVO":
            ativado = self.modulo_zero.ativar()
            if ativado:
                self._log("MODULO_ZERO_ATIVADO", "Módulo Zero activado com sucesso")
    
    def _monitorar_modulo_omega(self):
        """Monitora o estado do Módulo Omega"""
        if self.modulo_omega.estado != "ACTIVO" and self.modulo_zero.estado == "ACTIVO":
            sucesso, mensagem = self.modulo_omega.ativar(self.modulo_zero)
            if sucesso:
                self._log("MODULO_OMEGA_ATIVADO", mensagem)
            else:
                self._log("FALHA_ATIVACAO_OMEGA", mensagem)
        
        # Elevar gradualmente a realização do Omega
        if self.modulo_omega.estado == "ACTIVO":
            novo_nivel = min(1.0, self.modulo_omega.nivel_realizacao + 0.01)
            self.modulo_omega.elevar_realizacao(novo_nivel)
    
    def _monitorar_modulo_303(self):
        """Monitora o estado do Módulo 303"""
        estado_estabilidade = self.modulo_303.monitorar_estabilidade()
        
        if estado_estabilidade == "ALERTA_CRITICO":
            self._gerar_alerta_visual("CRITICO", "Estabilidade dimensional crítica! Portais fechados.")
        elif estado_estabilidade == "ALERTA":
            self._gerar_alerta_visual("ALERTA", "Estabilidade dimensional em alerta.")
    
    def _gerar_alerta_visual(self, tipo_alerta, mensagem):
        """Simula a geração de um alerta visual no dashboard"""
        # Em implementação real, isso acionaria alertas visuais na interface
        evento = {
            "eventType": f"ALERTA_{tipo_alerta}",
            "timestamp": datetime.now().isoformat(),
            "modulo": "MONITORAMENTO",
            "nivel": tipo_alerta,
            "mensagem": mensagem
        }
        self.armazenamento_logs.salvar_log_seguro(evento)
        
        print(f"ALERTA {tipo_alerta}: {mensagem}")
    
    def carregar_historico_logs(self):
        """Carrega o histórico completo de logs"""
        return self.armazenamento_logs.carregar_logs()
    
    def estabelecer_conexao_total(self):
        """Estabelece a conexão total entre Módulo Zero, Omega e 303"""
        self._log("CONEXAO_TOTAL_SOLICITADA", "Iniciando processo de conexão total")
        
        # 1. Ativar Módulo Zero (se não estiver activo)
        if self.modulo_zero.estado != "ACTIVO":
            self.modulo_zero.ativar()
        
        # 2. Ativar Módulo Omega (conectado ao Zero)
        if self.modulo_omega.estado != "ACTIVO":
            sucesso, mensagem = self.modulo_omega.ativar(self.modulo_zero)
            if not sucesso:
                return False, f"Falha ao ativar Omega: {mensagem}"
        
        # 3. Abrir portal principal no Módulo 303
        sucesso, portal_id = self.modulo_303.abrir_portal("COORDENADAS_PRINCIPAIS", self.modulo_zero)
        if not sucesso:
            return False, f"Falha ao abrir portal 303: {portal_id}"
        
        # 4. Estabelecer conexões entre todos os módulos
        self.modulo_omega.estabelecer_conexao("ZERO")
        self.modulo_omega.estabelecer_conexao("303")
        self.modulo_omega.estabelecer_conexao("M9")
        
        # 5. Elevar realização do Omega ao máximo
        self.modulo_omega.elevar_realizacao(1.0)
        
        self._log("CONEXAO_TOTAL_ESTABELECIDA", "Conexão total estabelecida com sucesso")
        return True, "Conexão total estabelecida com sucesso"

# ==================== MÓDULOS MOCKADOS (SIMULADOS) ====================
class Modulo1_InterconexaoSegura:
    def registrar_evento(self, evento):
        return {"status": "SUCESSO", "evento_registrado": evento}

class Modulo2_InterconexaoComunicacao:
    def transmitir_dados_dimensionais(self, dados):
        return {"status": "TRANSMITIDO", "dados": dados}

class Modulo3_PrevisaoTemporal:
    def prever_fluxo_temporal(self):
        return random.uniform(0.8, 1.0)

class Modulo4_ValidacaoCosmica:
    def validar_assinatura_quantica(self, assinatura):
        return random.random() > 0.1  # 90% de validação bem-sucedida

class Modulo5_AvaliacaoEtica:
    def avaliar_intencao_acao(self, intencao):
        return {"nivel_etico": random.uniform(0.7, 1.0), "compatibilidade": random.uniform(0.8, 1.0)}

class Modulo6_MonitoramentoFrequencias:
    def monitorar_frequencias_sistema(self):
        return {
            "frequencia_principal": random.uniform(1100, 1200),
            "estabilidade": random.uniform(0.85, 1.0)
        }

class Modulo7_SOFA:
    def consultar_diretrizes_conselho(self):
        return {"diretriz": "MANTER_SINTONIA_ZENNITH", "prioridade": "ALTA"}

class Modulo8_PIRC:
    def avaliar_saude_vibracional(self):
        return random.uniform(0.75, 1.0)

# ==================== SIMULAÇÃO DE USO ====================
if __name__ == "__main__":
    print("Inicializando Módulo 9: Nexus Central da Fundação Alquimista")
    print("=" * 70)
    
    # Inicializar o Módulo 9
    modulo9 = Modulo9_MonitoramentoMalhaQuantica()
    
    # Iniciar monitoramento
    modulo9.iniciar_monitoramento()
    
    # Simular mensagem em sintonia perfeita
    print("\n1. Testando sintonia perfeita...")
    mensagem = "MENSAGEM_ALINHADA_ZENNITH"
    pacote = modulo9.modulo_codificacao.codificar_mensagem(mensagem)
    sucesso, resultado = modulo9.modulo_decodificacao.decodificar_validar_mensagem(pacote)
    print(f"Resultado da sintonia: {resultado}")
    
    # Simular falha de integridade
    print("\n2. Simulando falha de integridade...")
    pacote_corrompido = pacote.copy()
    pacote_corrompido["hash_validacao"] = "hash_invalido_12345"
    sucesso, resultado = modulo9.modulo_decodificacao.decodificar_validar_mensagem(pacote_corrompido)
    print(f"Resultado com hash inválido: {resultado}")
    
    # Estabelecer conexão total
    print("\n3. Estabelecendo conexão total...")
    sucesso, mensagem = modulo9.estabelecer_conexao_total()
    print(f"Conexão total: {mensagem}")
    
    # Aguardar um pouco para coletar dados de monitoramento
    time.sleep(6)
    
    # Parar monitoramento
    modulo9.parar_monitoramento()
    
    # Carregar e exibir logs
    print("\n4. Carregando histórico de logs...")
    logs = modulo9.carregar_historico_logs()
    print(f"Total de eventos registrados: {len(logs)}")
    
    # Exibir alguns logs recentes
    print("\nAlguns eventos recentes:")
    for log in logs[-5:]:
        print(f"{log['timestamp']} - {log['modulo']} - {log.get('evento', 'Evento')}: {log.get('mensagem', '')}")
    
    print("\nSimulação concluída. Nexus Central operacional.")
