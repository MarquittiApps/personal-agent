import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';

interface Product {
  id?: number;
  name: string;
  brand: string;
  protocol: string;
}

export const HardwareCatalog: React.FC = () => {
  const { t } = useTranslation();
  const [products] = useState<Product[]>([
    { id: 1, name: 'Smart Bulb RGB', brand: 'HueLike', protocol: 'Zigbee' },
    { id: 2, name: 'Motion Sensor', brand: 'SafeHome', protocol: 'Z-Wave' },
  ]);

  return (
    <div className="card mt-8">
      <h3>{t('dashboard.iotCatalog')}</h3>
      <div className="overflow-x-auto mt-4">
        <table className="w-full text-left text-sm">
          <thead>
            <tr className="border-b border-white/10 text-white/60">
              <th className="pb-2 font-medium">{t('dashboard.name')}</th>
              <th className="pb-2 font-medium">{t('dashboard.brand')}</th>
              <th className="pb-2 font-medium">{t('dashboard.protocol')}</th>
              <th className="pb-2 font-medium">{t('dashboard.actions')}</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {products.map((p) => (
              <tr key={p.id} className="hover:bg-white/5 transition-colors">
                <td className="py-3 font-medium">{p.name}</td>
                <td className="py-3 text-white/70">{p.brand}</td>
                <td className="py-3">
                  <span className="px-2 py-0.5 bg-blue-500/20 text-blue-400 rounded-full text-[10px] uppercase font-bold border border-blue-500/30">
                    {p.protocol}
                  </span>
                </td>
                <td className="py-3">
                  <button className="text-emerald-400 hover:text-emerald-300 text-xs font-bold uppercase tracking-wider">{t('dashboard.edit')}</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className="mt-6 w-full py-2 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-sm font-bold transition-all">
        {t('dashboard.addNewDevice')}
      </button>
    </div>
  );
};
