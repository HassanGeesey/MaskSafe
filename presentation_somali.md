# IndabaX Somalia 2025: Soo bandhigidda Mashruuca - MaskSafe

## Dulmarka Mashruuca: MaskSafe
**Cinwaanka:** MaskSafe  
**Xubnaha Kooxda:** [Hassan Geesey, Abdullahi Ibrahim, Mohamed Ahmed, Camir Abbas, Abdisalan Jaka]  
**Ujeedada:** In la xoojiyo bedqabka caafimaadka dadweynaha iyadoo la isticmaalayo hab otomaatig ah oo lagu kormeelayo xirashada af-xirka (Face Mask).

---

## 1. Dhibaatada Jirta (Problem Statement)
Inkastoo laga soo kabsaday saameyntii COVID-19, haddana ilaalinta caafimaadka hab-dhiska neefsashada waxay weli muhiim u tahay isbitaallada, garoomada diyaaradaha, iyo meelaha dadku ku badan yahay.
*   **Caqabadaha Ilaalinta Buugga ah (Manual Enforcement):** In dad loo shaqaaleeyo ilaalinta af-xirka waa hawl adag, qaali ah, waxayna kordhin kartaa halista qaadista cudurka.
*   **Khaladaadka Bina-aadamka (Human Error):** Ilaalinta joogtada ah waxay keentaa daal, taas oo horseedi karta in la arki waayo dadka aan af-xirka si sax ah u xiran ama aan gabi ahaanba xiran.
*   **Xog Yaraanta (Data Scarcity):** Maamuladu ma haystaan xog dhab ah oo ku saabsan inta qof ee u hoggaansanta bedqabka si go'aanno sax ah loogu gaaro.

---

## 2. Yoolasha Horumarka Waara ee Bartilmaameedka ah (Targeted SDGs)
Mashruucani wuxuu waafaqsan yahay laba yool oo caalami ah:
*   **SDG 3: Caafimaad iyo Ladnaan:** Waxaan ka hortageynaa faafitaanka cudurada neefsashada iyadoo la isticmaalayo kormeer otomaatig ah.
*   **SDG 9: Warshadaha, Hal-abuurka iyo Kaabayaasha:** Isticmaalka tiknoolajiyada casriga ah ee AI (Computer Vision) si loo dhiso kaabayaal caafimaad oo caqli badan.

---

## 3. Xalka la soo Jeediyay (Proposed Solution)
**Qaabka Shaqada:**
Waxaan dhisnay **MaskSafe**, oo ah barnaamij isticmaalaya **Computer Vision** kaas oo aqoonsan kara saddex xaaladood:
1.  **Mask:** Xirashada af-xirka ee saxda ah.
2.  **Improperly Masked:** Af-xirka oo la xirtay balse aan daboolin sankii ama afkii.
3.  **No Mask:** Qofka oo aan gabi ahaanba xiran af-xir.

**AI/ML Methodology:**
*   **Architecture:** Waxaan isticmaalnay moodelka **YOLOv3 (You Only Look Once)** oo leh **Darknet-53 backbone** si loo helo isku-dheelitir u dhexeeya xawaaraha iyo saxsanaanta (precision).
*   **Performance:** Waxaan gaarnay **94.04% mAP (mean Average Precision)**.
*   **Real-time Optimization:** Nidaamku wuxuu si toos ah u falanqeynayaa **Live Video Streams** si uu jawaab degdeg ah uga bixiyo meelaha dadku ku badan yahay.

---

## 4. Agabka Farsamo ee la Isticmaalay (Technology Stack)
Mashruucan waxaa lagu dhisay agab furan (open-source) oo casri ah:
*   **Backend:** Python 3.7+, Flask (loogu talagalay server-ka iyo routing-ka).
*   **Computer Vision:** OpenCV (oo loo isticmaalay qabashada iyo falanqaynta sawirada/video-ga).
*   **Deep Learning Framework:** Darknet / YOLOv3 (inference-ka aqoonsiga mask-ga).
*   **Frontend:** HTML5, CSS3 (Glassmorphism design), iyo JavaScript.
*   **Data Handling:** NumPy (oo loo isticmaalay xisaabaadka matrix-ka ee sawirada).

---

## 5. Saameynta la Filayo (Expected Impact)
**Xaaladda Soomaaliya iyo meelo kaleba:**
*   **Bedqabka Hey'adaha:** Maadaama Soomaaliya ay ku jirto dib-u-dhiska nidaamka caafimaadka, MaskSafe waa qalab raqiis ah oo waxtar weyn u leh isbitaallada iyo xafiisyada dowladda.
*   **Hufnaanta Shaqada:** Habka otomaatigga ah wuxuu u oggolaanayaa ilaalada iyo shaqaalaha caafimaadka inay xoogga saaraan hawlo kale oo muhiim ah.
*   **Wacyigelinta Shacabka:** Aragtida tooska ah ee shaashadda ku tusaysa "Mask" ama "No Mask" waxay xasuusin u tahay dadweynaha si ay u ilaaliyaan fogaanshaha iyo bedqabka.
*   **Go'aan qaadasho ku salaysan Xog:** **Metrics Dashboard** wuxuu maamulka siinayaa tirokoob cad (F1-Score, AP) si loo xaqiijiyo waxtarka nidaamka ka hor intaanan la hirgelin.

---

## Arrimaha Guusha Keenay (Key Success Factors)
*   **Originality:** Moodelka YOLOv3 oo aan si gaar ah ugu tababarnay inuu aqoonsado xirashada khaldan (improper usage).
*   **Citations:** Waxaan isticmaalnay Face Mask Detection YOLO dataset iyo algorithm-ka YOLOv3 ee ay dhisneen Joseph Redmon & Ali Farhadi.
*   **Focus:** Waxaa loogu talagalay inuu ku shaqeeyo kombuyuutarada caadiga ah (Standard CPUs), taas oo ka dhigaysa mid ku habboon deegaanka Soomaaliya.

---

## Diyaarinta Live Demo
*   [ ] Muuji **Live Camera Feed** (Aqoonsiga tooska ah).
*   [ ] Tus sida loo upload gareeyo sawirka (**Image Upload**) laguna falanqaynayo.
*   [ ] Sharax **Metrics Dashboard** iyo waxa loola jeedo mAP marka ay timaado AI.
