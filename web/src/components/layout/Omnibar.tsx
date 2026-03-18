import React, { useState } from 'react'
import type { KeyboardEvent } from 'react'

interface OmnibarProps {
  onSend: (message: string) => void
}

export const Omnibar: React.FC<OmnibarProps> = ({ onSend }) => {
  const [value, setValue] = useState('')

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && value.trim()) {
      onSend(value)
      setValue('')
    }
  }

  return (
    <div className="omnibar-container">
      <div className="omnibar">
        <span className="omnibar-prefix">/</span>
        <input
          type="text"
          className="omnibar-input"
          placeholder="Type a command or message..."
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          autoFocus
        />
        <div className="omnibar-hint">Press Enter to send</div>
      </div>
    </div>
  )
}
