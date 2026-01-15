# Multi-Provider LLM Integration Lab

Este repositório contém implementações técnicas para integração com Large Language Models (LLMs) utilizando o **Google Gemini SDK** e a **API do OpenRouter**. O foco deste projeto é demonstrar o gerenciamento manual de contexto e a persistência de cadeias de raciocínio (*Chain-of-Thought*).

## 🛠️ Arquitetura e Implementação

O projeto explora duas abordagens distintas de comunicação com modelos de linguagem:

### 1. Google GenAI (Nativo)
Utiliza o modelo `gemini-2.5-flash` focado em conversação contínua.
- **Gerenciamento de Estado:** O código alterna IDs de interação (`previous_interaction_id`) para garantir que o histórico da conversa seja mantido sem a necessidade de reenviar todo o histórico de mensagens manualmente.
- **Configuração de Inferência:** - `thinking_level: "high"`: Habilita o processamento analítico profundo.
  - `temperature: 0.65`: Configurado para equilibrar precisão técnica com fluidez na resposta.

### 2. OpenRouter (REST API)
Utiliza o modelo `xiaomi/mimo-v2-flash:free` para demonstrar a manipulação de metadados de raciocínio.
- **Reasoning Persistence:** Captura o campo `reasoning_details` da resposta da IA.
- **Loop de Validação:** O script injeta o raciocínio anterior de volta na próxima requisição, permitindo que o modelo realize autocrítica e valide suas próprias conclusões lógicas.

---

## 🚀 Como Configurar

1. **Instale as dependências:**
   ```bash
   pip install -U google-genai requests