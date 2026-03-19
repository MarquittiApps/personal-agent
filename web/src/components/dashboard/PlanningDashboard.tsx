import React from 'react';

export const PlanningDashboard: React.FC = () => {
  return (
    <div className="w-full h-full flex flex-col md:flex-row gap-4 p-4 text-white">
      {/* Daily Layer */}
      <div className="flex-1 bg-black/40 backdrop-blur-md rounded-xl p-4 border border-white/10">
        <h2 className="text-xl font-semibold mb-4 text-emerald-400">Planejamento Diário</h2>
        <div className="flex flex-col gap-2">
          <div className="p-2 bg-white/5 rounded-md text-sm">Mock Daily Task</div>
        </div>
      </div>

      {/* Weekly Layer */}
      <div className="flex-1 bg-black/40 backdrop-blur-md rounded-xl p-4 border border-white/10">
        <h2 className="text-xl font-semibold mb-4 text-blue-400">Planejamento Semanal</h2>
        <div className="flex flex-col gap-2">
          <div className="p-2 bg-white/5 rounded-md text-sm">Mock Weekly Goal</div>
        </div>
      </div>

      {/* Monthly Layer */}
      <div className="flex-1 bg-black/40 backdrop-blur-md rounded-xl p-4 border border-white/10">
        <h2 className="text-xl font-semibold mb-4 text-purple-400">Planejamento Mensal</h2>
        <div className="flex flex-col gap-2">
          <div className="p-2 bg-white/5 rounded-md text-sm">Mock Monthly Milestone</div>
        </div>
      </div>
    </div>
  );
};
