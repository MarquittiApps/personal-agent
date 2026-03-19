import React from 'react'
import { useSystemStore } from '../../store/useSystemStore'
import { useTranslation } from 'react-i18next'

export const SystemDashboard: React.FC = () => {
  const { t } = useTranslation()
  const { system, agents } = useSystemStore()

  return (
    <section className="dashboard-grid">
      <div className="card">
        <h3>{t('dashboard.systemOverview')}</h3>
        <div className="status-indicator mb-4">
          <span className={`dot dot-${system.status === 'online' ? 'green' : 'red'}`}></span>
          <span className="status-text">{system.status === 'online' ? t('dashboard.coreOnline') : t('dashboard.coreOffline')}</span>
        </div>
        <div className="metrics-list">
          <div className="metric-item">
            <span className="metric-label">{t('dashboard.cpuLoad')}:</span>
            <span className="metric-value">{system.cpuLoad}</span>
          </div>
          <div className="metric-item">
            <span className="metric-label">{t('dashboard.memory')}:</span>
            <span className="metric-value">{system.memoryUsage}</span>
          </div>
        </div>
      </div>

      <div className="card">
        <h3>{t('dashboard.agentHealth')}</h3>
        <div className="agents-list">
          {agents.map((agent) => (
            <div key={agent.name} className="agent-item">
              <div className="agent-info">
                <span className="agent-name">{agent.name}</span>
                <span className="agent-message">{t(`common.agentStatus.${agent.message.toLowerCase()}`, agent.message)}</span>
              </div>
              <span className={`status-pill status-${agent.status}`}>
                {agent.status}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
