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
Home Page - Main video generation interface
Sidebar layout with System Config + FAQ.
Premium redesign with taste-skill principles.
DESIGN_VARIANCE: 5 | MOTION_INTENSITY: 3 | VISUAL_DENSITY: 4
"""

import sys
from pathlib import Path

# Add project root to sys.path
_script_dir = Path(__file__).resolve().parent
_project_root = _script_dir.parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

import streamlit as st

# Import state management
from web.state.session import init_session_state, init_i18n, get_pixelle_video

# Import components
from web.components.header import render_header
from web.components.settings import render_advanced_settings
from web.utils.streamlit_helpers import safe_rerun

# Page config
st.set_page_config(
    page_title="Pixelle-Video - AI Video Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)


def render_sidebar():
    """Render sidebar as admin navigation menu"""
    with st.sidebar:
        # Sidebar header
        st.markdown(
            """
            <div style="display:flex;align-items:center;gap:0.5rem;padding:0.5rem 0 1rem 0;border-bottom:1px solid var(--border-subtle, #1E293B);margin-bottom:0.75rem;">
                <div style="background:linear-gradient(135deg, #6366F1, #818CF8);width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.85rem;color:white;flex-shrink:0;">P</div>
                <div>
                    <div style="font-weight:600;font-size:0.9rem;color:#E2E8F0;">Pixelle-Video</div>
                    <div style="font-size:0.65rem;color:#64748B;letter-spacing:0.03em;">AI Video Generator</div>
                </div>
                <span style="margin-left:auto;font-size:0.6rem;color:#64748B;background:#141820;padding:0.1rem 0.4rem;border-radius:4px;border:1px solid #1E293B;">v0.2.0</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Nav label
        st.markdown(
            '<div style="font-size:0.65rem;font-weight:600;color:#64748B;text-transform:uppercase;letter-spacing:0.05em;padding:0.25rem 0.5rem;margin-bottom:0.25rem;">Navigation</div>',
            unsafe_allow_html=True
        )
        
        # Current active page
        current = st.session_state.get("admin_page", "dashboard")
        
        # Dashboard nav button
        is_dashboard = current == "dashboard"
        if st.button(
            "Dashboard",
            key="nav_dashboard",
            use_container_width=True,
            type="primary" if is_dashboard else "secondary",
            help="Video generation pipelines"
        ):
            st.session_state.admin_page = "dashboard"
            safe_rerun()
        
        # System Config nav button
        is_settings = current == "settings"
        if st.button(
            "System Config",
            key="nav_settings",
            use_container_width=True,
            type="primary" if is_settings else "secondary",
            help="Configure LLM, ComfyUI, API providers"
        ):
            st.session_state.admin_page = "settings"
            safe_rerun()


def main():
    """Main UI entry point - admin dashboard style"""
    # Initialize session state and i18n
    init_session_state()
    init_i18n()
    if "admin_page" not in st.session_state:
        st.session_state.admin_page = "dashboard"
    
    # Render sidebar navigation
    render_sidebar()
    
    # Main content area
    render_header()
    
    # Determine current page
    current_page = st.session_state.admin_page
    
    # ========================================================================
    # Page: System Configuration
    # ========================================================================
    if current_page == "settings":
        st.markdown(
            """
            <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:1rem;">
                <h3 style="margin:0;font-weight:600;font-size:1.15rem;color:#E2E8F0;">System Configuration</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        render_advanced_settings()
        return
    
    # ========================================================================
    # Page: Dashboard (default) - Pipeline Selection & Delegation
    # ========================================================================
    # Initialize Pixelle-Video
    pixelle_video = get_pixelle_video()
    
    from web.pipelines import get_all_pipeline_uis
    
    # Get all registered pipelines
    pipelines = get_all_pipeline_uis()
    
    # Use Tabs for pipeline selection
    tab_labels = [f"{p.icon} {p.display_name}" for p in pipelines]
    tabs = st.tabs(tab_labels)
    
    # Render each pipeline in its corresponding tab
    for i, pipeline in enumerate(pipelines):
        with tabs[i]:
            # Show description if available
            if pipeline.description:
                st.caption(pipeline.description)
            
            # Delegate rendering
            pipeline.render(pixelle_video)


if __name__ == "__main__":
    main()

