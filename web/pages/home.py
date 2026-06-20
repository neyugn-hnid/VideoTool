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
from web.i18n import tr
from web.utils.streamlit_helpers import safe_rerun

# Page config
st.set_page_config(
    page_title="D.AI",
    layout="wide",
    initial_sidebar_state="expanded",
)


def render_sidebar():
    """Sidebar hidden — navigation via gear icon in header"""
    pass


def main():
    """Main UI entry point - admin dashboard style"""
    # Initialize session state and i18n
    init_session_state()
    init_i18n()
    if "admin_page" not in st.session_state:
        st.session_state.admin_page = "dashboard"
    
    # Sidebar disabled — navigation via header gear icon
    render_sidebar()
    
    # Main content area
    render_header()
    
    # Determine current page
    current_page = st.session_state.admin_page
    
    # ========================================================================
    # Page: System Configuration
    # ========================================================================
    if current_page == "settings":
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

