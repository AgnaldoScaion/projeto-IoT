# 🚦 Trânsito Inteligente · Indaiatuba

Ecossistema de IoT e Inteligência Artificial para previsibilidade de trânsito, prevenção de acidentes e segurança viária no município de Indaiatuba (SP).

> **Fase atual:** Beta — dashboard com dados simulados (mock), pronta para receber dados reais dos sensores.

---

## 💡 Sobre o projeto

Sensores instalados nas vias coletam **velocidade**, **distância** e **taxa de desaceleração** em tempo real, permitindo identificar zonas de risco antes que acidentes aconteçam. A visão de longo prazo é integrar esses dados ao **COI** (Centro de Operações Integradas) da cidade, somando visão computacional para embasar decisões de sinalização, fiscalização e engenharia viária.

## 🧰 Stack

| Camada | Tecnologia |
|---|---|
| Hardware | ESP32 + sensor ultrassônico (distância) + infravermelho (velocidade) |
| Dashboard | HTML + CSS + JavaScript (single file) |
| Gráficos | Chart.js |
| Dados | JSON estruturado (mock, embutido no próprio HTML) |
| Integração futura | COI — visão computacional / ANPR |

## 📊 O que a dashboard mostra

- **Índice de risco de colisão** (frenagem × distância), em tempo real
- **Mapa de zonas críticas** por rua, com histórico de freadas bruscas
- **Fluxo de veículos e velocidade média** ao longo do dia
- **Feed de eventos de frenagem** dos sensores
- **Recomendações preventivas** para a gestão pública (lombadas, sinalização, fiscalização)

## 🚀 Como usar

Basta abrir o arquivo `dashboard-transito-indaiatuba.html` em qualquer navegador — não precisa de servidor, build ou instalação.

```bash
open dashboard-transito-indaiatuba.html
```

Os dados mock usados na simulação ficam embutidos no próprio arquivo, dentro de uma tag `<script type="application/json" id="data-architecture">`, prontos para serem substituídos pela leitura real dos sensores ESP32.

## 🗺️ Próximos passos

- Substituir dados mock por leitura em tempo real via MQTT/HTTP dos ESP32
- Conectar ao COI para cruzamento com visão computacional
- Persistência histórica dos eventos para análise de tendências

---

<sub>Projeto desenvolvido para Indaiatuba, SP.</sub>