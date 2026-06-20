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

from web.i18n import tr, set_language
from web.utils.streamlit_helpers import safe_rerun
from web.components.premium_styles import inject_custom_css


def render_header():
    """Render premium page header with title, version badge, and language toggle"""
    # Inject custom CSS once per session
    if "css_injected" not in st.session_state:
        inject_custom_css()
        st.session_state.css_injected = True
    
    # Inject CSS chỉ cho gear button, không ảnh hưởng nút khác
    st.markdown("""<style>
        .st-key-gear_btn button {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 4px !important;
            font-size: 20px !important;
            min-width: unset !important;
            min-height: unset !important;
        }
        .st-key-gear_btn button:hover {
            background: transparent !important;
            border: none !important;
        }
        /* Ẩn icon link heading */
        [data-testid="stHeaderActionElements"] {
            display: none !important;
        }
    </style>""", unsafe_allow_html=True)
    
    # Single row: title (left) | gear (right)
    cols = st.columns([9, 1])
    
    with cols[0]:
        st.markdown(
            f"""<div style="display:flex;align-items:center;gap:0.75rem;">
                <h3 style="margin:0;">{tr('app.title')}</h3>
            </div>""",
            unsafe_allow_html=True
        )
    
    with cols[1]:
        _render_settings_button()


def _render_settings_button():
    """Render a gear/settings icon button"""
    from web.utils.streamlit_helpers import safe_rerun
    
    is_settings = st.session_state.get("admin_page", "dashboard") == "settings"
    icon = "🏠" if is_settings else "⚙️"
    label = "Dashboard" if is_settings else "Cài đặt"
    
    if st.button(icon, key="gear_btn", help=label):
        st.session_state.admin_page = "settings" if not is_settings else "dashboard"
        safe_rerun()


def _render_lang_dropdown():
    """Language is fixed to Vietnamese"""
    pass

