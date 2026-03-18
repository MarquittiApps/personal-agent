import { render, screen } from '@testing-library/react'
import { Sidebar } from './Sidebar'
import { describe, it, expect } from 'vitest'

describe('Sidebar Component', () => {
  it('renders the sidebar navigation', () => {
    render(<Sidebar />)
    expect(screen.getByRole('navigation')).toBeInTheDocument()
  })

  it('contains links to all core modules', () => {
    render(<Sidebar />)
    expect(screen.getByText(/Command Center/i)).toBeInTheDocument()
    expect(screen.getByText(/Smart Home/i)).toBeInTheDocument()
    expect(screen.getByText(/Software Dev/i)).toBeInTheDocument()
    expect(screen.getByText(/Operations/i)).toBeInTheDocument()
  })
})
