![Language Python](https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge&logo=python&logoColor=white)
![Language C++](https://img.shields.io/badge/Language-C%2B%2B_11-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Platform ESP32](https://img.shields.io/badge/Hardware-ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-Flood_Fill-green?style=for-the-badge)
![Simulator MMS](https://img.shields.io/badge/Simulator-MMS-orange?style=for-the-badge)
![Simulator Wokwi](https://img.shields.io/badge/Simulator-Wokwi-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Integrated-success?style=for-the-badge)

# 🐭🤖 Projeto Integrado MicroMouse: Simulação & Hardware

Bem-vindo ao repositório oficial da nossa solução para o desafio MicroMouse! Este projeto foi desenvolvido como atividade avaliativa da disciplina de Fundamentos de Programação da UPE e adota uma abordagem híbrida, unindo a validação lógica em ambiente virtual com a implementação física embarcada.

## 🗂️ Estrutura do Projeto

O repositório está organizado em dois módulos principais para facilitar a avaliação:

### 1. 🧠 Módulo de Inteligência (`/simulacao_logica_python`)
O "cérebro" do robô. Aqui validamos a lógica de navegação e mapeamento.
- **Linguagem:** Python 3.
- **Ambiente:** Simulador Mackorone MMS.
- **Algoritmo:** Flood Fill (Propagação de Ondas).

### 2. 🔌 Módulo Físico / Firmware (`/simulacao_fisica_wokwi`)
O "corpo" do robô. Implementação para hardware real utilizando ESP32.
- **Microcontrolador:** ESP32 (Wi-Fi/Bluetooth Ready).
- **Sensores:** Ultrassônicos HC-SR04 para leitura de distância.
- **Atuadores:** Controle de tração diferencial (Drivers Ponte H).
- **Ambiente:** Wokwi (Simulação de Eletrônica) / Arduino IDE.

---

## 📋 Funcionalidades Principais

### 🐁 Navegação Autônoma
- **Mapeamento Dinâmico:** O robô começa sem conhecer o labirinto e descobre paredes usando sensores (virtuais ou físicos) à medida que explora.
- **Flood Fill (BFS):** Implementação robusta do algoritmo de busca em largura. O robô preenche o mapa com "ondas" de distância a partir do objetivo (centro), garantindo matematicamente o caminho ótimo.
- **Anti-Loop:** Graças à matriz de distâncias, o robô nunca entra em ciclos infinitos, um problema comum em algoritmos simples.

### 📡 Hardware (ESP32)
- **Leitura Sensorial:** Processamento de sinais de múltiplos sensores ultrassônicos para detectar paredes à frente, esquerda e direita.
- **Abstração de Hardware:** Funções de controle de motor que traduzem a lógica "Vire à Esquerda" para comandos elétricos nos pinos do ESP32, análogas à API do simulador.

---

## 🚀 Como Rodar o Projeto

### 🖥️ Opção A: Simulação Lógica (MMS)
1. Instale o simulador [Mackorone MMS](https://github.com/mackorone/mms).
2. Configure um novo robô apontando para a pasta `simulacao_logica_python`.
3. Use o comando de execução: `python main.py`.
4. Clique em **Run** e veja o algoritmo pintar o mapa!

### ⚡ Opção B: Simulação Física (Wokwi / ESP32)
1. Acesse o site [Wokwi.com](https://wokwi.com).
2. Carregue os arquivos da pasta `simulacao_fisica_wokwi` (incluindo `sketch.ino` e `diagram.json`).
3. Inicie a simulação para ver o comportamento elétrico, conexões e lógica de sensores em tempo real.
4. *Alternativamente: Carregue o código em um ESP32 físico via Arduino IDE.*

---

## 📊 Por que Flood Fill? (Comparativo Teórico)
Optamos por implementar o **Flood Fill** em vez do clássico *Wall Follower* (Seguidor de Parede/Mão Esquerda). 

Conforme estudado no material da disciplina:
> "O método Wall Follower possui eficiência limitada e falha em labirintos complexos que contêm ilhas ou loops, podendo nunca encontrar o destino."

Já o Flood Fill utiliza uma matriz de custos para garantir a convergência para o centro, explorando todas as rotas possíveis matematicamente e encontrando o caminho mais curto.

---

## 👨‍💻 Autores
<div align="center">
  
**Kauan Victor** • **João Lucas** • **Elbert Melo**
**Vicente Souza** • **Caio Magalhães** • **Enzo Esmeraldo**
</div>

<div align="center">

---
**⚠️ Nota sobre o Histórico de Versão:
Para garantir a integridade da entrega final e a separação correta entre os módulos de Simulação (Python) e Firmware (C++), o repositório passou por uma **refatoração estrutural completa** no dia [04/12].
Durante esse processo de organização de pastas (`git mv` e reestruturação de diretórios), o histórico de commits anterior foi unificado para manter a árvore do projeto limpa. Todos os membros da equipe participaram ativamente do desenvolvimento das etapas anteriores à esta organização, e continuaram o desenvolvimento do projeto ate sua ultima alteração.**
</div>

---
*Projeto desenvolvido na Universidade de Pernambuco (UPE) - 2024/2025.*
