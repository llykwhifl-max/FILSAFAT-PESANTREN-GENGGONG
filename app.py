import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN & TEMA WARNA
# ==========================================
st.set_page_config(
    page_title="Filsafat Ilmu & Pesantren Genggong",
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
    section[data-testid="stSidebar"] span {
        color: #d8f3dc;
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
    "<p style='text-align: center; font-size: 0.9em; color: #b7e4c7;'>Kajian Filsafat Ilmu & Pendidikan</p>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Pilih Menu Navigasi:",
    ["📖 1. Menu Materi", "⚖️ 2. Studi Kasus", "🎯 3. Kuis Interaktif (Mahasiswa)"],
)

# ==========================================
# 1. MENU MATERI (Sesuai 3.1 - 3.6 Jurnal)
# ==========================================
if menu == "📖 1. Menu Materi":
    st.title("📖 Materi Filsafat Ilmu & Pendidikan Pesantren")
    st.markdown(
        "Kajian ontologis, epistemologis, aksiologis, serta tujuan, nilai, dan orientasi pendidikan di **Pondok Pesantren Zainul Hasan Genggong**[span_0](start_span)[span_0](end_span)."
    )
    st.markdown("---")

    # Membuat 6 tab sesuai sub-bab naskah jurnal
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "3.1 Ontologi",
            "3.2 Epistimologi",
            "3.3 Aksiologi",
            "3.4 Hubungan Ketiga Landasan",
            "3.5 Tujuan Pendidikan",
            "3.6 Nilai & Orientasi",
        ]
    )

    with tab1:
        st.subheader("3.1 Ontologi")
        st.markdown(
            """
            * **Definisi & Fungsi:** Ontologi adalah cabang filsafat yang membahas hakikat keberadaan atau realitas untuk menjelaskan objek kajian suatu ilmu[span_1](start_span)[span_1](end_span). Hal ini memberikan batasan yang jelas agar ruang lingkup pembahasan tetap terarah[span_2](start_span)[span_2](end_span).
            * **Objek Kajian:** 
              1. **Objek Material:** Segala sesuatu yang menjadi bahan kajian (benda, manusia, masyarakat, alam, dan peristiwa kehidupan)[span_3](start_span)[span_3](end_span).
              2. **Objek Formal:** Sudut pandang atau cara tertentu yang digunakan untuk mengkaji objek material tersebut (misalnya perbedaan kacamata biologi, psikologi, maupun sosiologi)[span_4](start_span)[span_4](end_span).
            * **Basis Realitas:** Pengetahuan harus dipahami berdasarkan fakta dan keberadaannya secara objektif, bukan sekadar dugaan atau kepercayaan semata, guna menentukan batas metode penelitian yang valid[span_5](start_span)[span_5](end_span).
            """
        )

    with tab2:
        st.subheader("3.2 Epistimologi")
        st.markdown(
            """
            * **Definisi:** Cabang filsafat yang membahas sumber, proses, metode, dan kriteria kebenaran pengetahuan (bagaimana manusia memperoleh serta membuktikan kebenaran suatu pengetahuan)[span_6](start_span)[span_6](end_span).
            * **Metode Ilmiah:** Pengetahuan ilmiah diperoleh melalui tahapan sistematis, logis, objektif, dan dapat diuji ulang (identifikasi masalah, perumusan hipotesis, pengumpulan data, analisis, hingga penarikan kesimpulan)[span_7](start_span)[span_7](end_span).
            * **Kriteria Kebenaran:** Sesuai dengan fakta, dapat diterima secara logis, dan didukung bukti empiris. Sifat kebenaran ilmiah bersifat terbuka dan terus berkembang seiring ditemukannya bukti baru[span_8](start_span)[span_8](end_span).
            """
        )

    with tab3:
        st.subheader("3.3 Aksiologi")
        st.markdown(
            """
            * **Definisi:** Cabang filsafat yang membahas nilai, etika, moral, dan manfaat ilmu pengetahuan (untuk apa ilmu digunakan dan siapa yang memperoleh manfaatnya)[span_9](start_span)[span_9](end_span).
            * **Korelasi Moral & Etika:** Penerapan ilmu harus mempertimbangkan dampak positif bagi kemanusiaan dan lingkungan, serta tidak boleh digunakan untuk penindasan atau perusakan[span_10](start_span)[span_10](end_span).
            * **Nilai Praktis:** Ilmu pengetahuan diharapkan mampu memberikan solusi nyata guna meningkatkan kualitas hidup serta kesejahteraan bersama secara etis[span_11](start_span)[span_11](end_span).
            """
        )

    with tab4:
        st.subheader("3.4 Hubungan Ontologi, Epistimologi, dan Aksiologi")
        st.markdown(
            """
            * **Triadik Landasan Ilmu:** Ketiga landasan ini tidak dapat dipisahkan[span_12](start_span)[span_12](end_span). Ontologi menentukan **apa** yang dikaji, epistemologi menentukan **bagaimana** cara memperolehnya, dan aksiologi menentukan **untuk apa** pengetahuan tersebut digunakan[span_13](start_span)[span_13](end_span).
            * **Sintesis Komprehensif:** Keterpaduan ketiganya mengubah ilmu pengetahuan dari sekadar kumpulan informasi mentah menjadi sistem pengetahuan yang rasional, metodologis, etis, dan bertanggung jawab terhadap peradaban manusia[span_14](start_span)[span_14](end_span).
            """
        )

    with tab5:
        st.subheader("3.5 Tujuan Pendidikan Pesantren")
        st.markdown(
            """
            * **Dimensi Holistik:** Pendidikan pesantren tidak hanya berorientasi pada penguasaan pengetahuan keagamaan, tetapi juga pembentukan karakter, kedisiplinan, akhlak, keikhlasan, dan tanggung jawab sosial santri[span_15](start_span)[span_15](end_span).
            * **Implementasi di Genggong:** Diwujudkan melalui internalisasi nilai **Satlogi Santri** (*Sopan Santun, Ajeg/Istiqamah, Nasehat, Taqwallah, Ridlallah, dan Ikhlas Lillahi Ta'ala*)[span_16](start_span)[span_16](end_span).
            * **Budaya Organisasi Pesantren:** Didukung melalui tradisi metode salaf (*sorogan, bandongan, musyawarah, bahtsul masail*) serta keteladanan dan pembiasaan perilaku keseharian[span_17](start_span)[span_17](end_span).
            * **Adaptasi Kebutuhan Zaman:** Tujuan pendidikan pesantren terus berkembang dinamis dengan memperluas orientasi kelembagaan formal tanpa meninggalkan identitas dasarnya[span_18](start_span)[span_18](end_span).
            """
        )

    with tab6:
        st.subheader("3.6 Nilai dan Orientasi Pendidikan Pesantren")
        st.markdown(
            """
            * **Nilai sebagai Local Genius:** Satlogi Santri berfungsi menjaga prinsip moral, kecakapan spiritual, emosional, dan interpersonal santri sebagai identitas kultural (*local genius*)[span_19](start_span)[span_19](end_span).
            * **Dwi-Orientasi Pendidikan:**
              1. **Mempertahankan Tradisi:** Menjaga kesinambungan kajian kitab kuning, metode salaf, dan hubungan otoritatif kiai-santri[span_20](start_span)[span_20](end_span).
              2. **Mendorong Perubahan:** Menerapkan manajemen modern, pendidikan formal, dan adaptasi teknologi untuk menjawab kebutuhan masyarakat[span_21](start_span)[span_21](end_span).
            * **Karakter Adaptif:** Modernisasi di pesantren tidak dipahami sebagai upaya penggantian tradisi lama, melainkan proses selektif yang berlandaskan pada nilai-nilai fundamental kelembagaan pesantren[span_22](start_span)[span_22](end_span).
            """
        )

# ==========================================
# 2. MENU STUDI KASUS
# ==========================================
elif menu == "⚖️ 2. Studi Kasus":
    st.title("⚖️ Analisis Studi Kasus & Problem Solving Filosofis")
    st.markdown(
        "Kajian kasus akademis untuk melatih ketajaman analisis mahasiswa dalam membedah dimensi ontologis, epistemologis, dan aksiologis di pesantren."
    )
    st.markdown("---")

    with st.expander(
        "📌 Kasus 1: Pergeseran Otoritas Keilmuan di Era Digital (Tinjauan Epistemologi)"
    ):
        st.markdown(
            """
            **Analisis Kasus:**  
            Banyak santri masa kini mengandalkan mesin pencari internet atau AI instan untuk merumuskan hukum fikih ketimbang melewati tradisi *talaqqi* dan *bahtsul masail*. Dari sudut pandang epistemologi, hal ini memicu perdebatan mengenai validitas *sanad* dan metode verifikasi kebenaran teks.  
            **Titik Temu Filosofis:**  
            Digitalisasi dapat mempercepat akses informasi (alat bantu), namun validitas keilmuan tetap menuntut metodologi penalaran yang akurat melalui instrumen ushul fiqh dan bimbingan otoritas guru yang tersanad agar terhindar dari distorsi makna.
            """
        )

    with st.expander(
        "📌 Kasus 2: Dilema Transaksional vs Keikhlasan Nilai (Tinjauan Aksiologi)"
    ):
        st.markdown(
            """
            **Analisis Kasus:**  
            Sistem pendidikan modern menuntut akreditasi, indeks prestasi kumulatif (IPK), dan orientasi kerja yang pragmatis. Di sisi lain, aksiologi pesantren menjunjung tinggi nilai *Ikhlas Lillahi Ta'ala* dan orientasi ukhrawi.  
            **Titik Temu Filosofis:**  
            Pencapaian akademis formal diposisikan bukan sebagai komoditas transaksional semata, melainkan sebagai bentuk manifestasi ikhtiar profesional dan bentuk tanggung jawab pengabdian (*khidmah*) sosial yang bermanfaat luas.
            """
        )

# ==========================================
# 3. MENU KUIS INTERAKTIF (Tingkat Mahasiswa)
# ==========================================
elif menu == "🎯 3. Kuis Interaktif (Mahasiswa)":
    st.title("🎯 Uji Pemahaman Filsafat Ilmu & Pendidikan Pesantren")
    st.markdown(
        "Evaluasi berbasis analitis tingkat perguruan tinggi untuk menguji pemahaman terhadap keterkaitan landasan filsafat ilmu dan budaya pesantren Genggong."
    )
    st.markdown("---")

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    with st.form("quiz_form"):
        # Soal 1
        st.markdown(
            "### Soal 1: Ontologi & Objek Kajian (Landasan Filsafat Ilmu)"
        )
        q1 = st.radio(
            "Dalam kerangka ontologi ilmu pengetahuan, apa fungsi utama dari pembedaan antara objek material dan objek formal?",
            (
                "A. Menentukan besar kecilnya anggaran biaya penelitian ilmiah",
                "B. Memberikan batasan ruang lingkup yang jelas dan sudut pandang spesifik agar kajian ilmu terarah[span_23](start_span)[span_23](end_span)",
                "C. Menghilangkan seluruh perbedaan pandangan antar disiplin ilmu sosial",
                "D. Memastikan bahwa seluruh ilmu memiliki metode pengujian yang seragam",
            ),
            key="q1",
        )

        st.markdown("---")

        # Soal 2
        st.markdown("### Soal 2: Epistemologi & Metode Validasi")
        q2 = st.radio(
            "Mengapa metode ilmiah dan kriteria kebenaran dalam epistemologi bersifat terbuka serta dapat diperbaiki (*falsifiable* / berkembang)?",
            (
                "A. Karena kebenaran ilmiah tidak memiliki dasar argumen yang pasti",
                "B. Karena ilmu pengetahuan berkembang seiring ditemukannya bukti empiris dan hasil penelitian baru[span_24](start_span)[span_24](end_span)",
                "C. Karena setiap peneliti bebas mengubah hukum alam sesuai subjektivitasnya",
                "D. Karena tradisi lama harus selalu dihapus secara total",
            ),
            key="q2",
        )

        st.markdown("---")

        # Soal 3
        st.markdown("### Soal 3: Aksiologi & Tanggung Jawab Moral")
        q3 = st.radio(
            "Bagaimana kedudukan aksiologi dalam membatasi penerapan perkembangan sains dan teknologi modern?",
            (
                "A. Aksiologi mengharuskan ilmuwan fokus pada aspek teknis tanpa memedulikan etika",
                "B. Aksiologi berfungsi mengarahkan penggunaan ilmu agar berlandaskan nilai moral, etika, serta kesejahteraan kemanusiaan[span_25](start_span)[span_25](end_span)",
                "C. Aksiologi membatasi penemuan ilmiah agar tidak boleh mendatangkan keuntungan ekonomi",
                "D. Aksiologi hanya diterapkan pada rumpun ilmu agama semata",
            ),
            key="q3",
        )

        st.markdown("---")

        # Soal 4
        st.markdown("### Soal 4: Tujuan & Budaya Organisasi Pesantren")
        q4 = st.radio(
            "Berdasarkan kajian budaya organisasi pesantren di Genggong, apa peran utama dari penerapan nilai 'Satlogi Santri'?",
            (
                "A. Sebagai instrumen administratif untuk mengontrol kehadiran harian santri",
                "B. Sebagai local genius dan pedoman pembentukan karakter holistik (intelektual, moral, dan spiritual) santri[span_26](start_span)[span_26](end_span)",
                "C. Sebagai kurikulum pengganti seluruh kitab kuning salaf",
                "D. Sebagai standar baku penilaian akreditasi sekolah formal semata",
            ),
            key="q4",
        )

        st.markdown("---")

        # Soal 5
        st.markdown("### Soal 5: Orientasi Pendidikan & Modernisasi")
        q5 = st.radio(
            "Bagaimana pola orientasi pendidikan Pesantren Genggong dalam menghadapi arus modernisasi dan perubahan sosial?",
            (
                "A. Menolak seluruh unsur perubahan modern demi menjaga keaslian masa lalu",
                "B. Mengganti total tradisi salaf dengan sistem pendidikan sekuler modern",
                "C. Mengambil posisi dwi-orientasi: mempertahankan tradisi luhur yang baik sambil mengadopsi sistem modern yang maslahat (*adaptif*)[span_27](start_span)[span_27](end_span)",
                "D. Bersikap pasif dan menyerahkan seluruh arah kebijakan kepada dinamika pasar bebas",
            ),
            key="q5",
        )

        st.markdown("")
        submit_btn = st.form_submit_button("Evaluasi Jawaban Kuis")

    if submit_btn:
        score = 0
        total = 5

        # Kunci Jawaban
        c1 = "B. Memberikan batasan ruang lingkup yang jelas dan sudut pandang spesifik agar kajian ilmu terarah[span_28](start_span)[span_28](end_span)"
        c2 = "B. Karena ilmu pengetahuan berkembang seiring ditemukannya bukti empiris dan hasil penelitian baru[span_29](start_span)[span_29](end_span)"
        c3 = "B. Aksiologi berfungsi mengarahkan penggunaan ilmu agar berlandaskan nilai moral, etika, serta kesejahteraan kemanusiaan[span_30](start_span)[span_30](end_span)"
        c4 = "B. Sebagai local genius dan pedoman pembentukan karakter holistik (intelektual, moral, dan spiritual) santri[span_31](start_span)[span_31](end_span)"
        c5 = "C. Mengambil posisi dwi-orientasi: mempertahankan tradisi luhur yang baik sambil mengadopsi sistem modern yang maslahat (*adaptif*)[span_32](start_span)[span_32](end_span)"

        results = []

        if q1 == c1:
            score += 1
            results.append(
                (
                    True,
                    "Soal 1 Benar: Ontologi memetakan objek material dan formal agar batasan keilmuan menjadi jelas dan terarah[span_33](start_span)[span_33](end_span).",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 1 Salah: Objek material dan formal berfungsi memberikan batasan serta sudut pandang spesifik kajian ilmiah[span_34](start_span)[span_34](end_span).",
                )
            )

        if q2 == c2:
            score += 1
            results.append(
                (
                    True,
                    "Soal 2 Benar: Epistemologi memandang kebenaran ilmiah bersifat terbuka dan berkembang sesuai temuan bukti baru[span_35](start_span)[span_35](end_span).",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 2 Salah: Kebenaran ilmiah berkembang dinamis seiring hasil pembuktian dan penelitian baru[span_36](start_span)[span_36](end_span).",
                )
            )

        if q3 == c3:
            score += 1
            results.append(
                (
                    True,
                    "Soal 3 Benar: Aksiologi menuntut pemanfaatan ilmu senantiasa berpijak pada koridor moral, etika, dan kemaslahatan[span_37](start_span)[span_37](end_span).",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 3 Salah: Aksiologi mengarahkan pemanfaatan ilmu agar berlandaskan etika dan tanggung jawab kemanusiaan[span_38](start_span)[span_38](end_span).",
                )
            )

        if q4 == c4:
            score += 1
            results.append(
                (
                    True,
                    "Soal 4 Benar: Satlogi Santri bertindak sebagai local genius penguat karakter moral dan spiritual santri[span_39](start_span)[span_39](end_span).",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 4 Salah: Satlogi Santri merupakan local genius penyeimbang kecakapan spiritual dan moral santri[span_40](start_span)[span_40](end_span).",
                )
            )

        if q5 == c5:
            score += 1
            results.append(
                (
                    True,
                    "Soal 5 Benar: Pesantren menerapkan pola adaptif (dwi-orientasi) antara merawat tradisi lama dan mengambil inovasi maslahat[span_41](start_span)[span_41](end_span).",
                )
            )
        else:
            results.append(
                (
                    False,
                    "Soal 5 Salah: Pesantren memiliki orientasi adaptif dengan memelihara tradisi sekaligus mengadopsi sistem modern yang maslahat[span_42](start_span)[span_42](end_span).",
                )
            )

        st.markdown("---")
        st.subheader(
            f"Hasil Evaluasi Anda: Skor {score} dari {total} ({score*20}%)"
        )

        if score == 5:
            st.balloons()
            st.success(
                "Sempurna! Anda menguasai analisis komprehensif filsafat ilmu dan orientasi pendidikan pesantren dengan sangat baik."
            )
        elif score >= 3:
            st.success(
                "Bagus! Pemahaman konseptual Anda sudah matang sebagai mahasiswa. Tinjau kembali materi yang masih keliru."
            )
        else:
            st.error(
                "Mari tingkatkan pemahaman dengan membaca ulang sub-bab materi pada tab menu utama."
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
    "<p style='text-align: center; font-size: 0.8em; color: #74c69d;'>© 2026 • Kajian Jurnal Filsafat Pesantren Genggong</p>",
    unsafe_allow_html=True,
)
