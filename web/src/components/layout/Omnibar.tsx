import React, { useState } from 'react'
import type { KeyboardEvent } from 'react'
import { useTranslation } from 'react-i18next'

interface OmnibarProps {
  onSend: (message: string) => void
}

export const Omnibar: React.FC<OmnibarProps> = ({ onSend }) => {
  const { t, i18n } = useTranslation()
  const [value, setValue] = useState('')

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && value.trim()) {
      onSend(value)
      setValue('')
    }
  }

  const toggleLanguage = () => {
    const langs = ['en', 'pt', 'es']
    const nextIndex = (langs.indexOf(i18n.language) + 1) % langs.length
    i18n.changeLanguage(langs[nextIndex])
  }

  return (
    <div className="omnibar-container">
      <div className="omnibar">
        <button
          onClick={toggleLanguage}
          className="px-2 py-1 mr-2 text-[10px] font-bold bg-white/5 border border-white/10 rounded hover:bg-white/10 transition-colors uppercase text-slate-400"
        >
          {i18n.language}
        </button>
        <span className="omnibar-prefix">/</span>
        <input
          type="text"
          className="omnibar-input"
          placeholder={t('common.welcome')}
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
