import { BarChart3, CalendarCheck, Send } from "lucide-react";

const features = [
  {
    title: "Pianifica",
    description: "Programma campagne e calendari editoriali in pochi passi.",
    icon: CalendarCheck
  },
  {
    title: "Analizza",
    description: "Monitora KPI e performance con dashboard sintetiche.",
    icon: BarChart3
  },
  {
    title: "Distribuisci",
    description: "Pubblica contenuti multi-canale con un singolo flusso.",
    icon: Send
  }
];

export default function Home() {
  return (
    <div className="min-h-screen">
      <main className="mx-auto max-w-6xl px-6 py-16">
        <section className="grid gap-12 lg:grid-cols-[1.05fr_0.95fr] lg:items-center">
          <div className="space-y-6">
            <p className="inline-flex items-center gap-2 rounded-full bg-amber-100 px-3 py-1 text-sm font-semibold text-amber-900">
              Social Manager Hub
            </p>
            <h1 className="text-4xl font-semibold leading-tight text-slate-900 sm:text-5xl">
              Controllo totale sui tuoi contenuti social, dalla pianificazione alla
              reportistica.
            </h1>
            <p className="text-lg text-slate-700">
              Gestisci team, approvazioni e pubblicazioni con un unico pannello chiaro e
              operativo. Integra workflow agili e tieni sotto controllo ogni canale.
            </p>
            <div className="flex flex-wrap gap-4">
              <button className="rounded-full bg-slate-900 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-amber-200">
                Avvia la demo
              </button>
              <button className="rounded-full border border-slate-300 px-6 py-3 text-sm font-semibold text-slate-700">
                Scopri i flussi
              </button>
            </div>
          </div>
          <div className="grid gap-4 sm:grid-cols-2">
            {features.map((feature) => {
              const Icon = feature.icon;
              return (
                <div
                  key={feature.title}
                  className="rounded-3xl border border-slate-200 bg-white/70 p-5 shadow-sm backdrop-blur"
                >
                  <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-amber-100 text-amber-700">
                    <Icon className="h-6 w-6" />
                  </div>
                  <h3 className="mt-4 text-xl font-semibold text-slate-900">
                    {feature.title}
                  </h3>
                  <p className="mt-2 text-sm text-slate-600">{feature.description}</p>
                </div>
              );
            })}
          </div>
        </section>

        <section className="mt-16 grid gap-6 rounded-3xl border border-slate-200 bg-white/70 p-8 shadow-sm backdrop-blur">
          <div className="flex flex-wrap items-center justify-between gap-6">
            <div>
              <h2 className="text-2xl font-semibold text-slate-900">Sprint operativo</h2>
              <p className="mt-2 text-sm text-slate-600">
                Imposta approvazioni, asset e calendario per partire in 24 ore.
              </p>
            </div>
            <div className="flex items-center gap-3">
              <span className="rounded-full bg-emerald-100 px-3 py-1 text-xs font-semibold text-emerald-800">
                Team online
              </span>
              <span className="rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold text-sky-800">
                Live analytics
              </span>
            </div>
          </div>
          <div className="grid gap-4 text-sm text-slate-700 sm:grid-cols-3">
            <div className="rounded-2xl bg-amber-50 px-4 py-3">
              Calendario condiviso con tag e reminder.
            </div>
            <div className="rounded-2xl bg-sky-50 px-4 py-3">
              Libreria asset con versioning rapido.
            </div>
            <div className="rounded-2xl bg-emerald-50 px-4 py-3">
              Report automatici su engagement e reach.
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
