import flet as ft

def main(page: ft.Page):
    page.title = "מחשבון ריבית דריבית"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def calculate(e):
        # בדיקה אם שדה קלט ריק
        if not initial_investment.value or not monthly_deposit.value or not interest_rate.value or not years_input.value:
            error_dialog.content = ft.Text("אנא מלא את כל השדות.")
            error_dialog.open = True
            page.update()
            return
        
        try:
            initial = float(initial_investment.value)
            monthly = float(monthly_deposit.value)
            rate = float(interest_rate.value) / 100
            years = float(years_input.value)
            
            if initial < 0 or monthly < 0 or rate < 0 or years < 0:
                raise ValueError("הערכים חייבים להיות חיוביים")
            
            # ריבית חודשית
            monthly_rate = rate / 12
            total_months = int(years * 12)
            
            # חישוב סכום סופי
            final_amount = initial
            for _ in range(total_months):
                final_amount = final_amount * (1 + monthly_rate) + monthly
                
            total_invested = initial + (monthly * total_months)
            interest_earned = final_amount - total_invested
            
            # עדכון התוצאות
            total_invested_label.value = f"סכום מושקע: ₪{total_invested:,.2f}"
            interest_earned_label.value = f"רווחי ריבית: ₪{interest_earned:,.2f}"
            final_amount_label.value = f"סכום סופי: ₪{final_amount:,.2f}"
            page.update()
            
        except ValueError:
            error_dialog.content = ft.Text("אנא הזן מספרים חוקיים וחיוביים.")
            error_dialog.open = True
            page.update()

    def close_dialog(e):
        error_dialog.open = False
        page.update()

    def clear_fields(e):
        initial_investment.value = ""
        monthly_deposit.value = ""
        interest_rate.value = ""
        years_input.value = ""
        total_invested_label.value = "סכום מושקע: ₪0"
        interest_earned_label.value = "רווחי ריבית: ₪0"
        final_amount_label.value = "סכום סופי: ₪0"
        page.update()

    # שדות קלט
    initial_investment = ft.TextField(label="השקעה ראשונית (₪)", width=300, text_align=ft.TextAlign.CENTER)
    monthly_deposit = ft.TextField(label="הפקדה חודשית (₪)", width=300, text_align=ft.TextAlign.CENTER)
    interest_rate = ft.TextField(label="תשואה שנתית (%)", width=300, text_align=ft.TextAlign.CENTER)
    years_input = ft.TextField(label="תקופת ההשקעה (שנים)", width=300, text_align=ft.TextAlign.CENTER)
    
    # כפתור חישוב
    calculate_btn = ft.ElevatedButton(text="חשב", on_click=calculate)
    
    # כפתור ניקוי שדות
    clear_btn = ft.ElevatedButton(text="נקה שדות", on_click=clear_fields)
    
    # תוויות תוצאות
    total_invested_label = ft.Text(value="סכום מושקע: ₪0", text_align=ft.TextAlign.CENTER)
    interest_earned_label = ft.Text(value="רווחי ריבית: ₪0", text_align=ft.TextAlign.CENTER)
    final_amount_label = ft.Text(value="סכום סופי: ₪0", text_align=ft.TextAlign.CENTER)
    
    # דיאלוג שגיאה
    error_dialog = ft.AlertDialog(
        title=ft.Text("שגיאה"),
        actions=[
            ft.TextButton("אישור", on_click=close_dialog)
        ]
    )
    
    # טיפים להשקעה
    investment_tips = ft.Container(
        content=ft.Column(
            [
                ft.Text("טיפים למשקיע המתחיל", size=20, weight="bold", text_align=ft.TextAlign.RIGHT),
                ft.Text("1. גוון את ההשקעות שלך.", text_align=ft.TextAlign.RIGHT),
                ft.Text("2. למד על השוק לפני שאתה משקיע.", text_align=ft.TextAlign.RIGHT),
                ft.Text("3. חשוב לטווח ארוך.", text_align=ft.TextAlign.RIGHT),
                ft.Text("4. הימנע מהשקעות מסוכנות.", text_align=ft.TextAlign.RIGHT),
                ft.Text("5. עקוב אחרי התשואות שלך.", text_align=ft.TextAlign.RIGHT),
                ft.Text("6. עקוב אחרי דמי הניהול שנגבים ממך", text_align=ft.TextAlign.RIGHT)
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        border_radius=10,
        padding=10,
        border=ft.border.all(2, ft.colors.GREY),
        bgcolor=ft.colors.LIGHT_BLUE_100,
        width=300,
    )

    # הוספת רכיבים לעמוד
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        initial_investment,
                        monthly_deposit,
                        interest_rate,
                        years_input,
                        ft.Row([calculate_btn, clear_btn]),
                        total_invested_label,
                        interest_earned_label,
                        final_amount_label,
                        error_dialog,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                investment_tips,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )

ft.app(target=main)
