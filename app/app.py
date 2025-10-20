import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

min_15 = pd.read_csv(OUTPUT_DIR / 'ranking_tmin_top15_cold.csv')

top_15_districts = pd.read_csv(OUTPUT_DIR / 'ranking_tmin_top15_hot.csv')


def convert_for_download(df):
    return df.to_csv().encode("utf-8")

csv_min_15 = convert_for_download(min_15)
csv_top_15_districts = convert_for_download(top_15_districts)

# page title
st.set_page_config(page_title="Minimum-Temperature-Raster", layout="wide")


#  tabs
tab1, tab2, tab3 = st.tabs([' 🗂️ Data Descripion', ' 🗺️ Raster data analysis', ' 🌍 Public policy proposals '])


# tab 1: Data Description
with tab1:
    st.title('Descripción de los Datos')

    st.subheader("📌 Unidad de Análisis")

    st.write("**Análisis raster de temperaturas mínimas en el Perú**.")

    ## columnas de tab1
    a,b = st.columns(2)

    a.metric(label="Número de bandas", value="5", border= True)
    b.metric(label = '**Periodo de análisis**', value= '2020-2024', border= True)
    
    st.subheader("📊 Estadísticas por Banda")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("**Banda 1**")
        st.metric("Mín", "-9.05°C")
        st.metric("Máx", "24.64°C")
        st.metric("Media", "18.01°C")
    
    with col2:
        st.markdown("**Banda 2**")
        st.metric("Mín", "-10.02°C")
        st.metric("Máx", "24.39°C")
        st.metric("Media", "17.91°C")
    
    with col3:
        st.markdown("**Banda 3**")
        st.metric("Mín", "-9.87°C")
        st.metric("Máx", "24.21°C")
        st.metric("Media", "17.77°C")
    
    with col4:
        st.markdown("**Banda 4**")
        st.metric("Mín", "-9.06°C")
        st.metric("Máx", "24.12°C")
        st.metric("Media", "17.61°C")
    
    with col5:
        st.markdown("**Banda 5**")
        st.metric("Mín", "-8.85°C")
        st.metric("Máx", "24.15°C")
        st.metric("Media", "17.82°C")

# tab 2: Raster data analysis

with tab2:
    
    st.subheader('Análisis por Distrito')

    c, d = st.columns(2, border= False)

    with c:
        st.image(str(OUTPUT_DIR / 'hist_tmin.png'), width= 800)

    with d:
        st.image(str(OUTPUT_DIR / 'map_tmin_choropleth.png'), width= 800)


    e, f = st.columns(2, border= False)


    with e:
        st.write("### Distritos más fríos (Top 15)")
        st.download_button(
            label="📥 Descargar CSV", data= csv_min_15, file_name= 'Distritos más fríos (Top 15).csv')
        st.dataframe(min_15)

    with f:
        st.write("### Distritos frios más cálidos (Top 15)")
        st.download_button(
            label="📥 Descargar CSV", data= csv_top_15_districts, file_name= 'istritos frios más cálidos (Top 15).csv')
        st.dataframe(top_15_districts)


# tab 3: Public policy proposals
with tab3:
    st.header("💡 Propuestas de Política Pública: Intervenciones contra el Frío Extremo")
    
    st.markdown("""
    Basado en el análisis de temperatura mínima por distrito, se proponen **4 intervenciones prioritarias** 
    para zonas alto-andinas (Puno, Cusco, Tacna, Arequipa) y amazónicas (Loreto, Ucayali, Madre de Dios).
    """)
    
    # Resumen ejecutivo
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Inversión Total", "S/ 938 M", help="4 años")
    with col2:
        st.metric("Beneficiarios", "350,000", help="Directos")
    with col3:
        st.metric("Distritos Críticos", "95", help="Tmin < 1°C")
    with col4:
        st.metric("Reducción IRA", "-40%", help="Meta salud")
    
    st.markdown("---")
    
    # Propuesta 1: Viviendas Térmicas
    with st.expander("🏠 **PROPUESTA 1: Viviendas Térmicas** (Alto-Andina)", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Objetivo:** Reducir 40% los casos de IRA en niños <5 años y adultos >65 años.
            
            **Población objetivo:**
            - 15 distritos con Tmin < -0.3°C (Capazo, Susapaya, Tarata, Ticaco, Candarave, etc.)
            - 45,000 familias vulnerables
            
            **Intervención:**
            - Aislamiento térmico de paredes y techos
            - Cocinas mejoradas con chimenea
            - Kit de emergencia: 4 frazadas térmicas + ropa térmica infantil
            - Tambos/refugios térmicos comunales (1 cada 200 familias)
            - Sistema de alerta temprana de heladas (SMS/radio)
            """)
        
        with col2:
            st.markdown("""
            **💰 Costo:**
            - S/ 4,500/vivienda (básico)
            - S/ 8,000/vivienda (completo)
            - **Total: S/ 315 M** (3 años)
            
            **📊 KPIs:**
            - ✅ -40% IRA menores 5 años
            - ✅ -35% neumonías adultos mayores
            - ✅ -25% ausentismo escolar
            - ✅ +8°C temperatura interna nocturna
            """)
    
    # Propuesta 2: Agropecuaria
    with st.expander("🌾 **PROPUESTA 2: Anti-Heladas Agropecuarias** (Alto-Andina)"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Objetivo:** Reducir 50% pérdidas agrícolas y 30% mortalidad de camélidos por heladas.
            
            **Población objetivo:**
            - 80 distritos con Tmin < 1°C
            - 60,000 pequeños productores
            - 800,000 cabezas de alpacas/llamas
            
            **Intervención:**
            - **Agricultura:** Mallas protectoras, riego por aspersión nocturno, variedades resistentes
            - **Ganadería:** Mantas térmicas para crías, corrales techados, suplementación alimenticia
            - Capacitación: 100 promotores técnicos comunales
            """)
        
        with col2:
            st.markdown("""
            **💰 Costo:**
            - S/ 2,500/productor (agrícola)
            - S/ 3,200/familia (ganadero)
            - **Total: S/ 280 M** (4 años)
            
            **📊 KPIs:**
            - ✅ -50% pérdidas papa/quinua
            - ✅ -30% mortalidad crías alpaca
            - ✅ +25% ingresos familiares
            - ✅ 60,000 familias protegidas
            """)
    
    # Propuesta 3: Friajes Amazónicos
    with st.expander("🌴 **PROPUESTA 3: Protección Friajes Amazónicos** (Selva)"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Objetivo:** Reducir 60% complicaciones de salud durante friajes (Tmin < 12°C por ≥3 días).
            
            **Población objetivo:**
            - Comunidades nativas y rurales en Loreto, Ucayali, Madre de Dios
            - 120,000 personas (énfasis: pueblos indígenas)
            - 450 establecimientos de salud nivel I
            
            **Intervención:**
            - Red de 50 estaciones meteorológicas + alertas SMS/radio (15 lenguas nativas)
            - Kit familiar: 6 frazadas polares, mosquiteros térmicos, ropa térmica, combustible
            - 20 brigadas de respuesta rápida fluvial
            - Stock estratégico de medicamentos IRA en postas rurales
            """)
        
        with col2:
            st.markdown("""
            **💰 Costo:**
            - S/ 650/familia (kit básico)
            - S/ 18,000/estación meteorológica
            - S/ 95,000/brigada fluvial
            - **Total: S/ 145 M** (3 años)
            
            **📊 KPIs:**
            - ✅ 90% alertas con ≥72h anticipación
            - ✅ -60% hospitalizaciones IRA
            - ✅ 0 muertes por hipotermia
            - ✅ 120,000 personas protegidas
            """)
    
    # Propuesta 4: Escuelas
    with st.expander("🎒 **PROPUESTA 4: Escuelas Cálidas** (Andina + Amazónica)"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Objetivo:** Reducir 45% ausentismo escolar durante períodos de frío extremo.
            
            **Población objetivo:**
            - 800 instituciones educativas en zonas críticas (Tmin < 2°C andino, < 14°C amazónico)
            - 95,000 estudiantes primaria/secundaria
            - 3,500 docentes
            
            **Intervención:**
            - **Infraestructura:** Aislamiento térmico de aulas, ventanas dobles, calefacción solar pasiva
            - **Equipamiento:** 2 uniformes térmicos/estudiante, frazadas para aulas, comedores escolares
            - **Pedagógico:** Horarios flexibles, educación a distancia de emergencia (tablets 20% vulnerables)
            """)
        
        with col2:
            st.markdown("""
            **💰 Costo:**
            - S/ 8,500/aula (térmica)
            - S/ 180/uniforme térmico
            - S/ 35,000/comedor escolar
            - **Total: S/ 198 M** (4 años)
            
            **📊 KPIs:**
            - ✅ -45% ausentismo meses críticos
            - ✅ +0.8 pts en ECE
            - ✅ -35% IRA edad escolar
            - ✅ 95,000 estudiantes beneficiados
            """)
    
    st.markdown("---")
    
    # Tabla resumen
    st.subheader("📋 Resumen Presupuestal y Priorización")
    
    resumen_data = {
        'Propuesta': [
            '1. Viviendas Térmicas',
            '2. Anti-Heladas Agropecuarias',
            '3. Friajes Amazónicos',
            '4. Escuelas Cálidas'
        ],
        'Zona': ['Andes', 'Andes', 'Amazonía', 'Ambas'],
        'Inversión (S/ M)': [315, 280, 145, 198],
        'Beneficiarios': ['45,000 familias', '60,000 productores', '120,000 personas', '95,000 estudiantes'],
        'Plazo': ['3 años', '4 años', '3 años', '4 años'],
        'Prioridad': ['🔴 Alta', '🟡 Media', '🟡 Media', '🟢 Alta']
    }
    
    df_resumen = pd.DataFrame(resumen_data)
    st.dataframe(df_resumen, use_container_width=True, hide_index=True)
    
    # Financiamiento
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **💵 Fuentes de Financiamiento Sugeridas:**
        - 50% Tesoro Público (MIDIS, MINSA, MINEDU, MINAGRI)
        - 30% Gobiernos Regionales (canon, regalías)
        - 20% Cooperación internacional (BM, BID, fondos climáticos)
        """)
    
    with col2:
        st.markdown("""
        **⚡ Implementación Prioritaria 2026:**
        - **Fase 1:** 15 distritos con Tmin < -0.3°C (Propuesta 1)
        - **Fase 2:** Escuelas en zonas críticas (Propuesta 4)
        - **Fase 3:** Expansión agropecuaria y amazónica
        """)
    