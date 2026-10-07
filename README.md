# 🚦 Trânsito Inteligente · Indaiatuba

Ecossistema de IoT e Inteligência Artificial para previsibilidade de trânsito, prevenção de acidentes e segurança viária no município de Indaiatuba (SP).

---

## 💡 Sobre o projeto

Sensores instalados nas vias coletam **velocidade**, **distância** e **taxa de desaceleração** em tempo real, permitindo identificar zonas de risco antes que acidentes aconteçam. A visão de longo prazo é integrar esses dados ao **COI** (Centro de Operações Integradas) da cidade, somando visão computacional para embasar decisões de sinalização, fiscalização e engenharia viária.

## 🧰 Stack

| Camada | Tecnologia |
|---|---|
| Hardware | ESP32 + sensor ultrassônico (HC-SR04) + infravermelho (IR-Speed-02) |
| Backend | Python 3.10+ (FastAPI + Server-Sent Events) |
| Processamento | Algoritmo de filtragem de ruído e cálculo do Índice de Risco de Colisão |
| Dashboard | HTML5 + CSS3 + JavaScript (Single File / Live Data via SSE) |
| Gráficos | Chart.js |
| Hospedagem | Render.com (Web Service Gratuito) |

## 🚀 Como executar localmente

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt