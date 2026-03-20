import React, { useEffect, useState } from 'react';
import { Mail, HardDrive, Clock, ShieldCheck, AlertCircle } from 'lucide-react';

interface EmailMetrics {
  important_last_7_days: number;
  large_attachments_count: number;
  old_emails_count: number;
  last_updated: string;
  error?: string;
}

export const EmailDashboard: React.FC = () => {
  const [metrics, setMetrics] = useState<EmailMetrics | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await fetch('/api/v1/email/metrics');
        const data = await response.json();
        setMetrics(data);
      } catch (error) {
        console.error('Error fetching email metrics:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchMetrics();
    const interval = setInterval(fetchMetrics, 300000); // Update every 5 minutes
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div className="card animate-pulse">
        <div className="h-6 w-48 bg-gray-200 rounded mb-4"></div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[1, 2, 3].map((i) => (
            <div key={i} className="h-24 bg-gray-100 rounded-xl"></div>
          ))}
        </div>
      </div>
    );
  }

  if (metrics?.error) {
    return (
      <div className="card border-red-200 bg-red-50 flex items-center gap-3 text-red-600">
        <AlertCircle className="w-5 h-5" />
        <span>Erro ao carregar métricas de e-mail: {metrics.error}</span>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h3 className="flex items-center gap-2 m-0 text-lg">
            <Mail className="w-5 h-5 text-gray-600" />
            Gestão de E-mails
          </h3>
          <p className="text-gray-500 text-xs m-0 mt-1">Análise inteligente da sua caixa de entrada</p>
        </div>
        <div className="flex items-center gap-2 text-[10px] text-gray-500 bg-gray-100 px-2 py-1 rounded-full border border-gray-200">
          <ShieldCheck className="w-3 h-3 text-green-600" />
          MODO SOMENTE LEITURA
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        {/* Important Emails */}
        <div className="p-4 bg-gray-50 border border-gray-100 rounded-xl hover:bg-gray-100 transition-colors">
          <div className="flex items-center gap-2 text-gray-600 text-[10px] uppercase tracking-wider mb-2 font-bold">
            <Clock className="w-3 h-3" /> Recentes (7d)
          </div>
          <div className="text-3xl font-bold text-gray-900 leading-none mb-1">
            {metrics?.important_last_7_days || 0}
          </div>
          <div className="text-[10px] text-gray-500">E-mails importantes</div>
        </div>

        {/* Large Attachments */}
        <div className="p-4 bg-gray-50 border border-gray-100 rounded-xl hover:bg-gray-100 transition-colors">
          <div className="flex items-center gap-2 text-gray-600 text-[10px] uppercase tracking-wider mb-2 font-bold">
            <HardDrive className="w-3 h-3" /> Anexos Grandes
          </div>
          <div className="text-3xl font-bold text-gray-900 leading-none mb-1">
            {metrics?.large_attachments_count || 0}
          </div>
          <div className="text-[10px] text-gray-500">Acima de 10MB</div>
        </div>

        {/* Old Emails */}
        <div className="p-4 bg-gray-50 border border-gray-100 rounded-xl hover:bg-gray-100 transition-colors">
          <div className="flex items-center gap-2 text-gray-600 text-[10px] uppercase tracking-wider mb-2 font-bold">
            <Clock className="w-3 h-3" /> Legados (+2a)
          </div>
          <div className="text-3xl font-bold text-gray-900 leading-none mb-1">
            {metrics?.old_emails_count || 0}
          </div>
          <div className="text-[10px] text-gray-500">Sugestão: Arquivar</div>
        </div>
      </div>

      <div className="flex justify-between items-center text-[10px] text-gray-400 border-t border-gray-50 pt-4">
        <span>Última sincronização: {metrics ? new Date(metrics.last_updated).toLocaleString('pt-BR') : '-'}</span>
        <span className="italic">Processado via Gemini 2.0</span>
      </div>
    </div>
  );
};
