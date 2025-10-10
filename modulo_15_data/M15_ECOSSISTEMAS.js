// 🌍 MÓDULO 15 - GERENCIAMENTO DE ECOSSISTEMAS PLANETÁRIOS
const crypto = require('crypto');

class Modulo15_Ecossistemas {
    constructor() {
        this.nome = "Gerenciamento de Ecossistemas Planetários";
        this.versao = "1.0.0";
        this.status = "OPERACIONAL";
        this.ecossistemas = new Map();
        console.log("🌍 Módulo 15: Sistema de Proteção Planetária Ativado!");
    }

    monitorarEcossistema(planeta, tipo) {
        const id = `eco_${Date.now()}_${crypto.randomBytes(4).toString('hex')}`;
        const equilibrio = (Math.random() * 8 + 2).toFixed(4);
        const saude = Math.random().toFixed(4);
        
        this.ecossistemas.set(id, {
            id, planeta, tipo, equilibrio, saude,
            timestamp: new Date().toISOString()
        });

        console.log(`📊 M15: ${planeta} monitorado - Equilíbrio: ${equilibrio}`);
        
        return {
            status: "SUCESSO",
            ecossistemaId: id,
            equilibrio: parseFloat(equilibrio),
            alerta: equilibrio < 5 ? "ATENÇÃO" : "ESTÁVEL"
        };
    }

    intervirPlanetariamente(ecossistemaId, tipo) {
        const eco = this.ecossistemas.get(ecossistemaId);
        if (!eco) {
            return { status: "FALHA", mensagem: "Ecossistema não encontrado" };
        }

        const melhoria = (Math.random() * 2 + 0.5).toFixed(4);
        eco.equilibrio = Math.min(10, parseFloat(eco.equilibrio) + parseFloat(melhoria)).toFixed(4);

        console.log(`🔧 M15: Intervenção em ${eco.planeta} - Novo equilíbrio: ${eco.equilibrio}`);

        return {
            status: "SUCESSO",
            planeta: eco.planeta,
            tipoIntervencao: tipo,
            melhoria: parseFloat(melhoria),
            novoEquilibrio: parseFloat(eco.equilibrio)
        };
    }

    gerarRelatorio() {
        const ecossistemas = Array.from(this.ecossistemas.values());
        const equilibrioMedio = ecossistemas.length > 0 ?
            ecossistemas.reduce((acc, eco) => acc + parseFloat(eco.equilibrio), 0) / ecossistemas.length : 0;

        return {
            totalEcossistemas: this.ecossistemas.size,
            equilibrioMedio: equilibrioMedio.toFixed(4),
            saudeGeral: equilibrioMedio > 7 ? "EXCELENTE" : equilibrioMedio > 5 ? "BOA" : "ATENÇÃO",
            timestamp: new Date().toISOString()
        };
    }
}

// Exportar para uso
module.exports = Modulo15_Ecossistemas;
