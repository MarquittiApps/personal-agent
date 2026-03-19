import { describe, it, expect, beforeEach } from 'vitest';
import { usePlanningStore } from './usePlanningStore';
import type { PlanningPayload } from './usePlanningStore';

describe('usePlanningStore', () => {
  beforeEach(() => {
    // Reset state before each test
    usePlanningStore.setState({
      daily: [],
      weekly: [],
      monthly: [],
    });
  });

  it('should initialize with empty arrays', () => {
    const state = usePlanningStore.getState();
    expect(state.daily).toEqual([]);
    expect(state.weekly).toEqual([]);
    expect(state.monthly).toEqual([]);
  });

  it('should update state via syncPlanning', () => {
    const payload: PlanningPayload = {
      daily: [{ id: '1', title: 'Daily Task', status: 'pending' }],
      weekly: [{ id: '2', title: 'Weekly Goal', status: 'pending' }],
      monthly: [{ id: '3', title: 'Monthly Milestone', status: 'pending' }],
    };

    usePlanningStore.getState().syncPlanning(payload);

    const state = usePlanningStore.getState();
    expect(state.daily).toHaveLength(1);
    expect(state.daily[0].title).toBe('Daily Task');
    expect(state.weekly).toHaveLength(1);
    expect(state.monthly).toHaveLength(1);
  });
});
