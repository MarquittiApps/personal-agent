import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { PlanningDashboard } from './PlanningDashboard';

describe('PlanningDashboard', () => {
  it('renders three main layers: Daily, Weekly, and Monthly', () => {
    render(<PlanningDashboard />);
    
    expect(screen.getByText(/Planejamento Diário/i)).toBeInTheDocument();
    expect(screen.getByText(/Planejamento Semanal/i)).toBeInTheDocument();
    expect(screen.getByText(/Planejamento Mensal/i)).toBeInTheDocument();
  });
});
