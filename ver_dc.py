from telethon.sessions import StringSession

# Cole a sua string gerada aqui (coloquei um pedaço da sua como exemplo)
minha_session = '1AZWarzcBu2Rd29qSX4MCKOoAPsXkGU_R81XM2ThD4Xz-uGonr8uDnAypPUdpOb_24hY-F848S9hw8QfhaMBYXJO9pGnxCvPZ2DzqExtVUaTVWirCuxpxDflT6mz39MbFiIuFwcJdi_EEnQ4QIQV2ItQzZf_dfikmwsG_0hFETZ4aNgrZBolHqOh1CjuNBkKglq8ayLKA0psTXA-YPHVo_4DaUUsjaZ-0_nLOV18oAlosdsBpi2AiuT-VZqZ9Tsl4KaGxmuDUyd3hAawXUBw2vBW6ASUoByipml5Yv1qlnVeXqG9RqPTvIP0WQN4b0ZFBp-75iAYxQzdrywBH6irAnIgG8eYIu94='

# Pedimos para o Telethon abrir o pacote
sessao = StringSession(minha_session)

# Printamos os dados escondidos lá dentro!
print(f"🌍 Datacenter (DC): {sessao.dc_id}")
print(f"📡 Endereço IP do Servidor: {sessao.server_address}")
print(f"🚪 Porta de Conexão: {sessao.port}")