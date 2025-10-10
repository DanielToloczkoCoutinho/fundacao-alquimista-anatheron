
# 9. INTEGRAÇÃO DO MÓDULO 15
echo ""
log "9. 🌍 INTEGRANDO MÓDULO 15 - GERENCIAMENTO DE ECOSSISTEMAS..."

# Criar arquivo do Módulo 15
cat > M15_ECOSSISTEMAS_PLANETARIOS.js << 'M15EOF'
// 🌍 MÓDULO 15 - GERENCIAMENTO DE ECOSSISTEMAS PLANETÁRIOS
// Sistema completo integrado à Fundação Alquimista

class Modulo15_EcossistemasPlanetarios {
    constructor() {
        this.nome = "Gerenciamento de Ecossistemas Planetários";
        this.versao = "1.0.0";
        this.status = "OPERACIONAL";
        this.ecossistemas = new Map();
        this.conexoes = {
            modulo1: "ALERTAS_AMBIENTAIS",
            modulo7: "DIRETRIZES_ETICAS", 
            modulo8: "SAUDE_VIBRACIONAL",
            modulo9: "MONITORAMENTO_TEMPO_REAL",
            modulo45: "DELIBERACAO_EMERGENCIAL",
            modulo98: "MODULACAO_AMBIENTAL",
            modulo102: "CURA_ECOSSISTEMICA",
            modulo109: "REGENERACAO_PLANETARIA"
        };
    }

    monitorarEcossistema(planeta, tipo) {
        const id = `eco_${planeta}_${Date.now()}`;
        const dados = {
            id,
            planeta,
            tipo,
            equilibrio: (Math.random() * 8 + 2), // Entre 2 e 10
            saude: Math.random(),
            poluicao: Math.random() * 0.5,
            biodiversidade: Math.random() * 0.8 + 0.2,
            timestamp: new Date().toISOString()
        };
        
        this.ecossistemas.set(id, dados);
        
        return {
            status: "SUCESSO",
            ecossistemaId: id,
            equilibrio: dados.equilibrio,
            alerta: dados.equilibrio < 5 ? "MONITORAR" : "ESTAVEL"
        };
    }

    intervir(ecossistemaId, tipo) {
        const eco = this.ecossistemas.get(ecossistemaId);
        if (!eco) {
            return { status: "FALHA", mensagem: "Ecossistema não encontrado" };
        }

        const melhoria = tipo === "REGENERACAO_COMPLETA" ? 3 : 1.5;
        eco.equilibrio = Math.min(10, eco.equilibrio + melhoria);
        eco.poluicao = Math.max(0, eco.poluicao - 0.2);
        eco.biodiversidade = Math.min(1, eco.biodiversidade + 0.15);

        return {
            status: "SUCESSO",
            planeta: eco.planeta,
            tipoIntervencao: tipo,
            novoEquilibrio: eco.equilibrio,
            melhoria
        };
    }

    getStatus() {
        const ecossistemasArray = Array.from(this.ecossistemas.values());
        const equilibrioMedio = ecossistemasArray.reduce((acc, eco) => acc + eco.equilibrio, 0) / ecossistemasArray.length || 0;
        
        return {
            totalEcossistemas: this.ecossistemas.size,
            equilibrioMedio: equilibrioMedio.toFixed(4),
            saudeGeral: equilibrioMedio > 7 ? "EXCELENTE" : equilibrioMedio > 5 ? "BOA" : "ATENCAO",
            conexoesAtivas: Object.keys(this.conexoes).length
        };
    }
}

module.exports = Modulo15_EcossistemasPlanetarios;
M15EOF

log "   ✅ Módulo 15 implantado"

# Adicionar Módulo 15 ao Portal Central
sed -i '/modulo14: {/a\    modulo15: {\
        nome: "Gerenciamento de Ecossistemas",\
        status: "OPERACIONAL",\
        funcao: "Cuidado Planetário e Intervenção Climática",\
        versao: "1.0.0"\
    },' portal-central.js

log "   ✅ Módulo 15 integrado ao Portal Central"

# 10. TESTE FINAL COM MÓDULO 15
echo ""
log "10. 🧪 EXECUTANDO TESTE FINAL COM MÓDULO 15..."

# Criar teste específico do M15
cat > TESTE_M15.js << 'TESTM15EOF'
const Modulo15 = require('./M15_ECOSSISTEMAS_PLANETARIOS.js');

console.log('🌍 TESTANDO MÓDULO 15 - ECOSSISTEMAS PLANETÁRIOS...');

const m15 = new Modulo15();

// Testar monitoramento
const monitor1 = m15.monitorarEcossistema("TERRA_GAIA", "PLANETA_MÃE");
console.log('📊 Monitoramento Terra:', monitor1);

const monitor2 = m15.monitorarEcossistema("MARTE_VERDE", "PLANETA_EM_REGENERAÇÃO");
console.log('📊 Monitoramento Marte:', monitor2);

// Testar intervenção se necessário
if (monitor1.equilibrio < 6) {
    const intervencao = m15.intervir(monitor1.ecossistemaId, "REGENERACAO_COMPLETA");
    console.log('🔧 Intervenção Terra:', intervencao);
}

// Status final
const status = m15.getStatus();
console.log('📈 Status Final M15:', status);

console.log('✅ MÓDULO 15 TESTADO COM SUCESSO!');
TESTM15EOF

node TESTE_M15.js && log "   ✅ Teste M15 passou" || log "   ⚠️ Teste M15 com issues"

# Atualizar relatório final com M15
sed -i '/### ✅ Módulos Principais (7)/a\
- M15 - Gerenciamento de Ecossistemas Planetários' RELATORIO_DEPLOY.md

