# =========================================
# IMPORTS
# =========================================

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import base64

st.set_page_config(page_title="COORDENADA MX", layout="wide")

import os
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "fashion_trends_final.csv"))
def img_to_base64(path):
    full_path = os.path.join(os.path.dirname(__file__), path)
    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
.stApp { background-color: #f5f1ea; }
.block-container { padding-top: 2rem; padding-left: 4rem; padding-right: 4rem; }
.main-title { font-size: 82px; font-weight: 700; color: #2a2233; margin-bottom: 0; font-family: 'Cormorant Garamond', serif; line-height: 0.95; }
.subtitle { font-size: 14px; color: #8a7d74; margin-top: 8px; margin-bottom: 40px; letter-spacing: 4px; text-transform: uppercase; font-family: 'Inter', sans-serif; }
.section-title { font-size: 58px; font-family: 'Cormorant Garamond', serif; color: #2a2233; margin-top: 40px; margin-bottom: 30px; }
.card-category { fontDRAPED-size: 11px; letter-spacing: 3px; text-transform: uppercase; color: #7d7068; font-family: 'Inter', sans-serif; margin-top: 20px; margin-bottom: 10px; }
.card-title { font-size: 40px; color: #2f2430; margin-top: 0; font-family: 'Cormorant Garamond', serif; line-height: 0.95; }
.card-text { font-size: 15px; color: #5c524d; font-family: 'Inter', sans-serif; line-height: 1.8; margin-top: 10px; }
.arrow-link { display: flex; align-items: center; gap: 12px; margin-top: 24px; font-family: 'Inter', sans-serif; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; color: #7b6c62; }
.arrow-line { width: 90px; height: 1px; background-color: #7b6c62; position: relative; }
.arrow-line::after { content: ""; position: absolute; right: 0; top: -3px; width: 8px; height: 8px; border-top: 1px solid #7b6c62; border-right: 1px solid #7b6c62; transform: rotate(45deg); }
.highlight-card { background-color: #f8f5f0; border-radius: 16px; padding: 24px; border: 1px solid #ece4db; margin-bottom: 25px; }
.highlight-category { font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #8a7d74; font-family: 'Inter', sans-serif; }
.highlight-title { font-size: 30px; font-family: 'Cormorant Garamond', serif; color: #2b2230; margin-top: 12px; line-height: 1; }
.highlight-text { font-size: 14px; color: #5d5450; font-family: 'Inter', sans-serif; margin-top: 12px; line-height: 1.7; }
.color-label { font-family: 'Inter', sans-serif; font-size: 12px; letter-spacing: 4px; text-transform: uppercase; color: #8a7d74; margin-bottom: 12px; }
.color-title { font-family: 'Cormorant Garamond', serif; font-size: 64px; line-height: 0.9; color: #2a2233; margin-bottom: 28px; }
.color-text { font-family: 'Inter', sans-serif; font-size: 15px; line-height: 1.9; color: #5f5650; max-width: 520px; }
.ticker-wrapper { background-color: #2a2233; padding: 14px 0; overflow: hidden; white-space: nowrap; margin: 40px 0; }
.ticker-content { display: inline-block; animation: ticker 25s linear infinite; font-family: 'Inter', sans-serif; font-size: 12px; letter-spacing: 4px; text-transform: uppercase; color: rgba(255,255,255,0.85); }
.ticker-content span { color: #cfbca0; margin: 0 18px; }
@keyframes ticker { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">COORDENADA MX</div>
<div class="subtitle">INTELIGENCIA CULTURAL LATINOAMERICANA</div>
""", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Inicio", "Tendencias", "Estéticas", "Cultura", "Laboratorio", "Noticias"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "#f5f1ea", "padding": "0!important", "margin-bottom": "35px"},
        "nav-link": {"font-size": "14px", "font-family": "Inter", "font-weight": "600", "letter-spacing": "1.5px", "text-transform": "uppercase", "color": "#3b2c2c", "padding": "0px 25px"},
        "nav-link-selected": {"background-color": "#5c001f", "color": "white"},
    }
)

TICKER_HTML = """
<div class="ticker-wrapper">
    <div class="ticker-content">
        VISIBLE MIDRIFF <span>•</span> DRAPED ELEGANCE <span>•</span> COQUETTE TROPICAL <span>•</span>
        BARRO QUEMADO <span>•</span> GORPCORE LATAM <span>•</span> OFFICE SIREN <span>•</span>
        QUIET LUXURY <span>•</span> Europa impulsa la estética. México decide su permanencia. <span>•</span>
        VISIBLE MIDRIFF <span>•</span> DRAPED ELEGANCE <span>•</span> COQUETTE TROPICAL <span>•</span>
        BARRO QUEMADO <span>•</span> GORPCORE LATAM <span>•</span> OFFICE SIREN <span>•</span>
        QUIET LUXURY <span>•</span> Europa impulsa la estética. México decide su permanencia. <span>•</span>
    </div>
</div>
"""

if selected == "Inicio":

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image("ImagenHero.png", use_container_width=True)
        st.markdown("""
        <div style="position:relative;margin-top:-85px;margin-left:28px;z-index:10;">
            <div style="background:rgba(208,190,162,0.95);padding:16px 28px;display:inline-block;
                font-family:'Inter',sans-serif;font-size:13px;letter-spacing:4px;text-transform:uppercase;color:white;">
                001 | IDENTIDAD RAÍZ
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("ImagenTelas.png", use_container_width=True)
        st.markdown("""
        <div class="card-category">Tendencias</div>
        <div class="card-title">Minimalismo Utilitario</div>
        <div class="card-text">Materialidad orgánica, funcionalidad silenciosa y arquitectura emocional como nuevo lenguaje del lujo contemporáneo.</div>
        <div class="arrow-link"><div>Explorar materialidad</div><div class="arrow-line"></div></div>
        """, unsafe_allow_html=True)

    img_vis  = img_to_base64("Visible Midriff.png")
    img_coq  = img_to_base64("Coquette Aesthetic.png")
    img_drap = img_to_base64("Draped Elegance.png")

    components.html(f"""
        <style>
            * {{ margin:0;padding:0;box-sizing:border-box; }}
            body {{ background:transparent;font-family:'Inter',sans-serif; }}
            .esteticas-block {{ background:#5c001f;border-radius:24px;padding:48px 52px;margin-top:32px;display:flex;justify-content:space-between;align-items:center;gap:40px; }}
            .esteticas-left {{ flex:1; }}
            .esteticas-label {{ font-size:11px;letter-spacing:4px;text-transform:uppercase;color:rgba(255,255,255,0.5);margin-bottom:16px; }}
            .esteticas-title {{ font-family:'Cormorant Garamond',serif;font-size:72px;font-weight:700;line-height:0.88;color:white;margin-bottom:28px; }}
            .esteticas-sub {{ font-size:13px;line-height:1.8;color:rgba(255,255,255,0.65);max-width:320px;letter-spacing:0.3px; }}
            .esteticas-right {{ flex:1.2;min-width:0;overflow:hidden; }}
            .carousel {{ position:relative;width:100%;overflow:hidden;border-radius:16px; }}
            .carousel-track {{ display:flex;transition:transform 0.45s cubic-bezier(0.4,0,0.2,1); }}
            .carousel-slide {{ width:100%;height:400px;object-fit:cover;object-position:center;flex-shrink:0;display:block; }}
            .carousel-btn {{ position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.15);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.2);border-radius:50%;width:36px;height:36px;cursor:pointer;font-size:16px;color:white;z-index:10;display:flex;align-items:center;justify-content:center;transition:background 0.2s; }}
            .carousel-btn:hover {{ background:rgba(255,255,255,0.28); }}
            .btn-prev {{ left:10px; }} .btn-next {{ right:10px; }}
            .carousel-caption {{ position:absolute;bottom:0;left:0;right:0;padding:28px 18px 16px;background:linear-gradient(to top,rgba(0,0,0,0.7),transparent);border-radius:0 0 16px 16px;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:white; }}
            .carousel-dots {{ display:flex;justify-content:center;gap:6px;margin-top:14px; }}
            .dot {{ width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,0.3);cursor:pointer;transition:background 0.3s; }}
            .dot.active {{ background:white; }}
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&family=Inter:wght@300;400&display=swap" rel="stylesheet">
        <div class="esteticas-block">
            <div class="esteticas-left">
                <div class="esteticas-label">Coordenada MX / Análisis LATAM</div>
                <div class="esteticas-title">ESTÉTICAS<br>QUE<br>SOBREVIVEN</div>
                <div class="esteticas-sub">Las tendencias con mayor permanencia en México y Latinoamérica, filtradas por resonancia cultural, clima y adaptabilidad urbana.</div>
            </div>
            <div class="esteticas-right">
                <div class="carousel">
                    <div class="carousel-track" id="track">
                        <div style="position:relative;min-width:100%;flex-shrink:0;overflow:hidden;">
                            <img class="carousel-slide" src="data:image/png;base64,{img_vis}" />
                            <div class="carousel-caption">Visible Midriff — 6.94</div>
                        </div>
                        <div style="position:relative;min-width:100%;flex-shrink:0;overflow:hidden;">
                            <img class="carousel-slide" src="data:image/png;base64,{img_coq}" />
                            <div class="carousel-caption">Coquette Aesthetic — 6.21</div>
                        </div>
                        <div style="position:relative;min-width:100%;flex-shrink:0;overflow:hidden;">
                            <img class="carousel-slide" src="data:image/png;base64,{img_drap}" />
                            <div class="carousel-caption">Draped Elegance — 6.19</div>
                        </div>
                    </div>
                    <button class="carousel-btn btn-prev" onclick="move(-1)">&#8592;</button>
                    <button class="carousel-btn btn-next" onclick="move(1)">&#8594;</button>
                </div>
                <div class="carousel-dots">
                    <div class="dot active" id="dot-0" onclick="goTo(0)"></div>
                    <div class="dot" id="dot-1" onclick="goTo(1)"></div>
                    <div class="dot" id="dot-2" onclick="goTo(2)"></div>
                </div>
            </div>
        </div>
        <script>
            let current=0; const total=3;
            function updateDots(){{for(let i=0;i<total;i++)document.getElementById('dot-'+i).classList.remove('active');document.getElementById('dot-'+current).classList.add('active');}}
            function move(dir){{current=(current+dir+total)%total;document.getElementById('track').style.transform='translateX(-'+(current*100)+'%)';updateDots();}}
            function goTo(index){{current=index;document.getElementById('track').style.transform='translateX(-'+(current*100)+'%)';updateDots();}}
        </script>
    """, height=500)

    st.markdown(TICKER_HTML, unsafe_allow_html=True)

    img_telas = img_to_base64("Modelo Marron.png")
    img_arq   = img_to_base64("Arquitectura Marron.png")

    colColor1, colColor2 = st.columns([1.1, 1])

    with colColor1:
        st.markdown("""
        <div class="color-label">Color del mes</div>
        <div class="color-title">BARRO<br>QUEMADO</div>
        <div class="color-text">
            Europa continúa empujando neutralidad fría y lujo silencioso.<br><br>
            México regresa a pigmentos minerales, superficies cálidas y materialidad emocional ligada al territorio.<br><br>
            El barro ya no representa nostalgia artesanal. Representa permanencia visual en una era de hiperconsumo digital.
        </div>
        """, unsafe_allow_html=True)

    with colColor2:
        components.html(f"""
            <style>
                * {{ margin:0;padding:0;box-sizing:border-box; }}
                body {{ background:transparent; }}
                .carousel2 {{ position:relative;width:100%;overflow:hidden;border-radius:14px; }}
                .track2 {{ display:flex;transition:transform 0.4s ease; }}
                .slide2 {{ min-width:100%;height:260px;border-radius:14px;object-fit:cover;flex-shrink:0; }}
                .swatch {{ min-width:100%;height:260px;background:#9f3b21;border-radius:14px;position:relative;flex-shrink:0; }}
                .code {{ position:absolute;bottom:18px;left:18px;background:rgba(245,241,234,0.96);padding:12px 16px;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#2a2233;border-radius:6px;font-family:'Inter',sans-serif; }}
                .btn2 {{ position:absolute;top:45%;transform:translateY(-50%);background:rgba(245,241,234,0.85);border:none;border-radius:50%;width:32px;height:32px;cursor:pointer;font-size:16px;color:#2a2233;z-index:10;display:flex;align-items:center;justify-content:center; }}
                .btn2:hover {{ background:rgba(245,241,234,1); }}
                .prev2 {{ left:10px; }} .next2 {{ right:10px; }}
                .dots2 {{ display:flex;justify-content:center;gap:6px;margin-top:12px; }}
                .dot2 {{ width:6px;height:6px;border-radius:50%;background:#c9bdb4;cursor:pointer;transition:background 0.3s; }}
                .dot2.active {{ background:#9f3b21; }}
                .meta {{ margin-top:14px;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#8a7d74;font-family:'Inter',sans-serif; }}
            </style>
            <div class="carousel2">
                <div class="track2" id="track2">
                    <div class="swatch"><div class="code">CMX-01 / BARRO QUEMADO</div></div>
                    <img class="slide2" src="data:image/png;base64,{img_telas}" />
                    <img class="slide2" src="data:image/png;base64,{img_arq}" />
                </div>
                <button class="btn2 prev2" onclick="move2(-1)">&#8592;</button>
                <button class="btn2 next2" onclick="move2(1)">&#8594;</button>
            </div>
            <div class="dots2">
                <div class="dot2 active" id="d0" onclick="goTo2(0)"></div>
                <div class="dot2" id="d1" onclick="goTo2(1)"></div>
                <div class="dot2" id="d2" onclick="goTo2(2)"></div>
            </div>
            <div class="meta">Coordenada MX / Sistema Cromático Latinoamericano</div>
            <script>
                let cur2=0;const tot2=3;
                function updateDots2(){{for(let i=0;i<tot2;i++)document.getElementById('d'+i).classList.remove('active');document.getElementById('d'+cur2).classList.add('active');}}
                function move2(d){{cur2=(cur2+d+tot2)%tot2;document.getElementById('track2').style.transform='translateX(-'+(cur2*100)+'%)';updateDots2();}}
                function goTo2(i){{cur2=i;document.getElementById('track2').style.transform='translateX(-'+(cur2*100)+'%)';updateDots2();}}
            </script>
        """, height=340)
elif selected == "Tendencias":

    import plotly.graph_objects as go
    import numpy as np

    st.markdown('<div class="section-title">TENDENCIAS / Forecast Global</div>', unsafe_allow_html=True)

    ascendente   = df[df["trend_survival_type"] == "evolving"].sort_values("latam_survival_score", ascending=False)
    permanencia  = df[df["trend_survival_type"] == "long_lasting"].sort_values("latam_survival_score", ascending=False)
    evanescencia = df[df["trend_survival_type"] == "microtrend"].sort_values("latam_survival_score", ascending=True)

    x = np.linspace(0, 10, 300)
    asc  = 2.5 * np.exp(-((x - 2.5)**2) / 1.5)
    perm = 3.5 * np.exp(-((x - 5.5)**2) / 2.5)
    evan = 1.8 * np.exp(-((x - 8.5)**2) / 1.2)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x, y=asc,
        fill='tozeroy',
        fillcolor='rgba(207,188,160,0.35)',
        line=dict(color='#cfbca0', width=2),
        name='Ascendente',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=x, y=perm,
        fill='tozeroy',
        fillcolor='rgba(92,0,31,0.25)',
        line=dict(color='#5c001f', width=2.5),
        name='Permanencia',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=x, y=evan,
        fill='tozeroy',
        fillcolor='rgba(90,84,80,0.2)',
        line=dict(color='#8a7d74', width=1.5),
        name='Evanescencia',
        hoverinfo='skip'
    ))

    top_asc  = ascendente.iloc[0]
    top_perm = permanencia.iloc[0]
    top_evan = evanescencia.iloc[0]

    fig.add_annotation(
        x=2.5, y=2.8,
        text=f"<b>{top_asc['trend_name'].title()}</b><br>+{int(top_asc['growth_percent'])}%" if top_asc['growth_percent'] > 0 else f"<b>{top_asc['trend_name'].title()}</b>",
        showarrow=False, font=dict(family="Inter", size=11, color="#2a2233"),
        bgcolor="rgba(245,241,234,0.9)", borderpad=6
    )
    fig.add_annotation(
        x=5.5, y=3.8,
        text=f"<b>{top_perm['trend_name'].title()}</b><br>+{int(top_perm['growth_percent'])}%" if top_perm['growth_percent'] > 0 else f"<b>{top_perm['trend_name'].title()}</b>",
        showarrow=False, font=dict(family="Inter", size=11, color="white"),
        bgcolor="rgba(92,0,31,0.85)", borderpad=6
    )
    fig.add_annotation(
        x=8.5, y=2.1,
        text=f"<b>{top_evan['trend_name'].title()}</b>",
        showarrow=False, font=dict(family="Inter", size=11, color="#5c524d"),
        bgcolor="rgba(245,241,234,0.9)", borderpad=6
    )

    fig.add_vline(x=4, line_dash="dot", line_color="rgba(42,34,51,0.2)", line_width=1)
    fig.add_vline(x=7, line_dash="dot", line_color="rgba(42,34,51,0.2)", line_width=1)

    fig.add_annotation(x=1.5, y=4.2, text="ASCENDENTE <i>(Lo que viene)</i>",
        showarrow=False, font=dict(family="Inter", size=10, color="#7d7068"), xanchor="left")
    fig.add_annotation(x=4.2, y=4.2, text="PERMANENCIA <i>(Lo que se queda)</i>",
        showarrow=False, font=dict(family="Inter", size=10, color="#5c001f"), xanchor="left")
    fig.add_annotation(x=7.2, y=4.2, text="EVANESCENCIA <i>(Lo que se va)</i>",
        showarrow=False, font=dict(family="Inter", size=10, color="#8a7d74"), xanchor="left")

    fig.update_layout(
        height=320,
        margin=dict(l=0, r=0, t=40, b=20),
        paper_bgcolor='#f5f1ea',
        plot_bgcolor='#f5f1ea',
        showlegend=False,
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False,
                   title=dict(text="TIEMPO →", font=dict(family="Inter", size=10, color="#8a7d74"))),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False,
                   title=dict(text="PREDICCIÓN DE MERCADO", font=dict(family="Inter", size=10, color="#8a7d74"))),
        font=dict(family="Inter"),
    )

    st.plotly_chart(fig, use_container_width=True)

    col_a, col_p, col_e = st.columns(3)

    with col_a:
        st.markdown("""
        <div style="font-family:'Inter',sans-serif;font-size:11px;letter-spacing:3px;
            text-transform:uppercase;color:#cfbca0;margin-bottom:16px;">
            ▲ ASCENDENTE — Crece / Lo que viene
        </div>
        """, unsafe_allow_html=True)
        for _, row in ascendente.head(2).iterrows():
            growth = f"+{int(row['growth_percent'])}%" if row['growth_percent'] > 0 else "—"
            st.markdown(f"""
            <div class="highlight-card" style="border-left:3px solid #cfbca0;">
                <div class="highlight-category">Tendencia emergente</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text">
                    <strong>Macrotendencia:</strong> {row['macrotrend'].title()}<br>
                    <strong>Crecimiento:</strong> {growth}<br>
                    <strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}<br>
                    <strong>Mood estético:</strong> {row['mood_aesthetic'].title()}
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_p:
        st.markdown("""
        <div style="font-family:'Inter',sans-serif;font-size:11px;letter-spacing:3px;
            text-transform:uppercase;color:#5c001f;margin-bottom:16px;">
            ● PERMANENCIA — Se queda / El núcleo
        </div>
        """, unsafe_allow_html=True)
        for _, row in permanencia.head(2).iterrows():
            growth = f"+{int(row['growth_percent'])}%" if row['growth_percent'] > 0 else "—"
            st.markdown(f"""
            <div class="highlight-card" style="border-left:3px solid #5c001f;">
                <div class="highlight-category">Tendencia consolidada</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text">
                    <strong>Macrotendencia:</strong> {row['macrotrend'].title()}<br>
                    <strong>Crecimiento:</strong> {growth}<br>
                    <strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}<br>
                    <strong>Survival Score:</strong> {round(row['survival_score'], 2)}
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_e:
        st.markdown("""
        <div style="font-family:'Inter',sans-serif;font-size:11px;letter-spacing:3px;
            text-transform:uppercase;color:#8a7d74;margin-bottom:16px;">
            ▼ EVANESCENCIA — Se va / Declive
        </div>
        """, unsafe_allow_html=True)
        for _, row in evanescencia.head(2).iterrows():
            st.markdown(f"""
            <div class="highlight-card" style="border-left:3px solid #8a7d74;">
                <div class="highlight-category">En declive</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text">
                    <strong>Macrotendencia:</strong> {row['macrotrend'].title()}<br>
                    <strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}<br>
                    <strong>Mood estético:</strong> {row['mood_aesthetic'].title()}<br>
                    <strong>Tipo:</strong> Microtendencia
                </div>
            </div>
            """, unsafe_allow_html=True)


    # --- INSIGHT EDITORIAL ---
    st.markdown("""
    <div style="
        background:#2a2233;
        border-radius:12px;
        padding:20px 28px;
        margin-top:32px;
        font-family:'Inter',sans-serif;
        font-size:13px;
        color:rgba(255,255,255,0.75);
        letter-spacing:0.5px;
        line-height:1.8;
    ">
        <span style="color:#cfbca0;letter-spacing:3px;font-size:10px;text-transform:uppercase;">
            CM-FORECAST INSIGHT
        </span><br>
        Europa propone el concepto, pero el territorio dicta la supervivencia.
        Nuestro modelo no copia el entorno europeo — predice su mutación genética
        al chocar con el mercado latinoamericano.
    </div>
    """, unsafe_allow_html=True)
# --- GALERÍA HOVER ---

    img_coquette = img_to_base64("COQUETTE AESTHETIC.png")
    img_fringe   = img_to_base64("FRINGE MOTION.png")
    img_visible  = img_to_base64("VISIBLE MIDRIFF.png")
    img_draped   = img_to_base64("DRAPED ELEGANCE.png")
    img_layered  = img_to_base64("LAYERED VOLUME.png")
    img_mob      = img_to_base64("MOB WIFE AESTHETIC.png")

    components.html(f"""
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ background:transparent; font-family:'Inter',sans-serif; }}

        .gallery {{
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 8px;
            margin-top: 40px;
            height: 480px;
        }}

        .gallery-item {{
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            cursor: pointer;
            transition: flex 0.5s cubic-bezier(0.4,0,0.2,1);
            flex: 1;
        }}

        .gallery {{
            display: flex;
            gap: 8px;
        }}

        .gallery-item:hover {{
            flex: 3.5;
        }}

        .gallery-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center top;
            transition: transform 0.5s ease;
        }}

        .gallery-item:hover img {{
            transform: scale(1.03);
        }}

        .gallery-overlay {{
            position: absolute;
            bottom: 0; left: 0; right: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.3) 60%, transparent 100%);
            padding: 24px 18px 18px;
            opacity: 0;
            transition: opacity 0.4s ease;
            border-radius: 0 0 12px 12px;
        }}

        .gallery-item:hover .gallery-overlay {{
            opacity: 1;
        }}

        .gallery-badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 9px;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
            font-weight: 600;
        }}

        .badge-evolving   {{ background: rgba(207,188,160,0.9); color: #2a2233; }}
        .badge-long       {{ background: rgba(92,0,31,0.9);     color: white; }}
        .badge-microtrend {{ background: rgba(90,84,80,0.9);    color: white; }}

        .gallery-name {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 22px;
            font-weight: 700;
            color: white;
            line-height: 1;
            margin-bottom: 6px;
        }}

        .gallery-meta {{
            font-size: 11px;
            color: rgba(255,255,255,0.7);
            letter-spacing: 1px;
        }}

        .gallery-score {{
            position: absolute;
            top: 14px;
            right: 14px;
            background: rgba(245,241,234,0.92);
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 10px;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #2a2233;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.4s ease;
        }}

        .gallery-item:hover .gallery-score {{
            opacity: 1;
        }}
    </style>

    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">

    <div class="gallery">

        <div class="gallery-item">
            <img src="data:image/png;base64,{img_coquette}" />
            <div class="gallery-score">LATAM 6.21</div>
            <div class="gallery-overlay">
                <span class="gallery-badge badge-evolving">Ascendente</span>
                <div class="gallery-name">Coquette Aesthetic</div>
                <div class="gallery-meta">Romantic Revival · Hyper Femininity</div>
            </div>
        </div>

        <div class="gallery-item">
            <img src="data:image/png;base64,{img_fringe}" />
            <div class="gallery-score">LATAM 5.88</div>
            <div class="gallery-overlay">
                <span class="gallery-badge badge-evolving">Ascendente</span>
                <div class="gallery-name">Fringe Motion</div>
                <div class="gallery-meta">Artisanal Sophistication · Dynamic Movement</div>
            </div>
        </div>

        <div class="gallery-item">
            <img src="data:image/png;base64,{img_visible}" />
            <div class="gallery-score">LATAM 6.94</div>
            <div class="gallery-overlay">
                <span class="gallery-badge badge-long">Permanencia</span>
                <div class="gallery-name">Visible Midriff</div>
                <div class="gallery-meta">Sensual Minimalism · Confident Sensuality</div>
            </div>
        </div>

        <div class="gallery-item">
            <img src="data:image/png;base64,{img_draped}" />
            <div class="gallery-score">LATAM 6.19</div>
            <div class="gallery-overlay">
                <span class="gallery-badge badge-long">Permanencia</span>
                <div class="gallery-name">Draped Elegance</div>
                <div class="gallery-meta">Quiet Luxury · Sophisticated Calm</div>
            </div>
        </div>

        <div class="gallery-item">
            <img src="data:image/png;base64,{img_layered}" />
            <div class="gallery-score">LATAM 2.08</div>
            <div class="gallery-overlay">
                <span class="gallery-badge badge-microtrend">Declive</span>
                <div class="gallery-name">Layered Volume</div>
                <div class="gallery-meta">Romantic Volume · Editorial Romance</div>
            </div>
        </div>

        <div class="gallery-item">
            <img src="data:image/png;base64,{img_mob}" />
            <div class="gallery-score">LATAM 3.41</div>
            <div class="gallery-overlay">
                <span class="gallery-badge badge-microtrend">Declive</span>
                <div class="gallery-name">Mob Wife Aesthetic</div>
                <div class="gallery-meta">Luxury Excess · Opulent Drama</div>
            </div>
        </div>

    </div>
    """, height=500)

elif selected == "Estéticas":

    df_latam = df.sort_values("latam_survival_score", ascending=False)
    st.markdown('<div class="section-title">ESTÉTICAS QUE SOBREVIVEN</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-text" style="max-width:780px;margin-bottom:32px;">
        No todas las tendencias globales tienen la misma resonancia en México y Latinoamérica.
        El <strong>LATAM Survival Score</strong> pondera compatibilidad climática, resonancia
        cultural, factor emocional y adaptabilidad urbana.
    </div>
    """, unsafe_allow_html=True)

    colE1, colE2, colE3 = st.columns(3)
    with colE1:
        best = df_latam.iloc[0]
        st.markdown(f'<div class="highlight-card" style="text-align:center;"><div class="highlight-category">Estética líder LATAM</div><div class="highlight-title">{best["trend_name"].title()}</div></div>', unsafe_allow_html=True)
    with colE2:
        surviving = len(df[df["trend_survival_type"] != "microtrend"])
        st.markdown(f'<div class="highlight-card" style="text-align:center;"><div class="highlight-category">Sobreviven en LATAM</div><div class="card-title" style="font-size:48px;">{surviving}</div></div>', unsafe_allow_html=True)
    with colE3:
        avg = round(df["latam_survival_score"].mean(), 2)
        st.markdown(f'<div class="highlight-card" style="text-align:center;"><div class="highlight-category">Score promedio LATAM</div><div class="card-title" style="font-size:48px;">{avg}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="card-category" style="margin-bottom:14px;margin-top:40px;">RANKING — LATAM SURVIVAL SCORE</div>', unsafe_allow_html=True)

    tabla = df_latam[["trend_name","latam_survival_score","trend_survival_type","climate_fit","color_primary","mood_aesthetic"]].copy()
    tabla.columns = ["Tendencia","LATAM Score","Tipo","Clima","Color Principal","Mood"]
    tabla["Tendencia"] = tabla["Tendencia"].str.title()
    tabla["LATAM Score"] = tabla["LATAM Score"].round(2)

    def color_tipo(val):
        if val == "long_lasting": return "background-color:#d4edda;color:#1a472a;"
        elif val == "evolving": return "background-color:#fff3cd;color:#7d5a00;"
        else: return "background-color:#f8d7da;color:#7b1a24;"

    def color_score(val):
        if val >= 4: return "background-color:#2a2233;color:white;font-weight:600;"
        elif val >= 2.5: return "background-color:#9f3b21;color:white;"
        else: return "background-color:#efe7dc;color:#5c524d;"

    styled = (
        tabla.style
        .applymap(color_tipo, subset=["Tipo"])
        .applymap(color_score, subset=["LATAM Score"])
        .set_properties(**{"font-family":"Inter,sans-serif","font-size":"13px","padding":"10px 14px"})
        .set_table_styles([{"selector":"th","props":[("background-color","#5c001f"),("color","white"),("font-family","Inter,sans-serif"),("font-size","11px"),("letter-spacing","2px"),("text-transform","uppercase"),("padding","12px 14px")]}])
    )
    st.dataframe(styled, use_container_width=True, height=460)

    st.markdown('<div class="section-title" style="font-size:42px;margin-top:50px;">Top 3 Estéticas LATAM</div>', unsafe_allow_html=True)
    cols_top = st.columns(3)
    for i, (_, row) in enumerate(df_latam.head(3).iterrows()):
        with cols_top[i]:
            st.markdown(f"""
            <div class="highlight-card">
                <div class="highlight-category">{row['climate_fit'].upper()} — {row['trend_survival_type'].upper()}</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text">
                    <strong>Mood:</strong> {row['mood_aesthetic'].title()}<br>
                    <strong>Color:</strong> {row['color_primary'].title()}<br>
                    <strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}
                </div>
            </div>
            """, unsafe_allow_html=True)

elif selected == "Cultura":
    st.markdown('<div class="section-title">CULTURA</div>', unsafe_allow_html=True)
    st.write("Aquí irán análisis culturales.")

elif selected == "Laboratorio":
    st.markdown('<div class="section-title">LABORATORIO</div>', unsafe_allow_html=True)
    st.write("Aquí irá el trend generator.")

elif selected == "Noticias":
    st.markdown('<div class="section-title">NOTICIAS</div>', unsafe_allow_html=True)
    st.write("Aquí irán noticias editoriales.")
