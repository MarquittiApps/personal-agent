import React from 'react'

const modules = [
  { name: 'Command Center', path: '/' },
  { name: 'Smart Home', path: '/smart-home' },
  { name: 'Software Dev', path: '/software-dev' },
  { name: 'Operations', path: '/operations' },
]

export const Sidebar: React.FC = () => {
  return (
    <nav className="sidebar" role="navigation">
      <h2 className="sidebar-title">Personal AI Core</h2>
      <ul className="sidebar-list">
        {modules.map((module) => (
          <li key={module.name} className="sidebar-item">
            <a href={module.path} className="sidebar-link">
              {module.name}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  )
}
