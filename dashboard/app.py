import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import base64
import os

st.set_page_config(page_title="COORDENADA MX", layout="wide")

BASE_DIR = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(BASE_DIR, "fashion_trends_final.csv"))

def img_to_base64(filename):
    with open(os.path.join(BASE_DIR, filename), "rb") as f:
        return base64.b64encode(f.read()).decode()

def img_tag(filename, style="width:100%;border-radius:8px;"):
    b64 = img_to_base64(filename)
    return f'<img src="data:image/png;base64,{b64}" style="{style}"/>'

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
.stApp { background-color: #f5f1ea; }
.block-container { padding-top: 2rem; padding-left: 4rem; padding-right: 4rem; }
.main-title { font-size: 82px; font-weight: 700; color: #2a2233; margin-bottom: 0; font-family: 'Cormorant Garamond', serif; line-height: 0.95; }
.subtitle { font-size: 14px; color: #8a7d74; margin-top: 8px; margin-bottom: 40px; letter-spacing: 4px; text-transform: uppercase; font-family: 'Inter', sans-serif; }
.section-title { font-size: 58px; font-family: 'Cormorant Garamond', serif; color: #2a2233; margin-top: 40px; margin-bottom: 30px; }
.card-category { font-size: 11px; letter-spacing: 3px; text-transform: uppercase; color: #7d7068; font-family: 'Inter', sans-serif; margin-top: 20px; margin-bottom: 10px; }
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

# =========================================
# INICIO
# =========================================

if selected == "Inicio":

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(img_tag("ImagenHero.png", "width:100%;border-radius:8px;"), unsafe_allow_html=True)
        st.markdown("""
        <div style="position:relative;margin-top:-85px;margin-left:28px;z-index:10;">
            <div style="background:rgba(208,190,162,0.95);padding:16px 28px;display:inline-block;
                font-family:'Inter',sans-serif;font-size:13px;letter-spacing:4px;text-transform:uppercase;color:white;">
                001 | IDENTIDAD RAÍZ
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(img_tag("ImagenTelas.png", "width:100%;border-radius:8px;"), unsafe_allow_html=True)
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

# =========================================
# TENDENCIAS
# =========================================

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
    fig.add_trace(go.Scatter(x=x, y=asc, fill='tozeroy', fillcolor='rgba(207,188,160,0.35)', line=dict(color='#cfbca0', width=2), name='Ascendente', hoverinfo='skip'))
    fig.add_trace(go.Scatter(x=x, y=perm, fill='tozeroy', fillcolor='rgba(92,0,31,0.25)', line=dict(color='#5c001f', width=2.5), name='Permanencia', hoverinfo='skip'))
    fig.add_trace(go.Scatter(x=x, y=evan, fill='tozeroy', fillcolor='rgba(90,84,80,0.2)', line=dict(color='#8a7d74', width=1.5), name='Evanescencia', hoverinfo='skip'))

    top_asc  = ascendente.iloc[0]
    top_perm = permanencia.iloc[0]
    top_evan = evanescencia.iloc[0]

    fig.add_annotation(x=2.5, y=2.8, text=f"<b>{top_asc['trend_name'].title()}</b><br>+{int(top_asc['growth_percent'])}%" if top_asc['growth_percent'] > 0 else f"<b>{top_asc['trend_name'].title()}</b>", showarrow=False, font=dict(family="Inter", size=11, color="#2a2233"), bgcolor="rgba(245,241,234,0.9)", borderpad=6)
    fig.add_annotation(x=5.5, y=3.8, text=f"<b>{top_perm['trend_name'].title()}</b><br>+{int(top_perm['growth_percent'])}%" if top_perm['growth_percent'] > 0 else f"<b>{top_perm['trend_name'].title()}</b>", showarrow=False, font=dict(family="Inter", size=11, color="white"), bgcolor="rgba(92,0,31,0.85)", borderpad=6)
    fig.add_annotation(x=8.5, y=2.1, text=f"<b>{top_evan['trend_name'].title()}</b>", showarrow=False, font=dict(family="Inter", size=11, color="#5c524d"), bgcolor="rgba(245,241,234,0.9)", borderpad=6)

    fig.add_vline(x=4, line_dash="dot", line_color="rgba(42,34,51,0.2)", line_width=1)
    fig.add_vline(x=7, line_dash="dot", line_color="rgba(42,34,51,0.2)", line_width=1)

    fig.add_annotation(x=1.5, y=4.2, text="ASCENDENTE <i>(Lo que viene)</i>", showarrow=False, font=dict(family="Inter", size=10, color="#7d7068"), xanchor="left")
    fig.add_annotation(x=4.2, y=4.2, text="PERMANENCIA <i>(Lo que se queda)</i>", showarrow=False, font=dict(family="Inter", size=10, color="#5c001f"), xanchor="left")
    fig.add_annotation(x=7.2, y=4.2, text="EVANESCENCIA <i>(Lo que se va)</i>", showarrow=False, font=dict(family="Inter", size=10, color="#8a7d74"), xanchor="left")

    fig.update_layout(height=320, margin=dict(l=0, r=0, t=40, b=20), paper_bgcolor='#f5f1ea', plot_bgcolor='#f5f1ea', showlegend=False,
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False, title=dict(text="TIEMPO →", font=dict(family="Inter", size=10, color="#8a7d74"))),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, title=dict(text="PREDICCIÓN DE MERCADO", font=dict(family="Inter", size=10, color="#8a7d74"))),
        font=dict(family="Inter"))

    st.plotly_chart(fig, use_container_width=True)

    col_a, col_p, col_e = st.columns(3)

    with col_a:
        st.markdown('<div style="font-family:Inter,sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#cfbca0;margin-bottom:16px;">▲ ASCENDENTE — Crece / Lo que viene</div>', unsafe_allow_html=True)
        for _, row in ascendente.head(2).iterrows():
            growth = f"+{int(row['growth_percent'])}%" if row['growth_percent'] > 0 else "—"
            st.markdown(f"""<div class="highlight-card" style="border-left:3px solid #cfbca0;">
                <div class="highlight-category">Tendencia emergente</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text"><strong>Macrotendencia:</strong> {row['macrotrend'].title()}<br><strong>Crecimiento:</strong> {growth}<br><strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}<br><strong>Mood estético:</strong> {row['mood_aesthetic'].title()}</div>
            </div>""", unsafe_allow_html=True)

    with col_p:
        st.markdown('<div style="font-family:Inter,sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#5c001f;margin-bottom:16px;">● PERMANENCIA — Se queda / El núcleo</div>', unsafe_allow_html=True)
        for _, row in permanencia.head(2).iterrows():
            growth = f"+{int(row['growth_percent'])}%" if row['growth_percent'] > 0 else "—"
            st.markdown(f"""<div class="highlight-card" style="border-left:3px solid #5c001f;">
                <div class="highlight-category">Tendencia consolidada</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text"><strong>Macrotendencia:</strong> {row['macrotrend'].title()}<br><strong>Crecimiento:</strong> {growth}<br><strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}<br><strong>Survival Score:</strong> {round(row['survival_score'], 2)}</div>
            </div>""", unsafe_allow_html=True)

    with col_e:
        st.markdown('<div style="font-family:Inter,sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#8a7d74;margin-bottom:16px;">▼ EVANESCENCIA — Se va / Declive</div>', unsafe_allow_html=True)
        for _, row in evanescencia.head(2).iterrows():
            st.markdown(f"""<div class="highlight-card" style="border-left:3px solid #8a7d74;">
                <div class="highlight-category">En declive</div>
                <div class="highlight-title">{row['trend_name'].title()}</div>
                <div class="highlight-text"><strong>Macrotendencia:</strong> {row['macrotrend'].title()}<br><strong>LATAM Score:</strong> {round(row['latam_survival_score'], 2)}<br><strong>Mood estético:</strong> {row['mood_aesthetic'].title()}<br><strong>Tipo:</strong> Microtendencia</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="background:#2a2233;border-radius:12px;padding:20px 28px;margin-top:32px;font-family:'Inter',sans-serif;font-size:13px;color:rgba(255,255,255,0.75);letter-spacing:0.5px;line-height:1.8;">
        <span style="color:#cfbca0;letter-spacing:3px;font-size:10px;text-transform:uppercase;">CM-FORECAST INSIGHT</span><br>
        Europa propone el concepto, pero el territorio dicta la supervivencia. Nuestro modelo no copia el entorno europeo — predice su mutación genética al chocar con el mercado latinoamericano.
    </div>""", unsafe_allow_html=True)

    img_coquette = img_to_base64("COQUETTE AESTHETIC.png")
    img_fringe   = img_to_base64("FRINGE MOTION.png")
    img_visible  = img_to_base64("VISIBLE MIDRIFF.png")
    img_draped   = img_to_base64("DRAPED ELEGANCE.png")
    img_layered  = img_to_base64("LAYERED VOLUME.png")
    img_mob      = img_to_base64("MOB WIFE AESTHETIC.png")

    components.html(f"""
    <style>
        * {{ margin:0;padding:0;box-sizing:border-box; }}
        body {{ background:transparent;font-family:'Inter',sans-serif; }}
        .gallery {{ display:flex;gap:8px;margin-top:40px;height:480px; }}
        .gallery-item {{ position:relative;overflow:hidden;border-radius:12px;cursor:pointer;transition:flex 0.5s cubic-bezier(0.4,0,0.2,1);flex:1; }}
        .gallery-item:hover {{ flex:3.5; }}
        .gallery-item img {{ width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform 0.5s ease; }}
        .gallery-item:hover img {{ transform:scale(1.03); }}
        .gallery-overlay {{ position:absolute;bottom:0;left:0;right:0;background:linear-gradient(to top,rgba(0,0,0,0.85) 0%,rgba(0,0,0,0.3) 60%,transparent 100%);padding:24px 18px 18px;opacity:0;transition:opacity 0.4s ease;border-radius:0 0 12px 12px; }}
        .gallery-item:hover .gallery-overlay {{ opacity:1; }}
        .gallery-badge {{ display:inline-block;padding:4px 10px;border-radius:20px;font-size:9px;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;font-weight:600; }}
        .badge-evolving {{ background:rgba(207,188,160,0.9);color:#2a2233; }}
        .badge-long {{ background:rgba(92,0,31,0.9);color:white; }}
        .badge-microtrend {{ background:rgba(90,84,80,0.9);color:white; }}
        .gallery-name {{ font-family:'Cormorant Garamond',serif;font-size:22px;font-weight:700;color:white;line-height:1;margin-bottom:6px; }}
        .gallery-meta {{ font-size:11px;color:rgba(255,255,255,0.7);letter-spacing:1px; }}
        .gallery-score {{ position:absolute;top:14px;right:14px;background:rgba(245,241,234,0.92);padding:6px 10px;border-radius:6px;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#2a2233;font-weight:600;opacity:0;transition:opacity 0.4s ease; }}
        .gallery-item:hover .gallery-score {{ opacity:1; }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <div class="gallery">
        <div class="gallery-item"><img src="data:image/png;base64,{img_coquette}" /><div class="gallery-score">LATAM 6.21</div><div class="gallery-overlay"><span class="gallery-badge badge-evolving">Ascendente</span><div class="gallery-name">Coquette Aesthetic</div><div class="gallery-meta">Romantic Revival · Hyper Femininity</div></div></div>
        <div class="gallery-item"><img src="data:image/png;base64,{img_fringe}" /><div class="gallery-score">LATAM 5.88</div><div class="gallery-overlay"><span class="gallery-badge badge-evolving">Ascendente</span><div class="gallery-name">Fringe Motion</div><div class="gallery-meta">Artisanal Sophistication · Dynamic Movement</div></div></div>
        <div class="gallery-item"><img src="data:image/png;base64,{img_visible}" /><div class="gallery-score">LATAM 6.94</div><div class="gallery-overlay"><span class="gallery-badge badge-long">Permanencia</span><div class="gallery-name">Visible Midriff</div><div class="gallery-meta">Sensual Minimalism · Confident Sensuality</div></div></div>
        <div class="gallery-item"><img src="data:image/png;base64,{img_draped}" /><div class="gallery-score">LATAM 6.19</div><div class="gallery-overlay"><span class="gallery-badge badge-long">Permanencia</span><div class="gallery-name">Draped Elegance</div><div class="gallery-meta">Quiet Luxury · Sophisticated Calm</div></div></div>
        <div class="gallery-item"><img src="data:image/png;base64,{img_layered}" /><div class="gallery-score">LATAM 2.08</div><div class="gallery-overlay"><span class="gallery-badge badge-microtrend">Declive</span><div class="gallery-name">Layered Volume</div><div class="gallery-meta">Romantic Volume · Editorial Romance</div></div></div>
        <div class="gallery-item"><img src="data:image/png;base64,{img_mob}" /><div class="gallery-score">LATAM 3.41</div><div class="gallery-overlay"><span class="gallery-badge badge-microtrend">Declive</span><div class="gallery-name">Mob Wife Aesthetic</div><div class="gallery-meta">Luxury Excess · Opulent Drama</div></div></div>
    </div>
    """, height=520)

# =========================================
# ESTÉTICAS
# =========================================

elif selected == "Estéticas":
# Top 3 tropicalizado
    st.markdown('<div class="section-title" style="font-size:42px;margin-top:50px;">Top 3 Estéticas LATAM</div>', unsafe_allow_html=True)

    img_vis_trop  = img_to_base64("VISIBLE MIDRIFF TROPICALIZADA.png")
    img_coq_trop  = img_to_base64("COQUETTE AESTHETIC TROPICALIZADA.png")
    img_drap_trop = img_to_base64("DRAPED ELEGANCE TROPICALIZADA.png")

    top3_data = [
        {
            "img": img_vis_trop,
            "nombre": "Visible Midriff",
            "tipo": "LONG LASTING",
            "score": "6.94",
            "macro": "Sensual Minimalism",
            "mood": "Confident Sensuality",
            "color": "#5c001f",
        },
        {
            "img": img_coq_trop,
            "nombre": "Coquette Aesthetic",
            "tipo": "EVOLVING",
            "score": "6.21",
            "macro": "Romantic Revival",
            "mood": "Hyper Femininity",
            "color": "#cfbca0",
        },
        {
            "img": img_drap_trop,
            "nombre": "Draped Elegance",
            "tipo": "LONG LASTING",
            "score": "6.19",
            "macro": "Quiet Luxury",
            "mood": "Sophisticated Calm",
            "color": "#5c001f",
        },
    ]

    cols_top = st.columns(3)
    for i, (col, data) in enumerate(zip(cols_top, top3_data)):
        with col:
            st.markdown(f"""
            <div style="border-radius:16px;overflow:hidden;margin-bottom:8px;">
                <img src="data:image/png;base64,{data['img']}"
                    style="width:100%;height:320px;object-fit:cover;object-position:center top;border-radius:16px;display:block;"/>
            </div>
            <div class="highlight-card" style="border-top:3px solid {data['color']};margin-top:0;border-radius:0 0 16px 16px;">
                <div class="highlight-category">{data['tipo']} — LATAM {data['score']}</div>
                <div class="highlight-title">{data['nombre']}</div>
                <div class="highlight-text">
                    <strong>Macrotendencia:</strong> {data['macro']}<br>
                    <strong>Mood estético:</strong> {data['mood']}<br>
                    <strong>LATAM Score:</strong> {data['score']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            # --- GRÁFICA DE BURBUJAS ---
    import plotly.express as px
    import plotly.graph_objects as go

    st.markdown("""
    <div class="section-title" style="font-size:42px;margin-top:50px;">
    Mapa de Permanencia LATAM
    </div>
    <div class="card-text" style="max-width:780px;margin-bottom:32px;">
        Cada burbuja representa una tendencia. El tamaño indica su factor emocional,
        el eje X su compatibilidad urbana en México y el eje Y su score de permanencia LATAM.
    </div>
    """, unsafe_allow_html=True)

    bubble_df = df.copy()

    color_map = {
        "long_lasting": "#5c001f",
        "evolving":     "#cfbca0",
        "microtrend":   "#8a7d74"
    }

    label_map = {
        "long_lasting": "Permanencia",
        "evolving":     "Ascendente",
        "microtrend":   "Declive"
    }

    bubble_df["tipo_label"] = bubble_df["trend_survival_type"].map(label_map)
    bubble_df["color"]      = bubble_df["trend_survival_type"].map(color_map)
    bubble_df["nombre"]     = bubble_df["trend_name"].str.title()

    fig2 = go.Figure()

    for tipo, grupo in bubble_df.groupby("trend_survival_type"):
        fig2.add_trace(go.Scatter(
            x=grupo["urban_compatibility_mexico"],
            y=grupo["latam_survival_score"],
            mode="markers",
            name=label_map[tipo],
            text=grupo["nombre"],
            textposition="top center",
            textfont=dict(family="Inter", size=10, color="#2a2233"),
            marker=dict(
                size=grupo["emotional_factor"] * 5,
                color=color_map[tipo],
                opacity=0.85,
                line=dict(width=1.5, color="white")
            ),
            hovertemplate=(
                "<b>%{text}</b><br>"
                "Urban Compatibility: %{x}<br>"
                "LATAM Score: %{y:.2f}<br>"
                "<extra></extra>"
            )
        ))

    fig2.update_layout(
        height=480,
        margin=dict(l=20, r=20, t=40, b=40),
        paper_bgcolor='#f5f1ea',
        plot_bgcolor='#efe7dc',
        font=dict(family="Inter"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=11, family="Inter"),
        ),
        xaxis=dict(
            title=dict(text="Compatibilidad Urbana México →", font=dict(family="Inter", size=11, color="#8a7d74")),
            showgrid=True,
            gridcolor="rgba(138,125,116,0.15)",
            zeroline=False,
        ),
        yaxis=dict(
            title=dict(text="LATAM Survival Score →", font=dict(family="Inter", size=11, color="#8a7d74")),
            showgrid=True,
            gridcolor="rgba(138,125,116,0.15)",
            zeroline=False,
        ),
    )

    st.plotly_chart(fig2, use_container_width=True)

elif selected == "Cultura":
    st.markdown('<div class="section-title">CULTURA</div>', unsafe_allow_html=True)
    st.write("Aquí irán análisis culturales.")

elif selected == "Laboratorio":
    st.markdown('<div class="section-title">LABORATORIO</div>', unsafe_allow_html=True)
    st.write("Aquí irá el trend generator.")

elif selected == "Noticias":
    st.markdown('<div class="section-title">NOTICIAS</div>', unsafe_allow_html=True)
    st.write("Aquí irán noticias editoriales.")

# =========================================
# FOOTER
# =========================================

st.markdown("""
<div style="
    background-color: #2a2233;
    margin-top: 80px;
    padding: 52px 64px 36px 64px;
">
    <div style="
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 48px;
        margin-bottom: 48px;
    ">

        <!-- Columna 1: Branding -->
        <div>
            <div style="
                font-family: 'Cormorant Garamond', serif;
                font-size: 28px;
                font-weight: 700;
                color: white;
                letter-spacing: 2px;
                margin-bottom: 16px;
            ">
                COORDENADA MX
            </div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 13px;
                color: rgba(255,255,255,0.55);
                line-height: 1.8;
                max-width: 280px;
            ">
                Inteligencia cultural latinoamericana aplicada al forecast de tendencias.
                Modelo probabilístico de supervivencia estética para el mercado mexicano.
            </div>
            <div style="margin-top:24px;">
                <span style="
                    font-family: 'Inter', sans-serif;
                    font-size: 10px;
                    letter-spacing: 3px;
                    text-transform: uppercase;
                    color: #cfbca0;
                ">
                    EDICIÓN 01 — PRIMAVERA VERANO 2026
                </span>
            </div>
        </div>

        <!-- Columna 2: Navegación -->
        <div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 11px;
                letter-spacing: 3px;
                text-transform: uppercase;
                color: #cfbca0;
                margin-bottom: 20px;
            ">
                Plataforma
            </div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 13px;
                color: rgba(255,255,255,0.6);
                line-height: 2.2;
            ">
                Inicio<br>
                Tendencias<br>
                Estéticas<br>
                Cultura<br>
                Laboratorio<br>
                Noticias
            </div>
        </div>

        <!-- Columna 3: Contacto -->
        <div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 11px;
                letter-spacing: 3px;
                text-transform: uppercase;
                color: #cfbca0;
                margin-bottom: 20px;
            ">
                Contacto
            </div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 13px;
                color: rgba(255,255,255,0.6);
                line-height: 2.2;
            ">
                contacto@coordenadamx.com<br>
                Consultoría Privada<br>
                Trabaja con nosotros<br>
                Forecast Q2 2026
            </div>
        </div>

        <!-- Columna 4: Legal -->
        <div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 11px;
                letter-spacing: 3px;
                text-transform: uppercase;
                color: #cfbca0;
                margin-bottom: 20px;
            ">
                Legal
            </div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-size: 13px;
                color: rgba(255,255,255,0.6);
                line-height: 2.2;
            ">
                Términos de Servicio<br>
                Política de Privacidad<br>
                Créditos<br>
                © 2026 Coordenada MX
            </div>
        </div>

    </div>

    <!-- Línea divisoria -->
    <div style="
        height: 1px;
        background: rgba(255,255,255,0.1);
        margin-bottom: 24px;
    "></div>

    <!-- Bottom bar -->
    <div style="
        display: flex;
        justify-content: space-between;
        align-items: center;
    ">
        <div style="
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            color: rgba(255,255,255,0.3);
            letter-spacing: 2px;
        ">
            COORDENADA MX — INTELIGENCIA CULTURAL LATINOAMERICANA
        </div>
        <div style="
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            color: rgba(255,255,255,0.3);
            letter-spacing: 1px;
        ">
            Modelo probabilístico desarrollado con datos de TikTok, Pinterest, Google Trends, Vogue y Zara
        </div>
    </div>

</div>
""", unsafe_allow_html=True)
