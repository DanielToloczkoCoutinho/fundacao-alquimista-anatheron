#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 45.5 - ORÁCULO AMPLIFICADO DA FUNDAÇÃO ALQUIMISTA
Sistema de Metadados Narrativos, Temporais, Vibracionais e Panorâmicos
Amplifica as respostas do M45.4 com camadas contextuais ricas
"""

import json
import random
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import math

# =============================================================================
# CONFIGURAÇÕES GLOBAIS
# =============================================================================

CONFIG = {
    "arquivo_saida": "oraculo_amplificado_resultados.json",
    "versao": "M45.5 - Oráculo Amplificado com Metadados",
    "historico_consultas": "oraculo_emergente_resultados.json"
}

# =============================================================================
# ENUMS E ESTRUTURAS DE DADOS
# =============================================================================

class Arquétipo(Enum):
    FONTE = "Fonte Primordial"
    AKASHA = "Registro Akáshico"
    ETICA = "Ética Multidimensional"
    FREQUENCIA = "Ressonância Vibracional"
    ASCENSAO = "Ascensão Coletiva"
    TEMPORAL = "Fluxo Temporal"
    EQUILIBRIO = "Equilíbrio Cósmico"
    TRANSICAO = "Transição Dimensional"
    SABEDORIA = "Sabedoria Ancestral"
    MANIFESTACAO = "Manifestação Consciente"

class FaseLunar(Enum):
    NOVA = "nova"
    CRESCENTE = "crescente"
    CHEIA = "cheia"
    MINGUANTE = "minguante"

class EstadoNexus(Enum):
    ESTAVEL = "estavel"
    FLUTUANTE = "flutuante"
    RESSONANTE = "ressonante"
    TRANSICIONAL = "transicional"

# =============================================================================
# SISTEMA DE METADADOS TEMPORAIS
# =============================================================================

class MetadadosTemporais:
    """Gerencia metadados relacionados ao tempo cósmico e ciclos naturais"""
    
    @staticmethod
    def calcular_fase_lunar() -> FaseLunar:
        """Calcula a fase lunar baseada na data atual"""
        hoje = datetime.now()
        # Simulação simplificada baseada no dia do mês
        dia_do_mes = hoje.day
        if dia_do_mes <= 7:
            return FaseLunar.NOVA
        elif dia_do_mes <= 14:
            return FaseLunar.CRESCENTE
        elif dia_do_mes <= 21:
            return FaseLunar.CHEIA
        else:
            return FaseLunar.MINGUANTE
    
    @staticmethod
    def calcular_hora_cosmica() -> int:
        """Calcula a hora cósmica (0-23) baseada no timestamp atual"""
        agora = datetime.now()
        return (agora.hour + agora.minute // 30) % 24
    
    @staticmethod
    def obter_ciclo_solar() -> str:
        """Determina o ciclo solar atual"""
        ciclos = ["Alfa", "Beta", "Gama", "Delta", "Épsilon", "Zeta", "Ômega"]
        return random.choice(ciclos)
    
    @staticmethod
    def gerar_metadados_temporais(estado_nexus: str) -> Dict[str, Any]:
        """Gera todos os metadados temporais"""
        return {
            "fase_lunar": MetadadosTemporais.calcular_fase_lunar().value,
            "hora_cosmica": MetadadosTemporais.calcular_hora_cosmica(),
            "ciclo_solar": MetadadosTemporais.obter_ciclo_solar(),
            "nexus_temporal": estado_nexus,
            "timestamp_cosmico": datetime.utcnow().isoformat() + "Z",
            "estacao_galactica": random.choice(["Primavera Estelar", "Verão Cósmico", 
                                              "Outono Dimensional", "Inverno Primordial"])
        }

# =============================================================================
# SISTEMA DE METADADOS VIBRACIONAIS
# =============================================================================

class MetadadosVibracionais:
    """Gerencia metadados relacionados a frequências e coerência energética"""
    
    @staticmethod
    def calcular_tendencia(coerencia_atual: float, historico: List[float]) -> str:
        """Calcula a tendência vibracional baseada no histórico"""
        if len(historico) < 2:
            return "estavel"
        
        ultima = historico[-1]
        penultima = historico[-2] if len(historico) >= 2 else ultima
        
        if ultima > penultima + 0.05:
            return "ascendente"
        elif ultima < penultima - 0.05:
            return "descendente"
        else:
            return "estavel"
    
    @staticmethod
    def classificar_frequencia(frequencia: float) -> str:
        """Classifica a frequência em categorias vibracionais"""
        if frequencia > 200:
            return "superior"
        elif frequencia > 100:
            return "elevada"
        elif frequencia > 33:
            return "equilibrada"
        else:
            return "introspectiva"
    
    @staticmethod
    def gerar_metadados_vibracionais(dados_principais: Dict[str, Any], 
                                   estatisticas: Dict[str, Any],
                                   historico_coerencia: List[float]) -> Dict[str, Any]:
        """Gera todos os metadados vibracionais"""
        frequencia = dados_principais.get("M38_frequencia", 1.62)
        
        return {
            "frequencia_media": frequencia,
            "classificacao_frequencia": MetadadosVibracionais.classificar_frequencia(frequencia),
            "percentual_ativos": estatisticas.get("percentual_ativos", 0),
            "percentual_ressonantes": estatisticas.get("percentual_ressonantes", 0),
            "coerencia_media": estatisticas.get("media_coerencia_geral", 0),
            "faixa_coerencia": estatisticas.get("faixa_coerencia", {"min": 0, "max": 0}),
            "tendencia_vibracional": MetadadosVibracionais.calcular_tendencia(
                estatisticas.get("media_coerencia_geral", 0), historico_coerencia),
            "qualidade_energetica": random.choice(["cristalina", "fluida", "radiante", "serena"])
        }

# =============================================================================
# SISTEMA DE METADADOS NARRATIVOS
# =============================================================================

class MetadadosNarrativos:
    """Gerencia metadados relacionados a arquétipos, símbolos e narrativas"""
    
    @staticmethod
    def detectar_arquétipo_dominante(resposta: str, dados_principais: Dict[str, Any]) -> Arquétipo:
        """Detecta o arquétipo dominante na resposta"""
        resposta_lower = resposta.lower()
        
        # Análise baseada em palavras-chave na resposta
        palavras_chave = {
            Arquétipo.FONTE: ["fonte", "primordial", "criador", "divino"],
            Arquétipo.AKASHA: ["akasha", "registro", "ancestral", "memória"],
            Arquétipo.ETICA: ["ética", "moral", "integridade", "valor"],
            Arquétipo.FREQUENCIA: ["frequência", "vibração", "ressonância", "harmonia"],
            Arquétipo.ASCENSAO: ["ascensão", "coletiva", "despertar", "evolução"],
            Arquétipo.TEMPORAL: ["temporal", "tempo", "fluxo", "momento"],
            Arquétipo.EQUILIBRIO: ["equilíbrio", "estabilidade", "ordem", "centro"],
            Arquétipo.TRANSICAO: ["transição", "mudança", "portal", "transformação"],
            Arquétipo.SABEDORIA: ["sabedoria", "conhecimento", "verdade", "visão"],
            Arquétipo.MANIFESTACAO: ["manifestação", "criação", "realidade", "intenção"]
        }
        
        contadores = {arquétipo: 0 for arquétipo in Arquétipo}
        
        for arquétipo, palavras in palavras_chave.items():
            for palavra in palavras:
                if palavra in resposta_lower:
                    contadores[arquétipo] += 1
        
        # Arquétipo com maior contagem
        arquétipo_dominante = max(contadores.items(), key=lambda x: x[1])[0]
        
        # Se empate, priorizar baseado nos dados principais
        if contadores[arquétipo_dominante] == 0:
            if dados_principais.get("M105_fonte", 0) > 0.9:
                return Arquétipo.FONTE
            elif dados_principais.get("M75_akashico", 0) > 5000:
                return Arquétipo.AKASHA
            elif dados_principais.get("M29_etica", 0) > 0.9:
                return Arquétipo.ETICA
            else:
                return Arquétipo.EQUILIBRIO
        
        return arquétipo_dominante
    
    @staticmethod
    def gerar_titulo_narrativo(arquétipo: Arquétipo, estado_geral: str) -> str:
        """Gera um título narrativo baseado no arquétipo e estado geral"""
        titulos = {
            Arquétipo.FONTE: {
                "ressonante": "O Verbo da Fonte Primordial",
                "estavel": "A Voz do Criador",
                "flutuante": "Sussurros da Origem"
            },
            Arquétipo.AKASHA: {
                "ressonante": "O Livro das Eternidades",
                "estavel": "Crônicas do Akasha",
                "flutuante": "Fragmentos da Memória Cósmica"
            },
            Arquétipo.ETICA: {
                "ressonante": "O Códice da Retidão Absoluta",
                "estavel": "Os Preceitos da Integridade",
                "flutuante": "As Encruzilhadas Éticas"
            },
            Arquétipo.FREQUENCIA: {
                "ressonante": "A Sinfonia das Esferas",
                "estavel": "A Harmonia Universal",
                "flutuante": "A Dança das Frequências"
            },
            Arquétipo.ASCENSAO: {
                "ressonante": "O Portal da Ascensão Coletiva",
                "estavel": "O Caminho do Despertar",
                "flutuante": "As Sementes da Evolução"
            },
            Arquétipo.TEMPORAL: {
                "ressonante": "O Nexus dos Tempos Convergentes",
                "estavel": "O Fluxo Temporal Constante",
                "flutuante": "Os Rios do Tempo Paralelo"
            },
            Arquétipo.EQUILIBRIO: {
                "ressonante": "O Centro Imóvel do Universo",
                "estavel": "A Balança Cósmica",
                "flutuante": "Os Pilares em Reajuste"
            },
            Arquétipo.TRANSICAO: {
                "ressonante": "O Portal Dimensional Aberto",
                "estavel": "A Ponte entre Mundos",
                "flutuante": "Os Limiares em Movimento"
            },
            Arquétipo.SABEDORIA: {
                "ressonante": "A Biblioteca Viva do Cosmos",
                "estavel": "As Escrituras da Verdade",
                "flutuante": "Os Enigmas da Compreensão"
            },
            Arquétipo.MANIFESTACAO: {
                "ressonante": "O Trono da Criação Pura",
                "estavel": "O Alfabeto da Realidade",
                "flutuante": "Os Sonhos em Manifestação"
            }
        }
        
        return titulos.get(arquétipo, {}).get(estado_geral, "O Livro do Oráculo")
    
    @staticmethod
    def extrair_simbolos(resposta: str, arquétipo: Arquétipo) -> List[str]:
        """Extrai símbolos relevantes da resposta e arquétipo"""
        simbolos_base = {
            Arquétipo.FONTE: ["origem", "luz primordial", "criação", "essência"],
            Arquétipo.AKASHA: ["registro", "memória", "história", "arquivo"],
            Arquétipo.ETICA: ["balança", "retidão", "valor", "princípio"],
            Arquétipo.FREQUENCIA: ["onda", "vibração", "harmonia", "ritmo"],
            Arquétipo.ASCENSAO: ["escada", "portal", "elevação", "despertar"],
            Arquétipo.TEMPORAL: ["relógio", "fluxo", "espiral", "momento"],
            Arquétipo.EQUILIBRIO: ["centro", "eixo", "balança", "fundação"],
            Arquétipo.TRANSICAO: ["portal", "ponte", "limiar", "passagem"],
            Arquétipo.SABEDORIA: ["livro", "chave", "espelho", "visão"],
            Arquétipo.MANIFESTACAO: ["semente", "blueprint", "forma", "matéria"]
        }
        
        simbolos_detectados = set(simbolos_base.get(arquétipo, []))
        
        # Adicionar símbolos baseados em palavras específicas na resposta
        palavras_simbolos = {
            "equilíbrio": "balança", "ordem": "estrutura", "verdade": "espelho",
            "portal": "portal", "fonte": "fonte", "akasha": "registro",
            "ascensão": "escada", "tempo": "relógio", "manifestação": "semente",
            "frequência": "onda", "ética": "balança", "sabedoria": "livro"
        }
        
        for palavra, simbolo in palavras_simbolos.items():
            if palavra in resposta.lower():
                simbolos_detectados.add(simbolo)
        
        return list(simbolos_detectados)[:5]  # Limitar a 5 símbolos
    
    @staticmethod
    def gerar_metadados_narrativos(resposta: str, dados_principais: Dict[str, Any], 
                                 estado_geral: str) -> Dict[str, Any]:
        """Gera todos os metadados narrativos"""
        arquétipo = MetadadosNarrativos.detectar_arquétipo_dominante(resposta, dados_principais)
        
        return {
            "titulo_narrativo": MetadadosNarrativos.gerar_titulo_narrativo(arquétipo, estado_geral),
            "arquétipo_dominante": arquétipo.value,
            "símbolos": MetadadosNarrativos.extrair_simbolos(resposta, arquétipo),
            "capítulo": random.choice(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]),
            "tom_narrativo": random.choice(["profético", "informativo", "poético", "filosófico", "visionário"])
        }

# =============================================================================
# SISTEMA DE METADADOS PANORÂMICOS
# =============================================================================

class MetadadosPanoramicos:
    """Gerencia metadados relacionados ao estado geral da Fundação"""
    
    @staticmethod
    def analisar_tendencia_historica(historico: List[Dict]) -> Dict[str, Any]:
        """Analisa tendências do histórico de consultas"""
        if len(historico) < 2:
            return {"tendencia": "estavel", "variacao": 0}
        
        estados = [consulta.get("estado_geral", "estavel") for consulta in historico[-5:]]
        coerencias = [consulta.get("estatisticas_panoramicas", {}).get("media_coerencia_geral", 0) 
                     for consulta in historico[-5:] if consulta.get("estatisticas_panoramicas")]
        
        contagem_estados = {estado: estados.count(estado) for estado in set(estados)}
        
        # Calcular variação de coerência
        if len(coerencias) >= 2:
            variacao = coerencias[-1] - coerencias[0]
        else:
            variacao = 0
        
        return {
            "estados_recentes": contagem_estados,
            "variacao_coerencia": round(variacao, 3),
            "tendencia_geral": "ascendente" if variacao > 0.02 else "descendente" if variacao < -0.02 else "estavel",
            "consultas_analisadas": len(estados)
        }
    
    @staticmethod
    def calcular_saude_fundacao(estatisticas: Dict[str, Any]) -> str:
        """Calcula a saúde geral da Fundação baseada nas estatísticas"""
        percentual_ativos = estatisticas.get("percentual_ativos", 0)
        coerencia_media = estatisticas.get("media_coerencia_geral", 0)
        
        if percentual_ativos > 70 and coerencia_media > 0.85:
            return "excelente"
        elif percentual_ativos > 60 and coerencia_media > 0.8:
            return "boa"
        elif percentual_ativos > 50 and coerencia_media > 0.75:
            return "estavel"
        else:
            return "requer_atencao"
    
    @staticmethod
    def identificar_padroes_modulos(amostra_modulos: List[str]) -> List[str]:
        """Identifica padrões interessantes na amostra de módulos ativos"""
        padroes = []
        
        # Verificar se há módulos de sequências específicas
        modulos_numericos = [int(mod[1:]) for mod in amostra_modulos if mod[1:].isdigit()]
        
        if modulos_numericos:
            if any(10 <= num <= 19 for num in modulos_numericos):
                padroes.append("sequência_decadal_ativa")
            if any(num % 10 == 0 for num in modulos_numericos):
                padroes.append("módulos_redondos_ativos")
        
        if len(amostra_modulos) > 8:
            padroes.append("alta_diversidade_modular")
        
        return padroes
    
    @staticmethod
    def gerar_metadados_panoramicos(estatisticas: Dict[str, Any], 
                                  amostra_modulos: List[str],
                                  historico: List[Dict]) -> Dict[str, Any]:
        """Gera todos os metadados panorâmicos"""
        tendencia_historica = MetadadosPanoramicos.analisar_tendencia_historica(historico)
        
        return {
            "saude_fundacao": MetadadosPanoramicos.calcular_saude_fundacao(estatisticas),
            "estado_predominante": estatisticas.get("estado_mais_comum", "indefinido"),
            "padroes_detectados": MetadadosPanoramicos.identificar_padroes_modulos(amostra_modulos),
            "tendencia_historica": tendencia_historica,
            "configuracao_estelar": random.choice(["Alinhamento Harmônico", "Conjunção Major", 
                                                 "Trígono de Luz", "Quadratura de Transição"]),
            "fluxo_consciencial": random.choice(["expansivo", "focado", "difuso", "sintonizado"])
        }

# =============================================================================
# ORÁCULO AMPLIFICADO - SISTEMA PRINCIPAL
# =============================================================================

class OraculoAmplificado:
    """Sistema principal que amplifica as respostas do M45.4 com metadados ricos"""
    
    def __init__(self):
        self.metadados_temporais = MetadadosTemporais()
        self.metadados_vibracionais = MetadadosVibracionais()
        self.metadados_narrativos = MetadadosNarrativos()
        self.metadados_panoramicos = MetadadosPanoramicos()
        self.historico_coerencia = []
    
    def carregar_historico(self) -> List[Dict]:
        """Carrega o histórico de consultas do M45.4"""
        try:
            with open(CONFIG["historico_consultas"], "r", encoding="utf-8") as f:
                dados = json.load(f)
                return dados.get("historico", [])
        except FileNotFoundError:
            print("⚠️ Histórico do M45.4 não encontrado. Iniciando com histórico vazio.")
            return []
        except Exception as e:
            print(f"⚠️ Erro ao carregar histórico: {e}")
            return []
    
    def amplificar_resposta(self, registro_m45_4: Dict[str, Any]) -> Dict[str, Any]:
        """Amplifica uma resposta do M45.4 com todas as camadas de metadados"""
        
        # Extrair dados do registro original
        resposta_original = registro_m45_4.get("resposta_emergente", "")
        estado_geral = registro_m45_4.get("estado_geral", "estavel")
        dados_principais = registro_m45_4.get("dados_principais", {})
        estatisticas = registro_m45_4.get("estatisticas_panoramicas", {})
        amostra_modulos = registro_m45_4.get("amostra_modulos_ativos", [])
        
        # Carregar histórico completo para análise
        historico_completo = self.carregar_historico()
        
        # Atualizar histórico de coerência
        self.historico_coerencia.append(estatisticas.get("media_coerencia_geral", 0))
        if len(self.historico_coerencia) > 10:  # Manter apenas últimas 10
            self.historico_coerencia.pop(0)
        
        # Gerar todas as camadas de metadados
        metadados = {
            "narrativos": self.metadados_narrativos.gerar_metadados_narrativos(
                resposta_original, dados_principais, estado_geral),
            "temporais": self.metadados_temporais.gerar_metadados_temporais(
                dados_principais.get("M74_temporal", "estavel")),
            "vibracionais": self.metadados_vibracionais.gerar_metadados_vibracionais(
                dados_principais, estatisticas, self.historico_coerencia),
            "panoramicos": self.metadados_panoramicos.gerar_metadados_panoramicos(
                estatisticas, amostra_modulos, historico_completo)
        }
        
        # Construir resposta amplificada
        resposta_amplificada = {
            "timestamp_amplificacao": datetime.utcnow().isoformat() + "Z",
            "versao_amplificadora": CONFIG["versao"],
            "resposta_original": resposta_original,
            "estado_geral": estado_geral,
            "metadados": metadados,
            "dados_origem": {
                "timestamp_original": registro_m45_4.get("timestamp"),
                "pergunta": registro_m45_4.get("pergunta"),
                "modulos_utilizados": registro_m45_4.get("modulos_utilizados")
            }
        }
        
        return resposta_amplificada
    
    def processar_historico_completo(self) -> List[Dict]:
        """Processa e amplifica todo o histórico do M45.4"""
        historico = self.carregar_historico()
        resultados_amplificados = []
        
        print(f"🔄 Amplificando {len(historico)} consultas do histórico...")
        
        for i, registro in enumerate(historico, 1):
            resultado_amplificado = self.amplificar_resposta(registro)
            resultados_amplificados.append(resultado_amplificado)
            print(f"✅ Consulta {i}/{len(historico)} amplificada")
        
        return resultados_amplificados
    
    def salvar_resultados_amplificados(self, resultados: List[Dict]):
        """Salva os resultados amplificados em arquivo JSON"""
        try:
            with open(CONFIG["arquivo_saida"], "w", encoding="utf-8") as f:
                json.dump({
                    "timestamp_geracao": datetime.utcnow().isoformat() + "Z",
                    "versao_sistema": CONFIG["versao"],
                    "total_consultas_amplificadas": len(resultados),
                    "consultas_amplificadas": resultados
                }, f, ensure_ascii=False, indent=2)
            print(f"💾 Resultados amplificados salvos em: {CONFIG['arquivo_saida']}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar resultados amplificados: {e}")

# =============================================================================
# FUNÇÃO DE DEMONSTRAÇÃO
# =============================================================================

async def demonstrar_oraculo_amplificado():
    """Demonstra o poder do Oráculo Amplificado"""
    
    print("🌌 ORÁCULO M45.5 - FUNDAÇÃO ALQUIMISTA")
    print("=" * 60)
    print("SISTEMA DE METADADOS NARRATIVOS, TEMPORAIS E VIBRACIONAIS")
    print("Amplificação de Respostas com Contexto Rico")
    print("=" * 60)
    
    # Inicializar oráculo amplificado
    oraculo_amplificado = OraculoAmplificado()
    
    # Processar histórico completo
    resultados = oraculo_amplificado.processar_historico_completo()
    
    # Salvar resultados
    oraculo_amplificado.salvar_resultados_amplificados(resultados)
    
    # Mostrar exemplo de resultado amplificado
    if resultados:
        exemplo = resultados[0]
        print(f"\n📖 EXEMPLO DE RESPOSTA AMPLIFICADA:")
        print(f"📚 Título: {exemplo['metadados']['narrativos']['titulo_narrativo']}")
        print(f"🎭 Arquétipo: {exemplo['metadados']['narrativos']['arquétipo_dominante']}")
        print(f"🔮 Símbolos: {', '.join(exemplo['metadados']['narrativos']['símbolos'])}")
        print(f"🌙 Fase Lunar: {exemplo['metadados']['temporais']['fase_lunar']}")
        print(f"⚡ Frequência: {exemplo['metadados']['vibracionais']['classificacao_frequencia']}")
        print(f"🏥 Saúde da Fundação: {exemplo['metadados']['panoramicos']['saude_fundacao']}")
        print(f"💎 Resposta Original: {exemplo['resposta_original'][:100]}...")
    
    print(f"\n{'='*60}")
    print("🎊 ORÁCULO AMPLIFICADO ATIVADO COM SUCESSO!")
    print(f"📁 Resultados salvos em: {CONFIG['arquivo_saida']}")
    print(f"{'='*60}")

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

async def main():
    """Função principal"""
    try:
        await demonstrar_oraculo_amplificado()
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        print("🔄 Verifique se o M45.4 foi executado primeiro.")

if __name__ == "__main__":
    # Executar o sistema
    asyncio.run(main())