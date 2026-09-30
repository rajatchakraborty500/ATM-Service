import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="My ATM",
    page_icon="🏦",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #1f4e79;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 18px;
}

.balance-box {
    background-color: #1f4e79;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.balance-label {
    font-size: 18px;
}

.balance-value {
    font-size: 36px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Functions
# -----------------------------

def check_balance(balance):
    return balance


def deposit_money(balance, amount):

    if amount > 0:
        balance += amount
        return balance, True, f"Successfully deposited Rs {amount:.2f}"

    return balance, False, "Invalid deposit amount!"


def withdraw_money(balance, amount):

    if amount <= 0:
        return balance, False, "Invalid withdrawal amount!"

    elif amount > balance:
        return balance, False, "Insufficient balance!"

    else:
        balance -= amount
        return balance, True, f"Successfully withdrawn Rs {amount:.2f}"


# -----------------------------
# Session State
# -----------------------------

if "balance" not in st.session_state:
    st.session_state.balance = 5000.00


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="title">🏦 My ATM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Simple Banking System</div>',
    unsafe_allow_html=True
)

st.write("")


# -----------------------------
# Balance Display
# -----------------------------

st.markdown(
    f"""
    <div class="balance-box">
        <div class="balance-label">Current Balance</div>
        <div class="balance-value">Rs {st.session_state.balance:,.2f}</div>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar Menu
# -----------------------------

st.sidebar.title("🏦 ATM Menu")

choice = st.sidebar.radio(
    "Select an option",
    [
        "Check Balance",
        "Deposit Money",
        "Withdraw Money"
    ]
)


# -----------------------------
# Check Balance
# -----------------------------

if choice == "Check Balance":

    st.header("💰 Check Balance")

    st.success(
        f"Your current balance is Rs {st.session_state.balance:,.2f}"
    )


# -----------------------------
# Deposit Money
# -----------------------------

elif choice == "Deposit Money":

    st.header("➕ Deposit Money")

    amount = st.number_input(
        "Enter amount to deposit",
        min_value=0.0,
        step=100.0
    )

    if st.button("Deposit Money", use_container_width=True):

        new_balance, success, message = deposit_money(
            st.session_state.balance,
            amount
        )

        st.session_state.balance = new_balance

        if success:
            st.success(message)
            st.info(
                f"Available Balance: Rs {st.session_state.balance:,.2f}"
            )
        else:
            st.error(message)


# -----------------------------
# Withdraw Money
# -----------------------------

elif choice == "Withdraw Money":

    st.header("➖ Withdraw Money")

    amount = st.number_input(
        "Enter amount to withdraw",
        min_value=0.0,
        step=100.0
    )

    if st.button("Withdraw Money", use_container_width=True):

        new_balance, success, message = withdraw_money(
            st.session_state.balance,
            amount
        )

        st.session_state.balance = new_balance

        if success:
            st.success(message)
            st.info(
                f"Available Balance: Rs {st.session_state.balance:,.2f}"
            )
        else:
            st.error(message)


# -----------------------------
# Footer
# -----------------------------

st.write("")
st.divider()

st.caption("🔒 My ATM | Simple Python + Streamlit Banking Project")