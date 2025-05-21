
# Simulador de Automação Residencial IoT via MQTT

Este projeto simula um sistema de automação residencial utilizando MQTT com Python. Ele permite controlar remotamente dispositivos como lâmpadas de cômodos e a porta da garagem, recebendo comandos via tópicos MQTT.

---

## Funcionalidades

* Controle de luz da Sala, Cozinha, Quarto, Banheiro, Corredor, Copa e Garagem.
* Controle da Porta da Garagem (Abrir/Fechar).
* Simulação local via terminal MQTT (`mosquitto_pub`).
* Monitoramento do estado atual de cada dispositivo.
* Integração com qualquer broker MQTT (público ou local).

---

## Tecnologias e Ferramentas

* **Python 3.10+**
* **MQTT** via [paho-mqtt](https://pypi.org/project/paho-mqtt/)

---

## Instalação

### Instale as dependências:

```bash
pip install paho-mqtt
```

### (Opcional) Instale o cliente MQTT Mosquitto:

* Acesse: [https://mosquitto.org/download/](https://mosquitto.org/download/)
* Adicione o executável (`mosquitto_pub.exe`) ao **PATH** ou rode diretamente da pasta.

---

### Executar o simulador:

```bash
python testeIOT.py
```

---

## Enviar comandos MQTT (exemplos)

### Acender a luz da Sala:

```bash
mosquitto_pub -h broker.emqx.io -t Casa/Sala -m "Ligar"
```

### Apagar a luz da Cozinha:

```bash
mosquitto_pub -h broker.emqx.io -t Casa/Cozinha -m "Desligar"
```

### Abrir Porta da Garagem:

```bash
mosquitto_pub -h broker.emqx.io -t Casa/PortaGaragem -m "Abrir"
```

### Fechar Porta da Garagem:

```bash
mosquitto_pub -h broker.emqx.io -t Casa/PortaGaragem -m "Fechar"
```

---

## Estado dos Dispositivos

Após cada comando, o terminal exibirá o estado atualizado de todos os cômodos e dispositivos, como:

```
Mensagem recebida | Tópico: Casa/Sala | Conteúdo: Ligar
💡 Sala: Ligado

Estado Atual da Casa:
 - Sala: True
 - Cozinha: False
 - Quarto: False
 - Banheiro: False
 - Corredor: False
 - Copa: False
 - Garagem: False
 - PortaGaragem: Fechada
----------------------------------------
```


