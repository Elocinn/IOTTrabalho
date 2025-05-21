import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
port = 1883

topicos = [
    "Casa/Sala",
    "Casa/Cozinha",
    "Casa/Quarto",
    "Casa/Banheiro",
    "Casa/Corredor",
    "Casa/Garagem",
    "Casa/PortaGaragem"
]

estado_dispositivos = {
    "Sala": False,
    "Cozinha": False,
    "Quarto": False,
    "Banheiro": False,
    "Corredor": False,
    "Garagem": False,
    "PortaGaragem": "Fechada"
}


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado com sucesso ao broker MQTT")
    else:
        print("❌ Falha na conexão. Código:", rc)

    for topico in topicos:
        client.subscribe(topico)
        print(f"Inscrito no tópico: {topico}")


def on_message(client, userdata, msg):
    mensagem = msg.payload.decode()
    topico = msg.topic
    print(f"\nMensagem recebida | Tópico: {topico} | Conteúdo: {mensagem}")

    if topico == "Casa/PortaGaragem":
        controla_porta_garagem(mensagem)
    else:
        controla_led(topico, mensagem)

    mostrar_estado()


def controla_led(topico, mensagem):
    comodo = topico.split("/")[-1]  
    if mensagem.lower() == "ligar":
        estado_dispositivos[comodo] = True
        print(f"💡 {comodo}: Ligado")
    elif mensagem.lower() == "desligar":
        estado_dispositivos[comodo] = False
        print(f"💡 {comodo}: Desligado")
    else:
        print(f"⚠️ Comando inválido para {comodo}: {mensagem}")


def controla_porta_garagem(mensagem):
    if mensagem.lower() == "abrir":
        estado_dispositivos["PortaGaragem"] = "Aberta"
        print("🚪 Porta da Garagem: Aberta")
    elif mensagem.lower() == "fechar":
        estado_dispositivos["PortaGaragem"] = "Fechada"
        print("🚪 Porta da Garagem: Fechada")
    else:
        print(f"⚠️ Comando inválido para PortaGaragem: {mensagem}")


def mostrar_estado():
    print("\nEstado Atual da Casa:")
    for dispositivo, estado in estado_dispositivos.items():
        print(f" - {dispositivo}: {estado}")
    print("-" * 40)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("🔗 Conectando ao broker MQTT...")
client.connect(broker, port)

client.loop_forever()
