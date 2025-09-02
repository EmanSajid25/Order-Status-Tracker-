from flask import Flask, render_template, request
import pandas as pd
import re

app = Flask(__name__)

def load_orders(file_path):
    df = pd.read_csv(file_path)
    df['order_id'] = df['order_id'].astype(int)
    df['customer_name'] = df['customer_name'].str.strip().str.lower()
    df['status'] = df['status'].str.strip()
    df['delivery_date'] = df['delivery_date'].str.strip()
    return df

orders_df = load_orders("data_cleaned.csv")

def extract_order_id(user_input):
    match = re.search(r'\b(\d{4,})\b', user_input)
    if match:
        return int(match.group(1))
    return None

def get_order_status_by_id(order_id, df):
    order = df[df['order_id'] == order_id]
    if not order.empty:
        row = order.iloc[0]
        return f"Order {row['order_id']} for {row['customer_name'].title()} is {row['status']}. Estimated delivery: {row['delivery_date']}."
    else:
        return f"❌ No order found with ID {order_id}."

def get_orders_by_customer(name, df):
    name = name.strip().lower()
    orders = df[df['customer_name'] == name]
    if not orders.empty:
        responses = [f"Order {row['order_id']} is {row['status']}. Estimated delivery: {row['delivery_date']}." for _, row in orders.iterrows()]
        return "<br>".join(responses)
    else:
        return f"❌ No orders found for customer '{name.title()}'."

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        order_id = extract_order_id(user_input)
        if order_id:
            response = get_order_status_by_id(order_id, orders_df)
        else:
            words = user_input.split()
            if len(words) >= 2:
                possible_name = " ".join(words[-2:])
                response = get_orders_by_customer(possible_name, orders_df)
            else:
                response = "⚠️ Please enter a valid order ID or full name (e.g., Nate Warren or order 1065)."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

