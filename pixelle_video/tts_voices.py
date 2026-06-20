# Copyright (C) 2025 AIDC-AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
TTS Voice Configuration

Defines available voices for local Edge TTS inference.
"""

from typing import List, Dict, Any


# Edge TTS voice presets for local inference
# Only keep English and Vietnamese voices
EDGE_TTS_VOICES: List[Dict[str, Any]] = [
    # English voices
    {
        "id": "en-US-AriaNeural",
        "label_key": "tts.voice.en_US_AriaNeural",
        "locale": "en-US",
        "gender": "female"
    },
    {
        "id": "en-US-JennyNeural",
        "label_key": "tts.voice.en_US_JennyNeural",
        "locale": "en-US",
        "gender": "female"
    },
    {
        "id": "en-US-GuyNeural",
        "label_key": "tts.voice.en_US_GuyNeural",
        "locale": "en-US",
        "gender": "male"
    },
    {
        "id": "en-US-DavisNeural",
        "label_key": "tts.voice.en_US_DavisNeural",
        "locale": "en-US",
        "gender": "male"
    },
    {
        "id": "en-GB-SoniaNeural",
        "label_key": "tts.voice.en_GB_SoniaNeural",
        "locale": "en-GB",
        "gender": "female"
    },
    {
        "id": "en-GB-RyanNeural",
        "label_key": "tts.voice.en_GB_RyanNeural",
        "locale": "en-GB",
        "gender": "male"
    },

    # Vietnamese voices
    {
        "id": "vi-VN-HoaiMyNeural",
        "label_key": "tts.voice.vi-VN-HoaiMyNeural",
        "locale": "vi-VN",
        "gender": "female"
    },
    {
        "id": "vi-VN-NamMinhNeural",
        "label_key": "tts.voice.vi-VN-NamMinhNeural",
        "locale": "vi-VN",
        "gender": "male"
    },
]


def get_voice_display_name(voice_id: str, tr_func=None, locale: str = "zh_CN") -> str:
    """
    Get display name for voice
    
    Args:
        voice_id: Voice ID (e.g., "zh-CN-YunjianNeural")
        tr_func: Translation function (optional)
        locale: Current locale (default: "zh_CN")
    
    Returns:
        Display name (translated label if in Chinese, otherwise voice ID)
    """
    # Find voice config
    voice_config = next((v for v in EDGE_TTS_VOICES if v["id"] == voice_id), None)
    
    if not voice_config:
        return voice_id
    
    # If translation function available, use translated label
    if tr_func:
        label_key = voice_config["label_key"]
        return tr_func(label_key)
    
    # Fallback: return voice ID
    return voice_id


def speed_to_rate(speed: float) -> str:
    """
    Convert speed multiplier to Edge TTS rate parameter
    
    Args:
        speed: Speed multiplier (1.0 = normal, 1.2 = 120%)
    
    Returns:
        Rate string (e.g., "+20%", "-10%")
    
    Examples:
        1.0 → "+0%"
        1.2 → "+20%"
        0.8 → "-20%"
    """
    percentage = int((speed - 1.0) * 100)
    sign = "+" if percentage >= 0 else ""
    return f"{sign}{percentage}%"

