import React from 'react';
import { usePlanningStore, PlanningItem } from '../../store/usePlanningStore';

const PlanningSection: React.FC<{ title: string; items: PlanningItem[]; colorClass: string }> = ({ title, items, colorClass }) => (
  <div className="flex-1 bg-black/40 backdrop-blur-md rounded-xl p-4 border border-white/10 min-w-[280px]">
    <h2 className={`text-xl font-semibold mb-4 ${colorClass}`}>{title}</h2>
    <div className="flex flex-col gap-2">
      {items.length === 0 ? (
        <p className="text-white/40 italic text-sm">Nenhum item definido.</p>
      ) : (
        items.map((item) => (
          <div key={item.id} className="p-3 bg-white/5 rounded-lg border border-white/5 flex items-center justify-between group hover:bg-white/10 transition-colors">
            <span className="text-sm font-medium">{item.title}</span>
            <div className={`w-2 h-2 rounded-full ${
              item.status === 'completed' ? 'bg-emerald-400' : 
              item.status === 'in_progress' ? 'bg-blue-400' : 'bg-slate-400'
            }`} title={item.status} />
          </div>
        ))
      )}
    </div>
  </div>
);

export const PlanningDashboard: React.FC = () => {
  const { daily, weekly, monthly } = usePlanningStore();

  return (
    <section className="mt-8 mb-8">
      <h3 className="text-slate-400 uppercase text-xs font-bold tracking-widest mb-4">Planning Dashboard (3-Layer)</h3>
      <div className="w-full flex flex-col md:flex-row gap-4">
        <PlanningSection title="Planejamento Diário" items={daily} colorClass="text-emerald-400" />
        <PlanningSection title="Planejamento Semanal" items={weekly} colorClass="text-blue-400" />
        <PlanningSection title="Planejamento Mensal" items={monthly} colorClass="text-purple-400" />
      </div>
    </section>
  );
};
