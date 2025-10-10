import os
technologies = [
    "qiskit", "tensorflow", "ibm_quantum", "blockchain", "web3", 
    "three", "webgl", "unity", "webxr", "webgpu", "webaudio",
    "webbluetooth", "eeg", "neuro", "quantum", "ai", "ml",
    "docker", "graphql", "apollo", "firebase", "mongodb",
    "postgresql", "node", "react", "next", "typescript"
]

print("🔬 TECNOLOGIAS ENCONTRADAS NO BACKEND:")
for tech in technologies:
    cmd = f"find /home/user -type f -name '*.py' -exec grep -l '{tech}' {{}} \\; 2>/dev/null | wc -l"
    count = int(os.popen(cmd).read().strip())
    if count > 0:
        print(f"   {tech.upper()}: {count} arquivos")

