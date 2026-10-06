# 🚦 Trânsito Inteligente · Indaiatuba

Ecossistema de IoT e Inteligência Artificial para previsibilidade de trânsito, prevenção de acidentes e segurança viária no município de Indaiatuba (SP).

---

## 💡 Sobre o projeto

Sensores instalados nas vias coletam **velocidade**, **distância** e **taxa de desaceleração** em tempo real, permitindo identificar zonas de risco antes que acidentes aconteçam. A visão de longo prazo é integrar esses dados ao **COI** (Centro de Operações Integradas) da cidade, somando visão computacional para embasar decisões de sinalização, fiscalização e engenharia viária.

## 🧰 Stack

| Camada | Tecnologia |
|---|---|
| Hardware | ESP32 + sensor ultrassônico (distância HC-SR04) + infravermelho (velocidade IR-Speed-02) |
| Backend | Python 3.10+ (FastAPI + Server-Sent Events) |
| Processamento | Algoritmo de filtragem de ruído e cálculo do Índice de Risco de Colisão |
| Dashboard | HTML5 + CSS3 + JavaScript (Single File / Live Data) |
| Gráficos | Chart.js |
| Integração futura | COI — visão computacional / ANPR |

## 📊 Recursos da Dashboard

- **Índice de risco de colisão** calculado via Python em tempo real
- **Atualização contínua de fluxo e velocidade** sem recarregar a página
- **Feed ao vivo de frenagens bruscas** transmitido via SSE
- **Varredura de zonas críticas** por rua com indicativo de severidade
- **Recomendações preventivas** automatizadas para a gestão pública

## 🚀 Como executar o projeto

### 1. Iniciar o Backend em Python

Instale as dependências e inicie a API:

```bash
pip install fastapi uvicorn
python main.py