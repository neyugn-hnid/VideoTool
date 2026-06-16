"""
Pixelle-Video Premium UI Styles
Custom CSS injection for a polished, modern interface.
Applies taste-skill design principles: clean, minimal, premium dark.
"""

import streamlit as st


def inject_custom_css():
    """Inject global custom CSS for premium UI styling"""
    css = """
    <style>
    /* ===== ROOT VARIABLES ===== */
    :root {
        --accent: #6366F1;
        --accent-glow: rgba(99, 102, 241, 0.15);
        --bg-deep: #0B0E14;
        --bg-surface: #141820;
        --bg-elevated: #1A2235;
        --bg-hover: #1E293B;
        --border-subtle: #1E293B;
        --border-active: #2D3648;
        --text-primary: #E2E8F0;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --radius-sm: 6px;
        --radius-md: 10px;
        --radius-lg: 16px;
        --shadow-card: 0 1px 3px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
        --shadow-elevated: 0 4px 6px rgba(0,0,0,0.3), 0 10px 15px rgba(0,0,0,0.2);
    }

    /* ===== GLOBAL ===== */
    .stApp {
        background: var(--bg-deep);
    }

    /* ===== HEADER ===== */
    .pixelle-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 0;
        margin-bottom: 1rem;
        border-bottom: 1px solid var(--border-subtle);
    }
    .pixelle-header h3 {
        font-size: 1.35rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #E2E8F0 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .pixelle-header .header-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.7rem;
        font-weight: 500;
        color: var(--text-muted);
        background: var(--bg-surface);
        padding: 0.2rem 0.6rem;
        border-radius: var(--radius-sm);
        border: 1px solid var(--border-subtle);
        margin-left: 0.75rem;
        letter-spacing: 0.02em;
    }

    /* ===== SECTIONS / CARDS ===== */
    div[data-testid="stExpander"] {
        background: var(--bg-surface);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-card);
        margin-bottom: 0.75rem;
        overflow: hidden;
        transition: border-color 0.2s;
    }
    div[data-testid="stExpander"]:hover {
        border-color: var(--border-active);
    }
    div[data-testid="stExpander"] summary {
        padding: 0.75rem 1rem;
        font-weight: 600;
        font-size: 0.85rem;
        letter-spacing: 0.01em;
        color: var(--text-primary);
        background: transparent;
    }
    div[data-testid="stExpander"] summary p {
        font-size: 0.85rem;
        font-weight: 600;
    }

    /* ===== TABS ===== */
    div[data-testid="stTabs"] {
        margin-bottom: 1rem;
    }
    div[data-testid="stTabs"] button {
        font-size: 0.8rem;
        font-weight: 500;
        color: var(--text-secondary);
        padding: 0.4rem 1rem;
        border-radius: var(--radius-sm);
        transition: all 0.2s;
        gap: 0.35rem;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        color: var(--accent);
        background: var(--accent-glow);
        border-bottom: none;
    }
    div[data-testid="stTabs"] button:hover {
        color: var(--text-primary);
        background: var(--bg-hover);
    }

    /* ===== BUTTONS ===== */
    .stButton button {
        font-weight: 600;
        font-size: 0.85rem;
        border-radius: var(--radius-sm);
        border: none;
        padding: 0.4rem 1.2rem;
        transition: all 0.2s;
        letter-spacing: 0.01em;
    }
    .stButton button[kind="primary"],
    .stButton button[data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, var(--accent), #818CF8);
        color: white;
        box-shadow: 0 1px 3px var(--accent-glow);
    }
    .stButton button[kind="primary"]:hover,
    .stButton button[data-testid="baseButton-primary"]:hover {
        box-shadow: 0 4px 12px var(--accent-glow);
        transform: translateY(-1px);
    }
    .stButton button[kind="secondary"] {
        background: transparent;
        border: 1px solid var(--border-active);
        color: var(--text-secondary);
    }
    .stButton button[kind="secondary"]:hover {
        border-color: var(--accent);
        color: var(--accent);
        background: var(--accent-glow);
    }

    /* ===== GENERATE BUTTON (special) ===== */
    .generate-btn-container {
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid var(--border-subtle);
    }
    .generate-btn-container button {
        width: 100%;
        padding: 0.75rem !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em;
        background: linear-gradient(135deg, var(--accent), #4F46E5) !important;
        border-radius: var(--radius-md) !important;
        transition: all 0.25s !important;
    }
    .generate-btn-container button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px var(--accent-glow) !important;
    }

    /* ===== INPUTS ===== */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background: var(--bg-elevated) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
        font-size: 0.85rem;
        transition: border-color 0.2s;
    }
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px var(--accent-glow) !important;
    }

    /* ===== SLIDERS ===== */
    div[data-testid="stSlider"] div[data-baseweb="slider"] {
        margin: 0.5rem 0;
    }

    /* ===== RADIO / CHECKBOX ===== */
    div[data-testid="stRadio"] label,
    div[data-testid="stCheckbox"] label {
        font-size: 0.85rem;
        color: var(--text-secondary);
        gap: 0.4rem;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 0.25rem;
    }

    /* ===== METRICS / CAPTIONS ===== */
    .stCaption, div[data-testid="stCaption"] {
        color: var(--text-muted);
        font-size: 0.75rem;
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background: var(--bg-surface) !important;
        border-right: 1px solid var(--border-subtle);
        min-width: 320px !important;
    }
    section[data-testid="stSidebar"] .stMarkdown p {
        font-size: 0.85rem;
    }
    section[data-testid="stSidebar"] .stButton button {
        width: 100%;
        font-size: 0.85rem;
        padding: 0.5rem 0.8rem;
        font-weight: 600;
        text-align: left;
        justify-content: flex-start;
        background: transparent;
        border: 1px solid var(--border-subtle);
        color: var(--text-secondary);
        transition: all 0.2s;
        border-radius: var(--radius-sm);
        border-left: 3px solid transparent;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        border-color: var(--accent);
        color: var(--accent);
        background: var(--accent-glow);
        border-left-color: var(--accent);
    }
    /* Active nav item */
    section[data-testid="stSidebar"] .stButton button[kind="primary"] {
        background: rgba(99,102,241,0.12);
        color: var(--accent);
        border-color: transparent;
        border-left: 3px solid var(--accent);
    }
    section[data-testid="stSidebar"] .stButton button[kind="primary"]:hover {
        background: rgba(99,102,241,0.18);
        border-color: transparent;
    }
    /* Secondary/secondary style for inactive */
    section[data-testid="stSidebar"] .stButton button[kind="secondary"] {
        border-color: transparent;
        color: var(--text-secondary);
        font-size: 0.85rem;
        padding: 0.5rem 0.8rem;
        border-left: 3px solid transparent;
    }
    section[data-testid="stSidebar"] .stButton button[kind="secondary"]:hover {
        color: var(--accent);
        background: var(--accent-glow);
        border-left-color: var(--accent);
        border-color: transparent;
    }
    /* Sidebar scroll */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
        gap: 0.15rem;
    }

    /* ===== ALERTS ===== */
    div[data-testid="stAlert"] {
        border-radius: var(--radius-sm);
        font-size: 0.85rem;
        border: none;
    }
    div[data-testid="stAlert"][kind="info"] {
        background: var(--accent-glow);
        border-left: 3px solid var(--accent);
    }
    div[data-testid="stAlert"][kind="warning"] {
        background: rgba(245, 158, 11, 0.1);
        border-left: 3px solid var(--warningColor);
    }

    /* ===== PROGRESS ===== */
    div[data-testid="stProgress"] > div {
        background: var(--bg-elevated);
        border-radius: 999px;
        overflow: hidden;
    }
    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, var(--accent), #818CF8);
        border-radius: 999px;
    }

    /* ===== CONTAINERS ===== */
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.5rem;
    }

    /* ===== TIP / HINT TEXT ===== */
    .pixelle-tip {
        font-size: 0.75rem;
        color: var(--text-muted);
        padding: 0.5rem 0.75rem;
        background: var(--bg-elevated);
        border-radius: var(--radius-sm);
        border: 1px solid var(--border-subtle);
        margin: 0.5rem 0;
    }
    .pixelle-tip::before {
        content: "";
    }

    /* ===== STATUS BADGE ===== */
    .pixelle-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        font-size: 0.7rem;
        font-weight: 500;
        padding: 0.15rem 0.5rem;
        border-radius: 999px;
        background: var(--accent-glow);
        color: var(--accent);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .pixelle-header h3 { font-size: 1.1rem; }
        div[data-testid="stTabs"] button { font-size: 0.75rem; padding: 0.3rem 0.6rem; }
    }

    /* ===== FULL WIDTH MAIN CONTENT ===== */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    .stApp > header {
        max-width: 100% !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
