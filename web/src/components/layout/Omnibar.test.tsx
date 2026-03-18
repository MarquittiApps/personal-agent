import { render, screen, fireEvent } from '@testing-library/react'
import { Omnibar } from './Omnibar'
import { describe, it, expect, vi } from 'vitest'

describe('Omnibar Component', () => {
  it('renders the input field with placeholder', () => {
    render(<Omnibar onSend={() => {}} />)
    expect(screen.getByPlaceholderText(/Type a command or message/i)).toBeInTheDocument()
  })

  it('calls onSend when Enter is pressed', () => {
    const onSend = vi.fn()
    render(<Omnibar onSend={onSend} />)
    const input = screen.getByPlaceholderText(/Type a command or message/i)
    
    fireEvent.change(input, { target: { value: 'Hello AI' } })
    fireEvent.keyDown(input, { key: 'Enter', code: 'Enter' })
    
    expect(onSend).toHaveBeenCalledWith('Hello AI')
  })

  it('clears the input after sending', () => {
    render(<Omnibar onSend={() => {}} />)
    const input = screen.getByPlaceholderText(/Type a command or message/i) as HTMLInputElement
    
    fireEvent.change(input, { target: { value: 'Hello AI' } })
    fireEvent.keyDown(input, { key: 'Enter', code: 'Enter' })
    
    expect(input.value).toBe('')
  })
})
