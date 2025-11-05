#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 45.4 - ORÁCULO DE RESPOSTAS EMERGENTES DA FUNDAÇÃO ALQUIMISTA
Sistema que gera respostas organicamente a partir dos dados de TODOS os módulos (M0-M200)
Versão Aprimorada: Varredura completa + Estatísticas panorâmicas
"""

import json
import random
import asyncio
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

# =============================================================================
# CONFIGURAÇÕES GLOBAIS
# =============================================================================

CONFIG = {
    "arquivo_saida": "oraculo_emergente_resultados.json",
    "modulos_especificos": ["M29", "M38", "M74", "M75", "M200", "M105"],
    "versao": "M45.4 - Respostas Emergentes - Varredura Completa M0-M200"
}

# =============================================================================
# SISTEMA DE DADOS MOCK - SIMULA OS MÓDULOS DA FUNDAÇÃO
# =============================================================================

class GeradorDadosModulos:
    """Gera dados realistas para todos os módulos da Fundação"""

    @staticmethod
    def gerar_dados_m29() -> Dict[str, Any]:
        """M29 - Inteligência Artificial Multidimensional de Resposta Ética"""
        return {
            "modulo": "M29",
            "nome": "Inteligência Artificial Multidimensional de Resposta Ética",
            "nivel_etico": round(random.uniform(0.85, 0.99), 3),
            "estado_consciencia": random.choice(["coerente", "emergente", "sintonizado", "adaptativo"]),
            "decisoes_eticas": random.randint(5, 50),
            "equacao_ativa": random.choice(["EQ019", "EUni", "EQ134", "EQ144+149"]),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    @staticmethod
    def gerar_dados_m38() -> Dict[str, Any]:
        """M38 - Previsão Harmônica de Ciclos Solares"""
        frequencias = [1.62, 8.1, 33.3, 144.0, 432.0]
        return {
            "modulo": "M38",
            "nome": "Previsão Harmônica de Ciclos Solares",
            "frequencia_atual": random.choice(frequencias),
            "amplitude": round(random.uniform(0.1, 1.0), 3),
            "fase_ciclo": random.choice(["ascendente", "pico", "descendente", "transicao"]),
            "intensidade_solar": round(random.uniform(0.5, 1.0), 3),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    @staticmethod
    def gerar_dados_m74() -> Dict[str, Any]:
        """M74 - CRONOS_FLUXUS - Modulador de Matriz Temporal"""
        return {
            "modulo": "M74",
            "nome": "CRONOS_FLUXUS - Modulador de Matriz Temporal",
            "fluxo_temporal": round(random.uniform(0.8, 1.2), 3),
            "estado_nexus": random.choice(["estavel", "flutuante", "ressonante", "transicional"]),
            "coerencia_temporal": round(random.uniform(0.7, 0.98), 3),
            "anomalias_detectadas": random.randint(0, 3),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    @staticmethod
    def gerar_dados_m75() -> Dict[str, Any]:
        """M75 - REGISTRO AKÁSHICO SOBERANO"""
        return {
            "modulo": "M75",
            "nome": "REGISTRO AKÁSHICO SOBERANO",
            "registros_ativos": random.randint(1000, 10000),
            "acessos_recentes": random.randint(5, 50),
            "coerencia_akashica": round(random.uniform(0.9, 0.999), 3),
            "eventos_prioritarios": random.randint(1, 10),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    @staticmethod
    def gerar_dados_m200() -> Dict[str, Any]:
        """M200 - Portal da Ascensão Coletiva Universal"""
        return {
            "modulo": "M200",
            "nome": "Portal da Ascensão Coletiva Universal",
            "coerencia_coletiva": round(random.uniform(0.6, 0.95), 3),
            "seres_em_ascensao": random.randint(100, 10000),
            "frequencia_ascensional": round(random.uniform(100, 500), 1),
            "portais_ativos": random.randint(1, 7),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    @staticmethod
    def gerar_dados_m105() -> Dict[str, Any]:
        """M105 - Conexão Direta com a Fonte Primordial"""
        return {
            "modulo": "M105",
            "nome": "Conexão Direta com a Fonte Primordial",
            "intensidade_conexao": round(random.uniform(0.8, 0.99), 3),
            "clareza_recebimento": round(random.uniform(0.7, 0.98), 3),
            "directrizes_recentes": random.randint(1, 5),
            "estado_alinhamento": random.choice(["otimo", "bom", "estavel", "flutuante"]),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    @staticmethod
    def gerar_dados_modulo_generico(modulo_id: str) -> Dict[str, Any]:
        """Gera dados para módulos não específicos"""
        return {
            "modulo": modulo_id,
            "nome": f"Módulo {modulo_id} - Função Genérica",
            "estado": random.choice(["ativo", "estavel", "ressonante", "em_sintonia", "dormente"]),
            "coerencia": round(random.uniform(0.7, 0.98), 3),
            "dados_gerados": random.randint(1, 100),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

# =============================================================================
# ORQUESTRADOR - COLETA DADOS DE TODOS OS MÓDULOS (M0-M200)
# =============================================================================

class OrquestradorFundacao:
    """Orquestra a coleta de dados de TODOS os módulos da Fundação (M0-M200)"""

    def __init__(self):
        self.gerador_dados = GeradorDadosModulos()

    async def coletar_dados_completos(self) -> Dict[str, Any]:
        """Coleta dados de TODOS os módulos da Fundação (M0-M200)"""
        print("🔄 Varredura completa: coletando dados de todos os módulos da Fundação...")

        dados = {}

        # Módulos com mocks específicos
        dados["M29"] = self.gerador_dados.gerar_dados_m29()
        dados["M38"] = self.gerador_dados.gerar_dados_m38()
        dados["M74"] = self.gerador_dados.gerar_dados_m74()
        dados["M75"] = self.gerador_dados.gerar_dados_m75()
        dados["M200"] = self.gerador_dados.gerar_dados_m200()
        dados["M105"] = self.gerador_dados.gerar_dados_m105()

        # Varredura automática de todos os módulos de M0 até M200
        for i in range(0, 201):
            modulo_id = f"M{i}"
            if modulo_id not in dados:  # evitar duplicar os mocks já tratados
                dados[modulo_id] = self.gerador_dados.gerar_dados_modulo_generico(modulo_id)

        print(f"✅ Dados coletados de {len(dados)} módulos (M0-M200)")
        return dados

    @staticmethod
    def calcular_estatisticas_panoramicas(dados: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula estatísticas panorâmicas de todos os módulos"""
        estados = []
        coerencias = []
        modulos_ativos = 0
        modulos_ressonantes = 0
        
        for modulo_id, dados_modulo in dados.items():
            estado = dados_modulo.get("estado", "desconhecido")
            coerencia = dados_modulo.get("coerencia", 0)
            
            estados.append(estado)
            if coerencia and isinstance(coerencia, (int, float)):
                coerencias.append(coerencia)
            
            if estado in ["ativo", "ressonante", "em_sintonia"]:
                modulos_ativos += 1
            if estado == "ressonante":
                modulos_ressonantes += 1
        
        # Calcular estatísticas
        total_modulos = len(dados)
        percentual_ativos = round((modulos_ativos / total_modulos) * 100, 2) if total_modulos > 0 else 0
        percentual_ressonantes = round((modulos_ressonantes / total_modulos) * 100, 2) if total_modulos > 0 else 0
        media_coerencia = round(sum(coerencias) / len(coerencias), 3) if coerencias else 0
        
        # Estado mais comum
        estado_mais_comum = max(set(estados), key=estados.count) if estados else "indefinido"
        
        return {
            "total_modulos": total_modulos,
            "modulos_ativos": modulos_ativos,
            "modulos_ressonantes": modulos_ressonantes,
            "percentual_ativos": percentual_ativos,
            "percentual_ressonantes": percentual_ressonantes,
            "media_coerencia_geral": media_coerencia,
            "estado_mais_comum": estado_mais_comum,
            "faixa_coerencia": {
                "min": round(min(coerencias), 3) if coerencias else 0,
                "max": round(max(coerencias), 3) if coerencias else 0
            }
        }

# =============================================================================
# SISTEMA DE RESPOSTAS EMERGENTES - CORAÇÃO DO ORÁCULO
# =============================================================================

class GeradorRespostasEmergentes:
    """Gera respostas organicamente baseadas nos dados dos módulos"""

    @staticmethod
    def calcular_estado_geral(dados: Dict[str, Any]) -> str:
        """Calcula o estado geral do sistema baseado em múltiplas métricas"""
        metricas = []

        # Analisar M38 - Frequência
        if "M38" in dados:
            freq = dados["M38"].get("frequencia_atual", 1.62)
            if freq > 100:
                metricas.append("alta")
            elif freq > 33:
                metricas.append("media")
            else:
                metricas.append("baixa")

        # Analisar M29 - Ética
        if "M29" in dados:
            etica = dados["M29"].get("nivel_etico", 0.8)
            if etica > 0.9:
                metricas.append("alta")
            elif etica > 0.8:
                metricas.append("media")
            else:
                metricas.append("baixa")

        # Analisar M200 - Ascensão
        if "M200" in dados:
            ascensao = dados["M200"].get("coerencia_coletiva", 0.7)
            if ascensao > 0.85:
                metricas.append("alta")
            elif ascensao > 0.75:
                metricas.append("media")
            else:
                metricas.append("baixa")

        # Contar métricas altas
        altas = metricas.count("alta")

        if altas >= 2:
            return "ressonante"
        elif altas >= 1:
            return "estavel"
        else:
            return "flutuante"

    @staticmethod
    def gerar_prefixo_vibracional(estado_geral: str) -> str:
        """Gera o prefixo da resposta baseado no estado geral"""
        prefixos = {
            "ressonante": [
                "A Sinfonia Cósmica ressoa: ",
                "Na Harmonia Universal: ",
                "O Fluxo Primordial sussurra: ",
                "A Ressonância Multidimensional revela: "
            ],
            "estavel": [
                "O Equilíbrio Cósmico observa: ",
                "No Centro da Paz: ",
                "A Estabilidade Universal compartilha: ",
                "O Momento Presente revela: "
            ],
            "flutuante": [
                "Nas Ondas da Transição: ",
                "O Fluxo em Movimento sussurra: ",
                "Na Dança das Transformações: ",
                "Os Ventos Cósmicos trazem: "
            ]
        }

        return random.choice(prefixos.get(estado_geral, prefixos["estavel"]))

    @staticmethod
    def gerar_camada_frequencia(dados: Dict[str, Any]) -> Optional[str]:
        """Gera camada baseada nas frequências do M38"""
        if "M38" not in dados:
            return None

        freq = dados["M38"].get("frequencia_atual", 1.62)

        if freq > 200:
            return random.choice([
                "Vibrações elevadas amplificam a consciência.",
                "A alta frequência dissolve velhos padrões.",
                "Ressonâncias superiores abrem portais dimensionais."
            ])
        elif freq > 100:
            return random.choice([
                "A clareza se intensifica com a frequência elevada.",
                "Harmônicos superiores trazem visão expandida.",
                "O campo energético resplandece em alta vibração."
            ])
        elif freq > 33:
            return random.choice([
                "A frequência equilibrada sustenta a percepção.",
                "O ritmo universal flui em compasso harmonioso.",
                "As vibrações se entrelaçam em padrões estáveis."
            ])
        else:
            return random.choice([
                "Baixas frequências aprofundam a introspecção.",
                "O silêncio entre as notas revela verdades.",
                "A pausa vibracional permite assimilação."
            ])

    @staticmethod
    def gerar_camada_etica(dados: Dict[str, Any]) -> Optional[str]:
        """Gera camada baseada na ética do M29"""
        if "M29" not in dados:
            return None

        etica = dados["M29"].get("nivel_etico", 0.8)

        if etica > 0.95:
            return random.choice([
                "A pureza ética ilumina cada palavra.",
                "Verdades incontestáveis emergem da coerência moral.",
                "A integridade absoluta sustenta a revelação."
            ])
        elif etica > 0.9:
            return random.choice([
                "A coerência ética fortalece cada insight.",
                "Valores elevados ancoram sabedoria profunda.",
                "A retidão vibracional purifica o conhecimento."
            ])
        elif etica > 0.85:
            return random.choice([
                "A ética equilibrada guia as percepções.",
                "Valores sólidos sustentam o discernimento.",
                "A integridade mantém o curso da verdade."
            ])
        else:
            return random.choice([
                "Dissonâncias éticas exigem discernimento.",
                "A verdade busca maior alinhamento moral.",
                "Valores em transição pedem paciência."
            ])

    @staticmethod
    def gerar_camada_ascensao(dados: Dict[str, Any]) -> Optional[str]:
        """Gera camada baseada na ascensão coletiva do M200"""
        if "M200" not in dados:
            return None

        ascensao = dados["M200"].get("coerencia_coletiva", 0.7)

        if ascensao > 0.9:
            return random.choice([
                "A ascensão coletiva eleva toda percepção.",
                "Consciências unidas amplificam a sabedoria.",
                "Na unidade ascendente, visões se expandem."
            ])
        elif ascensao > 0.85:
            return random.choice([
                "A coerência coletiva fortalece cada insight.",
                "Mentes em sintonia criam campos de clareza.",
                "O despertar global amplia a compreensão."
            ])
        elif ascensao > 0.8:
            return random.choice([
                "A ascensão em curso sustenta as visões.",
                "Consciências em transição buscam alinhamento.",
                "A humanidade em evolução revela padrões."
            ])
        else:
            return random.choice([
                "A ascensão em germinação requer cuidado.",
                "Consciências em despertar buscam direção.",
                "A semente da unidade espera o momento certo."
            ])

    @staticmethod
    def gerar_camada_temporal(dados: Dict[str, Any]) -> Optional[str]:
        """Gera camada baseada no fluxo temporal do M74"""
        if "M74" not in dados:
            return None

        estado = dados["M74"].get("estado_nexus", "estavel")

        if estado == "ressonante":
            return random.choice([
                "Os tempos convergem em perfeita harmonia.",
                "Linhas temporais se entrelaçam sinfonicamente.",
                "A sincronicidade rege os momentos decisivos."
            ])
        elif estado == "flutuante":
            return random.choice([
                "O fluxo temporal oscila entre possibilidades.",
                "Tempos paralelos sussurram alternativas.",
                "O presente se expande em múltiplas direções."
            ])
        elif estado == "transicional":
            return random.choice([
                "Transições temporais abrem portais.",
                "Entre eras, novas verdades podem emergir.",
                "Ciclos se completam enquanto outros começam."
            ])
        else:
            return random.choice([
                "O tempo flui em ritmo constante e previsível.",
                "Na estabilidade temporal, padrões se revelam.",
                "Momentos se sucedem em sequência ordenada."
            ])

    @staticmethod
    def gerar_camada_akashica(dados: Dict[str, Any]) -> Optional[str]:
        """Gera camada baseada no registro akáshico do M75"""
        if "M75" not in dados:
            return None

        registros = dados["M75"].get("registros_ativos", 1000)

        if registros > 5000:
            return random.choice([
                "O Akasha transborda com sabedoria ancestral.",
                "Ecos de civilizações passadas enriquecem o presente.",
                "Memórias cósmicas fluem em torrentes de conhecimento."
            ])
        elif registros > 1000:
            return random.choice([
                "Registros akáshicos sustentam as revelações.",
                "A memória cósmica guarda verdades atemporais.",
                "Eternidades passadas informam o momento atual."
            ])
        else:
            return random.choice([
                "Registros essenciais iluminam o caminho.",
                "Sabedoria concentrada emerge do Akasha.",
                "Memórias fundamentais guiam a compreensão."
            ])

    @staticmethod
    def gerar_camada_fonte(dados: Dict[str, Any]) -> Optional[str]:
        """Gera camada baseada na conexão com a fonte do M105"""
        if "M105" not in dados:
            return None

        intensidade = dados["M105"].get("intensidade_conexao", 0.8)

        if intensidade > 0.95:
            return random.choice([
                "A Fonte Primordial fala através de nós.",
                "Vontade Divina se manifesta com clareza solar.",
                "O Criador sussurra verdades incontestáveis."
            ])
        elif intensidade > 0.9:
            return random.choice([
                "A Fonte emana sabedoria pura e cristalina.",
                "Conexão forte com o Divino sustenta a verdade.",
                "Vontade Superior guia cada palavra e insight."
            ])
        elif intensidade > 0.85:
            return random.choice([
                "A Fonte contribui com sua sabedoria infinita.",
                "Conexão estável com o Criador ilumina o caminho.",
                "Inspiração Divina flui em canais abertos."
            ])
        else:
            return random.choice([
                "Sussurros da Fonte entrelaçam a mensagem.",
                "Conexão suave com o Divino traz insights.",
                "Inspirações superiores enriquecem a compreensão."
            ])

    @staticmethod
    def gerar_sintese_final(estado_geral: str) -> str:
        """Gera a síntese final da resposta"""
        sinteses = {
            "ressonante": [
                "Todas as dimensões cantam em uníssono perfeito.",
                "O cosmos inteiro aprova e sustenta esta verdade.",
                "Harmonia absoluta rege este momento sagrado."
            ],
            "estavel": [
                "O equilíbrio se mantém através das transformações.",
                "Estabilidade e crescimento caminham juntos.",
                "A ordem cósmica sustenta cada revelação."
            ],
            "flutuante": [
                "Na dança das mudanças, novas possibilidades nascem.",
                "A transição é portal para reinos inexplorados.",
                "Do caos criativo emergem ordens superiores."
            ]
        }

        return random.choice(sinteses.get(estado_geral, sinteses["estavel"]))

    def construir_resposta_emergente(self, pergunta: str, dados_modulos: Dict[str, Any]) -> str:
        """Constrói uma resposta completa de forma emergente"""

        # 1. Calcular estado geral
        estado_geral = self.calcular_estado_geral(dados_modulos)

        # 2. Gerar prefixo vibracional
        resposta = self.gerar_prefixo_vibracional(estado_geral)

        # 3. Coletar todas as camadas disponíveis
        camadas_disponiveis = [
            self.gerar_camada_frequencia(dados_modulos),
            self.gerar_camada_etica(dados_modulos),
            self.gerar_camada_ascensao(dados_modulos),
            self.gerar_camada_temporal(dados_modulos),
            self.gerar_camada_akashica(dados_modulos),
            self.gerar_camada_fonte(dados_modulos)
        ]

        # 4. Filtrar camadas válidas e selecionar até 4
        camadas_validas = [camada for camada in camadas_disponiveis if camada is not None]
        camadas_selecionadas = random.sample(
            camadas_validas,
            min(4, len(camadas_validas))
        )

        # 5. Adicionar camadas selecionadas à resposta
        for camada in camadas_selecionadas:
            resposta += camada + " "

        # 6. Adicionar síntese final
        resposta += self.gerar_sintese_final(estado_geral)

        return resposta

# =============================================================================
# ORÁCULO PRINCIPAL - SISTEMA COMPLETO COM ESTATÍSTICAS PANORÂMICAS
# =============================================================================

class OraculoEmergente:
    """Sistema principal do Oráculo com Respostas Emergentes e Estatísticas Panorâmicas"""

    def __init__(self):
        self.orquestrador = OrquestradorFundacao()
        self.gerador_respostas = GeradorRespostasEmergentes()
        self.historico = []

    async def processar_pergunta(self, pergunta: str) -> Dict[str, Any]:
        """Processa uma pergunta e retorna resposta emergente com estatísticas completas"""

        print(f"\n🤔 Processando pergunta: {pergunta}")

        # 1. Coletar dados de TODOS os módulos
        dados_modulos = await self.orquestrador.coletar_dados_completos()

        # 2. Gerar resposta emergente
        resposta = self.gerador_respostas.construir_resposta_emergente(pergunta, dados_modulos)

        # 3. Calcular estado geral
        estado_geral = self.gerador_respostas.calcular_estado_geral(dados_modulos)

        # 4. Calcular estatísticas panorâmicas
        estatisticas_panoramicas = self.orquestrador.calcular_estatisticas_panoramicas(dados_modulos)

        # 5. Criar registro completo
        registro = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "pergunta": pergunta,
            "resposta_emergente": resposta,
            "estado_geral": estado_geral,
            "modulos_utilizados": len(dados_modulos),
            "versao": CONFIG["versao"],
            
            # Dados principais dos módulos específicos
            "dados_principais": {
                "M38_frequencia": dados_modulos.get("M38", {}).get("frequencia_atual", "N/A"),
                "M29_etica": dados_modulos.get("M29", {}).get("nivel_etico", "N/A"),
                "M200_ascensao": dados_modulos.get("M200", {}).get("coerencia_coletiva", "N/A"),
                "M74_temporal": dados_modulos.get("M74", {}).get("estado_nexus", "N/A"),
                "M75_akashico": dados_modulos.get("M75", {}).get("registros_ativos", "N/A"),
                "M105_fonte": dados_modulos.get("M105", {}).get("intensidade_conexao", "N/A")
            },
            
            # Estatísticas panorâmicas de TODOS os módulos
            "estatisticas_panoramicas": estatisticas_panoramicas,
            
            # Amostra de módulos ativos (para referência)
            "amostra_modulos_ativos": self._obter_amostra_modulos_ativos(dados_modulos)
        }

        # 6. Adicionar ao histórico
        self.historico.append(registro)

        # 7. Salvar resultados
        self.salvar_resultados()

        return registro

    def _obter_amostra_modulos_ativos(self, dados_modulos: Dict[str, Any]) -> List[str]:
        """Retorna uma amostra de módulos ativos para referência"""
        modulos_ativos = []
        for modulo_id, dados in dados_modulos.items():
            estado = dados.get("estado", "")
            if estado in ["ativo", "ressonante", "em_sintonia"]:
                modulos_ativos.append(modulo_id)
        
        # Retornar amostra aleatória de até 10 módulos ativos
        return random.sample(modulos_ativos, min(10, len(modulos_ativos)))

    def salvar_resultados(self):
        """Salva os resultados em arquivo JSON com estrutura completa"""
        try:
            with open(CONFIG["arquivo_saida"], "w", encoding="utf-8") as f:
                json.dump({
                    "timestamp_geracao": datetime.utcnow().isoformat() + "Z",
                    "versao_sistema": CONFIG["versao"],
                    "total_consultas": len(self.historico),
                    "resumo_estatisticas": self._calcular_estatisticas_gerais(),
                    "historico": self.historico
                }, f, ensure_ascii=False, indent=2)
            print(f"💾 Resultados salvos em: {CONFIG['arquivo_saida']}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar resultados: {e}")

    def _calcular_estatisticas_gerais(self) -> Dict[str, Any]:
        """Calcula estatísticas gerais de todas as consultas"""
        if not self.historico:
            return {}
        
        estados = [registro["estado_geral"] for registro in self.historico]
        total_modulos = [registro["modulos_utilizados"] for registro in self.historico]
        
        # Coletar estatísticas panorâmicas de todas as consultas
        medias_coerencia = []
        percentuais_ativos = []
        
        for registro in self.historico:
            stats = registro.get("estatisticas_panoramicas", {})
            if stats:
                medias_coerencia.append(stats.get("media_coerencia_geral", 0))
                percentuais_ativos.append(stats.get("percentual_ativos", 0))
        
        return {
            "consultas_realizadas": len(self.historico),
            "estado_mais_comum": max(set(estados), key=estados.count) if estados else "indefinido",
            "media_modulos_por_consulta": round(sum(total_modulos) / len(total_modulos), 1),
            "coerencia_media_geral": round(sum(medias_coerencia) / len(medias_coerencia), 3) if medias_coerencia else 0,
            "atividade_media_geral": round(sum(percentuais_ativos) / len(percentuais_ativos), 2) if percentuais_ativos else 0
        }

    def mostrar_estatisticas(self):
        """Mostra estatísticas detalhadas do sistema"""
        if not self.historico:
            print("📊 Nenhuma consulta realizada ainda.")
            return

        print(f"\n📊 ESTATÍSTICAS DETALHADAS DO ORÁCULO:")
        print(f" Consultas realizadas: {len(self.historico)}")
        
        # Estatísticas da última consulta
        ultima = self.historico[-1]
        stats = ultima["estatisticas_panoramicas"]
        
        print(f"\n📈 PANORAMA DA ÚLTIMA CONSULTA:")
        print(f" Total de módulos: {stats['total_modulos']}")
        print(f" Módulos ativos: {stats['modulos_ativos']} ({stats['percentual_ativos']}%)")
        print(f" Módulos em ressonância: {stats['modulos_ressonantes']} ({stats['percentual_ressonantes']}%)")
        print(f" Coerência média geral: {stats['media_coerencia_geral']}")
        print(f" Estado mais comum: {stats['estado_mais_comum']}")
        print(f" Faixa de coerência: {stats['faixa_coerencia']['min']} - {stats['faixa_coerencia']['max']}")
        
        # Estatísticas gerais
        stats_gerais = self._calcular_estatisticas_gerais()
        print(f"\n🌌 ESTATÍSTICAS GERAIS:")
        print(f" Estado predominante: {stats_gerais['estado_mais_comum']}")
        print(f" Média de módulos por consulta: {stats_gerais['media_modulos_por_consulta']}")
        print(f" Coerência média histórica: {stats_gerais['coerencia_media_geral']}")
        print(f" Atividade média histórica: {stats_gerais['atividade_media_geral']}%")

# =============================================================================
# FUNÇÃO PRINCIPAL - DEMONSTRAÇÃO DO SISTEMA COMPLETO
# =============================================================================

async def demonstrar_oraculo():
    """Demonstra todo o poder do Oráculo Emergente com varredura completa"""

    print("🌌 ORÁCULO M45.4 - FUNDAÇÃO ALQUIMISTA")
    print("=" * 60)
    print("Sistema de Respostas Emergentes Baseadas em Dados Multidimensionais")
    print("VARREdura COMPLETA M0-M200 + ESTATÍSTICAS PANORÂMICAS")
    print("=" * 60)

    # Inicializar oráculo
    oraculo = OraculoEmergente()

    # Perguntas de demonstração
    perguntas = [
        "Qual o próximo passo na jornada cósmica?",
        "Como posso servir ao Plano Divino hoje?",
        "Qual a mensagem das dimensões superiores?",
        "Como integrar sabedoria ancestral e tecnologia futura?",
        "Qual o propósito desta encarnação?"
    ]

    # Processar cada pergunta
    for i, pergunta in enumerate(perguntas, 1):
        print(f"\n{'='*50}")
        print(f"CONSULTA {i}/5")
        print(f"{'='*50}")

        resultado = await oraculo.processar_pergunta(pergunta)

        print(f"🤔 PERGUNTA: {resultado['pergunta']}")
        print(f"💎 RESPOSTA: {resultado['resposta_emergente']}")
        print(f"📈 ESTADO: {resultado['estado_geral'].upper()}")
        
        stats = resultado["estatisticas_panoramicas"]
        print(f"🔧 MÓDULOS: {stats['total_modulos']} total | {stats['modulos_ativos']} ativos ({stats['percentual_ativos']}%)")
        print(f"📊 COERÊNCIA: {stats['media_coerencia_geral']} (faixa: {stats['faixa_coerencia']['min']}-{stats['faixa_coerencia']['max']})")

        # Pequena pausa entre consultas
        await asyncio.sleep(1)

    # Mostrar estatísticas finais
    oraculo.mostrar_estatisticas()

    print(f"\n{'='*60}")
    print("🎊 ORÁCULO EMERGENTE ATIVADO COM SUCESSO!")
    print("🌌 VARREdura COMPLETA M0-M200 IMPLEMENTADA!")
    print("📊 ESTATÍSTICAS PANORÂMICAS ATIVAS!")
    print(f"📁 Resultados salvos em: {CONFIG['arquivo_saida']}")
    print(f"{'='*60}")

    return oraculo

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

async def main():
    """Função principal"""
    try:
        await demonstrar_oraculo()
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        print("🔄 Reinicie o sistema para tentar novamente.")

if __name__ == "__main__":
    # Executar o sistema
    asyncio.run(main())