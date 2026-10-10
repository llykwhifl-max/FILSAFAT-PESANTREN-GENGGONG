import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN & TEMA WARNA
# ==========================================
st.set_page_config(
    page_title="Filsafat Ilmu Pesantren Genggong",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS untuk nuansa hijau gelap khas pesantren (Emerald & Dark Green)
st.markdown(
    """
    <style>
    /* Global Styling */
    .main {
        background-color: #0f251e;
        color: #f0fdf4;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #081c15;
        border-right: 1px solid #1b4332;
    }
    section[data-testid="stSidebar"] .css-17eq0hr, section[data-testid="stSidebar"] span {
        color: #d8f3dc;
    }

    /* Card / Container Styling */
    .stCard {
        background-color: #1b4332;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #2d6a4f;
        margin-bottom: 15px;
    }

    /* Headers */
    h1, h2, h3 {
        color: #52b788 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2d6a4f;
        color: white;
        border-radius: 8px;
        border: 1px solid #52b788;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #40916c;
        color: #ffffff;
        border-color: #74c69d;
    }

    /* Success / Error override for dark theme */
    div.stSuccess {
        background-color: #1b4332;
        color: #d8f3dc;
        border: 1px solid #52b788;
    }
    div.stError {
        background-color: #381d1a;
        color: #ffd8d8;
        border: 1px solid #e05353;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# NAVIGASI UTAMA (SIDEBAR)
# ==========================================
st.sidebar.markdown(
    "<h2 style='text-align: center; color: #52b788;'>🌿 Pesantren Genggong</h2>",
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    "<p style='text-align: center; font-size: 0.9em; color: #b7e4c7;'>Filsafat Ilmu & Budaya Pendidikan</p>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Pilih Menu Navigasi:",
    ["📖 1. Menu Materi", "⚖️ 2. Studi Kasus", "🎯 3. Kuis Interaktif"],
)

# ==========================================
# 1. MENU MATERI
# ==========================================
if menu == "📖 1. Menu Materi":
    st.title("📖 Materi Filsafat Ilmu & Budaya Pendidikan")
    st.markdown(
        "Kajian epistemologis, ontologis, aksiologis, dan orientasi kultural di lingkungan **Pesantren Zainul Hasan Genggong**."
    )
    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["3.1 Ontologi", "3.2 Epistemologi", "3.3 Aksiologi", "3.6 Orientasi"]
    )

    with tab1:
        st.subheader(
            "3.1 Ontologi: Hakikat Objek Material & Formal Pesantren Genggong"
        )
        st.markdown(
            """
            Dalam perspektif ontologis, Pesantren Zainul Hasan Genggong memandang realitas semesta dan pendidikan secara komprehensif (*tauhidic worldview*):
            * **Objek Material:** Seluruh aspek kehidupan manusia—baik dimensi jasmaniah, akal pikiran, spiritualitas santri, maupun tata kelola ekosistem sosial di dalam dan luar pesantren.
            * **Objek Formal:** Hakikat ilmu pengetahuan yang bersumber dari ayat-ayat qauliyah (Al-Qur'an & Hadis) dan ayat-ayat kauniyah (fenomena alam & sosial), yang bermuara pada pengenalan (ma'rifat) dan pengabdian mutlak kepada Allah SWT.
            """
        )

    with tab2:
        st.subheader("3.2 Epistemologi: Metode Valid Memperoleh Ilmu")
        st.markdown(
            """
            Cara valid santri memperoleh, menguji, and membangun bangunan ilmu pengetahuan di Genggong bertumpu pada tradisi keilmuan salaf yang mapan:
            1. **Sorogan:** Metode individual di mana santri menghadap kiai/ustaz untuk membaca dan menyetorkan hafalan/kitab kuning secara personal, menjamin validitas pemahaman secara langsung (*sanad* bersambung).
            2. **Bandongan (Wetonan):** Metode kolektif di mana kiai membaca kitab dan santri menyimak serta memaknai (*gandul*) di kitab masing-masing, membangun kerangka pemahaman komunal yang sistematis.
            3. **Bahtsul Masa'il:** Forum dialektika kritis dan komparatif untuk memecahkan problematika kontemporer menggunakan metodologi ushul fiqh dan kaidah qawa'id fiqhiyyah yang ketat secara ilmiah.
            """
        )

    with tab3:
        st.subheader(
            "3.3 Aksiologi: Nilai Kemanfaatan Ilmu ('Satlogi Santri')"
        )
        st.markdown(
            "Aksiologi mengkaji dimensi nilai guna ilmu. Di Pesantren Genggong, orientasi nilai ini dirumuskan secara operasional dalam **Satlogi Santri**:"
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                * **1. Sopan Santun:** Menjunjung tinggi adab di atas ilmu pengetahuan.
                * **2. Ajeg / Istiqamah:** Konsistensi dalam beribadah, belajar, dan berbuat kebajikan.
                * **3. Nasehat:** Keterbukaan menerima bimbingan serta saling menasihati dalam kebenaran.
                """
            )
        with col2:
            st.markdown(
                """
                * **4. Taqwallah:** Landasan takwa sebagai tolok ukur kemuliaan insan.
                * **5. Ridlallah:** Orientasi akhir setiap amal semata-mata mencari rida Allah.
                * **6. Ikhlas Lillahi Ta'ala:** Pembebasan motif transaksional duniawi dalam beramal.
                """
            )

    with tab4:
        st.subheader(
            "3.6 Orientasi: Pola Adaptif Pesantren Menghadapi Zaman Modern"
        )
        st.markdown(
            """
            Pesantren Genggong memegang teguh kaidah ushul fiqh yang legendaris:
            > *Al-Muhafadzah 'ala al-qadimi al-shalih wa al-akhdu bi al-jadidi al-aslah*
            > (Melestarikan tradisi lama yang baik dan mengambil tradisi baru yang lebih maslahat).
            
            Pola adaptif ini terwujud dalam integrasi kurikulum kepesantrenan salaf dengan pendidikan formal modern, penguasaan teknologi digital, dan penguatan kemandirian ekonomi santri tanpa kehilangan ruh spiritualitas dan akar kulturalnya.
            """
        )

# ==========================================
# 2. MENU STUDI KASUS
# ==========================================
elif menu == "⚖️ 2. Studi Kasus":
    st.title("⚖️ Analisis Studi Kasus & Problem Solving Filosofis")
    st.markdown(
        "Kajian kasus nyata untuk melatih ketajaman berpikir kritis santri dan akademisi dalam menimbang aspek epistemologis, aksiologis, dan adab."
    )
    st.markdown("---")

    # Kasus 1
    with st.expander(
        "📌 Kasus 1: Sorogan vs Chat-GPT (Tantangan Epistemologi)", expanded=True
    ):
        st.markdown(
            """
            **Deskripsi Masalah:**  
            Seorang santri milenial menggunakan *Artificial Intelligence* (Chat-GPT) untuk merangkum kitab kuning dan mencari hukum fiqh secara instan tanpa melalui proses *talaqqi* (bimbingan langsung) dan membaca teks Arab asli dengan bimbingan guru.
            
            **Pertanyaan Filosofis (Epistemologi):**  
            Bagaimana validitas sanad keilmuan dan otoritas kebenaran teks yang diperoleh dari mesin dibandingkan dengan metode *Sorogan* yang memiliki mata rantai guru (*sanad*) hingga Rasulullah SAW?
            
            **Refleksi Pemecahan Masalah:**  
            AI berfungsi sebagai alat bantu (*tool*) percepatan informasi, namun bukan pemegang otoritas keilmuan (*sanad*). Validitas epistemologis dalam tradisi pesantren mensyaratkan adanya interaksi guru-murid untuk menghindari distorsi makna dan menjaga integritas spiritual (barokah ilmu).
            """
        )

    # Kasus 2
    with st.expander("📌 Kasus 2: Ikhlas vs Nilai Ujian (Dilema Aksiologi)"):
        st.markdown(
            """
            **Deskripsi Masalah:**  
            Sistem pendidikan formal menuntut perankingan, nilai angka (skor), dan ijazah sebagai legitimasi prestasi belajar. Di sisi lain, nilai *Aksiologi* pesantren menuntut orientasi ikhlas semata-mata karena Allah (*Lillahi Ta'ala*) tanpa orientasi transaksional pujian atau materi.
            
            **Pertanyaan Filosofis (Aksiologi):**  
            Bagaimana menyelaraskan orientasi nilai ukhrawi (keikhlasan) dengan tuntutan administratif pendidikan modern yang berbasis kompetisi kuantitatif?
            
            **Refleksi Pemecahan Masalah:**  
            Nilai ujian dipandang bukan sebagai tujuan akhir (*goal*), melainkan sebagai indikator objektivitas ikhtiyar maksimal (profesionalisme). Keikhlasan dijaga dengan meniatkan pencapaian nilai terbaik tersebut sebagai bentuk khidmat dan amanah keilmuan yang bermanfaat bagi sesama.
            """
        )

    # Kasus 3
    with st.expander(
        "📌 Kasus 3: Kritis vs Sopan Santun (Batasan Adab & Kebebasan Berpikir)"
    ):
        st.markdown(
            """
            **Deskripsi Masalah:**  
            Era informasi terbuka memicu budaya dekonstruksi berpikir di kalangan remaja. Sebagian santri mempertanyakan kebijakan pengasuh atau dawuh kiai dengan gaya argumentasi bebas yang terkesan menyamakan posisi guru dan murid layaknya debat kusir di media sosial.
            
            **Pertanyaan Filosofis (Etika & Epistemologi):**  
            Di mana titik keseimbangan antara kebebasan berpikir kritis dalam diskursus ilmiah dengan prinsip *Sopan Santun* dalam Satlogi Santri?
            
            **Refleksi Pemecahan Masalah:**  
            Kritik dan dialektika sangat dianjurkan dalam tradisi bahtsul masa'il, namun harus diletakkan dalam koridor *adab* (etika). Ilmu tanpa adab kehilangan nilai keberkahannya. Berpikir kritis harus santun, konstruktif, dan dilandasi rasa takzim kepada pemilik otoritas ilmu.
            """
        )

# ==========================================
# 3. MENU KUIS INTERAKTIF
# ==========================================
elif menu == "🎯 3. Kuis Interaktif":
    st.title("🎯 Kuis Interaktif Filsafat Ilmu & Budaya Genggong")
    st.markdown(
        "Uji pemahaman Anda mengenai materi ontologi, epistemologi, aksiologi, dan orientasi kultural Pesantren Genggong."
    )
    st.markdown("---")

    # Inisialisasi session state untuk menyimpan status jawaban kuis
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    with st.form("quiz_form"):
        # Soal 1
        st.markdown("### Soal 1: Ontologi")
        q1 = st.radio(
            "Dalam ontologi Islam, hakikat wujud tertinggi dan sumber dari segala realitas semesta alam bersumber pada:",
            (
                "A. Hukum kausalitas alam semesta semata",
                "B. Kemutlakan wujud Allah SWT",
                "C. Eksistensi akal pikiran manusia",
                "D. Konsensus sosial masyarakat",
            ),
            key="q1",
        )

        st.markdown("---")

        # Soal 2
        st.markdown("### Soal 2: Epistemologi")
        q2 = st.radio(
            "Metode Sorogan dan Bandongan di pesantren merupakan bagian dari kajian cabang filsafat ilmu mengenai cara memperoleh pengetahuan yang disebut:",
            ("A. Ontologi", "B. Aksiologi", "C. Epistemologi", "D. Kosmologi"),
            key="q2",
        )

        st.markdown("---")

        # Soal 3
        st.markdown("### Soal 3: Aksiologi")
        q3 = st.radio(
            "Konsep 'Satlogi Santri' (Sopan Santun, Ajeg, Nasehat, Taqwallah, Ridlallah, Ikhlas) secara filosofis paling erat kaitannya dengan cabang:",
            ("A. Epistemologi", "B. Aksiologi", "C. Logika Formal", "D. Ontologi"),
            key="q3",
        )

        st.markdown("---")

        # Soal 4
        st.markdown("### Soal 4: Orientasi Pesantren")
        q4 = st.radio(
            "Bagaimana sifat dasar pola adaptif Pesantren Genggong dalam menghadapi modernitas?",
            (
                "A. Menolak total seluruh unsur modernitas barat",
                "B. Mengganti seluruh tradisi salaf dengan sistem modern",
                "C. Adaptif dan bertahap dengan merawat tradisi lama yang baik serta mengambil hal baru yang lebih maslahat",
                "D. Bersikap pasif dan isolasionis terhadap perubahan zaman",
            ),
            key="q4",
        )

        st.markdown("")
        submit_btn = st.form_submit_button("Cek Jawaban Kuis")

    if submit_btn:
        score = 0
        total = 4

        # Validasi Jawaban
        correct_q1 = "B. Kemutlakan wujud Allah SWT"
        correct_q2 = "C. Epistemologi"
        correct_q3 = "B. Aksiologi"
        correct_q4 = (
            "C. Adaptif dan bertahap dengan merawat tradisi lama yang baik serta mengambil hal baru yang lebih maslahat"
        )

        results = []

        if q1 == correct_q1:
            score += 1
            results.append(
                (
                    True,
                    "Soal 1 Benar: Ontologi Islam menempatkan kemutlakan wujud Allah SWT sebagai sumber utama segala yang ada.",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 1 Salah: Hakikat wujud tertinggi dalam ontologi Islam adalah kemutlakan wujud Allah SWT.",
                )
            )

        if q2 == correct_q2:
            score += 1
            results.append(
                (
                    True,
                    "Soal 2 Benar: Sorogan dan Bandongan adalah metode dan sarana valid memperoleh ilmu, yang dibahas dalam Epistemologi.",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 2 Salah: Metode perolehan ilmu pengetahuan masuk ke dalam ranah Epistemologi.",
                )
            )

        if q3 == correct_q3:
            score += 1
            results.append(
                (
                    True,
                    "Soal 3 Benar: Satlogi Santri membahas nilai guna, moral, dan etika, yang merupakan cakupan dari Aksiologi.",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 3 Salah: Pembahasan tentang nilai dan moral (etika) adalah Aksiologi.",
                )
            )

        if q4 == correct_q4:
            score += 1
            results.append(
                (
                    True,
                    "Soal 4 Benar: Pesantren Genggong menerapkan prinsip al-muhafadzah 'ala al-qadimi al-shalih...",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 4 Salah: Pesantren bersifat adaptif dengan merawat tradisi salaf yang baik dan mengambil hal baru yang maslahat.",
                )
            )

        st.markdown("---")
        st.subheader(
            f"Hasil Kuis Anda: Skor {score} dari {total} ({score*25}%)"
        )

        if score == 4:
            st.balloons()
            st.success(
                "Luar Biasa! Anda memahami materi Filsafat Ilmu & Budaya Pesantren Genggong dengan sempurna."
            )
        elif score >= 2:
            st.success(
                "Bagus sekali! Pemahaman Anda sudah baik, silakan tinjau kembali beberapa materi pada menu utama."
            )
        else:
            st.error(
                "Tetap semangat! Mari pelajari ulang materi pada Menu Materi untuk memperdalam pemahaman."
            )

        for is_correct, explanation in results:
            if is_correct:
                st.success(explanation)
            else:
                st.error(explanation)

# ==========================================
# FOOTER
# ==========================================
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='text-align: center; font-size: 0.8em; color: #74c69d;'>© 2026 • Pesantren Zainul Hasan Genggong</p>",
    unsafe_allow_html=True,
)
