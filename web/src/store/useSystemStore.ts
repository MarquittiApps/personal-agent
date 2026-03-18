import { create } from 'zustand'

interface SystemStatus {
  status: 'online' | 'offline' | 'busy'
  memoryUsage: string
  cpuLoad: string
  lastUpdate: number
}

interface AgentHealth {
  name: string
  status: 'healthy' | 'warning' | 'error'
  message: string
}

interface SystemState {
  system: SystemStatus
  agents: AgentHealth[]
  updateSystem: (updates: Partial<SystemStatus>) => void
  setAgentHealth: (name: string, health: Partial<AgentHealth>) => void
}

export const useSystemStore = create<SystemState>((set) => ({
  system: {
    status: 'online',
    memoryUsage: '450MB',
    cpuLoad: '12%',
    lastUpdate: Date.now(),
  },
  agents: [
    { name: 'Meta-Agent', status: 'healthy', message: 'Ready' },
    { name: 'Software-Dev', status: 'healthy', message: 'Idle' },
    { name: 'Smart-Home', status: 'healthy', message: 'Monitoring' },
  ],
  updateSystem: (updates) =>
    set((state) => ({
      system: { ...state.system, ...updates, lastUpdate: Date.now() },
    })),
  setAgentHealth: (name, health) =>
    set((state) => ({
      agents: state.agents.map((agent) =>
        agent.name === name ? { ...agent, ...health } : agent
      ),
    })),
}))
