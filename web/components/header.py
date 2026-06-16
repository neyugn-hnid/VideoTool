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
Pixelle-Video Premium Header
Redesigned with taste-skill: clean, minimal, premium-dark tool UI.
DESIGN_VARIANCE: 5 | MOTION_INTENSITY: 3 | VISUAL_DENSITY: 4
"""

import streamlit as st

from web.i18n import tr, get_available_languages, set_language
from web.utils.streamlit_helpers import safe_rerun
from web.components.premium_styles import inject_custom_css


def render_header():
    """Render premium page header with title, version badge, and language selector"""
    # Inject custom CSS once per session
    if "css_injected" not in st.session_state:
        inject_custom_css()
        st.session_state.css_injected = True
    
    # Premium header layout
    st.markdown(
        f"""
        <div class="pixelle-header">
            <div style="display:flex;align-items:center;gap:0.75rem;">
                <h3>{tr('app.title')}</h3>
                <span class="header-badge">v0.2.0</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Language selector (inline, compact)
    _render_language_selector()


def _render_language_selector():
    """Render compact inline language selector"""
    languages = get_available_languages()
    lang_options = [f"{code} - {name}" for code, name in languages.items()]
    
    current_lang = st.session_state.get("language", "zh_CN")
    current_index = list(languages.keys()).index(current_lang) if current_lang in languages else 0
    
    selected = st.selectbox(
        tr("language.select"),
        options=lang_options,
        index=current_index,
        label_visibility="collapsed",
        key="lang_selector_header"
    )
    
    selected_code = selected.split(" - ")[0]
    if selected_code != current_lang:
        st.session_state.language = selected_code
        set_language(selected_code)
        safe_rerun()

