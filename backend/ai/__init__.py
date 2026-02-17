"""
AI Package - Gemini Integration
Issue #15, #12, #10, #16: Setup Gemini, generazione contenuti, prompts, immagini
"""

from .gemini_config import (
    get_gemini_config,
    GeminiConfig,
    test_gemini_connection
)
from .prompts import (
    SocialPlatform,
    ToneOfVoice,
    build_prompt,
    get_social_guidelines
)
from .generator import (
    ContentGenerator,
    get_content_generator
)

__all__ = [
    "get_gemini_config",
    "GeminiConfig",
    "test_gemini_connection",
    "SocialPlatform",
    "ToneOfVoice",
    "build_prompt",
    "get_social_guidelines",
    "ContentGenerator",
    "get_content_generator"
]
