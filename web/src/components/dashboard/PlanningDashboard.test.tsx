import { render, screen } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { PlanningDashboard } from './PlanningDashboard';

// Mock react-i18next
vi.mock('react-i18next', () => ({
  useTranslation: () => ({
    t: (key: string) => {
      const translations: Record<string, string> = {
        'dashboard.dailyPlanning': 'Daily Planning',
        'dashboard.weeklyPlanning': 'Weekly Planning',
        'dashboard.monthlyPlanning': 'Monthly Planning',
        'dashboard.planning': 'Planning Dashboard (3-Layer)',
        'dashboard.noItems': 'No items defined.',
      };
      return translations[key] || key;
    },
  }),
}));

describe('PlanningDashboard', () => {
  it('renders three main layers: Daily, Weekly, and Monthly', () => {
    render(<PlanningDashboard />);
    
    expect(screen.getByText(/Daily Planning/i)).toBeInTheDocument();
    expect(screen.getByText(/Weekly Planning/i)).toBeInTheDocument();
    expect(screen.getByText(/Monthly Planning/i)).toBeInTheDocument();
  });
});
