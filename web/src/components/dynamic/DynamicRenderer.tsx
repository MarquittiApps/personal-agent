import React from 'react';
import { DynamicRegistry } from './DynamicRegistry';
import type { DynamicComponentType } from './DynamicRegistry';

interface DynamicRendererProps {
  type: string;
  props?: any;
}

export const DynamicRenderer: React.FC<DynamicRendererProps> = ({ type, props }) => {
  const Component = DynamicRegistry[type as DynamicComponentType];

  if (!Component) {
    console.warn(`Dynamic component of type "${type}" not found in registry.`);
    return (
      <div className="p-4 border border-dashed border-slate-700 rounded-lg bg-slate-900/50 text-slate-400 text-sm">
        Component <strong>{type}</strong> is still being developed or not registered.
      </div>
    );
  }

  return (
    <React.Suspense fallback={<div className="animate-pulse h-24 bg-slate-800 rounded-lg" />}>
      <Component {...props} />
    </React.Suspense>
  );
};
