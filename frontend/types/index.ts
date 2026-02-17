/**
 * Types condivisi - devono essere speculari agli schema Pydantic del backend
 */

export interface Post {
  id: string;
  testo: string;
  social_target: string;
  data_programmazione?: string;
  created_at: string;
  status: "draft" | "scheduled" | "published";
}

export interface PostCreate {
  testo: string;
  social_target: string;
  data_programmazione?: string;
}

export interface PostAnalytics {
  post_id: string;
  views: number;
  likes: number;
  comments: number;
  shares: number;
}

export interface GenerateRequest {
  prompt: string;
  social_target: string;
}

export interface GenerateResponse {
  generated_text: string;
  timestamp: string;
}

// TODO: Mohamed/Alessandro - Aggiungere types per Calendar, Dashboard
