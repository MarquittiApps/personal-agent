import { render, screen } from '@testing-library/react'
import { MainLayout } from './MainLayout'
import { describe, it, expect } from 'vitest'

describe('MainLayout Component', () => {
  it('renders Sidebar and Main Content area', () => {
    render(
      <MainLayout>
        <div data-testid="test-content">Content</div>
      </MainLayout>
    )
    expect(screen.getByRole('navigation')).toBeInTheDocument()
    expect(screen.getByTestId('test-content')).toBeInTheDocument()
  })
})
