/**
 * API client per comunicazione con backend FastAPI
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = "ApiError";
  }
}

/**
 * Fetcher base per chiamate API
 */
export async function fetcher<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`;
  
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
  });

  if (!response.ok) {
    throw new ApiError(
      response.status,
      `API error: ${response.status} ${response.statusText}`
    );
  }

  return response.json();
}

/**
 * Genera contenuto AI tramite backend
 */
export async function generateContent(prompt: string, socialTarget: string = "linkedin") {
  return fetcher<{ generated_text: string; timestamp: string }>("/generate", {
    method: "POST",
    body: JSON.stringify({
      prompt,
      social_target: socialTarget,
    }),
  });
}

// TODO: Thomas/Patrick - Aggiungere funzioni per CRUD post, calendario, analytics
