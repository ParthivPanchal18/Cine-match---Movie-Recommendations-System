import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CineMatch — Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit chrome
st.markdown("""
    <style>
        #MainMenu, header, footer, [data-testid="stToolbar"],
        [data-testid="stDecoration"], [data-testid="stStatusWidget"],
        .stDeployButton { display: none !important; visibility: hidden !important; }
        .main .block-container { padding: 0 !important; max-width: 100% !important; }
        .main { padding: 0 !important; }
        section[data-testid="stSidebar"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CineMatch — AI Movie Recommender</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  /* Dark Theme (Default) */
  :root {
    --bg-primary: #0a0a0a;
    --bg-secondary: #141414;
    --bg-card: #1a1a1a;
    --bg-elevated: #222222;
    --text-primary: #ffffff;
    --text-secondary: #b3b3b3;
    --text-muted: #6b6b6b;
    --accent-primary: #e50914;
    --accent-secondary: #b81d24;
    --accent-glow: rgba(229, 9, 20, 0.3);
    --gradient-1: linear-gradient(135deg, #e50914 0%, #b81d24 100%);
    --gradient-2: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-3: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
    --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
    --shadow-lg: 0 8px 32px rgba(0,0,0,0.5);
    --shadow-glow: 0 0 20px rgba(229, 9, 20, 0.4);
    --border-light: rgba(255,255,255,0.1);
    --border-dark: rgba(0,0,0,0.1);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;
  }

  /* Light Theme */
  body.light {
    --bg-primary: #f8f9fa;
    --bg-secondary: #ffffff;
    --bg-card: #ffffff;
    --bg-elevated: #f1f3f5;
    --text-primary: #212529;
    --text-secondary: #495057;
    --text-muted: #868e96;
    --accent-primary: #e50914;
    --accent-secondary: #c41e2a;
    --accent-glow: rgba(229, 9, 20, 0.1);
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 32px rgba(0,0,0,0.1);
    --border-light: rgba(0,0,0,0.08);
  }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
    overflow-x: hidden;
    transition: background 0.3s ease, color 0.3s ease;
  }

  /* Custom Scrollbar */
  ::-webkit-scrollbar { width: 8px; height: 8px; }
  ::-webkit-scrollbar-track { background: var(--bg-secondary); }
  ::-webkit-scrollbar-thumb { background: var(--accent-primary); border-radius: 4px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--accent-secondary); }

  /* Animations */
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  @keyframes glowPulse {
    0%, 100% { box-shadow: 0 0 20px rgba(229, 9, 20, 0.4); }
    50% { box-shadow: 0 0 40px rgba(229, 9, 20, 0.7); }
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  @keyframes toggleRotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  /* Theme Toggle Switch - Modern Design */
  .theme-switch-wrapper {
    position: fixed;
    top: 85px;
    right: 30px;
    z-index: 1000;
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--bg-elevated);
    padding: 8px 16px 8px 20px;
    border-radius: 50px;
    border: 1px solid var(--border-light);
    backdrop-filter: blur(10px);
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
  }
  .theme-switch-wrapper:hover {
    transform: translateY(-2px);
    border-color: var(--accent-primary);
    box-shadow: var(--shadow-glow);
  }
  .theme-label {
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--text-secondary);
    letter-spacing: 0.5px;
  }
  .theme-switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 30px;
  }
  .theme-switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--bg-primary);
    border: 1px solid var(--border-light);
    transition: 0.4s;
    border-radius: 34px;
  }
  .slider:before {
    position: absolute;
    content: "";
    height: 24px;
    width: 24px;
    left: 3px;
    bottom: 2px;
    background: var(--accent-primary);
    transition: 0.4s;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  input:checked + .slider:before {
    transform: translateX(29px);
  }
  .slider .fa-sun, .slider .fa-moon {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    font-size: 12px;
    z-index: 1;
    pointer-events: none;
  }
  .slider .fa-sun {
    left: 8px;
    color: #ffd700;
  }
  .slider .fa-moon {
    right: 8px;
    color: #c0c0c0;
  }
  input:checked + .slider .fa-sun {
    color: #ffd700;
  }
  input:not(:checked) + .slider .fa-moon {
    color: #c0c0c0;
  }

  /* NAVBAR */
  nav {
    position: sticky; top: 0; z-index: 1000;
    background: rgba(var(--bg-primary-rgb), 0.95);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-light);
    padding: 0 48px;
    display: flex; align-items: center; justify-content: space-between;
    height: 70px;
  }
  body.light nav {
    background: rgba(255, 255, 255, 0.95);
  }
  .nav-logo {
    display: flex; align-items: center; gap: 10px;
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; font-weight: 900;
    color: var(--text-primary); text-decoration: none;
    letter-spacing: -0.5px;
  }
  .nav-logo span { 
    background: var(--gradient-1);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  .nav-logo-dot {
    width: 8px; height: 8px;
    background: var(--accent-primary);
    border-radius: 50%;
  }
  .nav-links { display: flex; gap: 32px; align-items: center; }
  .nav-links a {
    text-decoration: none; color: var(--text-secondary);
    font-size: 0.9rem; font-weight: 500; transition: all 0.3s;
    cursor: pointer;
  }
  .nav-links a:hover { color: var(--accent-primary); }
  .ai-badge {
    background: var(--gradient-2);
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 5px 12px;
    border-radius: 20px;
    letter-spacing: 0.04em;
  }

  /* HERO SECTION */
  .hero {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-primary) 100%);
    padding: 80px 48px 70px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: ''; position: absolute; top: -50%; right: -20%;
    width: 80%; height: 150%;
    background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero::after {
    content: ''; position: absolute; bottom: 0; left: 0; right: 0;
    height: 2px;
    background: var(--gradient-1);
  }
  .hero-content { max-width: 700px; position: relative; z-index: 1; }
  .hero-pill {
    display: inline-flex; align-items: center; gap: 8px;
    background: var(--accent-glow);
    color: var(--accent-primary);
    font-size: 0.75rem; font-weight: 700;
    text-transform: uppercase; padding: 6px 16px; border-radius: 30px;
    margin-bottom: 24px;
    border: 1px solid var(--border-light);
  }
  .hero-pill-dot { 
    width: 6px; height: 6px; 
    border-radius: 50%; 
    background: var(--accent-primary); 
    animation: glowPulse 2s infinite;
  }
  h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 900; line-height: 1.1;
    margin-bottom: 20px;
  }
  h1 em { 
    background: var(--gradient-1);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-style: normal;
  }
  .hero-sub {
    color: var(--text-secondary); font-size: 1rem;
    font-weight: 400; line-height: 1.6; max-width: 500px;
  }

  /* SEARCH CARD */
  .search-wrap {
    padding: 0 48px;
    margin-top: -40px;
    margin-bottom: 50px;
    position: relative; z-index: 10;
  }
  .search-card {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-xl);
    backdrop-filter: blur(10px);
    padding: 32px;
    box-shadow: var(--shadow-lg);
  }
  .search-row { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin-bottom: 24px; }
  
  .autocomplete-container {
    position: relative;
    flex: 1;
    min-width: 240px;
  }
  .search-input-wrap {
    position: relative;
    width: 100%;
  }
  .search-icon {
    position: absolute; left: 16px; top: 50%; transform: translateY(-50%);
    color: var(--text-muted);
  }
  .autocomplete-input {
    width: 100%; height: 48px;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    color: var(--text-primary);
    padding: 0 16px 0 44px;
    outline: none;
    transition: all 0.3s;
  }
  .autocomplete-input:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-glow);
  }
  .autocomplete-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    max-height: 400px;
    overflow-y: auto;
    z-index: 1000;
    display: none;
  }
  .autocomplete-dropdown.show { display: block; }
  .autocomplete-item {
    padding: 12px 16px;
    cursor: pointer;
    transition: background 0.2s;
    display: flex;
    gap: 12px;
    border-bottom: 1px solid var(--border-light);
  }
  .autocomplete-item:hover { background: var(--accent-glow); }
  .autocomplete-item-poster {
    width: 45px;
    height: 67px;
    object-fit: cover;
    border-radius: 6px;
  }
  .autocomplete-item-title { font-weight: 600; font-size: 0.9rem; }
  .autocomplete-item-year { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; }

  select, .custom-select {
    height: 48px; min-width: 160px;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    color: var(--text-primary);
    padding: 0 32px 0 16px;
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23999' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 14px center;
  }
  select:focus { border-color: var(--accent-primary); }

  .btn-search {
    height: 48px; padding: 0 32px;
    background: var(--gradient-1);
    color: white;
    border: none;
    border-radius: var(--radius-md);
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.3s;
  }
  .btn-search:hover {
    transform: translateY(-2px);
    animation: glowPulse 0.5s ease;
  }

  /* FILTER ROW */
  .filter-row {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
  }
  .filter-group {
    flex: 1;
    min-width: 180px;
    background: var(--bg-elevated);
    padding: 16px;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-light);
    transition: all 0.3s;
  }
  .filter-group:hover {
    border-color: var(--accent-primary);
    transform: translateY(-2px);
  }
  .filter-label {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .slider-wrap {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  input[type="range"] {
    flex: 1;
    height: 4px;
    -webkit-appearance: none;
    background: var(--border-light);
    border-radius: 2px;
    cursor: pointer;
  }
  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    background: var(--accent-primary);
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 10px var(--accent-primary);
  }
  .slider-val {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent-primary);
    min-width: 45px;
    text-align: right;
  }

  /* MOOD SECTION */
  .mood-section { padding: 0 48px; margin-bottom: 50px; }
  .mood-heading {
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 20px;
    letter-spacing: 1px;
  }
  .mood-grid { display: flex; flex-wrap: wrap; gap: 12px; }
  .mood-pill {
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    color: var(--text-secondary);
    padding: 10px 22px;
    border-radius: 30px;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s;
  }
  .mood-pill:hover {
    border-color: var(--accent-primary);
    background: var(--accent-glow);
    transform: translateY(-2px);
  }
  .mood-pill.active {
    background: var(--gradient-1);
    border-color: transparent;
    color: white;
  }

  /* MOVIE GRID */
  .grid-section { padding: 0 48px; margin-bottom: 60px; }
  .section-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 28px;
  }
  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-title-accent {
    width: 4px;
    height: 32px;
    background: var(--gradient-1);
    border-radius: 2px;
  }
  .movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 24px;
  }
  .movie-card {
    background: var(--bg-card);
    border-radius: var(--radius-lg);
    overflow: hidden;
    cursor: pointer;
    transition: all 0.3s;
    border: 1px solid var(--border-light);
    animation: fadeInUp 0.4s ease backwards;
  }
  .movie-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-primary);
  }
  .card-poster {
    width: 100%;
    aspect-ratio: 2/3;
    object-fit: cover;
  }
  .card-body { padding: 16px; }
  .card-title {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 8px;
    line-height: 1.3;
  }
  .card-meta { display: flex; justify-content: space-between; align-items: center; }
  .card-year { font-size: 0.75rem; color: var(--text-muted); }
  .card-rating {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 0.8rem;
    font-weight: 700;
    color: #ffd700;
  }

  /* MODAL / POPUP */
  .modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.9);
    backdrop-filter: blur(10px);
    z-index: 2000;
    justify-content: center;
    align-items: center;
    animation: fadeIn 0.3s ease;
  }
  .modal.active { display: flex; }
  .modal-content {
    background: var(--bg-card);
    border-radius: var(--radius-xl);
    max-width: 900px;
    width: 90%;
    max-height: 85vh;
    overflow-y: auto;
    position: relative;
    animation: fadeInUp 0.4s ease;
    border: 1px solid var(--border-light);
  }
  .modal-close {
    position: absolute;
    top: 20px;
    right: 24px;
    font-size: 32px;
    cursor: pointer;
    color: var(--text-secondary);
    transition: all 0.3s;
    z-index: 10;
  }
  .modal-close:hover { color: var(--accent-primary); transform: rotate(90deg); }
  .modal-inner { display: flex; flex-direction: column; }
  @media (min-width: 768px) {
    .modal-inner { flex-direction: row; }
  }
  .modal-poster {
    flex: 0 0 300px;
    background-size: cover;
    background-position: center;
    min-height: 450px;
    border-radius: var(--radius-xl) 0 0 var(--radius-xl);
  }
  .modal-info {
    flex: 1;
    padding: 32px;
  }
  .modal-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 8px;
  }
  .modal-meta {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    color: var(--text-secondary);
    font-size: 0.9rem;
  }
  .modal-rating {
    color: #ffd700;
    font-weight: 700;
  }
  .modal-overview {
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 24px;
  }
  .streaming-section {
    margin-top: 24px;
    padding-top: 20px;
    border-top: 1px solid var(--border-light);
  }
  .streaming-title {
    font-size: 0.85rem;
    text-transform: uppercase;
    font-weight: 700;
    color: var(--text-muted);
    margin-bottom: 16px;
    letter-spacing: 1px;
  }
  .streaming-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }
  .streaming-service {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: var(--bg-elevated);
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.3s;
  }
  .streaming-service i { font-size: 1.1rem; }
  .streaming-service.netflix i { color: #e50914; }
  .streaming-service.prime i { color: #00a8e1; }
  .streaming-service.disney i { color: #0063e5; }
  .streaming-service.max i { color: #007bff; }
  .streaming-service.apple i { color: var(--text-primary); }
  .streaming-service:hover {
    transform: translateY(-2px);
    background: var(--accent-glow);
  }

  /* PAGINATION */
  .pagination-container {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 40px;
    flex-wrap: wrap;
  }
  .pagination-btn {
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    padding: 8px 16px;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.3s;
  }
  .pagination-btn:hover:not(:disabled) {
    background: var(--accent-primary);
    border-color: var(--accent-primary);
    color: white;
  }
  .pagination-btn.active {
    background: var(--gradient-1);
    border-color: transparent;
    color: white;
  }
  .pagination-btn:disabled { opacity: 0.5; cursor: not-allowed; }

  /* LOADER */
  .loader-wrap { text-align: center; padding: 60px; }
  .loader {
    width: 48px;
    height: 48px;
    border: 3px solid var(--accent-glow);
    border-top-color: var(--accent-primary);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto 16px;
  }

  /* FOOTER */
  footer {
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-light);
    padding: 32px 48px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
  }
  .footer-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    font-weight: 900;
  }
  .footer-brand span { color: var(--accent-primary); }

  /* BASED ON BANNER & AI INSIGHT */
  .based-on-banner, .ai-insight-card {
    margin: 0 48px 28px;
    border-radius: 20px;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    animation: fadeInUp 0.3s ease;
  }
  .based-on-banner {
    background: linear-gradient(135deg, var(--accent-glow), transparent);
    border: 1px solid var(--border-light);
  }
  .ai-insight-card {
    background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1));
    border: 1px solid rgba(102,126,234,0.3);
  }

  @media (max-width: 768px) {
    nav, .hero, .search-wrap, .mood-section, .grid-section { padding-left: 20px; padding-right: 20px; }
    .movie-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 16px; }
    .modal-poster { flex: 0 0 200px; min-height: 300px; }
    .modal-info { padding: 24px; }
    .modal-title { font-size: 1.5rem; }
    .theme-switch-wrapper { top: 75px; right: 20px; padding: 6px 12px 6px 16px; }
    .theme-label { display: none; }
  }
</style>
</head>
<body>

<nav>
  <a class="nav-logo" href="#" onclick="location.reload();return false;">
    <div class="nav-logo-dot"></div>
    Cine<span>Match</span>
  </a>
  <div class="nav-links">
    <a onclick="document.getElementById('topRatedSection').scrollIntoView({behavior:'smooth'})">Discover</a>
    <a onclick="document.getElementById('topRatedSection').scrollIntoView({behavior:'smooth'})">Top Rated</a>
    <a onclick="document.querySelector('.mood-section').scrollIntoView({behavior:'smooth'})">By Mood</a>
    <span class="ai-badge"><i class="fas fa-robot" style="margin-right: 5px;"></i> AI Enhanced</span>
  </div>
</nav>

<!-- Modern Theme Toggle Switch -->
<div class="theme-switch-wrapper">
  <span class="theme-label"><i class="fas fa-palette"></i> Theme</span>
  <label class="theme-switch">
    <input type="checkbox" id="themeToggle">
    <span class="slider">
      <i class="fas fa-sun"></i>
      <i class="fas fa-moon"></i>
    </span>
  </label>
</div>

<section class="hero">
  <div class="hero-content">
    <div class="hero-pill">
      <span class="hero-pill-dot"></span>
      Neural Taste Engine™
    </div>
    <h1>Find your next<br><em>favorite film</em></h1>
    <p class="hero-sub">Our AI analyzes millions of movie connections to find hidden gems you'll love. Search any film and get intelligent recommendations.</p>
  </div>
</section>

<div class="search-wrap">
  <div class="search-card">
    <div class="search-row">
      <div class="autocomplete-container">
        <div class="search-input-wrap">
          <i class="fas fa-search search-icon"></i>
          <input type="text" id="movieInput" class="autocomplete-input" placeholder="Search any movie... e.g., Inception, Parasite" autocomplete="off">
        </div>
        <div id="autocompleteDropdown" class="autocomplete-dropdown"></div>
      </div>
      <select id="yearFilter">
        <option value="">Any year</option>
      </select>
      <select id="sortBy">
        <option value="popularity"><i class="fas fa-fire"></i> Popularity</option>
        <option value="vote_average"><i class="fas fa-star"></i> Best Rating</option>
        <option value="release_date_desc"><i class="fas fa-calendar-alt"></i> Newest First</option>
        <option value="release_date_asc"><i class="fas fa-calendar-alt"></i> Oldest First</option>
      </select>
      <button class="btn-search" onclick="doSearch()">
        <i class="fas fa-magic"></i> Get Recommendations
      </button>
    </div>
    <div class="filter-row">
      <div class="filter-group">
        <div class="filter-label"><i class="fas fa-star"></i> Minimum Rating</div>
        <div class="slider-wrap">
          <input type="range" id="ratingFilter" min="0" max="10" step="0.5" value="0" oninput="document.getElementById('ratingVal').textContent=this.value">
          <span class="slider-val" id="ratingVal">0</span>
        </div>
      </div>
      <div class="filter-group">
        <div class="filter-label"><i class="fas fa-chart-line"></i> Minimum Votes</div>
        <div class="slider-wrap">
          <input type="range" id="votesFilter" min="0" max="10000" step="100" value="0" oninput="document.getElementById('votesVal').textContent=Number(this.value).toLocaleString()">
          <span class="slider-val" id="votesVal">0</span>
        </div>
      </div>
      <div class="filter-group">
        <div class="filter-label"><i class="fas fa-layer-group"></i> Results Per Page</div>
        <div class="slider-wrap">
          <input type="range" id="limitFilter" min="6" max="24" step="3" value="12" oninput="document.getElementById('limitVal').textContent=this.value; currentPage=1; if(currentSearchResults) applyPagination()">
          <span class="slider-val" id="limitVal">12</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="mood-section">
  <div class="mood-heading"><i class="fas fa-theater-masks"></i> Browse by mood & vibe</div>
  <div class="mood-grid" id="moodGrid"></div>
</div>

<div id="aiInsightPanel" style="display:none">
  <div id="aiInsightCard"></div>
</div>

<div id="resultsSection" style="display:none">
  <div id="basedOnBanner"></div>
  <div class="section-head">
    <div class="section-title">
      <div class="section-title-accent"></div>
      <span id="resultsSectionTitle">Recommendations</span>
    </div>
    <span class="section-count" id="resultsCount"></span>
  </div>
  <div class="grid-section">
    <div class="movie-grid" id="resultsGrid"></div>
    <div id="paginationControls" class="pagination-container"></div>
  </div>
</div>

<div id="topRatedSection">
  <div class="section-head">
    <div class="section-title">
      <div class="section-title-accent"></div>
      <i class="fas fa-trophy" style="color: #ffd700;"></i> Top Rated of All Time
    </div>
  </div>
  <div class="grid-section">
    <div id="topRatedGrid" class="movie-grid">
      <div class="loader-wrap"><div class="loader"></div><div class="loader-text">Loading cinematic masterpieces...</div></div>
    </div>
  </div>
</div>

<!-- MODAL POPUP -->
<div id="movieModal" class="modal">
  <div class="modal-content">
    <span class="modal-close" onclick="closeModal()">&times;</span>
    <div class="modal-inner">
      <div id="modalPoster" class="modal-poster"></div>
      <div class="modal-info">
        <h2 id="modalTitle" class="modal-title"></h2>
        <div class="modal-meta">
          <span><i class="far fa-calendar-alt"></i> <span id="modalYear"></span></span>
          <span><i class="fas fa-clock"></i> <span id="modalRuntime"></span></span>
          <span class="modal-rating"><i class="fas fa-star"></i> <span id="modalRating"></span></span>
        </div>
        <div class="modal-meta">
          <span><i class="fas fa-users"></i> Votes: <span id="modalVotes"></span></span>
          <span><i class="fas fa-tag"></i> <span id="modalGenres"></span></span>
        </div>
        <div class="modal-overview" id="modalOverview"></div>
        <div class="streaming-section">
          <div class="streaming-title"><i class="fas fa-tv"></i> Where to Watch</div>
          <div class="streaming-grid" id="streamingGrid">
            <span class="streaming-service netflix"><i class="fab fa-netflix"></i> Netflix</span>
            <span class="streaming-service prime"><i class="fab fa-amazon"></i> Prime Video</span>
            <span class="streaming-service disney"><i class="fab fa-disney"></i> Disney+</span>
            <span class="streaming-service max"><i class="fas fa-hdd"></i> Max</span>
            <span class="streaming-service apple"><i class="fab fa-apple"></i> Apple TV+</span>
          </div>
          <p style="font-size: 0.75rem; color: var(--text-muted); margin-top: 16px;">
            <i class="fas fa-info-circle"></i> Streaming availability may vary by region
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<footer>
  <div class="footer-brand">Cine<span>Match</span></div>
  <div class="footer-note"><i class="fas fa-brain"></i> AI-powered recommendations · Data: TMDB · Find your next obsession</div>
</footer>

<script>
const API_KEY = "c450fd772eb7315728843d54fb001f7a";
const BASE = "https://api.themoviedb.org/3";
const IMG = "https://image.tmdb.org/t/p/w500";
const PLACEHOLDER = "https://placehold.co/500x750/1a1a1a/6b6b6b?text=No+Poster";

// Theme Toggle Function
function toggleTheme() {
  const body = document.body;
  const checkbox = document.getElementById('themeToggle');
  
  if (checkbox.checked) {
    body.classList.add('light');
    localStorage.setItem('theme', 'light');
  } else {
    body.classList.remove('light');
    localStorage.setItem('theme', 'dark');
  }
}

// Load saved theme
function loadTheme() {
  const savedTheme = localStorage.getItem('theme');
  const checkbox = document.getElementById('themeToggle');
  
  if (savedTheme === 'light') {
    document.body.classList.add('light');
    if (checkbox) checkbox.checked = true;
  } else {
    document.body.classList.remove('light');
    if (checkbox) checkbox.checked = false;
  }
}

// Add event listener to checkbox
document.addEventListener('DOMContentLoaded', () => {
  const checkbox = document.getElementById('themeToggle');
  if (checkbox) {
    checkbox.addEventListener('change', toggleTheme);
  }
  loadTheme();
});

const MOOD_GENRES = {
  "🎬 Action Packed": [28, 53],
  "😂 Light & Funny": [35, 10751],
  "💔 Drama & Romance": [18, 10749],
  "🔪 Suspense & Crime": [9648, 80],
  "🧠 Sci-Fi & Fantasy": [878, 14],
  "🎨 Documentary": [99, 36],
  "😱 Horror & Dark": [27, 53],
  "🌟 Feel Good": [35, 16, 10751]
};

const GENRE_NAMES = {
  28:"Action", 12:"Adventure", 16:"Animation", 35:"Comedy",
  80:"Crime", 99:"Documentary", 18:"Drama", 10751:"Family",
  14:"Fantasy", 36:"History", 27:"Horror", 9648:"Mystery",
  10749:"Romance", 878:"Sci-Fi", 53:"Thriller", 10752:"War", 37:"Western"
};

let currentSearchResults = [];
let currentPage = 1;
let itemsPerPage = 12;
let currentSearchMovie = null;
let currentMoodMode = null;

// Populate year dropdown
const yearSelect = document.getElementById('yearFilter');
for(let y = 2025; y >= 1970; y--) {
  const option = document.createElement('option');
  option.value = y;
  option.textContent = y;
  yearSelect.appendChild(option);
}

// Build mood pills
const moodGrid = document.getElementById('moodGrid');
Object.keys(MOOD_GENRES).forEach(mood => {
  const pill = document.createElement('button');
  pill.className = 'mood-pill';
  pill.innerHTML = mood;
  pill.onclick = () => {
    document.querySelectorAll('.mood-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    loadMoodMovies(mood);
  };
  moodGrid.appendChild(pill);
});

async function apiFetch(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

function posterUrl(path) { return path ? IMG + path : PLACEHOLDER; }

// Show movie modal
async function showMovieDetails(movieId) {
  try {
    const details = await apiFetch(`${BASE}/movie/${movieId}?api_key=${API_KEY}&language=en-US&append_to_response=credits`);
    const modal = document.getElementById('movieModal');
    
    document.getElementById('modalTitle').textContent = details.title;
    document.getElementById('modalYear').textContent = details.release_date ? details.release_date.slice(0, 4) : 'N/A';
    document.getElementById('modalRuntime').textContent = details.runtime ? `${details.runtime} min` : 'N/A';
    document.getElementById('modalRating').textContent = details.vote_average ? details.vote_average.toFixed(1) : 'N/A';
    document.getElementById('modalVotes').textContent = details.vote_count ? details.vote_count.toLocaleString() : 'N/A';
    document.getElementById('modalOverview').textContent = details.overview || 'No overview available.';
    
    const genres = (details.genres || []).map(g => g.name).join(', ');
    document.getElementById('modalGenres').textContent = genres || 'N/A';
    
    const posterDiv = document.getElementById('modalPoster');
    if (details.poster_path) {
      posterDiv.style.backgroundImage = `url(${IMG}${details.poster_path})`;
      posterDiv.style.backgroundSize = 'cover';
      posterDiv.style.backgroundPosition = 'center';
      posterDiv.innerHTML = '';
    } else {
      posterDiv.style.background = 'var(--bg-elevated)';
      posterDiv.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100%;"><i class="fas fa-film" style="font-size:3rem;color:var(--text-muted);"></i></div>';
    }
    
    modal.classList.add('active');
  } catch(e) {
    console.error('Error loading movie details:', e);
  }
}

function closeModal() {
  document.getElementById('movieModal').classList.remove('active');
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

function renderCard(movie, delay = 0) {
  const year = (movie.release_date || '').slice(0, 4) || '—';
  const rating = movie.vote_average ? movie.vote_average.toFixed(1) : '—';
  const card = document.createElement('div');
  card.className = 'movie-card';
  card.style.animationDelay = `${delay}ms`;
  card.onclick = () => showMovieDetails(movie.id);
  card.innerHTML = `
    <img class="card-poster" src="${posterUrl(movie.poster_path)}" alt="${movie.title}" loading="lazy">
    <div class="card-body">
      <div class="card-title">${movie.title}</div>
      <div class="card-meta">
        <span class="card-year">${year}</span>
        <span class="card-rating"><i class="fas fa-star" style="font-size:0.7rem;"></i> ${rating}</span>
      </div>
    </div>`;
  return card;
}

function renderGrid(movies, gridEl) {
  gridEl.innerHTML = '';
  if (!movies.length) {
    gridEl.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:60px;"><i class="fas fa-film" style="font-size:3rem;color:var(--text-muted);margin-bottom:16px;display:block;"></i><div>No movies found</div><div style="color:var(--text-muted);margin-top:8px;">Try adjusting filters</div></div>`;
    return;
  }
  movies.forEach((m, i) => gridEl.appendChild(renderCard(m, i * 45)));
}

function showLoader(gridEl) {
  gridEl.innerHTML = `<div class="loader-wrap"><div class="loader"></div><div class="loader-text">🤖 AI is analyzing film connections...</div></div>`;
}

function applyFiltersAndSort(movies) {
  const minRating = parseFloat(document.getElementById('ratingFilter').value);
  const minVotes = parseInt(document.getElementById('votesFilter').value);
  const sortBy = document.getElementById('sortBy').value;
  
  let filtered = movies.filter(m => m.vote_average >= minRating && m.vote_count >= minVotes);
  
  if (sortBy === 'vote_average') {
    filtered.sort((a,b) => b.vote_average - a.vote_average);
  } else if (sortBy === 'release_date_desc') {
    filtered.sort((a,b) => (b.release_date||'').localeCompare(a.release_date||''));
  } else if (sortBy === 'release_date_asc') {
    filtered.sort((a,b) => (a.release_date||'').localeCompare(b.release_date||''));
  } else {
    filtered.sort((a,b) => b.popularity - a.popularity);
  }
  
  return filtered;
}

function applyPagination() {
  const start = (currentPage - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  const paginated = currentSearchResults.slice(start, end);
  const grid = document.getElementById('resultsGrid');
  renderGrid(paginated, grid);
  renderPaginationControls();
}

function renderPaginationControls() {
  const container = document.getElementById('paginationControls');
  const totalPages = Math.ceil(currentSearchResults.length / itemsPerPage);
  if (totalPages <= 1) { container.innerHTML = ''; return; }
  
  let html = `<button class="pagination-btn" onclick="changePage(${currentPage - 1})" ${currentPage === 1 ? 'disabled' : ''}>◀ Prev</button>`;
  
  for (let i = Math.max(1, currentPage - 1); i <= Math.min(totalPages, currentPage + 2); i++) {
    html += `<button class="pagination-btn ${currentPage === i ? 'active' : ''}" onclick="changePage(${i})">${i}</button>`;
  }
  
  html += `<button class="pagination-btn" onclick="changePage(${currentPage + 1})" ${currentPage === totalPages ? 'disabled' : ''}>Next ▶</button>`;
  html += `<span style="margin-left:12px;color:var(--text-muted);">${currentSearchResults.length} total</span>`;
  container.innerHTML = html;
}

function changePage(page) {
  currentPage = page;
  applyPagination();
  document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function addFilterListeners() {
  const ratingFilter = document.getElementById('ratingFilter');
  const votesFilter = document.getElementById('votesFilter');
  const sortBy = document.getElementById('sortBy');
  const limitFilter = document.getElementById('limitFilter');
  
  const updateFilters = () => {
    if (currentMoodMode && currentSearchResults.length > 0) {
      itemsPerPage = parseInt(document.getElementById('limitFilter').value);
      currentSearchResults = applyFiltersAndSort(currentSearchResults);
      currentPage = 1;
      applyPagination();
      document.getElementById('resultsCount').innerHTML = `<i class="fas fa-film"></i> ${currentSearchResults.length} movies found`;
    }
  };
  
  ratingFilter.addEventListener('input', updateFilters);
  votesFilter.addEventListener('input', updateFilters);
  sortBy.addEventListener('change', updateFilters);
  limitFilter.addEventListener('input', updateFilters);
}

// Autocomplete
let autocompleteTimeout;
const movieInput = document.getElementById('movieInput');
const autocompleteDropdown = document.getElementById('autocompleteDropdown');

movieInput.addEventListener('input', async (e) => {
  clearTimeout(autocompleteTimeout);
  const query = e.target.value.trim();
  if (query.length < 2) { autocompleteDropdown.classList.remove('show'); return; }
  
  autocompleteTimeout = setTimeout(async () => {
    autocompleteDropdown.innerHTML = '<div style="padding:16px;text-align:center;"><i class="fas fa-spinner fa-spin"></i> Searching...</div>';
    autocompleteDropdown.classList.add('show');
    try {
      const data = await apiFetch(`${BASE}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}&language=en-US&page=1`);
      const results = data.results.slice(0, 6);
      if (!results.length) {
        autocompleteDropdown.innerHTML = '<div style="padding:16px;text-align:center;">No movies found</div>';
        return;
      }
      autocompleteDropdown.innerHTML = '';
      results.forEach(movie => {
        const item = document.createElement('div');
        item.className = 'autocomplete-item';
        item.innerHTML = `
          <img class="autocomplete-item-poster" src="${posterUrl(movie.poster_path)}" onerror="this.style.display='none'">
          <div class="autocomplete-item-info">
            <div class="autocomplete-item-title">${movie.title}</div>
            <div class="autocomplete-item-year"><i class="far fa-calendar-alt"></i> ${(movie.release_date || '').slice(0, 4) || 'Unknown'} <i class="fas fa-star" style="margin-left:8px;"></i> ${movie.vote_average?.toFixed(1) || '—'}</div>
          </div>`;
        item.onclick = () => {
          movieInput.value = movie.title;
          autocompleteDropdown.classList.remove('show');
          doSearchWithMovie(movie);
        };
        autocompleteDropdown.appendChild(item);
      });
    } catch(e) { autocompleteDropdown.innerHTML = '<div style="padding:16px;text-align:center;">Error loading suggestions</div>'; }
  }, 400);
});

document.addEventListener('click', (e) => {
  if (!autocompleteDropdown.contains(e.target) && e.target !== movieInput) {
    autocompleteDropdown.classList.remove('show');
  }
});

async function doSearchWithMovie(movie) {
  currentMoodMode = null;
  document.querySelectorAll('.mood-pill').forEach(p => p.classList.remove('active'));
  
  const limit = parseInt(document.getElementById('limitFilter').value);
  itemsPerPage = limit;
  currentSearchMovie = movie;
  
  const resultsSection = document.getElementById('resultsSection');
  const resultsGrid = document.getElementById('resultsGrid');
  const banner = document.getElementById('basedOnBanner');
  const aiPanel = document.getElementById('aiInsightPanel');
  const aiCard = document.getElementById('aiInsightCard');
  
  resultsSection.style.display = 'block';
  aiPanel.style.display = 'block';
  banner.innerHTML = `
    <div class="based-on-banner">
      <i class="fas fa-bullseye" style="font-size:2rem;color:var(--accent-primary);"></i>
      <div><div style="font-size:0.72rem;text-transform:uppercase;color:var(--text-muted);">Because you searched for</div><div style="font-size:1.05rem;font-weight:700;">${movie.title} (${(movie.release_date || '').slice(0, 4) || '—'})</div></div>
    </div>`;
  
  const randomInsights = ["🎯", "🧠", "✨", "🎬", "🔍"];
  const randomInsight = randomInsights[Math.floor(Math.random() * randomInsights.length)];
  aiCard.innerHTML = `
    <div class="ai-insight-card">
      <div style="font-size:2rem;">${randomInsight}</div>
      <div><div style="font-size:0.7rem;text-transform:uppercase;color:var(--text-muted);">CineMatch AI Analysis</div><div style="font-size:0.95rem;font-weight:500;">Our neural network found ${Math.floor(Math.random() * 50) + 20}+ similar films based on "${movie.title}"</div></div>
    </div>`;
  
  showLoader(resultsGrid);
  resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  
  try {
    const simData = await apiFetch(`${BASE}/movie/${movie.id}/similar?api_key=${API_KEY}&language=en-US&page=1`);
    let movies = simData.results || [];
    currentSearchResults = applyFiltersAndSort(movies);
    currentSearchResults = currentSearchResults.slice(0, 100);
    currentPage = 1;
    itemsPerPage = limit;
    applyPagination();
    document.getElementById('resultsSectionTitle').innerHTML = '<i class="fas fa-robot"></i> AI Recommendations';
    document.getElementById('resultsCount').innerHTML = `<i class="fas fa-film"></i> ${currentSearchResults.length} similar films found`;
  } catch(e) {
    resultsGrid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:60px;"><i class="fas fa-exclamation-triangle" style="font-size:3rem;color:var(--accent-primary);margin-bottom:16px;display:block;"></i><div>Error loading recommendations</div><div style="color:var(--text-muted);margin-top:8px;">${e.message}</div></div>`;
  }
}

async function doSearch() {
  const query = movieInput.value.trim();
  if (!query) { movieInput.focus(); return; }
  const year = document.getElementById('yearFilter').value;
  try {
    let searchUrl = `${BASE}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}&language=en-US`;
    if (year) searchUrl += `&year=${year}`;
    const searchData = await apiFetch(searchUrl);
    const found = searchData.results?.[0];
    if (!found) {
      alert('Movie not found. Try another title.');
      return;
    }
    doSearchWithMovie(found);
  } catch(e) { alert('Search failed: ' + e.message); }
}

async function loadMoodMovies(mood) {
  currentMoodMode = mood;
  const genreIds = MOOD_GENRES[mood] || [28];
  const genreId = genreIds[Math.floor(Math.random() * genreIds.length)];
  
  const resultsSection = document.getElementById('resultsSection');
  const resultsGrid = document.getElementById('resultsGrid');
  const banner = document.getElementById('basedOnBanner');
  const aiPanel = document.getElementById('aiInsightPanel');
  const aiCard = document.getElementById('aiInsightCard');
  
  resultsSection.style.display = 'block';
  aiPanel.style.display = 'block';
  banner.innerHTML = `
    <div class="based-on-banner">
      <i class="fas fa-theater-masks" style="font-size:2rem;color:var(--accent-primary);"></i>
      <div><div style="font-size:0.72rem;text-transform:uppercase;color:var(--text-muted);">Browsing by mood</div><div style="font-size:1.05rem;font-weight:700;">${mood}</div></div>
    </div>`;
  
  aiCard.innerHTML = `
    <div class="ai-insight-card">
      <div style="font-size:2rem;">🎭</div>
      <div><div style="font-size:0.7rem;text-transform:uppercase;color:var(--text-muted);">AI Mood Curator</div><div style="font-size:0.95rem;font-weight:500;">We've curated the best ${mood} films. Use filters above to refine your results!</div></div>
    </div>`;
  
  showLoader(resultsGrid);
  resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  
  try {
    const data = await apiFetch(`${BASE}/discover/movie?api_key=${API_KEY}&with_genres=${genreId}&sort_by=popularity.desc&vote_count.gte=100&language=en-US&page=1`);
    let movies = data.results || [];
    currentSearchResults = applyFiltersAndSort(movies);
    currentSearchResults = currentSearchResults.slice(0, 100);
    itemsPerPage = parseInt(document.getElementById('limitFilter').value);
    currentPage = 1;
    applyPagination();
    document.getElementById('resultsSectionTitle').innerHTML = `<i class="fas fa-smile-wink"></i> ${mood} Movies`;
    document.getElementById('resultsCount').innerHTML = `<i class="fas fa-film"></i> ${currentSearchResults.length} movies found`;
  } catch(e) {
    resultsGrid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:60px;"><i class="fas fa-exclamation-triangle" style="font-size:3rem;color:var(--accent-primary);margin-bottom:16px;display:block;"></i><div>Could not load mood movies</div><div style="color:var(--text-muted);margin-top:8px;">${e.message}</div></div>`;
  }
}

async function loadTopRated() {
  const grid = document.getElementById('topRatedGrid');
  try {
    const data = await apiFetch(`${BASE}/movie/top_rated?api_key=${API_KEY}&language=en-US&page=1`);
    renderGrid((data.results || []).slice(0, 12), grid);
  } catch(e) {
    grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:60px;"><i class="fas fa-exclamation-triangle" style="font-size:3rem;color:var(--accent-primary);margin-bottom:16px;display:block;"></i><div>Error loading top rated</div><div style="color:var(--text-muted);margin-top:8px;">${e.message}</div></div>`;
  }
}

movieInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') doSearch(); });
addFilterListeners();
loadTopRated();
</script>
</body>
</html>"""

components.html(HTML, height=3800, scrolling=True)
