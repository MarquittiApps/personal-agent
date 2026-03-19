import { useEffect, useCallback, useRef } from 'react';
import { useChatStore } from '../store/useChatStore';
import { usePlanningStore } from '../store/usePlanningStore';

const WS_URL = 'ws://localhost:8000/ws/chat';

export const useSocket = () => {
  const socketRef = useRef<WebSocket | null>(null);
  const { addMessage, updateStreamingMessage, finalizeStreamingMessage, setAgentStatus } = useChatStore();
  const streamingIdRef = useRef<string | null>(null);

  const connect = useCallback(() => {
    if (
      socketRef.current?.readyState === WebSocket.OPEN ||
      socketRef.current?.readyState === WebSocket.CONNECTING
    ) {
      return;
    }

    const socket = new WebSocket(WS_URL);
    socketRef.current = socket;

    socket.onopen = () => {
      console.log('WebSocket Connected');
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);

      switch (data.type) {
        case 'token':
          if (!streamingIdRef.current) {
            streamingIdRef.current = addMessage('assistant', '');
          }
          updateStreamingMessage(streamingIdRef.current, data.content);
          break;

        case 'status':
          setAgentStatus(data.content);
          break;
          
        case 'DASHBOARD_UPDATE':
          console.log('[DASHBOARD_UPDATE] payload recebido:', JSON.stringify(data, null, 2));
          console.log('[DASHBOARD_UPDATE] data.data:', data.data);
          if (data.data) {
            usePlanningStore.getState().syncPlanning(data.data);
            console.log('[DASHBOARD_UPDATE] store após sync:', usePlanningStore.getState());
          }
          addMessage('assistant', '\n\n✅ *Dashboard de planejamento atualizado com sucesso.*');
          break;

        case 'end':
          setAgentStatus(null);
          if (streamingIdRef.current) {
            finalizeStreamingMessage(streamingIdRef.current);
            streamingIdRef.current = null;
          }
          break;

        case 'error':
          setAgentStatus(null);
          console.error('WebSocket Error:', data.content);
          addMessage('assistant', `Erro: ${data.content}`);
          streamingIdRef.current = null;
          break;
      }
    };

    socket.onclose = () => {
      console.log('WebSocket Disconnected');
      if (socketRef.current === socket) {
        socketRef.current = null;
      }
    };

    socket.onerror = (error) => {
      console.error('WebSocket Socket Error:', error);
    };
  }, [addMessage, updateStreamingMessage, finalizeStreamingMessage]);

  const sendMessage = useCallback((text: string) => {
    if (socketRef.current?.readyState === WebSocket.OPEN) {
      addMessage('user', text);
      socketRef.current.send(JSON.stringify({ text }));
    } else {
      console.error('WebSocket is not connected');
      // Tenta reconectar
      connect();
    }
  }, [connect, addMessage]);

  useEffect(() => {
    connect();
    return () => {
      socketRef.current?.close();
    };
  }, [connect]);

  return { sendMessage, isConnected: socketRef.current?.readyState === WebSocket.OPEN };
};
