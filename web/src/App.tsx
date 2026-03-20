import { MainLayout } from './components/layout/MainLayout'
import { Omnibar } from './components/layout/Omnibar'
import { SystemDashboard } from './components/dashboard/SystemDashboard'
import { PlanningDashboard } from './components/dashboard/PlanningDashboard'
import { DynamicRenderer } from './components/dynamic/DynamicRenderer'
import { HardwareCatalog } from './components/dashboard/HardwareCatalog'
import { KnowledgeUpload } from './components/dashboard/KnowledgeUpload'
import { ChatMessage } from './components/dashboard/ChatMessage'
import { useChatStore } from './store/useChatStore'
import { useSocket } from './lib/useSocket'
import { useEffect, useRef } from 'react'

function App() {
  const { messages, agentStatus } = useChatStore()
  const { sendMessage } = useSocket()
  const chatEndRef = useRef<HTMLDivElement>(null)

  const handleSend = (message: string) => {
    sendMessage(message)
  }

  // Auto-scroll to latest message
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, agentStatus])

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
        <PlanningDashboard />

        <div className="mb-8">
          <DynamicRenderer type="EmailDashboard" />
        </div>

        <div className="flex flex-col lg:flex-row gap-8">
          <div className="flex-1">
            <HardwareCatalog />
          </div>
          <div className="flex-1">
            <KnowledgeUpload />
          </div>
        </div>

        <section className="chat-history mt-12 mb-8 flex-1 overflow-y-auto max-h-[50vh]">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-slate-400 uppercase text-xs font-bold tracking-widest">Interaction Log</h3>
            {agentStatus && (
              <div className="agent-status-indicator text-xs text-blue-400 font-medium animate-pulse">
                ● {agentStatus}
              </div>
            )}
          </div>
          <div className="space-y-4">
            {messages.length === 0 && (
              <p className="text-slate-400 italic text-sm">No recent interactions.</p>
            )}
            {messages.map((msg) => (
              <ChatMessage 
                key={msg.id} 
                role={msg.role} 
                content={msg.content} 
                isStreaming={msg.isStreaming} 
              />
            ))}
            <div ref={chatEndRef} />
          </div>
        </section>

        <Omnibar onSend={handleSend} />
      </div>
    </MainLayout>
  )
}

export default App
