import asyncio
import websockets

async def test_ws():
    print("Conectando ao WS...")
    try:
        async with websockets.connect('ws://localhost:8000/ws/chat') as websocket:
            print("Conectado! Enviando mensagem...")
            await websocket.send('{"text": "teste interno"}')
            print("Mensagem enviada. Aguardando resposta...")
            while True:
                response = await websocket.recv()
                print(f"Recebido: {response}")
    except Exception as e:
        print(f"Erro ao conectar ou ler WS: {e}")

asyncio.run(test_ws())
