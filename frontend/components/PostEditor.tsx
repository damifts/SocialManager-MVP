"use client";

import { useState } from "react";
import { Sparkles, Loader2 } from "lucide-react";
import { generateContent } from "@/lib/api";

/**
 * Componente editor per creazione post con assistenza AI
 */
export default function PostEditor() {
  const [prompt, setPrompt] = useState("");
  const [generatedText, setGeneratedText] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);

  const handleGenerate = async () => {
    if (!prompt.trim()) return;

    setIsGenerating(true);
    try {
      const response = await generateContent(prompt, "linkedin");
      setGeneratedText(response.generated_text);
    } catch (error) {
      console.error("Errore generazione:", error);
      alert("Errore durante la generazione. Verifica che il backend sia attivo.");
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="mx-auto max-w-2xl space-y-4">
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        <h2 className="mb-4 text-xl font-semibold text-slate-900">
          Editor Post AI-Assisted
        </h2>

        {/* TODO: Cristian Pola - Aggiungere selector social (LinkedIn, Twitter, etc.) */}
        
        <div className="space-y-4">
          <div>
            <label className="mb-2 block text-sm font-medium text-slate-700">
              Prompt per AI
            </label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Descrivi il contenuto che vuoi generare..."
              className="w-full rounded-lg border border-slate-300 px-4 py-3 text-slate-900 placeholder-slate-400 focus:border-amber-500 focus:outline-none focus:ring-2 focus:ring-amber-200"
              rows={3}
            />
          </div>

          <button
            onClick={handleGenerate}
            disabled={isGenerating || !prompt.trim()}
            className="flex items-center gap-2 rounded-full bg-slate-900 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-amber-200 hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isGenerating ? (
              <>
                <Loader2 className="h-4 w-4 animate-spin" />
                Generazione in corso...
              </>
            ) : (
              <>
                <Sparkles className="h-4 w-4" />
                Genera con AI
              </>
            )}
          </button>

          {generatedText && (
            <div className="rounded-lg bg-amber-50 p-4">
              <p className="text-sm font-medium text-amber-900 mb-2">Testo generato:</p>
              <p className="text-slate-700">{generatedText}</p>
            </div>
          )}
        </div>

        {/* TODO: Patrick - Aggiungere preview post formattato per social */}
        {/* TODO: Thomas - Integrare calendario per programmazione */}
      </div>
    </div>
  );
}
