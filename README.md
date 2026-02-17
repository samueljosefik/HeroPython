# HeroPython 🛡️

**HeroPython** é um protótipo de jogo do gênero **Aventura Point-and-Click** criado como parte de um teste técnico para tutores de Python. 
O projeto foca em código limpo, organização em classes e fidelidade aos requisitos de animação e lógica.

## 🛠️ Tecnologias e Regras
- **Linguagem:** Python 3.12
- **Biblioteca Principal:** [Pygame Zero (PgZero)](https://pygame-zero.readthedocs.io)
- **Módulos Adicionais:** `math`, `random` e `pygame.Rect`.
- **Conformidade:** Totalmente aderente ao **PEP 8**.

## 🎮 Funcionalidades
- **Movimentação:** Sistema de clique-e-siga com cálculo de ângulo via `math`.
- **Animação:** Classes customizadas para troca de frames (Idle e Walk) tanto para o herói quanto para os inimigos.
- **Inimigos:** Três tipos de inimigos com inteligência de patrulha territorial e detecção de colisão precisa.
- **Menu:** Interface interativa com controle de áudio (On/Off) e reinicialização lógica.
- **Dinamismo:** O objetivo final (Troféu) surge em localizações aleatórias a cada partida.

## 📦 Como Instalar
1. Clone o repositório ou baixe os arquivos.
2. Certifique-se de ter o [Python](https://www.python.org) instalado.
3. Instale o PgZero via terminal:
   ```bash
   pip install pgzero
