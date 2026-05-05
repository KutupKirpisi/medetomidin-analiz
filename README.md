# Kedilerde İntranasal Medetomidin – Sedasyon Analiz Sistemi

**Windows EXE** otomatik olarak GitHub Actions ile derlenir.

## ⬇️ EXE İndirme

1. Sağ taraftaki **Actions** sekmesine tıklayın
2. En üstteki **"Windows EXE Derle"** iş akışını açın
3. **Artifacts** bölümünden `MedetomidinAnalizSistemi-Windows-EXE` indirin
4. ZIP'i açın → `MedetomidinAnalizSistemi.exe` çift tıkla çalışır

---

## 📊 Özellikler

- 4 Grup: MED-AT-U / MED-AT-B / MED-DAM-U / MED-DAM-B
- Shapiro–Wilk + Levene normallik ve varyans testleri
- One-Way ANOVA + Tukey HSD post-hoc
- Kruskal–Wallis + Dunn post-hoc (Bonferroni)
- İki Yönlü Tekrarlı Ölçümler ANOVA (Grup × Zaman)
- Friedman Testi
- Ki-kare / Fisher Exact testi
- Monitörizasyon: HR, SpO₂, RT, fR, MAP, SAP, DAP (T0–T60)
- Sedasyon Skorlama (0–15)
- JSON veri kaydet/yükle, CSV dışa aktar
