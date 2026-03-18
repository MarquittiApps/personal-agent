import { MainLayout } from './components/layout/MainLayout'
import { Omnibar } from './components/layout/Omnibar'
import { SystemDashboard } from './components/dashboard/SystemDashboard'
import { useChatStore } from './store/useChatStore'
import { sendMessageToAI } from './lib/socket'

function App() {
  const { messages, addMessage, updateStreamingMessage, finalizeStreamingMessage } = useChatStore()

  const handleSend = (message: string) => {
    addMessage('user', message)
    
    // Start streaming assistant response
    const assistantMessageId = addMessage('assistant', '')
    
    sendMessageToAI(message, {
      onMessage: (content) => {
        updateStreamingMessage(assistantMessageId, content)
      },
      onDone: () => {
        finalizeStreamingMessage(assistantMessageId)
      }
    })
  }

  return (
    <MainLayout>
      <div className="dashboard">
        <header className="dashboard-header">
          <h1>Command Center</h1>
          <p className="subtitle">
            Welcome to the Personal AI Core. Select a module from the sidebar to get started.
          </p>
        </header>
        
        <SystemDashboard />

        <section className="chat-history mt-12 mb-8 flex-1">
          <h3 className="mb-4 text-slate-400 uppercase text-xs font-bold tracking-widest">Interaction Log</h3>
          <div className="space-y-4">
            {messages.length === 0 && (
              <p className="text-slate-400 italic text-sm">No recent interactions.</p>
            )}
            {messages.map((msg) => (
              <div key={msg.id} className={`message ${msg.role} ${msg.isStreaming ? 'streaming' : ''}`}>
                <div className="message-role">{msg.role === 'user' ? 'You' : 'AI'}</div>
                <div className="message-content">
                  {msg.content}
                  {msg.isStreaming && <span className="streaming-dot"></span>}
                </div>
              </div>
            ))}
          </div>
        </section>

        <Omnibar onSend={handleSend} />
      </div>
    </MainLayout>
  )
}

export default App
