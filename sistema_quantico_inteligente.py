#!/usr/bin/env python3
"""
🌌 SISTEMA QUÂNTICO INTELIGENTE DA FUNDAÇÃO
Detecta automaticamente o melhor ambiente disponível
"""

import sys
import subprocess
import os
from pathlib import Path

class QuantumEnvironmentDetector:
    """Detector de ambientes quânticos disponíveis"""
    
    def __init__(self):
        self.available_environments = []
        self.recommendation = ""
        
    def check_nix_environment(self):
        """Verificar ambiente Nix"""
        try:
            # Verificar se estamos no Nix
            nix_store = Path("/nix/store")
            if nix_store.exists():
                return "nix_detected"
            return "not_nix"
        except:
            return "unknown"
    
    def check_docker(self):
        """Verificar Docker"""
        try:
            result = subprocess.run(["docker", "--version"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return "available"
            return "not_available"
        except:
            return "not_available"
    
    def check_python_packages(self):
        """Verificar pacotes Python"""
        packages = {
            'numpy': False,
            'scipy': False, 
            'qiskit': False
        }
        
        for package in packages:
            try:
                __import__(package)
                packages[package] = True
            except ImportError:
                pass
                
        return packages
    
    def detect_environments(self):
        """Detectar todos os ambientes disponíveis"""
        print("🔍 DETECTANDO AMBIENTES DISPONÍVEIS...")
        
        # Verificar Nix
        nix_status = self.check_nix_environment()
        print(f"   🐚 Nix: {nix_status}")
        
        # Verificar Docker
        docker_status = self.check_docker()
        print(f"   🐳 Docker: {docker_status}")
        
        # Verificar pacotes Python
        packages = self.check_python_packages()
        installed = sum(packages.values())
        total = len(packages)
        print(f"   📦 Pacotes Python: {installed}/{total}")
        
        # Determinar ambientes disponíveis
        if docker_status == "available":
            self.available_environments.append("docker")
            
        if installed == total:
            self.available_environments.append("python_native")
            
        self.available_environments.append("simulator_pure")
        
        # Recomendação
        if "docker" in self.available_environments:
            self.recommendation = "docker"
        elif "python_native" in self.available_environments:
            self.recommendation = "python_native"
        else:
            self.recommendation = "simulator_pure"
    
    def run_quantum_system(self):
        """Executar no melhor ambiente disponível"""
        print(f"\n🎯 EXECUTANDO NO AMBIENTE: {self.recommendation.upper()}")
        
        if self.recommendation == "docker":
            self.run_docker_quantum()
        elif self.recommendation == "python_native":
            self.run_native_quantum()
        else:
            self.run_pure_simulator()
    
    def run_docker_quantum(self):
        """Executar via Docker"""
        print("🚀 INICIANDO SISTEMA DOCKER QUÂNTICO...")
        
        # Build da imagem se necessário
        build_cmd = [
            "docker", "build", "-t", "fundacao-quantica", 
            "-f", "Dockerfile.quantum.nix", "."
        ]
        
        subprocess.run(build_cmd, capture_output=True)
        
        # Executar container
        run_cmd = [
            "docker", "run", "--rm", "-it",
            "fundacao-quantica"
        ]
        
        subprocess.run(run_cmd)
    
    def run_native_quantum(self):
        """Executar nativamente"""
        print("⚡ INICIANDO SISTEMA QUÂNTICO NATIVO...")
        
        try:
            from qiskit import QuantumCircuit, Aer
            
            qc = QuantumCircuit(3, 3)
            qc.h(0)
            qc.cx(0, 1)
            qc.cx(1, 2)
            qc.measure_all()
            
            print("🔮 Circuito Criado:")
            print(qc)
            
            simulator = Aer.get_backend('aer_simulator')
            result = simulator.run(qc, shots=100).result()
            counts = result.get_counts()
            
            print(f"📊 Resultados: {counts}")
            print("✅ SISTEMA NATIVO OPERACIONAL!")
            
        except Exception as e:
            print(f"❌ Erro no sistema nativo: {e}")
            print("🔄 Alternando para simulador puro...")
            self.run_pure_simulator()
    
    def run_pure_simulator(self):
        """Executar simulador puro"""
        print("🎯 INICIANDO SIMULADOR QUÂNTICO PURO...")
        
        # Importar e executar simulador
        from simulador_quantico_puro import main as run_simulator
        run_simulator()

def main():
    """Função principal"""
    print("🌌 SISTEMA QUÂNTICO INTELIGENTE - FUNDAÇÃO ALQUIMISTA")
    print("=" * 60)
    
    detector = QuantumEnvironmentDetector()
    detector.detect_environments()
    
    print(f"\n📊 AMBIENTES DISPONÍVEIS: {', '.join(detector.available_environments)}")
    print(f"🎯 RECOMENDAÇÃO: {detector.recommendation}")
    
    detector.run_quantum_system()

if __name__ == "__main__":
    main()
