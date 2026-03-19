import { create } from 'zustand';

export interface PlanningItem {
  id: string;
  title: string;
  status: 'pending' | 'in_progress' | 'completed';
}

export interface PlanningPayload {
  daily: PlanningItem[];
  weekly: PlanningItem[];
  monthly: PlanningItem[];
}

interface PlanningState extends PlanningPayload {
  syncPlanning: (payload: PlanningPayload) => void;
}

export const usePlanningStore = create<PlanningState>((set) => ({
  daily: [],
  weekly: [],
  monthly: [],
  syncPlanning: (payload) => set((state) => ({
    ...state,
    ...payload,
  })),
}));
