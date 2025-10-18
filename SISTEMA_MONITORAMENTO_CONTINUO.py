#!/usr/bin/env python3
"""
📊 SISTEMA DE MONITORAMENTO CONTÍNUO - FUNDAÇÃO ALQUIMISTA
⚛️ Monitoramento em tempo real de performance e métricas
🌌 Alertas automáticos e dashboard integrado
"""

import time
import psutil
import json
from datetime import datetime
from pathlib import Path

class MonitoramentoContinuo:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.metricas = {}
        self.alertas = []
    
    def monitorar_performance(self):
        """Monitorar performance do sistema"""
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'active_scripts': self._contar_scripts_ativos()
        }
        
        self.metricas[datetime.now().strftime('%H:%M:%S')] = metrics
        return metrics
    
    def _contar_scripts_ativos(self):
        """Contar scripts Python ativos"""
        count = 0
        for process in psutil.process_iter(['name']):
            if process.info['name'] and 'python' in process.info['name'].lower():
                count += 1
        return count
    
    def verificar_alertas(self):
        """Verificar e gerar alertas"""
        metrics = self.monitorar_performance()
        
        if metrics['cpu_percent'] > 80:
            self.alertas.append(f"🚨 CPU: {metrics['cpu_percent']}%")
        if metrics['memory_percent'] > 85:
            self.alertas.append(f"🚨 MEMÓRIA: {metrics['memory_percent']}%")
        
        return self.alertas
    
    def gerar_dashboard(self):
        """Gerar dashboard de monitoramento"""
        print("📊 DASHBOARD DE MONITORAMENTO - FUNDAÇÃO ALQUIMISTA")
        print("=" * 50)
        
        metrics = self.monitorar_performance()
        alertas = self.verificar_alertas()
        
        print(f"⏰ Última atualização: {datetime.now().strftime('%H:%M:%S')}")
        print(f"🖥️  CPU: {metrics['cpu_percent']}%")
        print(f"💾 Memória: {metrics['memory_percent']}%")
        print(f"💿 Disco: {metrics['disk_usage']}%")
        print(f"🐍 Scripts ativos: {metrics['active_scripts']}")
        
        if alertas:
            print(f"🔔 ALERTAS: {', '.join(alertas)}")
        else:
            print("✅ SISTEMA ESTÁVEL")
        
        return metrics

# Execução contínua do monitoramento
if __name__ == "__main__":
    monitor = MonitoramentoContinuo()
    while True:
        monitor.gerar_dashboard()
        time.sleep(30)  # Atualizar a cada 30 segundos
