# 🧮 Calculadora Interativa - Desafio de 1 Semana

Este projeto é o resultado de um desafio pessoal de desenvolver uma aplicação completa — desde a concepção da ideia até a programação do Front-end e Back-end — em apenas **uma semana**. A aplicação consiste em uma calculadora funcional com uma interface gráfica moderna e interações dinâmicas.
---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando um stack moderno e eficiente:

*   **[Python](https://www.python.org/):** Linguagem principal para a lógica de programação (Back-end).
*   **[PyQt6](https://www.riverbankcomputing.com/software/pyqt/):** Framework utilizado para a criação da interface gráfica (GUI).
*   **Qt Designer:** Ferramenta para o design visual da aplicação (arquivo `.ui`).
*   **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Utilizado para criar interações e alertas nativos do sistema.
*   **QtWebEngine:** Para integração de componentes web dentro da aplicação desktop.

---

## 🏗️ Estrutura do Projeto

A arquitetura do projeto segue uma separação clara entre interface e lógica:

*   **`Main.py`**: O "cérebro" da aplicação. Contém toda a lógica de cálculo, gerenciamento de estados e a inicialização da interface.
*   **`MAIN.ui`**: Arquivo XML que define toda a estrutura visual, botões e layout da calculadora, permitindo uma manutenção visual independente do código.
*   **Tratamento de Erros**: Implementação de lógica específica para casos críticos, como a divisão por zero, que conta com uma interação bem-humorada e educativa para o usuário.

---

## 💪 Pontos Fortes

*   **Interface Responsiva:** Design limpo e intuitivo que facilita o uso.
*   **Interatividade Avançada:** Uso de alertas dinâmicos e feedback visual imediato através do componente `QLCDNumber`.
*   **Código Modular:** Funções bem definidas para cada operação, facilitando a expansão futura.
*   **Experiência do Usuário (UX):** Mensagens personalizadas e navegação integrada para auxiliar o usuário em erros comuns.

---

## ⚙️ Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você precisará instalar as dependências do projeto:

```bash
pip install PyQt6 pyautogui PyQt6-WebEngine
```

### Execução

1.  Clone o repositório:
    ```bash
    git clone https://github.com/GustavoABA/Calculadora.git
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd Calculadora
    ```
3.  Execute a aplicação:
    ```bash
    python Main.py
    ```

---

## 🧠 Estruturas de Dados e Lógica

O projeto utiliza estruturas fundamentais de programação para garantir eficiência:
*   **Variáveis Globais de Estado:** Para controlar os números digitados e a operação selecionada.
*   **Match-Case (Python 3.10+):** Utilizado para uma seleção de operações mais limpa e moderna.
*   **Event-Driven Programming:** A aplicação responde a cliques de botões através de conexões de sinais e slots do PyQt6.

---

Desenvolvido com ☕ e 💻 por [Gustavo Azevedo Barrozo](https://github.com/GustavoABA).
