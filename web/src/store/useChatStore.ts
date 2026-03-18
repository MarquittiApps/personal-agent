import { create } from 'zustand'

interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: number
  isStreaming?: boolean
}

interface ChatState {
  messages: Message[]
  addMessage: (role: 'user' | 'assistant', content: string) => string
  updateStreamingMessage: (id: string, content: string) => void
  finalizeStreamingMessage: (id: string) => void
  clearHistory: () => void
}

export const useChatStore = create<ChatState>((set) => ({
  messages: [],
  addMessage: (role, content) => {
    const id = Math.random().toString(36).substring(7)
    set((state) => ({
      messages: [
        ...state.messages,
        {
          id,
          role,
          content,
          timestamp: Date.now(),
          isStreaming: role === 'assistant',
        },
      ],
    }))
    return id
  },
  updateStreamingMessage: (id, content) =>
    set((state) => ({
      messages: state.messages.map((msg) =>
        msg.id === id ? { ...msg, content: msg.content + content } : msg
      ),
    })),
  finalizeStreamingMessage: (id) =>
    set((state) => ({
      messages: state.messages.map((msg) =>
        msg.id === id ? { ...msg, isStreaming: false } : msg
      ),
    })),
  clearHistory: () => set({ messages: [] }),
}))
