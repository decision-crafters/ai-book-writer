from typing import Optional, Dict, Any
import os
from .litellm_base import LiteLLMBase
from .deepseek_client import DeepSeekClient

class OpenAIImplementation(LiteLLMBase):
    """Implementation for OpenAI models"""
    
    def __init__(self, model: str, api_key: str, organization: Optional[str] = None, **kwargs):
        super().__init__(
            model=f"openai/{model}",
            api_key=api_key,
            organization=organization,
            **kwargs
        )

class DeepSeekImplementation(LiteLLMBase):
    """Implementation for DeepSeek models"""
    
    def __init__(self, config: Dict, **kwargs):
        """Initialize with configuration"""
        super().__init__(
            model="deepseek-chat",
            api_key=config.get("api_key"),
            base_url=config.get("base_url", "https://api.deepseek.com"),
            **kwargs
        )
        self.client = DeepSeekClient(config)
        
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using DeepSeek model"""
        response = self.client.generate(
            prompt=prompt,
            **kwargs
        )
        return response
        
    def generate_chat_completion(
        self,
        messages: list,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Generate chat completion using DeepSeek model"""
        response = self.client.chat_completion(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        return response

class GeminiImplementation(LiteLLMBase):
    """Implementation for Google Gemini models"""
    
    def __init__(self, model: str, api_key: str, organization: Optional[str] = None, **kwargs):
        super().__init__(
            model=f"gemini/{model}",
            api_key=api_key,
            organization=organization,
            **kwargs
        )

class GroqImplementation(LiteLLMBase):
    """Implementation for Groq models"""
    
    def __init__(self, model: str, api_key: str, organization: Optional[str] = None, **kwargs):
        super().__init__(
            model=f"groq/{model}",
            api_key=api_key,
            organization=organization,
            **kwargs
        )

class O1PreviewImplementation(LiteLLMBase):
    """Implementation for O1-Preview models"""
    
    def __init__(self, model: str, api_key: str, organization: Optional[str] = None, **kwargs):
        super().__init__(
            model=f"o1/{model}",
            api_key=api_key,
            base_url="https://api.o1.ai/v1",
            **kwargs
        )

class GeminiFlashImplementation(LiteLLMBase):
    """Implementation for Gemini 2.0 Flash Experimental models"""
    
    def __init__(self, model: str, api_key: str, organization: Optional[str] = None, **kwargs):
        super().__init__(
            model=f"gemini-flash/{model}",
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta",
            **kwargs
        )
