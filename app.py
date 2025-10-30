import streamlit as st
import datetime
import random

# إعدادات الصفحة
st.set_page_config(
    page_title="برنامج المحادثات",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم
st.markdown("""
<style>
    .main { direction: rtl; }
    .css-1d391kg { padding: 2rem; }
    .user-message { 
        background-color: #000000; 
        padding: 10px; 
        border-radius: 10px; 
        margin: 5px; 
        border: 1px solid #e0e0e0;
    }
    .other-message { 
        background-color: #333333; 
        padding: 10px; 
        border-radius: 10px; 
        margin: 5px; 
        border: 1px solid #e0e0e0;
    }
    .header { 
        text-align: center; 
        color: #2E86AB; 
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# البيانات
if 'conversations' not in st.session_state:
    st.session_state.conversations = {
        "محمد": [
            {"sender": "محمد", "message": "مرحباً، كيف حالك؟", "time": "10:30 ص"},
            {"sender": "ندى", "message": "أهلاً، أنا بخير الحمدلله. وأنت؟", "time": "10:31 ص"},
            {"sender": "محمد", "message": "بخير أيضاً، شكراً لك", "time": "10:32 ص"}
        ],
        "فاطمة": [
            {"sender": "فاطمة", "message": "هل انتهيت من التقرير؟", "time": "09:15 ص"},
            {"sender": "ندى", "message": "نعم، سأرسله لك الآن", "time": "09:20 ص"}
        ],
        "خالد": [
            {"sender": "ندى", "message": "هل نلتقي اليوم؟", "time": "أمس 08:30 م"},
            {"sender": "خالد", "message": "نعم، في المقهى المعتاد", "time": "أمس 08:35 م"}
        ],
        "سارة": [
            {"sender": "سارة", "message": "شكراً على المساعدة", "time": "الجمعة 03:45 م"},
            {"sender": "ندى", "message": "العفو، دائماً في الخدمة", "time": "الجمعة 03:50 م"}
        ],
        "ميس شيماء": [
            {"sender": "ندى", "message": "انا عملت برنامج", "time": "الجمعه 08:28 م"}
            {"sender": "ميس شيماء", "message": "برافو استمري يا ندى", "time": "الجمعه 08:30 ص"}
        ],

if 'current_user' not in st.session_state:
    st.session_state.current_user = {"name": "ندى", "status": "متاح"}

# الشريط الجانبي
with st.sidebar:
    st.markdown('<div class="header"><h1>💬 برنامج المحادثات</h1></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("👤 حسابك")
    st.write(f"**الاسم:** {st.session_state.current_user['name']}")
    
    new_status = st.selectbox("🟢 حالتك:", ["متاح", "مشغول", "غير متاح", "بالخارج"])
    st.session_state.current_user['status'] = new_status
    
    st.markdown("---")
    st.subheader("👥 المستخدمون")
    users = ["محمد", "فاطمة", "خالد", "سارة" ,"ميس شيماء" ,"منه", "زياد"]
    selected_user = st.selectbox("اختر مستخدم للمحادثة:", users)
    
    st.markdown("---")
    st.subheader("📞 المكالمات")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📞 اتصال", use_container_width=True):
            st.success(f"جاري الاتصال بـ {selected_user}...")
    
    with col2:
        if st.button("🎥 فيديو", use_container_width=True):
            st.success(f"جاري بدء مكالمة الفيديو مع {selected_user}...")

    st.markdown("---")
    st.subheader("ℹ️ معلومات")
    st.info("""
    **مميزات التطبيق:**
    ✓ دردشات نصية
    ✓ مكالمات صوتية
    ✓ مكالمات فيديو
    ✓ حالة المستخدم
    ✓ واجهة عربية
    """)

# المنطقة الرئيسية - المحادثة
st.markdown(f'<div class="header"><h2>💭 المحادثة مع {selected_user}</h2></div>', unsafe_allow_html=True)

# عرض الرسائل
if selected_user in st.session_state.conversations:
    for msg in st.session_state.conversations[selected_user]:
        if msg['sender'] == st.session_state.current_user['name']:
            st.markdown(f"""
            <div style='text-align: left; margin: 10px;'>
                <div class='user-message' style='text-align: right;'>
                    <b>أنت</b> ({msg['time']}):<br>
                    {msg['message']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='text-align: right; margin: 10px;'>
                <div class='other-message' style='text-align: left;'>
                    <b>{msg['sender']}</b> ({msg['time']}):<br>
                    {msg['message']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# إرسال رسالة جديدة
st.markdown("---")
st.subheader("✉️ إرسال رسالة جديدة")

col_msg1, col_msg2 = st.columns([3, 1])
with col_msg1:
    new_message = st.text_input("اكتب رسالتك هنا:", placeholder="اكتب رسالتك...")

with col_msg2:
    st.write("")  # مسافة
    st.write("")  # مسافة
    if st.button("🔄 إرسال", use_container_width=True):
        if new_message.strip():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            new_msg = {
                "sender": st.session_state.current_user['name'],
                "message": new_message,
                "time": current_time
            }
            if selected_user in st.session_state.conversations:
                st.session_state.conversations[selected_user].append(new_msg)
            else:
                st.session_state.conversations[selected_user] = [new_msg]
            st.rerun()

# قسم الإحصائيات والمعلومات
st.markdown("---")
col_stat1, col_stat2, col_stat3 = st.columns(3)

with col_stat1:
    st.subheader("📊 الإحصائيات")
    st.metric("المحادثات النشطة", "4")
    st.metric("المكالمات اليوم", "3")
    st.metric("الرسائل المرسلة", "12")

with col_stat2:
    st.subheader("🎯 الحالة الحالية")
    st.info(f"**الحالة:** {st.session_state.current_user['status']}")
    st.info(f"**المستخدم النشط:** {selected_user}")
    st.info(f"**آخر نشاط:** {datetime.datetime.now().strftime('%H:%M')}")

with col_stat3:
    st.subheader("⚙️ الإعدادات السريعة")
    if st.button("🔔 تفعيل الإشعارات", use_container_width=True):
        st.success("تم تفعيل الإشعارات")
    
    if st.button("🌙 الوضع الليلي", use_container_width=True):
        st.success("تم تفعيل الوضع الليلي")
    
    if st.button("🗑️ مسح المحادثة", use_container_width=True):
        if selected_user in st.session_state.conversations:
            st.session_state.conversations[selected_user] = []
            st.rerun()

# تذييل الصفحة
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <h3>برنامج المحادثات - إصدار 1.0</h3>
    <p>تم التطوير باستخدام Streamlit | واجهة عربية كاملة</p>
</div>
""", unsafe_allow_html=True)
