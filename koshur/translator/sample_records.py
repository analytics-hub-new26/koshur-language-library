"""
Authentic Sample Records for J&K Government Revenue & Archival Translation:
Curated primary-source records representing official Patwari registers,
deeds of conveyance (Bainama), mortgages (Rahannama), mutations (Intiqal),
and revenue court proceedings in classical Nastaliq/Shikasta phrasing.
"""

from typing import Dict, Any, List

SAMPLE_RECORDS: Dict[str, Dict[str, Any]] = {
    "jamabandi_shalimar": {
        "id": "jamabandi_shalimar",
        "title": "Jamabandi (Record of Rights) - Mauza Shalimar, Srinagar",
        "doc_type": "jamabandi",
        "date_fasli": "1342 Fasli",
        "date_gregorian": "1935 A.D.",
        "district": "Srinagar",
        "tehsil": "Srinagar",
        "village": "Shalimar",
        "urdu_text": """نقل جمع بندی چہار سالہ موضع شالیمار، تحصیل و ضلع سرینگر۔
سالِ بندوبست: سنہ ۱۳۴۲ فصلی مطابق ۱۹۳۵ء۔
کھیوٹ نمبر: ۱۴
کھتونی نمبر: ۲۸
پٹی / محل: ہارون

نام مالک معہ سکونت و قومیت:
غلام رسول ولد عبدالستار، قوم بٹ، ساکن شالیمار (حصہ برابر ۲/۳)
علی محمد ولد عبدالستار، ساکن شالیمار (حصہ ۱/۳) — مالک اعلیٰ

نام کاشتکار معہ احوال و قبضہ:
عبدالرحیم ولد قاسم ڈار، ساکن شالیمار — دخلکار موروثی (کاشت بذریعہ خود)

کیفیت اراضی و خسرہ نمبرات:
خسرہ نمبر ۴۱۲: رقبہ ۳ کنال ۸ مرلہ — آبی اول (باغ سیب)
خسرہ نمبر ۴۱۳: رقبہ ۲ کنال ۴ مرلہ — آبی دوئم (شالی زار)
میزان کل رقبہ: ۵ کنال ۱۲ مرلہ (مساوی ۱۱۲ مرلہ)

شرح لگان و مالگزاری:
مالگزاری سرکار: بارہ روپیہ چار آنہ سالانہ (۱۲ روپیہ ۴ آنہ)
مطالبہ آبانہ: تین روپیہ آٹھ آنہ
شرح حق مالکانہ: دو آنہ فی روپیہ

کیفیت و دستخط:
پڑتال گرداور بمقام شالیمار بتاریخ ۱۵ ماہ اسوج ۱۳۴۲ فصلی۔
دستخط پٹواری حلقہ بقلم خود۔
تصدیق نقل مطابق اصل: نائب تحصیلدار سرینگر。""".strip(),
        "notes": "Classic quadrennial Jamabandi record with dual ownership shares, occupancy tenancy, and irrigation categories."
    },

    "bainama_pampore": {
        "id": "bainama_pampore",
        "title": "Bainama (Absolute Sale Deed) - Mauza Pampore, Pulwama",
        "doc_type": "bainama",
        "date_fasli": "1338 Fasli",
        "date_gregorian": "1931 A.D.",
        "district": "Pulwama",
        "tehsil": "Pampore",
        "village": "Pampore",
        "urdu_text": """العبد
منکہ اسداللہ ولد نورالدین قوم میر ساکن قصبہ پامپور، تحصیل پامپور۔

اقرار می نماید و می نویسد کہ یک قطعہ اراضی زرعی منجملہ خسرہ نمبر ۵۶۸، واقع موضع پامپور، جس کا رقبہ ۲ کنال ۸ مرلہ (دو کنال آٹھ مرلہ) زعفران زمین (کریوہ) معہ جملہ حقوق داخلی و خارجی، حق آبپاشی، حقوق شجر و اشجار موروثی و ملکیتی خود بحق خریدار محمد سلطان ولد احمد شاہ قوم وانی ساکن پامپور، بعوض مبلغ ۵۰۰ روپیہ سکہ رائج الوقت (پانچ سو روپیہ) فروخت قطعی (بیع قطعی) کر دی ہے۔

اور کل زرِ بیع مبلغ ۵۰۰ روپیہ روبروئے گواہان نقد وصول پا کر اراضی مذکورہ سے اپنا قبضہ و دخل کلاً اٹھا کر قبضہ خریدار کو بدستِ خود دلوا دیا ہے۔ اب اراضی متذکرہ پر خریدار موصوف بدستور مالک و قابض ہو کر مثل دیگر مالکان اپنے نام انتقالِ بیع درج کروانے کا مجاز ہے۔

اراضی کے چہار طرفہ حدودِ اربعہ حسبِ ذیل ہیں:
شرقاً: زمین غلام محی الدین خسرہ نمبر ۵۶۷
غرباً: سڑک عام بجانب پانپور تا اونتی پورہ
شمالاً: باغ بادام خسرہ نمبر ۵۶۹
جنوباً: نالہ آبپاشی سرکاری

المرقوم ۱۵ ماہ وساکھ سنہ ۱۳۳۸ فصلی۔
دستخط بائع: اسداللہ میر (بقلم خود)
دستخط خریدار: محمد سلطان وانی
گواہ شد: عبدالخالق ولد رحمان ڈار ساکن پامپور
گواہ شد: پیارے لال ولد مدھوسودن ساکن پامپور
فقط""".strip(),
        "notes": "Classic Shikasta sale deed featuring Al-Abd formula, boundaries, consideration, and witness slots."
    },

    "intiqal_virasat": {
        "id": "intiqal_virasat",
        "title": "Intiqal (Order of Inheritance Mutation) - Mauza Mattan, Anantnag",
        "doc_type": "intiqal",
        "date_fasli": "1350 Fasli",
        "date_gregorian": "1943 A.D.",
        "district": "Anantnag",
        "tehsil": "Anantnag",
        "village": "Mattan",
        "urdu_text": """رجسٹر انتقال اراضی، موضع مٹن، تحصیل اننت ناگ۔
انتقال نمبر: ۱۸۹
نوعیت انتقال: وراثت (انتقالِ فوتیدگی)

مقدمہ فوتیدگی:
متوفی محمد سبحان ولد قادر لون ساکن مٹن بتاریخ ۱۰ ماہ ماگھ سنہ ۱۳۴۹ فصلی فوت ہو گیا۔
متوفی مذکور خسرہ نمبر ۱۲۴، ۱۲۵، ۱۲۶ واقع موضع مٹن میں کل رقبہ ۸ کنال ۱۶ مرلہ پر بحیثیت مالکِ کامل قابض تھا۔

شجرہ نسب وارثانِ قانونی:
متوفی محمد سبحان
├── بیٹا: عبدالغنی لون (حصہ ۱/۲)
├── بیٹا: منظور احمد لون (حصہ ۱/۴)
└── بیوہ: مسماۃ فاطمہ بیگم (حصہ ۱/۴)

رپورٹ پٹواری حلقہ:
فوتیدگی مسلۂ حقیقت میں درج کی گئی۔ متوفی کے علاوہ کوئی دیگر وارث موجود نہیں۔ وارثان مذکوران کا قبضہ موقع پر تصدیق شدہ ہے۔

حکم نائب تحصیلدار اننت ناگ:
آج اجلاس عام میں بمقام مٹن روبروئے معززینِ دیہہ و نمبردار تصدیق ہوئی۔ وارثانِ مذکوران کا نام بجائے متوفی محمد سبحان بموجب حصصِ قانونی درجِ جمع بندی کرنے کا حکم صادر فرمایا گیا۔
دستخط: نائب تحصیلدار اننت ناگ۔
فقط۔""".strip(),
        "notes": "Inheritance mutation order recording legal heirs, genealogical tree, and judicial attestation."
    },

    "rahannama_baramulla": {
        "id": "rahannama_baramulla",
        "title": "Rahannama (Mortgage Deed with Possession) - Mauza Sopore, Baramulla",
        "doc_type": "rahannama",
        "date_fasli": "1346 Fasli",
        "date_gregorian": "1939 A.D.",
        "district": "Baramulla",
        "tehsil": "Sopore",
        "village": "Sopore",
        "urdu_text": """العبد
منکہ خضر محمد ولد علی زرگر ساکن قصبہ سوپور، تحصیل سوپور۔

اقرار می نماید کہ اراضی زرعی خسرہ نمبر ۳۴۰، رقبہ ۴ کنال ۰ مرلہ (چار کنال) قسم خشکی واقع موضع سوپور بحق مرتہن بشیر احمد ولد جلال الدین تاجر ساکن سوپور بعوض قرضہ مبلغ ۳۵۰ روپیہ سکہ رائج الوقت (تین سو پچاس روپیہ) بطور رہن با قبضہ (رہن بالقبض) کر دی ہے۔

شرائط رہن حسبِ ذیل ہیں:
اولاً: قبضہ اراضی مذکورہ مرتہن کو دیا گیا ہے اور منافع اراضی بجائے سودِ قرضہ شمار ہوگا۔
ثانیاً: میعاد رہن پانچ سال مقرر ہے۔ بعد اختتامِ میعاد جب بھی راہن اصل رقم مبلغ ۳۵۰ روپیہ یکمشت ادا کرے گا، اراضی فک الرہن (واگزار) کر دی جائے گی۔
ثالثاً: راہن کو دورانِ میعاد رہن کسی دیگر شخص کو فروخت کرنے کا مجاز نہ ہوگا۔

تاریخ تحریر: ۵ ماہ جیٹھ سنہ ۱۳۴۶ فصلی۔
دستخط راہن: خضر محمد زرگر
دستخط مرتہن: بشیر احمد
گواہ شد: غلام قادر ساکن سوپور
گواہ شد: عبدالرحیم ساکن سوپور
فقط""".strip(),
        "notes": "Mortgage deed with usufruct (Rehn ba-Qabza) specifying loan amount, interest waiver, and redemption."
    },

    "arzi_dawa_anantnag": {
        "id": "arzi_dawa_anantnag",
        "title": "Arzi Dawa Lagan (Plaint for Arrears of Rent) - Revenue Court",
        "doc_type": "arzi_dawa_lagan",
        "date_fasli": "1348 Fasli",
        "date_gregorian": "1941 A.D.",
        "district": "Anantnag",
        "tehsil": "Kulgam",
        "village": "Kulgam",
        "urdu_text": """بخدمت جناب اسسٹنٹ کلکٹر درجہ اول (تحصیلدار صاحب بہادر) کولگام۔

عرضی دعویٰ بابت وصولیابی بقایا لگانِ اراضی زرعی۔
مدعی: غلام حسن ولد کریم خان زمیندار ساکن کولگام
بنام
مدعا علیہ: غلام محی الدین ولد عبداللہ مزارع (غیر دخلکار) ساکن کولگام

بیان دعویٰ:
۱۔ یہ کہ مدعی اراضی خسرہ نمبر ۷۸۹ رقبہ ۳ کنال ۶ مرلہ واقع موضع کولگام کا مالک و قابض ہے۔
۲۔ یہ کہ مدعا علیہ اراضی مذکورہ پر بطور غیر دخلکار کاشتکار سال ہائے فصلی ۱۳۴۶ و ۱۳۴۷ میں کاشت کرتا رہا۔
۳۔ یہ کہ مدعا علیہ کے ذمہ بقایا لگان بموجب بٹائی نصفی مبلغ ۴۸ روپیہ واجب الادا ہے۔
۴۔ یہ کہ مکرر تقاضا کے باوجود مدعا علیہ نے بقایا لگان ادا کرنے سے عذر و انکار کیا ہے۔

استدعا:
لہٰذا مدعی دست بدعا ہے کہ ڈگری مبلغ ۴۸ روپیہ معہ خرچہ عدالت بحق مدعی و بر خلاف مدعا علیہ صادر فرمائی جاوے۔
عرضی کنندہ: غلام حسن (دستخط بقلم خود)
تصدیق: منکہ مدعی بقسم کہتا ہوں کہ جملہ مندرجاتِ عرضی میرے علم و یقین سے درست ہیں۔""".strip(),
        "notes": "Revenue Court plaint claiming rent arrears with cause of action, tenancy status, and verification affidavit."
    }
}

def get_sample_record(sample_id: str) -> Dict[str, Any]:
    return SAMPLE_RECORDS.get(sample_id, {})

def list_sample_records() -> List[Dict[str, str]]:
    return [
        {
            "id": k,
            "title": v["title"],
            "doc_type": v["doc_type"],
            "district": v.get("district", ""),
            "village": v.get("village", ""),
            "date": v.get("date_gregorian", "")
        }
        for k, v in SAMPLE_RECORDS.items()
    ]